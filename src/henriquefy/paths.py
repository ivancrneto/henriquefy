"""Locate the data directories (kb/, skills/, state/) in a wheel or a checkout.

In the built wheel they are force-included under the package; in an editable
install the package resolves to src/henriquefy/, so we fall back to the repo root.
"""

from importlib import resources
from pathlib import Path

_DATA_DIRS = ("kb", "skills", "state")


def data_dir(name: str) -> Path:
    if name not in _DATA_DIRS:
        raise ValueError(f"unknown data dir {name!r}; expected one of {_DATA_DIRS}")
    packaged = resources.files("henriquefy") / name
    if packaged.is_dir():
        return Path(str(packaged))
    checkout = Path(__file__).resolve().parents[2] / name
    if checkout.is_dir():
        return checkout
    raise FileNotFoundError(f"henriquefy data dir {name!r} not found in package or checkout")


def kb_dir() -> Path:
    return data_dir("kb")


def skills_dir() -> Path:
    return data_dir("skills")


def state_dir() -> Path:
    return data_dir("state")
