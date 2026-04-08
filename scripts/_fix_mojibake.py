"""Replace common UTF-8 mojibake sequences in HTML (Windows/Latin-1 corruption)."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent

REPLACEMENTS = [
    ("Ã¢â‚¬â€", "—"),
    ("Ã¢â‚¬â€œ", "–"),
    ("Ã¢â‚¬â„¢", "'"),
    ("Ã¢â‚¬Â¦", "…"),
    ("Ã¢â‚¬Å“", "\u201c"),
    ("Ã¢â‚¬Â", "\u201d"),
    ("Ã¢â‚¬Â¢", "·"),
    ("Ã¢Å“â€œ", "✓"),
    ("Ãƒâ€šÃ‚Â·", "·"),
    ("Ãƒâ€šÃ‚Â»", "»"),
    ("Ã‚Â·", "·"),
    # Corrupted "←" used in blog back links
    ("ÃƒÂ¢Ã¢â‚¬Â Ã‚Â", "←"),
    # Corrupted "→" in job/blog links
    ("ÃƒÂ¢Ã¢â‚¬Â '", "→"),
    ("ÃƒÂ©", "é"),
]

count_files = 0
for path in root.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    orig = text
    for bad, good in REPLACEMENTS:
        text = text.replace(bad, good)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        count_files += 1
        print("fixed", path.relative_to(root))

print("done", count_files, "files")
