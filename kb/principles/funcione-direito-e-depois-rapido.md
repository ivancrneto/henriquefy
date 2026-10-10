---
id: funcione-direito-e-depois-rapido
title: Faça funcionar, faça direito e, se precisar, faça rápido
category: project
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: dicas-de-programacao
    lesson: null
    section: "6.11"
    timestamp: null
  - type: course
    course: dicas-de-programacao
    lesson: 30
    section: "5"
    timestamp: "0:01:59"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 30
    section: "5"
    timestamp: "0:02:08"
    verified: false
---
**Rule.** Work in three passes, in this order: make it work, make it right, and only if it needs it make it fast. Stopping after the first pass piles up technical debt; skipping to the third optimizes something that is not yet correct or clean.

**Why Henrique says so.** Every change negotiates with the past for the sake of a future (lesson 30, 0:01:38 to 0:01:54, `verified: false`, transcript paraphrase). The order is work, right, fast (lesson 30, 0:01:59 to 0:02:08), and stopping at "works" accumulates technical debt (lesson 30, 0:02:08 to 0:02:18). He pairs it with running early: a first version is never good, so get it running and iterate (lesson 1, 0:00:06, digest section 6.1).

**Looks like.** A feature that landed as a working spike and was cleaned up in the next commits, with optimization only after a measurement. Bad: a spike merged as is and never revisited, or a hand-tuned loop around logic nobody has tested.

**How to detect.** Judgment. Look for commits that add behavior and never come back to name, structure and tests; and for performance work with no measurement or no test behind it.

**How to fix.** Get the narrowest case working end to end, then refactor under the tests that now exist, and measure before touching speed. See [digest section 6.11](../courses/dicas-de-programacao.md).
