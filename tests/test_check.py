import json
import os
from pathlib import Path

import pytest

from henriquefy.check import check
from henriquefy.check.rules import RULES
from henriquefy.grade import grade, load_principles

FIXTURES = Path(__file__).resolve().parents[1] / "evals" / "fixtures"
CASES = sorted(p for p in FIXTURES.iterdir() if (p / "expected.json").is_file())


def _same_findings(findings, want: list[dict], target: str) -> bool:
    """A directory target names the file of each finding, so a finding that moves to another
    file on the same line fails; a file target's findings are all in that file."""
    with_path = not target.endswith(".py")
    assert all("path" in w for w in want) or not with_path, f"{target}: name each finding's path"

    def key(f: dict) -> tuple:
        return (f.get("path", ""), f["line"], f["rule"])

    got = [
        {"rule": f.rule, "line": f.line} | ({"path": f.path} if with_path else {}) for f in findings
    ]
    return sorted(got, key=key) == sorted(want, key=key)


@pytest.mark.parametrize("case", CASES, ids=[c.name for c in CASES])
def test_fixture_findings_match_exactly(case):
    expected = json.loads((case / "expected.json").read_text())
    for target, want in expected.items():
        path = case if target == "." else case / target
        findings = check(path, root=case).findings
        assert _same_findings(findings, want, target), f"{case.name}/{target}: {findings}"


def test_every_rule_has_a_fixture_and_a_known_principle():
    principles = load_principles()
    covered = set()
    for case in CASES:
        for findings in json.loads((case / "expected.json").read_text()).values():
            covered |= {f["rule"] for f in findings}
    for rule in RULES.values():
        assert rule.id in covered, f"{rule.id} has no fixture that fires it"
        assert rule.principle in principles, f"{rule.id} maps to unknown principle"


def test_grade_is_deterministic_and_bounded():
    """Two full runs, check included, give the same JSON."""
    a = grade(check(FIXTURES, root=FIXTURES)).to_json()
    b = grade(check(FIXTURES, root=FIXTURES)).to_json()
    assert a == b
    data = json.loads(a)
    assert data["nota_mecanica"] is not None and 0 <= data["nota_mecanica"] <= 10
    for d in data["dimensions"]:
        assert d["score"] is None or 0 <= d["score"] <= 10


def test_na_dimensions_when_no_evidence(tmp_path):
    (tmp_path / "mod.py").write_text("def f():\n    return 1\n")
    data = json.loads(grade(check(tmp_path, root=tmp_path)).to_json())
    by = {d["category"]: d["score"] for d in data["dimensions"]}
    assert by["api"] is None and by["simplicity"] is None
    assert by["testing"] is not None  # project.no-tests fired


def test_single_file_target_has_no_vacuous_testing_score(tmp_path):
    f = tmp_path / "service.py"
    f.write_text("def f():\n    return 1\n")
    data = json.loads(grade(check(f, root=tmp_path)).to_json())
    assert {d["category"]: d["score"] for d in data["dimensions"]}["testing"] is None


def test_principles_with_a_rule_are_not_judgment_only():
    principles = load_principles()
    for rule in RULES.values():
        assert principles[rule.principle].detectable in {"mechanical", "partial"}, rule.id


def test_subdirectory_target_uses_the_project_root():
    """Decouple detection, cycles and no-tests come from the root; findings from the target."""
    case = FIXTURES / "subdir-root"
    expected = json.loads((case / "expected.json").read_text())
    for target, want in expected.items():
        findings = check(case / target).findings
        assert _same_findings(findings, want, target), target
        assert not any(f.rule == "project.no-tests" for f in findings)


def test_unparseable_and_empty_targets_are_not_graded(tmp_path):
    (tmp_path / "a.py").write_text("def f(:\n    pass\n")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_a.py").write_text("def test_(:\n")
    data = json.loads(grade(check(tmp_path, root=tmp_path)).to_json())
    assert data["nota_mecanica"] is None and data["files"] == 0
    empty = tmp_path / "empty"
    empty.mkdir()
    assert json.loads(grade(check(empty, root=empty)).to_json())["nota_mecanica"] is None


def test_deeply_nested_expression_is_a_finding_not_a_crash(tmp_path):
    (tmp_path / "long.py").write_text("x = " + "+".join(["1"] * 200000) + "\n")
    result = check(tmp_path / "long.py", root=tmp_path)
    assert [f.rule for f in result.findings] == ["tooling.unparseable"]


def test_overrides_must_be_positive_integers(tmp_path, monkeypatch):
    from henriquefy.overrides import load_overrides

    monkeypatch.setenv("HENRIQUEFY_HOME", str(tmp_path))
    (tmp_path / "rubric.toml").write_text("[weights]\nprefira-excecoes-a-booleanos = 0\n")
    with pytest.raises(SystemExit):
        load_overrides(load_principles())
    (tmp_path / "rubric.toml").write_text("[weights]\nprefira-excecoes-a-booleanos = 5\n")
    principles = load_principles()
    assert load_overrides(principles) == ["weights.prefira-excecoes-a-booleanos=5"]
    assert principles["prefira-excecoes-a-booleanos"].weight == 5


def test_spread_formula_values():
    """Five findings in three of twenty files cost 3/20 of the principle, not 10/20."""
    from henriquefy.check import Finding, Result
    from henriquefy.check.rules import RULES

    rule = "errors.bare-except"
    findings = [Finding(rule, f"m{i % 3}.py", i + 1, "except:") for i in range(5)]
    result = Result("/x", 20, 2, "none", findings, target_is_dir=True)
    data = json.loads(grade(result).to_json())
    errors = next(d for d in data["dimensions"] if d["category"] == "errors")
    principle = RULES[rule].principle
    assert errors["principles"][principle]["files"] == 3
    assert errors["principles"][principle]["penalty"] == 0.15


def _project(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    (path / "pyproject.toml").write_text("[project]\nname = 'p'\n")
    (path / "tests").mkdir(exist_ok=True)
    (path / "tests" / "test_p.py").write_text("def test_p():\n    assert True\n")
    return path


MUTABLE = "def f(x=[]):\n    return x\n"


def test_nested_repositories_virtualenvs_and_tool_dirs_are_not_the_project(tmp_path):
    root = _project(tmp_path / "proj")
    for sub in ("vendor/clone", ".claude/worktrees/w", ".tox/py312", "env"):
        (root / sub).mkdir(parents=True)
        (root / sub / "m.py").write_text(MUTABLE)
    (root / "vendor/clone/.git").mkdir()
    (root / ".claude/worktrees/w/.git").write_text("gitdir: /elsewhere\n")
    (root / "env/pyvenv.cfg").write_text("home = /usr\n")
    assert check(root).findings == []
    # named explicitly, a pruned directory is checked
    clone = check(root / "vendor/clone", root=root)
    assert [f.path for f in clone.findings] == ["vendor/clone/m.py"]


def test_a_project_below_a_directory_named_build_is_checked(tmp_path):
    root = _project(tmp_path / "build" / "proj")
    (root / "m.py").write_text(MUTABLE)
    assert [f.rule for f in check(root).findings] == ["readability.mutable-default"]


@pytest.mark.skipif(os.name != "posix" or os.geteuid() == 0, reason="needs an unreadable file")
def test_odd_files_named_py_never_crash_or_hang(tmp_path):
    root = _project(tmp_path / "proj")
    (root / "pkg.py").mkdir()
    (root / "dangling.py").symlink_to(tmp_path / "missing.py")
    os.mkfifo(root / "pipe.py")
    (root / "locked.py").write_text("x = 1\n")
    (root / "locked.py").chmod(0)
    try:
        result = check(root)
    finally:
        (root / "locked.py").chmod(0o644)
    assert [(f.path, f.rule) for f in result.findings] == [("locked.py", "tooling.unparseable")]
    assert "cannot read" in result.findings[0].message


def test_a_file_target_parses_only_that_file(tmp_path, monkeypatch):
    import henriquefy.check as runner

    root = _project(tmp_path / "proj")
    (root / "m.py").write_text(MUTABLE)
    monkeypatch.setattr(runner, "python_files", lambda *a: pytest.fail("walked the root"))
    assert [f.rule for f in check(root / "m.py").findings] == ["readability.mutable-default"]


def test_root_search_stops_below_home(tmp_path, monkeypatch):
    from henriquefy.check import find_root

    (tmp_path / ".git").mkdir()  # a dotfiles repository in $HOME
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: tmp_path))
    loose = tmp_path / "scratch"
    loose.mkdir()
    assert find_root(loose) == loose
    assert find_root(tmp_path) == tmp_path


def test_target_outside_root_is_an_error(tmp_path, capsys):
    from henriquefy.cli import main

    a, b = _project(tmp_path / "a"), _project(tmp_path / "b")
    with pytest.raises(ValueError):
        check(a, root=b)
    assert main(["check", str(a), "--root", str(b)]) == 2
    assert "not inside" in capsys.readouterr().err


def test_long_import_and_class_chains_do_not_hit_the_recursion_limit(tmp_path):
    root = _project(tmp_path / "proj")
    n = 1500
    for i in range(n):
        nxt = (i + 1) % n  # the last module closes one cycle through all of them
        (root / f"m{i:04}.py").write_text(f"import m{nxt:04}\n")
    classes = [f"class C{i}(C{i - 1}):\n    pass\n" for i in range(1, n)]
    (root / "deep.py").write_text("\n".join(["class C0:\n    pass\n", *classes]))
    findings = check(root).findings
    assert [f.path for f in findings if f.rule == "modeling.import-cycle"] == ["m0000.py"]
    assert sum(f.rule == "modeling.inheritance-depth" for f in findings) == n - 3


def test_a_cycle_reaching_into_the_target_is_reported_there(tmp_path):
    root = _project(tmp_path / "proj")
    (root / "pkg" / "sub").mkdir(parents=True)
    (root / "pkg" / "__init__.py").write_text("")
    (root / "pkg" / "sub" / "__init__.py").write_text("")
    (root / "pkg" / "a.py").write_text("from pkg.sub import b\n")
    (root / "pkg" / "sub" / "b.py").write_text("from pkg import a\n")
    assert [f.path for f in check(root).findings] == ["pkg/a.py"]
    assert [f.path for f in check(root / "pkg" / "sub").findings] == ["pkg/sub/b.py"]


def test_malformed_overrides_are_named_not_tracebacks(tmp_path, monkeypatch, capsys):
    from henriquefy.overrides import load_overrides

    monkeypatch.setenv("HENRIQUEFY_HOME", str(tmp_path))
    for text in ("[weights\n", "weights = 3\n"):
        (tmp_path / "rubric.toml").write_text(text)
        with pytest.raises(SystemExit, match="rubric.toml"):
            load_overrides(load_principles())
    (tmp_path / "rubric.toml").write_text("[weights]\nno-such-principle = 4\n")
    assert load_overrides(load_principles()) == []
    assert "names no principle" in capsys.readouterr().err
