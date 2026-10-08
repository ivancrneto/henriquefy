import re
import subprocess
import sys
from pathlib import Path

from henriquefy import __version__
from henriquefy.cli import main

ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def _frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert m, f"{path} has no frontmatter"
    keys = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith(" "):
            key, _, value = line.partition(":")
            keys[key.strip()] = value.strip()
    return keys


def test_install_smoke_in_project_mode(tmp_path):
    result = subprocess.run(
        [sys.executable, "-m", "henriquefy.cli", "install", "--project"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    skill = tmp_path / ".claude" / "skills" / "henriquefy" / "SKILL.md"
    assert skill.is_file(), result.stdout + result.stderr
    assert f"henriquefy_version: {__version__}" in skill.read_text(encoding="utf-8")
    assert (skill.parent / "references" / "kb" / "INDEX.md").is_file()
    assert not (tmp_path / ".claude" / "skills" / "henrique-ingest").exists()


def test_install_all_and_reinstall_replaces(tmp_path):
    main(["install", "--target", str(tmp_path), "--all"])
    stray = tmp_path / "henriquefy" / "stray.txt"
    stray.write_text("x")
    main(["install", "--target", str(tmp_path), "--all"])
    assert not stray.exists()
    for name in ("henriquefy", "henrique-ingest", "henrique-watch"):
        assert (tmp_path / name / "SKILL.md").is_file()


def test_skill_frontmatter_is_spec_clean_and_small():
    root = Path(__file__).resolve().parents[1] / "skills"
    for skill_md in root.glob("*/SKILL.md"):
        keys = _frontmatter(skill_md)
        assert keys["name"] == skill_md.parent.name
        assert set(keys) <= ALLOWED_FRONTMATTER, f"{skill_md}: {set(keys) - ALLOWED_FRONTMATTER}"
        assert len(skill_md.read_text(encoding="utf-8").splitlines()) < 100
