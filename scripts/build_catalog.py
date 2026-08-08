#!/usr/bin/env python3
"""Build a compact Markdown report and static-site JSON from atlas data."""

from __future__ import annotations

import collections
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINKS = ROOT / "data" / "raw" / "catalog_links.jsonl"
REPORT = ROOT / "docs" / "CATALOG_STATUS.md"
SITE_DATA = ROOT / "site" / "data.json"
SITE_JSONL = ROOT / "site" / "catalog_links.jsonl"
SOURCE_LOCK = ROOT / "data" / "catalog_source_lock.json"


def read_jsonl(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def source_snapshot_time() -> str:
    """Return a reproducible build timestamp tied to the source snapshot."""
    if SOURCE_LOCK.exists():
        value = json.loads(SOURCE_LOCK.read_text()).get("generated_at")
        if value:
            return value
    return "1970-01-01T00:00:00+00:00"


def main() -> int:
    generated_at = source_snapshot_time()
    sources = json.loads((ROOT / "data" / "catalog_sources.json").read_text())["sources"]
    links = read_jsonl(LINKS)
    axiologies = json.loads((ROOT / "data" / "curated" / "axiologies.json").read_text())["axiologies"]
    instruments = json.loads((ROOT / "data" / "curated" / "instruments.json").read_text())["instruments"]
    models = read_jsonl(ROOT / "data" / "curated" / "models.jsonl")
    datasets = read_jsonl(ROOT / "data" / "curated" / "datasets.jsonl")
    works = read_jsonl(ROOT / "data" / "curated" / "works.jsonl")
    studies = read_jsonl(ROOT / "data" / "curated" / "studies.jsonl")
    type_counts = collections.Counter(row["link_type_guess"] for row in links)
    scope_counts = collections.Counter(row["scope_tier_guess"] for row in links)
    source_counts = collections.Counter()
    for row in links:
        for source_id in {occ["catalog_id"] for occ in row["occurrences"]}:
            source_counts[source_id] += 1

    lines = [
        "# Catalog status",
        "",
        f"Source snapshot: {generated_at}",
        "",
        f"- Unique discovered links: **{len(links)}**",
        f"- Curated axiological representations: **{len(axiologies)}**",
        f"- Curated instruments: **{len(instruments)}**",
        f"- Curated measurement models: **{len(models)}**",
        f"- Curated datasets: **{len(datasets)}**",
        f"- Curated works: **{len(works)}**",
        f"- Curated studies: **{len(studies)}**",
        "",
        "## By guessed link type",
        "",
        "| Type | Links |",
        "|---|---:|",
    ]
    lines.extend(f"| {key} | {value} |" for key, value in sorted(type_counts.items()))
    lines.extend(["", "## By guessed scope", "", "| Scope | Links |", "|---|---:|"])
    lines.extend(f"| {key} | {value} |" for key, value in sorted(scope_counts.items()))
    lines.extend(["", "## Unique links contributed by source", "", "| Catalog | Links |", "|---|---:|"])
    lines.extend(f"| {key} | {value} |" for key, value in source_counts.most_common())
    lines.extend(
        [
            "",
            "Counts describe the discovery queue, not verified scientific coverage. A link can appear in several source catalogs but is counted once globally.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines))

    SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
    SITE_JSONL.write_text(LINKS.read_text() if LINKS.exists() else "")
    SITE_DATA.write_text(
        json.dumps(
            {
                "generated_at": generated_at,
                "counts": {"links": len(links), "axiologies": len(axiologies), "instruments": len(instruments), "models": len(models), "datasets": len(datasets), "works": len(works), "studies": len(studies)},
                "links": links,
                "sources": sources,
                "works": works,
                "studies": studies,
                "axiologies": axiologies,
                "instruments": instruments,
                "models": models,
                "datasets": datasets,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n"
    )
    print(f"Wrote {REPORT.relative_to(ROOT)} and {SITE_DATA.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
