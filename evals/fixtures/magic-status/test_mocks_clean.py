from http import HTTPStatus

from requests import Response


def test_fake_reply(responses):
    responses.add("GET", "https://h/first", status=200, json={"ok": True})
    fake = Response()
    fake.status_code = 200
    assert fake.status_code == HTTPStatus.OK


def test_fake_positional_reply():
    fake = Response(b"{}", 201)
    assert fake.status_code == HTTPStatus.CREATED
