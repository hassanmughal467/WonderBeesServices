/**
 * WonderBees Services — UI: nav, mobile menu, scroll spy, reveals, testimonial slider, contact form
 */
(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }
  function $$(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function setYear() {
    var el = $("#year");
    if (el) el.textContent = String(new Date().getFullYear());
  }

  /* ---------- Mobile menu ---------- */
  function initMobileMenu() {
    var toggle = $("#menu-toggle");
    var panel = $("#mobile-menu");
    if (!toggle || !panel) return;

    function close() {
      panel.classList.add("hidden");
      toggle.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    }

    function open() {
      panel.classList.remove("hidden");
      toggle.setAttribute("aria-expanded", "true");
      document.body.style.overflow = "hidden";
    }

    toggle.addEventListener("click", function () {
      if (panel.classList.contains("hidden")) open();
      else close();
    });

    panel.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", close);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });
  }

  /* ---------- Scroll reveal ---------- */
  function initReveal() {
    if (prefersReducedMotion) {
      $$(".reveal-on-scroll").forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    $$(".reveal-on-scroll").forEach(function (el) {
      io.observe(el);
    });
  }

  /* ---------- Current page highlight (dropdown site model) ---------- */
  function initScrollSpy() {
    var page = document.body.getAttribute("data-page");
    highlightPageNav(page);
  }

  function highlightPageNav(page) {
    $$("[data-nav]").forEach(function (el) {
      el.classList.remove("is-active", "font-semibold");
    });
    if (!page || page === "home") return;
    $$('[data-nav="' + page + '"]').forEach(function (el) {
      /* Solid teal CTAs use white text; .is-active would force accent color and hide the label */
      if (el.classList.contains("bg-nn-teal")) return;
      el.classList.add("is-active", "font-semibold");
    });
  }

  /* ---------- reCAPTCHA v3 (site-wide badge + contact token) ---------- */
  function recaptchaConfigured() {
    var api = window.WonderbeeServicesAPI;
    if (!api || !api.API_CONFIG) return false;
    var k = api.API_CONFIG.recaptchaSiteKey || "";
    if (!k || k.indexOf("YOUR_RECAPTCHA") !== -1) return false;
    return true;
  }

  function initRecaptchaScript() {
    if (!recaptchaConfigured()) return;
    if (document.querySelector("script[data-site-recaptcha-v3]")) return;
    var k = window.WonderbeeServicesAPI.API_CONFIG.recaptchaSiteKey;
    var s = document.createElement("script");
    s.src = "https://www.google.com/recaptcha/api.js?render=" + encodeURIComponent(k);
    s.async = true;
    s.defer = true;
    s.setAttribute("data-site-recaptcha-v3", "1");
    document.head.appendChild(s);
  }

  /* ---------- Mega nav (mobile accordion + click-outside desktop) ---------- */
  function initMegaNav() {
    /* Mobile accordions */
    $$("[data-accordion-trigger]").forEach(function (btn) {
      var id = btn.getAttribute("aria-controls");
      var panel = id && document.getElementById(id);
      if (!panel) return;
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        panel.classList.toggle("hidden", open);
      });
    });

  }

  /* ---------- Cookie banner ---------- */
  function initCookieBanner() {
    var banner = $("#cookie-banner");
    if (!banner) return;
    try {
      if (window.localStorage.getItem("wonderbeeServicesCookieOk")) {
        banner.classList.add("hidden");
        return;
      }
    } catch (err) {
      /* ignore */
    }
    banner.classList.remove("hidden");
    var ok = $("#cookie-accept");
    if (ok)
      ok.addEventListener("click", function () {
        try {
          window.localStorage.setItem("wonderbeeServicesCookieOk", "1");
        } catch (err2) {
          /* ignore */
        }
        banner.classList.add("hidden");
      });
  }

  /* ---------- Carousels (any [data-carousel]) ---------- */
  function initCarousels() {
    $$("[data-carousel]").forEach(function (root) {
      var track = $(".carousel-track", root);
      if (!track) return;
      var slides = $$(".carousel-slide", track);
      var prev = $('[data-carousel-prev]', root);
      var next = $('[data-carousel-next]', root);
      var dots = $$("[data-carousel-dot]", root);
      var i = 0;
      var n = slides.length;
      if (n < 1) return;

      function go(index) {
        i = (index + n) % n;
        track.style.transform = "translateX(-" + (i * 100) / n + "%)";
        dots.forEach(function (d, j) {
          d.classList.toggle("bg-nn-link", j === i);
          d.classList.toggle("bg-nn-wash", j !== i);
          d.setAttribute("aria-selected", j === i ? "true" : "false");
        });
      }

      if (prev) prev.addEventListener("click", function () { go(i - 1); });
      if (next) next.addEventListener("click", function () { go(i + 1); });
      dots.forEach(function (d, j) {
        d.addEventListener("click", function () { go(j); });
      });

      if (prefersReducedMotion || n < 2) return;
      var ms = parseInt(root.getAttribute("data-carousel-interval") || "6000", 10);
      var autoplay = setInterval(function () { go(i + 1); }, ms);
      root.addEventListener("mouseenter", function () { clearInterval(autoplay); });
      root.addEventListener("mouseleave", function () {
        autoplay = setInterval(function () { go(i + 1); }, ms);
      });
    });
  }

  /* ---------- Testimonial slider (legacy id) ---------- */
  function initTestimonialSlider() {
    var root = $("#testimonial-slider");
    if (!root) return;

    var track = $(".testimonial-track", root);
    var slides = $$(".testimonial-slide", track);
    var prev = $('[data-slider="prev"]', root);
    var next = $('[data-slider="next"]', root);
    var dots = $$("[data-slider-dot]", root);
    var i = 0;
    var n = slides.length;
    if (n < 2) return;

    function go(index) {
      i = (index + n) % n;
      /* Percent is relative to the track width; each slide is 1/n of the track */
      track.style.transform = "translateX(-" + (i * 100) / n + "%)";
      dots.forEach(function (d, j) {
        d.classList.toggle("bg-nn-sage", j === i);
        d.classList.toggle("bg-nn-wash", j !== i);
        d.setAttribute("aria-selected", j === i ? "true" : "false");
      });
    }

    if (prev) prev.addEventListener("click", function () { go(i - 1); });
    if (next) next.addEventListener("click", function () { go(i + 1); });
    dots.forEach(function (d, j) {
      d.addEventListener("click", function () { go(j); });
    });

    if (prefersReducedMotion) return;

    var autoplay = setInterval(function () { go(i + 1); }, 7000);
    root.addEventListener("mouseenter", function () { clearInterval(autoplay); });
    root.addEventListener("mouseleave", function () {
      autoplay = setInterval(function () { go(i + 1); }, 7000);
    });
  }

  /**
   * @param {HTMLFormElement} form
   * @param {{ btn?: HTMLButtonElement | null, loading?: HTMLElement | null, ok?: HTMLElement | null, err?: HTMLElement | null }} el
   * @param {string} recaptchaAction
   */
  function bindFormspreeSubmit(form, el, recaptchaAction) {
    var btn = el.btn;
    var loading = el.loading;
    var ok = el.ok;
    var err = el.err;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!window.WonderbeeServicesAPI) return;

      if (form.id === "apply-family-form") {
        var em = form.querySelector("#apply-family-email");
        var emConfirm = form.querySelector("#apply-family-email-confirm");
        if (em && emConfirm && em.value.trim() !== emConfirm.value.trim()) {
          if (err) {
            err.textContent = "Email and confirm email must match.";
            err.classList.remove("hidden");
          }
          return;
        }
      }

      var endpoint = window.WonderbeeServicesAPI.API_CONFIG.formspree;
      if (!endpoint || endpoint.indexOf("YOUR_FORM_ID") !== -1) {
        if (err) {
          err.textContent = "Please set your Formspree endpoint in js/api.js (replace YOUR_FORM_ID).";
          err.classList.remove("hidden");
        }
        return;
      }

      if (loading) loading.classList.remove("hidden");
      if (ok) ok.classList.add("hidden");
      if (err) err.classList.add("hidden");
      if (btn) btn.disabled = true;

      var fd = new FormData(form);
      var siteKey = window.WonderbeeServicesAPI.API_CONFIG.recaptchaSiteKey;

      function postForm() {
        window.WonderbeeServicesAPI
          .submitContactViaFormspree(fd)
          .then(function (res) {
            if (res.ok) {
              form.reset();
              if (ok) ok.classList.remove("hidden");
            } else {
              return res
                .json()
                .catch(function () {
                  return {};
                })
                .then(function (data) {
                  throw new Error((data && data.error) || "Submit failed");
                });
            }
          })
          .catch(function () {
            if (err) {
              err.textContent = "Something went wrong. Please try again or call us directly.";
              err.classList.remove("hidden");
            }
          })
          .finally(function () {
            if (loading) loading.classList.add("hidden");
            if (btn) btn.disabled = false;
          });
      }

      if (recaptchaConfigured() && window.grecaptcha && typeof window.grecaptcha.execute === "function") {
        window.grecaptcha.ready(function () {
          window.grecaptcha
            .execute(siteKey, { action: recaptchaAction })
            .then(function (token) {
              fd.set("g-recaptcha-response", token);
              postForm();
            })
            .catch(function () {
              if (err) {
                err.textContent = "reCAPTCHA could not be verified. Please refresh and try again.";
                err.classList.remove("hidden");
              }
              if (loading) loading.classList.add("hidden");
              if (btn) btn.disabled = false;
            });
        });
      } else {
        postForm();
      }
    });
  }

  function attachFormspreeForm(form, elements, recaptchaAction) {
    if (!form) return;
    var tries = 0;
    function attach() {
      if (window.WonderbeeServicesAPI) {
        bindFormspreeSubmit(form, elements, recaptchaAction);
        return;
      }
      if (tries++ < 80) setTimeout(attach, 30);
    }
    attach();
  }

  /* ---------- Contact form (contact.html) ---------- */
  function initContactForm() {
    attachFormspreeForm(
      $("#contact-form"),
      {
        btn: $("#contact-submit"),
        loading: $("#form-loading"),
        ok: $("#form-success"),
        err: $("#form-error"),
      },
      "contact"
    );
  }

  /* ---------- Apply Now — same layout as contact (apply-nanny / apply-family) ---------- */
  function initApplyForms() {
    attachFormspreeForm(
      $("#apply-nanny-form"),
      {
        btn: $("#apply-nanny-submit"),
        loading: $("#apply-nanny-form-loading"),
        ok: $("#apply-nanny-form-success"),
        err: $("#apply-nanny-form-error"),
      },
      "apply_nanny"
    );
    attachFormspreeForm(
      $("#apply-family-form"),
      {
        btn: $("#apply-family-submit"),
        loading: $("#apply-family-form-loading"),
        ok: $("#apply-family-form-success"),
        err: $("#apply-family-form-error"),
      },
      "apply_family"
    );
  }

  /* ---------- Job openings — candidate interest (job-openings.html) ---------- */
  function initJobInterestForm() {
    var form = $("#job-interest-form");
    if (!form) return;

    var btn = $("#job-interest-submit");
    var loading = $("#job-form-loading");
    var ok = $("#job-form-success");
    var err = $("#job-form-error");

    var tries = 0;
    function attach() {
      if (window.WonderbeeServicesAPI) {
        bindSubmit();
        return;
      }
      if (tries++ < 80) setTimeout(attach, 30);
    }

    function bindSubmit() {
      bindFormspreeSubmit(
        form,
        { btn: btn, loading: loading, ok: ok, err: err },
        "job_interest"
      );
    }

    attach();
  }

  /* ---------- Header — reference-style solid bar + stronger shadow on scroll ---------- */
  function initHeaderScroll() {
    var header = $("#site-header");
    if (!header) return;
    function onScroll() {
      if (window.scrollY > 24) header.classList.add("is-scrolled");
      else header.classList.remove("is-scrolled");
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  document.addEventListener("DOMContentLoaded", function () {
    setYear();
    initRecaptchaScript();
    initMobileMenu();
    initMegaNav();
    initReveal();
    initScrollSpy();
    initCarousels();
    initTestimonialSlider();
    initContactForm();
    initApplyForms();
    initJobInterestForm();
    initHeaderScroll();
    initCookieBanner();
  });
})();
