---
id: isolamento-interacao-impacto
title: Isolamento, interação e impacto são os critérios de cada decisão
category: modeling
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-rapida
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: refatoracao-rapida
    lesson: 4
    section: "5"
    timestamp: "0:08:11"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 15
    section: "5"
    timestamp: "0:37:38"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 16
    section: "5"
    timestamp: "0:01:04"
    verified: false
---
**Rule.** Decide what to change, and how to decouple it, by asking three questions about each
part of the code and its neighbors: what it interacts with, what a change in it impacts, and how
isolated it is. Apply the questions at every scale, from a line to a module. These criteria need
no design-pattern vocabulary and no object orientation; functions are enough.

**Why Henrique says so.** He names three elements that are key for him, which are not things but
relations between sets of things: impact, interaction and isolation (lesson 4, 0:08:11 to
0:08:24, `verified: false`, transcript paraphrase), analyzed fractally, part by part (lesson 4,
0:10:23 to 0:10:36). Near the end of the live refactoring he calls them the moral of the story:
three criteria to evaluate what to touch and how to decouple, and you do not need to know design
or object orientation, you are using functions and the criterion of what belongs where, the
interaction, the impact and the isolation of each part among themselves (lesson 15, 0:37:38 to
0:38:09, `verified: false`, transcript paraphrase). The course is about the sensitivity to see
them (lesson 16, 0:01:04 to 0:01:23). Digest sections 3.2 and 6.2.

**Looks like.** A test that writes a file is rewritten to mock `open`, because writing to disk is
an impact the test should not have (digest section 6.11). A board accessed in eight commands is
put behind one `set_pixel`, so a change to the board's layout impacts one function (6.6, 6.7).
Bad: a refactoring justified only by a pattern's name, with no account of what the change
isolates or which impact it removes.

**How to detect.** Judgment. For a proposed change, ask whether it reduces the number of places a
change would impact, the number of parts a piece interacts with, or makes a part testable alone.
If none of the three moves, the change is cosmetic.

**How to fix.** List, for the part you are about to change, what it calls, what calls it and what
it touches outside memory (disk, network, global state). Make the move that shrinks one of those
lists, run the tests, repeat. See `superficie-de-contato`.
