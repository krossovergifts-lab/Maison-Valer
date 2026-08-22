Footer logo — centered.

Centers the footer brand lockup (M, MAISON VALÉR, Style With Purpose) and the
blurb beneath it within the brand column.

Install: overwrite css/style.css in your repo root.
Push:    git add . ; git commit -m "center footer logo" ; git push
(No rebuild needed — CSS only.)

If you'd rather keep the paragraph left-aligned and center ONLY the logo,
remove this line from the v2.5 block at the bottom of css/style.css:
    .foot-brand p { margin-left: auto; margin-right: auto; }
