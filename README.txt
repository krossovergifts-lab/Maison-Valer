Fix: logo (and header icons) not visible in LIGHT theme when the mobile menu is open.

Cause: on the home/desk pages the header is styled for a dark hero and keeps the
logo light; with the menu open in light theme the drawer behind it is light, so a
light logo disappeared. Now, while the menu is open in light theme, the header
switches to dark so the logo/icons stay visible.

Install (no rebuild — CSS + JS only):
  overwrite  css/style.css  and  js/site.js
  git add . ; git commit -m "fix header logo visibility in light theme menu" ; git push
