import importlib.util
import sys
from pathlib import Path

import django
import pytest
from django.conf import settings

if not settings.configured:
    settings.configure(DEBUG=True, ALLOWED_HOSTS=["*"], DEFAULT_CHARSET="utf-8")
    django.setup()

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = [p.name for p in (ROOT / "before", ROOT / "after") if (p / "views.py").is_file()]


@pytest.fixture(params=VARIANTS)
def views(request):
    """The module under test, before or after the transform; both must pass the same tests."""
    path = ROOT / request.param / "views.py"
    spec = importlib.util.spec_from_file_location(f"views_{request.param}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.ORDERS.clear()
    return module
