"""Add reveal-on-scroll to main content white cards (idempotent)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = '<div class="rounded-nn-2xl bg-white p-8 shadow-nn'
NEW = '<div class="reveal-on-scroll rounded-nn-2xl bg-white p-8 shadow-nn'

for path in sorted((ROOT / "pages").glob("*.html")) + [ROOT / "contact.html"]:
    t = path.read_text(encoding="utf-8")
    if OLD in t:
        t = t.replace(OLD, NEW)
        path.write_text(t, encoding="utf-8")
        print(path.relative_to(ROOT))
