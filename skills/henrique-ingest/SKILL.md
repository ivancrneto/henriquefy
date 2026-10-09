---
name: henrique-ingest
description: Maintainer skill for henriquefy. Turns a source (HTML digest, YouTube playlist, GitHub repo) into knowledge-base entries with citations. Use only when adding or updating henriquefy KB content.
metadata:
  henriquefy_version: dev
---

# henrique-ingest

Maintainer pipeline; runs from a checkout of the henriquefy repository, never from the
installed package. Every step writes under gitignored `sources/` first and only then into `kb/`.

## Commands

- Course from an HTML digest: `uv run python -m henriquefy.ingest.html_to_md sources/html/<course>.html kb/courses/<course>.md`
- Course from YouTube captions: `uv run python -m henriquefy.ingest.yt_fetch <course-id> --windows`, then
  distill with `prompts/distill-transcript.md` (pass 1 per lesson, pass 2 cross-cutting) into
  `kb/courses/<course>.md`. Course ids live in `state/playlists.json`.
- His repos: `uv run python -m henriquefy.ingest.gh_fetch` (manifest plus clones), then distill each
  with `prompts/distill-repo.md` into `kb/repos/<name>.md` and `kb/patterns/`.
- Alumni calibration: `uv run python -m henriquefy.ingest.gh_fetch --alumni`, then
  `uv run python -m henriquefy.ingest.calibrate`; record the hand review in `evals/calibration/`.
- After any KB change: `uv run python -m henriquefy.ingest.build_index`, then `uv run pytest -q`.

## Rules

Every claim cites a lesson and timestamp or a repo path and commit. Caption quotes are
`verified: false`. Alumni code is never excerpted, named or ranked in anything committed.
