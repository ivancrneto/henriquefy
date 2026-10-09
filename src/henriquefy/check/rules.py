"""Per-file mechanical rules. Each rule maps to a principle id in kb/principles/.

A rule is a function (tree, source_lines, context) -> list[Finding]. Rules are deliberately
narrow: they fire only on a syntactic shape that is wrong on its face. Everything that needs
judgment stays with the agent, as PLAN.md section 3 says.
"""

import ast
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from pathlib import Path

STATUS_KWARGS = {"status", "status_code"}
RESPONSE_CALL = re.compile(r"(Response|HTTPException|^render$|^abort$|^redirect$)$")
VERB_SEGMENT = re.compile(
    r"^(create|update|delete|remove|get|set|add|list|fetch|edit|save|new)([_-][a-z0-9_-]+)?$"
)
ROUTE_CALLS = {"path", "re_path", "url", "route", "add_api_route", "api_route"}
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}
BROAD_EXCEPTIONS = {"Exception", "BaseException"}
ENV_NAMES = {"environ", "getenv"}
ENV_WRITES = {"setdefault", "update"}
ASSERT_EQUALS = {"assertEqual", "assertEquals", "assertNotEqual", "assertNotEquals"}
ASSERT_PREFIX = "assert"
CLASS_METHOD_LIMIT = 15
SCOPES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)


@dataclass(frozen=True)
class Rule:
    id: str
    principle: str
    title: str
    detect: str
    fix: str
    scope: str = "file"  # file | repo


@dataclass
class Finding:
    rule: str
    path: str
    line: int
    message: str
    col: int = 0


@dataclass
class Context:
    path: Path
    root: Path
    is_test: bool
    depends_on_decouple: bool
    extra: dict = field(default_factory=dict)


RULES: dict[str, Rule] = {}
_IMPLS: dict[str, Callable[[ast.AST, list[str], Context], Iterable[Finding]]] = {}


def rule(id: str, principle: str, title: str, detect: str, fix: str, scope: str = "file"):
    def register(fn):
        RULES[id] = Rule(id, principle, title, detect, fix, scope)
        _IMPLS[id] = fn
        return fn

    return register


def _f(rule_id: str, ctx: Context, node: ast.AST, message: str) -> Finding:
    return Finding(
        rule_id, str(ctx.path), getattr(node, "lineno", 0), message, getattr(node, "col_offset", 0)
    )


@rule(
    "api.magic-status",
    "httpstatus-em-vez-de-numeros-magicos",
    "HTTP status as a bare integer",
    "An integer literal from 100 to 599 passed as `status=` or `status_code=`, or as a "
    "positional argument, to a response or HTTP error constructor (`JsonResponse(data, 201)`, "
    "`HttpResponse(body, 200)`, `HTTPException(404, ...)`, `abort(404)`, `render`, ...), or "
    "assigned to `status_code` (as a class attribute anywhere, annotated or not, as an attribute "
    "outside tests), or compared with a `.status_code` attribute (`!= 401`, `== 200`, "
    "`in (200, 201)`, `self.assertEqual(resp.status_code, 200)`, `assertNotEqual`, tests "
    "included). "
    "A mock like `responses.add(status=200)` or a fake `Response(body, 200)` built in a test "
    "file describes someone else's reply and is not flagged; tests are flagged for "
    "comparisons and `assertEqual` only.",
    "Use `http.HTTPStatus.<NAME>` (or `fastapi.status`) so the code reads as the status name.",
)
def magic_status(tree, lines, ctx):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _builds_response(node) and not ctx.is_test:
            for kw in node.keywords:
                if kw.arg in STATUS_KWARGS and _is_status_int(kw.value):
                    yield _f("api.magic-status", ctx, kw.value, f"{kw.arg}={kw.value.value}")
            for arg in node.args:
                if _is_status_int(arg):
                    yield _f("api.magic-status", ctx, arg, f"{_callee(node)}(..., {arg.value})")
        elif isinstance(node, ast.Call) and _callee(node) in ASSERT_EQUALS:
            pair = node.args[:2]
            if any(_is_status_attr(a) for a in pair):
                for a in pair:
                    if _is_status_int(a):
                        yield _f(
                            "api.magic-status",
                            ctx,
                            a,
                            f"{_callee(node)}(status_code, {a.value})",
                        )
        elif isinstance(node, ast.Assign | ast.AnnAssign) and _is_status_int(node.value):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(_is_status_target(t, ctx.is_test) for t in targets):
                yield _f("api.magic-status", ctx, node.value, f"status_code = {node.value.value}")
        elif isinstance(node, ast.Compare):
            operands = [node.left, *node.comparators]
            if any(_is_status_attr(o) for o in operands):
                for o in operands:
                    group = o.elts if isinstance(o, ast.Tuple | ast.List | ast.Set) else [o]
                    for item in group:
                        if _is_status_int(item):
                            yield _f(
                                "api.magic-status",
                                ctx,
                                item,
                                f"status_code compared with {item.value}",
                            )


def _is_status_attr(node: ast.AST) -> bool:
    return isinstance(node, ast.Attribute) and node.attr == "status_code"


def _builds_response(call: ast.Call) -> bool:
    """Calls that build a response or an HTTP error the code emits. A mock such as
    `responses.add(..., status=200)` describes someone else's reply and is not flagged."""
    name = _callee(call) or ""
    return bool(RESPONSE_CALL.search(name))


def _is_status_target(target: ast.AST, is_test: bool) -> bool:
    """`status_code = 201` as a class attribute anywhere; `resp.status_code = 404` only outside
    tests, where a fake `Response()` being set up is fixture data, not a response the code emits."""
    if isinstance(target, ast.Name) and target.id == "status_code":
        return True
    return isinstance(target, ast.Attribute) and target.attr == "status_code" and not is_test


def _is_status_int(node) -> bool:
    return (
        isinstance(node, ast.Constant) and isinstance(node.value, int) and 100 <= node.value <= 599
    )


@rule(
    "errors.bare-except",
    "prefira-excecoes-a-booleanos",
    "Bare or broad except that swallows the failure",
    "`except:` or `except Exception/BaseException:` whose body does not re-raise.",
    "Catch the specific exception you can handle; let the rest propagate.",
)
def bare_except(tree, lines, ctx):
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler) and _is_broad(node.type) and not _reraises(node):
            what = "except:" if node.type is None else f"except {ast.unparse(node.type)}:"
            yield _f("errors.bare-except", ctx, node, what)


def _is_broad(node) -> bool:
    if node is None:
        return True
    if isinstance(node, ast.Name):
        return node.id in BROAD_EXCEPTIONS
    if isinstance(node, ast.Tuple):
        return any(_is_broad(e) for e in node.elts)
    return False


def _reraises(handler: ast.ExceptHandler) -> bool:
    return any(isinstance(n, ast.Raise) for n in _walk_local(handler))


def _walk_local(node: ast.AST):
    """ast.walk that stays in the current scope: a nested def, lambda or class runs later,
    so its `raise` or `return` is not the handler's."""
    todo = [node]
    while todo:
        n = todo.pop()
        yield n
        for child in ast.iter_child_nodes(n):
            if not isinstance(child, SCOPES):
                todo.append(child)


@rule(
    "errors.bool-in-except",
    "prefira-excecoes-a-booleanos",
    "Failure turned into a boolean",
    "`return False`, `return None` or a bare `return` inside an `except` handler.",
    "Let the exception propagate, or raise a specific domain exception the caller can name.",
)
def bool_in_except(tree, lines, ctx):
    seen: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            for inner in _walk_local(node):
                if isinstance(inner, ast.Return) and _is_false_or_none(inner.value):
                    if id(inner) in seen:
                        continue
                    seen.add(id(inner))
                    what = "return" if inner.value is None else f"return {ast.unparse(inner.value)}"
                    yield _f("errors.bool-in-except", ctx, inner, what)


def _is_false_or_none(node) -> bool:
    """`return False`, `return None`, or a bare `return` (no value), which returns None."""
    if node is None:
        return True
    return isinstance(node, ast.Constant) and (node.value is False or node.value is None)


@rule(
    "readability.mutable-default",
    "o-codigo-e-a-interface",
    "Mutable default argument",
    "A list, dict or set literal (or call to list/dict/set) as a parameter default, in a "
    "`def` or a `lambda`.",
    "Default to `None` and build the value inside the function, or use an immutable default.",
)
def mutable_default(tree, lines, ctx):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef | ast.Lambda):
            defaults = node.args.defaults + node.args.kw_defaults
            for d in defaults:
                if d is not None and _is_mutable_literal(d):
                    yield _f("readability.mutable-default", ctx, d, f"default {ast.unparse(d)}")


def _is_mutable_literal(node) -> bool:
    if isinstance(node, ast.List | ast.Dict | ast.Set | ast.ListComp | ast.DictComp | ast.SetComp):
        return True
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"list", "dict", "set"}
    )


@rule(
    "testing.no-assert",
    "teste-primeiro-das-folhas",
    "Test without an assertion",
    "A `test_*` function or method that pytest collects (not one nested inside another "
    "function) with no `assert` statement, no call to an attribute whose name starts with "
    "`assert`, and no `pytest.raises`/`pytest.warns` block.",
    "Assert the behavior the test name promises, or delete the test.",
)
def no_assert(tree, lines, ctx):
    if not ctx.is_test or ctx.path.name == "conftest.py":
        return
    for node in _collectable_functions(tree):
        if not node.name.startswith("test"):
            continue
        if any("fixture" in ast.unparse(d) for d in node.decorator_list):
            continue
        if not any(_is_assertion(n) for n in ast.walk(node)):
            yield _f("testing.no-assert", ctx, node, f"{node.name} asserts nothing")


def _collectable_functions(tree: ast.AST):
    """Functions at module or class level; a `def test_helper()` inside a test is not a test."""
    todo = [tree]
    while todo:
        n = todo.pop()
        for child in ast.iter_child_nodes(n):
            if isinstance(child, ast.FunctionDef | ast.AsyncFunctionDef):
                yield child
            elif not isinstance(child, ast.Lambda):
                todo.append(child)


def _is_assertion(node) -> bool:
    if isinstance(node, ast.Assert):
        return True
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        name = node.func.attr
        return name.startswith(ASSERT_PREFIX) or name in {"raises", "warns", "fail"}
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        return node.func.id in {"raises", "warns", "fail"}
    if isinstance(node, ast.With):
        for item in node.items:
            call = item.context_expr
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute):
                if call.func.attr in {"raises", "warns", "assertRaises"}:
                    return True
    return False


@rule(
    "project.environ-without-decouple",
    "configuracao-fora-do-codigo",
    "Environment read directly in a project that uses python-decouple",
    "A configuration read from the environment, `os.environ[...]`, `os.environ.get(...)` or "
    "`os.getenv(...)`, also through `from os import environ, getenv`, in a project whose "
    "dependencies include `python-decouple`. Writes are not reads: an assignment or `del` on "
    "`os.environ[...]`, `os.environ.setdefault(...)` (Django's settings bootstrap in manage.py, "
    "wsgi.py and asgi.py), `os.environ.update(...)`, and `mock.patch.dict(os.environ, ...)` or "
    "`monkeypatch.setitem(os.environ, ...)` in a test.",
    "Read it through `decouple.config(...)`, with a cast and a default, in one place.",
)
def environ_without_decouple(tree, lines, ctx):
    if not ctx.depends_on_decouple:
        return
    imported = {
        alias.asname or alias.name: alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module == "os"
        for alias in node.names
        if alias.name in ENV_NAMES
    }

    def env(node) -> str | None:
        """`os.environ`, `os.getenv`, or a name imported from them; None for anything else."""
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id == "os" and node.attr in ENV_NAMES:
                return f"os.{node.attr}"
        if isinstance(node, ast.Name) and node.id in imported:
            return imported[node.id]
        return None

    writes: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in ENV_WRITES and env(node.func.value):
                writes.add(id(node.func.value))
            if node.func.attr == "dict" and _callee_name(node.func.value) == "patch":
                writes |= {id(a) for a in node.args if env(a)}
            if node.func.attr in {"setitem", "delitem"}:  # monkeypatch.setitem(os.environ, ...)
                writes |= {id(a) for a in node.args if env(a)}
        elif isinstance(node, ast.Subscript) and isinstance(node.ctx, ast.Store | ast.Del):
            if env(node.value):
                writes.add(id(node.value))
    for node in ast.walk(tree):
        what = env(node)
        if what and id(node) not in writes:
            yield _f("project.environ-without-decouple", ctx, node, what)


def _callee_name(node) -> str | None:
    return node.attr if isinstance(node, ast.Attribute) else getattr(node, "id", None)


@rule(
    "modeling.class-size",
    "uma-responsabilidade-por-identidade",
    "Class with too many methods",
    f"A class defining more than {CLASS_METHOD_LIMIT} methods, counted by name: a property "
    "setter or an `@overload` stub is the same method again.",
    "Find the second identity hiding in the class and give it its own name.",
)
def class_size(tree, lines, ctx):
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = {
                n.name for n in node.body if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef)
            }
            if len(methods) > CLASS_METHOD_LIMIT:
                yield _f(
                    "modeling.class-size", ctx, node, f"{node.name} has {len(methods)} methods"
                )


@rule(
    "api.verb-in-uri",
    "o-verbo-comanda",
    "Verb in the URI",
    "A route you define whose segment is a verb (create, update, delete, get, set, list, ...): "
    "`path()`, `re_path()`, `route()` calls, or `@app.<method>()` / `@router.<method>()` "
    "decorators. Client calls to someone else's URIs are not flagged.",
    "Name the resource in the URI and let the HTTP method carry the verb.",
)
def verb_in_uri(tree, lines, ctx):
    """Route definitions only: `path()`-style calls anywhere, `@app.<method>(...)` and
    `@router.<method>(...)` only as decorators. A client calling `session.get("/get_me")`
    does not own that URI and is never flagged."""
    seen: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            for deco in node.decorator_list:
                if isinstance(deco, ast.Call) and _callee(deco) in HTTP_METHODS:
                    yield from _route_findings(deco, ctx, seen)
        elif isinstance(node, ast.Call) and _callee(node) in ROUTE_CALLS:
            yield from _route_findings(node, ctx, seen)


def _callee(call: ast.Call) -> str | None:
    func = call.func
    return func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", None)


def _route_findings(call: ast.Call, ctx: Context, seen: set[int]):
    if not call.args or id(call) in seen:
        return
    seen.add(id(call))
    first = call.args[0]
    if not (isinstance(first, ast.Constant) and isinstance(first.value, str)):
        return
    if any(VERB_SEGMENT.match(seg) for seg in re.split(r"[/^$]", first.value)):
        yield _f("api.verb-in-uri", ctx, first, f"'{first.value}'")


@rule(
    "modeling.local-import",
    "evite-ciclos-busque-a-arvore",
    "Project import inside a function",
    "An `import` or `from ... import` of a relative module or of a top-level package of the "
    "target placed inside a function or method body, which usually dodges an import cycle.",
    "Move the import to the top of the module; if that fails with a cycle, invert the dependency "
    "that creates it.",
)
def local_import(tree, lines, ctx):
    packages = ctx.extra.get("packages", set())
    seen: set[int] = set()
    for fn in ast.walk(tree):
        if not isinstance(fn, ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        for node in ast.walk(fn):
            if id(node) in seen:
                continue
            seen.add(id(node))
            if isinstance(node, ast.ImportFrom):
                top = (node.module or "").split(".")[0]
                if node.level > 0 or top in packages:
                    yield _f("modeling.local-import", ctx, node, ast.unparse(node)[:60])
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in packages:
                        yield _f("modeling.local-import", ctx, node, f"import {alias.name}")
                        break


@rule(
    "modeling.import-cycle",
    "evite-ciclos-busque-a-arvore",
    "Import cycle between project modules",
    "Two or more project modules that import each other, directly or through a chain "
    "(strongly connected component of the import graph, `__init__` re-exports included). "
    "`from pkg import sub` goes through `pkg/__init__.py`, so a package whose `__init__` imports "
    "a module that imports its siblings through the package is a cycle (hamsterdan "
    "`readiness/net_v5`). Imports under `if TYPE_CHECKING:` run only for the type checker and "
    "add no edge.",
    "Invert one edge: a parameter with a default, a classmethod factory on the leaf, or a "
    "registry the leaf calls; then import modules directly, not through the package.",
    scope="repo",
)
def import_cycle(tree, lines, ctx):  # evaluated once per repo by the runner
    return []


@rule(
    "modeling.inheritance-depth",
    "componha-em-vez-de-herdar",
    "Deep inheritance chain",
    "A class three or more levels below another class defined in the project "
    "(external bases such as `Exception` or `models.Model` do not count).",
    "Flatten: move the varying behavior into a collaborator the class holds, and keep "
    "hierarchies one level deep.",
    scope="repo",
)
def inheritance_depth(tree, lines, ctx):  # evaluated once per repo by the runner
    return []


@rule(
    "project.no-tests",
    "teste-primeiro-das-folhas",
    "No tests in the project",
    "No `tests/` directory and no `test_*.py` or `*_test.py` file anywhere in the target "
    "(repo-scope rules run only when the target is a directory).",
    "Start with the leaves: one test file per module, written before the code it exercises.",
    scope="repo",
)
def no_tests(tree, lines, ctx):  # evaluated once per repo by the runner
    return []


def run_file_rules(tree: ast.AST, lines: list[str], ctx: Context) -> list[Finding]:
    out: list[Finding] = []
    for rule_id, impl in _IMPLS.items():
        if RULES[rule_id].scope == "file":
            out.extend(impl(tree, lines, ctx))
    return out
