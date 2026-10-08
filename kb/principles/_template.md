---
id: <kebab-case-id>
title: <his phrasing, Portuguese>
category: modeling            # modeling | simplicity | errors | testing | api | project | readability | career
weight: 3                     # 1-5, feeds the rubric
detectable: judgment          # mechanical | partial | judgment
era: timeless                 # timeless | 2010s | 2020s | 2026; only tooling principles are dated
scope: python                 # python | api | web | project | career; never a framework name
sources:
  - type: course
    course: <course-id>
    lesson: null              # set only when the section is a per-lesson one
    section: "<n.m>"          # section of kb/courses/<course-id>.md
    timestamp: null           # hh:mm:ss when the source is a transcript
  - type: repo
    class: his                # his | course; alumni never appears in a principle
    repo: <owner/name>
    path: <path>
    commit: <sha>
---
**Rule.** One-paragraph statement in English.

**Why Henrique says so.** The reasoning, in his terms. Verbatim quote in Portuguese, or a
timestamped paraphrase marked `verified: false`.

**Looks like.** Good example (from his repo when possible). Bad example.

**How to detect.** Signals a checker can use. Rule ids in `kb/check-rules.md`.

**How to fix.** The refactor, step by step, in his order.
