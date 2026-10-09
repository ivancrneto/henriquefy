import pytest


@pytest.fixture
def test_user():
    return {"name": "ana"}


def test_helper_without_assert():
    return 1
