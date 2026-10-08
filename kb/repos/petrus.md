---
repo: henriquebastos/petrus
commit: 3f85fc2094e50ece48bcf6bf9ace19cb0a22a544
era: 2026 to 2026
license: Apache-2.0
class: his
---
# petrus

Every path and line below is at commit `3f85fc2094e50ece48bcf6bf9ace19cb0a22a544` (pushed
2026-09-13). Excerpts are full because the license is Apache-2.0.

**What it is.** His runtime for processes modeled as Petri nets, the thing hamsterdan runs on:
`Petrus is a Python runtime for processes modeled as Petri nets. A net makes the process state
explicit: places hold data tokens, and transitions consume, read, or produce tokens as work
progresses. Each running instance records an append-only History so its state can be inspected
and reconstructed.` (README.md 3-7). Stack: Python 3.14, pydantic, `cel-python`, optional
psycopg, pyzmq, cryptography and two agent SDKs behind extras. Size: 1,012 tracked files;
45,334 lines under `src/petrus` in seven subpackages; 72,202 lines under `tests/`; a `spec/`
directory; 36 ast-grep rules under `rules/`. Published as `petrus-runtime` `0.1.0a1`
(pyproject.toml 2-3), alpha by its own account (README.md 15-17). Same Driver/Navigator method
as hamsterdan (AGENTS.md 18-20). Public history is 50 commits from 2026-08-25, the last two
recording a history cleanup (`docs: record completed history cleanup`, 2026-09-12).

**Layout.**

```text
AGENTS.md                          Ariad method pointer, orientation list, Driver/Navigator
README.md                          runtime description, status, a runnable demo, a table of next steps
pyproject.toml, uv.lock            hatchling, extras with exact pins and the reason for each pin
conftest.py                        --forbid-skips policy and a per-worker PostgreSQL container that fails loud
sgconfig.yml, rules/, rule-tests/  36 ast-grep boundary rules, each with a fixture test
scripts/check                      quick | full | release | mutation
spec/                              OVERVIEW.md, net-document-v1.md, observation profiles
docs/process/                      engineering-conventions.md (6.7K), engineering-review-cases.md (68K), development-guide.md, releasing.md, DST documents
docs/project/                      briefing, decisions, debt, exploration (ES-059 experiments), roadmap
src/petrus/
  __init__.py                      one line; the root is an empty namespace by rule
  impetus/                         net semantics and History: petrinet/, binding/, history/, history_store/, instance/, selection/, dsl, net_definition, net_document
  motus/                           Activity execution: activity/, dispatch/, execution/, transport/ (zeromq), worker/
  engine/                          Engine composes Impetus and Motus for one live instance
  agenticus/                       agent attachment, catalog, connection custody, runtime adapters
  fabric/                          cross-instance coordination prototype, unfinished
  processes/                       subprocess call protocol
  simulation.py, simulation_http.py  bounded simulation and its stdlib HTTP transport
  telemetry.py                     orthogonal leaf
tests/petrus/<subpackage>/         mirrors src; tests/project/ holds conventions, boundaries, distribution, release tests; tests/dst/ the deterministic simulation campaign
```

**How he tests.** pytest with `--randomly-seed=1729`, `timeout = 180`, three opt-in markers
for real providers (pyproject.toml 92-101). The same `--forbid-skips` hook as hamsterdan lives in
conftest.py 35-57, and the conftest docstring states the policy: `The suite FAILS LOUD, never
silently skips, when docker is genuinely required and absent: a skipped Postgres suite would
report a green bar the durable backend never earned` (conftest.py 9-12; the dashes in the
original are commas here). Tests mirror the source tree (`tests/petrus/impetus/petrinet/
test_marking.py` for `src/petrus/impetus/petrinet/marking.py`). Style is class-grouped behavior
sentences: `class TestMarking:` with `test_consume_removes_the_requested_tokens_and_is_immutable`
(tests/petrus/impetus/petrinet/test_marking.py 39, 52), arrange, act, assert separated by blank
lines, assertion messages that name the invariant: `assert m.place(p) == (first, second,
third), "original marking must be untouched"` (62). Failures are asserted by name and message:
`with pytest.raises(ValueError, match="not present")` (93). Structural conventions are tests
too: `test_structural_conventions_hold` runs `ast-grep scan` and fails on any error-severity
match (tests/project/test_conventions.py 85-92), and
`test_every_production_module_has_structural_rule_coverage_or_rationale` requires every module
under `src/petrus` to be named by a rule's `files` list or by an exemption manifest with a
written reason (51-66; the two exemptions at 30-33). Mutation testing is curated to `marking.py`
and `selection/__init__.py` (pyproject.toml 103-115). `hypothesis==6.164.0` is pinned exactly
(59-63). Real HTTP tests spin a server on port 0 and use `urllib` (tests/petrus/engine/
test_simulation_http.py 28-50). Not tested: the README demo at lines 47-71; no test contains
its output string.

**How he handles errors.** Two shapes coexist, and convention 44 names the second as a
design-dependent variant. Taxonomies: `class CustodyError(RuntimeError): """Agent Connection
custody refused an operation without exposing authority."""` with seven empty subclasses,
`HostNotEnrolled`, `LeaseConflict`, `StaleCustody`, `StaleAttachment`,
`ReauthorizationRequired`, `OperationConflict`, `StorageContention`
(src/petrus/agenticus/connection/custody.py 51-80); `CatalogRegistrationError(ValueError)`
with `DuplicateRegistrationError` and `AmbiguousRegistrationError`, and
`UnknownRegistrationError(LookupError)` respecting the host contract (agenticus/catalog/
resolution.py 34-58); `TokenNotPresent(ValueError)` whose docstring explains the fail-loud half
of the contract and which carries the token so callers can re-address the rejection in their
own terms (impetus/petrinet/marking.py 54-62). Failure as data: `class ActivityError(Exception):
"""Exception an Activity raises to classify a safe operational failure."""` builds an
`ActivityFailure` value with `kind`, `details`, `retryable`, `retry_after` (motus/activity/
__init__.py 416-433), because Activity outcomes are persisted and replayed.

The HTTP transport is the course's exception-to-status table written with the standard
library. `class _RequestError(Exception)` carries an `HTTPStatus`, a code and a message
(src/petrus/simulation_http.py 29-32); every validation raises one, `raise
_RequestError(HTTPStatus.BAD_REQUEST, "invalid_request", "request body must be strict JSON")
from None` (67); and one `_dispatch` maps at the boundary:

```python
        except _RequestError as error:
            self._error(error.status, error.code, error.message)
        except ConnectionError, TimeoutError:
            pass
        except Exception:
            self._error(HTTPStatus.INTERNAL_SERVER_ERROR, "internal_error", "internal server error")
```

(230-235). Method checking is explicit: `if method not in allow.split(", "):
self._error(HTTPStatus.METHOD_NOT_ALLOWED, "method_not_allowed", "method not allowed",
allow=allow)` (221-223), with the `Allow` value per path in `_allow` (237-240). No bare
integer appears; `from http import HTTPStatus` is line 7.

**Naming and interface.** The root is empty on purpose: `src/petrus/__init__.py` is one line,
and the exemption manifest says why: `"Empty project namespace; concepts are imported from
their defining modules."` (tests/project/test_conventions.py 31). A list of 50-odd removed root
exports is kept as a test so no facade creeps back (tests/project/test_package_boundaries.py
30-60). Public concepts are nouns from the Petri-net vocabulary (`Marking`, `Token`, `NetPath`,
`Engine`, `InlineDispatch`, `NetSpec`, README.md 48-52) and the DSL reads as a sentence:
`flow.p.pending >> flow.t.finish >> flow.p.done` (55). Underscore privacy is used freely here,
unlike the hamsterdan2 gate: `_RequestError`, `_dispatch`, `_allow`, `_encoded`
(simulation_http.py 29, 203, 238, 35), a private module `agenticus/attachment/_retention.py`,
and `_CompletionCommitRefused(RuntimeError)` (impetus/instance/__init__.py 305). Factories are
intention-named: `Engine.create(built.net, "hello-1", history=..., dispatch=..., marking=...)`
(README.md 58-64), `create_simulation_server(built, "127.0.0.1", 0, allowed_origin=ORIGIN)`
(test_simulation_http.py 31). The boundary rules are the interface contract in executable form:
`Petrinet Kernel firing must remain history-independent: do not import history, storage,
Instance, dispatch, workers, private coordination, infrastructure, or higher layers.`
(rules/petrinet-is-independent.yml 4).

**Packaging, config, tooling.** 2026. `hatchling==1.31.0`, `requires-python = ">=3.14"`,
two runtime dependencies (`cel-python>=0.1`, `pydantic>=2.12,<3`) and six extras whose exact
pins carry a comment explaining the pin: `The D11 posture: Absurd 0.4.0 exact-pinned, never
forked, a re-pin is a deliberate act that re-verifies the vendored schema hash`
(pyproject.toml 33-36; dash rendered as a comma), `Amp A1 is qualified only against this exact
Neo SDK build` (48-49). The dev group pulls the extras back in so one plain pytest run covers
them (64-71). Ruff: line 120, `C901` enabled on `src/petrus` only (117-129). `ty==0.0.63`.
`scripts/check` has the same shape as hamsterdan's with `quick | full | release | mutation`
(scripts/check 11-16), and the release path is a manual GitHub workflow with SHA-pinned actions
and `persist-credentials: false` (.github/workflows/release-check.yml 1-20). No Makefile.
Configuration: the runtime reads no environment variables under `src/petrus` apart from the
`PATH`-style plumbing in subprocess helpers; the opt-in acceptance tests read `IMPETUS_TEST_DSN`,
`E2B_API_KEY`, `PETRUS_RUN_CV10_E2B` directly with `os.environ` and `os.getenv`
(tests/absurd_support.py 141; tests/petrus/motus/test_private_execution_substrate.py 697-701).
Neither `python-decouple` nor `pydantic-settings` is present.

**README voice.** The first paragraph defines the thing in four plain sentences (README.md 3-7)
and the second draws the line of responsibility: `External effects are at-least-once, so
applications own idempotency and reconciliation where repeating an effect would matter.`
(10-11). Status is stated before the demo: `Petrus is alpha software.` (15). The demo is a
complete script with its command and expected output (`['Hello, Petrus!']`, 44-81), followed
by what the demo does not promise (83-86) and a table `What you want to do | Start here`
(90-97).

**What this repo adds to the KB.**

- erros-na-fronteira and httpstatus-em-vez-de-numeros-magicos: a stdlib rendition of the
  course's table, `_RequestError(HTTPStatus.X, code, message)` raised by validators and mapped
  once in `_dispatch` (src/petrus/simulation_http.py 29-32, 67, 230-235). Candidate `python`
  rendition for pattern `excecao-para-http`; not written in this pass.
- o-verbo-comanda: the hand-rolled `405` with an `Allow` header per path
  (src/petrus/simulation_http.py 218-225, 237-240), the same shape as the course's Django
  decorator; cited as see-also in pattern `verbo-por-rota`.
- prefira-excecoes-a-booleanos: `CustodyError` and its seven named outcomes
  (src/petrus/agenticus/connection/custody.py 51-80); `TokenNotPresent` carrying the token
  (impetus/petrinet/marking.py 54-62).
- evite-ciclos-busque-a-arvore: 36 rules under `rules/` name the forbidden direction per
  package (rules/petrinet-is-independent.yml 8-12), and `test_concept_rules_name_canonical_forbidden_dependencies`
  checks that the rules still forbid what the architecture says (tests/project/
  test_conventions.py 69-82).
- o-codigo-e-a-interface: the empty root namespace and the removed-exports test
  (tests/project/test_conventions.py 31; tests/project/test_package_boundaries.py 30-60);
  the DSL line `flow.p.pending >> flow.t.finish >> flow.p.done` (README.md 55).
- uma-responsabilidade-por-identidade: `Use a function when an operation has a narrow
  interface and little state. Use an object when binding state and behavior makes the interface
  materially smaller or enforces an invariant. Do not create a class merely to namespace one
  function` (docs/process/engineering-conventions.md 77-80).
- camada-de-servico: `Keep CLIs, scripts, servers, workers, and transport integrations as thin
  adapters over importable operations.` (71-72); `Inner operations return values or structured
  reports; only the outermost adapter prints, writes, or exits.` (98-99).
- teste-primeiro-das-folhas: `Test the public behavior and the reason it matters, not
  incidental helper decomposition.` (111-112); `Keep one-off setup inline.` (114);
  tests/petrus/impetus/petrinet/test_marking.py as a leaf test file.
- pragmatismo-sobre-pureza and postergue-decisoes: `Do not add framework-specific ceremony
  before Impetus owns that framework or surface. A future CLI, telemetry API, database adapter,
  or worker system earns its detailed conventions when implementation and review provide
  evidence.` (46-48); `An entry explicitly marked provisional is evidence, not binding
  convention, until the Navigator ratifies it.` (26-27).
- a-interface-e-o-que-importa: `Never silently ignore, neutralize, or overwrite an
  operator-provided option. Reject incompatible options before starting work.` (100-101).
- No pattern file written from this repo in this pass.

**Caveats.**

- PLAN.md calls this his Starlette code. At this commit there is no `starlette` or `fastapi`
  import under `src/petrus`; the only HTTP surface is `http.server` (src/petrus/
  simulation_http.py 8). The FastAPI code is in hamsterdan.
- The README demo is not executed by any test (no test contains `Hello, Petrus!`), which is
  what hamsterdan's convention 55 asks for; petrus's own conventions file does not state that
  rule.
- Banner comments and import-section comments, which the hamsterdan2 gate bans
  (quality/hamsterdan2/rules/no-banner-comments.yml), appear in 54 files here: `# ── Token
  ────` (tests/petrus/impetus/petrinet/test_marking.py 13, 36) and `# Python imports` /
  `# Pip imports` (conftest.py 17, 22). His 2026 repositories disagree with each other on this.
- `_dispatch` carries `# noqa: C901` (src/petrus/simulation_http.py 203), the documented
  exception route for a cohesive parser; and `except ConnectionError, TimeoutError: pass`
  (232-233) swallows at the transport rim, which is defensible there and nowhere else.
- Underscore privacy is pervasive (`_RequestError`, `_retention.py`,
  `_CompletionCommitRefused`), the opposite of beans, jira-genie and the hamsterdan2 gate.
- 26 indented import lines under `src/petrus`; some are `TYPE_CHECKING` blocks, some are
  function-local. Not audited line by line in this pass.
