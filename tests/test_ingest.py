"""Ingest helpers that need no network: HTML conversion, index lines, slugs, windows, forks."""

from henriquefy.ingest.build_index import rule_line
from henriquefy.ingest.calibrate import fork_of
from henriquefy.ingest.html_to_md import convert
from henriquefy.ingest.yt_fetch import course_id, playlist_entry, windows


def test_nested_lists_indent_to_the_parent_content_column():
    assert convert("<ol><li>a<ol><li>b</li></ol></li><li>c</li></ol>") == "1. a\n   1. b\n2. c\n"
    assert convert("<ul><li>a<ul><li>b</li></ul></li></ul>") == "- a\n  - b\n"


def test_ordered_list_keeps_its_start_number():
    """Section 12.9 is heading 12, item 9, also when the list was split and restarted at 5."""
    assert convert('<ol start="5"><li>x</li><li>y</li></ol>') == "5. x\n6. y\n"


def test_table_cells_keep_spaces_between_inline_tags_and_join_br():
    md = convert("<table><tr><td>a<br>b</td><td><code>x</code> <code>y</code></td></tr></table>")
    assert md == "| a b | `x` `y` |\n|---|---|\n"


def test_pre_keeps_entities_as_code():
    assert convert("<pre>if a &lt; b:\n    x = 1</pre>") == "```\nif a < b:\n    x = 1\n```\n"


def test_rule_line_does_not_stop_at_an_abbreviation(tmp_path):
    p = tmp_path / "x.md"
    p.write_text("---\nid: x\n---\n**Rule.** Read config once, e.g. through decouple. More.\n")
    assert rule_line(p) == "Read config once, e.g. through decouple."
    p.write_text("---\nid: x\n---\n**Rule.** Name it.\n\nWhy.\n")
    assert rule_line(p) == "Name it."


def test_course_slug_folds_accents_and_resolves_back():
    assert course_id({"title": "Pacote de Desafios Pythônicos: à vontade!"}) == (
        "pacote-de-desafios-pythonicos-a-vontade"
    )
    assert course_id({"title": "C++ & Python (2024)"}) == "c-python-2024"
    for p in __import__("json").loads(
        (__import__("henriquefy.paths").paths.state_dir() / "playlists.json").read_text()
    )["playlists"]:
        assert playlist_entry(course_id(p))["id"] == p["id"]


def test_windows_on_empty_and_single_event():
    assert windows([]) == ""
    assert windows([(0, "oi")]) == "## window 1: 0:00:00 to 0:00:00\n\n[0:00:00] oi\n"


def test_fork_of_uses_the_recorded_source_before_the_name():
    eventex = "henriquebastos/eventex"
    assert fork_of({"repo": "someone/my-renamed-project", "source": eventex}) == eventex
    assert fork_of({"repo": "someone/eventex", "source": "HBNetwork/pds-api-client"}) is None
    assert fork_of({"repo": "someone/eventex-wttd"}) == eventex
    assert fork_of({"repo": "someone/pacote-de-receitas"}) is None
