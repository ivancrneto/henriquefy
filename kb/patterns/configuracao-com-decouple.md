---
id: configuracao-com-decouple
title: Settings read once through decouple
principle: configuracao-fora-do-codigo
category: project
era: 2020s
frameworks:
  python: {origin: his, repo: HBNetwork/python-decouple, path: README.rst, commit: 0573e6f96637f08fb4cb85e0552f0622d36827d4}
---
**What.** One settings module imports `config` from `decouple` and declares every external
value once: its name, a `cast` to the type the code expects, and a `default` when the value is
optional. The value comes from the environment first, then from a `.env` or `settings.ini`
found next to the project, then from the default; a required key with no value raises
`UndefinedValueError` when the settings module is imported. The rest of the code imports the
settings module and never reads `os.environ`. It applies to any project with a secret, a
hostname or a flag that changes per deploy, in Django and in FastAPI alike.

## python
From `python-decouple` (MIT), `README.rst` at commit `0573e6f96637f08fb4cb85e0552f0622d36827d4`,
lines 81 and 87 to 90 (rst indentation removed), the canonical `settings.py`:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
```

The `.env` that feeds it, lines 150 to 155, created "in your repository's root directory"
(line 146) and never committed:

```
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
PERCENTILE=90%
#COMMENTED=42
```

The search order, lines 231 to 235: "Decouple always searches for Options in this order: 1.
Environment variables; 2. Repository: ini or .env file; 3. Default argument passed to config."
The code is `Config.get`, `decouple.py` lines 80 to 101 at the same commit: `os.environ`
first, the repository second, the default third, then `cast(value)`.

What to notice. `SECRET_KEY` has no default on purpose: "If SECRET_KEY is not present in the
.env, decouple will raise an UndefinedValueError. This fail fast policy helps you avoid chasing
misbehaviours when you eventually forget a parameter." (lines 208 to 210). `cast=bool` exists
because `os.environ['DEBUG']` is the string `"False"`, which is truthy (lines 48 to 62).
`cast` is any callable: `Csv()` turns `ALLOWED_HOSTS` into a list (lines 319 to 322) and
`dj_database_url.parse` turns a URL into the `DATABASES` entry (lines 179 to 185). A value is
overridden per run without touching a file: `DEBUG=True python manage.py` (line 225).

## Bad
```python
# views.py
import os
def send(request):
    host = os.environ.get("EMAIL_HOST", "localhost")
    port = int(os.environ["EMAIL_PORT"])          # KeyError on the first request, not at startup
    if os.getenv("DEBUG") == "True": ...          # "true" and "1" are not debug here

# client.py
API_TOKEN = "sk_live_51H..."                     # committed, and the same in every deploy
```

Each module decides name, type and default of the same setting again; a missing key fails on
the first request instead of at import; the secret is in the history for good. Rule
`project.environ-without-decouple` catches the first module in a project that depends on decouple.
