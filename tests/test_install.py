import re
import subprocess
import sys
from pathlib import Path

import pytest

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


def test_reinstall_over_a_symlinked_skill_replaces_the_link_not_its_target(tmp_path):
    real = tmp_path / "dotfiles" / "henriquefy"
    real.mkdir(parents=True)
    (real / "mine.txt").write_text("keep")
    skills = tmp_path / "skills"
    skills.mkdir()
    (skills / "henriquefy").symlink_to(real)
    (skills / "henrique-watch").symlink_to(tmp_path / "gone")  # dangling
    assert main(["install", "--target", str(skills), "--all"]) == 0
    assert not (skills / "henriquefy").is_symlink()
    assert (skills / "henriquefy" / "SKILL.md").is_file()
    assert (real / "mine.txt").read_text() == "keep"
    assert (skills / "henrique-watch" / "SKILL.md").is_file()


def test_install_refuses_to_overwrite_its_own_source(tmp_path, monkeypatch, capsys):
    import shutil

    import henriquefy.install as installer

    source = tmp_path / "skills"
    shutil.copytree(Path(__file__).resolve().parents[1] / "skills", source)
    monkeypatch.setattr(installer, "skills_dir", lambda: source)
    assert main(["install", "--target", str(source)]) == 2
    assert "own source" in capsys.readouterr().err
    assert (source / "henriquefy" / "SKILL.md").is_file()


SKILLS = Path(__file__).resolve().parents[1] / "skills"
WRAPPER = SKILLS / "henriquefy" / "scripts" / "henriquefy.sh"


@pytest.mark.parametrize("shell", ["sh", "bash", "dash"])
def test_wrapper_pins_the_stamped_version_under_cdpath_and_spaces(tmp_path, shell):
    """The wrapper reads the version next to it, whatever the shell, CDPATH or path."""
    import shutil

    if shutil.which(shell) is None:
        pytest.skip(f"{shell} not installed")
    skill = tmp_path / "with space" / "henriquefy"
    (skill / "scripts").mkdir(parents=True)
    shutil.copy(WRAPPER, skill / "scripts" / "henriquefy.sh")
    (skill / "SKILL.md").write_text('---\nmetadata:\n  henriquefy_version: "1.2.3"\r\n---\n')
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "uvx").write_text('#!/bin/sh\necho "uvx $*"\n')
    (bin_dir / "uvx").chmod(0o755)
    env = {"PATH": f"{bin_dir}:/usr/bin:/bin", "CDPATH": f"{tmp_path}:."}
    out = subprocess.run(
        [shell, "henriquefy/scripts/henriquefy.sh", "check", "a b"],
        cwd=skill.parent,
        env=env,
        capture_output=True,
        text=True,
    )
    assert out.returncode == 0, out.stderr
    assert out.stdout == "uvx --offline henriquefy==1.2.3 check a b\n"
