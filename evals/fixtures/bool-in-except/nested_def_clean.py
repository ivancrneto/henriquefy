def retrying(call):
    try:
        return call()
    except ConnectionError as exc:

        def fallback():
            return None

        raise RuntimeError(fallback) from exc
