Removed the 01/02/03 numbering from the mobile menu.

Install: overwrite build_site.py and css/style.css in your repo root.
Then:  python build_site.py
       git add . ; git commit -m "remove mobile menu numbering" ; git push

(The CSS also hides any leftover numbers, so even before a rebuild the numbers
won't show once style.css is updated.)
