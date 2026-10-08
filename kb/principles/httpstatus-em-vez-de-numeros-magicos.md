---
id: httpstatus-em-vez-de-numeros-magicos
title: HTTPStatus em vez de números mágicos
category: readability
weight: 3
detectable: mechanical
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: 5
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "9.3"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "10"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "11"
    timestamp: null
---
**Rule.** Never write an HTTP status code as a bare integer. Use `http.HTTPStatus` from the
standard library (`HTTPStatus.CREATED`, `HTTPStatus.NOT_FOUND`) in responses, in tests and in
every mapping, so the code names the meaning and the reader does not translate numbers.

**Why Henrique says so.** In lesson 5, moving the coffee shop from level 0 to level 1, he
replaces error strings with real status codes and adopts `http.HTTPStatus` so the codes are
readable and maintainable; the digest records it as the end of magic numbers (section 5,
lesson #5; section 10). Section 11 lists the tool next to the problem it solved: eliminate
magic status numbers and make the code more readable and maintainable. The broader point is in
section 6.2: raising from primitive types (status numbers) to classes with domain meaning
improves the intent of the code (lesson #5, digest paraphrase; no verbatim quote recorded).
Section 9.3 places the same move in the level 2 narrative, where status codes start to carry
meaning: 201 for creation, 204 for deletion, 404 and 405 for the two classic failures. Once a
code means something, its name belongs in the source.

**Looks like.** Lesson 5's response classes carry the status in their name and use the enum for
the value (digest section 10, lesson #5; pattern status-com-httpstatus):

```python
from http import HTTPStatus
from django.http import HttpResponse

class Created(HttpResponse):
    status_code = HTTPStatus.CREATED
```

Tests read the same way: `assert response.status_code == HTTPStatus.CONFLICT` says what was
expected without a comment. Bad: `return HttpResponse(status=409)`,
`assert response.status_code == 204`, a middleware table such as `{DoesNotExist: 404}`.

**How to detect.** Mechanical. Rule `api.magic-status`: an integer literal between 100 and 599
passed as `status=` or `status_code=` to a response constructor or route decorator, compared
with a `.status_code` attribute, assigned to a `status_code` class attribute, or given to
`HTTPException(status_code=...)`. `HTTPStatus.X`, `status.HTTP_X` and a named constant are the
allowed forms. Ports and sizes in the same range are ruled out by the keyword context.

**How to fix.** `from http import HTTPStatus`, then replace each literal with the member of the
same value; the enum is an `IntEnum`, so comparisons and `status=` arguments keep working. In
FastAPI, `fastapi.status.HTTP_201_CREATED` is equivalent and also fine. When the same status
repeats across views, give it a response class named after it, as lesson 5 does.
