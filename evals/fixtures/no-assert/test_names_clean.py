import pytest
from pytest import raises


@pytest.fixture
def test_order():
    return {}


def test_raises_as_name():
    with raises(ZeroDivisionError):
        1 / 0


def test_fail_counts():
    pytest.fail("explicit failure is an assertion")
