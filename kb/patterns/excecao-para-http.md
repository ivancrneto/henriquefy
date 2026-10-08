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
