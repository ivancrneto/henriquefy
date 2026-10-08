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
            for f in sorted(check(path).findings, key=lambda f: (f.path, f.line, f.rule))
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
    result = check(FIXTURES)
    a, b = grade(result).to_json(), grade(result).to_json()
    assert a == b
    data = json.loads(a)
    assert data["nota_mecanica"] is not None and 0 <= data["nota_mecanica"] <= 10
    for d in data["dimensions"]:
        assert d["score"] is None or 0 <= d["score"] <= 10


def test_na_dimensions_when_no_evidence(tmp_path):
    (tmp_path / "mod.py").write_text("def f():\n    return 1\n")
    data = json.loads(grade(check(tmp_path)).to_json())
    by = {d["category"]: d["score"] for d in data["dimensions"]}
    assert by["api"] is None and by["simplicity"] is None
    assert by["testing"] is not None  # project.no-tests fired


def test_single_file_target_has_no_vacuous_testing_score(tmp_path):
    f = tmp_path / "service.py"
    f.write_text("def f():\n    return 1\n")
    data = json.loads(grade(check(f)).to_json())
    assert {d["category"]: d["score"] for d in data["dimensions"]}["testing"] is None


def test_principles_with_a_rule_are_not_judgment_only():
    principles = load_principles()
    for rule in RULES.values():
        assert principles[rule.principle].detectable in {"mechanical", "partial"}, rule.id
