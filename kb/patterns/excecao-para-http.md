---
id: excecao-para-http
title: Domain exceptions mapped to HTTP at the boundary
principle: erros-na-fronteira
category: errors
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 6, section: "5"}
  fastapi: {origin: translated}
---
**What.** The domain raises its own exceptions (`OrderNotFound`, `InvalidTransition`) and never
imports a response class. One component at the boundary holds the table from exception type to
status code: a middleware in Django, `exception_handler` registrations in FastAPI. Views stop
catching domain errors.

## django
Shape from lesson 6, where middlewares take over exception handling such as the 404 and
standardize responses (digest section 5, lesson #6), plus the `409` of lessons 8 and 9 (section
9.4); the code is our reconstruction of the lesson, not his verbatim code.

```python
# cafe/domain.py: no Django imports here
class OrderNotFound(Exception): ...
class InvalidTransition(Exception): ...

# cafe/middleware.py
from http import HTTPStatus
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from cafe.domain import InvalidTransition, OrderNotFound

class DomainErrorsToHttp(MiddlewareMixin):
    STATUS = {OrderNotFound: HTTPStatus.NOT_FOUND, InvalidTransition: HTTPStatus.CONFLICT}

    def process_exception(self, request, exc):
        for exc_type, status in self.STATUS.items():
            if isinstance(exc, exc_type):
                return HttpResponse(status=status)
        return None
```

Register it in `MIDDLEWARE`. Returning `None` leaves unknown exceptions on Django's default
500 path, so the table names only the outcomes the domain actually has.

## fastapi
Our rendition, not his code. `@app.exception_handler` is the same table, one decorator per
exception type; route functions call the service and return, and never see the handlers.

His 2026 FastAPI code has no such handler. In `henriquebastos/hamsterdan` at commit
`5d382467eaa4ff837cbd6b93012c99081e0153f9` the route catches the domain exception itself and
turns it into `HTTPException`: `except WebhookRejected as error: raise
HTTPException(status_code=400, detail=str(error)) from None` (`src/hamsterdan/host/api.py`
46-49), and the body-size refusal is raised inline four lines earlier (43-44). The replacement
tree does the same with a response function instead of an exception: `except
WebhookRefusalError as error: return refusal_response(error.reason)` and `except
WebhookInboxCapacityError: return refusal_response("inbox_capacity_exhausted")`
(`src/hamsterdan2/host/api.py` 51-59), where `refusal_response` (29-34) is the type-to-status
table in function form, called from the route rather than registered on the app. The domain
half of the principle holds in both trees: `class WebhookRejected(ValueError)` lives in
`src/hamsterdan/github_app/webhooks.py` 45-46 and knows nothing about HTTP, and
`tests/test_architecture.py` 155-158 fails the build if FastAPI is imported outside `host`.
The one-table half is per route. The closest thing to the table in his code is in
`henriquebastos/petrus` at commit `3f85fc2094e50ece48bcf6bf9ace19cb0a22a544`,
`src/petrus/simulation_http.py` 29-32 and 230-235: a private `_RequestError(status, code,
message)` raised by every validator and mapped once in `_dispatch`, with `http.server` and
`http.HTTPStatus` instead of a framework.

```python
from http import HTTPStatus
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from cafe.domain import InvalidTransition, OrderNotFound

app = FastAPI()

@app.exception_handler(OrderNotFound)
def order_not_found(request: Request, exc: OrderNotFound):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"detail": str(exc)})

@app.exception_handler(InvalidTransition)
def invalid_transition(request: Request, exc: InvalidTransition):
    return JSONResponse(status_code=HTTPStatus.CONFLICT, content={"detail": str(exc)})
```

## Bad
```python
def cancel(request, order_id):
    try:
        order = shop.get(order_id)
    except KeyError:
        return HttpResponse(status=404)
    if order.status != "awaiting_payment":
        return HttpResponse(status=409)
    shop.cancel(order)
    return HttpResponse(status=204)
```
