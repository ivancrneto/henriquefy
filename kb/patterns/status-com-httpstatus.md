---
id: status-com-httpstatus
title: Status codes through HTTPStatus
principle: httpstatus-em-vez-de-numeros-magicos
category: readability
frameworks:
  django:  {origin: course, course: design-api-na-pratica, lesson: 5, section: "5"}
  fastapi: {origin: his, repo: henriquebastos/hamsterdan, path: src/hamsterdan/host/api.py, commit: 5d382467eaa4ff837cbd6b93012c99081e0153f9}
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
His code: `src/hamsterdan/host/api.py` 32-50 in `henriquebastos/hamsterdan` at commit
`5d382467eaa4ff837cbd6b93012c99081e0153f9` (2026, Apache-2.0). The webhook route declares its
success status by name on the decorator; the two refusals a few lines later pass a bare `400`.

```python
    app = FastAPI(title="Hamsterdan host", lifespan=lifespan)

    @app.get("/healthz")
    def health() -> dict[str, object]:
        return service.health()

    @app.post("/github/webhooks", status_code=status.HTTP_202_ACCEPTED)
    async def webhook(request: Request) -> dict[str, str]:
        body = bytearray()
        async for chunk in request.stream():
            body.extend(chunk)
            if len(body) > MAX_BODY_BYTES:
                raise HTTPException(status_code=400, detail="request body is too large")
        headers = [(name.decode("latin-1"), value.decode("latin-1")) for name, value in request.scope["headers"]]
        try:
            receipt = await asyncio.to_thread(service.custody.receive, headers, bytes(body))
        except WebhookRejected as error:
            raise HTTPException(status_code=400, detail=str(error)) from None
        return {"custody": "durable", "delivery_id": receipt.delivery_id, "disposition": receipt.disposition}
```

Line 38 is the principle: `status.HTTP_202_ACCEPTED` names the meaning. Lines 44 and 49 are
against it: `HTTPException(status_code=400, ...)` is the magic number the course removes in
lesson 5, and rule `api.magic-status` fires on both. The form he teaches is
`status.HTTP_400_BAD_REQUEST` or `HTTPStatus.BAD_REQUEST`. His own replacement tree in the same
repository does it that way: `status.HTTP_503_SERVICE_UNAVAILABLE if reason ==
"inbox_capacity_exhausted" else status.HTTP_400_BAD_REQUEST` (`src/hamsterdan2/host/api.py` 31,
same commit). The tests for this route also compare bare integers, `assert response.status_code
== 202` (`tests/integration/host/test_service.py` 402), where the course would write
`HTTPStatus.ACCEPTED`. `http.HTTPStatus` is never imported anywhere in hamsterdan; `fastapi.status`
is the only named form he uses there, and either spelling satisfies the principle.

## Bad
```python
def create(request):
    order = shop.place(**json.loads(request.body))
    return HttpResponse(json.dumps({"id": order.id}), status=201)

def test_create(client, payload):
    assert client.post("/orders", data=payload).status_code == 201
```
