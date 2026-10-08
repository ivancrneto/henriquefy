---
id: execute-antes-de-ler
title: Execute antes de ler; cerque o comportamento antes de mudar
category: testing
weight: 5
detectable: partial
era: timeless
scope: python
sources:
  - type: course
    course: refatoracao-na-pratica
    lesson: null
    section: "6.2"
    timestamp: null
  - type: course
    course: refatoracao-na-pratica
    lesson: 20
    section: "5"
    timestamp: "0:02:17"
    verified: false
  - type: course
    course: refatoracao-na-pratica
    lesson: 20
    section: "5"
    timestamp: "0:05:08"
    verified: false
  - type: course
    course: refatoracao-na-pratica
    lesson: 2
    section: "5"
    timestamp: null
---
**Rule.** Never refactor code you cannot prove still works. Before reading legacy code, run it;
before changing it, fence its current behavior with black-box tests, golden files for a
deterministic program, and run them after every single move. A refactoring without a test run
between steps is a rewrite with extra risk.

**Why Henrique says so.** This is the rule the course repeats most, in twelve of its lessons
(digest section 6.2). Handed a program with no tests, he runs it first: execute before you read,
so you know what it does, not what it says (lesson 20, 0:02:17, `verified: false`, transcript
paraphrase). Then he captures its output as golden files and compares with `diff`, and only then
turns that into pytest, so every later step has a verdict (lesson 20, 0:05:08 to 0:06:49,
`verified: false`, transcript paraphrase). Refactoring is changing structure without changing
behavior (digest section 6.1), and behavior you have not pinned cannot be shown unchanged.

**Looks like.** A `tests/` directory that appears in the first commit of a refactoring, holding
characterization tests of the program as found, warts included; then small commits, each green.
Bad: a refactoring commit that touches twenty functions with no test in the tree, or a test
suite added after the rewrite that only proves the new behavior.

**How to detect.** Partial. Mechanical: a project with no tests at all (rule `project.no-tests`)
is the precondition this principle forbids refactoring under. Judgment: whether tests existed
before the change, whether they pin the old behavior, whether the steps were small enough to
run them between.

**How to fix.** Run the program and keep its outputs. Write black-box tests from those outputs,
golden files when the program is deterministic. Only then change one thing, run, repeat. This is
step 2 of the henriquefy `transform` playbook.
