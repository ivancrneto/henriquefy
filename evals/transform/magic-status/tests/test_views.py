import json
from http import HTTPStatus

from django.test import RequestFactory


def post(body):
    return RequestFactory().post("/orders/", data=body, content_type="application/json")


def test_create_order_returns_201_and_the_order(views):
    response = views.create_order(post('{"balance": 100}'))
    assert response.status_code == HTTPStatus.CREATED
    assert json.loads(response.content) == {"id": 1, "balance": 100}


def test_create_order_with_bad_json_returns_400(views):
    response = views.create_order(post("{not json"))
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert json.loads(response.content) == {"error": "bad json"}


def test_order_detail_404_then_200(views):
    assert views.order_detail(RequestFactory().get("/orders/1/"), 1).status_code == HTTPStatus.NOT_FOUND
    views.create_order(post('{"balance": 5}'))
    response = views.order_detail(RequestFactory().get("/orders/1/"), 1)
    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.content)["balance"] == 5


def test_charge_returns_true_and_debits(views):
    order = {"id": 1, "balance": 10}
    assert views.charge(order, 4) is True
    assert order["balance"] == 6


def test_charge_returns_false_when_short(views):
    order = {"id": 1, "balance": 3}
    assert views.charge(order, 4) is False
    assert order["balance"] == 3
