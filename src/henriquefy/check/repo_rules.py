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


def import_cycles(
    trees: dict[str, ast.AST], root_paths: dict[str, str], scope: set[str] | None = None
) -> list[Finding]:
    """One finding per cycle, anchored at line 1 of its first member inside `scope` (all paths
    when None), so a cycle that reaches into a checked subdirectory is reported there."""
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
            inside = [m for m in members if scope is None or root_paths[m] in scope]
            anchor = (inside or members)[0]
            findings.append(
                Finding(CYCLE_RULE, root_paths[anchor], 1, "import cycle: " + " -> ".join(members))
            )
    return findings


def _tarjan(graph: dict[str, set[str]]) -> list[set[str]]:
    """Strongly connected components, iteratively: a long import chain must not hit the
    recursion limit."""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    out: list[set[str]] = []
    for root in sorted(graph):
        if root in index:
            continue
        index[root] = low[root] = len(index)
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(sorted(graph.get(root, ()))))]
        while work:
            v, edges = work[-1]
            w = next(edges, None)
            if w is not None:
                if w not in index:
                    index[w] = low[w] = len(index)
                    stack.append(w)
                    on_stack.add(w)
                    work.append((w, iter(sorted(graph.get(w, ())))))
                elif w in on_stack:
                    low[v] = min(low[v], index[w])
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[v])
            if low[v] == index[v]:
                component = set()
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    component.add(w)
                    if w == v:
                        break
                out.append(component)
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

    def parents(key: tuple[str, str]) -> list[tuple[str, str]]:
        return [r for r in (resolve(key[0], b) for b in classes[key][1]) if r is not None]

    cache: dict[tuple[str, str], int] = {}

    def depth(start: tuple[str, str]) -> int:
        """Longest chain of project bases above `start`, iteratively (generated code can chain
        past the recursion limit); a base already on the path (a cycle) counts one level."""
        if start in cache:
            return cache[start]
        best = {start: 0}
        path = [(start, iter(parents(start)))]
        on_path = {start}
        while path:
            key, todo = path[-1]
            base = next(todo, None)
            if base is None:
                path.pop()
                on_path.discard(key)
                cache.setdefault(key, best[key])
                if path:
                    below = path[-1][0]
                    best[below] = max(best[below], 1 + cache[key])
            elif base in on_path:
                best[key] = max(best[key], 1)
            elif base in cache:
                best[key] = max(best[key], 1 + cache[base])
            else:
                best[base] = 0
                on_path.add(base)
                path.append((base, iter(parents(base))))
        return cache[start]

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
    if isinstance(node, ast.Subscript):  # class Repo(Base[Model])
        node = node.value
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return ""
