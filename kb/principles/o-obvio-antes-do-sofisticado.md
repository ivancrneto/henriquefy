---
id: o-obvio-antes-do-sofisticado
title: Nem sempre o código mais sofisticado é o melhor
category: simplicity
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: desafios-pythonicos
    lesson: null
    section: "3.2"
    timestamp: null
  - type: course
    course: desafios-pythonicos
    lesson: 8
    section: "5"
    timestamp: "0:02:39"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 8
    section: "5"
    timestamp: "0:02:44"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 5
    section: "5"
    timestamp: "0:01:52"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 11
    section: "5"
    timestamp: "0:02:32"
    verified: false
---
**Rule.** Prefer the obvious, simple solution over the clever one. A one-liner, a nested
comprehension or an advanced feature is not better because it is shorter or more advanced; the
plain version usually wins on memory, readability and maintenance. Write the sophisticated
versions as practice, then keep the one a reader understands at a glance.

**Why Henrique says so.** After showing the counter loop, the list comprehension and the
generator expression for the same exercise, he draws the lesson: not always is the most
sophisticated code the best; the most obvious and simple solution tends to be the most efficient
in memory, readability and maintainability, and using advanced features does not mean writing
the best code (Pacote de Desafios Pythônicos, lesson 8, 0:02:37 to 0:03:00, `verified: false`,
transcript paraphrase). He offers the one-line version as an exercise in six lessons and
distrusts it each time he judges it: will it look good like that (lesson 2, 0:00:58 to 0:01:02),
I don't think it is that elegant (lesson 5, 0:01:50 to 0:01:56), it looks quite weird (lesson 11,
0:02:30 to 0:02:36). A first solution that is not sophisticated, focused on solving the problem,
is welcome (lesson 14, 0:03:48 to 0:04:00). Digest sections 3.2 and 6.2.

**Looks like.** Reconstructed from lesson 8's speech (digest section 5), not his code:

```python
def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count
```

Bad: the same function as `return sum(1 for w in ws if len(w) > 1 and w[0] == w[-1])` chosen
because it fits on one line, or a `reduce` with a `lambda` where a loop reads as the problem.
Neither is wrong; the course asks why the clever form was kept.

**How to detect.** Judgment. Signals: a line that needs to be unpacked mentally before it can be
read; nested comprehensions or chained `lambda`s where a named loop or helper reads as the
problem; a commit that turns working plain code into a shorter version with no behavior change
and no reason given.

**How to fix.** Write the obvious version, then compare it with the compact one for a reader who
does not know the trick; keep the compact one only when it is also the clearer one. Related:
`escolha-a-regra-mais-simples` (the same choice for domain rules), `codigo-linear`,
`funcione-direito-e-depois-rapido`.
