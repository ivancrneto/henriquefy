---
title: Tooling drift, 2012 to 2026
class: his
kind: drift
span: 2012 to 2026
old:
  - {repo: henriquebastos/django-aggregate-if, commit: 588c1487bc88a8996d4ee9c2c9d50fa4a4484872, files_dated: 2013 to 2014}
  - {repo: henriquebastos/sqlformatter, commit: c36c66a4c720dfde37343d300ae731285c5600ad, files_dated: 2014 to 2020}
  - {repo: henriquebastos/django-test-without-migrations, commit: b665a0d203cb615a1a923caf06cff298bf73707e, files_dated: 2014 to 2017}
  - {repo: henriquebastos/eventex, commit: 26b0ba5b7fc5dfdd2e9cdf52c3317b6b65978ec0, files_dated: 2020}
  - {repo: henriquebastos/pacote-desafios-pythonicos, commit: ae90952cdaa7690a31e62f4715f0bd60600213b3, files_dated: 2020}
new:
  - {repo: henriquebastos/hamsterdan, commit: 5d382467eaa4ff837cbd6b93012c99081e0153f9, files_dated: 2026}
  - {repo: henriquebastos/beans, commit: ddfa931815bc580eeae39e7bcef1cceab204d2eb, files_dated: 2026}
  - {repo: henriquebastos/jira-genie, commit: 405a8f4042e8fbb2780ce1c2ee0048c47ff03af7, files_dated: 2026}
---
# Tooling drift, 2012 to 2026

What changed in how Henrique packages, configures, tests, lints, ships and documents a Python
project between the Django-era libraries and the 2026 agent-era repositories, and what did
not. Every cell names a repo, a path and the year the file was written at the cited commit.
Dates are of files, not of repositories: `eventex` was created in 2015 but its Python at the
manifest commit was regenerated on Django 3.1.2 in 2020; `django-aggregate-if` was created in
2012 but the earliest file reachable in the shallow clone is from 2013 and the tooling files
are from 2014. The 2026 clones (`hamsterdan`, `beans`, `jira-genie`) are read here for
contrast only; their own digests are `kb/repos/hamsterdan.md`, `kb/repos/beans.md` and
`kb/repos/jira-genie.md`, which agree on the settings point below ("Neither `python-decouple`
nor `pydantic-settings` is used.", `kb/repos/beans.md:146`, `kb/repos/jira-genie.md:133`).

The era policy applies to this file and nowhere else in the digests: packaging, dependency
management, settings, CI, lint and Python version are the concerns where "old form" and "new
form" differ. Modeling, naming, error handling and the shape of a test are listed under
Timeless because the 2014 and 2026 files agree on them.

## One row per concern

| Concern | Old form (repo, path, year) | New form (repo, path, year) | What moved |
|---|---|---|---|
| Packaging | `setup.py` with setuptools, version as a string literal, `py_modules`, `long_description=open("README.rst")`: django-aggregate-if `setup.py:6-33` (2014); sqlformatter `setup.py:9-29` (2014, bumped 2020); django-test-without-migrations `setup.py:6-34` plus `setup.cfg:1-2` universal wheel and `build.sh:4-6` running `python setup.py sdist bdist_wheel` (2015). eventex and pacote-desafios-pythonicos were never packaged. | `pyproject.toml` (PEP 621) with a `src/` layout and `[project.scripts]`: beans `pyproject.toml:1-24` with `uv_build` (`:16-21`, 2026); jira-genie `pyproject.toml:1-28` with `setuptools.build_meta` and `packages.find where = ["src"]` (`:20-25`, 2026); hamsterdan `pyproject.toml:38-49` with hatchling and `only-include = ["src/hamsterdan"]` (2026). `uv build` in release (beans `.github/workflows/release.yml:54`). | The backend is still whatever is least in the way (three backends across three 2026 repos). Metadata moved from Python to TOML; the layout moved to `src/`. |
| Dependency management | Exact pins in `requirements.txt` for an app: eventex `requirements.txt:1-12` (2020); exact pins turned into `install_requires` for a library: sqlformatter `setup.py:19` reading `requirements.txt:1-2` (`Pygments==1.6`, `sqlparse==0.3.1`, 2020); build tools mixed into the pin file: django-test-without-migrations `requirements.txt:1-5` (Django, nose, tox, wheel, 2015); or no file at all, deps per tox env: django-aggregate-if commit `779945e` "Remove requirements.txt" and `tox.ini:36-37` (2014). | Ranged runtime deps and a `[dependency-groups] dev` table: hamsterdan `pyproject.toml:12-36` (`fastapi>=0.116,<1`, 2026); beans `pyproject.toml:11-14, 26-33`; jira-genie `pyproject.toml:11-15, 30-37`. A committed `uv.lock` in all three; `uv sync --frozen` in CI (hamsterdan `.github/workflows/ci.yml:20`); `uv.toml:2` `exclude-newer` for reproducible resolution; a git dependency pinned by full sha (hamsterdan `pyproject.toml:16`). Exact pins survive only where he wants them: `githubkit[auth-app]==0.16.0`, `mutmut==3.6.0`, `ty==0.0.63` (hamsterdan `pyproject.toml:16, 29, 35`). | Pins moved from the declaration to the lock file. Runtime and development dependencies are separated by table, not by file name. |
| Settings and secrets | python-decouple with casts and a `.env`: eventex `eventex/settings.py:15, 26-31, 84-87, 130-135` (2020), `contrib/env-sample:1-9`, `.gitignore:2`, `README.md:36-46` with `heroku config:set`, `contrib/secret_gen.py:8-9`. A library reads one Django setting with a default at import: django-test-without-migrations `_base.py:12-15` (2015). Test settings hardcode `SECRET_KEY='secret'`: django-aggregate-if `tests/test_sqlite.py:16` (2014). | No 2026 clone depends on python-decouple. `os.environ.get` with a default, at the CLI layer: jira-genie `src/jira_genie/cli.py:244-245`, `config.py:28` (2026); the environment passed in as a parameter so tests inject a dict: hamsterdan `src/hamsterdan/host/service.py:65-66`, beans `src/beans/workspace.py:23, 60` (`env=os.environ` as a default argument). Secrets never in files: hamsterdan `scripts/with-runtime-secrets:34-35` wraps the process in `op run --environment`, `env-ops.tpl:1-3` holds `op://` references, `deployment/config/runtime.env:1-5` holds only non-secret settings. The rule is written down: "Defaults and configuration values (API keys, base URLs, feature flags) belong in the CLI layer, not in library modules." (jira-genie `docs/conventions.md:9-12`). | The rule (config outside code, read once, with a default) held. The tool changed: from a library that reads `.env` to plain `os.environ` injected through a parameter, and a secrets manager for production. |
| Test runner and layout | Django's runner through `manage.py test`: eventex `README.md:23`, `.travis.yml:9` (2020), with a `tests/` package per app and one module per unit (`eventex/core/tests/test_model_contact.py`, `test_view_home.py`). Libraries: a hand-written `runtests.py` plus a throwaway test app: django-aggregate-if `runtests.py:24-44`, `tests/aggregation/` (2014); django-test-without-migrations `runtests.py:19-37` via subprocess, `tests/myapp/` (2015), nose as the second runner (`tests/nose_settings.py:25`). sqlformatter: no tests (2014 to 2020). pacote: a print-based checker in each file (`01_donuts.py:19-33`, 2020). | pytest, configured in `pyproject.toml`: beans `:35-37` (coverage in `addopts`), jira-genie `:39-41`, hamsterdan `:51-58` (fixed `--randomly-seed=1729`, `timeout = 30`, markers). `tests/` at the repo root mirroring `src/` module by module (beans `tests/test_models.py` for `src/beans/models.py`), or split into `tests/unit` and `tests/integration` (hamsterdan). Plain `assert` on whole models (beans `tests/test_models.py:18-35`), `responses` for HTTP instead of mocking sessions (jira-genie `docs/testing.md:8-16`), hypothesis in dev deps (beans `pyproject.toml:28`), a conftest that fails the session on any skip (hamsterdan `conftest.py:9-14`, `scripts/check:76`). tox survives only as a multi-Python matrix over uv (beans `tox.ini:1-11`). | From the framework's runner to pytest; from a test app inside `tests/` to one test module per source module; from `assertEqual` to bare `assert` on equality of whole objects. |
| Lint and format | No linter, formatter or type checker in any repo. The only signal is a landscape.io badge: django-aggregate-if `README.rst:8-10` (2014), django-test-without-migrations `README.rst:8-10` (2014). Indentation drifts inside one project: eventex `eventex/subscriptions/admin.py:7-31` (tabs) against `eventex/core/admin.py` (spaces) (2020). `# coding: utf-8` headers: sqlformatter `sqlformatter.py:1` (2014). | ruff with an explicit rule set in `pyproject.toml`: beans `:39-47` (`E,F,I,N,UP,RUF`, isort config), jira-genie `:43-51`, hamsterdan `:68-73` (mccabe max 10). `ruff format --check` and `ty check` in the gate: hamsterdan `scripts/check:52-54`; ast-grep structural rules (`scripts/check:68-69`, `sgconfig.yml`). CI runs `ruff check src/ tests/` before tests (beans `.github/workflows/ci.yml:25`). | From nothing to lint, format and type checks in one script that humans, agents and CI all call (hamsterdan `scripts/check:2`, "One deterministic feedback interface for agents and humans."). |
| CI | Travis: django-aggregate-if `.travis.yml:1-50` (matrix of `DJANGO` and `DB` env vars with database services and eight excludes, 2014); django-test-without-migrations `.travis.yml:1-8` delegating to tox via tox-travis (2015); eventex `.travis.yml:1-9` (copy env-sample, makemigrations, test, 2020). First GitHub Actions file, publish only: sqlformatter `.github/workflows/main.yml:3-17` on `v*` tags, `pypa/gh-action-pypi-publish@master`, a token in `secrets.pypi` (2020). | GitHub Actions `ci.yml` on push and pull request with a Python matrix over uv: beans `.github/workflows/ci.yml:16-26` (3.12 to 3.14), jira-genie `ci.yml:17-25` (3.11 to 3.14); hamsterdan `ci.yml:12-21` runs `scripts/check tests`. A `release.yml` on published release: reuses `ci.yml` by `workflow_call`, generates the changelog with git-cliff, `uv build`, trusted publishing with `id-token: write` and `pypa/gh-action-pypi-publish@release/v1`, then bumps the Homebrew formula (beans `release.yml:11-74`, same in jira-genie). | Travis to Actions; a password secret to OIDC trusted publishing; a bare publish step to a release pipeline that tests first and writes the changelog. |
| Python version floor | 2.7 and 3.4: django-aggregate-if `tox.ini:3-25`, `setup.py:27-28`, `six` and `from __future__ import unicode_literals` in `aggregate_if.py:12-13` (2014). 2.7 and 3.6: django-test-without-migrations `tox.ini:2` (2017). 3.6 by deployment file: eventex `runtime.txt:1` (`python-3.6.1`, 2020). 3.6 by syntax only: pacote `01_donuts.py:31` f-strings (2020). | `requires-python` in `pyproject.toml`: jira-genie `:10` (`>=3.11`), beans `:10` (`>=3.12`), hamsterdan `:8` (`>=3.14`). A `.python-version` per repo (hamsterdan `.python-version:1` = `3.14.7`, beans = `3.14`, jira-genie = `3.13`). The CI matrix is the supported range (jira-genie `ci.yml:18`). `ruff target-version = "py314"` (hamsterdan `pyproject.toml:70`). | From two majors and `six` to the newest release at the time, floor declared in metadata and enforced by the matrix. |
| Type hints | None. 0 of 128 `def`s in eventex, 0 of 47 in `aggregate_if.py`, 0 of 6 in `sqlformatter.py` carry an annotation (grep at the manifest commits); sample: eventex `eventex/core/managers.py:5-19` (2020). | A written rule: "Annotate return types. Don't annotate parameters when the default value tells the story." (beans `AGENTS.md:122-124`, 2026). Counts at the manifest commits: hamsterdan `src/` 838 of 1177 `def`s with a return annotation, beans `src/` 86 of 140, jira-genie `src/` 7 of 102. A type checker in the gate for one of the three (hamsterdan `scripts/check:54`, `ty`); `TypedDict` at seams (hamsterdan `docs/process/engineering-conventions.md:308-321`). | From none to returns-first annotations. Uneven: the oldest 2026 repo (jira-genie, created March) is nearly unannotated; the one with a checker is fully annotated. |
| Docs and README | README.rst with a badge block, a one-line definition, the problem, Installation, Usage, Inspiration, Author or Contributors, a Changelog section inside the README, License: django-aggregate-if `README.rst:1-157` (2014), django-test-without-migrations `README.rst:1-105` (2017), sqlformatter `README.rst:1-117` with the MIT text pasted (2020). A Portuguese README.md that is an operations card: eventex `README.md:1-49` (2020). No README: pacote (2020). | README.md with a banner image, a one-line pitch and a quick start: jira-genie `README.md:1-15`, beans `README.md:1-12`. A separate `CHANGELOG.md` generated by git-cliff (beans `cliff.toml`, `release.yml:40-52`). `AGENTS.md` as the contract for AI coding agents (beans `AGENTS.md`, jira-genie `AGENTS.md`, hamsterdan `AGENTS.md:1-60`). A `docs/` tree with conventions, testing and tooling written out (jira-genie `docs/conventions.md`, `docs/testing.md`, `docs/tooling.md`) or a full Ariad process tree (hamsterdan `docs/process/engineering-conventions.md`, 19.6K). `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` (hamsterdan). | The README stopped carrying the changelog and the license text. The conventions he used to apply silently are now files an agent reads first. |

## What did not change

The 2026 repos still open the README with the problem, still keep dependencies to a handful,
still name a test after the behavior it asserts and put the action in a setup step, still read
configuration in one place with a default, still comment the why and not the what, and still
build composition out of small parts instead of class trees. The list below pairs one old and
one new citation per practice.

## Timeless

- Problem-first README opener. django-aggregate-if `README.rst:20-23` (2014): "*Aggregate-if*
  adds conditional aggregates to Django. Conditional aggregates can help you reduce the ammount
  of queries". jira-genie `README.md:7-11` (2026): "Your AI agent's interface to Jira Cloud.
  JSON in, JSON out." followed by what the agent gets.
- Configuration read in one place, with a declared default, never a secret in the repo.
  eventex `eventex/settings.py:26-31` (2020). jira-genie `src/jira_genie/cli.py:244-245` and
  `docs/conventions.md:9-12` (2026).
- One test module per unit, named after it. eventex `eventex/core/tests/test_model_speaker.py`
  (2020). beans `tests/test_models.py` for `src/beans/models.py` (2026).
- A scenario class with a one-line docstring, a `setUp` that performs the action, and short
  methods that each assert one consequence. eventex
  `eventex/subscriptions/tests/test_view_new.py:8-18` (2020). hamsterdan
  `docs/process/engineering-conventions.md:269-270` (2026): "Test classes are scenarios with a
  one-line contract docstring; methods are tiny behavior sentences"; beans
  `tests/test_models.py:15-16`.
- Tests go through the public surface. eventex `test_form_subscription.py:53-59` builds the
  form the user would (2020). jira-genie `docs/conventions.md:24-27` (2026): "Test through the
  public-facing functions; helpers get coverage indirectly."
- Known data, not random data, in tests. django-aggregate-if `tests/aggregation/tests.py:23`
  fixture (2014); eventex `test_view_home.py:6` (2020). beans `tests/test_models.py:12`
  `FIXED_TIME` and hamsterdan `pyproject.toml:52` fixed seed (2026).
- Composition over a fixed base class. django-test-without-migrations `_base.py:12-15, 41` and
  `test.py:4` (2015): a mixin over whichever command the settings name. jira-genie
  `docs/conventions.md:29-31` (2026): "Compose small functions rather than building class
  hierarchies."
- Comments explain why, never what. django-test-without-migrations `runtests.py:19-21` (2015):
  "We need to use subprocess.call ... because we can only setup django's settings once".
  hamsterdan `scripts/check:81-84` (2026): why workers are capped at four.
- Few dependencies, named by what they do. django-aggregate-if `setup.py:13-15` (`six` only,
  2014); django-test-without-migrations `setup.py:17` (none, 2015). beans `pyproject.toml:11-14`
  (`pydantic`, `typer`, 2026); jira-genie `pyproject.toml:11-15` (three).
- Options forwarded under the names of the library that owns them, no option schema.
  sqlformatter `sqlformatter.py:13-18` (2014). beans `src/beans/workspace.py:23, 60` default
  arguments carry the configuration (2026); jira-genie `docs/conventions.md:48-50`.
- Author line unchanged. django-aggregate-if `setup.py:10` (2014) and beans
  `pyproject.toml:7-9` (2026): "Henrique Bastos", `henrique@bastos.net`.

## Era tags to set

Only tooling entries carry an era (`skills/henrique-ingest/prompts/distill-repo.md:56-57`;
`PLAN.md`, era policy of 2026-10-08). Checked against every file under `kb/principles/` and
`kb/patterns/` at the time of writing.

- `kb/principles/configuracao-fora-do-codigo.md`: keep `era: 2020s`. Its sources are the API
  course and the python-decouple README, and its "Looks like" is decouple-specific. Two facts
  for whoever revisits it: the shape first appears in his code in 2015 to 2020 (eventex
  `settings.py:26-31`) and in 2015 as a Django setting with a default
  (django-test-without-migrations `_base.py:12-15`); and none of the three 2026 clones depends
  on python-decouple, all read `os.environ` and inject it through a parameter (row "Settings
  and secrets"). The mechanical rule `project.environ-without-decouple` fires only when the
  project already depends on decouple (`kb/check-rules.md`), so the 2026 repos are not flagged.
  The rule stays dated to the tool, not to the practice; a future amendment could add the
  2026 form to "Looks like" without changing the era.
- `kb/patterns/configuracao-com-decouple.md` (new, untracked at the time of writing): set
  `era: 2020s`. It is the only pattern file whose subject is a tool. Its `python` rendition is
  python-decouple's own README at commit `0573e6f96637f08fb4cb85e0552f0622d36827d4`, the same
  source as the principle, and the 2026 repos do not use the tool (row "Settings and secrets").
  The pattern template has no `era` key, so adding one is a template decision as much as a
  file edit; the principle it serves already carries `2020s`, which is the value to mirror.
- No other existing principle or pattern should carry an era. The thirteen other pattern files
  (`camada-de-servico-django`, `cliente-de-api-profissional`, `colecao-como-entidade`,
  `coordenador-sem-regra-de-negocio`, `estrategia-por-composicao`, `excecao-para-http`,
  `excecoes-de-dominio-tratadas-pelo-nome`, `links-por-estado`, `mediador-sem-ciclos`,
  `mensagens-que-leem-como-frases`, `serializacao-de-tipos`, `status-com-httpstatus`,
  `verbo-por-rota`) and the other twenty principles are about modeling, errors, testing, API
  shape and readability, which this file shows unchanged from 2014 to 2026; `era: timeless` is
  correct on all of them.
- Eras for tooling entries that these digests would justify writing, should someone write
  them (none exist yet): `setup.py` plus `tox` plus `runtests.py` as the library test harness,
  `era: 2010s` (django-aggregate-if 2014, django-test-without-migrations 2015);
  `requirements.txt` with exact pins for an application, `era: 2010s` (eventex 2020 is the
  last instance); Travis matrix as CI, `era: 2010s`; GitHub Actions publish-only on tags,
  `era: 2020s` (sqlformatter 2020); python-decouple settings module, `era: 2020s` to match
  the principle; `pyproject.toml` with `uv.lock`, ruff, pytest in `pyproject`, release via
  trusted publishing and git-cliff, `era: 2026` (beans, jira-genie, hamsterdan).
