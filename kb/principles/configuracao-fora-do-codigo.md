---
id: configuracao-fora-do-codigo
title: Configuração fora do código
category: project
weight: 2
detectable: partial
era: 2020s
scope: project
sources:
  - type: course
    course: design-api-na-pratica
    lesson: null
    section: "14.1"
    timestamp: null
  - type: course
    course: design-api-na-pratica
    lesson: 7
    section: "5"
    timestamp: null
  - type: repo
    class: his
    repo: HBNetwork/python-decouple
    path: README.rst
    commit: 0573e6f96637f08fb4cb85e0552f0622d36827d4
---
**Rule.** Settings and credentials live outside the code, read in one place with a declared
type and a default. His tool for it is `python-decouple`: `config("KEY", cast=int, default=...)`
instead of `os.environ` scattered through modules and secrets hardcoded in examples.

**Why Henrique says so.** The API digest lists `python-decouple` as the HB Network project
behind every API client example in the course: strict separation of configuration from code,
and API consumption without hardcoded credentials (digest section 14.1). The lesson 7 client
work, where a token and a base URL have to come from somewhere, is where the course leans on it
(digest section 5, lesson 7). This is a tooling principle, dated 2020s: the rule is timeless,
the library is his current answer to it.

**Looks like.** A `settings.py` or `config.py` with `from decouple import config` and every
external value declared once: `API_TOKEN = config("API_TOKEN")`,
`TIMEOUT = config("TIMEOUT", cast=int, default=30)`. Bad: `os.environ["API_TOKEN"]` inside a
request function, `os.getenv("DEBUG") == "True"` string comparisons, a token pasted into a demo.

**How to detect.** Partial. Mechanical, only in a project that already depends on
`python-decouple`: `os.environ`, `os.environ.get` or `os.getenv` anywhere in the code (rule
`project.environ-without-decouple`). Whether a project that does not use decouple should adopt
it is a judgment finding, and FastAPI projects commonly use pydantic-settings for the same job.

**How to fix.** Add `python-decouple`, create one module that reads every setting with `config`
and a cast, and replace each `os.environ` read with an import from that module. Keep secrets in
`.env` or the environment, never in the repository.
