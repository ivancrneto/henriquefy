"""Nota mecânica: a pure function of the mechanical findings and the rubric weights.

Formula (also stated in kb/rubric.md):
  penalty(principle) = min(1, 2 * findings(principle) / files)
  penalty(dimension) = weighted mean of its mechanical/partial principles' penalties
  score(dimension)   = 10 * (1 - penalty), rounded to one decimal
  overall            = weighted mean of the scored dimensions
A dimension is N/A when none of its principles has an applicable rule in the target.
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from henriquefy.check import Result
from henriquefy.check.rules import RULES
from henriquefy.paths import kb_dir

DIMENSIONS = {
    "modeling": "Modelagem",
    "simplicity": "Simplicidade",
    "errors": "Erros",
    "testing": "Testes",
    "api": "API",
    "project": "Projeto e config",
    "readability": "Legibilidade",
}
ERA_YEAR = {"timeless": 0, "2010s": 2010, "2020s": 2020, "2026": 2026}


@dataclass
class Principle:
    id: str
    category: str
    weight: int
    detectable: str
    era: str
    citation: str


@dataclass
class DimensionScore:
    name: str
    category: str
    weight: int
    score: float | None
    principles: dict[str, dict] = field(default_factory=dict)


@dataclass
class Grade:
    overall: float | None
    dimensions: list[DimensionScore]
    files: int
    findings: int
    framework: str
    era: int | None
    drift: list[str]

    def to_json(self) -> str:
        return json.dumps(
            {
                "nota_mecanica": self.overall,
                "era": self.era,
                "files": self.files,
                "findings": self.findings,
                "framework": self.framework,
                "dimensions": [
                    {
                        "name": d.name,
                        "category": d.category,
                        "weight": d.weight,
                        "score": d.score,
                        "principles": d.principles,
                    }
                    for d in self.dimensions
                ],
                "tooling_drift": self.drift,
            },
            indent=2,
            ensure_ascii=False,
        )


def _field(fm: str, key: str, default: str = "") -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).split("#", 1)[0].strip() if m else default


def load_principles(kb: Path | None = None) -> dict[str, Principle]:
    kb = kb or kb_dir()
    out = {}
    for path in sorted((kb / "principles").glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---\n", text, re.S).group(1)
        course = re.search(r"course:\s*(\S+)", fm)
        section = re.search(r'section:\s*"([^"]+)"', fm)
        citation = (
            f"{course.group(1)} section {section.group(1)}" if course and section else path.stem
        )
        out[path.stem] = Principle(
            path.stem,
            _field(fm, "category"),
            int(_field(fm, "weight", "3")),
            _field(fm, "detectable"),
            _field(fm, "era", "timeless"),
            citation,
        )
    return out


def grade(
    result: Result, era: int | None = None, principles: dict[str, Principle] | None = None
) -> Grade:
    principles = principles or load_principles()
    files = max(result.files, 1)
    counts: dict[str, int] = {}
    applicable: set[str] = set()
    for f in result.findings:
        rule = RULES.get(f.rule)
        if rule:
            counts[rule.principle] = counts.get(rule.principle, 0) + 1
    for rule in RULES.values():
        if _rule_applies(rule.id, result):
            applicable.add(rule.principle)
    drift: list[str] = []
    dims: list[DimensionScore] = []
    for category, name in DIMENSIONS.items():
        members = [
            p
            for p in principles.values()
            if p.category == category
            and p.detectable in {"mechanical", "partial"}
            and p.id in applicable
        ]
        if era is not None:
            kept = []
            for p in members:
                if ERA_YEAR.get(p.era, 0) > era:
                    if counts.get(p.id):
                        drift.append(
                            f"{p.id}: {counts[p.id]} finding(s) on a {p.era} practice,"
                            f" graded as era {era}"
                        )
                else:
                    kept.append(p)
            members = kept
        if not members:
            dims.append(DimensionScore(name, category, 0, None))
            continue
        total_w = sum(p.weight for p in members)
        detail = {}
        penalty = 0.0
        for p in members:
            n = counts.get(p.id, 0)
            pen = min(1.0, 2 * n / files)
            penalty += p.weight * pen
            detail[p.id] = {"weight": p.weight, "findings": n, "penalty": round(pen, 3)}
        score = round(10 * (1 - penalty / total_w), 1)
        dims.append(DimensionScore(name, category, total_w, score, detail))
    scored = [d for d in dims if d.score is not None]
    overall = (
        round(sum(d.score * d.weight for d in scored) / sum(d.weight for d in scored), 1)
        if scored
        else None
    )
    return Grade(overall, dims, result.files, len(result.findings), result.framework, era, drift)


def _rule_applies(rule_id: str, result: Result) -> bool:
    """Whether a rule had a chance to fire: tests rules need test files, API rules a web framework
    or any status/route call, decouple rule a decouple dependency (signalled by the runner)."""
    if rule_id in {"testing.no-assert"}:
        return result.test_files > 0
    if rule_id in {"project.no-tests", "modeling.import-cycle", "modeling.inheritance-depth"}:
        return result.target_is_dir
    if rule_id == "api.verb-in-uri":
        return result.signals.get("routes", False)
    if rule_id == "api.magic-status":
        return result.signals.get("responses", False) or any(
            f.rule == "api.magic-status" for f in result.findings
        )
    if rule_id == "project.environ-without-decouple":
        return result.depends_on_decouple
    return True
