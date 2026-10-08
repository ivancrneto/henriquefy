---
repo: henriquebastos/python-jsonstar
commit: 6fb683e8ca6aa53ce24d0c7de36b1b0bc7b62f75
era: 2024 to 2025
license: MIT
class: his
---
# python-jsonstar

**What it is.** `jsonstar`, a drop-in replacement for the standard `json` module whose encoder
serializes `Decimal`, `datetime`, `date`, `time`, `timedelta`, `UUID`, `set`, `frozenset`,
dataclasses, attrs classes, pydantic models and Django models through a registry of functions
keyed by type, extensible per encoder class or library-wide. Version 1.1.1 on PyPI
(`pyproject.toml` line 39), five modules of about 190 lines. The code was extracted from an
earlier project in 2022 (`4998137` "Extract json tools to a new jsonplus root", 2022-10-08) and
renamed from JSONPlus to JSONStar on 2024-02-06 (`9663225`); the GitHub repository dates from
the same day, the last push is 2025-03-01, 59 commits in the clone. It is the custom encoder
lesson 7 of Design de API arrives at after the `datetime` bug and the money debate (API digest
section 15.2), and `requests-pro` recommends it in the `ProSession` docstring.

**Layout.**

```
jsonstar/
  __init__.py           dump, dumps, load, loads with the star classes as defaults (7 to 20);
                        register_default_encoder (23 to 24)
  encoder.py            TypedEncoderRegistry (14 to 20); EncoderMeta (23 to 31); JSONEncoderStar
                        with register, register_default_encoder and default (34 to 93)
  default_encoders.py   optional django, pydantic and attrs encoders under try/except ImportError
                        (7 to 39); encode_timedelta_as_iso_string (42 to 50);
                        DEFAULT_FUNCTIONAL_ENCODERS (57 to 60); DEFAULT_TYPED_ENCODERS (62 to 73)
  decoder.py            JSONDecoderStar: an object_hook that turns ISO strings into datetime
  null_dict.py          NullDict and the NULL_DICT singleton, a read-only empty default argument
tests/
  test_default_encoder.py   one TestX class per default encoder
  test_encoder.py           precedence between typed, functional and default encoders
  test_register_defaults.py module API and isolation of defaults between subclasses
pyproject.toml (poetry), poetry.lock, lint.sh, .pre-commit-config.yaml,
.github/workflows/{push,lint,test,publish}.yml
```

**How he tests.** pytest 8 with freezegun, pytz, pydantic 2, attrs and Django 4.2 as dev
dependencies (`pyproject.toml` lines 65 to 77). One class per type, `TestDatetimeEncoder`,
`TestDateEncoder`, `TestDecimalEncoder` and so on (`tests/test_default_encoder.py` lines 18 to
189), a one-line `encode` helper (lines 14 to 15), `parametrize` over four timezones (lines 19
to 30), Django configured inside a class-scoped autouse fixture (lines 116 to 132). The
precedence tests carry the rule in their name:
`test_typed_encoders_have_precedence_over_functional_encoders` (`tests/test_encoder.py` lines
42 to 47), `test_encoder_for_inherited_type_has_precedence_over_encoder_for_base_type` with a
`Mother`, `Father`, `Child` diamond (lines 62 to 79). An autouse `monkeypatch` fixture empties
the class registries so no test leaks into another (lines 24 to 27); `Mock(side_effect=Exception)`
proves a functional encoder was not called (lines 99 to 105). Not tested: `dump`, `load`,
`loads` and `JSONDecoderStar` (no test imports the decoder). The three methods of
`TestTimeEncoder` lack the `test_` prefix (`tests/test_default_encoder.py` lines 41 to 49), so
pytest never collects them (`pyproject.toml` lines 79 to 80 set only `python_files`).

**How he handles errors.** No exception class. `default` tries typed encoders by `isinstance`,
then functional encoders, then `super().default(o)`, so the stdlib `TypeError` is the error for
an unknown type (`jsonstar/encoder.py` lines 84 to 93; `tests/test_encoder.py` lines 94 to
96). Functional encoders run under `with suppress(Exception)` (lines 89 to 91): any failure in
any of them is skipped silently and the next one is tried. The decoder hook catches
`(ValueError, TypeError)` from `fromisoformat` and keeps the string (`jsonstar/decoder.py`
lines 13 to 17). Optional dependencies are `try/except ImportError` with an empty registry as
the fallback (`jsonstar/default_encoders.py` lines 7 to 39).

**Naming and interface.** `JSONEncoderStar` and `JSONDecoderStar` carry the module's star;
`TypedEncoderRegistry` is an `OrderedDict` whose `__setitem__` moves base types to the end so a
subclass's encoder wins (`encoder.py` lines 14 to 20); `EncoderMeta` gives every subclass its
own registries (lines 23 to 31); `FUNCTIONAL` is a nested sentinel class with a docstring
(lines 35 to 36); `register` on the instance versus `register_default_encoder` on the class
(lines 71 to 82); `typed_encoders` is a `ChainMap` over instance and class defaults (lines 65
to 69). `NULL_DICT` is a singleton default argument (`null_dict.py` lines 6 to 27). `__all__`
is declared in `encoder.py` line 11 and `null_dict.py` line 1. The module functions mirror the
stdlib names so `import jsonstar as json` works (`__init__.py` lines 7 to 20). The documented
way to declare class encoders is the underscore attribute `_default_typed_encoders`
(`README.md` lines 98 to 100).

**Packaging, config, tooling.** 2025. Build backend `poetry-core` (`pyproject.toml` lines 1 to
3); a `[project]` table with only the name and URLs, added in 2025 (`e0484c0` "Add pyproject
name (#1)"), while version, description, license and classifiers live in `[tool.poetry]`
(lines 37 to 60); `python = ">=3.9"` (line 63); `poetry.lock` committed. black at line length
120 targeting py311 (lines 14 to 16), isort with the black profile (lines 27 to 35), flake8 at
120, all three as local pre-commit hooks (`entry: python -m black`, `language: system`,
`.pre-commit-config.yaml` lines 33 to 76) next to `poetry-check` and `poetry-lock` hooks
(lines 77 to 93). `lint.sh` is a zsh script that sources `$VENV_BIN/activate` and runs the three
hooks on the files given (lines 1 to 6). Push runs lint then test on 3.9 to 3.12
(`.github/workflows/test.yml` line 11; 3.13 excluded by `ae1d17c` "Exclude 3.13 to avoid
pydantic colision"); a release runs both and publishes with trusted publishing (`publish.yml`
lines 17 to 22, 36). His 2026 repos moved from this poetry, black and isort stack to uv and ruff.

**README voice.** "JSON* is an extensible json module to serialize all objects!" (`README.md`
line 1). Every heading is a question: "How to install it?", "How to start using it?", "Why use
it?", "What default encoders are provided?", "How do I add my own encoder?" (lines 7, 13, 19,
55, 76). The promise: "Simply change your import from `import json` to `import jsonstar as
json` and you're good to go." (line 17). The motivating example is a pydantic `Employee` with a
`Decimal` salary, a `date` birthday and a `set` of roles, and the output line shows the salary
as the string `"1000.00"` (lines 21 to 52). "From experience we find that class encoders are
the most common use case." (line 88). The same contributing sentence as requests-pro (line 139).

**What this repo adds to the KB.**
- representacao-nao-e-codificacao: `jsonstar/default_encoders.py` 62 to 73 and
  `jsonstar/encoder.py` 84 to 93; pattern serializacao-de-tipos (existing).
- a-interface-e-o-que-importa: the stdlib-shaped surface, `jsonstar/__init__.py` 7 to 24 and
  `README.md` 15 to 17.
- componha-em-vez-de-herdar: a conversion is a function registered by type, not a subclass
  per type; subclassing the encoder only scopes defaults (`README.md` 80 to 81).
- escolha-a-regra-mais-simples: three ordered lookups and nothing else, `jsonstar/encoder.py`
  84 to 93.
- nao-projete-a-generalizacao: attrs support is one functional encoder behind an import guard,
  `jsonstar/default_encoders.py` 31 to 39.
- No new pattern file from this repo in this pass.

**Caveats.**
- `dump` passes the decoder as the encoder: `def dump(obj, fp, cls=JSONDecoderStar, **kwargs)`
  (`jsonstar/__init__.py` line 7). At this commit `jsonstar.dump({"a": 1}, fp)` raises
  `TypeError: __init__() got an unexpected keyword argument 'skipkeys'` (run to confirm). No
  test covers `dump`.
- `load` defaults to `cls=None` while `loads` defaults to `JSONDecoderStar`
  (`jsonstar/__init__.py` lines 15 to 20): the two halves of the same API disagree.
- The decoder converts every string that `datetime.fromisoformat` accepts, including a plain
  `"2024-01-01"`, into a `datetime` (`jsonstar/decoder.py` lines 13 to 17; confirmed by
  running `loads`), with no way to opt out; the README never mentions the decoder.
- `suppress(Exception)` around every functional encoder (`jsonstar/encoder.py` line 90) is the
  shape rule `errors.bare-except` describes: a bug inside an encoder is indistinguishable from
  "not my type".
- Three tests never run: `TestTimeEncoder` methods without the `test_` prefix
  (`tests/test_default_encoder.py` lines 41 to 49). The `time` encoder is unverified.
- The README's examples do not run: `from jsonstar as json` (line 50) is a syntax error, and
  `json.register_default_encoder(Decimal, two_decimals_encoder)` (line 118) reverses the
  signature `register_default_encoder(function, type_=...)` (`jsonstar/__init__.py` line 23).
- `pydantic_dict` calls `o.dict()` (`jsonstar/default_encoders.py` lines 21 to 22), the method
  pydantic 2 deprecates, while the dev dependency is `pydantic = "^2.6.0"` (`pyproject.toml`
  line 74).
- The public way to declare class encoders is an underscore attribute (`README.md` lines 98 to
  100 against `jsonstar/encoder.py` lines 38 to 39); `default` is annotated `-> str` and
  returns lists and dicts (`encoder.py` line 84).
- Package metadata is split between `[project]` and `[tool.poetry]`; `lint.sh` needs zsh and a
  `$VENV_BIN` variable.
