---
repo: henriquebastos/sqlformatter
commit: c36c66a4c720dfde37343d300ae731285c5600ad
era: 2014 to 2022
license: MIT
class: his
---
# sqlformatter

**What it is.** A `logging.Formatter` that reindents and colorizes the SQL Django's
`django.db.backends` logger emits, plus a `logdb()` toggle for shell sessions. One module of 82
lines, two dependencies (sqlparse, Pygments), no tests. Extracted from a client project in
March 2014 ("Extract code from its original project", `f414788`), last touched 2020-10-30 when
he bumped to 1.4, added a GitHub Actions publish workflow and committed the built tarball. 24
commits, 22 his. MIT: excerpts are full.

**Layout.**

```
sqlformatter/
├── sqlformatter.py            SqlFormatter, LogDb, the module-level logdb instance
├── setup.py                   setuptools, py_modules, install_requires read from requirements.txt
├── requirements.txt           Pygments==1.6, sqlparse==0.3.1
├── MANIFEST.in                include README.rst and requirements.txt
├── README.rst                 problem, screenshot, install, two usage modes, license text
├── screenshot.png             the colored output
├── LICENSE                    MIT
├── dist/sqlformatter-1.4.tar.gz   the built sdist, committed ("Record dist", 2020-10-30)
├── .github/workflows/main.yml publish to PyPI on v* tags; no test job
└── .gitignore                 the GitHub Python template of 2013
```

**How he tests.** He does not. There is no `tests/` directory, no `test_*.py`, no test step
in CI; the workflow only publishes (`.github/workflows/main.yml:7-17`). The README stands in
for a smoke test: a three-line shell session, enable, run a query, disable (`README.rst:45-53`),
and a screenshot (`:20`).

**How he handles errors.** Nothing is declared or caught. `format` reads `record.sql`
(`sqlformatter.py:28`), an attribute only Django's database logger sets, so attaching the
formatter to any other logger raises `AttributeError` on the first record. Option kwargs are
popped before the parent constructor sees them (`:13-18`), so an unknown option reaches
`logging.Formatter` and fails there. The Windows limitation is handled at import, not at
call time: `logdb = LogDb(highlight=False)` when `os.name == 'nt'` (`:79-82`, commit
`2ea0403`, "Closes #1 Windows does not support highlight.").

**Naming and interface.** Two classes and one instance. `SqlFormatter(logging.Formatter)`
takes five keyword options whose names are the underlying libraries' names (`highlight`,
`style` for Pygments; `parse`, `reindent`, `keyword_case` for sqlparse, `:13-18`), holds a
lexer and a terminal formatter as `_lexer` and `_formatter` (`:20-21`), and overrides only
`format` (`:25-36`). `LogDb` is a toggle object:

```python
class LogDb:
    def __init__(self, name='django.db.backends', handler=None, propagate=None, **kwargs):
        self.name = name
        self.propagate = propagate

        self.handler = handler or logging.StreamHandler(sys.stdout)
        self.formatter = SqlFormatter(**kwargs)

        self.running = False

    def __call__(self, **options):
        # Toggle
        if not self.running:
            self.enable()
            self.running = True
        else:
            self.disable()
            self.running = False

        return self.running
```
(`sqlformatter.py:39-58`), with `enable` and `disable` as the two verbs (`:60-77`). The public
surface is `SqlFormatter`, for `LOGGING` settings, and `logdb`, for a shell (`README.rst:34-84`);
`LogDb` is importable but undocumented.

**Packaging, config, tooling (2014, re-released 2020).** `setup.py:9-29`: version `'1.4'`
literal, `py_modules=['sqlformatter']`, `long_description` from `README.rst`, and
`install_requires=open(REQUIREMENTS).readlines()` (`:19`), which turns the two exact pins of
`requirements.txt:1-2` (`Pygments==1.6`, `sqlparse==0.3.1`) into hard constraints on every
installing project. `MANIFEST.in:1-2` ships both files. `# coding: utf-8` and
`super(SqlFormatter, self).__init__` (`sqlformatter.py:1, 23, 26`): Python 2 compatible in
2020. The CI file is the first GitHub Actions workflow among the repos in this set:

```yaml
on:
  push:
    tags: v*
...
      - name: Publish package
        if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags')
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: __token__
          password: ${{ secrets.pypi }}
```
(`.github/workflows/main.yml:3-5, 12-17`): publish on tag, action pinned to `@master`, a
PyPI token in a secret, no checkout, no build, no tests. The sdist it would publish is also
committed to the repository (`dist/sqlformatter-1.4.tar.gz`). No lint, no formatter, no
Makefile.

**README voice.** Problem, then relief: "Logging your SQL to the console helps you understand
whats going on under the ORM. However, queries can get pretty big resulting on a code wall."
(`README.rst:4-6`), "*SQLFormater* is a logging formatter that *idents* and *colorize* your
SQL statements making everything legible again." (`:8`). "How it looks like?" is a screenshot
(`:17-21`). Usage is split by situation, "Temporarily enable it during a console session"
(`:36`) and "Add it to your Django Logging settings" (`:55`), each with a paste-ready block.
Customization is one sentence and a shrug: "Check out the source code." (`:92`). The MIT text
is pasted in full at the end (`:94-117`).

**What this repo adds to the KB.**
- `o-codigo-e-a-interface`: `logdb()` reads as the thing it does, and the README's usage is
  three lines of a shell session (`README.rst:45-53`; `sqlformatter.py:49-58`).
- `nao-projete-a-generalizacao`: options are forwarded by name to the libraries that own them
  (`sqlformatter.py:13-18, 31, 34`); no option schema, no settings object.
- `pragmatismo-sobre-pureza`: the Windows case is one `if` at import (`:79-82`), not a
  capability layer.
- `uma-responsabilidade-por-identidade`: formatting (`SqlFormatter`) and wiring to a logger
  (`LogDb`) are separate objects (`:11, 39`).
- Pattern files: none written or amended in this pass.

**Caveats.**
- Zero tests on a published library (no `tests/`, no test job in `.github/workflows/main.yml`).
  Both courses treat the test as the specification; this repo has none.
- Exact pins as `install_requires` (`setup.py:19` with `requirements.txt:1-2`): a logging
  helper that forbids any other `sqlparse` in the project. The API course calls a conflicting
  pin set "documentação que mente" (`kb/courses/design-api-na-pratica.md:1466`); this is the
  library-side version of the same mistake.
- `dist/sqlformatter-1.4.tar.gz` is committed; build artifacts in git.
- `pypa/gh-action-pypi-publish@master` (`main.yml:14`): an unpinned action on the publish
  path; the 2026 repos pin `@release/v1`.
- `self.propagate` is both a constructor argument and the saved logger state
  (`sqlformatter.py:40-42, 67, 76-77`); one attribute with two meanings.
- `LogDb.__call__(**options)` accepts options it ignores (`:49`).
- `format` assumes `record.sql` exists (`:28`); no message when it does not.
- README typos: "whats", "resulting on", "SQLFormater", "idents", "passa" (`README.rst:4, 6, 8, 89`).
