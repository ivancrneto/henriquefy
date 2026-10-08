def add(item, items=None):
    items = [] if items is None else items
    items.append(item)
    return items


def configure(options=None, *, tags=()):
    return options or {}, tags
