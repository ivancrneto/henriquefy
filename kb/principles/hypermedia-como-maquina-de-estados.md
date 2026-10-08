---
id: hypermedia-como-maquina-de-estados
title: Hypermedia como máquina de estados
category: api
weight: 4
detectable: judgment
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.3"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "7"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "9.4"
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
**Rule.** When a resource has states, the server owns the transitions and tells the client which
ones are available now, as links in the representation. The client follows links instead of
building URLs and instead of re-implementing the rules that say when an action is allowed. A
link that is absent is an action that is not possible.

**Why Henrique says so.** No nível 3, o que eu vou usar é o HTTP como uma máquina de estado da
aplicação (lesson #8, no timestamp, `verified: false`, digest section 5). Lesson 8 models the
order's states (sem pedido, aguardando pagamento, preparando, entregue, concluído) before any
code and makes the server responsible for transitions: cancel and update happen only when the
state permits, and the links in the response tell the client what is available (section 5,
lesson #8). Lesson 9 implements it: existe uma relação entre links possíveis e o status da sua
ordem (lesson #9, no timestamp, `verified: false`, digest section 7), and the code is refactored
to derive links from the domain state instead of a fixed list (section 5, lesson #9; section
9.4). The point is decoupling: o importante é você desacoplar um pouco mais o cliente; você diz
para ele não apenas qual é o link, mas como navegar até ele (lesson #9, no timestamp,
`verified: false`, digest section 5). Climbing the maturity levels is not dogma: it is done to
reduce work by using the patterns the web already offers (section 4, lesson #3).

**Looks like.** An order awaiting payment answers with `self`, `update`, `cancel` and `pay`; the
same order after payment answers with `self` only, and a `DELETE` on it gets `409` (section 9.4;
pattern links-por-estado). The client's loop is: read the representation, pick a link by its
relation name, follow it. Bad: a client that hardcodes `/orders/{id}/cancel` and checks
`if order["status"] == "paid"` before calling it, duplicating the server's rules in every
consumer; a server that returns the same link set in every state.

**How to detect.** Judgment. Hints: a `status` or `state` field in representations and no
`links` key; clients in the repository that format URLs from templates; the same predicate on
state (`if status ==`) present in both server and client code; a `409` that is never issued.
None of these can be scored without reading the domain.

**How to fix.** Draw the state machine first (section 6.4). For each state list the allowed
transitions; each becomes a link relation. Compute the links from the state in one function and
attach them to every representation of the resource. Refuse transitions the state forbids with
a domain exception mapped to `409` (erros-na-fronteira). Then simplify the client until it only
follows links.
