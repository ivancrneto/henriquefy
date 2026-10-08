---
id: a-interface-e-o-que-importa
title: A interface é o que importa
category: api
weight: 5
detectable: judgment
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.1"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.1"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "7"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 1
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 3
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 6
    section: "5"
    timestamp: null
---
**Rule.** Design an API from its boundary inward. Decide first what the outside world needs to
say to the system and what it needs back, then decide how to sustain that inside. The database
schema, the ORM and the framework's shortcuts come last and never dictate the shape of the
interface.

**Why Henrique says so.** The first lesson is spent on the word itself: o importante é o
interface; a gente tá o tempo inteiro olhando para application e olhando para programming, mas o
relevante no que a API faz é o interface; entendendo o interface, o resto todo se resolve
(lesson #1, no timestamp, `verified: false`, digest section 7). An API is uma especificação de
como um software pode interagir com outro software (lesson #1, no timestamp, `verified: false`,
digest section 7): a layer of indirection that lets two systems cooperate without knowing each
other, and interfaces predate the web, from Unix pipes to POSIX (digest section 3.1). The
practical consequence comes in lesson 3: se você está desenvolvendo uma API e sua atenção está no
modelo do banco, repense: o mais importante é pensar para fora, na fronteira do sistema (lesson
#3, no timestamp, `verified: false`, digest section 6.1). Lesson 6 names the obstacle: the
challenge of API design is not using the framework but understanding why it hides from you the
boundary between the outer universe and the inner one of your code (lesson #6, digest section
6.1, paraphrase). The client is the thermometer: when consuming the API hurts, the design is at
fault, not the client (digest section 6.3, lesson #7).

**Looks like.** The course builds the coffee shop API top-down: lesson 3 starts with a
command-line client against a level 0 endpoint and keeps persistence light, a prevalence store
instead of a relational database, so the design is exercised before any table exists (digest
section 5, lesson #3; section 10). Lesson 8 draws the order's state machine before writing
code, and resources and verbs follow from what a customer does with an order (section 5, lesson #8). Bad: starting from `models.py`, generating one endpoint per
model and letting the ORM's field list become the response body, which he calls the level 2
trap: você começa a tentar fazer select automático a partir do modelo do banco de dados
refletido na API (lesson #6, no timestamp, `verified: false`, digest section 5).

**How to detect.** Judgment. A checker can only surface hints: response bodies built from
`model_to_dict`, `fields = "__all__"` or `vars(model)`; URL names that are table names; one
endpoint per model and no resource that is a process (a payment, a cancellation); no client,
test client or contract exercising the API from outside. None of these is a finding on its own.

**How to fix.** Write the client first, even as a script: what does the consumer send and what
does it need back. Name the resources from that conversation, not from the tables
(recurso-nao-e-entidade-de-banco). Draw the state machine if the resource has states
(hypermedia-como-maquina-de-estados). Only then map each representation onto whatever
persistence exists, and keep the mapping in one place (camada-de-servico) so the schema can
change without the boundary noticing.
