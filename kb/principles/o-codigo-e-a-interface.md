---
id: o-codigo-e-a-interface
title: O código é a interface
category: readability
weight: 4
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.10"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 23
    section: "10"
    timestamp: "0:07:40"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 6
    section: "7"
    timestamp: "0:01:41"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/realstate.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** The code itself, as read by its callers, is the design artifact: the names of classes
and methods, the messages a test sends, the sentence a line of code forms. No diagram or
document stands above it. So the interface is discovered by writing the calling code first (the
test), and a name that reads badly is a sign that the abstraction is wrong, not a cosmetic
problem.

**Why Henrique says so.** In lesson 23 the new collection is first called `PlayerCollection`
and discarded because achei que ficou muito misturado, então decidi criar um conceito novo
(lesson 23, 7:40, `verified: false`, transcript paraphrase): the bad name exposed a missing
concept, and `Competitors` is born from a test file written before the implementation (digest
sections 10 and 21.1). The habit starts in lesson 6, where he writes the test and ignores the
editor's red underlines: eu tô aqui fazendo uma espécie de pensamento positivo sobre o código
dessa maneira eu não me distraio com os detalhes de implementação e o foco em descobrir
precisamente as interfaces que eu desejo (lesson 6, 1:41, `verified: false`, transcript
paraphrase). Lesson 12 ties class and method names to the subject and verb of a concise user
story, and lesson 13 sets the direction, from code to diagram and never the reverse (digest
section 8).

**Looks like.** `monopoly/realstate.py` at commit `bffb0c2` has the line the digest calls the
most elegant in the project, three messages that read as the domain sentence:

```python
def rent_to(self, player):
    if self.owner_is(player):
        return

    self.owner.receive(player.pay(self.rent))
```

The names `pay`, `receive`, `invest`, `sell_to`, `rent_to`, `deal` and `foreclose` are the
glossary of lesson 16 made executable, and `pay` returns the amount so that the sentence can be
written (digest sections 19.1 and 19.2). Bad: `PlayerCollection`, `DataManager`,
`process_turn_data`, or a method whose docstring has to explain what its name does not.

**How to detect.** Judgment only. Signals: names made of generic suffixes (`Collection`,
`Manager`, `Helper`, `Util`, `Data`) that describe the shape and not the concept; a method name
that needs a comment to be read; a test that cannot be read as a sentence about the domain; a
design document or diagram that disagrees with the code and is treated as the truth. A suffix
list is countable, but the course gives no such list, so a checker would at most surface those
names for a human to judge.

**How to fix.** Write the test first and read it aloud as a sentence: who sends what to whom.
If the sentence is awkward, rename or split the receiver, not the test. When a name has to be
qualified ("collection of players that also knows the order and who left"), look for the
concept that owns all of it and name that (`Competitors`). Keep the vocabulary of the decupagem
in the identifiers, and see nao-projete-a-generalizacao for when a name should wait.
