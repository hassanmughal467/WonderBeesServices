# -*- coding: utf-8 -*-
"""Unify header bar + nav with index.html (premium pill, same CTAs)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_INNER = (
    "mx-auto flex max-w-nn items-center justify-between gap-3 rounded-nn-xl "
    "border border-nn-wash bg-nn-surface/95 px-4 py-2 shadow-md backdrop-blur-sm "
    "sm:px-6 lg:gap-6"
)
NEW_INNER = (
    "nn-header-premium mx-auto flex max-w-nn items-center justify-between gap-3 "
    "rounded-nn-xl border border-nn-wash/70 bg-white/95 px-4 py-2.5 "
    "shadow-[0_8px_40px_-12px_rgba(25,27,65,0.12)] backdrop-blur-md sm:px-6 lg:gap-5"
)

OLD_NAV = 'hidden flex-1 justify-end lg:flex lg:flex-wrap lg:items-center"'
NEW_NAV = 'hidden flex-1 items-center justify-end gap-x-0.5 lg:flex lg:flex-wrap"'

SPAN_FIND_BLOG = (
    '<a href="../apply-family.html" data-nav="apply-family" class="nav-apply-highlight nn-navlink">'
    '<span class="nav-apply-highlight__title">Find A Specialist</span>'
    '<span class="nav-apply-highlight__sub">Start Now</span></a>'
)
SPAN_FIND_PAGES = (
    '<a href="apply-family.html" data-nav="apply-family" class="nav-apply-highlight nn-navlink">'
    '<span class="nav-apply-highlight__title">Find A Specialist</span>'
    '<span class="nav-apply-highlight__sub">Start Now</span></a>'
)

DESK_BLOG_FIND = (
    '<a\n            href="../apply-family.html"\n            data-nav="apply-family"\n            '
    'class="ml-2 inline-flex items-center justify-center rounded-nn bg-nn-teal px-4 py-2 '
    'text-sm font-semibold text-white shadow-md shadow-nn-teal/30 transition '
    'hover:bg-secondary hover:brightness-[0.97] focus:outline-none focus-visible:ring-2 '
    'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n            >Find a Specialist</a\n          >'
)
MOB_BLOG_FIND = (
    '<a\n            href="../apply-family.html"\n            data-nav="apply-family"\n            '
    'class="block rounded-lg bg-nn-teal px-3 py-2.5 text-center text-sm font-semibold text-white '
    'shadow-sm hover:brightness-95"\n            >Find a Specialist</a\n          >'
)

DESK_PAGES_SPAN_FIND = (
    '<a\n        href="apply-family.html"\n        data-nav="apply-family"\n        '
    'class="ml-2 inline-flex items-center justify-center rounded-nn bg-nn-teal px-4 py-2 '
    'text-sm font-semibold text-white shadow-md shadow-nn-teal/30 transition '
    'hover:bg-secondary hover:brightness-[0.97] focus:outline-none focus-visible:ring-2 '
    'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n        >Find a Specialist</a\n      >'
)
MOB_PAGES_SPAN_FIND = (
    '<a\n            href="apply-family.html"\n            data-nav="apply-family"\n            '
    'class="block rounded-lg bg-nn-teal px-3 py-2.5 text-center text-sm font-semibold text-white '
    'shadow-sm hover:brightness-95"\n            >Find a Specialist</a\n          >'
)


def patch_span_find_pages(text: str) -> str:
    if SPAN_FIND_PAGES not in text:
        return text
    text, n = re.subn(re.escape(SPAN_FIND_PAGES), DESK_PAGES_SPAN_FIND, text, count=1)
    if n:
        text, _ = re.subn(re.escape(SPAN_FIND_PAGES), MOB_PAGES_SPAN_FIND, text, count=1)
    return text


def patch_blog_nav(text: str) -> str:
    if SPAN_FIND_BLOG not in text:
        return text
    text, n = re.subn(re.escape(SPAN_FIND_BLOG), DESK_BLOG_FIND, text, count=1)
    if n:
        text, _ = re.subn(re.escape(SPAN_FIND_BLOG), MOB_BLOG_FIND, text, count=1)
    return text


def patch_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel.endswith("index.html") or rel.endswith("apply-family.html"):
        return False
    raw = path.read_text(encoding="utf-8")
    if 'id="header-inner"' not in raw:
        return False
    text = raw
    text = text.replace(OLD_INNER, NEW_INNER)
    text = text.replace(OLD_NAV, NEW_NAV)
    for o, n in [
        ('class="nn-navlink px-3 py-2 text-nn-small">Home', 'class="nn-navlink px-3 py-2 text-[0.9375rem] font-medium tracking-tight text-nn-secondary">Home'),
        ('class="nn-navlink flex items-center gap-1 px-3 py-2 text-nn-small text-nn-secondary"', 'class="nn-navlink flex items-center gap-1 px-3 py-2 text-[0.9375rem] font-medium tracking-tight text-nn-secondary"'),
        ('class="nn-navlink px-3 py-2 text-nn-small">About', 'class="nn-navlink px-3 py-2 text-[0.9375rem] font-medium tracking-tight text-nn-secondary">About'),
        ('class="nn-navlink px-3 py-2 text-nn-small">Contact', 'class="nn-navlink px-3 py-2 text-[0.9375rem] font-medium tracking-tight text-nn-secondary">Contact'),
    ]:
        text = text.replace(o, n)

    if "pages/blog/" in rel:
        text = text.replace(
            '<a href="../job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>',
            '<a\n            href="../job-openings.html"\n            data-nav="job-openings"\n            '
            'class="ml-1 inline-flex items-center justify-center rounded-nn border-2 border-nn-teal '
            'bg-transparent px-4 py-2 text-sm font-semibold text-nn-teal transition '
            'hover:bg-nn-teal/[0.08] focus:outline-none focus-visible:ring-2 '
            'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n            >Join the Team</a\n          >',
        )
        text = patch_blog_nav(text)
        text = text.replace(
            '<a href="../job-openings.html" data-nav="job-openings" '
            'class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>',
            '<a\n            href="../job-openings.html"\n            data-nav="job-openings"\n            '
            'class="block rounded-lg border-2 border-nn-teal px-3 py-2.5 text-center text-sm font-semibold '
            'text-nn-teal hover:bg-nn-teal/[0.06]"\n            >Join the Team</a\n          >',
        )
    elif rel == "contact.html":
        text = text.replace(
            '<a href="pages/job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>',
            '<a\n            href="pages/job-openings.html"\n            data-nav="job-openings"\n            '
            'class="ml-1 inline-flex items-center justify-center rounded-nn border-2 border-nn-teal '
            'bg-transparent px-4 py-2 text-sm font-semibold text-nn-teal transition '
            'hover:bg-nn-teal/[0.08] focus:outline-none focus-visible:ring-2 '
            'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n            >Join the Team</a\n          >',
        )
        text = text.replace(
            '<a href="pages/apply-family.html" data-nav="apply-family" '
            'class="nav-apply-highlight nn-navlink px-3 py-2 text-nn-small font-medium">Find a Specialist</a>',
            '<a\n            href="pages/apply-family.html"\n            data-nav="apply-family"\n            '
            'class="ml-2 inline-flex items-center justify-center rounded-nn bg-nn-teal px-4 py-2 '
            'text-sm font-semibold text-white shadow-md shadow-nn-teal/30 transition '
            'hover:bg-secondary hover:brightness-[0.97] focus:outline-none focus-visible:ring-2 '
            'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n            >Find a Specialist</a\n          >',
        )
        text = text.replace(
            '<a href="pages/job-openings.html" data-nav="job-openings" '
            'class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>',
            '<a\n            href="pages/job-openings.html"\n            data-nav="job-openings"\n            '
            'class="block rounded-lg border-2 border-nn-teal px-3 py-2.5 text-center text-sm font-semibold '
            'text-nn-teal hover:bg-nn-teal/[0.06]"\n            >Join the Team</a\n          >',
        )
        text = text.replace(
            '<a href="pages/apply-family.html" data-nav="apply-family" '
            'class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>',
            '<a\n            href="pages/apply-family.html"\n            data-nav="apply-family"\n            '
            'class="block rounded-lg bg-nn-teal px-3 py-2.5 text-center text-sm font-semibold text-white '
            'shadow-sm hover:brightness-95"\n            >Find a Specialist</a\n          >',
        )
    else:
        text = text.replace(
            '<a href="job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>',
            '<a\n        href="job-openings.html"\n        data-nav="job-openings"\n        '
            'class="ml-1 inline-flex items-center justify-center rounded-nn border-2 border-nn-teal '
            'bg-transparent px-4 py-2 text-sm font-semibold text-nn-teal transition '
            'hover:bg-nn-teal/[0.08] focus:outline-none focus-visible:ring-2 '
            'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n        >Join the Team</a\n      >',
        )
        text = text.replace(
            '<a href="apply-family.html" data-nav="apply-family" '
            'class="nav-apply-highlight nn-navlink px-3 py-2 text-nn-small font-medium">Find a Specialist</a>',
            '<a\n        href="apply-family.html"\n        data-nav="apply-family"\n        '
            'class="ml-2 inline-flex items-center justify-center rounded-nn bg-nn-teal px-4 py-2 '
            'text-sm font-semibold text-white shadow-md shadow-nn-teal/30 transition '
            'hover:bg-secondary hover:brightness-[0.97] focus:outline-none focus-visible:ring-2 '
            'focus-visible:ring-nn-teal focus-visible:ring-offset-2"\n        >Find a Specialist</a\n      >',
        )
        text = text.replace(
            '<a href="job-openings.html" data-nav="job-openings" '
            'class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>',
            '<a\n            href="job-openings.html"\n            data-nav="job-openings"\n            '
            'class="block rounded-lg border-2 border-nn-teal px-3 py-2.5 text-center text-sm font-semibold '
            'text-nn-teal hover:bg-nn-teal/[0.06]"\n            >Join the Team</a\n          >',
        )
        text = text.replace(
            '<a href="apply-family.html" data-nav="apply-family" '
            'class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>',
            '<a\n            href="apply-family.html"\n            data-nav="apply-family"\n            '
            'class="block rounded-lg bg-nn-teal px-3 py-2.5 text-center text-sm font-semibold text-white '
            'shadow-sm hover:brightness-95"\n            >Find a Specialist</a\n          >',
        )
        text = patch_span_find_pages(text)

    if text != raw:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in str(path):
            continue
        if patch_file(path):
            print(path.relative_to(ROOT))
            n += 1
    print("Updated", n, "files")


if __name__ == "__main__":
    main()