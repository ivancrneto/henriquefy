---
id: use-o-framework-sem-abstrai-lo
title: Use o framework; não o abstraia nem o construa antes do sistema
category: simplicity
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: dicas-de-programacao
    lesson: null
    section: "6.17"
    timestamp: null
  - type: course
    course: dicas-de-programacao
    lesson: 33
    section: "5"
    timestamp: "0:00:17"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 33
    section: "5"
    timestamp: "0:01:28"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 50
    section: "5"
    timestamp: "0:00:14"
    verified: false
---
**Rule.** Use the framework you chose directly. Decoupling pays by letting you intervene, not by letting you swap parts. Do not wrap the framework behind your own abstraction, and do not build a framework before the system that needs it.

**Why Henrique says so.** The advantage of decoupling is to intervene, not to swap (lesson 33, 0:00:17 to 0:00:29, `verified: false`, transcript paraphrase). Abstracting the framework is what he does not do at all (lesson 33, 0:01:28 to 0:01:41). Everything is a library (lesson 41, 0:00:15), and do not build the framework before the system (lesson 50, 0:00:14 to 0:00:29; noisy captions).

**Looks like.** Views and models that use Django idioms directly, with business rules in plain objects kept apart. Bad: an `AbstractWebFramework` layer written so the project could change frameworks someday.

**How to detect.** Judgment: wrapper classes whose only job is to forward to one framework, with a single implementation.

**How to fix.** Inline the wrapper, keep the business rules independent of the framework, and extract a shared piece only when a second real use appears. Related: `nao-projete-a-generalizacao`.
