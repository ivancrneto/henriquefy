---
id: erro-antes-da-falha
title: Erro antes de falha
category: testing
weight: 4
detectable: judgment
era: timeless
scope: python
sources:
  - type: course
    course: raio-x-do-tdd
    lesson: null
    section: "6.3"
    timestamp: null
  - type: course
    course: raio-x-do-tdd
    lesson: 3
    section: "5"
    timestamp: "0:08:03"
    verified: false
  - type: course
    course: raio-x-do-tdd
    lesson: 3
    section: "5"
    timestamp: "0:07:25"
    verified: false
  - type: course
    course: raio-x-do-tdd
    lesson: 4
    section: "5"
    timestamp: "0:04:35"
    verified: false
  - type: course
    course: raio-x-do-tdd
    lesson: 5
    section: "5"
    timestamp: "0:20:17"
    verified: false
---
**Rule.** An error and a failure are different, and the error comes first. A failure is an
expectation that was not met. An error is the code blowing up: an exception that was not the
expectation. Fix the error before you chase the failed assertion. A report that stops at the
first one hides the rest, and the rest is often the cause.

**Why Henrique says so.** In the fizzbuzz kata he separates the two as soon as the first test
runs: a failed expectation is a failure, anything else exploding in the code is an error, and
solving an error is always higher priority than solving a failure (lesson 3, 0:07:25 and
0:08:03, `verified: false`, transcript paraphrase). The happy-numbers dojo walks the same
states: exceptions are the error state, and assert returning false is the failure state
(lesson 4, 0:04:35, `verified: false`, transcript paraphrase). When he later breaks the same
kata on purpose, a wrong boolean is a failure and an undefined name is an error (lesson 5,
0:20:17 and 0:20:42, `verified: false`, transcript paraphrase). He also wants every test to
run, because the first error may have been caused by another (lesson 5, 0:01:06,
`verified: false`, transcript paraphrase).

**Looks like.** The suite runs to the end. A `NameError` or `TypeError` is fixed before the
assertion message is tuned. Bad: editing the expected value while the test still raises
because the function does not exist.

**How to detect.** Judgment. A red test whose traceback is an unexpected exception, treated as
if the assertion were wrong. No mechanical rule yet.

**How to fix.** Read the traceback from the bottom. If the exception is not the failed
expectation, make that exception go away with the smallest change that lets the test reach the
assertion. Only then change the code so the expectation holds.
