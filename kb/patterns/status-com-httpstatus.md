---
id: status-com-httpstatus
title: Status codes through HTTPStatus
principle: httpstatus-em-vez-de-numeros-magicos
category: readability
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 5, section: "5"}
  fastapi: {origin: translated}
---
**What.** Every status code in responses, tests and exception mappings is a named member of
`http.HTTPStatus` (in FastAPI, `fastapi.status` is the equivalent), never an integer literal. A
status that repeats gets a response class named after it, so a view reads `return Created(body)`.

## django
Shape from lesson 5, where `http.HTTPStatus` replaces magic numbers and responses get classes
with meaning (digest section 5, lesson #5; section 10); the code below is our reconstruction of
the lesson, not his verbatim code.

```python
import json
from http import HTTPStatus

from django.http import HttpResponse, JsonResponse

from cafe.service import order_url, shop


class Created(JsonResponse):
    status_code = HTTPStatus.CREATED

class NoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT


def create(request):
    order = shop.place(**json.loads(request.body))
    return Created({"id": order.id}, headers={"Location": order_url(request, order)})

def test_create_answers_201(client, payload):
    response = client.post("/orders", data=payload, content_type="application/json")
    assert response.status_code == HTTPStatus.CREATED
```

`HTTPStatus` is an `IntEnum`, so the class attribute works anywhere Django expects an `int`.

## fastapi
Our rendition, not his code. FastAPI ships `fastapi.status` (`HTTP_201_CREATED`); `http.HTTPStatus`
works just as well, since route decorators take an `int`. Pick one spelling per project.

```python
from http import HTTPStatus

from fastapi import FastAPI, Response, status

app = FastAPI()

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create(payload: OrderIn, response: Response):
    order = shop.place(**payload.model_dump())
    response.headers["Location"] = f"/orders/{order.id}"
    return {"id": order.id}

@app.delete("/orders/{order_id}", status_code=HTTPStatus.NO_CONTENT)
def cancel(order_id: int):
    shop.cancel(order_id)
```

## Bad
```python
def create(request):
    order = shop.place(**json.loads(request.body))
    return HttpResponse(json.dumps({"id": order.id}), status=201)

def test_create(client, payload):
    assert client.post("/orders", data=payload).status_code == 201
```
