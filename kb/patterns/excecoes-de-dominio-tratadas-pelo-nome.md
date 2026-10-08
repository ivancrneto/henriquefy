---
id: excecoes-de-dominio-tratadas-pelo-nome
title: Exceções de domínio tratadas pelo nome
principle: prefira-excecoes-a-booleanos
category: errors
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: monopoly/board.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** The module that owns an operation declares one `Exception` subclass per outcome the
system must tell apart and raises each where the outcome is known. The caller that drives the
flow catches them by name: one `except` per reaction, siblings that share a reaction grouped in a
tuple, the rest propagating. No boolean return, no `if` on a flag, no reading of the message. It
applies whenever a step in a sequence can end in more than one business outcome.

## python
`monopoly/player.py` at commit `bffb0c2` declares `OutOfMoney`, `NotEnoughMoney` and
`AbortInvestment` (lines 4 to 11); `pay` raises the first (lines 44 to 49), `invest` raises the
second before consulting the strategy and the third when it declines (lines 54 to 61). The turn,
`monopoly/board.py` lines 31 to 39, handles them by name:

```python
    def turn(self, player, steps):
        real_state = self.move(player, steps)

        try:
            real_state.deal(player)
        except (AbortInvestment, NotEnoughMoney):
            pass
        except OutOfMoney:
            self.remove(player)
```

What to notice. Two outcomes share one reaction and the tuple says so; the third removes the
player. The turn never asks `deal` what happened: the property mediates, the player raises, the
board reacts, and `pay` and `invest` still return the amount paid on the happy path. The three
are siblings directly under `Exception`, so handler order does not matter and no caller catches
all of them by accident. Lesson 18 replaced booleans with these exceptions (digest sections 10
and 12.9); in lesson 21 at 8:21 the handlers enter the turn as `try/except ... pass`, test
first, one test per outcome in `tests/test_board.py` (digest section 19.7). The cost is line 1
of `board.py`, the one import pointing against the dependency tree (digest section 19.3); see
evite-ciclos-busque-a-arvore.

## Bad
The shape this replaces: a flag per outcome, re-derived at every call site.

```python
def invest(self, price, rent):
    if price > self.balance or not self.strategy.should_buy(self.balance, price, rent):
        return False
    ...

if not real_state.deal(player):               # in the board
    if player.balance < real_state.rent:      # bankruptcy, or just a no?
        self.remove(player)
```

The board re-implements the player's rules to learn which failure it got, and each new outcome
is a new flag threaded through every caller.
