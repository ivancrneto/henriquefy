from decouple import config

TOKEN = config("API_TOKEN")
DEBUG = config("DEBUG", cast=bool, default=False)
