---
id: uma-responsabilidade-por-identidade
title: Uma responsabilidade por identidade
category: modeling
weight: 5
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.6"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 17
    section: "9"
    timestamp: "0:03:25"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 15
    section: "9"
    timestamp: "0:08:34"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Each entity owns exactly one responsibility, stated in one sentence, and holds only the
state that responsibility needs. If a second concern shows up, it belongs to another object, even
when the real-world thing would carry both. Strip the class until the sentence is all that is left.

**Why Henrique says so.** He names the principle while building the CRC cards, princípio da
responsabilidade única que ajuda você a reduzir o acoplamento (lesson 15, 8:34,
`verified: false`, transcript paraphrase), and applies it without mercy in the review: the
player keeps no position and no list of properties, because a responsabilidade do jogador é
lidar com dinheiro é isso então esse jogador ele é quase igual uma conta bancária (lesson 17,
3:25, `verified: false`, transcript paraphrase). Position is the board's state; ownership is the
property's state. The failure mode has a name in lesson 8, "vazamento de responsabilidade":
logic that lives in no object, such as the interval loop that sat in the factory instead of in
a type of its own (digest section 7).

**Looks like.** `monopoly/player.py` at commit `bffb0c2` is the whole of the player's state:

```python
class Player:
    def __init__(self, initial_balance, strategy=Impulsive()):
        self.balance = initial_balance
        self.strategy = strategy

    def pay(self, amount):
        if amount > self.balance:
            raise OutOfMoney(repr(self))

        self.balance -= amount
        return amount
```

Two attributes, three money methods, no reference to the board or to any property (digest
section 19.1). `monopoly/board.py` keeps the positions, `{p: -1 for p in players}`, and the
property keeps its `owner`. Bad: `Player` with `position`, `properties = []` and `board`, so
that moving, buying and going bankrupt all edit the same object from three places.

**How to detect.** Judgment only. Signals: a class whose attributes come from two vocabularies
(money and position, order and payment); a class description that needs "and"; a method that
reads and writes the state of two collaborators at once; the same fact stored in two objects,
the players list in `Game` and the dict in `Board` that lesson 23 refactors (digest section
10). Method and line counts are countable, but the course sets no number, so they are hints for
a reviewer, not rules.

**How to fix.** Write the one sentence for the class. Move every attribute the sentence does not
cover to the object whose sentence does cover it, or create that object (the property, not the
player, knows its owner). Replace direct edits with messages: `player.pay(amount)` returns the
amount so the receiver can `receive` it without touching the payer's balance (digest section
19.2). When the same fact lives twice, pick one owner; see deixe-o-codigo-descansar for when.
