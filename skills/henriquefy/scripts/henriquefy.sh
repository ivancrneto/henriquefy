#!/usr/bin/env sh
# Run the henriquefy CLI pinned to the version this skill was installed from.
# uvx contacts the index on every run; --offline reuses the cache. Try offline first.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
V="$(sed -n 's/^ *henriquefy_version: *//p' "$HERE/../SKILL.md" | head -1)"
if uvx --offline "henriquefy==$V" --version >/dev/null 2>&1; then
  exec uvx --offline "henriquefy==$V" "$@"
fi
if uvx "henriquefy==$V" --version >/dev/null 2>&1; then
  exec uvx "henriquefy==$V" "$@"
fi
echo "henriquefy $V not cached; connect once or run uvx henriquefy@latest update" >&2
exit 1
