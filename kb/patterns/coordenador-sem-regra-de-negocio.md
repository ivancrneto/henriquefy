---
id: coordenador-sem-regra-de-negocio
title: Coordenador sem regra de negócio
principle: uma-responsabilidade-por-identidade
category: modeling
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: monopoly/game.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** The root object of a flow sequences the collaborators and reports the result; it holds
no domain rule. It decides who goes next, when to stop and what to return, and delegates every
decision about money, ownership or movement to the object whose identity owns it. A domain rule
showing up in the coordinator means an entity is missing or was bypassed. It applies to the
`Game`, the `main`, the view, the command handler: anything whose job is to call things in order.

## python
`monopoly/game.py` at commit `bffb0c2`, lines 27 to 40, the whole of what the game decides:

```python
        for p in cycle(self.players):
            if p not in self.board.players:
                continue

            self.board.turn(p, self.dice())
            turn_count += 1

            if len(self.board.players) == 1:
                break

            if turn_count >= 1000:
                break

        return self.leader
```

What to notice. `Game` has three members: `leader` (lines 14 to 18, a sort by balance), `dice()`
(lines 20 to 22, a `staticmethod` over `random.randint`: the `Dado` card from the CRC of lesson
15, reduced to a method because it holds no state) and `run`. It does not charge rent, debit,
decide a purchase or know what money is; `Board.turn` and `RealState.deal` do, and
`Player.from_strategies` builds the players outside it (lesson 21 at 21:18: generating the game
is not the game's job; digest section 11). Lesson 21 at 0:09 applies the same test to the turn:
no state, so no object, and it became `Board.turn`. The digest also marks what is left on the
floor here: `INITIAL_BALANCE` on line 8 is dead code, `1000` is a magic number, and the
`continue` on lines 28 to 29 is the smell lesson 23 removes (see colecao-como-entidade). Lesson
15 at 0:46 names the alternative: start from the outside in and you get um proceduralzão, the
`Jogo` class the CRC session refused to create as a classe Deus (digest sections 9 and 16).

## Bad
The shape this replaces: the root class that knows every rule.

```python
class Game:
    def run(self):
        for p in cycle(self.players):
            prop = self.properties[(self.positions[p] + random.randint(1, 6)) % 20]
            if prop.owner is None and p.balance >= prop.price and p.wants(prop):
                p.balance -= prop.price; prop.owner = p
```

Every rule in one method, no entity testable on its own, and the rent branch still to come.
