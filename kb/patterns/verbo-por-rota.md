---
id: verbo-por-rota
title: Verb declared per route
principle: o-verbo-comanda
category: api
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 5, section: "5"}
  fastapi: {origin: his, repo: henriquebastos/hamsterdan, path: src/hamsterdan/host/api.py, commit: 5d382467eaa4ff837cbd6b93012c99081e0153f9}
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
His code: `src/hamsterdan/host/api.py` 32-39 in `henriquebastos/hamsterdan` at commit
`5d382467eaa4ff837cbd6b93012c99081e0153f9` (2026, Apache-2.0). Two routes, two nouns, and the
method is the only verb in sight.

```python
    app = FastAPI(title="Hamsterdan host", lifespan=lifespan)

    @app.get("/healthz")
    def health() -> dict[str, object]:
        return service.health()

    @app.post("/github/webhooks", status_code=status.HTTP_202_ACCEPTED)
    async def webhook(request: Request) -> dict[str, str]:
```

`/healthz` is read with `GET`; `/github/webhooks` receives a delivery with `POST`. The path
never says `receive` or `check`; the decorator does, and a `DELETE /github/webhooks` gets `405`
from the router before any of his code runs. The replacement tree keeps the same resource name
under a different app: `@app.post("/github/webhooks", status_code=status.HTTP_200_OK)`
(`src/hamsterdan2/host/api.py` 49, same commit). The function names are nouns or the event
they handle (`health`, `webhook`, `receive`), not `get_health` or `post_webhook`; rule
`api.verb-in-uri` has nothing to flag here.

See also the Django shape written by hand in the standard library, in `henriquebastos/petrus`
at commit `3f85fc2094e50ece48bcf6bf9ace19cb0a22a544`, `src/petrus/simulation_http.py` 218-225
and 237-240: a per-path `Allow` string (`"GET, OPTIONS"`) and `if method not in allow.split(",
"): self._error(HTTPStatus.METHOD_NOT_ALLOWED, "method_not_allowed", "method not allowed",
allow=allow)`, which is the `allow` decorator above as a method on the request handler.

## Bad
```python
path("order/create", views.create),   # urls.py: the action is in the path
path("order/delete", views.delete),

def create(request):  # views.py: any method works, including GET
    order = shop.place(**request.GET.dict())
    return HttpResponse(f"Order={order.id}")
```
