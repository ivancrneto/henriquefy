"""Write self-contained skill directories for Claude Code.

The installed skill never points back into site-packages: the KB is copied into
references/kb/ of the henriquefy skill, and SKILL.md records the version it came
from under the free-form `metadata` frontmatter key.
"""

import re
import shutil
from pathlib import Path

from . import __version__
from .paths import kb_dir, skills_dir

CONSUMER = "henriquefy"
MAINTAINER = ("henrique-ingest", "henrique-watch")
_VERSION_LINE = re.compile(r"^(\s*henriquefy_version:\s*).*$", re.M)


def install(target: Path, *, all_skills: bool = False) -> list[Path]:
    """Install skills under `target` (a `skills/` directory). Returns the written dirs."""
    names = (CONSUMER, *MAINTAINER) if all_skills else (CONSUMER,)
    written = []
    for name in names:
        src = skills_dir() / name
        dest = target / name
        if dest.resolve() == src.resolve() or src.resolve().is_relative_to(dest.resolve()):
            raise ValueError(f"{dest} is the skill's own source; install somewhere else")
        if dest.is_symlink():  # a link (stow, dotfiles) is replaced, never followed into
            dest.unlink()
        elif dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        if name == CONSUMER:
            shutil.copytree(kb_dir(), dest / "references" / "kb")
        _stamp_version(dest / "SKILL.md")
        for script in (dest / "scripts").glob("*.sh") if (dest / "scripts").is_dir() else ():
            script.chmod(0o755)
        written.append(dest)
    return written


def _stamp_version(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    stamped, n = _VERSION_LINE.subn(rf"\g<1>{__version__}", text, count=1)
    if n != 1:
        raise RuntimeError(f"{skill_md} has no `henriquefy_version:` line under metadata")
    skill_md.write_text(stamped, encoding="utf-8")
