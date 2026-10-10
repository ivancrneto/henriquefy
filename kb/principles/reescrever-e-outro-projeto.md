---
id: reescrever-e-outro-projeto
title: Reescrever com outra tecnologia é outro projeto, com outro risco
category: project
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: dicas-de-programacao
    lesson: null
    section: "6.13"
    timestamp: null
  - type: course
    course: dicas-de-programacao
    lesson: 31
    section: "5"
    timestamp: "0:00:52"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 31
    section: "5"
    timestamp: "0:02:49"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 27
    section: "5"
    timestamp: "0:02:19"
    verified: false
---
**Rule.** Changing technology, architecture and scope together is not a refactor, it is a new project with its own budget and risk. Treat legacy with regression tests, refactoring and targeted interventions, and a programmer's job is to manage that risk.

**Why Henrique says so.** Rewriting in another technology, architecture and scope is another project, with a spreadsheet and a budget (lesson 31, 0:00:52 to 0:02:21, `verified: false`, transcript paraphrase). Throwing the legacy away and starting from scratch is very expensive (lesson 27, 0:02:19 to 0:02:23). The programmer's work is to manage risk (lesson 31, 0:02:49 to 0:03:00).

**Looks like.** A ticket "rewrite X in Y" that has an estimate, a rollback plan and a parallel-run period. Bad: a rewrite proposed as cleanup, with no test pinning the old behavior.

**How to detect.** Judgment: a change that swaps language or framework, restructures and adds scope in one step.

**How to fix.** Pin the behavior with regression tests, then move in small steps that keep the system running; when a real rewrite is justified, scope and price it as a project. Related: `execute-antes-de-ler`.
