---
id: teste-o-efeito-nao-o-codigo
title: Não teste código, teste o efeito do código
category: testing
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: labirinto-dos-testes
    lesson: null
    section: "3.7"
    timestamp: null
  - type: course
    course: labirinto-dos-testes
    lesson: 4
    section: "5"
    timestamp: "0:07:24"
    verified: false
  - type: course
    course: labirinto-dos-testes
    lesson: 5
    section: "5"
    timestamp: "0:07:23"
    verified: false
  - type: course
    course: labirinto-dos-testes
    lesson: 7
    section: "5"
    timestamp: "0:00:20"
    verified: false
---
**Rule.** Assert what the code does to the world (the returned value, the state it leaves, the
response, the record written), not how it does it. A test that has to change every time the
implementation changes is testing the code, and is a bad test.

**Why Henrique says so.** A test that changes when the code changes is testing the code; what you
want is to test the effect, so that changing the implementation does not touch the test
(Superando o Labirinto dos Testes, lesson 4, 0:07:20 to 0:07:31, `verified: false`, transcript
paraphrase). That is why he prefers black-box to white-box tests (lesson 5, 0:07:17 to 0:07:30),
and why a test is bad, for him, when there is a one-to-one relation between a change in the code
and a change in the test (lesson 7, 0:00:11 to 0:00:22). The test states the initial state, the
final state and the transition, not the implementation (lesson 3, 0:04:45 to 0:05:32).

**Looks like.** `assert order.status == Order.PAID` after `pay(order)`; `assert
response.status_code == HTTPStatus.CREATED` and the row exists. Bad: `mock.assert_called_once_with`
on each private helper, asserting the order of internal calls, or patching a function the code
under test merely happens to use today.

**How to detect.** Partly mechanical signals for a judgment call: tests dominated by
`assert_called*` on the module's own collaborators; patches of private names (`_helper`); a
refactor commit that touches many tests without changing behavior.

**How to fix.** Rewrite the assertion against the observable result, keep mocks only at the
boundary with external systems, and rerun the refactor to see the tests stay untouched. Related:
`a-interface-e-o-que-importa`, `teste-o-minimo-pelo-risco`.
