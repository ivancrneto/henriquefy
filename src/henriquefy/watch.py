"""Find what HB Network and Henrique's GitHub published since the last run, and queue it for ingest.

    henriquefy watch            # or: uv run python -m henriquefy.watch

Lists the channel's uploads and playlists with yt-dlp, and his repos with `gh api`, compares them
with ~/.henriquefy/state/watch.json, and appends the new sources, each with the command to run, to
~/.henriquefy/state/queue.md. The first run records a baseline and queues nothing.
YouTube's keyless RSS feeds (the original plan) answered 404 for every channel and playlist on
2026-10-14, so listing goes through yt-dlp, which the ingest already needs.
"""

import json
import subprocess
import sys
from collections.abc import Callable
from datetime import date

from .ingest.gh_fetch import OWNERS, gh
from .ingest.yt_fetch import course_id
from .paths import home, state_dir

CHANNEL = "https://www.youtube.com/channel/{}"


def _flat(url: str) -> list[dict]:
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "-J", url], capture_output=True, text=True, check=True
    ).stdout
    return [{"id": e["id"], "title": e.get("title")} for e in json.loads(out).get("entries", [])]


def uploads(channel_id: str) -> list[dict]:
    return _flat(CHANNEL.format(channel_id) + "/videos")


def playlists(channel_id: str) -> list[dict]:
    return _flat(CHANNEL.format(channel_id) + "/playlists")


def playlist_videos(playlist_id: str) -> list[str]:
    return [v["id"] for v in _flat(f"https://www.youtube.com/playlist?list={playlist_id}")]


def repos() -> dict[str, str]:
    """His own repos (forks of other people's excluded) and when each was last pushed."""
    pushed = {}
    for owner in OWNERS:
        kind = "orgs" if owner == "HBNetwork" else "users"
        for r in gh(f"{kind}/{owner}/repos?per_page=100", paginate=True):
            if not r.get("fork"):
                pushed[r["full_name"]] = r["pushed_at"]
    return pushed


def find_new(
    state: dict,
    known: list[dict],
    channel_uploads: list[dict],
    channel_playlists: list[dict],
    videos_of: Callable[[str], list[str]],
    his_repos: dict[str, str] | None,
) -> tuple[list[str], dict]:
    """Queue lines for everything not in `state`, and the state to save after this run.

    `known` is state/playlists.json's list; `his_repos` is None when GitHub was unreachable,
    which keeps the repo state as it was.
    """
    seen = set(state.get("videos", []))
    seen_playlists = set(state.get("playlists", []))
    old_repos = state.get("repos", {})
    by_id = {p["id"]: p for p in known}
    queue = []

    for p in channel_playlists:
        if p["id"] not in by_id and p["id"] not in seen_playlists:
            queue.append(
                f"- [ ] playlist {p['id']} {p['title']!r}: new playlist;"
                " add it to state/playlists.json with a tier"
            )

    fresh = [v for v in channel_uploads if v["id"] not in seen]
    home_of = {}
    if fresh:  # open the known playlists only when there is something to place
        for p in known:
            for vid in videos_of(p["id"]):
                home_of.setdefault(vid, p)
    for v in fresh:
        p = home_of.get(v["id"])
        if p is None:
            queue.append(
                f"- [ ] video {v['id']} {v['title']!r}: unassigned, check for a new playlist"
            )
            continue
        queue.append(
            f"- [ ] video {v['id']} {v['title']!r} in {p['title']!r}:"
            f" uv run python -m henriquefy.ingest.yt_fetch {course_id(p)} --windows"
        )

    if his_repos is not None:
        for name, pushed in sorted(his_repos.items()):
            if name not in old_repos:
                queue.append(f"- [ ] repo {name}: new repo, pushed {pushed}; worth mining?")
            elif pushed > old_repos[name]:
                queue.append(
                    f"- [ ] repo {name}: pushed {pushed} (was {old_repos[name]});"
                    f" if kb/repos/{name.split('/')[1]}.md exists,"
                    " uv run python -m henriquefy.ingest.gh_fetch and re-distill it"
                )

    new_state = {
        "videos": sorted(seen | {v["id"] for v in channel_uploads}),
        "playlists": sorted(seen_playlists | {p["id"] for p in channel_playlists}),
        "repos": old_repos if his_repos is None else his_repos,
    }
    return queue, new_state


def main(argv: list[str] | None = None) -> int:
    known = json.loads((state_dir() / "playlists.json").read_text(encoding="utf-8"))
    channel = known["channel_id"]
    try:
        channel_uploads, channel_playlists = uploads(channel), playlists(channel)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"cannot list the channel with yt-dlp: {exc}", file=sys.stderr)
        return 2
    try:
        his_repos = repos()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"skipping GitHub (gh api failed: {exc}); repo state kept", file=sys.stderr)
        his_repos = None

    state_path = home() / "state" / "watch.json"
    first_run = not state_path.is_file()
    state = {} if first_run else json.loads(state_path.read_text(encoding="utf-8"))
    videos_of = (lambda _: []) if first_run else playlist_videos  # a baseline places nothing
    queue, new_state = find_new(
        state, known["playlists"], channel_uploads, channel_playlists, videos_of, his_repos
    )
    state_path.parent.mkdir(parents=True, exist_ok=True)
    if first_run:
        queue = []
        print(f"baseline recorded in {state_path}; the next run queues what is new")
    if queue:
        with (state_path.parent / "queue.md").open("a", encoding="utf-8") as f:
            f.write(f"\n## {date.today()}\n\n" + "\n".join(queue) + "\n")
        print("\n".join(queue))
        print(f"appended {len(queue)} to {state_path.parent / 'queue.md'}")
    elif not first_run:
        print("nothing new")
    state_path.write_text(json.dumps(new_state, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
