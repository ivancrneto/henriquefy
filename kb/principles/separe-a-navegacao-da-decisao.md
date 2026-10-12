---
id: separe-a-navegacao-da-decisao
title: Tire a navegação de dentro do for e passe a decisão como função
category: readability
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-rapida
    lesson: null
    section: "6.9"
    timestamp: null
  - type: course
    course: refatoracao-rapida
    lesson: null
    section: "6.12"
    timestamp: null
  - type: course
    course: refatoracao-rapida
    lesson: 12
    section: "5"
    timestamp: "0:04:58"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 14
    section: "5"
    timestamp: "0:31:47"
    verified: false
  - type: course
    course: refatoracao-rapida
    lesson: 14
    section: "5"
    timestamp: "0:39:05"
    verified: false
---
**Rule.** A loop that both walks a structure and decides what to do at each step ties the two
together. Pull the walking out into a generator that yields positions, and pass the per-step
decision in as a function, the way `sorted` takes `key`. The algorithm then knows neither the
data structure nor the policy, and either can change alone.

**Why Henrique says so.** The `for` is a very dangerous thing, because we are used to using it
indiscriminately and it tangles things, it ties the structures together; what he wants is to take
the logic of navigating a rectangle and extract it to something higher level (lesson 12, 0:04:58
to 0:05:18, `verified: false`, transcript paraphrase). The extracted `region` generator then
produces coordinates, and generators connected to generators form a flow of transformation
(lesson 12, 0:05:43; 0:13:52 to 0:14:03). In the flood fill he goes one step further: an
algorithm that computes coordinates and also depends on the board's structure has two
responsibilities (lesson 14, 0:27:50 to 0:28:05), so the generic algorithm receives the `inside`
and `match` functions, exactly as Python's sort receives the key, by dependency inversion (lesson
14, 0:31:47 to 0:32:11), and whoever calls it configures it (lesson 14, 0:39:05 to 0:39:22).
Digest sections 6.9 and 6.12.

**Looks like.** Reconstructed from lesson 12's speech (digest section 5), not published code:

```python
def region(col_start, col_end, row_start, row_end):
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            yield col, row

def set_many(board, coords, value):
    for c in coords:
        set_item(board, c, value)
```

Vertical line, horizontal line and rectangle become three calls of `set_many` over three
regions: `region(col, col, start, end)`, `region(start, end, row, row)` and
`region(c0, c1, r0, r1)`.
Bad: three functions, each with its own nested `for`, each indexing the board directly.

**How to detect.** Judgment. Nested loops that index a structure and also branch on a policy; the
same loop shape repeated across functions with a different body (see the one, two, three
repetitions in `nao-projete-a-generalizacao`).

**How to fix.** Extract the iteration into a generator that yields the positions. Replace the
loop body with a call. If the body encodes a choice the caller should make (what counts as
inside, what matches), make it a function parameter. Run the tests after each step.
