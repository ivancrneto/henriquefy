"""Phase 5 exit criterion: the committed after/ of the transform fixture passes the fixture's
tests, loses the rule ids listed as gone, keeps the ones listed as remaining, and preserves the
public names and signatures."""

import importlib.util
import inspect
import re
import subprocess
import sys
from pathlib import Path

import pytest

from henriquefy.check import check

FIXTURE = Path(__file__).resolve().parents[1] / "evals" / "transform" / "magic-status"


def expected() -> dict[str, list[str]]:
    text = (FIXTURE / "expected.md").read_text(encoding="utf-8")
    out = {}
    for section in ("gone", "remain", "public"):
        block = text.split(f"## {section}", 1)[1].split("\n## ", 1)[0]
        out[section] = re.findall(r"^- (.+)$", block, re.M)
    return out


def load(variant: str):
    path = FIXTURE / variant / "views.py"
    spec = importlib.util.spec_from_file_location(f"transform_{variant}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module", autouse=True)
def django_settings():
    import django
    from django.conf import settings

    if not settings.configured:
        settings.configure(DEBUG=True, ALLOWED_HOSTS=["*"], DEFAULT_CHARSET="utf-8")
        django.setup()


def test_after_exists():
    assert (FIXTURE / "after" / "views.py").is_file(), "run the transform and commit after/views.py"


def test_fixture_tests_pass_on_before_and_after():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(FIXTURE / "tests")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "after" in result.stdout or "passed" in result.stdout


def test_findings_gone_and_remaining():
    want = expected()
    before = {
        f.rule for f in check(FIXTURE / "before" / "views.py", root=FIXTURE / "before").findings
    }
    after = {f.rule for f in check(FIXTURE / "after" / "views.py", root=FIXTURE / "after").findings}
    for rule in want["gone"]:
        assert rule in before, f"{rule} never fired on before/; the fixture is wrong"
        assert rule not in after, f"{rule} still fires on after/"
    for rule in want["remain"]:
        assert rule in after, f"{rule} was removed, but it must remain (public behavior)"


def test_public_interface_unchanged():
    before, after = load("before"), load("after")
    for entry in expected()["public"]:
        name = entry.split("(")[0]
        assert hasattr(after, name), f"{name} disappeared"
        if "(" in entry:
            sig_before = inspect.signature(getattr(before, name))
            sig_after = inspect.signature(getattr(after, name))
            assert sig_after == sig_before, f"{name}: {sig_before} -> {sig_after}"
            assert str(sig_after).replace(" ", "") == entry[len(name) :].replace(" ", "")
