def add(item, items=[]):
    items.append(item)
    return items


def configure(options={}, *, tags=set()):
    return options, tags
