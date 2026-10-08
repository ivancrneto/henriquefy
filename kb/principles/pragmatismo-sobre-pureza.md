---
id: pragmatismo-sobre-pureza
title: Pragmatismo sobre pureza
category: simplicity
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "6.4"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "7"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 3
    section: "5"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 9
    section: "5"
    timestamp: null
---
**Rule.** Treat design choices as trade-offs with costs and benefits, never as right versus
wrong. Make it work first and make it pretty after. Let the work be pulled by the need at hand
rather than pushed by a preconception of the ideal solution, and stop abstracting when the
abstraction stops being practical.

**Why Henrique says so.** He frames the whole course this way in lesson 1: o desafio desse
programa é fazer um conteúdo puxado pela necessidade do aluno e não empurrado por uma
preconcepção do que seria o ideal de falar sobre API (lesson #1, no timestamp,
`verified: false`, digest section 2). Lesson 3 gives the rule for decisions: não trate as coisas
como certo e errado, trate como trade-off, como escolha (lesson #3, no timestamp,
`verified: false`, digest sections 2 and 6.4), and applies it to the maturity model itself,
which is climbed to reduce work, not out of dogma (section 4). Lesson 9 gives the order of
work, primeiro faz funcionar, depois faz bonito (lesson #9, no timestamp, `verified: false`,
digest section 2), and the limit on abstraction: quanto mais você tenta abstrair, menos prático
você fica (lesson #9, no timestamp, `verified: false`, digest section 6.2). The companion
warning is the framework trap, where você para de fazer um sistema e começa a fazer um
framework (lesson #9, no timestamp, `verified: false`, digest section 7).

**Looks like.** Lesson 3 keeps persistence light, a prevalence store rather than a relational
database, because the design is what is being exercised and the database would be weight
without benefit at that stage (digest section 5, lesson #3; section 11). Lesson 9 serializes
`Decimal` and handles `404` and `405` as they come up, cleaning after the feature works (section
5, lesson #9). Bad: a hypermedia layer on an internal API with one consumer; a generic resource
framework written before the second resource existed; a refactor argued from purity (it is not
REST) rather than from a cost.

**How to detect.** Judgment only. Signals in review: abstractions with a single user;
configuration for cases that do not occur; a history where structure precedes behavior; review
comments that cite a rule without naming the cost it avoids.

**How to fix.** Name the need that pulls the change and the cost of not making it. Ship the
working version. Refactor only toward a pain you can point at (deixe-o-codigo-descansar). When
a generalization is tempting, write the second concrete case first and let it ask for the
abstraction; if it does not ask, leave the duplication.
