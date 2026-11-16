---
id: nomes-do-dominio-do-problema
title: Busque no domínio do problema o nome das variáveis
category: readability
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: desafios-pythonicos
    lesson: null
    section: "3.1"
    timestamp: null
  - type: course
    course: desafios-pythonicos
    lesson: 3
    section: "5"
    timestamp: "0:02:09"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 5
    section: "5"
    timestamp: "0:01:32"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 9
    section: "5"
    timestamp: "0:01:39"
    verified: false
  - type: course
    course: desafios-pythonicos
    lesson: 13
    section: "5"
    timestamp: "0:06:55"
    verified: false
---
**Rule.** Name variables, including short-lived auxiliaries, with words from the problem being
solved, not from the data type or the mechanics. A function that manipulates verbs has `verb`,
`suffix`, `ending`, not `s`, `text` or `msg`. When the problem is split in parts, each part keeps
the problem's vocabulary. Names stay short, but meaningful beats short.

**Why Henrique says so.** It is the most repeated hint of the Desafios Pythônicos series
(digest section 3.1). Avoid variables like s, text or message, things not related to the
problem's domain; the problem is manipulating verbs, so look there for the names (Pacote de
Desafios Pythônicos, lesson 5, 0:01:32 to 0:01:50, `verified: false`, transcript paraphrase).
Auxiliary names should be meaningful and at the same time not take much space (lesson 3,
0:02:09 to 0:02:22). When dividing a problem, keep its semantics: the list of words that start
with x and the list of those that do not, instead of a quick shortcut variable that makes the
code harder for the next reader (lesson 9, 0:01:36 to 0:02:14). In the wordcount, avoid names
outside the domain of counting words (lesson 13, 0:06:47 to 0:07:00). He asks for attention to
variable names from the first exercise (lesson 1, 0:01:40 to 0:01:45).

**Looks like.** Reconstructed for this note, not his code:

```python
def front_x(words):
    x_words = sorted(w for w in words if w.startswith('x'))
    other_words = sorted(w for w in words if not w.startswith('x'))
    return x_words + other_words
```

Bad: `def front_x(lst): a = [...]; b = [...]; return a + b`, or `s`, `tmp`, `data`, `res`
in a function whose problem has its own words. His own kit names several stub parameters `s`
(`05_verbing.py:13` at commit `ae90952`), which the digest records as a contrast, not as his
advice.

**How to detect.** Judgment. Signals: single-letter or generic names (`s`, `text`, `msg`,
`data`, `tmp`, `res`, `lst`, `a`/`b`) outside a tiny comprehension or a loop index; two
variables in one function whose names say nothing about how they differ; names that describe
the type (`string`, `list1`) where the problem has a word.

**How to fix.** Read the problem statement and pick its nouns; rename each variable to the word
the statement would use, and when a name gets long, look for a shorter word from the same
vocabulary rather than an abbreviation. Related: `o-codigo-e-a-interface` (names of classes and
methods as design), `codigo-linear`.
