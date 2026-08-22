# -*- coding: utf-8 -*-
"""
Maison Valér — pull catalogue from Sanity and write products.json for build_site.py.

- Reads PUBLISHED products + categories from your Sanity backend.
- Auto-translates English -> Russian + Arabic (free MyMemory API, cached).
- Writes products.json next to build_site.py.

Run on your machine (needs internet):
    python sanity_sync.py
Then:
    python build_site.py

No paid keys required. Uses only the Python standard library.
Optional environment variables:
    SANITY_TOKEN     read token, only needed if your dataset is PRIVATE
    MYMEMORY_EMAIL   your email -> raises the free translation daily limit
"""
import os, json, time, urllib.parse, urllib.request

PROJECT_ID = "epxj3lh6"
DATASET    = "production"
API_VER    = "v2021-10-21"
IMG_PARAMS = "?w=1200&h=1200&fit=crop&auto=format"     # square, optimised
CACHE_FILE = "translations-cache.json"

GROQ = """{
  "categories": *[_type=="category"]|order(order asc){"value": value.current, title, order},
  "products": *[_type=="product"]|order(order asc){
    _id, name, sub, desc, sku, archetype, badge, order, sections,
    "cats": categories[]->value.current,
    "colors": colors[]{colorKey, "imgs": images[].asset->url},
    d2dRole, d2dBestFor, d2dCarries, "d2dImg": d2dImage.asset->url
  },
  "siteImages": *[_type=="siteImages"][0]{
    "heroImage": heroImage.asset->url,
    "homeFeature": homeFeature.asset->url,
    "homeImage1": homeImage1.asset->url,
    "homeImage2": homeImage2.asset->url,
    "aboutImage1": aboutImage1.asset->url,
    "aboutImage2": aboutImage2.asset->url,
    "extras": extraImages[]{key, "url": image.asset->url}
  }
}"""

# ---------------------------------------------------------------- fetch
def fetch():
    url = (f"https://{PROJECT_ID}.api.sanity.io/{API_VER}/data/query/{DATASET}"
           f"?query={urllib.parse.quote(GROQ)}")
    req = urllib.request.Request(url)
    token = os.environ.get("SANITY_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["result"]

# ---------------------------------------------------------------- translate
_cache = {}
def _load_cache():
    global _cache
    if os.path.exists(CACHE_FILE):
        try: _cache = json.load(open(CACHE_FILE, encoding="utf-8"))
        except Exception: _cache = {}
def _save_cache():
    json.dump(_cache, open(CACHE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def translate(text, lang):
    """EN -> lang via MyMemory (free). Cached. Falls back to English on any failure."""
    text = (text or "").strip()
    if not text or lang == "en":
        return text
    ck = f"{lang}:{text}"
    if ck in _cache:
        return _cache[ck]
    try:
        q = urllib.parse.quote(text)
        url = f"https://api.mymemory.translated.net/get?q={q}&langpair=en|{lang}"
        email = os.environ.get("MYMEMORY_EMAIL")
        if email:
            url += "&de=" + urllib.parse.quote(email)
        with urllib.request.urlopen(url, timeout=20) as r:
            data = json.load(r)
        out = (data.get("responseData") or {}).get("translatedText") or ""
        # MyMemory sometimes returns an ALL-CAPS quota warning instead of a translation
        if not out or "MYMEMORY WARNING" in out.upper() or "QUERY LENGTH LIMIT" in out.upper():
            out = text
        _cache[ck] = out
        time.sleep(0.4)  # be polite to the free endpoint
        return out
    except Exception as e:
        print(f"  ! translate failed ({lang}) for {text[:40]!r}: {e} — keeping English")
        return text

def tri(text):
    return {"en": text or "", "ru": translate(text, "ru"), "ar": translate(text, "ar")}

# ---------------------------------------------------------------- build
def main():
    print("Fetching catalogue from Sanity…")
    res = fetch()
    cats_in = res.get("categories") or []
    prods_in = res.get("products") or []
    print(f"  {len(prods_in)} products, {len(cats_in)} categories")
    if not prods_in:
        print("No published products found. Publish at least one product, then re-run.")
        return

    _load_cache()
    print("Translating EN -> RU / AR (cached; only new text is fetched)…")

    categories = [{"value": c.get("value"), "title": tri(c.get("title")), "order": c.get("order", 100)}
                  for c in cats_in if c.get("value")]

    products = []
    for p in prods_in:
        colors = []
        for cw in (p.get("colors") or []):
            ck = cw.get("colorKey")
            if not ck:
                continue
            imgs = [(u + IMG_PARAMS) for u in (cw.get("imgs") or []) if u]
            colors.append({"colorKey": ck, "imgs": imgs})
        d = {
            "sku": p.get("sku", ""),
            "order": p.get("order", 100),
            "sections": p.get("sections") or ["collection"],
            "cats": [c for c in (p.get("cats") or []) if c],
            "name": tri(p.get("name")),
            "sub": tri(p.get("sub")),
            "desc": tri(p.get("desc")),
            "archetype": tri(p.get("archetype")),
            "badge": tri(p.get("badge")) if (p.get("badge") or "").strip() else {"en": "", "ru": "", "ar": ""},
            "colors": colors,
        }
        if p.get("d2dImg"):
            d["d2dImg"] = p["d2dImg"] + IMG_PARAMS
        if (p.get("d2dRole") or p.get("d2dBestFor") or p.get("d2dCarries")):
            d["d2dRole"] = tri(p.get("d2dRole") or p.get("sub"))
            d["d2dBestFor"] = tri(p.get("d2dBestFor"))
            d["d2dCarries"] = tri(p.get("d2dCarries"))
        products.append(d)

    _save_cache()
    # editorial site images (banners / section images / future page images)
    EDIT_PARAMS = "?w=1800&auto=format"      # preserve aspect (no square crop) for editorial art
    si_in = res.get("siteImages") or {}
    site_images = {}
    for slot in ("heroImage", "homeFeature", "homeImage1", "homeImage2", "aboutImage1", "aboutImage2"):
        u = si_in.get(slot)
        if u:
            site_images[slot] = u + EDIT_PARAMS
    for ex in (si_in.get("extras") or []):
        if ex.get("key") and ex.get("url"):
            site_images[ex["key"]] = ex["url"] + EDIT_PARAMS

    json.dump({"categories": categories, "products": products, "siteImages": site_images},
              open("products.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Wrote products.json  ({len(products)} products, {len(categories)} categories, {len(site_images)} site images).")
    print("Now run:  python build_site.py")

if __name__ == "__main__":
    main()
