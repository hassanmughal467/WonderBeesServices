"""Remove data-nav from links inside <main> — keep nav highlight in header only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def strip_data_nav(block: str) -> str:
    return re.sub(r"\s+data-nav=\"[^\"]+\"", "", block)


def patch_file(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")

    def repl(m: re.Match) -> str:
        return strip_data_nav(m.group(0))

    new = re.sub(r"<main\b[^>]*>.*?</main>", repl, raw, flags=re.DOTALL | re.IGNORECASE)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        print("stripped main:", path.relative_to(ROOT))


def main() -> None:
    for path in sorted((ROOT / "pages").glob("*.html")) + [ROOT / "index.html", ROOT / "contact.html"]:
        if path.exists():
            patch_file(path)


if __name__ == "__main__":
    main()
