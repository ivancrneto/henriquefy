def save(record):
    try:
        record.save()
    except ValueError:
        return
    return record
