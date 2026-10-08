---
repo: henriquebastos/requests-pro
commit: cd280f025041c8352823ee6aa5b77c09ddee3cf0
era: 2024 to 2026
license: MIT
class: his
---
# requests-pro

**What it is.** A framework for building API clients on top of `requests`: a session that
absorbs base URL, JSON encoding and decoding, custom response class and timeout; an auth
object that renews its token lazily and retries once on 401; a token store over any cache; an
audit adapter that records every exchange; and a two-line `Client` whose seven verbs are
`partialmethod`. Version 1.0.0 on PyPI as `requests-pro` (`pyproject.toml` line 21), about 530
lines in seven modules under `src/requestspro/`, src layout, `requests` as the only runtime
dependency. It is lesson 7 of Design de API na Prática taken to a product (API digest sections
14.1 and 15.1). The GitHub repository dates from 2024-08-08 (manifest); the git history starts
on 2025-05-11 with "Importing source code" (`99a438b`), 18 commits, the last on 2026-08-28.
Sponsored by Routable (`README.md` lines 44 to 48). Since 2026-06-12 (`ffe618d` "docs: adopt
Ariad as the development method") it carries `AGENTS.md` and a `docs/` tree with briefing,
decisions, a debt ledger, a worklog and product principles, written for coding agents.

**Layout.**

```
src/requestspro/
  __init__.py          empty: no public surface declared
  client.py            Client (request plus seven partialmethod verbs, 6 to 23); MainClient with
                       audit and the from_credentials contract (26 to 40)
  sessions.py          BaseSession with timeout (10 to 23); BaseUrlSession (26 to 45);
                       CustomResponseSession (48 to 65); ProResponse (68 to 82);
                       CustomJsonSession (85 to 168); ProSession composing the three (171 to 209)
  auth.py              RecoverableAuth: authorize, token property with lazy renew, handle_401
  token.py             ExpireValue, an expiring in-memory value (6 to 30); TokenStore, a callable
                       over a cache-like object (33 to 55)
  audit.py             AuditDict TypedDicts (10 to 32); Audit adapter decorator (38 to 113);
                       httplog (116 to 141)
  audit_for_django.py  an audit entry built from a Django HttpRequest
  utc.py               UTC and utc_now
demo/eduzz.py          the canonical client: error, response, session, auth, main client, subclients
tests/                 conftest.py with the responses fixture; eight modules, one per concern
docs/                  project/briefing, decisions, debt, roadmap; process/development-guide,
                       worklog; product/principles
AGENTS.md, .agents/setup, pyproject.toml, uv.lock, .pre-commit-config.yaml,
.github/workflows/{push,lint,test,publish,claude,claude-code-review}.yml
```

**How he tests.** pytest 8.3 or later, `responses` for HTTP, `freezegun` and an injected `now`
for time, `unittest.mock` where a double is needed (`pyproject.toml` lines 9 to 16).
`tests/conftest.py` lines 5 to 8 yield a `responses.RequestsMock(assert_all_requests_are_fired=False)`.
Tests are grouped in `TestX` classes named after the behavior, with given/when/then comments
(`tests/test_client.py` lines 10 to 18; `tests/test_session_json.py` lines 84 to 107),
`pytest.mark.parametrize` for variants (the seven verbs, `tests/test_client.py` lines 55 to
65; float and tuple timeouts, `tests/test_session_timeout.py` lines 51 to 70), sample
subclasses declared in the test module (`SampleAuth`, `tests/test_auth.py` lines 18 to 20;
`SampleClient`, `tests/test_audit.py` lines 38 to 46), and a hand-rolled
`CannedAdapter(BaseAdapter)` when `responses` would consume the stream under test
(`tests/test_audit.py` lines 155 to 171, reason in the docstring). The house style is written
down in `docs/process/development-guide.md` line 38: "given/when/then comments, small `TestX`
classes per behavior, `pytest.mark.parametrize` for variants, `responses` for HTTP mocking,
`freezegun`/injected `now` for time." 41 tests (`docs/project/briefing.md` line 18). Not
tested: `demo/eduzz.py` and `audit_for_django.py`.

**How he handles errors.** The package declares no exception class. `Client.request` calls
`response.raise_for_status()` and returns the decoded JSON or `None` on an empty body
(`src/requestspro/client.py` lines 12 to 15), so `requests.HTTPError` is what a consumer
catches. `handle_401` retries the request once with a fresh session and then
`raise_for_status()` on the second answer (`src/requestspro/auth.py` lines 58 to 78).
`NotImplementedError` marks the two methods a subclass must write, `renew` (`auth.py` lines
43 to 44) and `from_credentials` (`client.py` lines 33 to 40). A `ValueError` from
`json.dumps` is re-raised as `InvalidJSONError` (`sessions.py` lines 155 to 158). Translating
the API's error envelope is the concrete client's job: the demo's `EduzzResponse.raise_for_status`
reads `code` and `details` and raises `EduzzAPIError(RequestException)` when the status is in
`ERROR_STATUSES` (`demo/eduzz.py` lines 51 to 72), and the decisions log places the next
translation, client exception to domain exception, in a service layer
(`docs/project/decisions.md` lines 51 to 60).

**Naming and interface.** Mixins named by the concern they add, `BaseUrlSession`,
`CustomJsonSession`, `CustomResponseSession`, composed in one line into `ProSession`
(`sessions.py` line 171); `Pro` marks the assembled classes (`ProSession`, `ProResponse`).
Configuration is an uppercase class attribute with an instance override: `TIMEOUT`, `BASE_URL`,
`RESPONSE_CLASS`, `JSON_ENCODER`, `SESSION_CLASS` (`sessions.py` lines 13, 29, 49, 88 to 93;
`auth.py` line 6). `TokenStore` is a callable: `store()` reads, `store(value, expires_in)`
writes (`token.py` lines 46 to 51). Factories are classmethods, `Audit.for_session`
(`audit.py` lines 45 to 50), `TokenStore.in_memory` (`token.py` lines 53 to 55),
`EduzzClient.from_credentials` (`demo/eduzz.py` lines 118 to 123). `httplog` is a plain
function returning a `TypedDict` (`audit.py` lines 116 to 141). Private helpers carry an
underscore: `_recover`, `_recovery_request`, `_safe_get_request_body`, `_cast_response`.
Two properties are labeled "For testing purpose only." (`auth.py` lines 33 to 41). Docstrings
explain mechanism, for instance the four steps by which `requests` prepares a body and where
the override intervenes (`sessions.py` lines 122 to 135). `__init__.py` is empty; consumers
import from modules (`demo/eduzz.py` lines 34 to 38).

**Packaging, config, tooling.** 2026. Build backend `setuptools>=77` (`pyproject.toml` lines 1
to 3), `[project]` with `requires-python = ">=3.10"` and `requests >= 2.32.3` as the only
dependency (lines 35 to 38), `[dependency-groups]` for uv with `dev` and `demo` (lines 5 to 16),
`uv.lock` committed and installed with `uv sync --locked --all-extras --dev`
(`.github/workflows/test.yml` line 21; `.agents/setup` lines 11 to 12, uv pinned to 0.12.7 on
line 5). Ruff with `select = ["ALL"]` and an ignore list (lines 82 to 85), line length 120,
`target-version = "py312"` (lines 62 to 64), isort sections with a `testing` section so pytest,
responses and freezegun are imported after the subject (lines 66 to 80). pre-commit runs ruff
v0.11.9 with `--fix` and `ruff-format` (`.pre-commit-config.yaml` lines 22 to 27). Push runs
lint then test on 3.10 to 3.13 (`push.yml`; `test.yml` line 11); a GitHub release runs both and
publishes with trusted publishing (`publish.yml` lines 17 to 22, 35). Claude PR assistant and
code-review workflows were added on 2025-07-30 (`6de7c67`, `f246122`). No settings or secrets
in the package; the demo takes credentials from argparse with `os.getenv` defaults
(`demo/eduzz.py` lines 176 to 178).

**README voice.** "RequestsPro is the easy way to build professional-grade API clients."
(`README.md` line 3), then eight "Key features" that lead with "Transparent" (lines 7 to 14)
and a quick start that is one pointer: "Check the demo/eduzz.py to see a simple yet complete
API client example." (line 18). Contributing: "Pull requests are welcome and must have
associated tests." (line 32). The thesis is in the demo's docstring: "The Client and
SubClients are simple because we handled all the API crazyness before, so they are just thin
wrappers around the API." (`demo/eduzz.py` lines 24 to 25). The 2026 docs restate it as
"Endpoints stay trivial" and "Composable over configurable" (`docs/product/principles.md`
lines 7 to 9 and 19 to 21). The README has the License section twice (lines 26 to 28 and 36 to
38) and the typos "conserns" and "Extremelly" (lines 13 to 14).

**What this repo adds to the KB.**
- a-interface-e-o-que-importa: `src/requestspro/client.py` 6 to 23 and `demo/eduzz.py` 132 to
  167; pattern cliente-de-api-profissional (existing).
- representacao-nao-e-codificacao: `src/requestspro/sessions.py` 85 to 120 chooses the encoder
  once per session and recommends jsonstar (184 to 202); pattern serializacao-de-tipos
  (existing, cites the recommendation).
- componha-em-vez-de-herdar: `ProSession` built from three mixins (`sessions.py` 171); `Audit`
  wraps an adapter instead of subclassing `HTTPAdapter` (`audit.py` 38 to 62); composition is
  explicit in `from_credentials` (`demo/eduzz.py` 118 to 123).
- erros-na-fronteira: the envelope is translated once in `EduzzResponse.raise_for_status`
  (`demo/eduzz.py` 58 to 72); `docs/project/decisions.md` 51 to 60.
- uma-responsabilidade-por-identidade: one module per concern; `token.py` 33 to 55 is a store
  that knows nothing about HTTP.
- teste-primeiro-das-folhas: the written house style, `docs/process/development-guide.md` 38.
- nao-projete-a-generalizacao: "A workaround that a concrete client has to hand-roll is a
  roadmap signal, not a permanent resident." (`docs/product/principles.md` line 29); open
  questions stay open in `docs/project/decisions.md` 73 to 101.
- No new pattern file from this repo in this pass.

**Caveats.**
- Status codes as bare integers. `if response.status_code != 401:` (`src/requestspro/auth.py`
  line 62); `assert r.status_code == 200` (`tests/test_auth.py` line 62;
  `tests/test_session_timeout.py` lines 70, 84, 98); `== [401, 401]` (`tests/test_audit.py`
  line 105); `d["response"]["status_code"] == 200` (`tests/test_audit.py` line 129);
  `status=201` as a default parameter (`src/requestspro/audit_for_django.py` line 20);
  `ERROR_STATUSES = {400, 401, 403, 404, 405, 409, 422, 500}` (`demo/eduzz.py` line 61). Rule
  `api.magic-status` fires on each; the `responses.add(status=...)` mocks are not flagged. His
  own lesson 5 replaced magic numbers with `http.HTTPStatus`; this package never imports it.
- The declared floor is Python 3.10, but `type HttpHeaders = dict[str, str]`
  (`audit_for_django.py` line 10) is 3.12 syntax and ruff targets py312; the module fails to
  import on 3.10 and 3.11. His ledger carries it as D-003 (`docs/project/debt.md` line 23).
- `patch.object(auth, "renew", return_value=("EXPIRED2", -1))` is never started
  (`tests/test_auth.py` line 71); `test_auth_dont_recover_twice` passes for another reason
  (D-009, `debt.md` line 29). A test that does not test what its name promises.
- `response.__class__ = response_class` (`sessions.py` line 64), called "Magic" in its own
  docstring, skips `__init__` and makes the mixin order load-bearing (D-005).
- `BaseSession.__init__` swallows unknown keyword arguments (`sessions.py` lines 15 to 17);
  `InvalidJSONError(ve, request=self)` passes the session as the request (line 158);
  `handle_401` has a dead `recover_401` parameter (`auth.py` line 58) and retries with the
  stored token without invalidating it first (D-007, D-011).
- The demo, "the recipe's exhibit" (`docs/process/development-guide.md` line 50), discards
  the result of `dt.replace(tzinfo=SAO_PAULO)` (`demo/eduzz.py` line 108), so the token TTL
  is computed in the wrong timezone; argparse positionals with `default=` never fall back to
  the environment (lines 176 to 178); it has no tests (D-010). It reads credentials with
  `os.getenv` rather than his own decouple.
- `Audit.events` grows without bound and headers are recorded unredacted (D-004).
- CI was red on every push from 2025-07-31 to 2026-06-12 because the lint job failed and
  blocked tests and releases (`docs/project/briefing.md` line 18).
