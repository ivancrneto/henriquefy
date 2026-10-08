---
repo: henriquebastos/hamsterdan
commit: 5d382467eaa4ff837cbd6b93012c99081e0153f9
era: 2026 to 2026
license: Apache-2.0
class: his
---
# hamsterdan

Every path and line below is at commit `5d382467eaa4ff837cbd6b93012c99081e0153f9` (pushed
2026-09-11). Excerpts are full because the license is Apache-2.0.

**What it is.** A GitHub App that watches pull requests and drives review, CI observation,
agent repair and human approval through one Petri-net workflow on his own runtime, Petrus
(README.md 3-6). Stack: Python 3.14, FastAPI for the webhook ingress, githubkit for the
provider, pydantic, SQLite stores, uv. Size: 976 tracked files; 29,367 lines under `src/`
(the operational V5 runtime in `src/hamsterdan`, 46 modules, plus a non-selectable
replacement tree `src/hamsterdan2`, 19 modules); 29,248 lines in `tests/`, 1,394 in
`tests2/`, and a `deployment/` package with its own tests. The code was written with an
agent as Driver and him as Navigator (AGENTS.md 10-12), so this is the repository where he
wrote his rules down for someone else to follow: `docs/process/engineering-conventions.md`
(68 numbered conventions plus a typed-data decision ladder), `tests/test_architecture.py`,
seven ast-grep rules under `quality/hamsterdan2/rules/`, and one non-blocking audit rule under
`audit-rules/`. Public history is 50 commits from 2026-08-31 after a clean-root rebaseline; the
worklog goes back to 2026-08-01 (docs/process/worklog/index.md 6).

**Layout.**

```text
AGENTS.md                      agent contract: Driver/Navigator, lifecycle, architecture contract, secrets
CONTRIBUTING.md, SECURITY.md   early source publication notices
README.md                      what it is, architecture diagram, "start with" file list
pyproject.toml, uv.toml, uv.lock, .python-version   hatchling build, frozen uv, resolver cutoff, 3.14.7
conftest.py                    --forbid-skips pytest policy shared by serial and xdist runs
sgconfig.yml, audit-rules/, audit-rule-tests/        non-blocking ast-grep audit (reflective access)
scripts/check                  one feedback interface: quick | hamsterdan2 | tests | full | release | audit | mutation
quality/hamsterdan2/           strict gate for the replacement tree: ruff.toml (select ALL, mccabe 4), 7 ast-grep rules
deployment/                    Containerfile, ansible, deploy/release/observe scripts, their tests
docs/process/                  engineering-conventions.md, development-guide.md, complex-system-correctness.md, worklog/
docs/project/                  briefing, decisions/records (28), debt/items (13), exploration, roadmap
docs/product/principles.md     six product principles
src/hamsterdan/
  __init__.py                  empty namespace: `__all__: list[str] = []`
  contracts/                   readiness.py, readiness_v5.py: neutral typed contracts shared by siblings
  github_app/                  the only owner of githubkit and httpx: auth, config, effects, gateway, models, routing, transport, webhooks
  agents/                      credential-free typed agent protocol and the Pi runner
  readiness/net_v5/            the workflow Net: board, ci, conversation, dashboard, esc, gating, life, mutation, readiness, reminders, review, startup, topology
  host/                        the only composition root: api.py (FastAPI), service.py, __main__.py, v5/ runtime, agenticus, export, git_publish
  operator.py                  JSON-output operator CLI
  testing/                     readiness world and campaign generators used by integration tests
src/hamsterdan2/               replacement outer system: github_app, host (api, application, composition, database, pr_workflows, values, webhook_inbox), readiness, workflow
tests/                         test_architecture.py, test_check_command.py, test_distribution.py, test_pytest_policy.py, unit/, integration/
tests2/                        replacement suite: test_architecture.py, test_enum_privacy.py, test_feedback.py, intake tests
```

**How he tests.** Runner is pytest with `pytest-randomly` at a fixed seed, `pytest-timeout`
and `pytest-xdist` (pyproject.toml 30-33, 51-54: `addopts = "--randomly-seed=1729"`,
`timeout = 30`). The routine suite runs on four workers and fails on any skip: `scripts/check`
76 `uv run pytest -q "$@" --randomly-seed="$seed" --forbid-skips -m "$ROUTINE_TESTS"`; the
`--forbid-skips` option is a repository conftest hook that turns a green session with skips into
`TESTS_FAILED` (conftest.py 10-32), and that policy is itself tested by running pytest on a probe
file (tests/test_pytest_policy.py 18-40). `release` repeats the suite serially with a second
seed (scripts/check 108-112). Layout is `tests/unit/<package>/` mirroring `src/`, plus
`tests/integration/host/` and four repository-level tests at the top (`test_architecture.py`,
`test_check_command.py`, `test_distribution.py`, `test_pytest_policy.py`).

Most tests are module-level functions with long behavior names:
`test_fastapi_accepts_durably_before_work_deduplicates_and_has_sanitized_health`
(tests/integration/host/test_service.py 389). Class scenarios appear where convention 57 asks
for them, in the Net loop tests and in `tests2/`: `class TestWebhookInboxHandoff:` with the
one-line contract docstring `"""Raw intake, semantic dedupe, and History completion have
distinct owners."""` (tests2/test_webhook_inbox_intake.py 164-165), arrange, act and assert
separated by blank lines (167-198). Fakes are duck-typed classes that record calls and classify
by mode, not `unittest.mock`: `class FakeBroker:` with `self.calls: list[tuple] = []`
(tests/unit/host/test_v5_rerun.py 46-70). `monkeypatch` appears in 13 test files, at seams the
module does not own (`monkeypatch.setattr(os, "fsync", observe)`, tests/unit/host/test_pi_a2.py
45). The FastAPI boundary is tested through `TestClient(create_app(host, reconcile_startup=False))`
with signed bodies (test_service.py 398-414). Whole-record assertions are the norm:
`assert response.json() == {"custody": "durable", "delivery_id": delivery, "disposition":
"accepted"}` (403).

Architecture is tested, not described. `tests/test_architecture.py` parses imports with `ast`
and asserts: siblings never import one another (62-72), only `host` composes concrete
subsystems (75-97), siblings and contracts never import host (100-106), FastAPI stays in host
and githubkit/httpx stay in github_app (144-158), and no module imports the `petrus` root or an
`impetus` facade (127-131). `tests2/test_architecture.py` adds a cycle check with
`graphlib.TopologicalSorter` (95-110), forbids `__init__.py` re-exports (79-92), pins which
file may import FastAPI (137-148), and even pins the three SQLite file names (212-231).
`tests2/test_enum_privacy.py` fails when an enum member is read outside its owning module:
`"Enum vocabulary leaked; read state through is_*/can_*/has_* predicates:\n"` (45-48).
`tests/test_distribution.py` builds the wheel and sdist and asserts no `.env`, `.pem` or
`.sqlite` member (13-36). Mutation testing is curated to one module (pyproject.toml 60-66).
Not tested: the README has no worked example, so there is nothing to execute (see Caveats).

**How he handles errors.** The V5 tree declares flat, named exceptions per boundary:
`class WebhookRejected(ValueError): pass` (src/hamsterdan/github_app/webhooks.py 45-46),
raised eleven times with instructive messages (`"signature verification failed"`, 183;
`"delivery id is malformed"` with `from None`, 179); `class ConfigurationError(ValueError):
"""A configuration failure that never includes a secret value."""` (github_app/config.py
23-24); `GitHubBoundaryError(RuntimeError)` carrying a bounded `failure_class`,
`provider_status` and `provider_detail` validated in `__init__` (github_app/models.py 22-40);
and `RerunRefusedError(RuntimeError)` whose docstring says why it is deliberately not a
`GitHubBoundaryError` (43-47). The replacement tree follows convention 43 to the letter: a base
per module with empty named subclasses, `class WebhookInboxError(Exception)` then
`WebhookInboxCapacityError`, `WebhookInboxCorruptionError`, `WebhookInboxDeliveryNotFoundError`,
`ProviderRouteNotConfiguredError` (src/hamsterdan2/host/webhook_inbox.py 59-76), the same in
`pr_workflows.py` 28-40, `database.py` 116-124 and `readiness/runtime.py` 47-59; and
`WebhookRefusalError(Exception)` carries a typed `reason: RefusalReason` (hamsterdan2/github_app/
webhooks.py 68-73).

What reaches the HTTP boundary is mapped inside the route, not by a registered handler.
`src/hamsterdan/host/api.py` 46-49:

```python
        try:
            receipt = await asyncio.to_thread(service.custody.receive, headers, bytes(body))
        except WebhookRejected as error:
            raise HTTPException(status_code=400, detail=str(error)) from None
```

and `src/hamsterdan2/host/api.py` 51-59 catches `WebhookRefusalError` and
`WebhookInboxCapacityError` and returns `refusal_response(reason)`, a single function that picks
`status.HTTP_503_SERVICE_UNAVAILABLE` or `status.HTTP_400_BAD_REQUEST` and serializes a pydantic
`WebhookRefusalResponse` (21-34). The CLI rim does the same in one place: `except
(ConfigurationError, RuntimeError, ValueError) as error: parser().error(str(error))`
(host/__main__.py 262-264). The domain side is clean: `WebhookRejected` lives in `github_app`,
which cannot import FastAPI (tests/test_architecture.py 155-158).

**Naming and interface.** Packages do not re-export: `src/hamsterdan/__init__.py` is
`"""Hamsterdan application package; public concepts live in their owning modules."""` and
`__all__: list[str] = []` (1-3), enforced by `test_project_uses_the_petrus_distribution_without_compatibility_facades`
(tests/test_architecture.py 51-59) and, for the replacement tree, by
`test_packages_do_not_reexport_children_or_offer_facades` (tests2/test_architecture.py 79-92).
The one exception is `host/__init__.py`, which exports `HostService` and `create_app` (3-6).
Module names follow convention 6: singular for one concept (`gateway.py`, `binding.py`),
plural for a family (`webhooks.py`, `effects.py`, `timers.py`); there is no `utils.py` or
`helpers.py` anywhere under `src/`. Classes are nouns named for a role, not a layer:
`HostService`, `WebhookInbox`, `PullRequestAuthority`, `GitHubWebhookNormalizer`
(hamsterdan2/host/composition.py 10-15). Wiring lives in intention-named constructors:
`HostConfig.from_environment` (github_app/config.py 229-230), `ApplicationDatabase.from_path`
(composition.py 35), `build_hamsterdan(*, state_root)` (53-58); `create_app(service, *,
reconcile_startup=True)` takes the service, it does not build it (host/api.py 15). Keyword-only
parameters are the default for anything with more than two arguments (config.py 202-213).

One domain value is a native subtype: `class PositiveIdentifier(int):` with `__slots__ = ()`
(hamsterdan2/github_app/models.py 57-60), `DeliveryId`, `RepositoryFullName`,
`ProviderRouteId` (tests2/test_webhook_inbox_intake.py 17-23). Pydantic is the shape authority at
the boundary and nowhere else: `class GitHubRepository(BaseModel): model_config =
ConfigDict(extra="ignore", frozen=True, strict=True)` (hamsterdan2/github_app/models.py 82-86).
Private names are the one place the two trees disagree: V5 uses `_credentials`,
`_compose_agent_runtime`, `_positive_decimal` (config.py 27, 250; __main__.py 237); the
replacement gate bans underscore methods and underscore dataclass fields outright
(quality/hamsterdan2/rules/no-underscore-methods.yml 6-9, no-underscore-dataclass-fields.yml
6-8), and the conventions say the V5 tree is not retrofitted (engineering-conventions.md 107).

**Packaging, config, tooling.** 2026. Build backend `hatchling==1.31.0` (pyproject.toml 38-40);
`uv` with `exclude-newer = "2026-08-15T10:57:40Z"` so resolution cannot drift (uv.toml 1-2) and
`export UV_FROZEN=1` in every check (scripts/check 7); `.python-version` is `3.14.7`. Runtime
dependencies are six, each with an upper bound or an exact pin: `fastapi>=0.116,<1`,
`githubkit[auth-app]==0.16.0`, `petrus @ git+https://...@89baf78...` (12-19). Dev group:
`ruff`, `ty==0.0.63`, `mutmut==3.6.0`, `hypothesis`, `ast-grep-cli`, `pytest-randomly`,
`pytest-timeout`, `pytest-xdist` (21-36). Ruff: line length 120, target py314, mccabe 10 (68-73);
the replacement gate selects `ALL` with eleven documented ignores and mccabe 4
(quality/hamsterdan2/ruff.toml 6-19, 36-37). CI is one job: `uv sync --frozen` then
`scripts/check tests` (.github/workflows/ci.yml 19-21). No Makefile; `scripts/check` is the
Makefile, and `tests/test_check_command.py` pins its exact command lines (77-82, 92-103).

Configuration is read from the environment by hand, in `HostConfig.from_environment`
(src/hamsterdan/github_app/config.py 229-248): each key goes through a validator that raises
`ConfigurationError` (`_positive_decimal`, `_slug`, `_identifier`, `_secret`, 27-60), retired
keys are rejected by name (232-235), and the secrets are popped from `os.environ` right after
the read (host/__main__.py 220-221, 233). A second read lives in `__main__.py` with string
defaults cast by hand: `int(os.getenv("HAMSTERDAN_PORT", "8000"))` (202),
`float(os.getenv("HAMSTERDAN_REMINDER_SECONDS", "259200"))` (245); a third in
`QualificationFault.from_environment` (host/service.py 64-77). Every `from_environment` takes
`environment: Mapping[str, str] | None = None` so tests pass a dict (config.py 230-231).
Neither `python-decouple` nor `pydantic-settings` appears anywhere in the repository. Secrets
come from 1Password Environments through `scripts/with-runtime-secrets` (AGENTS.md 94-99);
`.envrc` holds selectors only (118-119).

**README voice.** First sentence: `Hamsterdan is a GitHub-native PR-readiness application
powered by Petrus.` (README.md 3-4). The promise is bounded immediately: `This is an early
source publication` (8), `Public CI remains disabled` (10), `Hamsterdan never merges.` (72-73).
There is no worked example; instead an ASCII architecture diagram (38-49), the shortest
maintainer path through one reconciliation (58-66), and a "Start with:" list of five files
(79-85). The docs explain themselves in the same register: `This document owns reusable
implementation practice for Hamsterdan.` (docs/process/engineering-conventions.md 3) and
`Promote mechanically checkable structure into the repository quality gate when one clear test
owner can enforce it.` (11-12).

**What this repo adds to the KB.**

- erros-na-fronteira: convention 4 `Normalize provider data at the boundary. ... Do not let SDK
  or HTTP types cross into contracts, readiness, or the Net. A third-party library gets exactly
  one boundary module; code above it speaks domain vocabulary and cannot tell which library is
  underneath.` (engineering-conventions.md 30-34) and convention 27 `Domain logic raises and
  returns; only the rim ... prints, exits, renders, or touches the network.` (154-156);
  enforced by tests/test_architecture.py 144-158. The mapping to HTTP is per route
  (src/hamsterdan/host/api.py 46-49; src/hamsterdan2/host/api.py 29-34, 51-59), not one
  registered handler; see pattern `excecao-para-http`.
- httpstatus-em-vez-de-numeros-magicos: `status.HTTP_202_ACCEPTED` on the route decorator
  (src/hamsterdan/host/api.py 38) next to `HTTPException(status_code=400, ...)` (44, 49);
  the replacement tree uses only `status.HTTP_*` (src/hamsterdan2/host/api.py 31, 49, 61).
  Pattern `status-com-httpstatus` now carries this as its fastapi rendition.
- o-verbo-comanda: `@app.get("/healthz")` and `@app.post("/github/webhooks", ...)`
  (src/hamsterdan/host/api.py 34, 38); noun paths, the method is the verb. Pattern
  `verbo-por-rota`, fastapi rendition.
- prefira-excecoes-a-booleanos: convention 43 `Conditions worth naming get a type, and business
  errors get their hierarchy from the start: a base domain exception ... with the named outcomes
  as its empty subclasses` (204-208) and `Routing them IS the business rule.` (209);
  src/hamsterdan2/host/webhook_inbox.py 59-76.
- evite-ciclos-busque-a-arvore: convention 42 `Imports live at the top of the module. ... In
  src/hamsterdan2 the ban is outright: a cycle means the module graph is wrong.` (196-200);
  rule quality/hamsterdan2/rules/no-function-local-imports.yml 6 `A cycle means the module graph
  is wrong; fix the graph.`; cycle test tests2/test_architecture.py 95-110; sibling isolation
  tests/test_architecture.py 62-72.
- componha-em-vez-de-herdar: `Mixins are banned. Compose different types and aggregate types`
  (quality/hamsterdan2/rules/no-adhoc-mixins.yml 6-8); convention 36 `the base class exists only
  for what it truly shares; composition is a module-constant tuple; no ABC, no registration
  framework.` (179-181); convention 20's ladder, bare container, inherit it, encapsulate it
  (119-131), is the criterion for when extending a built-in is honest.
- uma-responsabilidade-por-identidade: convention 6 `Use a function for a narrow operation with
  little state. Use an object when bound state materially reduces the interface or enforces an
  invariant. No utils.py or helpers.py` (41-44); convention 48 `a method name never repeats its
  class name` (237).
- o-codigo-e-a-interface: convention 47 `Tell, don't ask: internal state is revealed through
  predicate methods ... never by exporting its representation for callers to compare.`
  (229-231), enforced by tests2/test_enum_privacy.py 45-48; convention 49 `The public interface
  of a class reads like a clear sentence` (239-241).
- camada-de-servico: convention 5 `Keep CLIs, servers, workers, and transports as thin adapters
  over importable operations.` (35-38); the route body is `return service.health()` and one call
  to `service.custody.receive` (src/hamsterdan/host/api.py 36, 47).
- configuracao-fora-do-codigo: convention 18 `Effect sources (randomness, environ, clock, sleep,
  paths, secrets) enter as keyword-default parameters that tests override; never a DI
  framework.` (98-100; the parentheses replace his dashes); convention 12 `Credentials are
  opaque, redacted, host-owned values.` (67); `HostConfig.from_environment`
  (src/hamsterdan/github_app/config.py 229-248). The tool differs from the course (no
  `python-decouple`); see Caveats.
- teste-primeiro-das-folhas: `1. Add one behavioral test and confirm the intended failure. 2.
  Make the smallest correct implementation pass it. 3. Refactor under the focused test`
  (docs/process/development-guide.md 60-62); convention 13 `Test public behavior and the reason
  it matters rather than incidental helper decomposition.` (74-75); convention 14 `Fake only the
  expensive or nondeterministic seam; use real objects everywhere else.` (78-79).
- nao-projete-a-generalizacao and postergue-decisoes: convention 43 `Beyond the base, the deeper
  hierarchy is a nudge, not a mandate: grow it as usage reveals the need` (212-214); convention
  24 `Use a dataclass only where it removes real boilerplate, never as a category default.`
  (141-142); convention 66 `every new dependency is justified by what the stdlib cannot do.`
  (296-297); product principle 6 `add live reload only after its atomic authority replacement
  semantics are proven necessary.` (docs/product/principles.md 19-20).
- pragmatismo-sobre-pureza: convention 17's complexity tiers, at most 10, review from 11 to 15,
  documented exception above (89-93); convention 63 `Guidance, not a blanket mandate.` (291);
  convention 44 `failure becomes persisted state instead of an exception taxonomy, a
  design-dependent variant, not a preference reversal.` (216-218).
- escolha-a-regra-mais-simples: the typed-data ladder `the wider a piece of data travels, the
  stronger its shape must be. First match wins` (311-312) ending with `A primitive, return it
  bare.` (330).
- representacao-nao-e-codificacao: convention 26 `Pydantic models are shape authority for
  external input and serialized output, never the internal default.` (148-150);
  `WebhookRefusalResponse(refusal=reason).model_dump(mode="json")` (src/hamsterdan2/host/api.py
  33).
- a-interface-e-o-que-importa: convention 45 `An error message is part of the API: name the
  fix, list what was expected and what is available.` (219-220).
- deixe-o-codigo-descansar: convention 62 `a golden master is the cheapest one when refactoring
  working code.` (285-286); `The existing V5 tree is not retrofitted.` (107).
- Pattern files amended: `kb/patterns/status-com-httpstatus.md` (fastapi rendition replaced with
  his), `kb/patterns/verbo-por-rota.md` (fastapi rendition replaced with his),
  `kb/patterns/excecao-para-http.md` (translated rendition kept; note on his per-route mapping
  added).

**Caveats.**

- Bare status integers where the course says never: `raise HTTPException(status_code=400,
  detail="request body is too large")` and `raise HTTPException(status_code=400,
  detail=str(error)) from None` (src/hamsterdan/host/api.py 44, 49), four lines after
  `status_code=status.HTTP_202_ACCEPTED` (38). The tests assert bare numbers too: `assert
  response.status_code == 202` (tests/integration/host/test_service.py 402, 406, 408, 450) and
  `assert response.status_code == 200` (tests2/test_webhook_inbox_intake.py 185, 291, 324, 423).
  `http.HTTPStatus` is never imported in this repository; `fastapi.status` is the only named form.
- No exception handler at the boundary. The course's shape is one table from exception type to
  status; here each route catches and maps inline (src/hamsterdan/host/api.py 46-49;
  src/hamsterdan2/host/api.py 51-59). With two routes the cost is small, and `refusal_response`
  (29-34) is already the table in function form.
- Configuration is read in three places, not one, and without a declared cast: `HostConfig.from_environment`
  (src/hamsterdan/github_app/config.py 229-248), `os.getenv` with manual `int()` and `float()`
  in host/__main__.py 201-202 and 244-245, and `QualificationFault.from_environment`
  (host/service.py 64-77). The principle's tool, `python-decouple`, is absent; rule
  `project.environ-without-decouple` would not fire because the dependency is absent, and the
  judgment finding stands.
- Convention 55 (`The README develops one realistic worked example, and a test executes that
  example verbatim`, engineering-conventions.md 261-262) is not met by this repository's own
  README, which has no example (README.md 1-141).
- Module size: `src/hamsterdan/contracts/readiness_v5.py` is 1,491 lines and
  `src/hamsterdan/host/testing/readiness_world.py` 1,715; `operator.py` 1,269. Whether each
  holds one identity is a judgment call; the conventions themselves say `split responsibilities
  before provider, workflow, and hosting concerns accumulate in one module` (39-41).
- V5 uses `typing.Protocol` in 11 modules and underscore-private helpers throughout, both of
  which the replacement gate disfavors or bans (engineering-conventions.md 193-195;
  quality/hamsterdan2/rules/no-underscore-methods.yml). He states the gap himself: `The existing
  V5 tree is not retrofitted.` (107).
- The test docstrings in the V5 unit suite are long narratives, 21 lines on one module and 11
  on one fake (tests/unit/host/test_v5_rerun.py 1-21, 47-57), against convention 54
  `Docstrings are rare and load-bearing` (259-260) and 57 `near-zero comments` (271).
