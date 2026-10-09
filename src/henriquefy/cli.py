"""Command line entry point: install, check, grade."""

import argparse
import sys
from pathlib import Path

from . import __version__
from .install import install
from .overrides import load_overrides


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="henriquefy",
        description="Henrique Bastos's practices, applied to your code.",
    )
    parser.add_argument("--version", action="version", version=f"henriquefy {__version__}")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("install", help="write the henriquefy skill for Claude Code")
    where = p.add_mutually_exclusive_group()
    where.add_argument(
        "--project",
        action="store_true",
        help="install into ./.claude/skills/ of the current directory instead of ~/.claude/skills/",
    )
    where.add_argument("--target", type=Path, help="install into this skills directory")
    p.add_argument(
        "--all",
        action="store_true",
        help="also install the maintainer skills henrique-ingest and henrique-watch",
    )
    sub.add_parser(
        "update", help="re-install the skill from this version; run as uvx henriquefy@latest update"
    )
    for name, help_ in (
        ("check", "mechanical rules only; no Claude needed"),
        ("grade", "Nota mecânica, deterministic"),
    ):
        q = sub.add_parser(name, help=help_)
        q.add_argument("path", nargs="?", default=".", type=Path)
        q.add_argument("--json", action="store_true", help="machine-readable output")
        q.add_argument(
            "--era", type=int, help="grade against his practice of this year (calibration)"
        )
        q.add_argument(
            "--root",
            type=Path,
            help="project root; default: nearest pyproject, setup or .git above path",
        )
        if name == "grade":
            q.add_argument(
                "--report",
                action="store_true",
                help="also write .henriquefy/report.md and grade.jsonl",
            )
    return parser


def _skills_target(args: argparse.Namespace) -> Path:
    if args.target:
        return args.target
    if args.project:
        return Path.cwd() / ".claude" / "skills"
    return Path.home() / ".claude" / "skills"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "install":
        target = _skills_target(args)
        target.mkdir(parents=True, exist_ok=True)
        try:
            written = install(target, all_skills=args.all)
        except ValueError as exc:
            print(exc, file=sys.stderr)
            return 2
        for path in written:
            print(f"installed {path}")
        if args.project:
            print("note: the KB copy under .claude/skills/ is now inside this repo's git tree")
        return 0
    if args.command == "update":
        target = Path.home() / ".claude" / "skills"
        target.mkdir(parents=True, exist_ok=True)
        for path in install(target):
            print(f"updated {path} to {__version__}")
        return 0
    if args.command in {"check", "grade"}:
        return _check_or_grade(args)
    build_parser().print_help()
    return 2


def _check_or_grade(args: argparse.Namespace) -> int:
    from .check import check, describe
    from .grade import grade, load_principles
    from .grade.report import render, write_report

    if not args.path.exists():
        print(f"no such path: {args.path}", file=sys.stderr)
        return 2
    try:
        result = check(args.path, root=args.root)
    except ValueError as exc:  # --root that does not contain the path
        print(exc, file=sys.stderr)
        return 2
    principles = load_principles()
    if args.command == "check":
        print(result.to_json() if args.json else describe(result, principles))
        return 1 if result.findings else 0
    overridden = load_overrides(principles)
    g = grade(result, era=args.era, principles=principles)
    g.overrides = overridden
    text = render(g, result, overrides_active=overridden)
    print(g.to_json() if args.json else text)
    if args.report:
        root = args.path if args.path.is_dir() else args.path.parent
        print(f"wrote {write_report(root.resolve(), g, result, text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
