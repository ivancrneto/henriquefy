---
id: superficie-de-contato
title: Reduza a superfície de contato
category: modeling
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: procedural-para-oo
    lesson: null
    section: "6.4"
    timestamp: null
  - type: course
    course: procedural-para-oo
    lesson: 2
    section: "5"
    timestamp: "0:09:30"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 6
    section: "5"
    timestamp: "0:03:54"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 6
    section: "5"
    timestamp: "0:07:22"
    verified: false
  - type: course
    course: procedural-para-oo
    lesson: 10
    section: "5"
    timestamp: "0:22:12"
    verified: false
---
**Rule.** Two parts should meet on a small contact surface. The import list is that surface:
each name imported is contact the caller has with the other module. A relationship wired
straight into the code ties the parts together. Complex systems should meet in the dynamics,
through the interface, at the moment they run.

**Why Henrique says so.** On the basket of apples he says the contact surface between the two
pieces of code is too large and has to be reduced (lesson 2, 0:09:30, `verified: false`,
transcript paraphrase). While splitting the game of life he treats every import as the size of
the contact between the game and the bitmap (lesson 6, 0:03:54, `verified: false`, transcript
paraphrase), and swapping two imports for one is a small edit with conceptual progress (0:07:22,
`verified: false`, transcript paraphrase). In the last lesson the same rule rises from modules
to systems: when he structures the relationship directly, physically in the code, he is tying
himself down; the relationship has to happen in the dynamics, in the life of the parts (lesson
10, 0:22:12, `verified: false`, transcript paraphrase).

**Looks like.** The game imports one name from the bitmap and asks it for what it needs. Bad:
the game imports `x`, `y` and the offset and assembles a coordinate the bitmap already knows
how to build.

**How to detect.** Judgment. A long import list from one module, or a caller that reaches past
an object into the structure that object owns. No mechanical rule yet.

**How to fix.** Put a layer in the middle that already does the behavior. Drop the imports the
caller no longer needs. Keep the caller's interest on what comes back, not on what the other
part is.
