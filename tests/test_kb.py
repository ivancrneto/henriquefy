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
    section = index.split("## Principles", 1)[1].split("\n## ", 1)[0]
    listed = set(re.findall(r"^- ([a-z0-9-]+) \| ", section, re.M))
    on_disk = {p.stem for p in principles()}
    assert listed == on_disk, f"index/disk mismatch: {listed ^ on_disk}"


def test_ask_evals_cite_existing_principles():
    table = (Path(__file__).resolve().parents[1] / "evals" / "ask.md").read_text(encoding="utf-8")
    on_disk = {p.stem for p in principles()}
    for row in re.findall(r"^\|(?!---)(?! question)(.+)\|$", table, re.M):
        cells = [c.strip() for c in row.split("|")]
        if len(cells) >= 2 and cells[1]:
            assert cells[1] in on_disk, f"evals/ask.md cites unknown principle {cells[1]}"


ORIGINS = {"his", "course", "translated"}


def patterns() -> list[Path]:
    return sorted(p for p in (KB / "patterns").glob("*.md") if not p.name.startswith("_"))


def test_patterns_reference_existing_principles_and_valid_origins():
    on_disk = {p.stem for p in principles()}
    for path in patterns():
        fm = _frontmatter(path)
        assert _field(fm, "id") == path.stem
        assert _field(fm, "principle") in on_disk, f"{path}: unknown principle"
        renditions = re.findall(r"^\s{2}(python|django|fastapi):\s*\{(.*)\}", fm, re.M)
        assert renditions, f"{path}: no renditions"
        for _, body in renditions:
            origin = re.search(r"origin:\s*(\w+)", body)
            assert origin and origin.group(1) in ORIGINS, f"{path}: bad origin in {body}"
            if origin.group(1) == "his":
                assert re.search(r"commit:\s*[0-9a-f]{40}", body), f"{path}: his needs a full sha"
        text = path.read_text(encoding="utf-8")
        for fw, _ in renditions:
            assert f"\n## {fw}\n" in text, f"{path}: missing ## {fw} section"


def test_generated_files_are_up_to_date():
    from henriquefy.ingest.build_index import main

    assert main(["--check"]) == 0


def test_rule_ids_in_principles_exist_or_are_marked_candidates():
    from henriquefy.check.rules import RULES

    pattern = re.compile(r"`((?:api|errors|modeling|testing|project|readability)\.[\w-]+)`")
    for path in principles():
        text = path.read_text(encoding="utf-8")
        for m in pattern.finditer(text):
            if m.group(1) in RULES:
                continue
            before = text[max(0, m.start() - 60) : m.start()]
            assert "candidate" in before, (
                f"{path.name}: {m.group(1)} is not implemented and not marked candidate"
            )


def test_rule_backed_principles_have_an_example_from_his_code_or_lessons():
    """Phase 3 exit criterion: every mechanical or partial principle has a pattern rendition
    with origin his (repo, path, commit) or origin course (course, lesson, section)."""
    from henriquefy.check.rules import RULES

    backed = {r.principle for r in RULES.values()}
    covered: dict[str, bool] = {}
    for path in patterns():
        fm = _frontmatter(path)
        principle = _field(fm, "principle")
        for _, body in re.findall(r"^\s{2}(python|django|fastapi):\s*\{(.*)\}", fm, re.M):
            his = "origin: his" in body and re.search(r"commit:\s*[0-9a-f]{40}", body)
            course = "origin: course" in body and "lesson:" in body and "section:" in body
            if his or course:
                covered[principle] = True
    missing = sorted(p for p in backed if not covered.get(p))
    assert not missing, f"no cited example for: {missing}"


DIGEST_SCHEMA = [
    "visão geral",
    "filosofia",
    "pilares",
    "aulas",
    "princípios",
    "citações",
    "evolução técnica",
    "arsenal",
    "glossário",
    "perguntas",
    "repositórios",
    "linha a linha",
    "execução real",
]


def test_course_digests_follow_the_schema():
    for path in sorted((KB / "courses").glob("*.md")):
        if path.name == "README.md":
            continue
        headings = " | ".join(
            h.lower() for h in re.findall(r"^## (.+)$", path.read_text(encoding="utf-8"), re.M)
        )
        missing = [k for k in DIGEST_SCHEMA if k not in headings]
        assert not missing, f"{path.name} lacks sections: {missing}"
