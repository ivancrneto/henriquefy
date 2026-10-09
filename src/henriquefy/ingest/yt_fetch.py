"""Fetch a playlist's metadata and automatic captions, and turn them into timestamped text.

    python -m henriquefy.ingest.yt_fetch <playlist_id|course_id> [--windows]

Writes under sources/transcripts/<course>/ (gitignored):
  playlist.json                 metadata per lesson (id, title, duration, upload date)
  NN-<video_id>.json3           raw caption file from yt-dlp (pt-orig, falling back to pt)
  NN-<video_id>.md              timestamped text, one line per caption event
  NN-<video_id>.windows.md      with --windows: ~15 minute windows with 2 minutes of overlap
Auto captions have no punctuation and mis-hear names and code; the distiller is told so.
"""

import json
import subprocess
import sys
import unicodedata
from pathlib import Path

from henriquefy.paths import state_dir

WINDOW = 15 * 60
OVERLAP = 2 * 60
LANGS = ("pt-orig", "pt")


def playlist_entry(key: str) -> dict:
    data = json.loads((state_dir() / "playlists.json").read_text(encoding="utf-8"))
    for p in data["playlists"]:
        if key in (p["id"], p.get("course"), course_id(p)):
            return p
    raise SystemExit(f"unknown playlist or course {key!r}; see state/playlists.json")


def course_id(entry: dict) -> str:
    """The entry's `course`, or a slug of its title: accents folded, punctuation dropped."""
    if entry.get("course"):
        return entry["course"]
    folded = unicodedata.normalize("NFKD", entry["title"].lower())
    slug = "".join(c for c in folded if not unicodedata.combining(c))
    return "-".join("".join(c if c.isalnum() else " " for c in slug).split())


def list_videos(playlist_id: str) -> list[dict]:
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "-J", f"https://www.youtube.com/playlist?list={playlist_id}"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    data = json.loads(out)
    return [
        {"index": i + 1, "id": e["id"], "title": e.get("title"), "duration": e.get("duration")}
        for i, e in enumerate(data.get("entries", []))
    ]


def fetch_captions(video_id: str, dest_stem: Path) -> Path | None:
    for lang in LANGS:
        subprocess.run(
            [
                "yt-dlp",
                "--skip-download",
                "--write-auto-sub",
                "--sub-lang",
                lang,
                "--sub-format",
                "json3",
                "--sleep-subtitles",
                "2",
                "-o",
                str(dest_stem),
                f"https://www.youtube.com/watch?v={video_id}",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        found = list(dest_stem.parent.glob(f"{dest_stem.name}.{lang}.json3"))
        if found:
            target = dest_stem.with_suffix(".json3")
            found[0].rename(target)
            return target
    return None


def json3_to_lines(raw: dict) -> list[tuple[int, str]]:
    """(start_ms, text) per caption event; aAppend events and newline-only segs are dropped."""
    lines = []
    for ev in raw.get("events", []):
        if ev.get("aAppend") or "segs" not in ev:
            continue
        text = "".join(s.get("utf8", "") for s in ev["segs"]).replace("\n", " ").strip()
        if text:
            lines.append((int(ev.get("tStartMs", 0)), text))
    return lines


def hms(ms: int) -> str:
    s = ms // 1000
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def render(lines: list[tuple[int, str]]) -> str:
    return "\n".join(f"[{hms(t)}] {text}" for t, text in lines) + "\n"


def windows(lines: list[tuple[int, str]]) -> str:
    if not lines:
        return ""
    end = lines[-1][0]
    out, start, n = [], 0, 1
    while start <= end:
        stop = start + WINDOW * 1000
        chunk = [(t, x) for t, x in lines if start - OVERLAP * 1000 <= t < stop]
        out.append(
            f"## window {n}: {hms(max(0, start - OVERLAP * 1000))} to {hms(min(stop, end))}\n\n"
            + render(chunk)
        )
        start, n = stop, n + 1
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    entry = playlist_entry(argv[0])
    course = course_id(entry)
    root = Path("sources/transcripts") / course
    root.mkdir(parents=True, exist_ok=True)
    videos = list_videos(entry["id"])
    (root / "playlist.json").write_text(
        json.dumps(
            {"course": course, "playlist": entry, "videos": videos}, indent=2, ensure_ascii=False
        )
    )
    missing = []
    for v in videos:
        stem = root / f"{v['index']:02d}-{v['id']}"
        if not stem.with_suffix(".md").exists():
            cap = (
                fetch_captions(v["id"], stem)
                if not stem.with_suffix(".json3").exists()
                else stem.with_suffix(".json3")
            )
            if cap is None:
                missing.append(v["id"])
                continue
            lines = json3_to_lines(json.loads(cap.read_text(encoding="utf-8")))
            stem.with_suffix(".md").write_text(render(lines), encoding="utf-8")
            if "--windows" in argv:
                stem.with_suffix(".windows.md").write_text(windows(lines), encoding="utf-8")
        print(f"{stem.name}: {v['title']} ({v['duration']}s)")
    if missing:
        print(f"no captions for {len(missing)} video(s): {' '.join(missing)}", file=sys.stderr)
    print(f"{course}: {len(videos) - len(missing)}/{len(videos)} transcripts under {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
