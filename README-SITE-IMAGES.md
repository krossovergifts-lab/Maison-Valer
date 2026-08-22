# Maison Valér — manage site images (banners & section images) from the backend

Adds a "Site Images" section to the Studio so banners, home/about section images,
and future-page images can be uploaded + published like products. Each slot shows
recommended dimensions. If a slot is left empty, the site uses the current bundled
image (nothing breaks).

This has TWO parts — the Studio (backend) and the Site (front-end).

## PART 1 — Studio (backend)
Folder:  C:\Users\Admin\Desktop\maison-valer-studio\maison-valer-2026
Copy these in, overwriting:
  - schemaTypes/siteImages.ts   (new)
  - schemaTypes/index.ts        (adds siteImages)
  - structure.ts                (adds "Site Images" to the sidebar)

Then re-deploy the Studio so maison-valer.sanity.studio updates:
    npx sanity deploy

Now the Studio sidebar shows: Site Settings | Site Images | Categories | Products.
Open "Site Images", upload your banners / section images (follow the size hints),
and Publish.

## PART 2 — Site (front-end)
Folder:  C:\Users\Admin\Desktop\Maison-Valer-main
Copy these in, overwriting:
  - build_site.py     (uses backend images, falls back to bundled files)
  - sanity_sync.py    (pulls the site images)

## Then go live (as usual)
Double-click sync.bat  (or run the three commands).
Any image you set in "Site Images" replaces the bundled one; empty slots keep the current image.

## Future pages
When you build a new page later, its image slots get added to "Site Images" then.
You can pre-upload images now under "Extra images (for future pages)" with a key.
