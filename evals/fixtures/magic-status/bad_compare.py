def renew_if_needed(response):
    if response.status_code != 401:
        return response
    return None


def test_ok(response):
    assert response.status_code == 200
