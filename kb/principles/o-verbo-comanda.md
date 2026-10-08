---
id: o-verbo-comanda
title: O verbo comanda
category: api
weight: 4
detectable: partial
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "9.3"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 5
    section: "5"
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
---
**Rule.** The URI names the resource and the HTTP method says what to do with it. `POST`
creates, `GET` reads without side effects, `PUT` replaces the whole representation, `PATCH`
changes part of it, `DELETE` removes, and the status code tells the outcome. Actions never live
in the path, and a method the resource does not support gets `405`.

**Why Henrique says so.** This is Richardson level 2 in his reading of the model. Level 1 has
URIs per resource but, as he puts it, a gente fica preso geralmente a um único verbo HTTP
(lesson #5, no timestamp, `verified: false`, digest section 5). Level 2 treats the API as
collections of resources manipulated by `POST`, `GET`, `PUT`, `PATCH` and `DELETE`, with status
codes that mean something (digest section 4; section 5, lesson #6). The uniform interface is
the reason: few verbs over many nouns, which is what lets clients and servers evolve
independently (section 3.5). He is precise about `PUT`: você não manda só o atributo que está
mudando, você manda tudo de novo (lesson #6, no timestamp, `verified: false`, digest section
9.3). Lesson 8 adds the rule for choosing: pick the verb by the meaning of the user's action in
the real world, not by technical CRUD (section 5, lesson #8). Level 0's `GET` that creates an
order is the counterexample he starts from (section 9.1, lesson #3).

**Looks like.** Lesson 5 introduces a decorator that declares which methods a view accepts and
answers `405` to the others; lesson 6 routes one resource URL to a different function per
method (digest section 5, lessons #5 and #6; pattern verbo-por-rota). Creation answers `201`
with a `Location` header, deletion `204` (section 9.3). Bad: `POST /orders/1/cancel` when
`DELETE /orders/1` says the same thing; `GET /PlaceOrder?coffee=latte` creating state; a view
that never reads `request.method`.

**How to detect.** Partial. Mechanical candidates: path segments that are verbs (`create`,
`read`, `update`, `delete`, `get`, `list`, `add`, `remove`) in URL patterns or route decorators
(rule `api.verb-in-uri`); a `GET` handler that calls `save()`, `create()`, `delete()` or a
service method named like a mutation (rule `api.get-with-side-effect`); views routed for every
method that never read `request.method`. Judgment: whether `PUT` really replaces or should be
`PATCH`; whether cancel is a `DELETE` on the order or a `POST` to a cancellation resource; `405`
versus `404` for an unknown method on a known resource.

**How to fix.** Collapse `/resource/<action>` routes into one path per collection and one per
item. Declare the accepted methods on each view (verbo-por-rota) and return `405` otherwise.
Move the action's meaning into the method and the outcome into the status: `201` plus
`Location` on create, `204` on delete, `409` when the state forbids it (erros-na-fronteira).
Keep `GET` free of side effects so it can be cached.
