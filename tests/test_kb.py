import re
from pathlib import Path

KB = Path(__file__).resolve().parents[1] / "kb"
CATEGORIES = {
    "modeling",
    "simplicity",
    "errors",
    "testing",
    "api",
    "project",
    "readability",
    "career",
}
DETECTABLE = {"mechanical", "partial", "judgment"}


def _frontmatter(path: Path) -> str:
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    assert m, f"{path} has no frontmatter"
    return m.group(1)


def _field(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    assert m, f"missing field {key}"
    return m.group(1).strip()


def principles() -> list[Path]:
    return sorted(p for p in (KB / "principles").glob("*.md") if not p.name.startswith("_"))


def test_principles_have_valid_frontmatter_and_citations():
    assert principles(), "no principle files"
    for path in principles():
        fm = _frontmatter(path)
        assert _field(fm, "id") == path.stem
        assert _field(fm, "category") in CATEGORIES
        assert _field(fm, "detectable") in DETECTABLE
        assert "sources:" in fm and "- type:" in fm, f"{path} has no sources"
        for course in re.findall(r"^\s+course:\s*(\S+)$", fm, re.M):
            assert (KB / "courses" / f"{course}.md").is_file(), f"{path}: unknown course {course}"
        for commit in re.findall(r"^\s+commit:\s*(\S+)$", fm, re.M):
            assert re.fullmatch(r"[0-9a-f]{40}", commit), f"{path}: commit must be a full sha"


def test_index_lists_every_principle_and_only_existing_ones():
    index = (KB / "INDEX.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"^- ([a-z0-9-]+) \| ", index, re.M))
    on_disk = {p.stem for p in principles()}
    assert listed == on_disk, f"index/disk mismatch: {listed ^ on_disk}"


def test_ask_evals_cite_existing_principles():
    table = (Path(__file__).resolve().parents[1] / "evals" / "ask.md").read_text(encoding="utf-8")
    on_disk = {p.stem for p in principles()}
    for row in re.findall(r"^\|(?!---)(?! question)(.+)\|$", table, re.M):
        cells = [c.strip() for c in row.split("|")]
        if len(cells) >= 2 and cells[1]:
            assert cells[1] in on_disk, f"evals/ask.md cites unknown principle {cells[1]}"
