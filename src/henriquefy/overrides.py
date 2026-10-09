"""User rubric overrides from ~/.henriquefy/rubric.toml: `[weights]` id = int.

Overrides make the Nota mecânica non-comparable across machines, so the report names them.
Calibration and exit criteria run with none.
"""

import os
import sys
import tomllib
from pathlib import Path


def overrides_path() -> Path:
    return Path(os.environ.get("HENRIQUEFY_HOME", Path.home() / ".henriquefy")) / "rubric.toml"


def load_overrides(principles: dict) -> list[str]:
    path = overrides_path()
    if not path.is_file():
        return []
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise SystemExit(f"{path}: not valid TOML: {exc}") from exc
    weights = data.get("weights", {})
    if not isinstance(weights, dict):
        raise SystemExit(f"{path}: [weights] must be a table of principle id = integer")
    applied = []
    for pid, weight in weights.items():
        if not isinstance(weight, int) or isinstance(weight, bool) or weight < 1:
            raise SystemExit(f"{path}: weights.{pid} must be a positive integer, got {weight!r}")
        if pid in principles:
            principles[pid].weight = weight
            applied.append(f"weights.{pid}={weight}")
        else:
            print(f"{path}: weights.{pid} names no principle; ignored", file=sys.stderr)
    return applied
