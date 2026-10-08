---
id: deixe-o-codigo-descansar
title: Deixe o código descansar
category: simplicity
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.1"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 23
    section: "10"
    timestamp: "0:00:00"
    verified: false
---
**Rule.** Before refactoring, let the code sit until you understand it. Write the thing, run
it, live with it, and only then reshape it. Do not refactor while the problem is still moving in
your head, and do not design the generalization before the code has asked for it.

**Why Henrique says so.** He opens the last lesson of the OO course by calling this the one
fundamental technique of programming in any paradigm: existe uma técnica fundamental quando você
programa em qualquer paradigma, sobre objetos não é diferente; essa técnica é deixar o código
descansar (lesson 23, 0:00, `verified: false`, transcript paraphrase). The course itself is built
on it: four lessons of modeling before a line of code, and the refactoring of `Game.run` only
after the simulator already worked and its technical debt could be seen (digest section 12.1).
Resting is what lets the debt show: the same information living in two places, chained dots
that reveal coupling, a name that does not fit.

**Looks like.** In `monopoly`, lesson 23 refactors a working `Game` after the whole simulator has
run thousands of games: the players lived in both `Game` and `Board`, so a new `Competitors`
entity is extracted, named only after `PlayerCollection` was tried and rejected. Bad: pulling a
base class out of the first two classes you wrote, or renaming and restructuring in the same
session that produced the code.

**How to detect.** Judgment only. Signals in a review: a refactor commit that follows the feature
commit by minutes; abstractions with a single implementation; a `Base*` class introduced before
the second concrete case existed. No mechanical rule.

**How to fix.** Finish the behavior under test first. Leave it. Come back when the pain is
concrete and nameable (duplicated state, chained access, a wrong name), and extract exactly the
entity that pain points at. The same rule applied to abstractions is nao-projete-a-generalizacao (digest section 12.2).
