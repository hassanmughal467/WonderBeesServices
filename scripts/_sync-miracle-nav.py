"""Sync main nav to Miracle-style IA (Home, Services x3, About, Contact, Join, Find)."""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent

nav_pages = r'''    <nav class="hidden flex-1 justify-end lg:flex lg:flex-wrap lg:items-center" aria-label="Primary">
      <a href="../index.html#hero" data-nav="home" class="nn-navlink px-3 py-2 text-nn-small">Home</a>
      <div class="nav-flyout-wrap relative">
        <button type="button" class="nn-navlink flex items-center gap-1 px-3 py-2 text-nn-small text-nn-secondary" aria-expanded="false" aria-haspopup="true">
          Services
          <svg class="h-3 w-3 opacity-70" fill="currentColor" viewBox="0 0 320 512" aria-hidden="true"><path d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"/></svg>
        </button>
        <div class="nav-flyout-panel absolute right-0 top-full z-50 w-56 pt-3 xl:left-0 xl:right-auto" role="menu">
          <div class="rounded-nn-lg bg-nn-blush py-2 shadow-nn-card ring-1 ring-nn-wash/50">
            <a href="our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
            <a href="pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call/Hotel</a>
            <a href="household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
          </div>
        </div>
      </div>
      <a href="about.html" data-nav="about" class="nn-navlink px-3 py-2 text-nn-small">About</a>
      <a href="../contact.html" data-nav="contact" class="nn-navlink px-3 py-2 text-nn-small">Contact</a>
      <a href="job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>
      <a href="apply-family.html" data-nav="apply-family" class="nav-apply-highlight nn-navlink px-3 py-2 text-nn-small font-medium">Find a Specialist</a>
    </nav>'''

mobile_pages = r'''  <div id="mobile-menu" class="mx-auto mt-2 hidden max-h-[85vh] max-w-nn overflow-y-auto rounded-nn-xl border border-nn-wash bg-nn-surface px-2 py-3 shadow-nn-card lg:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">
    <div class="space-y-1">
      <a href="../index.html#hero" data-nav="home" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Home</a>
      <div class="border-b border-nn-wash/80 pb-2">
        <button type="button" class="flex w-full items-center justify-between rounded-lg px-3 py-2 text-left text-sm font-medium text-nn-secondary hover:bg-nn-page" data-accordion-trigger aria-expanded="false" aria-controls="acc-families">
          Services <span class="text-nn-pink-soft" aria-hidden="true">+</span>
        </button>
        <div id="acc-families" class="hidden space-y-0.5 pl-2 pt-1">
          <a href="our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
          <a href="pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call/Hotel</a>
          <a href="household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
        </div>
      </div>
      <a href="about.html" data-nav="about" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">About</a>
      <a href="../contact.html" data-nav="contact" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Contact</a>
      <a href="job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>
      <a href="apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
    </div>
  </div>'''

mobile_blog = r'''      <div id="mobile-menu" class="mx-auto mt-2 hidden max-h-[85vh] max-w-nn overflow-y-auto rounded-nn-xl border border-nn-wash bg-nn-surface px-2 py-3 shadow-nn-card lg:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">
        <div class="space-y-1">
          <a href="../../index.html#hero" data-nav="home" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Home</a>
          <div class="border-b border-nn-wash/80 pb-2">
            <button type="button" class="flex w-full items-center justify-between rounded-lg px-3 py-2 text-left text-sm font-medium text-nn-secondary hover:bg-nn-page" data-accordion-trigger aria-expanded="false" aria-controls="acc-families">
              Services <span class="text-nn-pink-soft" aria-hidden="true">+</span>
            </button>
            <div id="acc-families" class="hidden space-y-0.5 pl-2 pt-1">
              <a href="../our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
              <a href="../pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call/Hotel</a>
              <a href="../household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
            </div>
          </div>
          <a href="../about.html" data-nav="about" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">About</a>
          <a href="../../contact.html" data-nav="contact" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Contact</a>
          <a href="../job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>
          <a href="../apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
        </div>
      </div>'''

nav_blog = r'''        <nav class="hidden flex-1 justify-end lg:flex lg:flex-wrap lg:items-center" aria-label="Primary">
          <a href="../../index.html#hero" data-nav="home" class="nn-navlink px-3 py-2 text-nn-small">Home</a>
          <div class="nav-flyout-wrap relative">
            <button type="button" class="nn-navlink flex items-center gap-1 px-3 py-2 text-nn-small text-nn-secondary" aria-expanded="false" aria-haspopup="true">
              Services
              <svg class="h-3 w-3 opacity-70" fill="currentColor" viewBox="0 0 320 512" aria-hidden="true"><path d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"/></svg>
            </button>
            <div class="nav-flyout-panel absolute right-0 top-full z-50 w-56 pt-3 xl:left-0 xl:right-auto" role="menu">
              <div class="rounded-nn-lg bg-nn-blush py-2 shadow-nn-card ring-1 ring-nn-wash/50">
                <a href="../our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
                <a href="../pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call/Hotel</a>
                <a href="../household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
              </div>
            </div>
          </div>
          <a href="../about.html" data-nav="about" class="nn-navlink px-3 py-2 text-nn-small">About</a>
          <a href="../../contact.html" data-nav="contact" class="nn-navlink px-3 py-2 text-nn-small">Contact</a>
          <a href="../job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>
          <a href="../apply-family.html" data-nav="apply-family" class="nav-apply-highlight nn-navlink px-3 py-2 text-nn-small font-medium">Find a Specialist</a>
        </nav>'''

pat_nav_pages = re.compile(
    r'<nav class="hidden flex-1 justify-end lg:flex" aria-label="Primary">.*?</nav>\s*<button type="button" class="inline-flex items-center justify-center rounded-md p-2 text-nn-secondary lg:hidden"',
    re.DOTALL,
)
pat_mobile_pages = re.compile(
    r'(?s)<div id="mobile-menu" class="mx-auto mt-2 hidden max-h-\[85vh\] max-w-nn overflow-y-auto rounded-nn-xl border border-nn-wash bg-nn-surface px-2 py-3 shadow-nn-card lg:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">.*\n  </div>\n</header>',
)

pat_nav_blog = re.compile(
    r'<nav class="hidden flex-1 justify-end lg:flex" aria-label="Primary">.*?</nav>\s*<button type="button" class="inline-flex items-center justify-center rounded-md p-2 text-nn-secondary lg:hidden"',
    re.DOTALL,
)
pat_mobile_blog = re.compile(
    r'(?s)<div id="mobile-menu" class="mx-auto mt-2 hidden max-h-\[85vh\] max-w-nn overflow-y-auto rounded-nn-xl border border-nn-wash bg-nn-surface px-2 py-3 shadow-nn-card lg:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">.*\n      </div>\n    </header>',
)


def patch_file(path: Path, nav: str, mobile: str, is_blog: bool) -> bool:
    t = path.read_text(encoding="utf-8")
    t2, n1 = pat_nav_pages.subn(
        nav + '\n    <button type="button" class="inline-flex items-center justify-center rounded-md p-2 text-nn-secondary lg:hidden"',
        t,
        count=1,
    ) if not is_blog else pat_nav_blog.subn(
        nav + '\n        <button type="button" class="inline-flex items-center justify-center rounded-md p-2 text-nn-secondary lg:hidden"',
        t,
        count=1,
    )
    if n1 != 1:
        return False
    t3, n2 = (
        pat_mobile_pages.subn(mobile + "\n</header>", t2, count=1)
        if not is_blog
        else pat_mobile_blog.subn(mobile + "\n    </header>", t2, count=1)
    )
    if n2 != 1:
        return False
    path.write_text(t3, encoding="utf-8")
    return True


contact_nav = r'''    <nav class="hidden flex-1 justify-end lg:flex lg:flex-wrap lg:items-center" aria-label="Primary">
      <a href="index.html#hero" data-nav="home" class="nn-navlink px-3 py-2 text-nn-small">Home</a>
      <div class="nav-flyout-wrap relative">
        <button type="button" class="nn-navlink flex items-center gap-1 px-3 py-2 text-nn-small text-nn-secondary" aria-expanded="false" aria-haspopup="true">
          Services
          <svg class="h-3 w-3 opacity-70" fill="currentColor" viewBox="0 0 320 512" aria-hidden="true"><path d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"/></svg>
        </button>
        <div class="nav-flyout-panel absolute right-0 top-full z-50 w-56 pt-3 xl:left-0 xl:right-auto" role="menu">
          <div class="rounded-nn-lg bg-nn-blush py-2 shadow-nn-card ring-1 ring-nn-wash/50">
            <a href="pages/our-nannies.html" data-nav="our-nannies" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Nanny Placement</a>
            <a href="pages/pricing.html" data-nav="pricing" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">On Call/Hotel</a>
            <a href="pages/household-managers.html" data-nav="household-managers" class="block px-4 py-2.5 text-sm text-nn-secondary hover:bg-primary/10" role="menuitem">Newborn Care Specialist NCS</a>
          </div>
        </div>
      </div>
      <a href="pages/about.html" data-nav="about" class="nn-navlink px-3 py-2 text-nn-small">About</a>
      <a href="contact.html" data-nav="contact" class="nn-navlink px-3 py-2 text-nn-small">Contact</a>
      <a href="pages/job-openings.html" data-nav="job-openings" class="nn-navlink px-3 py-2 text-nn-small">Join the Team</a>
      <a href="pages/apply-family.html" data-nav="apply-family" class="nav-apply-highlight nn-navlink px-3 py-2 text-nn-small font-medium">Find a Specialist</a>
    </nav>'''
contact_mobile = r'''  <div id="mobile-menu" class="mx-auto mt-2 hidden max-h-[85vh] max-w-nn overflow-y-auto rounded-nn-xl border border-nn-wash bg-nn-surface px-2 py-3 shadow-nn-card lg:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">
    <div class="space-y-1">
      <a href="index.html#hero" data-nav="home" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Home</a>
      <div class="border-b border-nn-wash/80 pb-2">
        <button type="button" class="flex w-full items-center justify-between rounded-lg px-3 py-2 text-left text-sm font-medium text-nn-secondary hover:bg-nn-page" data-accordion-trigger aria-expanded="false" aria-controls="acc-families">
          Services <span class="text-nn-pink-soft" aria-hidden="true">+</span>
        </button>
        <div id="acc-families" class="hidden space-y-0.5 pl-2 pt-1">
          <a href="pages/our-nannies.html" data-nav="our-nannies" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Nanny Placement</a>
          <a href="pages/pricing.html" data-nav="pricing" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">On Call/Hotel</a>
          <a href="pages/household-managers.html" data-nav="household-managers" class="block rounded-lg px-3 py-2 text-sm text-nn-body hover:bg-nn-page">Newborn Care Specialist NCS</a>
        </div>
      </div>
      <a href="pages/about.html" data-nav="about" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">About</a>
      <a href="contact.html" data-nav="contact" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Contact</a>
      <a href="pages/job-openings.html" data-nav="job-openings" class="block rounded-lg px-3 py-2 text-sm font-medium text-nn-secondary hover:bg-nn-page">Join the Team</a>
      <a href="pages/apply-family.html" data-nav="apply-family" class="block rounded-lg px-3 py-2 text-sm font-semibold text-nn-link hover:bg-nn-page">Find a Specialist</a>
    </div>
  </div>'''

ok = 0
for f in sorted(root.glob("pages/*.html")):
    if patch_file(f, nav_pages, mobile_pages, is_blog=False):
        ok += 1
        print("patched", f.name)
for f in sorted((root / "pages" / "blog").glob("*.html")):
    if patch_file(f, nav_blog, mobile_blog, is_blog=True):
        ok += 1
        print("patched blog", f.name)

c = root / "contact.html"
t = c.read_text(encoding="utf-8")
t, n1 = pat_nav_pages.subn(
    contact_nav + '\n    <button type="button" class="inline-flex items-center justify-center rounded-md p-2 text-nn-secondary lg:hidden"',
    t,
    count=1,
)
if n1 == 1:
    t, n2 = pat_mobile_pages.subn(contact_mobile + "\n</header>", t, count=1)
    if n2 == 1:
        c.write_text(t, encoding="utf-8")
        ok += 1
        print("patched contact.html")

print("done", ok)
