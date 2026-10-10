---
id: estanque-e-depois-repare
title: Na urgência, estanque agora e repare depois, avisando o efeito colateral
category: project
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: dicas-de-programacao
    lesson: null
    section: "6.12"
    timestamp: null
  - type: course
    course: dicas-de-programacao
    lesson: 40
    section: "5"
    timestamp: "0:01:20"
    verified: false
  - type: course
    course: dicas-de-programacao
    lesson: 40
    section: "5"
    timestamp: "0:01:45"
    verified: false
---
**Rule.** When a manager asks for a quick change, split it in two: stop the bleeding now, plan the repair later, and say out loud what side effect the shortcut leaves. Whoever decides to skip the repair knows the technical bill will come.

**Why Henrique says so.** The most important part is communicating the side effect of the chosen strategy (lesson 40, 0:01:20 to 0:01:45, `verified: false`, transcript paraphrase). Stop the bleeding first, reparative surgery after (lesson 40, 0:01:45 to 0:01:58). Whoever decides not to repair knows the bill arrives (lesson 40, 0:02:09 to 0:02:18).

**Looks like.** A hotfix commit with a TODO that links a ticket for the proper fix, and a note to the requester about the trade-off. Bad: a hotfix with no follow-up and no one told.

**How to detect.** Judgment: shortcut code with no recorded follow-up.

**How to fix.** Ship the minimal patch, write down the debt and its cost, and schedule the repair. See `funcione-direito-e-depois-rapido`.
