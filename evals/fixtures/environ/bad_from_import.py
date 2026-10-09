from os import environ as env
from os import getenv

HOST = getenv("HOST")
PORT = env["PORT"]
env["SEEN"] = "1"
