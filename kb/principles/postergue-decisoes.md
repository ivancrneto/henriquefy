---
id: postergue-decisoes
title: Postergue decisões enquanto o entendimento cresce
category: modeling
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.4"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 14
    section: "9"
    timestamp: "0:14:28"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 16
    section: "9"
    timestamp: "0:01:02"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/realstate.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Do not decide what you do not yet understand. Leave the open question open, keep
working on the parts you do understand, and let the decision fall out when the surrounding code
or the rewritten requirement makes it obvious. The most abstract piece comes last, because it is
the one that depends on everything else being understood.

**Why Henrique says so.** The course is built in that order. Lesson 14 reads the problem and
deliberately leaves its central question unanswered: um jogador ativamente vai lá e compra ou a
propriedade vai lá e se oferece pro jogador ou alguma outra coisa intermedia essa relação
(lesson 14, 14:28, `verified: false`, transcript paraphrase). Lesson 16 rewrites the text before
modeling anything: eu chamo de a decoupagem é quando eu pego o texto parágrafo parágrafo e eu
vou refraseando em frases específicas diretas sem anuidade (lesson 16, 1:02, `verified: false`,
transcript paraphrase; "anuidade" is the caption's misreading of "ambiguidade"). The digest
names this as the reason the decupagem comes before the CRC review and the most abstract class
is left for last in lesson 17 (sections 12.4 and 9). The question from lesson 14 is only
answered in lesson 19, inside the property, and lesson 22 closes the course saying the modeling
is never final (digest section 10).

**Looks like.** `monopoly/realstate.py` at commit `bffb0c2` is where the postponed decision
landed, after `Player` existed and the tests showed which object knew enough to decide:

```python
def deal(self, player):
    if self.has_owner():
        self.rent_to(player)
    else:
        self.sell_to(player)
```

The property mediates; `Board` never asks whether a square has an owner (digest section 19.2).
Bad: deciding in lesson 14 that `Board` would check ownership and call `player.buy(property)`,
and then carrying that decision into every later class.

**How to detect.** Judgment only. Signals: a design decision recorded in a docstring or ticket
before the first test exists; parameters and attributes reserved for a feature nobody has asked
for; a class created in the first commit and reshaped in the next three; decisions that mirror
the real world rather than the simulation (lesson 17, digest section 9). No mechanical rule: a
checker cannot tell a postponed decision from a missing one.

**How to fix.** Write the open question down, in one sentence, in the glossary or the test file.
Build the leaves that do not depend on it (see pense-localmente). When two or three concrete
callers exist, the answer is usually visible in which object already holds the data; put the
decision there and delete the question. Revisit the modeling after it runs, as
deixe-o-codigo-descansar prescribes.
