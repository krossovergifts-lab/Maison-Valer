# Maison Valér — "Get a Quote" button update

Adds a Get a Quote button to every product card with a trending cognac
fill-sweep hover effect. Clicking it opens the Contact page with the
enquiry pre-filled (product name + SKU in the message, and the matching
"Piece of interest" selected).

Fits your no-price, corporate-gifting model — "Get a Quote", not "Buy Now".
Fully translated (EN / RU / AR) and RTL-aware.

## Install
Unzip into your site repo root and overwrite:
  - build_site.py      (adds the button + i18n keys)
  - css/style.css      (button styling)
  - js/site.js         (quote pre-fill on the contact page)

## Rebuild + push
    python build_site.py
    git add . ; git commit -m "add Get a Quote button on product cards" ; git push

(No need to re-run sanity_sync.py unless your backend content changed.)
