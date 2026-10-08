---
id: colecao-como-entidade
title: Coleção como entidade
principle: o-codigo-e-a-interface
category: modeling
frameworks:
  python: {origin: course, course: oo-na-pratica, lesson: 23, section: "21.2"}
---
**What.** When the same group of objects lives in two places (a list here, a dict there) and the
code around it reads like `self.board.players`, the group is an entity that has not been named
yet. Give it a class, let the protocols the callers already use (`[]`, `len`, `for`) be its
interface, and move the derived state (who leads, who is still in) inside. Deletion becomes a
mark instead of a `del`, so an iteration in progress keeps working. The name is part of the
design: one that reads badly (`PlayerCollection`) says the abstraction is not found yet.

## python
`origin: course`: the shape is what lesson 23 builds live; the code is the digest's reconstruction
(section 21.2), run against the original repo, not his verbatim code. The repo has no `competitors.py`.

```python
class Competitors:
    def __init__(self, players=()):
        self.players = {player: -1 for player in players}
        self.removed = set()

    def __delitem__(self, player):
        self.removed.add(player)

    def __len__(self):
        return len(self.players) - len(self.removed)

    def __iter__(self):
        for player in self.players:
            if player in self.removed:
                continue
            yield player
```

What to notice. The interface is what `Board` already did to its dict: index, assign, delete,
`len`, iterate, so `__getitem__` and `__setitem__` are plain pass-throughs (digest section 21.3);
the test file came first, at 8:55, to draw it. `__delitem__` marks instead of deleting, a delete
virtual (16:41), and `__len__` subtracts the removed so `len(competitors) == 1` still ends the
game; the mark exists because `itertools.cycle` caches its items and `del` during iteration
breaks (lesson 21 at 37:50, lesson 23 at 26:24). The name came at 7:40: `PlayerCollection` read
as a mix, so competidores was invented (digest section 12.10; see deixe-o-codigo-descansar).
`leader` moves in too (31:53; at 33:35 `Game.leader` is only a proxy); the digest flags its
`max(self, ...)` over active players as an inference and the one behavior change: the original
`Game.leader` could crown an eliminated player (sections 21.6 and 21.7).

## Bad
The shape this replaces, from the published `game.py` at `bffb0c2`:

```python
self.board = Board(self.players, properties)  # Game keeps a list, Board a dict
for p in cycle(self.players):
    if p not in self.board.players:           # the symptom
        continue
```

Two homes for one fact, a `continue` that only reconciles them, and a `del` that forgets who played.
