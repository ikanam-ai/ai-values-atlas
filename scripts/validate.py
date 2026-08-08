#!/usr/bin/env python3
"""Dependency-free structural validation for atlas source data."""

from __future__ import annotations

import json
import pathlib
import re
import sys
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_json(path: pathlib.Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001 - report all parse failures together
        raise ValueError(f"{path}: {exc}") from exc


def load_jsonl(path: pathlib.Path):
    if not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: {exc}") from exc
    return rows


def valid_url(value: str) -> bool:
    parsed = urllib.parse.urlsplit(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    source_config = load_json(ROOT / "data" / "catalog_sources.json")
    source_ids = [source["id"] for source in source_config.get("sources", [])]
    if len(source_ids) != len(set(source_ids)):
        errors.append("Duplicate catalog source IDs")

    axiology_data = load_json(ROOT / "data" / "curated" / "axiologies.json")
    axiologies = axiology_data.get("axiologies", [])
    axiology_ids = [row.get("id") for row in axiologies]
    if len(axiology_ids) != len(set(axiology_ids)):
        errors.append("Duplicate axiology IDs")
    for row in axiologies:
        for field in ("id", "name", "family", "origin_domain", "representation_type", "interpretability", "status", "primary_sources"):
            if field not in row:
                errors.append(f"Axiology {row.get('id', '<unknown>')} missing {field}")
        for url in row.get("primary_sources", []):
            if not valid_url(url):
                errors.append(f"Axiology {row.get('id')} has invalid URL: {url}")
        count = row.get("dimension_count")
        dims = row.get("dimensions", [])
        if count is not None and dims and count != len(dims):
            errors.append(f"Axiology {row.get('id')} dimension_count={count}, dimensions={len(dims)}")

    instruments = load_json(ROOT / "data" / "curated" / "instruments.json").get("instruments", [])
    instrument_ids = [row.get("id") for row in instruments]
    if len(instrument_ids) != len(set(instrument_ids)):
        errors.append("Duplicate instrument IDs")
    for row in instruments:
        for axiology_id in row.get("axiology_ids", []):
            if axiology_id not in axiology_ids:
                errors.append(f"Instrument {row.get('id')} references unknown axiology {axiology_id}")
        if not valid_url(row.get("primary_url", "")):
            errors.append(f"Instrument {row.get('id')} has invalid primary_url")

    links = load_jsonl(ROOT / "data" / "raw" / "catalog_links.jsonl")
    link_ids = set()
    link_urls = set()
    for row in links:
        if row.get("id") in link_ids:
            errors.append(f"Duplicate link ID {row.get('id')}")
        link_ids.add(row.get("id"))
        if row.get("url") in link_urls:
            errors.append(f"Duplicate link URL {row.get('url')}")
        link_urls.add(row.get("url"))
        if not valid_url(row.get("url", "")):
            errors.append(f"Invalid link URL {row.get('url')}")
        if row.get("link_type_guess") == "publication":
            year = row.get("publication_year")
            if not isinstance(year, int) or not 1950 <= year <= 2026:
                errors.append(f"Publication {row.get('id')} has missing or invalid year: {year}")
            title = (row.get("context_title") or row.get("label") or "").strip()
            if not title or title.lower() in {"paper", "pdf", "link"} or re.fullmatch(r"(?:\d{4}\.[\w.-]+/?|\d{6,}\.\d{6,})", title):
                errors.append(f"Publication {row.get('id')} has a weak title: {title}")
        parsed_url = urllib.parse.urlsplit(row.get("url", ""))
        if parsed_url.netloc == "openreview.net" and parsed_url.path in {"/forum", "/pdf"}:
            if not urllib.parse.parse_qs(parsed_url.query).get("id"):
                errors.append(f"OpenReview identity URL lost its id parameter: {row.get('url')}")
        for occurrence in row.get("occurrences", []):
            if occurrence.get("catalog_id") not in source_ids:
                errors.append(f"Link {row.get('id')} references unknown catalog {occurrence.get('catalog_id')}")

    for readme_name in ("README.md", "README_RU.md"):
        readme = (ROOT / readme_name).read_text()
        catalog = readme.split("<!-- complete-catalog:start -->", 1)[-1].split("<!-- complete-catalog:end -->", 1)[0]
        catalog_urls = re.findall(r"\]\((https?://[^)]+)\)", catalog)
        catalog_url_counts = {url: catalog_urls.count(url) for url in set(catalog_urls)}
        missing_readme_urls = sorted(row["url"] for row in links if row.get("url") not in catalog_url_counts)
        if missing_readme_urls:
            errors.append(f"{readme_name} complete catalog is missing {len(missing_readme_urls)} discovered URLs")
        duplicate_readme_urls = [row["url"] for row in links if catalog_url_counts.get(row["url"]) != 1]
        if duplicate_readme_urls:
            errors.append(f"{readme_name} complete catalog has {len(duplicate_readme_urls)} URLs appearing other than once")
        if "<sub>" in catalog or re.search(r"^- \*\*\[", catalog, re.M):
            errors.append(f"{readme_name} catalog uses the deprecated mixed-font or linked-title format")
    if "README_RU.md" not in (ROOT / "README.md").read_text() or "README.md" not in (ROOT / "README_RU.md").read_text():
        errors.append("README language switch is incomplete")

    models = load_jsonl(ROOT / "data" / "curated" / "models.jsonl")
    model_ids = [row.get("id") for row in models]
    if len(model_ids) != len(set(model_ids)):
        errors.append("Duplicate model IDs")
    for row in models:
        for axiology_id in row.get("axiology_ids", []):
            if axiology_id not in axiology_ids:
                errors.append(f"Model {row.get('id')} references unknown axiology {axiology_id}")
        if not valid_url(row.get("primary_url", "")):
            errors.append(f"Model {row.get('id')} has invalid primary_url")

    datasets = load_jsonl(ROOT / "data" / "curated" / "datasets.jsonl")
    dataset_ids = [row.get("id") for row in datasets]
    if len(dataset_ids) != len(set(dataset_ids)):
        errors.append("Duplicate dataset IDs")
    for row in datasets:
        for axiology_id in row.get("axiology_ids", []):
            if axiology_id not in axiology_ids:
                errors.append(f"Dataset {row.get('id')} references unknown axiology {axiology_id}")
        for instrument_id in row.get("instrument_ids", []):
            if instrument_id not in instrument_ids:
                errors.append(f"Dataset {row.get('id')} references unknown instrument {instrument_id}")
        if not valid_url(row.get("primary_url", "")):
            errors.append(f"Dataset {row.get('id')} has invalid primary_url")

    works = load_jsonl(ROOT / "data" / "curated" / "works.jsonl")
    work_ids = [row.get("id") for row in works]
    if len(work_ids) != len(set(work_ids)):
        errors.append("Duplicate work IDs")
    for row in works:
        for field in ("id", "title", "year", "primary_url", "work_types", "research_roles", "scope_tier", "source_catalogs", "curation"):
            if field not in row:
                errors.append(f"Work {row.get('id', '<unknown>')} missing {field}")
        if not valid_url(row.get("primary_url", "")):
            errors.append(f"Work {row.get('id')} has invalid primary_url")
        for source_id in row.get("source_catalogs", []):
            if source_id not in source_ids:
                errors.append(f"Work {row.get('id')} references unknown source {source_id}")

    studies = load_jsonl(ROOT / "data" / "curated" / "studies.jsonl")
    study_ids = [row.get("id") for row in studies]
    if len(study_ids) != len(set(study_ids)):
        errors.append("Duplicate study IDs")
    for row in studies:
        if row.get("work_id") not in work_ids:
            errors.append(f"Study {row.get('id')} references unknown work {row.get('work_id')}")
        for usage in row.get("axiology_usages", []):
            axiology_id = usage.get("axiology_id")
            if axiology_id is not None and axiology_id not in axiology_ids:
                errors.append(f"Study {row.get('id')} references unknown axiology {axiology_id}")
            if axiology_id is None and usage.get("model_status") not in {"implicit", "none"}:
                errors.append(f"Study {row.get('id')} has null axiology without implicit/none status")
        for dataset_id in row.get("dataset_ids", []):
            if dataset_id not in dataset_ids:
                errors.append(f"Study {row.get('id')} references unknown dataset {dataset_id}")
        for instrument_id in row.get("instrument_ids", []):
            if instrument_id not in instrument_ids:
                errors.append(f"Study {row.get('id')} references unknown instrument {instrument_id}")
        for relation in row.get("model_relations", []):
            if relation.get("model_id") not in model_ids:
                errors.append(f"Study {row.get('id')} references unknown model {relation.get('model_id')}")

    site_data = load_json(ROOT / "site" / "data.json")
    site_links = site_data.get("links", [])
    if len(site_links) != len(links):
        errors.append(f"Site index has {len(site_links)} links but raw catalog has {len(links)}")
    site_publications = [row for row in site_links if row.get("link_type_guess") == "publication"]
    if any(not row.get("research_class") or not row.get("research_class_id") for row in site_publications):
        errors.append("Site publication index has entries without a research class")
    featured_count = sum(bool(row.get("featured")) for row in site_publications)
    if not 0 < featured_count < len(site_publications):
        errors.append(f"Site featured-work count is implausible: {featured_count}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"VALIDATION PASSED: {len(source_ids)} catalogs, {len(links)} discovered links, "
        f"{len(axiologies)} axiologies, {len(instruments)} instruments, "
        f"{len(models)} models, {len(datasets)} datasets, {len(works)} works, {len(studies)} studies"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
