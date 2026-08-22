# Maison Valér — mobile edits

1) Product image is now SWIPEABLE on touch: swipe left = next image,
   swipe right = previous (cycles through the active colour's photos).
   Thumbnails and hover still work on desktop.

2) Filter bar: removed "Everyday" and "Gifting" chips, and the glass pill
   now hugs its content (no oversized bar). On small screens it scrolls
   sideways instead of wrapping to a second line.
   (Products tagged everyday/gifting still appear under "All".)

## Install
Unzip into your site repo root, overwrite:
  - build_site.py     (filter chips: All / Desk / Travel)
  - css/style.css     (filter-bar width + mobile scroll)
  - js/site.js        (swipe gesture)

## Rebuild + push
    python build_site.py
    git add . ; git commit -m "mobile: swipeable product image, tidy filter bar" ; git push

To bring back Everyday/Gifting chips later, edit EXCLUDE_FILTERS near the top
of build_site.py (set it to an empty set).
