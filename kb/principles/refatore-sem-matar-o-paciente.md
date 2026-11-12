---
id: refatore-sem-matar-o-paciente
title: Não mate o paciente, a classe nova serve primeiro ao código antigo
category: project
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-poo-legado
    lesson: null
    section: "6.3"
    timestamp: null
  - type: course
    course: refatoracao-poo-legado
    lesson: null
    section: "6.4"
    timestamp: null
  - type: course
    course: refatoracao-poo-legado
    lesson: 5
    section: "5"
    timestamp: "0:06:32"
    verified: false
  - type: course
    course: refatoracao-poo-legado
    lesson: 5
    section: "5"
    timestamp: "0:06:51"
    verified: false
  - type: course
    course: refatoracao-poo-legado
    lesson: 6
    section: "5"
    timestamp: "0:06:11"
    verified: false
  - type: course
    course: refatoracao-poo-legado
    lesson: 9
    section: "5"
    timestamp: "0:01:54"
    verified: false
---
**Rule.** To move logic out of legacy code into a new class, build the class under tests with
the interface the old code already uses, so the program keeps running at every step. Any
adapter that exists only for the old code is declared temporary and deleted once nothing calls
it.

**Why Henrique says so.** He does not throw the tutorial author's logic away, because the game
would stop working (Refatoração com POO em código legado, lesson 5, 0:06:43 to 0:06:51). He
builds a `Snake` class by tests and moves into it the logic that belongs to the snake, keeping
the interface with the game (lesson 5, 0:06:51 to 0:07:13, `verified: false`, transcript
paraphrase). The `__setitem__` that lets the old index-based algorithm work on the class is
temporary and he does not want to expose it (lesson 5, 0:06:32 to 0:06:40); index zero returning
the head is a temporary hack (lesson 8, 0:02:29); when nothing uses `__setitem__` any more it goes
(lesson 9, 0:01:54 to 0:01:58). He likes the exercise because it trains how to extract behavior
to make room to take the code where you want, without killing the software (lesson 6, 0:06:11 to
0:06:28, `verified: false`, transcript paraphrase).

**Looks like.** `class Snake` with `__getitem__` and a `__setitem__` commented as temporary, the
old loop still indexing `snake[0]`, tests green and the game runnable after each commit; a later
commit that drops `__setitem__`. Bad: a branch that replaces the loop and the data structure at
once and runs again only at the end.

**How to detect.** Judgment, with history in scope: a refactoring commit after which the program
or its tests did not run; an adapter method added "for now" that is still there with no callers.

**How to fix.** Give the new object the old interface first, move one behavior at a time with the
tests run between moves, and remove each adapter in the commit that removes its last caller.
Related: `execute-antes-de-ler`, `reescrever-e-outro-projeto`, `superficie-de-contato`.
