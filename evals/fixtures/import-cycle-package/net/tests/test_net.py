from net import build


def test_build_lists_every_loop():
    assert build() == ["ci", "review"]
