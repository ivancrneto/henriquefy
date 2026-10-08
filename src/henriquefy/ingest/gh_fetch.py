"""List Henrique Bastos's repositories, record provenance, and shallow-clone the mining list.

    python -m henriquefy.ingest.gh_fetch            # his repos: manifest + clones of MINING
    python -m henriquefy.ingest.gh_fetch --alumni   # forks of his course repos, class alumni

Writes sources/repos/manifest.json (gitignored) with sha, pushed date, license and class, and
extends evals/calibration/his.json's repo list with the shas used. Needs `gh auth login`.
Alumni repos are cloned under random ids; the id-to-repo map stays in the gitignored manifest.
"""

import json
import secrets
import subprocess
import sys
from datetime import date
from pathlib import Path

OWNERS = ("henriquebastos", "HBNetwork")
MINING = [
    "henriquebastos/hamsterdan",
    "henriquebastos/monopoly",
    "henriquebastos/requests-pro",
    "henriquebastos/python-jsonstar",
    "HBNetwork/python-decouple",
    "henriquebastos/pacote-desafios-pythonicos",
    "henriquebastos/eventex",
    "henriquebastos/beans",
    "henriquebastos/jira-genie",
    "henriquebastos/petrus-engine",
    "henriquebastos/petrus",
    "henriquebastos/django-aggregate-if",
    "henriquebastos/django-test-without-migrations",
    "henriquebastos/sqlformatter",
]
ALUMNI_SOURCES = {
    "henriquebastos/eventex": None,  # all forks
    "henriquebastos/pacote-desafios-pythonicos": 25,  # sample
    "HBNetwork/pds-api-client": None,
    "HBNetwork/pds-multi-tenant": None,
    "HBNetwork/pds-testes-tecnicos": None,
    "HBNetwork/pds-microservicos": None,
}
ALUMNI_NAMED = ["virb30/design-api", "HenriqueCCdA/Design_de_API_na_pratica"]


def gh(path: str) -> list | dict:
    """GET a GitHub API path; list endpoints are paginated and merged by gh itself."""
    if "per_page" in path:
        out = subprocess.run(
            ["gh", "api", "--paginate", "--slurp", path], capture_output=True, text=True, check=True
        ).stdout
        pages = json.loads(out)
        return [item for page in pages for item in page]
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def repo_record(full_name: str, klass: str) -> dict:
    meta = gh(f"repos/{full_name}")
    head = gh(f"repos/{full_name}/commits?per_page=1")
    return {
        "repo": full_name,
        "class": klass,
        "sha": head[0]["sha"] if head else None,
        "pushed_at": meta.get("pushed_at"),
        "created_at": meta.get("created_at"),
        "license": (meta.get("license") or {}).get("spdx_id"),
        "language": meta.get("language"),
        "fork": meta.get("fork", False),
    }


def clone(full_name: str, dest: Path, sha: str | None) -> None:
    if dest.exists():
        return
    subprocess.run(
        ["git", "clone", "-q", "--depth", "50", f"https://github.com/{full_name}.git", str(dest)],
        check=True,
    )
    if sha:
        subprocess.run(["git", "-C", str(dest), "checkout", "-q", sha], check=False)


def his(root: Path) -> list[dict]:
    listed = []
    for owner in OWNERS:
        kind = "orgs" if owner == "HBNetwork" else "users"
        listed += [r["full_name"] for r in gh(f"{kind}/{owner}/repos?per_page=100")]
    records = []
    for name in MINING:
        rec = repo_record(name, "his")
        clone(name, root / name.split("/")[1], rec["sha"])
        records.append(rec)
    return records + [
        {"repo": n, "class": "his", "listed_only": True} for n in listed if n not in MINING
    ]


def alumni(root: Path) -> list[dict]:
    records = []
    candidates = list(ALUMNI_NAMED)
    for source, limit in ALUMNI_SOURCES.items():
        forks = [f["full_name"] for f in gh(f"repos/{source}/forks?per_page=100")]
        forks.sort()
        if limit and len(forks) > limit:
            step = len(forks) / limit
            forks = [forks[int(i * step)] for i in range(limit)]
        candidates += forks
    for name in candidates:
        try:
            rec = repo_record(name, "alumni")
        except subprocess.CalledProcessError:
            continue
        rec["id"] = secrets.token_hex(6)
        clone(name, root / "alumni" / rec["id"], rec["sha"])
        records.append(rec)
    return records


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    root = Path("sources/repos")
    root.mkdir(parents=True, exist_ok=True)
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.is_file() else {}
    if "--alumni" in argv:
        manifest["alumni"] = alumni(root)
    else:
        manifest["his"] = his(root)
    manifest["fetched"] = str(date.today())
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    key = "alumni" if "--alumni" in argv else "his"
    print(f"{key}: {len(manifest[key])} records; manifest at {manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
