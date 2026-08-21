/* =========================================================
   MAISON VALÉR — site behaviours (v2)
   theme · header · drawer · reveal · parallax · filter ·
   product gallery (colour-swap + hover/second image + thumbs) ·
   i18n (EN / RU / AR + RTL) · contact form
   ========================================================= */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Theme ---------- */
  function storedTheme() { try { return localStorage.getItem('mv-theme'); } catch (e) { return null; } }
  function saveTheme(t) { try { localStorage.setItem('mv-theme', t); } catch (e) {} }
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', t === 'light' ? '#f2ebde' : '#14100c');
  }
  applyTheme(storedTheme() || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'));
  function bindTheme() {
    var toggle = document.querySelector('.theme-toggle');
    if (!toggle) return;
    toggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next); saveTheme(next);
    });
  }

  /* ---------- i18n (EN / RU / AR + RTL) ---------- */
  function bindI18n() {
    var I18N = window.MV_I18N || {};
    var LANGS = window.MV_LANGS || ['en'];
    var LOCAL = {
      form_need: { en: 'Please add your name and email so we can reply.',
                   ru: 'Пожалуйста, укажите имя и эл. почту, чтобы мы могли ответить.',
                   ar: 'يرجى إضافة اسمك وبريدك الإلكتروني حتى نتمكن من الرد.' },
      form_open: { en: 'Opening your email client to send this enquiry…',
                   ru: 'Открываем почтовый клиент для отправки запроса…',
                   ar: 'يتم فتح برنامج البريد لإرسال هذا الاستفسار…' }
    };
    function stored() { try { return localStorage.getItem('mv-lang'); } catch (e) { return null; } }
    function save(l) { try { localStorage.setItem('mv-lang', l); } catch (e) {} }
    var cur = stored() || 'en';
    if (LANGS.indexOf(cur) < 0) cur = 'en';

    function look(key) { var e = I18N[key] || LOCAL[key]; return e ? (e[cur] || e.en) : null; }
    window.MV_t = function (key) { var v = look(key); return v == null ? key : v; };
    window.MV_lang = function () { return cur; };

    function apply() {
      root.setAttribute('lang', cur);
      root.setAttribute('dir', cur === 'ar' ? 'rtl' : 'ltr');
      document.querySelectorAll('[data-i18n]').forEach(function (el) {
        var v = look(el.getAttribute('data-i18n')); if (v != null) el.textContent = v;
      });
      document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
        var v = look(el.getAttribute('data-i18n-html')); if (v != null) el.innerHTML = v;
      });
      document.querySelectorAll('[data-i18n-ph]').forEach(function (el) {
        var v = look(el.getAttribute('data-i18n-ph')); if (v != null) el.setAttribute('placeholder', v);
      });
      document.querySelectorAll('[data-i18n-title]').forEach(function (el) {
        var v = look(el.getAttribute('data-i18n-title'));
        if (v != null) { el.setAttribute('title', v); el.setAttribute('aria-label', v); }
      });
      document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
        var v = look(el.getAttribute('data-i18n-aria')); if (v != null) el.setAttribute('aria-label', v);
      });
      document.querySelectorAll('.lang-switch button').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-lang') === cur);
      });
      if (window.MV_afterApply) window.MV_afterApply();
    }
    function setLang(l) { if (LANGS.indexOf(l) < 0) return; cur = l; save(l); apply(); }
    window.MV_setLang = setLang;
    document.querySelectorAll('.lang-switch button').forEach(function (b) {
      b.addEventListener('click', function () { setLang(b.getAttribute('data-lang')); });
    });
    apply();
  }

  /* ---------- Header scroll state ---------- */
  function bindHeader() {
    var head = document.querySelector('.site-head');
    if (!head) return;
    var onScroll = function () { head.classList.toggle('scrolled', window.scrollY > 24); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile drawer ---------- */
  function bindDrawer() {
    var burger = document.querySelector('.burger');
    var drawer = document.querySelector('.drawer');
    if (!burger || !drawer) return;
    var toggle = function (open) {
      burger.classList.toggle('open', open);
      drawer.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () { toggle(!drawer.classList.contains('open')); });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { toggle(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) toggle(false);
    });
  }

  /* ---------- Scroll reveal ---------- */
  function bindReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    if (reduceMotion || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Hero parallax ---------- */
  function bindParallax() {
    if (reduceMotion) return;
    var layers = document.querySelectorAll('[data-parallax]');
    if (!layers.length) return;
    var ticking = false;
    var update = function () {
      var y = window.scrollY;
      layers.forEach(function (l) {
        var speed = parseFloat(l.getAttribute('data-parallax')) || 0.15;
        l.style.transform = 'translate3d(0,' + (y * speed) + 'px,0) scale(1.06)';
      });
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---------- Product gallery: colour-swap + hover image + thumbnails ---------- */
  function imgSrc(name) {
    // paths are pre-resolved by the generator (full URL or local path);
    // tolerate a bare name too, just in case.
    if (/^https?:\/\//.test(name) || name.indexOf('/') > -1 || name.indexOf('.webp') > -1) return name;
    return 'images/products/' + name + '.webp';
  }

  function setupCard(card) {
    var jsonEl = card.querySelector('.pcard-json');
    var media = card.querySelector('.pcard-media');
    var baseImg = card.querySelector('.pcard-img');
    var thumbs = card.querySelector('.pcard-thumbs');
    if (!jsonEl || !media || !baseImg || !thumbs) return;

    var data; try { data = JSON.parse(jsonEl.textContent); } catch (e) { return; }
    var colors = (data.colors || []).filter(function (c) { return c.imgs && c.imgs.length; });
    if (!colors.length) return;

    // hover / second-image layer
    var altImg = new Image();
    altImg.className = 'pcard-img pcard-img--alt';
    altImg.alt = ''; altImg.setAttribute('aria-hidden', 'true');
    altImg.addEventListener('error', function () { media.classList.remove('has-alt'); });
    media.insertBefore(altImg, thumbs);

    var state = { color: colors[0], idx: 0 };

    baseImg.addEventListener('error', function () {
      if (baseImg._fb) return; baseImg._fb = 1; baseImg.src = imgSrc(colors[0].imgs[0]);
    });

    function setMain(i) {
      state.idx = i;
      var imgs = state.color.imgs;
      baseImg._fb = 0;
      baseImg.src = imgSrc(imgs[i]);
      if (imgs.length > 1) {
        altImg.src = imgSrc(imgs[(i + 1) % imgs.length]);
        media.classList.add('has-alt');
      } else {
        media.classList.remove('has-alt');
      }
      thumbs.querySelectorAll('.pcard-thumb').forEach(function (t) {
        t.classList.toggle('active', +t.getAttribute('data-idx') === i);
      });
    }

    function buildThumbs() {
      thumbs.innerHTML = '';
      var imgs = state.color.imgs;
      if (imgs.length < 2) return; // single image -> no strip
      imgs.forEach(function (name, i) {
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'pcard-thumb' + (i === 0 ? ' active' : '');
        b.setAttribute('data-idx', i);
        b.setAttribute('aria-label', state.color.name + ' view ' + (i + 1));
        var im = new Image(); im.loading = 'lazy'; im.alt = '';
        im.addEventListener('error', function () { b.remove(); });
        im.src = imgSrc(name);
        b.appendChild(im);
        b.addEventListener('mouseenter', function () { setMain(i); });
        b.addEventListener('click', function (e) { e.preventDefault(); setMain(i); });
        thumbs.appendChild(b);
      });
    }

    function selectColor(c) { state.color = c; buildThumbs(); setMain(0); }

    card.querySelectorAll('.swatch').forEach(function (sw) {
      var key = sw.getAttribute('data-color');
      var match = colors.filter(function (x) { return x.k === key; })[0];
      sw.addEventListener('click', function () {
        card.querySelectorAll('.swatch').forEach(function (s) { s.classList.remove('active'); });
        sw.classList.add('active');
        selectColor(match || colors[0]);
      });
    });

    selectColor(colors[0]);
  }

  function bindGalleries() {
    document.querySelectorAll('.pcard').forEach(setupCard);
  }

  /* ---------- Title reveal (line mask, re-runs on language change) ---------- */
  var titleIO = null;
  function collectTitles() { return document.querySelectorAll('.hero-title, main h1.display'); }
  function splitTitle(el) {
    var parts = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = parts.map(function (p, i) {
      return '<span class="tl-line"><span class="tl-inner" style="--d:' + (i * 0.09) + 's">' + p + '</span></span>';
    }).join('');
    el.classList.add('anim-title');
  }
  function bindTitles() {
    var titles = collectTitles();
    if (!titles.length) return;
    if (reduceMotion) { titles.forEach(function (el) { splitTitle(el); el.classList.add('in'); }); return; }
    if (titleIO) titleIO.disconnect();
    titleIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); titleIO.unobserve(en.target); } });
    }, { threshold: 0.2, rootMargin: '0px 0px -6% 0px' });
    titles.forEach(function (el) {
      splitTitle(el);
      if (el.closest('.hero, .d2d-hero')) {
        requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('in'); }); });
      } else {
        titleIO.observe(el);
      }
    });
  }
  window.MV_afterApply = bindTitles; // language switch rewrites headings -> re-split & re-animate

  /* ---------- Collection filter ---------- */
  function bindFilter() {
    var bar = document.querySelector('.filterbar');
    if (!bar) return;
    var chips = bar.querySelectorAll('.chip');
    var cards = document.querySelectorAll('.pcard[data-cat]');
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        var cat = chip.getAttribute('data-filter');
        cards.forEach(function (card) {
          var match = cat === 'all' || card.getAttribute('data-cat').indexOf(cat) > -1;
          card.classList.toggle('hide', !match);
        });
      });
    });
  }

  /* ---------- Quote prefill (from a product card's Get a Quote button) ---------- */
  function bindQuotePrefill() {
    var form = document.querySelector('.form');
    if (!form) return;
    var params = new URLSearchParams(window.location.search);
    var sku = params.get('product');
    var name = params.get('name');
    if (!sku && !name) return;
    var msg = form.querySelector('[name="message"]');
    if (msg && !msg.value) {
      var lead = window.MV_t ? window.MV_t('quote_prefill') : "I'd like a quote for ";
      msg.value = lead + (name || '') + (sku ? ' (' + sku + ')' : '') + '.';
    }
    var sel = form.querySelector('[name="interest"]');
    if (sel && name) {
      for (var i = 0; i < sel.options.length; i++) {
        if (sel.options[i].text.trim() === name.trim()) { sel.selectedIndex = i; break; }
      }
    }
    try { form.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (e) {}
  }

  /* ---------- Contact form (client-side mailto) ---------- */
  function bindForm() {
    var form = document.querySelector('.form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    var T = function (k) { return window.MV_t ? window.MV_t(k) : k; };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('[name="name"]');
      var email = form.querySelector('[name="email"]');
      if (!name.value.trim() || !email.value.trim()) {
        if (status) status.textContent = T('form_need');
        return;
      }
      var val = function (n) { var el = form.querySelector('[name="' + n + '"]'); return el ? el.value : ''; };
      var subject = encodeURIComponent('Maison Valér — Enquiry from ' + name.value.trim());
      var body = encodeURIComponent(
        'Name: ' + name.value.trim() +
        '\nEmail: ' + email.value.trim() +
        '\nCompany: ' + val('company') +
        '\nInterest: ' + val('interest') +
        '\nQuantity: ' + val('quantity') +
        '\n\n' + val('message')
      );
      if (status) status.textContent = T('form_open');
      window.location.href = 'mailto:hello@maisonvaler.com?subject=' + subject + '&body=' + body;
    });
  }

  /* ---------- Footer year ---------- */
  function setYear() {
    var y = document.querySelector('[data-year]');
    if (y) y.textContent = new Date().getFullYear();
  }

  /* ---------- Init ---------- */
  function init() {
    bindTheme();
    bindI18n();          // sets lang + dir before layout-sensitive work
    bindHeader(); bindDrawer(); bindReveal(); bindParallax();
    bindGalleries(); bindTitles(); bindFilter(); bindForm(); bindQuotePrefill(); setYear();
    requestAnimationFrame(function () { document.body.classList.add('load'); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
