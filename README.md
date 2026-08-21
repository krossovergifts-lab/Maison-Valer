# Maison Valér — Website

A five-page static site for the Maison Valér leather-goods line (a Krossover sub-brand).
Pure HTML / CSS / vanilla JS — **no build step, no dependencies**. Deploys to Vercel as-is.

## Pages
| File | Page |
|------|------|
| `index.html` | Home |
| `collection.html` | The Collection (all 6 pieces + filters) |
| `desk-to-destinations.html` | Desk to Destinations (featured theme) |
| `about.html` | The House |
| `contact.html` | Enquire |

## Structure
```
css/style.css      one shared stylesheet (design tokens + all components)
js/site.js         theme toggle, scroll reveals, parallax, filters, mailto form
fonts/             self-hosted variable fonts (Fraunces + Archivo) — no Google CDN
images/            optimised .webp product & lifestyle photography
vercel.json        { cleanUrls: true, trailingSlash: false }
```

## Run locally
Just open `index.html` in a browser, or serve the folder:
```bash
python3 -m http.server 8080   # then visit http://localhost:8080
```

## Deploy (VS Code → GitHub → Vercel)
1. Open this folder in VS Code.
2. `git init && git add . && git commit -m "Maison Valér site"`
3. Create a repo and push (e.g. under `krossovergifts-lab`).
4. In Vercel: **Add New → Project → Import** the repo.
   - Framework preset: **Other**
   - Build command: *(leave empty)*
   - Output directory: `.` (root)
5. Deploy. `cleanUrls` gives you `/collection`, `/about`, etc.

## Editing notes
- **Colours / fonts** live as CSS variables at the top of `css/style.css` (`:root` for dark, `[data-theme="light"]` for light).
- **Products** are defined once in `build_site.py` (the generator). Edit there and re-run `python3 build_site.py` to regenerate all pages so nav/footer never drift. You can also edit the HTML directly if you prefer.
- **Enquiry email** is `hello@maisonvaler.com` — change it in `contact.html` (the `mailto:` and the form handler in `js/site.js`) to your real inbox.
- The **hero** is intentionally a dark cinematic band in both light and dark themes; the rest of each page follows the theme toggle.

*Style, refined.*
