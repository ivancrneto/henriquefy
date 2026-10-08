---
id: nao-projete-a-generalizacao
title: Não projete a generalização, deixe o código pedi-la
category: simplicity
weight: 5
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "12.2"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 7
    section: "7"
    timestamp: "0:26:51"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 7
    section: "7"
    timestamp: "0:38:28"
    verified: false
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: monopoly/player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Do not design the abstraction up front. Write the concrete cases first, even if that
means repeating code, and extract a base class, a factory or a registry only when the repetition
itself shows which generalization is needed. The abstraction is the last thing you write, shaped
by the cases that exist, never by the cases you imagine.

**Why Henrique says so.** In lesson 7 he builds `Int8`, `Int16`, `Int24` and `Int32` by copying
one class four times, and only then diagnoses the coupling and extracts `select`, the `Integer`
base class and the `register` mechanism: Não começa do básico começa replicando o código e deixa
o código pedir para você uma generalização (lesson 7, 26:51, `verified: false`, transcript
paraphrase). He closes the lesson with the method itself: simplifica baixa a bola implementa
alguma coisa e faz com que o código te mostre o caminho um bom design vem de você eliminar o
excesso (lesson 7, 38:28, `verified: false`, transcript paraphrase). The modeling keeps the
same order: lesson 17 leaves the most abstract class for last, and lesson 14 calls any code
decision taken during modeling "design precoce" (digest section 9). A generalization designed
before the cases exist encodes an assumption, and an assumption deforms the model.

**Looks like.** `monopoly/player.py` at commit `bffb0c2` has four strategies and a base class that
holds exactly what the four needed to share, one method:

```python
class Strategy:
    def __str__(self):
        return self.__class__.__name__

class Impulsive(Strategy):
    @staticmethod
    def should_buy(balance, price, rent):
        return True
```

`Strategy` does not declare `should_buy`; the convention lives in the four concrete classes
(digest section 19.1). Bad: an `AbstractStrategy(ABC)` with `should_buy`, `name` and `describe`
as abstract methods, written before the second strategy existed, plus a registry no caller asks
for.

**How to detect.** Judgment only. Signals: a base class or `ABC` with a single concrete subclass
in the package; abstract methods every subclass implements the same way; a registry or hook
added in the same commit as the first concrete case; a `Base*` or `Abstract*` name whose
subclasses share nothing beyond the inheritance line. None is a rule, since the second case may
be the next commit; a checker can list them as questions for the reviewer.

**How to fix.** Write the second and third concrete case in full, copying the first. Run the
tests. Look at what repeated and what did not: the repeated part is the generalization the code
asked for, and only that part moves up. Name the abstraction after the cases, not before them.
If an abstraction already exists with one implementation, inline it back and wait, which is
deixe-o-codigo-descansar applied to hierarchies.
