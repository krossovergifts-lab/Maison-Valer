# Maison Valér — real logo in header & footer

Replaces the old mark with your actual logo artwork (M monogram + MAISON VALÉR +
"Style With Purpose"), extracted into the site's theme-aware mask system so it
auto-colours: bone on dark backgrounds, ink on light — no separate files per theme.

- Header: M + MAISON VALÉR lockup.
- Footer: M + MAISON VALÉR + "Style With Purpose" tagline.

## Install
Unzip into your repo root and overwrite:
  - build_site.py
  - css/style.css
  - images/monogram.png   (replaces old M)
  - images/wordmark.png    (new — "MAISON VALÉR")
  - images/tagline.png     (new — "Style With Purpose")

## Rebuild + push
    python build_site.py
    git add . ; git commit -m "use real Maison Valer logo in header and footer" ; git push

Note: the logo uses CSS masks (same technique as your original monogram), so it
renders and recolours correctly in real browsers on your live site.
