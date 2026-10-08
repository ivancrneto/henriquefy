---
id: recurso-nao-e-entidade-de-banco
title: Recurso não é entidade de banco de dados
category: api
weight: 4
detectable: judgment
era: timeless
scope: api
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "3.5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "7"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 2
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
**Rule.** A resource is a projection of something in the world that is useful to a consumer in
some context, not a row in a table. Resources can be processes, workflows and transitions (a
payment, a cancellation) that are never persisted as such; one table may back several
resources, and some resources have no table at all.

**Why Henrique says so.** Lesson 2 defines the term: o recurso não é a coisa em si; o recurso é
uma projeção, uma interpretação que eu dou de algo que existe no mundo (lesson #2, no timestamp,
`verified: false`, digest section 3.2), and removes the persistence assumption outright: o
recurso da sua API não precisa ser algo que vai ser guardado no banco (lesson #2, no timestamp,
`verified: false`, digest section 7). The digest records the classic error as confusing a
resource with a table, and notes that a resource may be a process or a workflow (section 3.2).
The reason it matters is coupling: the web's architecture exists to give low coupling and
isolation, so parts evolve independently, and APIs that mirror database models destroy exactly
that (section 3.5). Lesson 6 says what happens when the ORM dictates the design: o problema do
nível 2 é que você começa a tentar fazer select automático a partir do modelo do banco de dados
refletido na API; vira uma cagada, porque não é para isso (lesson #6, no timestamp,
`verified: false`, digest section 5). The digest calls this programming by coincidence (section
5, lesson #6).

**Looks like.** In the level 3 model of lesson 8, the order moves through aguardando pagamento,
preparando, entregue and concluído, and the actions a customer takes (pay, cancel, update)
become addressable things with their own verbs, status codes and links (digest section 5,
lesson #8; section 9.4). Paying is a resource even if the shop stores no payment table; it is
the transition that matters to the consumer. Bad: `GET /orders`, `POST /orders`,
`GET /order_items`, one mirror per model, with the state machine left for the client to
reconstruct from field values.

**How to detect.** Judgment. Hints a checker can list: every URL pattern names a model class in
lowercase and nothing else; serializers or forms declared with `fields = "__all__"`; response
keys identical to column names including `*_id` foreign keys; no resource whose name is an
action or a step. Each is common in acceptable code too, so report them as context, not as a
finding.

**How to fix.** List what the consumer needs to do, in the consumer's words. For each item ask
whether it is a thing (a noun with an identifier) or a step in a process; steps get their own
resource, with a verb chosen by its meaning (o-verbo-comanda). Then map resources onto
persistence in a service layer (camada-de-servico), accepting that one table may serve several
resources and that some resources have no table.
