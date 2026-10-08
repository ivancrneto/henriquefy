# distill-repo

Input: a local clone of one of Henrique Bastos's repositories (class `his`) at a known commit,
plus `sources/repos/manifest.json` for sha, dates and license. Output: `kb/repos/<name>.md` and,
where the code shows a principle in practice, a `his` rendition in `kb/patterns/`.

## Digest schema (`kb/repos/<name>.md`)

```markdown
---
repo: <owner/name>
commit: <full sha>
era: <year created> to <year last pushed>
license: <spdx or none>
class: his
---
# <name>

**What it is.** One paragraph: purpose, size, stack, where it sits in his work.

**Layout.** Tree of the top level and the package, with one phrase per file on what it owns.

**How he tests.** Runner, layout of tests, naming, fixtures, mocks, what is and is not tested.
Cite files and line ranges.

**How he handles errors.** Exceptions declared, where raised, where handled, what reaches the
boundary. Cite.

**Naming and interface.** Module, class and function names; what the public surface is; what is
private. Cite.

**Packaging, config, tooling.** Build backend, dependency pinning, settings and secrets, CI,
Makefile, lint. State the year; this is where drift lives.

**README voice.** How he explains the project: first sentence, what he promises, examples.

**What this repo adds to the KB.** One bullet per principle it illustrates, with the principle
id and the file:line that shows it. One bullet per pattern file written or amended.

**Caveats.** Anything the code does that his courses argue against, stated plainly with the
line. Nothing is hidden to protect the score.
```

## Rules

- Every claim cites a path and line range at the manifest commit. Code excerpts: full excerpts
  from MIT or Apache repos; quotation-length (at most about 15 lines) from unlicensed or copyleft
  ones (`monopoly`, `eventex`, `pacote-desafios-pythonicos`, `gnucash-to-beancount`,
  `itauscraper`, `dcache`, `chipy8`).
- English prose. His own words (commit messages, docstrings, docs) in the original language,
  cited with path and line.
- A pattern rendition from a repo is `origin: his` with `repo`, `path`, `commit`. It replaces a
  `translated` rendition of the same framework when it shows the same shape; the `translated`
  one is deleted, not kept beside it.
- Never name, link or excerpt alumni code. Never add em-dashes or [[wikilinks]].
- Set `era` only on tooling: packaging, config, dependency management, CI, lint. Everything
  about modeling, errors, testing and naming stays `timeless`.
