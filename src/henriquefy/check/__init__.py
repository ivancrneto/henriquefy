"""Mechanical checks: find the project root, parse every Python file once, run the per-file
rules on the files in scope, the whole-repo rules over the root, and apply suppressions."""

import ast
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .repo_rules import import_cycles, inheritance_depth, module_name
from .rules import HTTP_METHODS, RESPONSE_CALL, ROUTE_CALLS, RULES, Context, Finding, run_file_rules

IGNORE = re.compile(r"#\s*henriquefy:\s*ignore\[([\w.,\s-]+)\]")
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".henriquefy", "build", "dist"}
TEST_FILE = re.compile(r"(^|/)(tests?/|test_[^/]+\.py$|[^/]+_test\.py$|conftest\.py$)")
ROOT_MARKERS = ("pyproject.toml", "setup.py", "setup.cfg", ".git")
UNPARSEABLE = "tooling.unparseable"
PARSE_ERRORS = (SyntaxError, ValueError, RecursionError, MemoryError)


@dataclass
class Result:
    root: str
    files: int
    test_files: int
    framework: str
    findings: list[Finding]
    depends_on_decouple: bool = False
    signals: dict[str, bool] = field(default_factory=dict)
    target_is_dir: bool = True
    unparseable: int = 0
    target: str = ""

    def to_json(self) -> str:
        data = asdict(self)
        data["findings"] = sorted(data["findings"], key=lambda f: (f["path"], f["line"], f["rule"]))
        return json.dumps(data, indent=2, ensure_ascii=False)


def find_root(target: Path) -> Path:
    """Nearest ancestor holding a project marker; the target's directory when none exists."""
    start = target if target.is_dir() else target.parent
    for directory in (start, *start.parents):
        if any((directory / marker).exists() for marker in ROOT_MARKERS):
            return directory
    return start


def python_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(p for p in root.rglob("*.py") if not any(part in SKIP_DIRS for part in p.parts))


def depends_on_decouple(root: Path) -> bool:
    names = ("pyproject.toml", "setup.py", "setup.cfg", "Pipfile")
    candidates = [root / n for n in names] + list(root.glob("requirements*.txt"))
    return any(
        f.is_file() and "decouple" in f.read_text(encoding="utf-8", errors="replace")
        for f in candidates
    )


def detect_framework(sources: list[str]) -> str:
    joined = "\n".join(sources)
    for name in ("django", "fastapi", "starlette"):
        if re.search(rf"^\s*(from|import)\s+{name}\b", joined, re.M):
            return name
    return "none"


def _packages(root: Path) -> set[str]:
    found = {p.name for p in root.iterdir() if (p / "__init__.py").is_file()} | {root.name}
    if (root / "src").is_dir():
        found |= {p.name for p in (root / "src").iterdir() if (p / "__init__.py").is_file()}
    return found


def check(target: Path, root: Path | None = None) -> Result:
    """`root` overrides project-root discovery (the nearest pyproject, setup or .git above
    the target); every repo-level signal is computed from the root, findings from the target."""
    target = target.resolve()
    root = root.resolve() if root else find_root(target)
    all_files = python_files(root)
    if target.is_file() and target not in all_files:
        all_files.append(target)
    in_scope = {p for p in all_files if p == target or target in p.parents}
    decouple = depends_on_decouple(root)
    packages = _packages(root)
    trees: dict[str, ast.AST] = {}
    rel_paths: dict[str, str] = {}
    lines_by_path: dict[str, list[str]] = {}
    sources: list[str] = []
    findings: list[Finding] = []
    signals = {"routes": False, "responses": False}
    files = test_files = unparseable = root_test_files = 0
    for path in all_files:
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        rel_str = str(rel).replace("\\", "/")
        source = path.read_text(encoding="utf-8", errors="replace")
        is_test = bool(TEST_FILE.search(rel_str))
        try:
            tree = ast.parse(source, filename=str(path))
        except PARSE_ERRORS as exc:
            if path in in_scope:
                unparseable += 1
                msg = getattr(exc, "msg", None) or type(exc).__name__
                findings.append(
                    Finding(
                        UNPARSEABLE,
                        rel_str,
                        getattr(exc, "lineno", None) or 1,
                        f"cannot parse ({msg}); excluded from scoring. Newer syntax? Run under"
                        " `uvx --python 3.14 henriquefy`",
                    )
                )
            continue
        root_test_files += is_test
        lines = source.splitlines()
        mod = module_name(rel, packages)
        trees[mod] = tree
        rel_paths[mod] = rel_str
        lines_by_path[rel_str] = lines
        if path not in in_scope:
            continue
        files += 1
        test_files += is_test
        sources.append(source)
        ctx = Context(
            path=rel,
            root=root,
            is_test=is_test,
            depends_on_decouple=decouple,
            extra={"packages": packages},
        )
        findings.extend(run_file_rules(tree, lines, ctx))
        _collect_signals(tree, signals)
    if target.is_dir():
        scope_paths = {
            str(p.relative_to(root)).replace("\\", "/") for p in in_scope if p.is_relative_to(root)
        }
        repo_findings = import_cycles(trees, rel_paths) + inheritance_depth(trees, rel_paths)
        findings.extend(f for f in repo_findings if f.path in scope_paths)
        if root_test_files == 0:
            findings.append(Finding("project.no-tests", ".", 0, "no test files found"))
    findings = _apply_suppressions(findings, lines_by_path)
    findings = _dedupe(findings)
    return Result(
        str(root),
        files,
        test_files,
        detect_framework(sources),
        findings,
        decouple,
        signals,
        target.is_dir(),
        unparseable,
        str(target),
    )


def _collect_signals(tree: ast.AST, signals: dict[str, bool]) -> None:
    """Whether the file defines routes or builds responses, so API rules count as applicable
    only where they had a chance to fire."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")
            if name in ROUTE_CALLS:
                signals["routes"] = True
            if name and RESPONSE_CALL.search(name):
                signals["responses"] = True
        elif isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            for deco in node.decorator_list:
                f = deco.func if isinstance(deco, ast.Call) else deco
                if isinstance(f, ast.Attribute) and f.attr in HTTP_METHODS:
                    signals["routes"] = True
        elif isinstance(node, ast.ClassDef) and RESPONSE_CALL.search(node.name):
            signals["responses"] = True


def _apply_suppressions(
    findings: list[Finding], lines_by_path: dict[str, list[str]]
) -> list[Finding]:
    kept = []
    for f in findings:
        lines = lines_by_path.get(f.path, [])
        anchors = [n for n in (f.line, f.line - 1, 1, 2) if 0 < n <= len(lines)] if f.line else []
        suppressed = any(
            f.rule in {r.strip() for r in m.group(1).split(",")}
            for n in anchors
            for m in IGNORE.finditer(lines[n - 1])
        )
        if not suppressed:
            kept.append(f)
    return kept


def _dedupe(findings: list[Finding]) -> list[Finding]:
    seen: set[tuple] = set()
    out = []
    for f in findings:
        key = (f.rule, f.path, f.line, f.col, f.message)
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def describe(result: Result, principles: dict | None = None) -> str:
    """One line per finding: path:line, rule, what, why, citation, fix."""
    principles = principles or {}
    head = f"{result.root}: {result.files} files in scope, {result.test_files} test files"
    lines = [f"{head}, framework {result.framework}"]
    if result.unparseable:
        lines.append(
            f"{result.unparseable} file(s) could not be parsed and are excluded from scoring"
        )
    for f in sorted(result.findings, key=lambda f: (f.path, f.line, f.rule)):
        rule = RULES.get(f.rule)
        if rule is None:
            lines.append(f"{f.path}:{f.line}  {f.rule}  {f.message}")
            continue
        p = principles.get(rule.principle)
        citation = getattr(p, "citation", None) or rule.principle
        lines.append(
            f"{f.path}:{f.line}  {f.rule}  {f.message}. {rule.title} [{rule.principle}; {citation}]"
            f" Fix: {rule.fix}"
        )
    if not result.findings:
        lines.append("no findings")
    return "\n".join(lines)
