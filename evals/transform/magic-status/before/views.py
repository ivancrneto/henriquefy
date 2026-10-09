"""Orders API, Django function views. henriquefy transform fixture."""

import json

from django.http import JsonResponse

ORDERS = {}


class NotEnoughMoney(Exception):
    pass


def charge(order, amount):
    """Return True when the charge went through, False when the balance is short."""
    try:
        if amount > order["balance"]:
            raise NotEnoughMoney(order["id"])
        order["balance"] -= amount
        return True
    except NotEnoughMoney:
        return False


def create_order(request):
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "bad json"}, status=400)
    order = {"id": len(ORDERS) + 1, "balance": data.get("balance", 0)}
    ORDERS[order["id"]] = order
    return JsonResponse(order, status=201)


def order_detail(request, pk):
    order = ORDERS.get(pk)
    if order is None:
        return JsonResponse({"error": "not found"}, status=404)
    return JsonResponse(order, status=200)
