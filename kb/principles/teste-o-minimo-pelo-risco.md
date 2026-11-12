---
id: teste-o-minimo-pelo-risco
title: Sempre o mínimo possível, nunca menos que o mínimo
category: testing
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: labirinto-dos-testes
    lesson: null
    section: "3.3"
    timestamp: null
  - type: course
    course: labirinto-dos-testes
    lesson: null
    section: "3.6"
    timestamp: null
  - type: course
    course: labirinto-dos-testes
    lesson: 2
    section: "5"
    timestamp: "0:04:47"
    verified: false
  - type: course
    course: labirinto-dos-testes
    lesson: 3
    section: "5"
    timestamp: "0:16:34"
    verified: false
  - type: course
    course: labirinto-dos-testes
    lesson: 3
    section: "5"
    timestamp: "0:18:27"
    verified: false
  - type: course
    course: labirinto-dos-testes
    lesson: 7
    section: "5"
    timestamp: "0:16:14"
    verified: false
---
**Rule.** Tests buy confidence, never proof, so decide how much to test by risk in context:
always the minimum, never less than the minimum. Ask what needs testing, not how to test, and
point the tests (and the coverage you look at) at the paths whose failure costs the most.

**Why Henrique says so.** Following Myers (1979), testing is analysing a program to find errors
and defects, not validating that it works; more defects found means more confidence, and the
software is never proven to work (Superando o Labirinto dos Testes, lesson 2, 0:00:20 to
0:01:17, `verified: false`, transcript paraphrase). A test is a tool for confidence, not a
guarantee; it gives evidence that the system works (lesson 3, 0:15:44 to 0:16:22). How much to test is
always the minimum possible, never less than the minimum, found by risk analysis (lesson 2,
0:04:38 to 0:05:10). Change the question from how do I test to what do I need to test; the risks
are to life, money, reputation, opportunity, budget and deadline (lesson 3, 0:16:34 to 0:17:05),
and tolerance depends on context, so there is no best testing practice outside one (0:18:13 to
0:18:35). He sets no coverage target; he reads the coverage of what matters by risk (lesson 7,
0:16:01 to 0:16:34). He closes the course on the same line (lesson 8, 0:00:13, `verified:
false`, transcript paraphrase).

**Looks like.** The payment and permission paths carry scenario tests for each branch; a
formatting helper has one. Bad: a CI gate on 100% coverage that fills with tests of getters and
constants while the money path has one happy-path test; or no tests at all because "tests don't
prove anything".

**How to detect.** Judgment: compare where the tests are with where the risk is. Signals: a
coverage threshold as the only test policy; tests clustered on trivial code; branches of code
that moves money, data or permissions with no scenario.

**How to fix.** List what breaks worst if it fails, write the scenarios for those paths first,
read the coverage report only for them, and delete tests that guard nothing. Related: `taft`,
`teste-primeiro-das-folhas`, `teste-o-efeito-nao-o-codigo`.
