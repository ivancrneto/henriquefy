---
id: objeto-e-um-processo
title: O objeto é um processo, não uma estrutura com métodos
category: modeling
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: procedural-para-oo
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: procedural-para-oo
    lesson: 1
    section: "5"
    timestamp: "0:24:31"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 1
    section: "5"
    timestamp: "0:30:28"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 2
    section: "5"
    timestamp: "0:04:38"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 2
    section: "5"
    timestamp: "0:12:11"
    verified: false
---
**Rule.** An object is a process that provides a service. A class whose caller still runs the
steps is procedural code with classes. Encapsulation is the articulation of behavior: the
ability to solve the problem lives in the object, not in the consumer, even when no private
attribute was touched.

**Why Henrique says so.** In lesson 1 he rejects the picture of objects as data and code stuck
together: in the concept the object sits above that, because the object is a process (lesson 1,
0:24:31, `verified: false`, transcript paraphrase). A data structure with methods is not
necessarily an object (lesson 1, 0:30:28, `verified: false`, transcript paraphrase). Lesson 2
shows the basket of apples that sorts and lets the caller pick an index: it runs, and he still
says he is programming procedurally with classes (0:04:38, `verified: false`, transcript
paraphrase). The violation of encapsulation is not touching the hidden `data`; it is that the
ability to solve the problem is in the consumer (0:12:11, `verified: false`, transcript
paraphrase).

**Looks like.** The caller asks for the heaviest apple and does not know whether the object
sorts or takes a max. Bad: the caller calls `sort`, then `get` on the last index, so the
strategy lives outside the object.

**How to detect.** Judgment. The caller sequences the collaborator's methods in order to
produce a result the collaborator could have returned in one message. A class with methods is
not evidence either way.

**How to fix.** Name the service the caller actually wants. Move the steps that produce it
into the object. Leave the caller with one message and no knowledge of the order.
