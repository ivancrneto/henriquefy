---
id: estrategia-por-composicao
title: Estratégia por composição
principle: componha-em-vez-de-herdar
category: modeling
frameworks:
  python: {origin: his, repo: henriquebastos/monopoly, path: monopoly/player.py, commit: bffb0c269b00836066d0bb064ca4e38a80cad210}
---
**What.** The behavior that varies between instances of an entity lives in a small object the
entity receives at construction and consults through one method, not in a subclass per
variation. The variations are stateless, so one instance of each sits in a module-level tuple,
and a `classmethod` factory on the entity turns the tuple into one entity per variation. It
applies when a class would otherwise fork into `ImpulsivePlayer`, `CautiousPlayer` and so on.

## python
`monopoly/player.py` at commit `bffb0c2`, lines 17 to 20 and 37 (lines 22 to 35 declare `Demanding`,
`Cautious` and `Gambler` in the same shape), then lines 39 to 42 and 66 to 68:

```python
class Impulsive(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return True

STRATEGIES = (Impulsive(), Demanding(), Cautious(), Gambler())
```

```python
class Player:
    def __init__(self, initial_balance, strategy=Impulsive()):
        self.balance = initial_balance
        self.strategy = strategy

    @classmethod
    def from_strategies(cls, balance):
        return [cls(balance, strategy=s) for s in STRATEGIES]
```

What to notice. `Player` asks its strategy one question, `should_buy(balance, price, rent)`, on
line 58: three numbers, never the property (digest section 11). Every `should_buy` is a
`@staticmethod`, so the shared instances and the `Impulsive()` default on line 40 are safe; give
a strategy state and that default becomes a bug (digest section 19.1). `Strategy` declares no
`should_buy` (lines 13 to 15); all it knows is its name, which `Simulation` groups winners by.
The factory is a `classmethod`, not a `PlayerFactory` class: in lesson 21 at 24:17 he says Python
has classmethods and classes are objects. Lesson 18 at 17:23 weighs composition against
inheritance here, and he validates a student's inheritance version: the criterion is the effect,
not the rule (digest section 12.8).

## Bad
The shape this replaces: the variation baked into the entity's identity.

```python
class ImpulsivePlayer(Player):
    def should_buy(self, price, rent): return True

class CautiousPlayer(Player):
    def should_buy(self, price, rent): return self.balance - price >= 80
```

Four classes to test instead of one, no swapping a strategy on a living player, `isinstance` everywhere.
