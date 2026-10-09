"""Grade the alumni clones and compare each of his course repos with its own forks.

    python -m henriquefy.ingest.calibrate

Reads sources/repos/manifest.json (gitignored; holds the id-to-repo map), grades every alumni
clone under sources/repos/alumni/<id>/, and writes evals/calibration/alumni.json keyed by the
random id only. The originals are compared with the median of their forks on every timeless
dimension of the Nota mecânica; no fork is named anywhere in the committed output.
"""

import json
import statistics
import sys
from pathlib import Path

from henriquefy.check import check
from henriquefy.grade import grade

TIMELESS = ("modeling", "simplicity", "errors", "testing", "readability")
ORIGINALS = {
    "henriquebastos/eventex": "eventex",
    "henriquebastos/pacote-desafios-pythonicos": "pacote-desafios-pythonicos",
}


def score(path: Path) -> dict:
    g = grade(check(path))
    return {
        "nota_mecanica": g.overall,
        "findings": g.findings,
        "files": g.files,
        "dimensions": {d.category: d.score for d in g.dimensions},
    }


def fork_of(rec: dict) -> str | None:
    """The original a fork came from: the `source` gh_fetch records; for records written
    before it did, a name that starts with the original's full name (a renamed fork is lost)."""
    if "source" in rec:
        return rec["source"] if rec["source"] in ORIGINALS else None
    name = rec["repo"].split("/")[1].lower()
    for original, folder in ORIGINALS.items():
        if name.startswith(folder):
            return original
    return None


def compare(original: str, folder: Path, forks: list[dict]) -> dict:
    own = score(folder)
    row = {"original": own["dimensions"], "forks": len(forks), "fork_median": {}, "ok": {}}
    for dim in TIMELESS:
        values = [f["dimensions"][dim] for f in forks if f["dimensions"].get(dim) is not None]
        mine = own["dimensions"].get(dim)
        if values and mine is not None:
            med = statistics.median(values)
            row["fork_median"][dim] = med
            row["ok"][dim] = mine >= med
    return row


def main() -> int:
    root = Path("sources/repos")
    manifest = json.loads((root / "manifest.json").read_text())
    alumni = manifest.get("alumni", [])
    if not alumni:
        print("no alumni in manifest; run gh_fetch --alumni first", file=sys.stderr)
        return 1
    scored: dict[str, dict] = {}
    for rec in alumni:
        clone = root / "alumni" / rec["id"]
        if clone.is_dir():
            scored[rec["id"]] = score(clone) | {"fork_of": fork_of(rec)}
    comparisons = {
        original: compare(
            original,
            root / folder,
            [s for s in scored.values() if s["fork_of"] == original],
        )
        for original, folder in ORIGINALS.items()
    }
    out = {
        "note": "Alumni repos graded locally and keyed by random id, never by name; the id map"
        " lives in gitignored sources/repos/manifest.json.",
        "date": manifest.get("fetched"),
        "alumni": scored,
        "comparisons": comparisons,
    }
    Path("evals/calibration").mkdir(parents=True, exist_ok=True)
    Path("evals/calibration/alumni.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n"
    )
    print(json.dumps(comparisons, indent=2))
    print(f"{len(scored)} alumni repos graded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
