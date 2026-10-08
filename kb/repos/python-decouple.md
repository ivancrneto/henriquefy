---
repo: HBNetwork/python-decouple
commit: 0573e6f96637f08fb4cb85e0552f0622d36827d4
era: 2014 to 2024
license: MIT
class: his
---
# python-decouple

**What it is.** A single-module library, `decouple.py` (317 lines), that reads a setting by
name from the environment, then from a `.env` or `settings.ini` found next to the caller, then
from a default, and casts it with any callable. Version 3.8 (`setup.py` line 9). His most used
project, about three thousand stars, the base of every API client example in Design de API
(API digest section 14.1). The GitHub repository dates from 2014-02-25 and now lives in the
HBNetwork organization; the clone is shallow, 111 commits since 2017, 71 of them his; the
commit at hand is a README merge from 2024-01-01 ("Merge pull request #157"), the last push
2024-11-28. "It was originally designed for Django, but became an independent generic tool for
separating settings from code." (`README.rst` lines 15 to 16). The code still runs on Python 2.

**Layout.**

```
decouple.py       strtobool (29 to 43); UndefinedValueError and the Undefined sentinel (46 to 58);
                  Config (61 to 107); RepositoryEmpty, RepositoryIni, RepositoryEnv,
                  RepositorySecret (110 to 188); AutoConfig (191 to 248); the module-level
                  config instance (251 to 253); Csv and Choices helpers (257 to 316)
tests/
  test_env.py, test_ini.py        a Config over an in-memory file, one test per parsing rule
  test_autoconfig.py              file discovery, with real fixture dirs under tests/autoconfig/
  test_secrets.py                 Docker-style secrets dir, fixtures under tests/secrets/
  test_helper_csv.py, test_helper_choices.py, test_strtobool.py
README.rst, CHANGELOG.md, setup.py, setup.cfg, MANIFEST.in, requirements.txt, tox.ini,
.travis.yml, .editorconfig, .github/workflows/{main,python-publish}.yml
```

**How he tests.** pytest with the `mock` backport (`from mock import patch`,
`tests/test_env.py` line 4) under tox `py2, py3` (`tox.ini` lines 1 to 8). A module-scoped
`config` fixture patches `decouple.open` to return a `StringIO` holding an inline `.env`
(`tests/test_env.py` lines 18 to 57) or `.ini` (`tests/test_ini.py` lines 18 to 43); then one
test per rule, named after the rule: `test_env_comment`, `test_env_percent_not_escaped`,
`test_env_no_interpolation`, `test_env_bool_true`, `test_env_undefined`,
`test_env_empty_string_means_false` (`tests/test_env.py` lines 60 to 124), each mirrored for
ini. Discovery is tested against real files, `tests/autoconfig/env/.env` and
`tests/autoconfig/ini/project/settings.ini`, with `_caller_path` patched
(`tests/test_autoconfig.py` lines 8 to 19). Precedence of the environment is tested by
setting `os.environ` inline and deleting it after (`tests/test_env.py` lines 91 to 94;
`tests/test_secrets.py` lines 25 to 31). `parametrize` arrives in 2022 for `strtobool`
(`tests/test_strtobool.py` lines 5 to 12; his commit `f802447` "Parametrize tests"). A
regression test explains its bug in the docstring (`tests/test_autoconfig.py` lines 22 to 38).
Not tested: `_caller_path` itself, which is always patched.

**How he handles errors.** `UndefinedValueError(Exception)` (`decouple.py` lines 46 to 47) is
raised by `Config.get` when a key is in neither the environment nor the repository and has no
default (lines 90 to 92), with the message "{} not found. Declare it as envvar or define a
default value." The `Undefined` class and its instance `undefined` (lines 50 to 58) tell "no
default given" from `default=None`. Repositories raise `KeyError` for a missing key (lines
140, 166, 188; `d596515`, 2023). `strtobool` raises `ValueError("Invalid truth value: ...")`
(line 43) and `Choices` raises `ValueError` listing the valid values (lines 312 to 315).
`AutoConfig._load` wraps the file search in `except Exception` to "Avoid unintended
permission errors" and falls back to `RepositoryEmpty` (lines 229 to 236). The README states
the policy: "This fail fast policy helps you avoid chasing misbehaviours when you eventually
forget a parameter." (`README.rst` line 210).

**Naming and interface.** `Config` "Coordinates all the configuration retrieval"
(`README.rst` lines 240 to 242); `Repository*` classes share `__contains__` and `__getitem__`
and are a few lines each (`decouple.py` lines 110 to 188); `AutoConfig` is "a lazy `Config`
factory that detects which configuration repository you're using" (`README.rst` lines 256 to
258), driven by the `SUPPORTED` ordered dict from file name to class (`decouple.py` lines 202
to 205). The public entry point is a module-level instance, with the comment "A
pré-instantiated AutoConfig to improve decouple's usability / now just import config and
start using with no configuration." (lines 251 to 253). `cast` takes any callable (lines 80,
96 to 101), and the helpers `Csv` and `Choices` are callable classes (lines 257 to 316).
Private methods carry an underscore: `_cast_boolean`, `_cast_do_nothing`, `_find_file`,
`_load`, `_caller_path`, the last one with "# MAGIC! Get the caller's module path." (line
240). The surface the README teaches: `config`, `Config`, `RepositoryEnv`, `RepositoryIni`,
`Csv`, `Choices`, `UndefinedValueError`.

**Packaging, config, tooling.** 2014 to 2024, with the tooling frozen between 2017 and 2022.
`setup.py` with `py_modules=['decouple']` and `version='3.8'` (lines 8 to 14), no
`pyproject.toml`; `setup.cfg` holds only `license-file`; `MANIFEST.in` includes LICENSE.
`requirements.txt` pins `mock==2.0.0`, `pytest==3.2.0`, `tox==2.7.0`, `docutils==0.14`,
`Pygments>=2.7.4` and `twine` (lines 1 to 6). `.travis.yml` for 2.7 and 3.6 and its badge
(`README.rst` lines 18 to 20) are dead; the live CI is a GitHub Action running tox inside
`python:3.10-alpine` and `python:2.7-alpine` containers (`.github/workflows/main.yml` lines 23
to 59; the 3.10 job is his `4f16fbe`, 2022-02-02). Publishing runs `python setup.py sdist
bdist_wheel` and twine with `PYPI_USERNAME` and `PYPI_PASSWORD` secrets
(`.github/workflows/python-publish.yml` lines 26 to 31, 2021). Python 2 shims at the top of the
module: `ConfigParser` versus `SafeConfigParser`, `text_type = unicode`, `readfp`
(`decouple.py` lines 13 to 23); `# coding: utf-8` on every file. `.editorconfig` with 4-space
indent (lines 5 to 10). No lint, no formatter. The contributor setup is venv, pip and tox, and
"Decouple supports both Python 2.7 and 3.6. Make sure you have both installed."
(`README.rst` lines 470 to 479).

**README voice.** Title: "Python Decouple: Strict separation of settings from code"
(`README.rst` line 2). First sentence: "Decouple helps you to organize your settings so that
you can change parameters without having to redeploy your app." (lines 5 to 6), then four
numbered things it makes easy (lines 10 to 13). "Why?" splits a settings file into project
settings and instance settings: "You should be able to change instance settings without
redeploying your app." (lines 29 to 42). "Why not just use environment variables?" shows the
`DEBUG=False` gotcha and answers "Decouple provides a solution that doesn't look like a
workaround: `config('DEBUG', cast=bool)`." (lines 45 to 62). Usage is two numbered steps
(lines 77 to 90), then a full Django `settings.py` (lines 158 to 199), the fail-fast note
(lines 202 to 210), "Since version 3.0, decouple respects the unix way." (line 218), a "How
does it work?" naming the four classes (lines 228 to 267), the `cast` section with the four
Django examples (lines 270 to 305), and a five-question FAQ added in 2023 (lines 398 to 460).
Closing: "You can submit pull requests and issues for discussion. However I only consider
merging tested code." (lines 486 to 487).

**What this repo adds to the KB.**
- configuracao-fora-do-codigo: `README.rst` 81 and 87 to 90, `decouple.py` 80 to 101; pattern
  configuracao-com-decouple (written in this pass).
- prefira-excecoes-a-booleanos: a missing key raises `UndefinedValueError` instead of
  returning `None` (`decouple.py` 90 to 92); the `Undefined` sentinel (50 to 58).
- escolha-a-regra-mais-simples: `cast` is any callable, and `bool` is the one special case
  because `bool("False")` is `True` (`decouple.py` 96 to 101; `README.rst` 283 to 285).
- componha-em-vez-de-herdar: `Config(repository)` (`decouple.py` 66 to 67); `Csv(cast=...,
  post_process=...)` built from callables (262 to 287); repositories combined with `ChainMap`
  in FAQ 5 (`README.rst` 454 to 460).
- a-interface-e-o-que-importa: `from decouple import config` then `config('KEY')`, nothing to
  configure first (`decouple.py` 251 to 253).
- nao-projete-a-generalizacao: `RepositorySecret` for Docker secrets arrived in 3.6 and
  `Choices` in 3.4 (`CHANGELOG.md` 9 to 12 and 26 to 29), each as a few lines in the same module.

**Caveats.**
- `except Exception` without re-raise in `AutoConfig._load` (`decouple.py` lines 230 to 233):
  a permission error on a config file becomes "no config file" silently. Rule
  `errors.bare-except` fires.
- The environment-first rule is implemented twice: in `Config.get` (lines 86 to 87) and again
  in every repository's `__contains__` (lines 133 to 134, 163, 185), so `RepositoryEmpty` and
  `RepositoryEnv` answer differently for a key that exists only in the environment. The README
  documents the duplication (lines 244 to 254) rather than removing it.
- `_caller_path` reads `sys._getframe()` two frames up (lines 238 to 242); the comment says
  "MAGIC!" and the tests always patch it.
- Tests change process state without teardown: `os.environ` set and deleted inline in seven
  places, `os.chdir(subdir)` never restored (`tests/test_autoconfig.py` line 35);
  `test_autoconfig_none` and `test_autoconfig_is_not_a_file` are the same test (lines 41 to
  47 and 58 to 63).
- Python 2 code paths, a `py2` tox env and a `python:2.7-alpine` CI job in a 2024 codebase
  (`decouple.py` 13 to 23; `main.yml` 42 to 59); `pytest==3.2.0` and `mock==2.0.0` pinned since
  2017 (`requirements.txt` 1 to 2).
- Releases upload with a username and password (`python-publish.yml` 27 to 28); his 2025 and
  2026 repos use trusted publishing.
- Version 3.8 (`setup.py` line 9, `860969c` 2023-03-01) has no CHANGELOG entry; the changelog
  stops at 3.7 (`CHANGELOG.md` lines 4 to 7).
- `Config.get` casts the default too (`value = default` at line 94, `cast(value)` at 101), so
  `config('X', default=None, cast=int)` raises `TypeError`; only the `bool` case is tested
  (`tests/test_ini.py` lines 87 to 99).
- No `__all__`, no lint, no formatter; the module mixes a Portuguese accent into an English
  comment (`decouple.py` line 251).
