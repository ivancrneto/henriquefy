---
repo: henriquebastos/beans
commit: ddfa931815bc580eeae39e7bcef1cceab204d2eb
era: 2026 to 2026
license: MIT
class: his
---
# beans

Every path and line below is at commit `ddfa931815bc580eeae39e7bcef1cceab204d2eb` (pushed
2026-09-02). Excerpts are full because the license is MIT.

**What it is.** `Graph-based issue tracker for AI agent coordination.` (README.md 3): a CLI
and library where issues are nodes in a SQLite-backed dependency graph, built so agents can
ask "what is ready to work on" (README.md 83-84). Stack: Python 3.12+, pydantic, typer,
sqlite3, uv. Size: 40 tracked files; 1,677 lines in six modules under `src/beans`; 3,118 lines
in ten test files. Published on PyPI as `magic-beans` 0.7.0 with the command `beans`
(pyproject.toml 2-3, 23-24). It is the smallest of his 2026 repositories and the one with the
clearest written house style (AGENTS.md); jira-genie reuses that style almost verbatim. 51
commits from 2026-03-27 to 2026-09-02 in conventional-commit form, the last one
`refactor: not-found exceptions own their message via class template`.

**Layout.**

```text
AGENTS.md            philosophy, module map, code style, dependency injection, testing, workflow, releasing
README.md            why beans exists (a critique of beads), design principles, quick start, commands
CHANGELOG.md, cliff.toml   git-cliff changelog from conventional commits
pyproject.toml       uv_build backend, typer + pydantic, ruff E,F,I,N,UP,RUF, pytest with coverage
tox.ini              py312, py313, py314 with the uv runner
.github/workflows/   ci.yml (matrix 3.12 to 3.14), release.yml
docs/                plans/, improvement proposals, phase specs, ideal help output
src/beans/
  models.py          pydantic models, BeanId(str), the exception family; no I/O
  store.py           the only module that touches SQLite; module-level row mappers and query builders
  api.py             one function per use case, composes store calls, raises domain errors
  config.py          global config as a pydantic model read from the XDG config directory
  workspace.py       finding the .beans directory: env var, registry, walk-up; init and migrate
  cli.py             typer wiring: parse, call api, format; maps exceptions to exit code 1
  templates/         AGENTS.md template copied into a project on init
tests/test_<module>.py   one file per module plus test_init, test_journal, test_registry, test_identifier
```

**How he tests.** pytest with coverage on by default: `addopts = "--cov=beans
--cov-report=term-missing --no-header -q"` (pyproject.toml 35-37); `hypothesis` and
`time-machine` in the dev group (28-32). One test file per source module. Classes group
behaviors and carry a one-line contract docstring: `class TestBeanDefaults: """A Bean created
with only a title gets sensible defaults."""` (tests/test_models.py 15-16), `class
TestCommandWiring: """Each command routes through api.py and returns exit code 0."""`
(tests/test_cli.py 39-40). The rule he wrote for it: `Assert against the model, not individual
fields` and `For model defaults, use model_dump() against an expected dict with fixed id and
created_at to pin dynamic fields.` (AGENTS.md 161-178), done at tests/test_models.py 18-35. No
mocks: `BeanStore gets a real SQLite :memory: database. Test real behavior, not mock wiring.`
(AGENTS.md 157-159). The CLI is tested through `typer.testing.CliRunner` behind two fixtures,
`cli` returning `(exit_code, output)` and `jcli` parsing the JSON (tests/test_cli.py 18-36).
Environment is injected with `monkeypatch.setenv("XDG_CONFIG_HOME", ...)` (tests/test_config.py
13-15, 22-23). `One assertion purpose per test` and `Readability over DRY. Allow repetition in
tests.` (AGENTS.md 208-216). The workflow is red-green-refactor with a commit at each step
(AGENTS.md 220-226). Not tested: the README's command transcripts are illustrative, not
executed.

**How he handles errors.** The domain declares a family in `models.py` and renders messages
from a class template, his last commit on the repository:

```python
class NotFoundError(KeyError):
    # KeyError wraps str(e) in quotes; raise with the offending ids and
    # let each subclass render its own instructive message.
    template: str

    def __str__(self):
        return self.template.format(*self.args)


class BeanNotFoundError(NotFoundError):
    template = "Bean not found: {0}"


class ParentBeanNotFoundError(BeanNotFoundError):
    template = "Parent bean {0} does not exist"


class DepNotFoundError(NotFoundError):
    template = "No dependency from {0} to {1}"


class CyclicDepError(ValueError):
    pass


class OpenChildrenError(ValueError):
    pass
```

(src/beans/models.py 12-38); `ProjectNotFoundError(NotFoundError)` joins the family from
`workspace.py` 71-72. `api.py` raises them where the outcome is known: `raise
ParentBeanNotFoundError(parent_id)` (27), `if store.update(bean_id, **clean) == 0: raise
BeanNotFoundError(bean_id)` (43-44), `raise OpenChildrenError(f"Cannot close {bean_id}: {count}
open ... remain")` (55-57). `cli.py` handles them by name at each command, `except
(BeanNotFoundError, OpenChildrenError) as e: error(rc, e)` (298), and one function turns the
exception into output: an `Error` pydantic model as JSON when `--json`, the message on stderr
otherwise, then `raise typer.Exit(code=1) from e` (140-146). `models.py` imports nothing from
typer, so the domain knows nothing about the CLI (1-9).

**Naming and interface.** `No underscore prefixes. Everything is public.` (AGENTS.md 34-37) and
the code keeps to it: `columns`, `row`, `rows`, `one_bean`, `beans`, `deps` are module-level
functions in `store.py` 13-40, where another author would write `_row_to_dict` (the bad
example at AGENTS.md 52-55). `Functions over methods. If it doesn't need self, it's a standalone
function` (39-42). The one value with domain meaning is a native subtype validated at
construction, with pydantic hooks so it composes into models:

```python
class BeanId(str):
    pattern = ID_PATTERN

    def __new__(cls, value="", **kwargs):
        if not cls.pattern.match(value):
            raise ValueError(f"Invalid bean id: {value}")
        return super().__new__(cls, value)
```

(src/beans/models.py 45-51; schema hooks 53-61; `generate` classmethod 63-65; `type_prefix`
property 67-69). Constants flow through signatures instead of being reached for: `def
find_beans_dir(start=None, dirname=DEFAULT_BEANS_DIR, env=os.environ, var=ENV_BEANS_DIR,
config_file=None) -> Path:` (workspace.py 60; rule at AGENTS.md 58-78). `**kwargs over dict
for named fields` (80-93), seen at `def update_bean(store: Store, bean_id, **fields) -> Bean:`
(api.py 40). Type annotations: `Annotate return types. Don't annotate parameters when the
default value tells the story.` (122-124), which is why most parameters are bare. Each
`api.py` function is one use case named as a verb phrase: `create_bean`, `show_bean`,
`update_bean`, `close_bean` (19, 36, 40, 48).

**Packaging, config, tooling.** 2026. Build backend `uv_build>=0.10.7,<0.11.0`
(pyproject.toml 16-21), `requires-python = ">=3.12"` after a short detour through 3.10
support (commits of 2026-04-14: `fix: lower requires-python to >=3.10` then `chore: raise
requires-python to >=3.12, revert 3.10/3.11 workarounds`). Two runtime dependencies with lower
bounds only: `pydantic>=2.0`, `typer>=0.9` (11-14). Ruff `select = ["E", "F", "I", "N", "UP",
"RUF"]`, line length 120, `force-sort-within-sections = true` with `# Python imports` / `# Pip
imports` / `# Internal imports` section comments mandated by AGENTS.md 106-120. CI matrix 3.12
to 3.14 running `uv run ruff check src/ tests/` and `uv run pytest` (.github/workflows/ci.yml
15-22); `tox.ini` with `uv-venv-runner` for the same matrix. Releases are a bump, a
`git-cliff` changelog, a tag and `gh release create` (AGENTS.md 263-283). No Makefile.
Configuration: a pydantic `Config` model loaded from `~/.config/beans/config.json`
(`Config.from_path`, src/beans/config.py 52-59) and two XDG reads with `os.environ.get`
(`config_dir`, `data_dir`, 87-98); the store location comes from `MAGIC_BEANS_DIR` through an
`env=os.environ` keyword default (workspace.py 23-26, 60-68); `MAGIC_BEANS_PARENT_ID` is read
in `cli.py` 67-70. Neither `python-decouple` nor `pydantic-settings` is used.

**README voice.** Two lines of pitch before the description: `Coding with AI makes developers
absurdly productive. Coffee keeps them going. Beans keep the whole loop fed.` (README.md 5-6),
then a terminal transcript (12-22). The "Why" section is a point-by-point critique of the tool
it replaces, named and linked (24-53), a comparison table (60-72), and six design principles
in bold, `Polite software.`, `Embedded storage.`, `Graph-native.`, `Agent-friendly.`,
`Minimal by default.`, `Journal-based sync.` (76-95). He explains by contrast and by promise:
`Beans never modifies files without asking, never installs hooks, never runs background
processes, and never phones home.` (76-77).

**What this repo adds to the KB.**

- prefira-excecoes-a-booleanos: the `NotFoundError` family with class templates
  (src/beans/models.py 12-38) and the by-name handling in `cli.py` (223, 237, 298, 549, 565).
- erros-na-fronteira, CLI form: `api.py` raises, `models.py` has no typer import, and one
  `error()` at the rim renders JSON or stderr and exits (src/beans/cli.py 140-146).
- componha-em-vez-de-herdar: extending a built-in where that is honest, `class BeanId(str)`
  (models.py 45-51), the same move as the course's `IntervalMap(dict)`; `Compose small
  functions rather than building class hierarchies.` (AGENTS.md 41-42).
- uma-responsabilidade-por-identidade and camada-de-servico: the module map with one sentence
  per module, `models.py: Pydantic models, pure functions, no I/O`, `api.py: Command API,
  composes store calls, returns models`, `cli.py: Typer CLI, thin wiring layer (parse, call,
  format)` (AGENTS.md 15-30; the arrows in the original are commas here).
- evite-ciclos-busque-a-arvore: `models.py: Pure data and pure functions. No imports from store
  or cli.` (AGENTS.md 25); dependency direction models, store, api, cli (api.py 5-16, cli.py
  16-53).
- configuracao-fora-do-codigo: `Default arguments for configurability. Never reference
  module-level constants directly inside function bodies. Instead, pass them as default
  arguments.` (AGENTS.md 58-63) and `env=os.environ` as a parameter (workspace.py 23, 60).
  A different tool from the course's `python-decouple`, same intent: one declared place, a
  default, testable without patching.
- o-codigo-e-a-interface: `**kwargs over dict for named fields ... It reads better at the call
  site and lets the interpreter catch typos.` (AGENTS.md 80-83); `Assert against the model, not
  individual fields` (161-175).
- teste-primeiro-das-folhas: `Red-green-refactor TDD` with a commit after green and after
  refactor (AGENTS.md 220-226); `No mocks` (157-159); one test file per leaf module.
- nao-projete-a-generalizacao and postergue-decisoes: `No over-engineering. Don't build
  abstractions until you have two concrete uses.` and `Defer what you don't need.` (AGENTS.md
  10-11).
- No pattern file written from this repo in this pass; `BeanId` is a candidate `python`
  rendition for a native-subtype pattern.

**Caveats.**

- `raise ParentBeanNotFoundError(parent_id)` inside `except BeanNotFoundError:` without
  `from` (src/beans/api.py 24-27), against hamsterdan's convention 43 `chain causes with raise
  ... from` and the course's habit of keeping the cause.
- Clock reads are inline, `datetime.now(UTC)` in a model default and in `close_bean`
  (src/beans/models.py 93; api.py 58), which the hamsterdan2 gate forbids (`Time is injected.`,
  quality/hamsterdan2/rules/clock-has-one-owner.yml 6). `time-machine` is in the dev group to
  compensate in tests.
- Two function-local imports: `from pydantic_core import core_schema` inside
  `__get_pydantic_core_schema__` (models.py 55) and `import shutil` inside a command (cli.py
  189); rule `modeling.local-import` fires on neither (both are third-party or stdlib), and
  hamsterdan's convention 42 would still want them at the top.
- AGENTS.md's module map names `project.py` (21, 29); the module is `workspace.py`. The doc
  drifted from the code.
- `close_bean` lists every bean to find open children (api.py 51-52); fine at this size, a
  query belongs in `store.py` when the graph grows.
- Section comments (`# Python imports`) are mandated here (AGENTS.md 106-120) and banned in
  spirit by hamsterdan's convention 53 (`Comments state the why or invariant the code cannot
  show`). The two repositories disagree.
