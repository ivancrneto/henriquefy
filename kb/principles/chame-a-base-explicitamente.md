---
id: chame-a-base-explicitamente
title: Chame o __init__ da base explicitamente
category: modeling
weight: 3
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: raio-x-da-oo
    lesson: null
    section: "6.9"
    timestamp: null
  - type: course
    course: raio-x-da-oo
    lesson: 5
    section: "5"
    timestamp: "0:02:09"
    verified: false
  - type: course
    course: raio-x-da-oo
    lesson: 5
    section: "5"
    timestamp: "0:02:38"
    verified: false
---
**Rule.** When a subclass defines `__init__`, the base class's `__init__` does not run on its
own; the subclass method replaces it. If the base initialization matters, call it yourself with
`super().__init__(...)`, and decide whether it runs before or after your own setup.

**Why Henrique says so.** In lesson 5 he overrides `__init__` in a subclass and shows that the
base version is simply gone unless called: the method of the subclass substitutes the one of
the base, and you control if and when the base one runs (lesson 5, 0:02:09 to 0:02:35,
`verified: false`, transcript paraphrase). He then explains what `super()` really does: it
holds the resolution logic for which prior class in the hierarchy gets the call, which is what
makes multiple inheritance workable (lesson 5, 0:02:38 to 0:02:55, `verified: false`,
transcript paraphrase).

**Looks like.** `def __init__(self, name): super().__init__(); self.name = name`. Bad: a
subclass `__init__` that sets its own attributes and silently skips the base's, leaving the
instance half-built.

**How to detect.** Partial. A candidate rule `modeling.init-without-super`, not yet implemented:
a class with a project-defined base that defines `__init__` and never calls `super().__init__`
or `Base.__init__`. Judgment: whether the base initialization was meant to be skipped.

**How to fix.** Add the `super().__init__(...)` call with the arguments the base expects, in
the position that matches the order you need; if the base has nothing to initialize, say so in
a comment rather than leaving the reader to wonder.
