def test_total_uses_a_local_helper():
    def test_helper(items):
        return sum(items)

    assert test_helper([1, 2]) == 3
