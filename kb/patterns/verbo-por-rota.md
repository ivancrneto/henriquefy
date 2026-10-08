---
id: verbo-por-rota
title: Verb declared per route
principle: o-verbo-comanda
category: api
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 5, section: "5"}
  fastapi: {origin: translated}
---
**What.** Each view declares which HTTP methods it accepts, and anything else gets
`405 Method Not Allowed` without the view running. In Django that is a decorator built with
`functools.wraps`, plus a dispatcher that sends each method of one resource URL to its own
function; in FastAPI the route decorator already is the declaration.

## django
Shape from lesson 5, where a decorator framework intercepts requests and validates the allowed
verbs so the views stay clean (digest section 5, lesson #5; section 11), and lesson 6, where one
resource URL is handled per method (section 5, lesson #6); our reconstruction, not his code.

```python
import functools
from http import HTTPStatus

from django.http import HttpResponse


def allow(*methods):
    allowed = tuple(m.upper() for m in methods)

    def decorator(view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method not in allowed:
                return HttpResponse(status=HTTPStatus.METHOD_NOT_ALLOWED, headers={"Allow": ", ".join(allowed)})
            return view(request, *args, **kwargs)
        return wrapper
    return decorator


@allow("GET", "DELETE")
def order(request, order_id):
    handlers = {"GET": read, "DELETE": cancel}
    return handlers[request.method](request, order_id)
```

`read` and `cancel` are plain views under their own `@allow`. `functools.wraps` keeps the
view's name and docstring for the URL resolver and the test output; `Allow` is what `405` asks for.

## fastapi
Our rendition, not his code. The per-method route decorators are the declaration; another
method on the same path gets `405` from the router, so there is nothing to write.

```python
from http import HTTPStatus
from fastapi import FastAPI

app = FastAPI()

@app.get("/orders/{order_id}")
def read(order_id: int):
    return represent(shop.get(order_id))

@app.delete("/orders/{order_id}", status_code=HTTPStatus.NO_CONTENT)
def cancel(order_id: int):
    shop.cancel(order_id)
```

## Bad
```python
path("order/create", views.create),   # urls.py: the action is in the path
path("order/delete", views.delete),

def create(request):  # views.py: any method works, including GET
    order = shop.place(**request.GET.dict())
    return HttpResponse(f"Order={order.id}")
```
