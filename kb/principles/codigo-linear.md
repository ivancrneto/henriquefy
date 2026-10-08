---
id: codigo-linear
title: Código linear: uma entrada, uma saída, sem caso especial
category: readability
weight: 4
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-na-pratica
    lesson: null
    section: "6.6"
    timestamp: null
  - type: course
    course: refatoracao-na-pratica
    lesson: 7
    section: "5"
    timestamp: null
  - type: course
    course: refatoracao-na-pratica
    lesson: 12
    section: "5"
    timestamp: null
  - type: course
    course: refatoracao-na-pratica
    lesson: 24
    section: "5"
    timestamp: null
---
**Rule.** A function reads top to bottom with one way in and one way out: input, processing,
output, in that order. Special cases are dissolved before the main path, not threaded through
it with flags. Every `if` has an `else`, and a default value is for the exception, set first,
then overridden by the normal case. An early return is allowed only as an abort at the top.

**Why Henrique says so.** Lesson 7 is the labyrinth lesson: nested conditions and multiple
exits make the reader carry state in their head, and his closing line is to keep the code
linear (digest sections 5, lesson 7, and 6.6). Lesson 12 adds the shape of a decision: an `if`
without an `else` hides a path, and the default-before-`if` form makes the exceptional case
explicit (digest section 5, lesson 12). In the wordcount refactoring he inverts conditions so
the stop condition comes first and the body stays flat (lesson 24, digest section 5). Entrada,
processamento, saída is the fractal he applies at every level (digest section 3).

**Looks like.** `result = default` then `if condition: result = other` then `return result`.
A guard clause at the top that aborts, then a single straight path. Bad: three nested `if`s with
a `return` in each branch and a `flag` variable updated along the way.

**How to detect.** Partial. A candidate rule `readability.multiple-returns`, not yet implemented:
a function with more than one `return` where the extra returns are not guard clauses at the top.
Judgment: flags carried through a function, special cases handled mid-path, input and output
mixed with processing.

**How to fix.** List the steps, separate input from processing from output, pull special cases
to the top as aborts or to a preparation step, give every `if` its `else` or its default, and
leave one `return`.
