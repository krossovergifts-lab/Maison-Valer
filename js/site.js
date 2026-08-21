/* =========================================================
   MAISON VALÉR — site behaviours
   ========================================================= */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Theme ---------- */
  function storedTheme() {
    try { return localStorage.getItem('mv-theme'); } catch (e) { return null; }
  }
  function saveTheme(t) {
    try { localStorage.setItem('mv-theme', t); } catch (e) {}
  }
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', t === 'light' ? '#f2ebde' : '#14100c');
  }
  var initial = storedTheme() ||
    (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  applyTheme(initial);

  function bindTheme() {
    var toggle = document.querySelector('.theme-toggle');
    if (!toggle) return;
    toggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next); saveTheme(next);
    });
  }

  /* ---------- Header scroll state ---------- */
  function bindHeader() {
    var head = document.querySelector('.site-head');
    if (!head) return;
    var onScroll = function () {
      if (window.scrollY > 24) head.classList.add('scrolled');
      else head.classList.remove('scrolled');
    };
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
    burger.addEventListener('click', function () {
      toggle(!drawer.classList.contains('open'));
    });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { toggle(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) toggle(false);
    });
  }

  /* ---------- Scroll reveal ---------- */
  function bindReveal() {
    var els = document.querySelectorAll('.reveal, .img-reveal');
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

  /* ---------- Contact form (client-side) ---------- */
  function bindForm() {
    var form = document.querySelector('.form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('[name="name"]');
      var email = form.querySelector('[name="email"]');
      if (!name.value.trim() || !email.value.trim()) {
        if (status) status.textContent = 'Please add your name and email so we can reply.';
        return;
      }
      var subject = encodeURIComponent('Maison Valér — Enquiry from ' + name.value.trim());
      var body = encodeURIComponent(
        'Name: ' + name.value.trim() +
        '\nEmail: ' + email.value.trim() +
        '\nCompany: ' + (form.querySelector('[name="company"]') || {}).value +
        '\nInterest: ' + (form.querySelector('[name="interest"]') || {}).value +
        '\nQuantity: ' + (form.querySelector('[name="quantity"]') || {}).value +
        '\n\n' + (form.querySelector('[name="message"]') || {}).value
      );
      if (status) status.textContent = 'Opening your email client to send this enquiry…';
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
    bindTheme(); bindHeader(); bindDrawer(); bindReveal();
    bindParallax(); bindFilter(); bindForm(); setYear();
    requestAnimationFrame(function () { document.body.classList.add('load'); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
