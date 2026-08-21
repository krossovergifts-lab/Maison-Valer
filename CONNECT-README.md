# Maison Valér — Connect the site to the Sanity backend

This makes the live website render from your Sanity backend instead of a hard-coded list.
Your DESIGN does not change — only where product/category data comes from.

## Install (one-time)
Unzip this into your SITE repo root and overwrite when asked:
    C:\Users\Admin\Desktop\Maison-Valer-main
Files:
  - build_site.py            (updated: reads products.json, falls back to demo data if absent)
  - sanity_sync.py           (new: pulls from Sanity + auto-translates -> products.json)
  - js/site.js               (updated: gallery handles Sanity image URLs)
  - images/products/_ph-*.webp  (5 neutral "image coming soon" tiles used until a colour has photos)

You can ignore/delete the old placeholder tiles and IMAGE-MANIFEST.md — no longer needed;
Sanity serves and crops the real images.

## Every time you want the site to reflect the backend
Run these two commands in the repo folder:

    python sanity_sync.py     # fetch backend + translate EN->RU/AR  -> products.json
    python build_site.py      # regenerate the pages + js/i18n.js

Then publish as usual:

    git add .
    git commit -m "sync catalogue from Sanity"
    git push                  # Vercel redeploys

Commit `products.json` and `translations-cache.json` too (the cache means translations
aren't re-fetched every time).

## Notes
- Products with no images yet show a neutral "IMAGE COMING SOON" tile per colour.
  As soon as a colourway gets photos in the Studio (then re-sync), the real images appear.
- Translation is free (MyMemory) and cached. To raise the daily limit, set an email:
      setx MYMEMORY_EMAIL "you@example.com"      (Windows, then reopen the terminal)
  If a translation ever reads wrong, you'll be able to override it later.
- Token: only needed if your Sanity dataset is PRIVATE. Free plan = public = no token.
  If sanity_sync.py returns 401/403 from Sanity, create a Viewer token
  (manage.sanity.io -> API -> Tokens) and set it:
      setx SANITY_TOKEN "your-viewer-token"

## Final step (auto "Publish -> live") — set up with your developer
To make hitting Publish in the Studio rebuild the site automatically:
  1. Vercel -> project Settings -> Git -> Deploy Hooks -> create one -> copy its URL.
  2. Make Vercel run the build: set the Build Command to
         pip install pillow >/dev/null 2>&1; python sanity_sync.py && python build_site.py
     (or run the two scripts in a GitHub Action).
  3. Sanity -> manage.sanity.io -> API -> Webhooks -> add -> paste the Vercel Deploy Hook URL,
     trigger on create/update/delete of `product` and `category`.
Now: Publish in the backend -> Sanity pings Vercel -> site rebuilds in ~1-2 min.
