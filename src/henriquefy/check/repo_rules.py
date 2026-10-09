"""Whole-repo rules: they need every file parsed before they can run.

import cycles: strongly connected components of the in-project import graph.
inheritance depth: chains of classes defined in the project, A -> B -> C -> D.
"""

import ast
from pathlib import Path

from .rules import Finding

CYCLE_RULE = "modeling.import-cycle"
DEPTH_RULE = "modeling.inheritance-depth"
MAX_DEPTH = 2  # D(C(B(A))) has depth 3 and is flagged


def module_name(rel: Path, packages: set[str]) -> str:
    parts = list(rel.with_suffix("").parts)
    if parts and parts[0] == "src":
        parts = parts[1:]
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _resolve(current: str, node: ast.Import | ast.ImportFrom, modules: set[str]) -> set[str]:
    """Targets inside the project that an import statement refers to."""
    targets: set[str] = set()
    if isinstance(node, ast.Import):
        for alias in node.names:
            targets |= _closest(alias.name, modules)
        return targets
    base = node.module or ""
    if node.level:
        package = current.split(".")
        if not _is_package(current, modules):
            package = package[:-1]
        package = package[: len(package) - (node.level - 1)] if node.level > 1 else package
        base = ".".join(p for p in [*package, base] if p)
    for alias in node.names:
        targets |= _closest(f"{base}.{alias.name}" if base else alias.name, modules)
    targets |= _closest(base, modules)
    return targets


def _is_package(name: str, modules: set[str]) -> bool:
    return any(m.startswith(name + ".") for m in modules)


def _closest(dotted: str, modules: set[str]) -> set[str]:
    parts = dotted.split(".")
    for i in range(len(parts), 0, -1):
        candidate = ".".join(parts[:i])
        if candidate in modules:
            return {candidate}
    return set()


def import_cycles(trees: dict[str, ast.AST], root_paths: dict[str, str]) -> list[Finding]:
    modules = set(trees)
    graph: dict[str, set[str]] = {m: set() for m in modules}
    for name, tree in trees.items():
        for node in ast.walk(tree):
            if isinstance(node, ast.Import | ast.ImportFrom):
                graph[name] |= _resolve(name, node, modules) - {name}
    findings = []
    for component in _tarjan(graph):
        if len(component) > 1:
            members = sorted(component)
            findings.append(
                Finding(
                    CYCLE_RULE, root_paths[members[0]], 1, "import cycle: " + " -> ".join(members)
                )
            )
    return findings


def _tarjan(graph: dict[str, set[str]]) -> list[set[str]]:
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    out: list[set[str]] = []
    counter = 0

    def strong(v: str) -> None:
        nonlocal counter
        index[v] = low[v] = counter
        counter += 1
        stack.append(v)
        on_stack.add(v)
        for w in graph.get(v, ()):
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            component = set()
            while True:
                w = stack.pop()
                on_stack.discard(w)
                component.add(w)
                if w == v:
                    break
            out.append(component)

    for v in sorted(graph):
        if v not in index:
            strong(v)
    return out


def inheritance_depth(trees: dict[str, ast.AST], root_paths: dict[str, str]) -> list[Finding]:
    """Classes are keyed by module and name; a base resolves to the same module first, then to
    a unique class of that name anywhere in the project. `class Model(models.Model)` is not a
    level: an attribute base whose name equals the class's own is external."""
    classes: dict[tuple[str, str], tuple[int, list[str]]] = {}
    by_name: dict[str, list[tuple[str, str]]] = {}
    for module, tree in trees.items():
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases = []
                for b in node.bases:
                    name = _base_name(b)
                    if name and not (isinstance(b, ast.Attribute) and name == node.name):
                        bases.append(name)
                key = (module, node.name)
                if key not in classes:
                    classes[key] = (node.lineno, bases)
                    by_name.setdefault(node.name, []).append(key)

    def resolve(module: str, base: str) -> tuple[str, str] | None:
        if (module, base) in classes:
            return (module, base)
        candidates = by_name.get(base, [])
        return candidates[0] if len(candidates) == 1 else None

    cache: dict[tuple[str, str], int] = {}

    def depth(key: tuple[str, str], seen: frozenset = frozenset()) -> int:
        if key in seen:
            return 0
        if key in cache:
            return cache[key]
        _, bases = classes[key]
        resolved = [resolve(key[0], b) for b in bases]
        d = max((1 + depth(r, seen | {key}) for r in resolved if r is not None), default=0)
        cache[key] = d
        return d

    findings = []
    for key, (line, _) in sorted(classes.items(), key=lambda kv: (kv[0][0], kv[1][0])):
        d = depth(key)
        if d > MAX_DEPTH:
            findings.append(
                Finding(
                    DEPTH_RULE,
                    root_paths[key[0]],
                    line,
                    f"{key[1]} is {d} levels below a project class",
                )
            )
    return findings


def _base_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return ""
