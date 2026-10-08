---
id: teste-primeiro-das-folhas
title: Teste primeiro, começando pelas folhas
category: testing
weight: 5
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "2.2"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: 18
    section: "10"
    timestamp: "0:00:16"
    verified: false
  - type: course
    course: oo-na-pratica
    lesson: 6
    section: "7"
    timestamp: null
  - type: course
    course: oo-na-pratica
    lesson: null
    section: "19.7"
    timestamp: null
  - type: repo
    class: his
    repo: henriquebastos/monopoly
    path: tests/test_player.py
    commit: bffb0c269b00836066d0bb064ca4e38a80cad210
---
**Rule.** Write the test before the code, and start with the leaves of the system: the entities
with one responsibility and few relations. The cycle is short: write the test, watch it fail,
implement the minimum, watch it pass. The tests are the executable specification; a test that
asserts nothing specifies nothing.

**Why Henrique says so.** He opens the implementation of the simulator by saying where he will
start: eu quero começar comendo pelas beiradas, indo pelas folhas do sistema (lesson 18, 0:16,
`verified: false`, transcript paraphrase), and why: eu vou fazer de dentro para fora, pegando o
jogador, pegando a propriedade, porque eles estão com responsabilidades únicas e poucas relações
(lesson 18, 1:46, `verified: false`, transcript paraphrase). From lesson 6 on, the method is
"pensamento positivo": write the test first and ignore the editor's error marks on names that
do not exist yet (digest section 7, lesson 6; glossary). The digest's reading of his test files
(section 19.7) calls them the only source of the specification the transcript does not give:
`test_pay` states that `p.pay(10) == 10`, and the boundary values in the strategy tests fix the
rules at `> 50` and `>= 80`.

**Looks like.** `monopoly/tests/test_player.py` at commit `bffb0c2`: fifteen small tests, each
asserting one behavior of `Player`, with a single mock in the whole project, for `random.choice`
in the gambler strategy, because that is the only non-deterministic decision. Bad: a test
module written after the fact that instantiates objects and calls methods without asserting
anything, or an integration test written first because "I want to see it working".

**How to detect.** Partial. Mechanical: a `test_*` function with no `assert`, no call to an
attribute named `assert*`, and no `pytest.raises` or `pytest.warns` block (rule
`testing.no-assert`; known false positive: assertions delegated to a helper, handled with the
ignore comment); a project with no tests at all (rule `project.no-tests`). Judgment: whether the
tests came first, whether they start at the leaves, and whether each one names a behavior.

**How to fix.** Pick the leaf: the class with the fewest collaborators. Write one test for one
behavior, run it, watch it fail for the right reason, write the minimum, run it green. Move
outward only when the leaf is covered. Mock only what is non-deterministic or external.
