def outer(table, key):
    try:
        try:
            return table[key]
        except KeyError:
            return None
    except TypeError:
        return False
