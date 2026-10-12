---
id: fluxo-antes-da-estrutura
title: Entenda a estrutura, depois o fluxo, e mude a estrutura mantendo o fluxo
category: modeling
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-rapida
    lesson: null
    section: "6.1"
    timestamp: null
  - type: course
    course: refatoracao-rapida
    lesson: 4
    section: "5"
    timestamp: "0:03:33"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 3
    section: "5"
    timestamp: "0:02:39"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 8
    section: "5"
    timestamp: "0:08:07"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 16
    section: "5"
    timestamp: "0:02:08"
    verified: false
---
**Rule.** When refactoring, read the structure only to find the flow: what the program does,
step by step, from its entry point. Then change the structure so the flow stays the same and
becomes easier to see. Do not introduce new structure (a type, a class, a pattern) while the
flow is still tangled; get the flow right with plain functions first, and the right structure
shows up afterwards.

**Why Henrique says so.** He states the order as the core of the method: first understand what
structure that is, from there understand the flow, and then change the structure to keep the
flow (lesson 4, 0:03:33 to 0:03:41, `verified: false`, transcript paraphrase). Beginners look
only at the structure and never at the flow (lesson 3, 0:02:39 to 0:02:46). When a student
proposes a coordinate type in the middle of the work he refuses it: you will not have structure
today, today is a day of flow, not of structure (lesson 8, 0:08:07, `verified: false`,
transcript paraphrase). At the end of the course the payoff is that a class would now be easy,
because they never got stuck in the class structure trying to fit things; they built small
abstractions first, and the class is a later choice (lesson 16, 0:02:08 to 0:02:55). Digest
sections 3.1 and 6.1.

**Looks like.** A refactoring that first extracts `set_pixel(board, x, y, color)` and
`region(x1, y1, x2, y2)` as functions, keeps every command's behavior under test, and only at
the end considers a `Board` class. Bad: a refactoring that opens with `class Coordinate` and
`class Board` and then tries to fit the old commands into them.

**How to detect.** Judgment. A refactoring diff whose first commits add classes or type
hierarchies while the old procedural flow is still in place; new structure with no test showing
the flow unchanged.

**How to fix.** Run the program, read it from the entry point simulating execution, write a test
that pins each path (see `execute-antes-de-ler`). Then move one step at a time with functions,
keeping the tests green. Introduce a class only when the functions already show what it holds.
See `nao-projete-a-generalizacao`.
