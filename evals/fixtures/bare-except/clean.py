import logging


def load(path):
    try:
        return open(path).read()
    except FileNotFoundError:
        return ""


def parse(text):
    try:
        return int(text)
    except Exception:
        logging.exception("parse failed")
        raise
