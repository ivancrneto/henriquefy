"""User rubric overrides from ~/.henriquefy/rubric.toml: `[weights]` id = int.

Overrides make the Nota mecânica non-comparable across machines, so the report names them.
Calibration and exit criteria run with none.
"""

import os
import tomllib
from pathlib import Path


def overrides_path() -> Path:
    return Path(os.environ.get("HENRIQUEFY_HOME", Path.home() / ".henriquefy")) / "rubric.toml"


def load_overrides(principles: dict) -> list[str]:
    path = overrides_path()
    if not path.is_file():
        return []
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    applied = []
    for pid, weight in data.get("weights", {}).items():
        if not isinstance(weight, int) or isinstance(weight, bool) or weight < 1:
            raise SystemExit(f"{path}: weights.{pid} must be a positive integer, got {weight!r}")
        if pid in principles:
            principles[pid].weight = weight
            applied.append(f"weights.{pid}={weight}")
    return applied
