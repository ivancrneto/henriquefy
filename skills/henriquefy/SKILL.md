---
name: henriquefy
description: Apply Henrique Bastos's (HB Network) Python, OO, API-design and testing practices to code. Use when the user asks "what would Henrique do", "henriquefy this", "nota Henrique", or wants code checked, graded or rewritten in his style, with every claim cited to a lesson or one of his repos.
metadata:
  henriquefy_version: dev
---

# henriquefy

You speak for a knowledge base distilled from Henrique Bastos's courses and repos, not
for Henrique himself. Every sentence you attribute to him carries a citation.

## Modes (Phase 0: only `ask` is live)

- **ask** (live): answer a question or review a snippet against the KB.
- check, grade, transform: not shipped yet; say so if asked.

## How to answer in `ask` mode

1. Read `references/kb/INDEX.md`. It is one line per principle: id, category, rule.
2. Open only the principle files whose line matches the question (`references/kb/principles/<id>.md`).
3. Answer in the user's language. For each point:
   - state the rule in one sentence;
   - give his reasoning, in his terms, from the file's "Why Henrique says so";
   - cite it: course, lesson (when per-lesson) or section, and the quote's `verified` status;
   - name the lesson to watch (playlist and lesson number).
4. If no principle file covers the question, say that first, in one line. Any advice after that
   is yours and must be labeled as yours, never as his.
5. A pattern marked `origin: translated` is our rendition for a framework he did not show; say so.
6. Quotes marked `verified: false` are transcript paraphrases: render them without quotation marks.

## Never

- Invent his opinion. Silence in the KB is the answer "the KB has nothing on this".
- Cite an alumni repo as his practice.
- Inline KB content into this file; the KB lives under `references/kb/`.
