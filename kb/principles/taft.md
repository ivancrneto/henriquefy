---
id: taft
title: Testar o tempo todo, automaticamente
category: testing
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: raio-x-do-tdd
    lesson: null
    section: "6.1"
    timestamp: null
  - type: course
    course: raio-x-do-tdd
    lesson: 1
    section: "5"
    timestamp: "0:13:35"
    verified: false
  - type: course
    course: raio-x-do-tdd
    lesson: 1
    section: "5"
    timestamp: "0:13:38"
    verified: false
  - type: course
    course: raio-x-do-tdd
    lesson: 1
    section: "5"
    timestamp: "0:14:10"
    verified: false
---
**Rule.** Test all the time, and test automatically. Untested code is a risk. Manual testing
does not scale. The kind of test (functional, unit, load, acceptance) is a tool in the box.
The point is why you test, and that the test runs every time the code moves.

**Why Henrique says so.** Lesson 1 is the mantra lesson. The playlist title is TAFT. The
caption hears the name as Dafiti and the expansion as test all the fucking time, said as
teste all the fucking all the fucking o tempo inteiro (lesson 1, 0:13:27 and 0:13:30,
`verified: false`, transcript paraphrase). His line, right after: untested code is a risk to
society, you have to test the software all the time (0:13:38, `verified: false`, transcript
paraphrase). Manual testing does not scale, so the test has to be automatic (0:14:10,
`verified: false`, transcript paraphrase). He attributes the term to Brian Lions, as the
caption hears the name, and does not spell a URL (0:13:47).

**Looks like.** A change lands with an automatic check that already failed once for the wrong
reason and now passes. Bad: a feature considered done because someone clicked through it once.

**How to detect.** Judgment. A behavior change with no test run, or a suite that only a person
can execute. No mechanical rule yet.

**How to fix.** Turn the expectation into an automatic check before the next edit. Keep the
check in the path that already runs, so the next change cannot land in silence.
