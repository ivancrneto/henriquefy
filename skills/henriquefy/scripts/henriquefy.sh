#!/usr/bin/env sh
# Run the henriquefy CLI pinned to the version this skill was installed from.
# uvx contacts the index on every run; --offline reuses the cache. Try offline first.
set -u
# HENRIQUEFY_CLI=/path/to/henriquefy (for example a checkout's .venv/bin/henriquefy) runs that
# executable instead of uvx, so a checkout or an unreleased version can be used.
if [ -n "${HENRIQUEFY_CLI:-}" ]; then
  exec "$HENRIQUEFY_CLI" "$@"
fi
# CDPATH would make cd print the directory into HERE; quotes and CR are stripped from V.
HERE="$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)"
V="$(sed -n 's/^ *henriquefy_version: *//p' "$HERE/../SKILL.md" | head -1 | tr -d "\"' \r")"
if uvx --offline "henriquefy==$V" --version >/dev/null 2>&1; then
  exec uvx --offline "henriquefy==$V" "$@"
fi
if uvx "henriquefy==$V" --version >/dev/null 2>&1; then
  exec uvx "henriquefy==$V" "$@"
fi
# exit 3: the CLI could not run (exit 1 means findings were found)
echo "henriquefy $V is not cached and could not be fetched; connect once, or run: uvx henriquefy@latest update" >&2
exit 3
