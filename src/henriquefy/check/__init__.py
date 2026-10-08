"""Mechanical checks: parse each Python file once, run the per-file rules, apply suppressions."""

import ast
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .rules import HTTP_METHODS, RESPONSE_CALL, ROUTE_CALLS, RULES, Context, Finding, run_file_rules

IGNORE = re.compile(r"#\s*henriquefy:\s*ignore\[([\w.,\s-]+)\]")
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".henriquefy", "build", "dist"}
TEST_FILE = re.compile(r"(^|/)(tests?/|test_[^/]+\.py$|[^/]+_test\.py$)")
UNPARSEABLE = "tooling.unparseable"


@dataclass
class Result:
    root: str
    files: int
    test_files: int
    framework: str
    findings: list[Finding]
    depends_on_decouple: bool = False
    signals: dict[str, bool] = field(default_factory=dict)

    def to_json(self) -> str:
        data = asdict(self)
        data["findings"] = sorted(data["findings"], key=lambda f: (f["path"], f["line"], f["rule"]))
        return json.dumps(data, indent=2, ensure_ascii=False)


def python_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(p for p in target.rglob("*.py") if not any(part in SKIP_DIRS for part in p.parts))


def depends_on_decouple(root: Path) -> bool:
    names = ("pyproject.toml", "setup.py", "setup.cfg", "Pipfile")
    candidates = [root / n for n in names] + list(root.glob("requirements*.txt"))
    return any(
        f.is_file() and "decouple" in f.read_text(encoding="utf-8", errors="replace")
        for f in candidates
    )


def detect_framework(sources: list[str]) -> str:
    joined = "\n".join(sources)
    if re.search(r"^\s*(from|import)\s+django\b", joined, re.M):
        return "django"
    if re.search(r"^\s*(from|import)\s+fastapi\b", joined, re.M):
        return "fastapi"
    if re.search(r"^\s*(from|import)\s+starlette\b", joined, re.M):
        return "starlette"
    return "none"


def check(target: Path) -> Result:
    target = target.resolve()
    root = target if target.is_dir() else target.parent
    files = python_files(target)
    decouple = depends_on_decouple(root)
    sources: list[str] = []
    findings: list[Finding] = []
    test_files = 0
    signals = {"routes": False, "responses": False}
    for path in files:
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        source = path.read_text(encoding="utf-8", errors="replace")
        sources.append(source)
        lines = source.splitlines()
        is_test = bool(TEST_FILE.search(str(rel).replace("\\", "/")))
        test_files += is_test
        ctx = Context(path=rel, root=root, is_test=is_test, depends_on_decouple=decouple)
        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError as exc:
            findings.append(
                Finding(UNPARSEABLE, str(rel), exc.lineno or 1, f"cannot parse: {exc.msg}")
            )
            continue
        findings.extend(_apply_suppressions(run_file_rules(tree, lines, ctx), lines))
        _collect_signals(tree, signals)
    if target.is_dir() and test_files == 0:
        findings.append(Finding("project.no-tests", str(rel_root(root)), 0, "no test files found"))
    return Result(
        str(root), len(files), test_files, detect_framework(sources), findings, decouple, signals
    )


def _collect_signals(tree: ast.AST, signals: dict[str, bool]) -> None:
    """Whether the file defines routes or builds responses, so API and status rules count as
    applicable only where they had a chance to fire."""
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


def rel_root(root: Path) -> str:
    return "."


def _apply_suppressions(findings: list[Finding], lines: list[str]) -> list[Finding]:
    kept = []
    for f in findings:
        candidates = [lines[f.line - 1]] if 0 < f.line <= len(lines) else []
        if f.line >= 2:
            candidates.append(lines[f.line - 2])
        suppressed = any(
            f.rule in {r.strip() for r in m.group(1).split(",")}
            for text in candidates
            for m in IGNORE.finditer(text)
        )
        if not suppressed:
            kept.append(f)
    return kept


def describe(result: Result, principles: dict[str, dict] | None = None) -> str:
    """One line per finding: path:line, rule, why, citation, fix."""
    principles = principles or {}
    lines = [
        f"{result.root}: {result.files} files, {result.test_files} test files,"
        f" framework {result.framework}"
    ]
    for f in sorted(result.findings, key=lambda f: (f.path, f.line, f.rule)):
        rule = RULES.get(f.rule)
        if rule is None:
            lines.append(f"{f.path}:{f.line}  {f.rule}  {f.message}")
            continue
        p = principles.get(rule.principle, {})
        citation = p.get("citation", rule.principle)
        lines.append(
            f"{f.path}:{f.line}  {f.rule}  {f.message}. {rule.title}: {rule.detect}"
            f" [{citation}] Fix: {rule.fix}"
        )
    if not result.findings:
        lines.append("no findings")
    return "\n".join(lines)
