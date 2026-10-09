from http import HTTPStatus

from app.views import create
from app.world import created_reply


def test_create_replies_created():
    assert create(None).status_code == HTTPStatus.CREATED
    assert created_reply()[0].status_code == HTTPStatus.CREATED
