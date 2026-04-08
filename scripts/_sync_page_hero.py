"""
Replace light gradient page heroes with .nn-page-hero (same photo + overlay as home).
Run from site root: python scripts/_sync_page_hero.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OUTER_ABOUT = """      <div class="relative overflow-hidden border-b border-nn-wash/40 bg-hero-gradient">
        <div class="pointer-events-none absolute bottom-0 right-0 h-36 w-36 bg-nn-flowers opacity-40 sm:h-48 sm:w-48" aria-hidden="true"></div>
        <div class="relative mx-auto max-w-nn px-4 py-12 sm:px-6 sm:pb-14 sm:pt-16 lg:py-16">"""

OUTER_STANDARD = """      <div class="border-b border-nn-wash/40 bg-hero-gradient">
        <div class="mx-auto max-w-nn px-4 py-12 sm:px-6 sm:pb-14 sm:pt-16 lg:py-16">"""

OUTER_BLOG = """      <div class="border-b border-nn-wash/40 bg-hero-gradient">
        <div class="mx-auto max-w-nn px-4 py-10 sm:px-6 sm:py-14 lg:py-16">"""

OUTER_CONTACT = """      <div class="border-b border-nn-wash/40 bg-hero-gradient">
        <div class="mx-auto max-w-nn px-4 py-12 text-center sm:px-6 sm:pb-14 sm:pt-16 lg:py-16">"""

INNER_NEW = """      <div class="nn-page-hero relative scroll-mt-24 sm:scroll-mt-28" aria-labelledby="page-hero-heading">
        <div class="relative z-[1] mx-auto max-w-nn px-4 py-12 sm:px-6 sm:pb-14 sm:pt-16 lg:py-16">"""

INNER_NEW_CENTER = """      <div class="nn-page-hero relative scroll-mt-24 sm:scroll-mt-28" aria-labelledby="page-hero-heading">
        <div class="relative z-[1] mx-auto max-w-nn px-4 py-12 text-center sm:px-6 sm:pb-14 sm:pt-16 lg:py-16">"""

APPLY_FAMILY_OLD = """      <!-- Find a specialist hero -->
      <div class="nn-find-specialist-hero relative overflow-hidden border-b border-white/10">
        <div class="pointer-events-none absolute inset-0 bg-[radial-gradient(1200px_480px_at_50%_-20%,rgba(98,172,223,0.35),transparent),linear-gradient(165deg,#191b41_0%,#2a2d5e_50%,#191b41_100%)]" aria-hidden="true"></div>
        <div class="pointer-events-none absolute inset-0 bg-[url('https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=2000&q=70')] bg-cover bg-[50%_38%] opacity-[0.12] mix-blend-luminosity" aria-hidden="true"></div>
        <div class="relative mx-auto max-w-[1600px] px-4 py-14 text-center sm:px-8 sm:py-16 lg:px-12 lg:py-20">
          <p class="text-xs font-semibold uppercase tracking-[0.28em] text-nn-teal-light">Find a specialist</p>
          <h1 class="nn-find-specialist-hero__title mt-5 font-display text-3xl font-light leading-tight text-white sm:text-4xl sm:leading-tight lg:text-[2.75rem]">Let&rsquo;s find your specialist today</h1>
          <p class="mx-auto mt-4 max-w-2xl font-display text-lg font-medium uppercase tracking-[0.18em] text-white/90 sm:text-xl sm:tracking-[0.22em]">Find a Specialist</p>
          <p class="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-white/82 sm:text-lg">
            Thank you for your interest in working with WonderBees Services. Start with the application below and we will get back to you to schedule an interview and walk through the best options for your family.
          </p>
        </div>
      </div>"""

APPLY_FAMILY_NEW = """      <div class="nn-page-hero relative scroll-mt-24 sm:scroll-mt-28" aria-labelledby="page-hero-heading">
        <div class="relative z-[1] mx-auto max-w-nn px-4 py-14 text-center sm:px-6 sm:py-16 lg:py-20">
          <p class="text-xs font-semibold uppercase tracking-[0.28em] text-nn-teal-light">Find a specialist</p>
          <h1 id="page-hero-heading" class="nn-hero-premium__title mt-5 text-3xl font-semibold leading-tight tracking-[-0.02em] text-white sm:text-4xl lg:text-[2.75rem]">Let&rsquo;s find your specialist today</h1>
          <p class="mx-auto mt-4 max-w-2xl font-display text-base font-semibold uppercase tracking-[0.2em] text-white/95 sm:text-lg sm:tracking-[0.28em]">WonderBees Services</p>
          <p class="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-white/88 sm:text-lg">
            Thank you for your interest in working with WonderBees Services. Start with the application below and we will get back to you to schedule an interview and walk through the best options for your family.
          </p>
        </div>
      </div>"""


def patch_blog_breadcrumb(html: str) -> str:
    html = html.replace(
        '<nav class="text-xs font-medium text-nn-link" aria-label="Breadcrumb">',
        '<nav class="text-xs font-medium text-white/80" aria-label="Breadcrumb">',
    )
    html = re.sub(
        r'(<li><a href="[^"]+" class=")hover:underline(")',
        r"\1text-white/90 underline-offset-2 hover:text-white hover:underline\2",
        html,
        count=1,
    )
    html = html.replace(
        '<li class="text-nn-body">',
        '<li class="text-white/65">',
        1,
    )
    return html


def apply_structure(path: Path, text: str) -> str:
    if APPLY_FAMILY_OLD in text:
        text = text.replace(APPLY_FAMILY_OLD, APPLY_FAMILY_NEW)
    if OUTER_ABOUT in text:
        text = text.replace(OUTER_ABOUT, INNER_NEW)
    elif path.name == "contact.html" and OUTER_CONTACT in text:
        text = text.replace(OUTER_CONTACT, INNER_NEW_CENTER)
    elif OUTER_BLOG in text and path.parent.name == "blog" and path.name != "blog.html":
        text = text.replace(OUTER_BLOG, INNER_NEW)
    elif OUTER_STANDARD in text:
        text = text.replace(OUTER_STANDARD, INNER_NEW)
    return text


def typography_blog_post(text: str) -> str:
    text = patch_blog_breadcrumb(text)
    text = text.replace(
        'text-xs font-semibold uppercase tracking-[0.2em] text-nn-link">',
        'text-xs font-semibold uppercase tracking-[0.28em] text-nn-teal-light">',
        1,
    )
    text = text.replace(
        'class="mt-3 max-w-4xl font-sans text-3xl font-light leading-tight text-nn-secondary sm:text-[2.35rem]"',
        'id="page-hero-heading" class="nn-page-hero__title-blog mt-3 max-w-4xl text-3xl font-semibold leading-tight tracking-[-0.02em] text-white sm:text-[2.35rem]"',
        1,
    )
    text = text.replace(
        'class="mt-4 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-nn-body"',
        'class="mt-4 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-white/75"',
        1,
    )
    text = text.replace(
        '<span class="text-nn-wash" aria-hidden="true">·</span>',
        '<span class="text-white/45" aria-hidden="true">·</span>',
        1,
    )
    return text


def typography_about(text: str) -> str:
    text = text.replace(
        'text-xs font-semibold uppercase tracking-[0.2em] text-nn-link">',
        'text-xs font-semibold uppercase tracking-[0.28em] text-nn-teal-light">',
        1,
    )
    text = text.replace(
        "<h1 class=\"mt-4 font-display text-3xl font-light leading-tight text-nn-secondary text-balance sm:text-[2.35rem] sm:leading-tight\">WonderBees Services</h1>",
        '<h1 id="page-hero-heading" class="nn-hero-premium__title mt-4 text-3xl font-semibold uppercase leading-tight tracking-[0.02em] text-white text-balance sm:text-4xl sm:tracking-[0.03em]">WonderBees <span class="text-nn-teal-light">Services</span></h1>',
        1,
    )
    text = text.replace(
        'class="mt-5 max-w-3xl text-base text-nn-body sm:text-lg"',
        'class="mt-5 max-w-3xl text-base leading-relaxed text-white/88 sm:text-lg"',
        1,
    )
    return text


def typography_standard(text: str) -> str:
    text = text.replace(
        'text-xs font-semibold uppercase tracking-[0.2em] text-nn-link">',
        'text-xs font-semibold uppercase tracking-[0.28em] text-nn-teal-light">',
        1,
    )
    if 'id="page-hero-heading"' not in text:
        text = text.replace(
            'class="mt-4 font-sans text-3xl font-light text-nn-secondary sm:text-[2.35rem] sm:leading-tight"',
            'id="page-hero-heading" class="nn-hero-premium__title mt-4 text-3xl font-semibold uppercase leading-tight tracking-[0.02em] text-white sm:text-[2.35rem] sm:leading-tight sm:tracking-[0.03em]"',
            1,
        )
    for old, new in (
        (
            'class="mt-5 max-w-3xl text-lg text-nn-body"',
            'class="mt-5 max-w-3xl text-lg leading-relaxed text-white/88"',
        ),
        (
            'class="mt-5 max-w-3xl text-base text-nn-body sm:text-lg"',
            'class="mt-5 max-w-3xl text-base leading-relaxed text-white/88 sm:text-lg"',
        ),
        (
            'class="mx-auto mt-5 max-w-2xl text-lg text-nn-body"',
            'class="mx-auto mt-5 max-w-2xl text-lg leading-relaxed text-white/88"',
        ),
    ):
        text = text.replace(old, new, 1)
    return text


def main() -> None:
    updated = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        text = apply_structure(path, text)
        if "nn-page-hero" not in text or text == orig:
            if text != orig:
                path.write_text(text, encoding="utf-8")
                updated += 1
            continue

        rel = path.relative_to(ROOT)
        is_blog_post = path.parent.name == "blog" and path.name != "blog.html"
        is_apply_family = path.name == "apply-family.html"

        if is_apply_family:
            pass  # hero copy already complete in APPLY_FAMILY_NEW
        elif is_blog_post:
            text = typography_blog_post(text)
        elif path.name == "about.html":
            text = typography_about(text)
        else:
            text = typography_standard(text)

        if text != orig:
            path.write_text(text, encoding="utf-8")
            updated += 1
            print(rel)

    print(f"Updated {updated} file(s).")


if __name__ == "__main__":
    main()
