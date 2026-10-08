---
id: pense-localmente
title: Pense localmente, nunca globalmente
category: modeling
weight: 5
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.5"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 12
    section: "8"
    timestamp: "0:01:38"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 15
    section: "9"
    timestamp: "0:00:46"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/game.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Model and build from the parts, not from the whole. Each object is designed from its
own context: what it knows, what it decides, which few collaborators it talks to. Do not start
from the orchestrator, do not start from the `for` loop, and do not imagine yourself running the
system; the sequence of execution should emerge from the objects interacting.

**Why Henrique says so.** It is the modeling rule he repeats most. quando você tá modelando o
sistema de objetos você não pode pensar Global se você pensar Global você vai impor uma visão um
pressuposto em cima do problema e isso vai deformar a sua modelagem você tem que pensar local
(lesson 12, 1:38, `verified: false`, transcript paraphrase). Starting from `Jogo` in the CRC
session would have pulled everything into it: tu vai fazer um proceduralzão porque você começou
de fora para dentro ao invés de dentro para fora (lesson 15, 0:46, `verified: false`, transcript
paraphrase). Lesson 11 gives the confidence behind it, you think in the parts trusting that the
whole will be more than their sum, and lesson 18 implements in the same order, from the leaves
with one responsibility and few relations inward (digest sections 8 and 10).

**Looks like.** `monopoly/game.py` at commit `bffb0c2` is the class he refused to model first,
and when it finally exists it holds no business rule, only sequencing:

```python
def run(self, counter=0):
    turn_count = counter

    for p in cycle(self.players):
        if p not in self.board.players:
            continue

        self.board.turn(p, self.dice())
        turn_count += 1
```

Money, rent, purchase and elimination are decided in `Player`, `RealState` and `Board` (digest
section 19.4). Bad: a `Game` that owns balances, positions and properties as dicts and runs
every rule inside one loop, "código procedural com classe" (lesson 12, digest section 8).

**How to detect.** Judgment, with hints. Signals: one class named `Game`, `App`, `Manager` or
`System` holding most of the package's lines and state; coordinators that read other objects'
attributes and compute on them instead of sending a message (the `top_left.x` case of lesson 6,
digest section 7); long attribute chains, which lesson 23 names as a coupling symptom (digest
section 10). Chain length and class-size ratios are countable, but the course gives no
threshold, so a checker reports them as questions, not findings.

**How to fix.** Pick the leaves: the entities with one responsibility and few relations. Write
their tests first, from inside their own context, and ignore how the whole will run. Give each
decision to the object that already holds the data for it (the property decides between sale
and rent). Add the orchestrator last, and keep it to sequencing. If a coordinator is computing
on another object's state, move the computation into that object and send a message instead;
see uma-responsabilidade-por-identidade and evite-ciclos-busque-a-arvore.
