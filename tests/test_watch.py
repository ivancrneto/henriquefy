"""watch: fixture listings, a temporary state, no network (PLAN.md Phase 6 exit criterion)."""

import json

from henriquefy import watch

KNOWN = [{"id": "PLdicas", "title": "Dicas de Programação", "course": "dicas-de-programacao"}]
STATE = {
    "videos": ["old1"],
    "playlists": ["PLdicas"],
    "repos": {"henriquebastos/monopoly": "2022-01-01T00:00:00Z"},
}
UPLOADS = [
    {"id": "old1", "title": "Velho"},
    {"id": "new1", "title": "Dica nova"},
    {"id": "new2", "title": "Avulso"},
]
PLAYLIST_VIDEOS = {"PLdicas": ["old1", "new1"]}


def test_new_video_in_a_known_playlist_queues_its_ingest_and_a_stray_is_unassigned():
    queue, state = watch.find_new(
        STATE, KNOWN, UPLOADS, [{"id": "PLdicas", "title": "Dicas"}], PLAYLIST_VIDEOS.get, None
    )
    assert queue == [
        "- [ ] video new1 'Dica nova' in 'Dicas de Programação':"
        " uv run python -m henriquefy.ingest.yt_fetch dicas-de-programacao --windows",
        "- [ ] video new2 'Avulso': unassigned, check for a new playlist",
    ]
    assert state["videos"] == ["new1", "new2", "old1"]
    assert state["repos"] == STATE["repos"]  # GitHub unreachable: kept as it was


def test_nothing_new_lists_no_playlist():
    def videos_of(_):
        raise AssertionError("no fresh upload, so no playlist should be opened")

    queue, _ = watch.find_new(STATE, KNOWN, UPLOADS[:1], [], videos_of, None)
    assert queue == []


def test_new_playlist_and_repos_are_queued():
    repos = {
        "henriquebastos/monopoly": "2026-10-01T00:00:00Z",
        "henriquebastos/novo": "2026-10-02T00:00:00Z",
    }
    queue, state = watch.find_new(
        STATE,
        KNOWN,
        UPLOADS[:1],
        [{"id": "PLnew", "title": "Novo curso"}],
        PLAYLIST_VIDEOS.get,
        repos,
    )
    assert queue[0].startswith("- [ ] playlist PLnew 'Novo curso': new playlist")
    assert (
        "henriquebastos/monopoly: pushed 2026-10-01T00:00:00Z (was 2022-01-01T00:00:00Z)"
        in queue[1]
    )
    assert queue[2].startswith("- [ ] repo henriquebastos/novo: new repo")
    assert state["repos"] == repos and "PLnew" in state["playlists"]


def test_first_run_records_a_baseline_then_the_second_queues(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("HENRIQUEFY_HOME", str(tmp_path))
    monkeypatch.setattr(watch, "uploads", lambda _: UPLOADS[:1])
    monkeypatch.setattr(watch, "playlists", lambda _: [])
    monkeypatch.setattr(watch, "repos", lambda: {})
    monkeypatch.setattr(
        watch,
        "playlist_videos",
        lambda pid: ["new1"] if pid == "PLeKXYyZCJHxdnGoV8TBYzKqsm8p3PIEeQ" else [],
    )
    assert watch.main() == 0
    assert not (tmp_path / "state" / "queue.md").exists()
    assert json.loads((tmp_path / "state" / "watch.json").read_text())["videos"] == ["old1"]

    monkeypatch.setattr(watch, "uploads", lambda _: UPLOADS[:2])
    assert watch.main() == 0
    queue = (tmp_path / "state" / "queue.md").read_text()
    assert "yt_fetch dicas-de-programacao --windows" in queue
    assert "nothing new" not in capsys.readouterr().out
