# -*- coding: utf-8 -*-
"""Assemble Maison Valér static site from shared partials."""
import os

OUT = "site"

# ---------------- SVG icons ----------------
ARW = '<svg class="arw" viewBox="0 0 24 24" fill="none" width="16" height="16" aria-hidden="true"><path d="M4 12h15m0 0-6-6m6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SUN = '<svg class="i-sun" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.5"/><path d="M12 2.5v2.6M12 18.9v2.6M4.2 4.2l1.9 1.9M17.9 17.9l1.9 1.9M2.5 12h2.6M18.9 12h2.6M4.2 19.8l1.9-1.9M17.9 6.1l1.9-1.9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 10l6 6 6-6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

IC_LEATHER = '<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M16 4c3 3 7 3 10 2-1 4-1 7 1 10-3 1-5 3-6 6-2-2-5-2-7 0-1-3-3-5-6-6 2-3 2-6 1-10 3 1 7 1 12-2Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M16 10v9" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="1 3"/></svg>'
IC_PEN = '<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="14" y="5" width="4" height="22" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M9 11c-2 1.7-2 8.3 0 10M23 11c2 1.7 2 8.3 0 10" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
IC_SLIM = '<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="7" y="5" width="18" height="22" rx="2.5" stroke="currentColor" stroke-width="1.4"/><path d="M11 5v22" stroke="currentColor" stroke-width="1.4"/><path d="M18 14h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
IC_BRAND = '<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="5" y="8" width="22" height="16" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M24 6l2 2M22 8l3-3 2 2-3 3" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'
IC_GIFT = '<svg class="ic" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="6" y="13" width="20" height="13" rx="1.5" stroke="currentColor" stroke-width="1.4"/><path d="M4 13h24v4H4zM16 13v13" stroke="currentColor" stroke-width="1.4"/><path d="M16 13c-4 0-6-1-6-3.5S12 6 16 13Zm0 0c4 0 6-1 6-3.5S20 6 16 13Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>'

MONO = '<span class="mono" aria-hidden="true"></span>'

def wordmark(big=False):
    return ('<span class="wordmark"><span class="maison">Maison</span>'
            '<span class="valer">Valér</span></span>')

# ---------------- Head ----------------
def head(title, desc, page):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#14100c">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preload" href="fonts/fraunces-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body>'''

# ---------------- Header ----------------
NAV_ITEMS = [
    ("index.html", "Home", "home"),
    ("collection.html", "Collection", "collection"),
    ("desk-to-destinations.html", "Desk to Destinations", "d2d"),
    ("about.html", "About", "about"),
    ("contact.html", "Contact", "contact"),
]

def header(page):
    links = ""
    for href, label, key in NAV_ITEMS:
        cur = ' aria-current="page"' if key == page else ""
        links += f'<a href="{href}"{cur}>{label}</a>'
    draw = ""
    for i, (href, label, key) in enumerate(NAV_ITEMS, 1):
        draw += f'<a href="{href}"><span class="n">0{i}</span>{label}</a>'
    over = " over-dark" if page in ("home", "d2d") else ""
    return f'''
<header class="site-head{over}">
  <div class="head-inner">
    <a class="brand" href="index.html" aria-label="Maison Valér home">{MONO}{wordmark()}</a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="head-actions">
      <button class="theme-toggle" type="button" aria-label="Switch colour theme">{SUN}{MOON}</button>
      <a class="btn btn--solid head-cta" href="contact.html">Enquire {ARW}</a>
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="drawer" aria-label="Mobile">{draw}</nav>
<div class="side-rail" aria-hidden="true">#MaisonValér — Style, Refined</div>
'''

# ---------------- Footer ----------------
def footer():
    return f'''
<section class="section cta-band">
  {MONO_BIG()}
  <div class="wrap reveal">
    <p class="eyebrow center" style="justify-content:center">Corporate gifting · Wholesale · Bespoke</p>
    <h2 class="display" style="margin-top:22px">Carry something <em>considered.</em></h2>
    <p class="lede">Maison Valér partners with brands and businesses to craft leather essentials that carry identity, intent, and lasting impression — from a single desk to a thousand.</p>
    <a class="btn btn--solid" href="contact.html">Start an enquiry {ARW}</a>
  </div>
</section>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        {MONO}
        {wordmark()}
        <p>Leather essentials shaped for professionals who move between the desk and the world. Refined in form, purposeful in function.</p>
      </div>
      <div class="foot-col">
        <h5>Explore</h5>
        <a href="collection.html">The Collection</a>
        <a href="desk-to-destinations.html">Desk to Destinations</a>
        <a href="about.html">The House</a>
        <a href="contact.html">Enquire</a>
      </div>
      <div class="foot-col">
        <h5>Collection</h5>
        <a href="collection.html">The Strategist</a>
        <a href="collection.html">The Minimalist</a>
        <a href="collection.html">The Explorer</a>
        <a href="collection.html">The Identifier</a>
      </div>
      <div class="foot-col">
        <h5>Connect</h5>
        <a href="mailto:hello@maisonvaler.com">hello@maisonvaler.com</a>
        <a href="contact.html">Dubai · United Arab Emirates</a>
        <a href="contact.html">Trade &amp; Wholesale</a>
      </div>
    </div>
    <div class="foot-bottom">
      <p>© <span data-year>2026</span> Maison Valér. The language of considered design.</p>
      <p>Style, Refined.</p>
    </div>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>'''

def MONO_BIG():
    return '<span class="mono" aria-hidden="true" style="width:clamp(160px,30vw,340px);height:clamp(160px,30vw,340px);color:var(--bone);opacity:.05;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:0"></span>'

# ---------------- Products data ----------------
PRODUCTS = [
    dict(sku="REXORA-11653", arch="The Strategist", name="Executive Organizer",
         sub="with Magnetic Pen Holder", price="32", img="organizer-brown",
         cat="desk gifting", colors=["brown","black","gray"],
         desc="Notes, documents and a magnetic pen — held in one refined leather profile built for meetings and the move."),
    dict(sku="MAGTEC-11659", arch="The Minimalist", name="Magnetic Card Holder",
         sub="MagSafe Phone Wallet", price="14", img="cardholder-life",
         cat="travel everyday", colors=["brown","black","gray"],
         desc="Everyday cards in a slim MagSafe form that snaps to the phone and disappears into the pocket."),
    dict(sku="LEPORT-11662", arch="The Explorer", name="Premium Travel Wallet",
         sub="Multifunctional Passport Holder", price="20", img="life-passport",
         cat="travel gifting", colors=["brown","black","gray"],
         desc="Passport, cards and boarding pass in a structured fold — organised from check-in to destination."),
    dict(sku="LETHEG-11658", arch="The Identifier", name="Leather Luggage Tag",
         sub="Concealed ID", price="8", img="luggage-tag",
         cat="travel gifting", colors=["brown","black","gray"],
         desc="A quiet mark of ownership — refined presence on the belt, privacy for the details within."),
    dict(sku="MAGFOLD-11656", arch="The Companion", name="Magnetic Card Holder & Stand",
         sub="Fold-out MagSafe Stand", price="14", img="cardholder-gray",
         cat="everyday desk", colors=["gray","blue","green"],
         desc="Cards that hold, then fold — a magnetic stand for the desk, the flight, the in-between."),
    dict(sku="MAGFOLDRA-11655", arch="The Reserve", name="Magnetic Power Bank & Stand",
         sub="Wireless MagSafe Power", price="44", img="flatlay-phone",
         cat="everyday desk", colors=["blue","gray"],
         desc="Wireless power with a fold-out stand — a quiet reserve of energy that stays with the phone."),
]

def colorname(c):
    return {"brown":"Brown","black":"Black","gray":"Gray","blue":"Blue","green":"Green"}[c]

def swatches(colors):
    s = ""
    for c in colors:
        s += f'<span class="swatch sw-{c}" title="{colorname(c)}"></span>'
    return f'<div class="swatches" aria-label="Colours">{s}</div>'

def product_card(p, delay=""):
    tags = ""
    return f'''
      <article class="pcard reveal {delay}" data-cat="{p['cat']}">
        <a class="pcard-media img-reveal" href="collection.html" aria-label="{p['name']}">
          <span class="pcard-tag">New Arrival</span>
          <span class="pcard-arch">{p['arch']}</span>
          <img src="images/{p['img']}.webp" alt="{p['name']} in {colorname(p['colors'][0])} leather" loading="lazy" width="900" height="1125">
        </a>
        <div class="pcard-body">
          <span class="sku">{p['sku']}</span>
          <h3>{p['name']}<br><span style="font-style:italic;font-weight:360">{p['sub']}</span></h3>
          <p>{p['desc']}</p>
          <div class="pcard-foot">
            {swatches(p['colors'])}
            <span class="pcard-price">AED {p['price']} <small>/ unit</small></span>
          </div>
        </div>
      </article>'''

# =====================================================================
# PAGE: HOME
# =====================================================================
def page_home():
    cards = "".join(product_card(p, ["","d1","d2","d3"][i]) for i, p in enumerate(PRODUCTS[:4]))
    return head("Maison Valér — Style, Refined.",
                "Maison Valér crafts premium leather essentials for work, travel and executive gifting. The language of considered design.",
                "home") + header("home") + f'''
<main>
  <!-- HERO -->
  <section class="hero">
    <div class="hero-media" data-parallax="0.12">
      <img src="images/hero-desk.webp" alt="Maison Valér cognac leather desk essentials" width="1900" height="1900" fetchpriority="high">
    </div>
    <div class="hero-inner wrap">
      <p class="hero-eyebrow eyebrow fade-seq d1">The Language of Considered Design</p>
      <h1 class="hero-title display">
        <span class="line l1"><span>Style,</span></span>
        <span class="line l2"><span><em>refined.</em></span></span>
      </h1>
      <div class="hero-sub fade-seq d2">
        <p class="lede">Leather essentials for those who move between the desk and the world — refined in form, purposeful in function, consistent in character.</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center">
          <a class="btn btn--solid" href="collection.html">Explore the collection {ARW}</a>
          <a class="btn btn--ghost" href="desk-to-destinations.html">Desk to Destinations</a>
        </div>
      </div>
    </div>
  </section>

  <!-- RIBBON -->
  <div class="ribbon" aria-hidden="true">
    <div class="ribbon-track">
      <span>Style, Refined.</span><span class="star">✦</span>
      <span>The Language of Considered Design</span><span class="star">✦</span>
      <span>Brand Smarter, Not Louder</span><span class="star">✦</span>
      <span>Desk to Destination</span><span class="star">✦</span>
      <span>Style, Refined.</span><span class="star">✦</span>
      <span>The Language of Considered Design</span><span class="star">✦</span>
      <span>Brand Smarter, Not Louder</span><span class="star">✦</span>
      <span>Desk to Destination</span><span class="star">✦</span>
    </div>
  </div>

  <!-- ETHOS -->
  <section class="section ethos">
    <div class="wrap grid two">
      <div class="reveal">
        <p class="eyebrow">The House</p>
        <h2 class="display" style="margin-top:20px">Design begins with <em>restraint.</em></h2>
        <p class="lede" style="margin-top:28px">Each detail is deliberate, each material chosen for its integrity, each form shaped to serve a clear purpose. The result is a collection that speaks through clarity — not noise.</p>
        <div class="ethos-stats">
          <div class="stat"><span class="num">6</span><span class="lbl">Signature pieces</span></div>
          <div class="stat"><span class="num">3</span><span class="lbl">Leather finishes</span></div>
          <div class="stat"><span class="num">1</span><span class="lbl">Considered idea</span></div>
        </div>
        <a class="tlink" href="about.html" style="margin-top:40px">Read our philosophy {ARW}</a>
      </div>
      <div class="reveal d1">
        <div class="figure tall img-reveal"><img src="images/organizer-fan.webp" alt="Organizer in brown, gray and black leather" loading="lazy" width="1100" height="880"></div>
        <div class="cap"><span>Available in Brown · Black · Gray</span><span>Full-grain finish</span></div>
      </div>
    </div>
  </section>

  <!-- COLLECTION PREVIEW -->
  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="eyebrow">The Collection</p>
        <h2 class="display">Essentials, edited.</h2>
        <p class="lede">Four archetypes for the working professional — and the accessories that keep them powered and in place.</p>
      </div>
      <div class="prod-grid">{cards}</div>
      <div style="margin-top:48px" class="reveal"><a class="btn btn--ghost" href="collection.html">View all six pieces {ARW}</a></div>
    </div>
  </section>

  <!-- DESK TO DESTINATIONS BAND -->
  <section class="section" style="background:var(--coal);border-block:1px solid var(--line)">
    <div class="wrap grid two">
      <div class="reveal">
        <div class="figure img-reveal" style="aspect-ratio:1/1"><img src="images/mascots.webp" alt="The Desk to Destinations leather characters" loading="lazy" width="1195" height="1195"></div>
      </div>
      <div class="reveal d1">
        <p class="eyebrow">Featured Theme</p>
        <h2 class="display" style="font-size:clamp(34px,5.6vw,72px);margin-top:20px">Desk to <em>Destination.</em></h2>
        <p class="lede" style="margin-top:26px">A curated leather family for professionals who value order, movement and presence. Each piece transitions seamlessly between work and travel — not accessories, but companions.</p>
        <a class="btn btn--solid" href="desk-to-destinations.html" style="margin-top:36px">Meet the family {ARW}</a>
      </div>
    </div>
  </section>

  <!-- MATERIALS SPLIT -->
  <section class="section">
    <div class="wrap grid two">
      <div class="reveal">
        <div class="figure tall img-reveal"><img src="images/briefcase.webp" alt="Executive with leather essentials and briefcase" loading="lazy" width="1100" height="1473"></div>
      </div>
      <div class="reveal d1">
        <p class="eyebrow">Materials</p>
        <h2 class="display" style="font-size:clamp(30px,4.6vw,58px);margin-top:20px">Selected for <em>longevity.</em></h2>
        <p class="lede" style="margin-top:26px">Material, form and finish in perfect balance. Premium leather that ages naturally, stitching built for daily use, and a branding-ready surface made for the mark that matters — yours.</p>
        <div class="pillars" style="margin-top:44px;grid-template-columns:1fr 1fr">
          <div class="pillar"><span class="k">01</span><h3>Full-grain leather</h3><p>Chosen for integrity and a patina that deepens with time.</p></div>
          <div class="pillar"><span class="k">02</span><h3>Made to be marked</h3><p>A clean, considered surface for embossed or foiled identity.</p></div>
        </div>
      </div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: COLLECTION
# =====================================================================
def page_collection():
    cards = "".join(product_card(p, ["","d1","d2","d3","","d1"][i]) for i, p in enumerate(PRODUCTS))
    return head("Collection — Maison Valér",
                "The full Maison Valér collection: organizers, card holders, travel wallets, luggage tags and magnetic accessories in premium leather.",
                "collection") + header("collection") + f'''
<main>
  <section class="section section--tight" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap">
      <div class="section-head reveal" style="max-width:900px">
        <p class="eyebrow">The Collection · 2026</p>
        <h1 class="display" style="font-size:clamp(44px,8vw,110px);margin-top:18px">Six pieces,<br>one <em class="serif-it" style="color:var(--cognac)">standard.</em></h1>
        <p class="lede" style="margin-top:28px">Every item is offered in a considered range of finishes and made ready for your brand. Prices are per unit for trade and corporate gifting.</p>
      </div>

      <div class="filterbar reveal" role="tablist" aria-label="Filter collection">
        <button class="chip active" data-filter="all">All</button>
        <button class="chip" data-filter="desk">Desk</button>
        <button class="chip" data-filter="travel">Travel</button>
        <button class="chip" data-filter="everyday">Everyday</button>
        <button class="chip" data-filter="gifting">Gifting</button>
      </div>

      <div class="prod-grid">{cards}</div>
    </div>
  </section>

  <!-- FEATURE STRIP -->
  <section class="section--tight">
    <div class="feat-strip reveal">
      <div class="feat">{IC_LEATHER}<h4>Premium Leather</h4><p>Full-grain construction with a refined, natural texture.</p></div>
      <div class="feat">{IC_PEN}<h4>Magnetic Detail</h4><p>Considered magnetic closures and MagSafe alignment.</p></div>
      <div class="feat">{IC_SLIM}<h4>Slim Profile</h4><p>Executive forms that slip into bag, pocket or briefcase.</p></div>
      <div class="feat">{IC_BRAND}<h4>Branding Ready</h4><p>A clean surface built for embossed or foiled identity.</p></div>
      <div class="feat">{IC_GIFT}<h4>Gift Ready</h4><p>Corporate-gifting presentation, out of the box.</p></div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: DESK TO DESTINATIONS
# =====================================================================
def page_d2d():
    archs = [
        dict(n="01", role="Organizer with Magnetic Pen Holder", name="The", em="Strategist",
             img="life-organizer", sku="REXORA-11653", price="32",
             p="Perfect for meetings, planning sessions and executive gifting. Keeps ideas, tools and workflow aligned — whether at the desk or on the move.",
             use="Meetings · Travel work", carry="Notes · Pen · Documents"),
        dict(n="02", role="MagSafe Card Holder", name="The", em="Minimalist",
             img="cardholder-gray", sku="MAGTEC-11659", price="14",
             p="Ideal for everyday professionals who prefer lightweight carry. Seamlessly transitions from office use to travel without the need for a full wallet.",
             use="Everyday · Commute", carry="Cards · MagSafe"),
        dict(n="03", role="Multifunctional Passport Holder", name="The", em="Explorer",
             img="life-passport", sku="LEPORT-11662", price="20",
             p="Designed for frequent travellers, executives and corporate gifting. Keeps travel essentials organised and accessible from check-in to destination.",
             use="Travel · Business", carry="Passport · Cards · Pass"),
        dict(n="04", role="Leather Luggage Tag", name="The", em="Identifier",
             img="luggage-tag", sku="LETHEG-11658", price="8",
             p="Ideal for business travel, corporate gifting and brand identity. Adds a refined, professional presence while ensuring easy luggage recognition.",
             use="Travel · Gifting", carry="Concealed ID"),
    ]
    blocks = ""
    for a in archs:
        blocks += f'''
      <article class="arch reveal">
        <div class="arch-media img-reveal"><img src="images/{a['img']}.webp" alt="{a['name']} {a['em']} — {a['role']}" loading="lazy" width="950" height="1187"></div>
        <div>
          <span class="arch-index">{a['n']}</span>
          <h2>{a['name']} <em>{a['em']}</em></h2>
          <p class="role">{a['role']}</p>
          <p>{a['p']}</p>
          <div class="arch-meta">
            <div><span class="k">Best for</span><span class="v">{a['use']}</span></div>
            <div><span class="k">Carries</span><span class="v">{a['carry']}</span></div>
            <div><span class="k">From</span><span class="v">AED {a['price']}</span></div>
          </div>
          <div style="margin-top:30px;display:flex;gap:14px;align-items:center;flex-wrap:wrap">
            {swatches(["brown","black","gray"])}
            <span class="sku" style="font-size:11px;letter-spacing:.18em;color:var(--faint);text-transform:uppercase">{a['sku']}</span>
          </div>
        </div>
      </article>'''
    return head("Desk to Destinations — Maison Valér",
                "Desk to Destinations: a curated leather family — the Strategist, the Minimalist, the Explorer and the Identifier — built to move from desk to destination.",
                "d2d") + header("d2d") + f'''
<main>
  <!-- HERO -->
  <section class="d2d-hero">
    <div class="hero-media" data-parallax="0.1"><img src="images/mascots.webp" alt="The Desk to Destinations leather characters at the airport" width="1195" height="1688" fetchpriority="high"></div>
    <div class="hero-inner wrap">
      <p class="hero-eyebrow eyebrow fade-seq d1">Featured Theme</p>
      <h1 class="hero-title display" style="font-size:clamp(46px,11vw,150px)">
        <span class="line l1"><span>Desk to</span></span>
        <span class="line l2"><span><em>destination.</em></span></span>
      </h1>
      <p class="lede fade-seq d2" style="margin-top:30px;max-width:52ch">A curated leather essentials theme for professionals who value order, movement and presence — crafted to transition seamlessly between work and travel.</p>
    </div>
  </section>

  <div class="ribbon" aria-hidden="true">
    <div class="ribbon-track">
      <span>The Strategist</span><span class="star">✦</span>
      <span>The Minimalist</span><span class="star">✦</span>
      <span>The Explorer</span><span class="star">✦</span>
      <span>The Identifier</span><span class="star">✦</span>
      <span>The Strategist</span><span class="star">✦</span>
      <span>The Minimalist</span><span class="star">✦</span>
      <span>The Explorer</span><span class="star">✦</span>
      <span>The Identifier</span><span class="star">✦</span>
    </div>
  </div>

  <!-- INTRO -->
  <section class="section section--tight">
    <div class="wrap" style="max-width:900px">
      <p class="eyebrow reveal">The Idea</p>
      <p class="manifesto reveal d1" style="max-width:26ch;margin-top:22px">Not accessories. <em>Companions</em> — built to carry ideas, identity and intent.</p>
    </div>
  </section>

  <!-- ARCHETYPES -->
  <section class="section" style="padding-top:0">
    <div class="wrap">{blocks}</div>
  </section>

  <!-- FEATURES -->
  <section class="section--tight">
    <div class="feat-strip reveal">
      <div class="feat">{IC_LEATHER}<h4>Premium Leather</h4><p>Full-grain construction, refined texture.</p></div>
      <div class="feat">{IC_PEN}<h4>Magnetic Pen Holder</h4><p>Quick access, secure placement.</p></div>
      <div class="feat">{IC_SLIM}<h4>Slim Executive Profile</h4><p>Fits easily into bags and briefcases.</p></div>
      <div class="feat">{IC_BRAND}<h4>Branding Ready</h4><p>A surface made for your mark.</p></div>
      <div class="feat">{IC_GIFT}<h4>Corporate Gift Ready</h4><p>Presentation, out of the box.</p></div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: ABOUT
# =====================================================================
def page_about():
    return head("The House — Maison Valér",
                "At Maison Valér, design begins with restraint. Learn the philosophy behind the language of considered design.",
                "about") + header("about") + f'''
<main>
  <section class="section section--tight" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap">
      <div class="section-head reveal" style="max-width:1000px">
        <p class="eyebrow">The House</p>
        <h1 class="display" style="font-size:clamp(44px,8vw,112px);margin-top:18px">Clarity,<br>not <em class="serif-it" style="color:var(--cognac)">noise.</em></h1>
      </div>
      <div class="grid two">
        <div class="reveal"><div class="figure tall img-reveal"><img src="images/life-organizer.webp" alt="Executive using a Maison Valér organizer" loading="lazy" width="950" height="1187"></div></div>
        <div class="reveal d1">
          <p class="manifesto">Every detail serves a <em>purpose</em> — material, form and finish in perfect balance.</p>
          <p class="lede" style="margin-top:30px">Maison Valér is designed for those who value precision, restraint and timeless clarity. Design begins with restraint: each detail deliberate, each material chosen for its integrity, and each form shaped to serve a clear purpose.</p>
          <p class="lede" style="margin-top:20px">The result is a collection that speaks through clarity — a considered response to a world that too often shouts. We prefer to brand smarter, not louder.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--coal);border-block:1px solid var(--line)">
    <div class="wrap">
      <div class="section-head reveal"><p class="eyebrow">Principles</p><h2 class="display" style="margin-top:18px">What we hold to.</h2></div>
      <div class="pillars">
        <div class="pillar reveal"><span class="k">i.</span><h3>Restraint</h3><p>We remove before we add. Nothing on a Maison Valér piece is there to decorate — only to serve.</p></div>
        <div class="pillar reveal d1"><span class="k">ii.</span><h3>Integrity</h3><p>Materials are selected for longevity. Full-grain leather that ages honestly, stitching built for daily use.</p></div>
        <div class="pillar reveal d2"><span class="k">iii.</span><h3>Presence</h3><p>Refined form that carries identity quietly — a considered surface made ready for your mark.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap grid two">
      <div class="reveal d1">
        <p class="eyebrow">From desk to destination</p>
        <h2 class="display" style="font-size:clamp(30px,4.6vw,58px);margin-top:20px">Built to <em>move</em> with you.</h2>
        <p class="lede" style="margin-top:26px">Our essentials are made for professionals in motion — the organiser on the desk, the card holder in the pocket, the passport wallet at the gate, the tag on the case. One consistent character, wherever work takes you.</p>
        <a class="tlink" href="desk-to-destinations.html" style="margin-top:36px">Explore the theme {ARW}</a>
      </div>
      <div class="reveal"><div class="figure tall img-reveal"><img src="images/airport-man.webp" alt="Traveller with Maison Valér essentials at the airport" loading="lazy" width="1500" height="1094"></div></div>
    </div>
  </section>
</main>
''' + footer()

# =====================================================================
# PAGE: CONTACT
# =====================================================================
def page_contact():
    opts = "".join(f'<option>{p["name"]}</option>' for p in PRODUCTS)
    return head("Contact — Maison Valér",
                "Enquire with Maison Valér for corporate gifting, wholesale and bespoke leather essentials.",
                "contact") + header("contact") + f'''
<main>
  <section class="section" style="padding-top:clamp(120px,16vh,190px)">
    <div class="wrap grid two" style="align-items:start;gap:clamp(40px,6vw,100px)">
      <div class="reveal">
        <p class="eyebrow">Enquire</p>
        <h1 class="display" style="font-size:clamp(40px,7vw,96px);margin-top:16px">Let's make it <em class="serif-it" style="color:var(--cognac)">yours.</em></h1>
        <p class="lede" style="margin-top:26px">Tell us about your brand and the occasion. We'll come back with finishes, branding options and pricing for corporate gifting, wholesale or bespoke runs.</p>
        <div class="contact-side" style="margin-top:52px">
          <div class="contact-item"><p class="k">Email</p><a class="v" href="mailto:hello@maisonvaler.com">hello@maisonvaler.com</a></div>
          <div class="contact-item"><p class="k">Studio</p><p class="v">Dubai · United Arab Emirates</p></div>
          <div class="contact-item"><p class="k">Trade</p><p class="v">Wholesale &amp; corporate gifting</p></div>
        </div>
      </div>

      <div class="reveal d1" style="background:var(--card);border:1px solid var(--line);border-radius:10px;padding:clamp(24px,3vw,44px)">
        <form class="form" novalidate>
          <div class="two-col">
            <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" placeholder="Your name" autocomplete="name"></div>
            <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="you@company.com" autocomplete="email"></div>
          </div>
          <div class="two-col">
            <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" placeholder="Company / brand" autocomplete="organization"></div>
            <div class="field"><label for="quantity">Quantity</label><input id="quantity" name="quantity" type="text" placeholder="e.g. 250 units"></div>
          </div>
          <div class="field">
            <label for="interest">Piece of interest</label>
            <select id="interest" name="interest">
              <option>The full collection</option>
              {opts}
              <option>Desk to Destinations set</option>
              <option>Bespoke / other</option>
            </select>
          </div>
          <div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="Tell us about the occasion, branding and timeline…"></textarea></div>
          <div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap">
            <button class="btn btn--solid" type="submit">Send enquiry {ARW}</button>
            <span class="form-status" role="status" aria-live="polite"></span>
          </div>
          <p class="form-note">This opens your email client with the details prefilled. Prefer to write directly? <a href="mailto:hello@maisonvaler.com" style="color:var(--cognac)">hello@maisonvaler.com</a></p>
        </form>
      </div>
    </div>
  </section>
</main>
''' + footer()

# ---------------- Write ----------------
pages = {
    "index.html": page_home(),
    "collection.html": page_collection(),
    "desk-to-destinations.html": page_d2d(),
    "about.html": page_about(),
    "contact.html": page_contact(),
}
os.makedirs(OUT, exist_ok=True)
for fn, html in pages.items():
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fn, len(html), "chars")

# vercel + readme
with open(os.path.join(OUT, "vercel.json"), "w") as f:
    f.write('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n')
print("done")
