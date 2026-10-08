---
id: links-por-estado
title: Links derived from the resource state
principle: hypermedia-como-maquina-de-estados
category: api
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 9, section: "5"}
---
**What.** The representation of a stateful resource carries a `links` object whose keys are the
transitions available in the current state (`self`, `update`, `cancel`, `pay`) and whose values
are absolute URLs. One function computes the links from the state; every view that returns the
resource calls it. A transition missing from `links` is refused by the service with a domain
exception mapped to `409` (pattern excecao-para-http).

## django
Shape from lesson 9, where the links `self`, `update`, `cancel` and `pay` are derived from the
order's status instead of a fixed list (digest section 5, lesson #9; section 9.4), over the
state machine drawn in lesson 8 (section 5, lesson #8); the code is our reconstruction of the
lesson, not his verbatim code.

```python
from enum import Enum

from django.urls import reverse


class Status(Enum):
    AWAITING_PAYMENT = "awaiting_payment"
    PREPARING = "preparing"
    DELIVERED = "delivered"


TRANSITIONS = {
    Status.AWAITING_PAYMENT: ("update", "cancel", "pay"),
    Status.PREPARING: (),
    Status.DELIVERED: (),
}

ROUTES = {"self": "order", "update": "order", "cancel": "order", "pay": "payment"}


def links_for(request, order):
    relations = ("self", *TRANSITIONS[order.status])
    return {rel: request.build_absolute_uri(reverse(ROUTES[rel], args=[order.id])) for rel in relations}


def represent(request, order):
    body = order.as_dict()
    body["links"] = links_for(request, order)
    return body
```

`TRANSITIONS` is the lesson 8 state machine written as data: a new state is a new row, not a
new `if`. Views call `represent` on every return, so the client always sees its current
options, and the payment test asserts that `update` and `cancel` disappear afterwards.

## Bad
```python
def read(request, order_id):
    order = shop.get(order_id)
    body = order.as_dict()
    body["links"] = {
        "self": f"/orders/{order.id}",
        "update": f"/orders/{order.id}",
        "cancel": f"/orders/{order.id}",
        "pay": f"/payments/{order.id}",
    }  # same links in every state; the client has to know when cancel is allowed
    return Ok(body)
```
