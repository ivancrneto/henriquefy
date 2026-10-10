---
id: migracao-junto-do-codigo
title: A migração caminha junto com a mudança de código
category: project
weight: 2
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: dicas-de-programacao
    lesson: null
    section: "6.16"
    timestamp: null
  - type: course
    course: dicas-de-programacao
    lesson: 22
    section: "5"
    timestamp: "0:00:42"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 22
    section: "5"
    timestamp: "0:02:57"
    verified: false
---
**Rule.** Schema and database state are part of the code. Generate the migration with the code change and commit them together.

**Why Henrique says so.** Schema and database state are part of the code (lesson 22, 0:00:42 to 0:00:53, `verified: false`, transcript paraphrase). Generate the migration before the commit, matched to the change (lesson 22, 0:02:57 to 0:03:23).

**Looks like.** One commit with a model change and its migration file. Bad: a model change whose migration lands later, or a migration edited by hand on the server.

**How to detect.** Judgment, with a possible mechanical check: model files changed with no new migration in the same commit.

**How to fix.** Run the migration generator before committing and review the generated file as code.
