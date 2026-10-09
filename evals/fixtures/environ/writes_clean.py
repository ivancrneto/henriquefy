import os
from unittest import mock

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
os.environ["TZ"] = "UTC"
os.environ.update({"LANG": "C"})
del os.environ["TZ"]


@mock.patch.dict(os.environ, {"DEBUG": "1"})
def run():
    return 1


def test_debug(monkeypatch):
    monkeypatch.setitem(os.environ, "DEBUG", "1")
