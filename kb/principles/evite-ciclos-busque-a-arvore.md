---
id: evite-ciclos-busque-a-arvore
title: Evite ciclos; busque a árvore
category: modeling
weight: 4
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.7"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 17
    section: "9"
    timestamp: "0:02:51"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 7
    section: "7"
    timestamp: "0:22:07"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/realstate.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/game.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Dependencies between objects, and between modules, point one way. The model reads as
a tree: leaves know nothing about their users, the root knows the leaves only through public
messages, and no two things depend on each other. When a cycle appears, invert one edge.

**Why Henrique says so.** The CRC review in lesson 17 is described as a cyclomatic analysis of
the model, and the target shape is stated outright: o ideal é que a gente tem um modelo que
evita ciclos o modelo geralmente ele tem uma descrição de árvore (lesson 17, 2:51,
`verified: false`, transcript paraphrase). He had met the problem in code in lesson 7, where
each integer class instantiated the next: as implementação claramente tem um problema muito
sério um problema de acoplamento veja que agora cada classe está dependendo uma da outra
diretamente (lesson 7, 22:07, `verified: false`, transcript paraphrase), fixed by
`Integer.register` inverting the dependency (digest section 7). Lesson 23 opens by naming the
"triângulo" between game, players and board as the thing to eliminate (digest section 10).

**Looks like.** `monopoly/realstate.py` at commit `bffb0c2` imports nothing from the project
and knows the player only through messages:

```python
def rent_to(self, player):
    if self.owner_is(player):
        return

    self.owner.receive(player.pay(self.rent))
```

`player.py` imports nothing either; `board.py` imports from `player`; `simulation.py` imports
from all (digest section 19.0). The one place his own code bends the rule is `monopoly/game.py`:
`from monopoly import Board` goes through the package, whose `__init__` imports `simulation`,
which imports `Game` back; it works only because of the line order in `__init__.py` (digest
sections 19.4 and 19.6). Bad: `Player` holding a `board` so it can move itself, while `Board`
holds the players.

**How to detect.** Partial. Mechanical: build the import graph of the package, including
re-exports through `__init__.py`, and report every strongly connected component with more than
one module (rule `modeling.import-cycle`); an in-package `from package import Name` that
resolves through the package's own `__init__` is a second signal. Judgment: object-level cycles
(A holds B, B holds A) and a leaf calling back into its caller through a passed-in reference are
invisible to imports; those need a reading of who sends messages to whom.

**How to fix.** Draw the dependency direction, modules first, then objects. For each back edge,
pick the inversion he uses: a parameter with a default (`owner=None`), a `classmethod` factory
on the leaf (`Player.from_strategies`), or a registry the leaf calls. Import modules directly
(`from monopoly.board import Board`) rather than through the package, then re-run the graph.
