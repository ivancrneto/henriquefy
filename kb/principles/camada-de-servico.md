---
id: camada-de-servico
title: Camada de serviço
category: modeling
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "7"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "11"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 7
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 9
    section: "5"
    timestamp: null
---
**Rule.** Business rules live in domain objects and in a service layer that the views call;
views parse the request, call one service operation, and build the response. Let the layer
appear when the code asks for it: start in the view, and move logic out when the view has
grown past what one reader can hold.

**Why Henrique says so.** In lesson 9, as the level 3 implementation grows, logic leaves the
Django views for domain models and service-like structures, a separation of responsibilities he
describes as emerging rather than planned: o código vai ajudando a gente a chegar nessa camada
de serviço (lesson #9, no timestamp, `verified: false`, digest section 5). Section 11 records
the problem it solves: taking business logic out of views as the code grows. His order of work
is the one from lesson 7: vou fazendo funcionar; depois que funcionar, o código pede pelo amor
de Deus: 150 linhas, 250 linhas, ele vai pedindo me organiza melhor (lesson #7, no timestamp,
`verified: false`, digest section 6.2). This is deixe-o-codigo-descansar applied to web code:
the layer is extracted after it is visible, not designed up front. Lesson 9 also warns against
the opposite failure, generalizing until você para de fazer um sistema e começa a fazer um
framework (lesson #9, no timestamp, `verified: false`, digest section 7).

**Looks like.** A `CoffeeShop` object with `place(...)`, `pay(order_id, amount)` and
`cancel(order_id)` that checks the state, raises domain exceptions and persists; views of three
or four lines each that decode the body, call one of those and return the representation with
its links (pattern camada-de-servico-django). Tests hit the service directly for the rules and
the view for the contract. Bad: a view that validates fields, checks `order.status`, updates
it, converts money and builds links in sixty lines, with the same checks copied into the next
view.

**How to detect.** Judgment. Hints a checker can collect: view functions longer than roughly
thirty statements; `.status` or `.state` comparisons inside views; the same mutation sequence on
a model in two views; domain modules importing `django.http` or `fastapi`. A domain module that
imports nothing from the framework is the positive signal.

**How to fix.** Make it work in the view first. When two views share a rule, or one view reads
past a screen, move the rule into a method on the domain object or into a service function
named after the user's action. Replace the view's body with parse, call, respond. Keep the
service free of request and response objects, so it can be tested without the web client.
