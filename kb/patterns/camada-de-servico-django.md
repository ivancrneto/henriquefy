---
id: camada-de-servico-django
title: Service layer under Django views
principle: camada-de-servico
category: modeling
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 9, section: "5"}
---
**What.** A plain Python object (`CoffeeShop`) owns the business operations of the resource: it
checks state, raises domain exceptions and persists. Views are three lines: parse the request,
call one operation, return the representation. The service imports nothing from Django, so it
is tested directly and reused by a script or a worker. Applies once a view starts holding
rules, which in the course happens at level 3.

## django
Shape from lesson 9, where logic moves out of the views into domain models and service-like
structures as the level 3 implementation grows (digest section 5, lesson #9; section 11); the
code is our reconstruction of the lesson, not his verbatim code.

```python
# cafe/service.py: no Django imports here
from decimal import Decimal

from cafe.domain import InvalidTransition, OrderNotFound, Status


class CoffeeShop:
    def __init__(self, store):
        self.store = store

    def get(self, order_id):
        try:
            return self.store[order_id]
        except KeyError:
            raise OrderNotFound(order_id) from None

    def pay(self, order_id, amount: Decimal):
        order = self.get(order_id)
        if order.status is not Status.AWAITING_PAYMENT:
            raise InvalidTransition(f"order {order_id} is {order.status.value}")
        if amount != order.price:
            raise InvalidTransition(f"expected {order.price}, got {amount}")
        order.status = Status.PREPARING
        return order

# cafe/views.py
@allow("PUT")
def payment(request, order_id):
    data = json.loads(request.body)
    order = shop.pay(order_id, Decimal(data["amount"]))
    return Ok(represent(request, order))
```

The rule `is not Status.AWAITING_PAYMENT` appears in the service only, and the middleware turns
`InvalidTransition` into `409`. The view knows the wire format and nothing else.

## Bad
```python
@allow("PUT")
def payment(request, order_id):
    data = json.loads(request.body)
    if order_id not in store:
        return HttpResponse(status=404)
    order = store[order_id]
    if order.status != "awaiting_payment":
        return HttpResponse(status=409)
    order.status = "preparing"
    store.save(order)
    return JsonResponse({"id": order.id, "status": order.status, "links": {"self": f"/orders/{order.id}"}})
```
