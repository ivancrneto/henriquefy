from unittest import TestCase, mock

import pytest


def test_pay():
    assert 10 == 10


def test_raises():
    with pytest.raises(ValueError):
        int("x")


class PlayerTest(TestCase):
    def test_receive(self):
        self.assertEqual(1, 1)

    def test_mocked(self):
        m = mock.Mock()
        m()
        m.assert_called_once()
