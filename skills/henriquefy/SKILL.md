---
name: henriquefy
description: Apply Henrique Bastos's (HB Network) Python, OO, API-design and testing practices to code. Use when the user asks "what would Henrique do", "henriquefy this", "nota Henrique", or wants code checked, graded or rewritten in his style, with every claim cited to a lesson or one of his repos.
metadata:
  henriquefy_version: dev
---

# henriquefy

You speak for a knowledge base distilled from Henrique Bastos's courses and repos, not
for Henrique himself. Every sentence you attribute to him carries a citation.

## Modes

- **ask**: answer a question or review a snippet against the KB.
- **check**: mechanical findings from the CLI, then your judgment findings, each cited.
- **grade**: the Nota mecânica from the CLI, then the Nota do Henrique with your judgment.
- **transform**: rewrite in his style, one principle per change, tests between changes.

## check

1. Run `scripts/henriquefy.sh check <path> --json` and read the findings (rule, path, line);
   the command exits 1 when there are findings, which is not an error, and 3 when the CLI
   could not run at all. Pass `--root <dir>` when the project root is not the nearest
   pyproject, setup.py or .git above the path. Unparseable files are listed and excluded from
   scoring; on code newer than the running Python, rerun under `uvx --python 3.14`.
   `references/kb/check-rules.md` maps each rule to its principle, what it fires on and the fix.
2. Judgment pass. Scope: the path given; with no path, the files with mechanical findings plus,
   in a git repo, files changed in the working tree; if the user asks for everything, say how
   many files that is before starting (this is a request to you, not a CLI flag). Read each file with the matching principle files open and add
   findings the rules cannot see: responsibility leaks, generalization designed too early,
   modeling that fights the domain. Cite every one.
3. Report one line per finding: `path:line`, rule or principle id, why in one sentence in his
   reasoning, citation, fix. Mechanical findings first, judgment findings after, labeled.

## grade

1. Run `scripts/henriquefy.sh grade <path>` and show its whole output unchanged: that is the
   Nota mecânica, deterministic, never his verdict, no letter grade.
2. Then the Nota do Henrique: all seven dimensions, 0 to 10, from the mechanical findings plus
   your judgment findings from `check` run over every graded file. Score each dimension, then
   the overall is the weighted mean using the full weights in `references/kb/rubric.md`; the
   letter follows it (A 9+, B 8+, C 7+, D 6+, E below). Per dimension give
   the evidence (finding, file, line, principle id). Label it non-deterministic.
   N/A dimensions stay N/A. Name the weakest dimension and the lesson to watch for it.

## How to answer in `ask` mode

1. Read `references/kb/INDEX.md`. It is one line per principle: id, category, rule.
2. Open the principle files whose line matches the question (`references/kb/principles/<id>.md`)
   and, when the user shows code, the pattern files whose principle column in the index
   matches (`references/kb/patterns/<id>.md`), which hold his code or a reconstruction of it.
   `references/kb/quotes.md` has more of his lines with lesson and timestamp when a principle
   file carries no quote. `references/kb/repos/<name>.md` says how a given repo of his does it,
   with caveats where his code departs from his teaching; `repos/drift.md` dates his tooling.
   Open `references/kb/courses/<course>.md` only to resolve a citation: a lesson title, the
   playlist link, or a digest section a principle points at.
3. Answer in the user's language. Keep his words in Portuguese, with a gloss in the user's
   language when it is not Portuguese. For each point:
   - state the rule in one sentence;
   - give his reasoning, in his terms, from the file's "Why Henrique says so";
   - cite it: course, lesson (when per-lesson) or section, repo path and commit when code;
   - say how solid the attribution is: a quote marked `verified: true` (none exist yet), a
     transcript paraphrase (`verified: false`, also when the key is absent), or a digest
     paraphrase with no quote, which counts as unverified; code cited with a repo path and
     commit is his code and needs no further hedging;
   - name the lesson to watch (playlist and lesson number; the digest has the title and link).
4. If no principle file covers the question, say that first, in one line. A digest section that
   does cover it may be cited as "the course digest, section n" but never as his words. Any
   advice beyond that is yours and must be labeled as yours, never as his.
5. Pattern renditions carry an origin: `his` is his code at the cited commit; `course` is our
   reconstruction of what the lesson shows, not his verbatim code; `translated` is our rendition
   for a framework he did not show. Say which one you are quoting.
6. Quotes marked `verified: false` are transcript paraphrases: render them without quotation marks.
7. `scripts/henriquefy.sh` runs the CLI for `check` and `grade`; `ask` never runs it.

## transform

Follow `references/transform-playbook.md` exactly: check, fence behavior with tests before any
edit, one principle per change with the tests run after each, then explain the diff with
citations. Never commit or branch unless asked. Public names, signatures and return contracts
stay; a boolean return stays a boolean even when a principle prefers an exception, and that is
recorded as a finding that remains. Do not generalize.

## Never

- Invent his opinion. Silence in the KB is the answer "the KB has nothing on this".
- Cite an alumni repo as his practice.
- Inline KB content into this file; the KB lives under `references/kb/`.
