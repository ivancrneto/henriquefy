---
id: erros-na-fronteira
title: Erros na fronteira
category: errors
weight: 4
detectable: partial
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "9.4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "11"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 6
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 8
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 9
    section: "5"
    timestamp: null
---
**Rule.** The domain raises named exceptions and knows nothing about HTTP. One piece of code at
the boundary, a middleware or an exception handler, maps each exception type to a status code
and a response shape. Views do not catch domain errors to build error responses, and domain
code never imports a response class.

**Why Henrique says so.** Lesson 6 introduces middlewares to handle exceptions such as the 404
and to standardize responses (digest section 5, lesson #6; section 11), taking error handling
out of the views. Lesson 8, while modeling the state machine and before any code exists,
derives the exception from the model: a existência da possibilidade de conflito já indica para
mim que eu vou ter um novo tipo de exceção; eu nem vi o código ainda, eu estou aqui para fazer
a gente pensar (lesson #8, no timestamp, `verified: false`, digest section 6.4). That exception
becomes `409 Conflict` when the client attempts an operation the current state forbids (section
5, lesson #8; section 9.4), and lesson 9 handles `404` and `405` the same way while cleaning up
the level 3 implementation (section 5, lesson #9). It is prefira-excecoes-a-booleanos carried
to the boundary: outcomes have names, and the translation to transport happens once.

**Looks like.** A domain module with `class OrderNotFound(Exception)` and
`class InvalidTransition(Exception)`, raised by the service when the order does not exist or
its state forbids the action; a middleware table
`{OrderNotFound: HTTPStatus.NOT_FOUND, InvalidTransition: HTTPStatus.CONFLICT}` (pattern
excecao-para-http). Bad: `try: order = shop.get(id) except KeyError: return
HttpResponse(status=404)` repeated in every view; or a service that raises
`HTTPException(409)` from inside the domain, welding the model to one transport.

**How to detect.** Partial. Mechanical candidates: `HttpResponse`, `JsonResponse`,
`JSONResponse` or `HTTPException` imported or raised in a module that otherwise imports no web
framework (candidate rule `errors.http-in-domain`, not yet implemented); the same `except X: return <response>` pair repeated
across views (candidate rule `errors.repeated-except-response`, not yet implemented); `raise Http404` inside a function that is
not a view. Judgment: whether a given exception is a domain outcome or a transport error, and
which status fits it (`409` versus `422` versus `400`).

**How to fix.** Name the outcomes as exception classes in the domain module. Raise them where
the outcome is known. Write one handler at the boundary that maps type to status and body, and
register it once (Django middleware, FastAPI `exception_handler`). Delete the `try/except` from
the views; the ones that remain should be about request parsing, not business rules. Add the
`409` mapping as soon as the state machine shows a transition that can be refused.
