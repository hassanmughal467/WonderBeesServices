"""Inject data-nav after href on primary nav anchors (idempotent)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Full href attribute as in HTML, then data-nav value
SPEC = [
    ('href="pages/our-process.html"', "our-process"),
    ('href="pages/our-nannies.html"', "our-nannies"),
    ('href="pages/household-managers.html"', "household-managers"),
    ('href="pages/pricing.html"', "pricing"),
    ('href="pages/family-faq.html"', "family-faq"),
    ('href="pages/apply-family.html"', "apply-family"),
    ('href="pages/job-openings.html"', "job-openings"),
    ('href="pages/why-nannies.html"', "why-nannies"),
    ('href="pages/apply-nanny.html"', "apply-nanny"),
    ('href="pages/about.html"', "about"),
    ('href="pages/blog.html"', "blog"),
    ('href="our-process.html"', "our-process"),
    ('href="our-nannies.html"', "our-nannies"),
    ('href="household-managers.html"', "household-managers"),
    ('href="pricing.html"', "pricing"),
    ('href="family-faq.html"', "family-faq"),
    ('href="apply-family.html"', "apply-family"),
    ('href="job-openings.html"', "job-openings"),
    ('href="why-nannies.html"', "why-nannies"),
    ('href="apply-nanny.html"', "apply-nanny"),
    ('href="about.html"', "about"),
    ('href="blog.html"', "blog"),
    ('href="../contact.html"', "contact"),
    ('href="contact.html"', "contact"),
]


def patch(text: str) -> str:
    for href_attr, nav in SPEC:
        escaped = re.escape(href_attr)
        pat = re.compile(escaped + r"(?!\s+data-nav=)")
        repl = f'{href_attr} data-nav="{nav}"'
        text = pat.sub(repl, text)
    return text


def main() -> None:
    paths = [ROOT / "index.html", ROOT / "contact.html"] + sorted((ROOT / "pages").glob("*.html"))
    for path in paths:
        raw = path.read_text(encoding="utf-8")
        new = patch(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            print("patched", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
