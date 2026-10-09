import json
from pathlib import Path

import pytest

from henriquefy.check import check
from henriquefy.check.rules import RULES
from henriquefy.grade import grade, load_principles

FIXTURES = Path(__file__).resolve().parents[1] / "evals" / "fixtures"
CASES = sorted(p for p in FIXTURES.iterdir() if (p / "expected.json").is_file())


@pytest.mark.parametrize("case", CASES, ids=[c.name for c in CASES])
def test_fixture_findings_match_exactly(case):
    expected = json.loads((case / "expected.json").read_text())
    for target, want in expected.items():
        path = case if target == "." else case / target
        got = [
            {"rule": f.rule, "line": f.line}
            for f in sorted(check(path, root=case).findings, key=lambda f: (f.path, f.line, f.rule))
        ]
        assert got == sorted(want, key=lambda f: (f["line"], f["rule"])), f"{case.name}/{target}"


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
    result = check(FIXTURES, root=FIXTURES)
    a, b = grade(result).to_json(), grade(result).to_json()
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
        got = sorted(
            ({"rule": f.rule, "line": f.line} for f in check(case / target).findings),
            key=lambda f: (f["line"], f["rule"]),
        )
        assert got == sorted(want, key=lambda f: (f["line"], f["rule"])), target
        assert not any(f.rule == "project.no-tests" for f in check(case / target).findings)


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
