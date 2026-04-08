import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "pages"
for p in root.glob("*.html"):
    t = p.read_text(encoding="utf-8")
    t = t.replace("\u00e2\u20ac\u00a2", "\u2022")  # mojibake for bullet
    t = t.replace("\u00c2\u00a9", "\u00a9")  # mojibake for copyright
    t = t.replace("That\u00e2\u20ac\u2122s OK", "That's OK")
    p.write_text(t, encoding="utf-8")
    print(p.name)
