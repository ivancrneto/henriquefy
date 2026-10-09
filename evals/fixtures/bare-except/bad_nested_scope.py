def load(path):
    try:
        return open(path).read()
    except Exception:

        def later():
            raise RuntimeError(path)

        return later
