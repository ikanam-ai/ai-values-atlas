#!/usr/bin/env python3
"""Build the public site dataset from the curated JSONL records."""

from __future__ import annotations

import collections
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKS_PATH = ROOT / "data" / "works.jsonl"
RESOURCES_PATH = ROOT / "data" / "resources.jsonl"
RAW_LINKS_PATH = ROOT / "data" / "raw" / "catalog_links.jsonl"
SITE_DATA_PATH = ROOT / "site" / "data.json"


def read_jsonl(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def order_work(work: dict) -> dict:
    fields = (
        "id", "title", "year", "venue", "publication_status", "scope",
        "domains", "contribution_types", "links", "release",
    )
    ordered = {field: work[field] for field in fields if field in work}
    if "release" in ordered:
        release = ordered["release"]
        ordered["release"] = {
            field: release[field] for field in ("licenses", "available") if field in release
        }
    return ordered


def order_resource(resource: dict) -> dict:
    fields = ("id", "title", "url", "roles", "kind")
    return {field: resource[field] for field in fields if field in resource}


def main() -> int:
    works = [order_work(work) for work in read_jsonl(WORKS_PATH)]
    resources = [order_resource(resource) for resource in read_jsonl(RESOURCES_PATH)]
    source_links = read_jsonl(RAW_LINKS_PATH)
    current = json.loads(SITE_DATA_PATH.read_text())

    domain_counts = collections.Counter(
        domain for work in works for domain in work.get("domains", [])
    )
    domains = [
        {**domain, "work_count": domain_counts[domain["id"]]}
        for domain in current["domains"]
    ]
    year_counts = collections.Counter(work["year"] for work in works)

    payload = {
        "title": current["title"],
        "tagline": current["tagline"],
        "stats": {
            "research_works": len(works),
            "domains": len(domains),
            "source_links": len(source_links),
            "work_resource_relations": sum(len(work.get("links", [])) for work in works),
            "standalone_resources": len(resources),
        },
        "domains": domains,
        "works": works,
        "standalone_resources": resources,
        "year_counts": [
            {"year": year, "count": count}
            for year, count in sorted(year_counts.items())
        ],
    }
    SITE_DATA_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )
    print(
        f"Built {SITE_DATA_PATH.relative_to(ROOT)}: "
        f"{len(works)} works, {len(source_links)} source links, {len(resources)} resources"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
