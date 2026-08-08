#!/usr/bin/env python3
"""Clone or update public source catalogs used for link discovery."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "data" / "catalog_sources.json"
DEFAULT_CACHE = ROOT / ".cache" / "catalog-sources"
LOCK = ROOT / "data" / "catalog_source_lock.json"


def run(*args: str, cwd: pathlib.Path | None = None) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=pathlib.Path, default=DEFAULT_CACHE)
    parser.add_argument("--no-update", action="store_true")
    args = parser.parse_args()

    config = json.loads(CONFIG.read_text())
    args.cache.mkdir(parents=True, exist_ok=True)
    locked = []

    for source in config["sources"]:
        if source.get("kind", "git_readme") != "git_readme":
            locked.append(
                {
                    "id": source["id"],
                    "kind": source["kind"],
                    "path": source["seed_file"],
                }
            )
            print(f"{source['id']}: local snapshot")
            continue
        target = args.cache / source["id"]
        if not target.exists():
            run("git", "clone", "--depth", "1", source["repo"], str(target))
        elif not args.no_update:
            run("git", "fetch", "--depth", "1", "origin", cwd=target)
            default_branch = run("git", "symbolic-ref", "--short", "refs/remotes/origin/HEAD", cwd=target)
            run("git", "reset", "--hard", default_branch, cwd=target)

        commit = run("git", "rev-parse", "HEAD", cwd=target)
        commit_date = run("git", "show", "-s", "--format=%cI", "HEAD", cwd=target)
        locked.append(
            {
                "id": source["id"],
                "kind": "git_readme",
                "repo": source["repo"],
                "commit": commit,
                "commit_date": commit_date,
            }
        )
        print(f"{source['id']}: {commit[:12]}")

    payload = {
        "schema_version": "1.0.0",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sources": locked,
    }
    LOCK.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(exc.stderr, file=sys.stderr)
        raise
