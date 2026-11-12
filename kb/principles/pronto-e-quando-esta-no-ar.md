---
id: pronto-e-quando-esta-no-ar
title: Pronto é quando está no ar
category: project
weight: 3
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: protagonista-da-carreira
    lesson: null
    section: "6.4"
    timestamp: null
  - type: course
    course: protagonista-da-carreira
    lesson: null
    section: "6.5"
    timestamp: null
  - type: course
    course: protagonista-da-carreira
    lesson: 3
    section: "5"
    timestamp: "0:06:02"
    verified: false
  - type: course
    course: protagonista-da-carreira
    lesson: 3
    section: "5"
    timestamp: "0:07:46"
    verified: false
  - type: course
    course: protagonista-da-carreira
    lesson: 3
    section: "5"
    timestamp: "0:02:40"
    verified: false
---
**Rule.** A task is done when it is deployed and the client can use it, not when the code is
written. Setting up the project, running every test and releasing are each one command.

**Why Henrique says so.** The most common dialogue in software is the manager asking whether it
is done and the programmer answering that it only needs to go live, which is the works on my
machine syndrome (Workshop: Torne-se protagonista da sua carreira na programação, lesson 3,
0:06:02 to 0:06:15, `verified: false`, Whisper transcript paraphrase). Finishing a task includes
the deploy, so the client can use what you made, and until you get real feedback from the client
nothing is really done (lesson 3, 0:06:30 to 0:06:46). However complex the deploy is, you need a
way to put the code on a server easily: no copying files to a pen drive or logging in as root,
one command makes the release happen (lesson 3, 0:07:19 to 0:07:48, `verified: false`, Whisper
transcript paraphrase). The same goes for the start of the work: a new programmer should prepare
everything with one command, and one command runs all the tests (lesson 3, 0:02:40 to 0:03:10).

**Looks like.** A `make deploy`, `scripts/release` or release workflow that ships the merged code,
next to one-command setup and test entries in the README. Bad: a merged PR whose ticket is closed
while the deploy is a manual checklist someone runs next week.

**How to detect.** Judgment: a project with no scripted setup, test or release step; a README
whose deploy section is a list of manual server steps.

**How to fix.** Script the setup, the test run and the release until each is one command, and
count a task as done only after its deploy. Related: `eficacia-acima-de-eficiencia`, `taft`,
`funcione-direito-e-depois-rapido`.
