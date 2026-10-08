from henriquefy.paths import kb_dir, skills_dir, state_dir


def test_data_dirs_resolve():
    assert (kb_dir() / "LICENSE").is_file()
    assert (skills_dir() / "henriquefy" / "SKILL.md").is_file()
    assert (state_dir() / "playlists.json").is_file()
