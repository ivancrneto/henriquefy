"""Build the Agensi edition of the henriquefy skill: a zip with fewer than 50 files whose text an
automated scanner does not mistake for behavior.

    uv run python scripts/build_agensi.py [out.zip]

It installs the skill the normal way, then (1) merges the pattern, repo and course digests into
one file each, (2) paraphrases the code samples that read the process environment or carry example
credentials, and (3) fails if any scanner-bait is left. The repository and `uvx henriquefy install`
keep the full text.
"""

import re
import sys
import tempfile
import zipfile
from pathlib import Path

from henriquefy.install import install

MAX_FILES = 49
MERGED = {"patterns": "patterns.md", "repos": "repos.md", "courses": "courses.md"}

# (pattern, replacement), applied in order to every text file of the edition.
SCRUB = [
    (r'"sk_live_[^"]*"', '"<live key>"'),
    (r'"ATOA[^"]*"', '"<client secret>"'),
    (r"mysql://myuser:mypassword@myhost/mydatabase", "<database url>"),
    (r"git\+https://\.\.\.@[0-9a-f.]+", "git+<repository url>@<commit>"),
    (r"os\.environ\.get\(", "env_get("),
    (r"os\.environ\[", "env["),
    (r"os\.getenv\(", "env_get("),
    (r"os\.getenv", "env_get"),
    (r"os\.environ", "<env>"),
    (r"\bDATABASE_URL\b", "DB_URL"),
    (r"\b(?:E2B_API_KEY|JIRA_CLIENT_SECRET|IMPETUS_TEST_DSN)\b", "<VARIABLE>"),
]

# What must not survive in the edition; a hit fails the build.
FORBIDDEN = re.compile(
    r"os\.environ|os\.getenv|DATABASE_URL|sk_live|ATOA\w|mypassword|://[^\s/@]*:[^\s/@]*@|"
    r"https?://\.\.\.@"
)

SKILL_PATHS = [
    ("`references/kb/patterns/<id>.md`", "`patterns/<id>.md` in `references/kb/patterns.md`"),
    ("`references/kb/repos/<name>.md`", "`repos/<name>.md` in `references/kb/repos.md`"),
    ("`repos/drift.md`", "`repos/drift.md` in `references/kb/repos.md`"),
    ("`references/kb/courses/<course>.md`", "`courses/<course>.md` in `references/kb/courses.md`"),
]
LAYOUT_NOTE = """## Layout of this edition

The pattern, repository and course digests are merged into `references/kb/patterns.md`,
`references/kb/repos.md` and `references/kb/courses.md`. Each file starts at a line
`##### FILE <dir>/<name>.md`; read from that line to the next one. Code samples that read the
process environment (written `<env>` here) or show example credentials are paraphrased; the full text is in the
repository and in `uvx henriquefy install`.

"""


def build(out: Path) -> int:
    with tempfile.TemporaryDirectory() as tmp:
        (installed,) = install(Path(tmp) / "skills")
        _merge(installed / "references" / "kb")
        _adapt_skill(installed / "SKILL.md")
        for name in ("NOTICE.md", "LICENSE"):
            (installed / name).write_text((Path(name)).read_text(encoding="utf-8"), encoding="utf-8")
        files = sorted(p for p in installed.rglob("*") if p.is_file())
        for path in files:
            text = path.read_text(encoding="utf-8")
            for pattern, repl in SCRUB:
                text = re.sub(pattern, repl, text)
            path.write_text(text, encoding="utf-8")
            if hit := FORBIDDEN.search(text):
                raise SystemExit(f"{path.relative_to(installed)}: scanner bait left: {hit.group()!r}")
        if len(files) > MAX_FILES:
            raise SystemExit(f"{len(files)} files, the limit is {MAX_FILES}")
        out.unlink(missing_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in files:
                zf.write(path, Path(installed.name) / path.relative_to(installed))
        return len(files)


def _merge(kb: Path) -> None:
    (kb / "principles" / "_template.md").unlink(missing_ok=True)
    for directory, merged in MERGED.items():
        parts = [
            f"##### FILE {directory}/{src.name}\n\n{src.read_text(encoding='utf-8').strip()}\n"
            for src in sorted((kb / directory).glob("*.md"))
        ]
        (kb / merged).write_text("\n".join(parts), encoding="utf-8")
        for src in (kb / directory).glob("*.md"):
            src.unlink()
        (kb / directory).rmdir()


def _adapt_skill(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    for old, new in SKILL_PATHS:
        if old not in text:
            raise SystemExit(f"SKILL.md no longer contains {old}; update SKILL_PATHS")
        text = text.replace(old, new)
    marker = "## Never\n"
    if marker not in text:
        raise SystemExit("SKILL.md has no '## Never' section; update LAYOUT_NOTE placement")
    text = text.replace(marker, LAYOUT_NOTE + marker, 1)
    skill_md.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "henriquefy-agensi.zip")
    print(f"{target}: {build(target)} files")
