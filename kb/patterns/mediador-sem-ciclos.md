---
id: mediador-sem-ciclos
title: Mediador sem ciclos
principle: evite-ciclos-busque-a-arvore
category: modeling
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: monopoly/realstate.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** When two entities of the same kind must interact (a tenant and an owner), the
interaction lives in the one object that already knows both, and only that object holds a
reference in that direction. The leaf exposes a few public methods and knows nobody; the
mediator calls them and decides; the coordinator above never asks who owns what. Dependencies
then form a tree: each module imports from the layer below, never sideways or upward.

## python
`monopoly/realstate.py` at commit `bffb0c2`, lines 22 to 32 (`sell_to`, lines 16 to 20, is the
other branch: `player.invest(self.price, self.rent)` and then `self.owner = player`):

```python
    def rent_to(self, player):
        if self.owner_is(player):
            return

        self.owner.receive(player.pay(self.rent))

    def deal(self, player):
        if self.has_owner():
            self.rent_to(player)
        else:
            self.sell_to(player)
```

What to notice. The property is the only object that sees two players at once, and line 26 is
three messages in one: the visitor pays, `pay` returns the amount, the owner receives it; nobody
touches another object's balance (digest section 19.2). `deal` chooses between renting and
selling inside the property, so `Board.turn` (`board.py` line 35) just calls it. In lesson 19 at
11:22 he says this self-control justifies concentrating sale and rent in the property, and at
17:52 that the only knowledge `RealState` has of `Player` is its public API. `realstate.py` and
`player.py` import nothing from the project; `board.py` imports from `player`; `game.py` from
`board`: the tree lesson 17 at 2:51 prescribes, o ideal é um modelo que evita ciclos, com uma
descrição de árvore (`verified: false`). Two edges are off the tree: `board.py` line 1 (the
player's exceptions) and `game.py` line 4 (`Board` via the package, whose `__init__` pulls
`simulation`, which pulls `game`; sections 19.3, 19.4 and 19.6). `Player` never learns of `Board`.

## Bad
The shape this replaces: the leaf reaching up and sideways through a back-reference.

```python
class Player:
    def __init__(self, balance, board):
        self.board = board          # the leaf knows its container

    def land(self):
        square = self.board.properties[self.board.position_of(self)]
        if square.owner and square.owner is not self:
            square.owner.balance += square.rent
```

`Player` imports `Board`, `Board` imports `Player`, and the money rule is spread across the
player, the square and whoever calls `land`.
