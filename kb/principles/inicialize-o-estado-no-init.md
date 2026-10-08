---
id: inicialize-o-estado-no-init
title: Inicialize o estado no __init__
category: modeling
weight: 3
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: raio-x-da-oo
    lesson: null
    section: "6.8"
    timestamp: null
  - type: course
    course: raio-x-da-oo
    lesson: 4
    section: "5"
    timestamp: "0:12:51"
    verified: false
  - type: course
    course: raio-x-da-oo
    lesson: 4
    section: "5"
    timestamp: "0:14:32"
    verified: false
---
**Rule.** Every attribute an instance will ever have is assigned in `__init__`, even when its
first useful value only arrives later. An attribute created inside another method exists only on
the instances that happened to call that method, so two objects of the same class stop having
the same shape.

**Why Henrique says so.** In lesson 4 he builds a `Car` whose `ignition` method sets
`motor_running` on `self`; calling it on one instance and then reading the attribute on a second
instance raises `AttributeError`, because the second object never ran `ignition` (lesson 4,
0:14:32 to 0:15:28, `verified: false`, transcript paraphrase). His rule, stated before the demo:
the attributes of the object are initialized in the `__init__`, so the state is consistent for
every instance (lesson 4, 0:12:51 and 0:15:20, `verified: false`, transcript paraphrase). The
class is the DNA of its instances (digest section 3), and DNA that varies per instance is not a
class.

**Looks like.** `def __init__(self): self.motor_running = False`, then `ignition` only flips it.
Bad: `def ignition(self): self.motor_running = True` with no `__init__` assignment, so
`d.motor_running` fails on a fresh instance.

**How to detect.** Partial. A candidate rule `modeling.attr-outside-init`, not yet implemented:
an assignment to `self.<name>` inside a method of a class whose `__init__` never assigns
`self.<name>`. Judgment: attributes set by framework hooks or by `setattr` loops.

**How to fix.** Move the first assignment into `__init__` with the value that means "not yet"
(`False`, `None`, an empty collection), and keep the other methods as transitions.
