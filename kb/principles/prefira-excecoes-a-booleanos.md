---
id: prefira-excecoes-a-booleanos
title: Prefira exceções específicas a booleanos e if
category: errors
weight: 4
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.9"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 18
    section: "10"
    timestamp: null
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/board.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** When an operation can end in more than one way that the caller must tell apart, name
each outcome as a specific exception instead of returning a boolean and branching on it. The
caller then handles each outcome by name, and the ones it does not handle propagate on their own.

**Why Henrique says so.** In lesson 18, implementing `Player` test-first, he replaces booleans
and `if` with domain exceptions, because a boolean collapses outcomes that the game must
distinguish: not buying a property is not the same as going bankrupt (digest sections 10 and
12.9). Three named outcomes, three paths; with a boolean the board could not tell "did not buy"
from "is out of the game", and that distinction decides whether the player leaves.

**Looks like.** `monopoly/player.py` at commit `bffb0c2` declares three exceptions and raises
them from the two operations that can fail:

```python
class OutOfMoney(Exception): ...
class NotEnoughMoney(Exception): ...
class AbortInvestment(Exception): ...

def pay(self, amount):
    if amount > self.balance:
        raise OutOfMoney(repr(self))
    self.balance -= amount
    return amount

def invest(self, price, rent):
    if price > self.balance:
        raise NotEnoughMoney(f'{self!r} can not aford {price}.')
    if not self.strategy.should_buy(self.balance, price, rent):
        raise AbortInvestment(f'{self!r} aborted the investment.')
    return self.pay(price)
```

`monopoly/board.py` then handles them by name in the turn: `AbortInvestment` and
`NotEnoughMoney` fall through (nothing changes), `OutOfMoney` removes the player. Bad: `invest`
returning `False` for both "could not afford" and "strategy declined", and every caller
re-deriving which one happened.

**How to detect.** Partial. Mechanical: `return False` inside an `except` handler (rule
`errors.bool-in-except`), which swallows a named failure into a flag. Judgment: a function whose
boolean return is checked by callers to decide between error paths; sibling outcomes encoded as
`None` versus `False`; a broad `except` that turns distinct failures into one.

**How to fix.** Name each outcome as an `Exception` subclass in the module that owns the
operation. Raise at the point where the outcome is known. Replace `if not op(): ...` at call
sites with `try: op() except SpecificOutcome: ...`, one handler per outcome the caller actually
treats differently, and let the rest propagate. Keep the exceptions siblings unless a caller
needs to catch a family.
