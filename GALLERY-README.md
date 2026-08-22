# Maison Valér — gallery fix (e-commerce style)

Fixes the "thumbnail hover changes image" bug and standardises the gallery.

What changed:
- REMOVED the hover second-image feature entirely (no more image swap on hover).
- Thumbnails now change the main image on CLICK only.
- MOBILE: swipe left = next image, swipe right = previous (cycles the colour's photos).
- DESKTOP: subtle prev / next arrows appear on hover for the same navigation.
- Colour swatch still switches the image set and resets to that colour's first photo.
- Missing images fall back gracefully (no broken states).

This is front-end only (CSS + JS). The page HTML did not change.

## Install (no rebuild needed)
Unzip into your site repo root and overwrite:
  - css/style.css
  - js/site.js

## Push
    git add . ; git commit -m "gallery: remove hover-swap, click thumbs + swipe/arrows" ; git push

(You can run `python build_site.py` too — harmless — but it isn't required for this fix.)
