---
name: henrique-watch
description: Maintainer skill for henriquefy. Checks HB Network playlists and Henrique Bastos's GitHub for new videos and commits and queues them for henrique-ingest. Use only when maintaining the henriquefy KB.
metadata:
  henriquefy_version: dev
---

# henrique-watch

Run `uvx henriquefy watch` (or `uv run henriquefy watch` from a checkout). It needs `yt-dlp` on
PATH and `gh auth login`; without `gh` it still checks YouTube and says it skipped GitHub.

It compares the channel's uploads and playlists and his repos with
`~/.henriquefy/state/watch.json` and appends what is new to `~/.henriquefy/state/queue.md`. The
first run only records a baseline. `HENRIQUEFY_HOME` moves `~/.henriquefy`.

Then work the queue with henrique-ingest, one item at a time:

- **Video in a known playlist:** run the `yt_fetch` command printed on the line, then update that
  course's digest.
- **Unassigned video:** find its playlist on the channel; if it is new, it will show as a playlist
  line too.
- **New playlist:** add it to `state/playlists.json` with a tier (see PLAN.md, section 2.5) in a PR.
- **Repo pushed or new:** if `kb/repos/<name>.md` exists, re-run `gh_fetch` and re-distill it;
  a new repo is a candidate for the mining list.

Tick the box in `queue.md` when an item is done. Schedule it weekly with cron, launchd or an agent
scheduler; the command is all it needs.
