---
repo: henriquebastos/jira-genie
commit: 405a8f4042e8fbb2780ce1c2ee0048c47ff03af7
era: 2026 to 2026
license: MIT
class: his
---
# jira-genie

Every path and line below is at commit `405a8f4042e8fbb2780ce1c2ee0048c47ff03af7` (pushed
2026-09-18). Excerpts are full because the license is MIT.

**What it is.** `Your AI agent's interface to Jira Cloud. JSON in, JSON out.` (README.md 7): a
CLI and library over the Jira Cloud REST API with OAuth 2.0 (3LO) plus PKCE, schema-aware field
names (`story_points` instead of `customfield_10036`, 10-11), templates, shell completion and
an installable agent skill. Stack: Python 3.11+, argparse, `requests-pro` (his own HTTP client
library), `mistune` for Markdown to ADF, `argcomplete`. Size: 60 tracked files; 1,768 lines in
twelve modules under `src/jira_genie`; 2,308 lines in twelve test files. Version 0.4.0, command
`jira` (pyproject.toml 3, 27-28). It consumes beans for its own task tracking (`beans.jsonl`
at the root; AGENTS.md 23-25) and copies beans's house style into `docs/conventions.md` and
`docs/testing.md`. 50 commits from 2026-03-27 to 2026-09-17, conventional with `#closes
bean-...` trailers.

**Layout.**

```text
AGENTS.md                 a map: orientation links, verification gate, work tracking, releasing
README.md                 pitch, why, install, quick start, agent integration, error handling, auth
PLAN.md, PRIVACY.md       implementation design; privacy statement for the default OAuth app
docs/                     architecture.md, conventions.md, testing.md, contributing.md, workflow.md, tooling.md, beans.md, a handoff note
skills/jira-genie/SKILL.md   the agent skill, packaged into the wheel (pyproject.toml 17-18)
scripts/                  release.sh, worktree-create.sh, worktree-remove.sh
pyproject.toml            setuptools build, requests-pro unpinned, ruff E,F,I,N,UP,RUF, pytest with coverage
.github/workflows/        ci.yml (matrix 3.11 to 3.14), release.yml
src/jira_genie/
  __main__.py             three lines, delegates to cli
  cli.py                  argparse: parse() is pure, cli() dispatches and owns I/O; _handle_* per command group
  client.py               JiraSession(ProSession) and sub-clients composed into JiraClient
  auth.py                 JiraAuth(RecoverableAuth): OAuth login flow with a local HTTP callback, token renewal
  config.py               discover_instance_dir(): instance arg, JIRA_INSTANCE, config.json default, single instance
  schema.py               field registry and per-type schema from createmeta; friendly_name()
  templates.py            JSON templates on disk
  adf.py                  Markdown to Atlassian Document Format and back
  cache.py, completers.py, formatters.py, skill.py   small leaves
tests/test_<module>.py    one file per module; conftest.py with the responses fixture
```

**How he tests.** pytest with coverage on by default (pyproject.toml 39-41); dev group
`responses`, `time-machine`, `ruff` (30-37). HTTP is mocked at the transport, never at the
session: `This project uses the responses library to mock HTTP calls at the transport level,
the same pattern as requests-pro. Don't mock session classes or build fake adapters` (docs/
testing.md 10-12); the shared fixture is `responses_lib.RequestsMock(assert_all_requests_are_fired=False)`
(tests/conftest.py 6-9). Tests assert the request that went out: `assert
"fields=summary%2Cstatus" in req.url` (tests/test_client.py 57-61). Configuration is tested by
passing the base directory, not by patching: `discover_instance_dir(base_dir=tmp_path)`
(tests/test_config.py 20-23), with `monkeypatch.setenv("JIRA_INSTANCE", "other")` only for the
env-var branch (31-36). Errors are asserted by type and message: `with pytest.raises(ConfigError,
match="Multiple instances")` (48-49). Classes group behaviors, mostly without docstrings
(`class TestIssueSubClient:`, test_client.py 51). The written rules are beans's: `No mocks
(when possible)`, `Assert against the model, not individual fields`, `One assertion purpose per
test`, `Readability over DRY` (docs/testing.md 3-6, 37-40, 84-92), plus one of his own: `When
using a private or less-known dependency, read its test suite before writing your own tests.`
(31-35). The CLI's `parse()` is tested directly, `no CliRunner needed` (docs/conventions.md
169-177).

**How he handles errors.** Three flat exceptions, one per module that owns an outcome: `class
ConfigError(Exception): pass` (src/jira_genie/config.py 9-10), `class JiraAuthError(Exception):
pass` (auth.py 33-34), `class TemplateError(Exception): pass` (templates.py 9-10). Messages
name the next action: `raise ConfigError(f"No config directory found at {base}. Run: jira auth
login")` (config.py 26), `raise JiraAuthError("Not logged in. Run: jira auth login")` (auth.py
54), and list what is available: `raise ValueError(f"Status '{status_name}' not found.
Available: {available}")` (client.py 50-51). HTTP failures are left to `requests`:
`response.raise_for_status()` in `safe_request` (client.py 14-18). One rim turns everything
into structured output:

```python
def cli(argv=None):
    """Entry point. Parses, dispatches, handles I/O."""
    try:
        _dispatch(parse(argv))
    except SystemExit:
        raise
    except Exception as e:
        print(json.dumps({"error": str(e), "type": type(e).__name__}), file=sys.stderr)
        sys.exit(1)
```

(src/jira_genie/cli.py 199-207), which the README documents as the contract: `All errors
output structured JSON to stderr` with the example `{"error": "404 Client Error: Not Found for
url: ...", "type": "HTTPError"}` (README.md 103-113). Handlers catch `ConfigError` and
`FileNotFoundError` together where "not configured yet" is a normal state (cli.py 255, 265).

**Naming and interface.** The public surface is the command tree: `jira auth login`, `jira
fields sync`, `jira issue get DEV-123`, `jira search "<jql>"`, `jira bulk edit` (README.md
45-86). Internally the library is a session class plus sub-clients composed into one client:

```python
class JiraClient(MainClient):
    def __init__(self, session):
        super().__init__(session, audit=False)
        self.issue = IssueSubClient(session)
        self.search = SearchSubClient(session)
        self.sprint = SprintSubClient(session)
        self.board = BoardSubClient(session)
        self.user = UserSubClient(session)
```

(src/jira_genie/client.py 151-158), so callers write `client.issue.transition("DEV-1",
"Done")`. The session extends the host library at one hook only: `class
JiraSession(ProSession): def before_prepare_body(self, request):` with a docstring that names
the foreign mechanism (`CloudFront blocks GET with Content-Type: application/json`, 6-11).
Wiring is a classmethod, `JiraClient.from_config(cls, instance=None)` (160-184). Functions
take their configuration as defaults: `def discover_instance_dir(instance=None,
base_dir=BASE_DIR)` (config.py 13), `def generate_pkce(nbytes=PKCE_BYTES)` (auth.py 24).
`parse()` carries the docstring `"""Pure parsing. Returns a Namespace. No I/O."""` (cli.py
17-18). The stated rule is `No underscore prefixes ... If it's in the module, it's part of the
module.` (docs/conventions.md 18-23); the CLI does not follow it: `_dispatch`, `_handle_auth`,
`_handle_fields` and the rest (cli.py 210, 239, 270-634).

**Packaging, config, tooling.** 2026. Build backend `setuptools>=75.0` with `where = ["src"]`
(pyproject.toml 20-25), the only one of the four repositories not on hatchling or uv_build;
`requires-python = ">=3.11"`. Three runtime dependencies: `argcomplete>=3.6.3`,
`mistune>=3.1`, `requests-pro` with no version at all (11-15). Ruff `E, F, I, N, UP, RUF`,
line 120, `force-sort-within-sections` (43-51); the same `# Python imports` section comments
as beans (cli.py 1-10). CI matrix 3.11 to 3.14, `uv run ruff check src/ tests/` and `uv run
pytest` (.github/workflows/ci.yml 15-20); releases through `./scripts/release.sh 0.5.0`
(`never release manually`, AGENTS.md 27-34) and a Homebrew tap (README.md 29-31). No Makefile.
Configuration: per-instance `config.json` files under `~/.config/jira-genie/<cloud_id>/`
resolved by `discover_instance_dir` in a stated order, `1. instance arg 2. JIRA_INSTANCE env
var 3. config.json -> 'default' 4. Only one instance exists? Use it. 5. Error` (config.py
13-22, 28); `JIRA_CLIENT_ID` and `JIRA_CLIENT_SECRET` read with `os.environ.get` in
`_handle_auth` (cli.py 244-245); tokens kept by `requests-pro`'s `TokenStore` over a
`FileCache` (client.py 180-181). Neither `python-decouple` nor `pydantic-settings` is used.
The default OAuth app's client id and client secret are literals in the source
(`DEFAULT_CLIENT_ID`, `DEFAULT_CLIENT_SECRET`, cli.py 12-14); see Caveats.

**README voice.** Pitch first, in the second person: `Give your agents the ability to search,
create, edit, and manage Jira issues through a simple CLI.` (README.md 9-10). A "Why" list of
six bold promises, `JSON by default`, `Friendly field names`, `Templates`, `Shell completion`,
`Zero-config auth`, `Agent-ready` (17-24), then install, a numbered quick start with the JSON
each command prints (44-63), and an "Agent Integration" section written as shell comments an
agent would follow (70-87). The error contract gets its own section with an example (103-113).

**What this repo adds to the KB.**

- a-interface-e-o-que-importa: the product is an interface decision, `JSON in, JSON out` and
  friendly names resolved from the live schema (README.md 7, 17-24; src/jira_genie/schema.py
  8-10); error messages that name the fix (config.py 26, 60; client.py 50-51).
- erros-na-fronteira, CLI form: library modules raise, one rim renders (src/jira_genie/cli.py
  199-207); README.md 103-113 states it as a contract.
- componha-em-vez-de-herdar: `JiraClient` holds five sub-clients (client.py 151-158);
  `JiraSession(ProSession)` overrides one hook of the host library and nothing else (6-11).
- camada-de-servico and uma-responsabilidade-por-identidade: `parse / cli split. Separate
  parsing from execution for testability` (docs/conventions.md 154-167); `Pure by default. Push
  I/O to the boundary.` (9-12).
- configuracao-fora-do-codigo: `Default arguments for configurability` (docs/conventions.md
  48-68) applied to `base_dir=BASE_DIR` (config.py 13), which is what makes
  `discover_instance_dir(base_dir=tmp_path)` testable without patching (tests/test_config.py
  20-23). The same file also contradicts the principle; see Caveats.
- teste-primeiro-das-folhas: `Check upstream test patterns` (docs/testing.md 31-35); the
  verification gate `uv run pytest` then `uv run ruff check src/ tests/` (AGENTS.md 16-21).
- pragmatismo-sobre-pureza: `argparse (not Typer). ... The Jira field schema is dynamic
  (varies per instance) ... Decorator-based frameworks fight this; argparse gives full runtime
  control with no dependencies.` (docs/conventions.md 147-152): the tool is chosen by the
  domain's shape, against his own default in beans.
- No pattern file written from this repo in this pass.

**Caveats.**

- A client secret in source: `DEFAULT_CLIENT_SECRET = "ATOA0mBJ..."` (src/jira_genie/cli.py
  13-14), used as the default for `_handle_auth` (239). His own convention here says `Defaults
  and configuration values (API keys, base URLs, feature flags) belong in the CLI layer`
  (docs/conventions.md 10-12), and README.md 127 presents the shipped OAuth app as a feature;
  the course principle says credentials never live in the repository. Stated plainly: this is
  against configuracao-fora-do-codigo, by design.
- Function-local imports throughout: 37 indented import lines under `src/jira_genie`, most of
  them `from jira_genie.<module> import ...` inside handlers (cli.py 243, 250, 261, 270, 273,
  310, 326, 347, 358, 418-419, 428, 438, 445, 456, 494-495, 511-512, 524, 634; completers.py
  37, 51; formatters.py 17; schema.py 81), and `from_config` with the comment `# Internal
  imports to avoid circular deps` (client.py 163-170). Rule `modeling.local-import` fires on
  each project-internal one; hamsterdan's convention 42 says `a cycle means the module graph is
  wrong`.
- Underscore-prefixed handlers (`_dispatch`, `_handle_*`, cli.py 210-634) against the repo's
  own `No underscore prefixes` (docs/conventions.md 18-23).
- `except Exception as e:` at the rim without re-raise (cli.py 205-207); rule
  `errors.bare-except` fires. It is the documented contract for agents, and a narrower set
  (`ConfigError`, `JiraAuthError`, `TemplateError`, `requests.HTTPError`, `ValueError`) would
  keep the contract and let programming errors surface.
- `requests-pro` has no version bound (pyproject.toml 14), so an install today and one next
  year may differ; hamsterdan pins everything, including by commit.
- Clock reads inline, `datetime.now(UTC)` (src/jira_genie/cache.py 8; schema.py 155), as in
  beans; the hamsterdan2 gate forbids it.
- `safe_request` is a generic name for "request that tolerates 204" (client.py 14-18); beans's
  and hamsterdan's rules both ask for a name that states the capability.
