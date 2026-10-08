---
id: escolha-a-regra-mais-simples
title: Escolha a regra mais simples
category: simplicity
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.3"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 18
    section: "10"
    timestamp: "0:11:39"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 21
    section: "10"
    timestamp: "0:00:09"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** When the domain leaves a choice open, take the rule that needs the least code and the
least state, even when a richer rule would be more faithful to the original specification.
Revise the specification rather than the design: the simple rule can be replaced later if the
problem asks for it, the complex one has to be maintained now.

**Why Henrique says so.** The rule is stated during the modeling in lesson 16 (digest section 9)
and applied in lesson 18, when the payment rule turns into code. Lesson 16 had decided that the
owner receives the full rent even from a player who cannot pay, creating money; in lesson 18 he
reverses it on the spot: não é mais fácil quando o cara não tem dinheiro para pagar ninguém
recebe nada e o cara sai do jogo simplesmente isso entendeu ninguém recebe nada o cara sai do
jogo (lesson 18, 11:39, `verified: false`, transcript paraphrase). The digest records it as a
business rule revised for simplicity, not a bug (section 11). Lesson 21 applies it to
structure: acho que não precisa ter um objeto turno porque ele seria um método estático
basicamente ele não tem um estado (lesson 21, 0:09, `verified: false`, transcript paraphrase),
and the same reasoning turns the `Dado` card into `Game.dice()`, one `randint` (digest sections
10 and 12.3).

**Looks like.** `monopoly/player.py` at commit `bffb0c2`: a player who cannot pay raises and
nothing is transferred, no partial payment, no debt, no creditor logic:

```python
def pay(self, amount):
    if amount > self.balance:
        raise OutOfMoney(repr(self))

    self.balance -= amount
    return amount
```

`monopoly/game.py` at the same commit keeps the die to one line, `return random.randint(1, 6)`,
as a static method. Bad: a `Debt` ledger that lets the owner collect what the bankrupt player
had left, a `Dice` class with sides and history, or any rule justified by "the real game does
it that way" (the course rejects modeling the real world in lessons 14 and 17, digest section 9).

**How to detect.** Judgment only. Signals: a branch that exists for a case the tests never
exercise; a class without state that wraps a single call (`Dice`, `Turn`, `Rodada`); a rule
implemented in two steps where the spec allowed one; code that mirrors the physical process
(money moving hand to hand) rather than what the simulation needs. A checker cannot know which
rules the domain allows, so it can only surface stateless classes and untested branches as
questions.

**How to fix.** Write the candidate rules down in one sentence each, the decupagem of lesson 16
(digest section 9). Pick the one with the fewest objects and the fewest branches, and mark the
decision as yours so it can be revisited. Implement it under test. If the simulation or the
client later shows the rule is wrong, change it then; see postergue-decisoes.
