---
id: componha-em-vez-de-herdar
title: Componha em vez de herdar, quando puder
category: modeling
weight: 3
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.8"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 18
    section: "10"
    timestamp: "0:17:23"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 7
    section: "7"
    timestamp: "0:25:55"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** When an object needs a behavior that varies, give it a collaborator that carries the
behavior instead of subclassing it. Inheritance is kept where it is cheap and honest: a thin
base for shared mechanics, or a built-in extended with domain semantics. Judge by the effect.

**Why Henrique says so.** In lesson 18 the player receives a strategy object and asks it
`should_buy`; he then discusses composition against inheritance for those strategies and
validates a student's answer that used inheritance, so the digest records the criterion as the
effect, not the rule (lesson 18, 17:23, `verified: false`, transcript paraphrase; digest section
12.8). The background is lesson 7: Originalmente a
orientação objetos Era exatamente assim os esquemas de classe não era feito para herança mas
sim mas sim para criar camada de em direção para passagem de mensagens (lesson 7, 25:55,
`verified: false`, transcript paraphrase; "em direção" is the caption's misreading of
"indireção"). Inheritance is a tool for building indirection, not the point of the paradigm
(digest section 17).

**Looks like.** `monopoly/player.py` at commit `bffb0c2` composes the player with a strategy and
keeps the strategy hierarchy one level deep, with a base that only knows its name:

```python
class Strategy:
    def __str__(self):
        return self.__class__.__name__

class Cautious(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return balance - price >= 80

class Player:
    def __init__(self, initial_balance, strategy=Impulsive()):
        self.balance = initial_balance
        self.strategy = strategy
```

Where inheritance fits he uses it: `class IntervalMap(dict)` in lesson 8 extends the built-in
to carry interval semantics (digest section 7). Bad: `CautiousPlayer(Player)` and three
siblings, each overriding `invest`, so every money fix must be checked in four classes.

**How to detect.** Partial. Mechanical: project-defined class hierarchies deeper than two levels,
excluding `Exception`, `ABC` and built-in or third-party bases (rule
`modeling.inheritance-depth`); a subclass that overrides most of its parent's methods, which
suggests a collaborator in disguise. Judgment: whether a base class is a thin shared mechanic
(fine) or a behavior axis that should have been an attribute.

**How to fix.** Name the varying behavior as a noun (strategy, policy, formatter). Make it an
object with one method and no state where possible, and pass it into the constructor with a
sensible default. Collapse the subclasses into instances of that object. Keep a base class only
for what every variant shares mechanically, as `Strategy.__str__` does.
