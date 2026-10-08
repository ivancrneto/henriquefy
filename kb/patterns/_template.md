---
id: <kebab-case-id>
title: <short name>
principle: <principle-id>          # the principle this pattern makes concrete
category: errors                   # same set as principles
era: timeless                      # set only when the pattern's subject is a tool (packaging, config, CI)
frameworks:                        # one entry per rendition; keys: python | django | fastapi
  python:  {origin: his, repo: <owner/name>, path: <path>, commit: <sha>}
  django:  {origin: course, course: <course-id>, lesson: <n>, section: "<n.m>"}   # shape from the lesson, code rewritten by us
  fastapi: {origin: translated}    # our rendition of his principle for a framework he did not show
---
**What.** One paragraph: the shape of the code and when it applies.

## python
Code excerpt (quotation-length when the repo is unlicensed) with path and commit, then two or
three sentences on what to notice.

## django
`origin: course` means the shape is what the lesson shows and the code is our reconstruction,
not his verbatim code; say so in the first line. Never copy code from alumni repos.

## fastapi
Marked `translated`: say in the first line that this is our rendition, not his code.

## Bad
The shape this pattern replaces, in a few lines of code.
