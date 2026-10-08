"""Command line entry point. Phase 0 ships `install` and `--version` only."""

import argparse
import sys
from pathlib import Path

from . import __version__
from .install import install


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
        for path in install(target, all_skills=args.all):
            print(f"installed {path}")
        if args.project:
            print("note: the KB copy under .claude/skills/ is now inside this repo's git tree")
        return 0
    build_parser().print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
