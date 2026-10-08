def load(path):
    try:
        return open(path).read()
    except:
        return ""


def parse(text):
    try:
        return int(text)
    except Exception:
        return 0
