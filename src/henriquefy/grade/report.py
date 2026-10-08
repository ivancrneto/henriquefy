"""Render the Nota mecânica as text, and write report.md plus a JSON trend entry."""

import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from henriquefy.check import Result, describe
from henriquefy.grade import Grade


def render(grade: Grade, result: Result, overrides_active: list[str] | None = None) -> str:
    nota = "N/A" if grade.overall is None else grade.overall
    lines = [f"Nota mecânica: {nota}  (deterministic; not his verdict)"]
    lines.append(
        f"{result.files} files, {len(result.findings)} findings, framework {result.framework}"
        + (f", graded as era {grade.era}" if grade.era else "")
    )
    if overrides_active:
        lines.append(f"rubric overrides active: {', '.join(overrides_active)}")
    lines.append("")
    lines.append("| dimension | applicable weight | score | evidence |")
    lines.append("|---|---|---|---|")
    for d in grade.dimensions:
        score = "N/A" if d.score is None else f"{d.score}"
        evidence = (
            ", ".join(f"{p} {v['findings']}" for p, v in d.principles.items())
            or "no applicable rule"
        )
        lines.append(f"| {d.name} | {d.weight} | {score} | {evidence} |")
    scored = [d for d in grade.dimensions if d.score is not None and d.score < 10]
    if scored:
        w = min(scored, key=lambda d: (d.score, -d.weight, d.name))
        worst = max(w.principles.items(), key=lambda kv: (kv[1]["findings"], kv[0]))[0]
        lines.append("")
        lines.append(
            f"Weakest dimension: {w.name} (ties broken by weight, then name)."
            f" Read kb/principles/{worst}.md for the lesson to watch."
        )
    for note in grade.drift:
        lines.append(f"tooling drift: {note}")
    lines.append("")
    lines.append(describe(result))
    return "\n".join(lines).rstrip() + "\n"


def write_report(root: Path, grade: Grade, result: Result, text: str) -> Path:
    out = root / ".henriquefy"
    out.mkdir(exist_ok=True)
    (out / "report.md").write_text(text, encoding="utf-8")
    entry = {
        "at": datetime.now(UTC).isoformat(timespec="seconds"),
        "commit": _git_sha(root),
        "nota_mecanica": grade.overall,
        "dimensions": {d.category: d.score for d in grade.dimensions},
    }
    trend = out / "grade.jsonl"
    with trend.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return out / "report.md"


def _git_sha(root: Path) -> str | None:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
