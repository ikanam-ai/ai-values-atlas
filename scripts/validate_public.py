#!/usr/bin/env python3
"""Validate the content-first public Atlas without rebuilding generated files."""

from __future__ import annotations

import json
import pathlib
import re
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKS_PATH = ROOT / "data" / "works.jsonl"
RESOURCES_PATH = ROOT / "data" / "resources.jsonl"
SITE_DATA_PATH = ROOT / "site" / "data.json"


def read_jsonl(path: pathlib.Path) -> list[dict]:
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
    works = read_jsonl(WORKS_PATH)
    resources = read_jsonl(RESOURCES_PATH)
    site_data = json.loads(SITE_DATA_PATH.read_text())
    readme = (ROOT / "README.md").read_text()

    if len(works) != 701:
        errors.append(f"Expected 701 research works, found {len(works)}")
    if len(resources) != 94:
        errors.append(f"Expected 94 independent resources, found {len(resources)}")

    work_ids = [row.get("id") for row in works]
    resource_ids = [row.get("id") for row in resources]
    if len(work_ids) != len(set(work_ids)):
        errors.append("Duplicate work IDs")
    if len(resource_ids) != len(set(resource_ids)):
        errors.append("Duplicate independent-resource IDs")

    domains = {row["id"] for row in site_data.get("domains", [])}
    if len(domains) != 10:
        errors.append(f"Expected 10 research domains, found {len(domains)}")

    allowed_status = {"published", "preprint"}
    allowed_roles = {
        "paper", "preprint", "paper version", "code", "dataset", "model",
        "prompts", "outputs", "analysis", "project", "supplement", "instrument",
        "book", "catalog", "course", "policy", "reference",
    }
    for row in works:
        for field in ("id", "title", "year", "domains", "contribution_types", "links"):
            if field not in row:
                errors.append(f"Work {row.get('id', '<unknown>')} missing {field}")
        forbidden_editorial_fields = {
            "rankings", "domain_score", "scientific_contribution",
            "field_relevance", "influence", "score_formula",
            "description", "limitations",
        }
        present_editorial_fields = forbidden_editorial_fields.intersection(row)
        if present_editorial_fields:
            errors.append(
                f"Work {row.get('id')} exposes internal editorial fields: "
                f"{', '.join(sorted(present_editorial_fields))}"
            )
        if row.get("publication_status") not in allowed_status:
            errors.append(f"Work {row.get('id')} has invalid publication status")
        if not row.get("links"):
            errors.append(f"Work {row.get('id')} has no links")
        for domain in row.get("domains", []):
            if domain not in domains:
                errors.append(f"Work {row.get('id')} references unknown domain {domain}")
        for link in row.get("links", []):
            if link.get("label") not in allowed_roles:
                errors.append(f"Work {row.get('id')} has unsupported link role {link.get('label')}")
            if not valid_url(link.get("url", "")):
                errors.append(f"Work {row.get('id')} has invalid URL {link.get('url')}")

    for row in resources:
        if not valid_url(row.get("url", "")):
            errors.append(f"Resource {row.get('id')} has invalid URL {row.get('url')}")
        if not row.get("roles") or not row.get("kind"):
            errors.append(f"Resource {row.get('id')} lacks a content type")

    site_work_ids = [row.get("id") for row in site_data.get("works", [])]
    site_resource_ids = [row.get("id") for row in site_data.get("standalone_resources", [])]
    if site_work_ids != work_ids:
        errors.append("site/data.json work records differ from data/works.jsonl")
    if site_resource_ids != resource_ids:
        errors.append("site/data.json resource records differ from data/resources.jsonl")
    if "score_formula" in site_data:
        errors.append("site/data.json exposes the removed editorial score formula")
    if any("description" in row or "limitations" in row for row in site_data.get("works", [])):
        errors.append("site/data.json exposes internal work descriptions or limitations")

    stats = site_data.get("stats", {})
    expected_stats = {
        "research_works": 701,
        "domains": 10,
        "source_links": 1013,
        "work_resource_relations": 943,
        "standalone_resources": 94,
    }
    if stats != expected_stats:
        errors.append(f"Site statistics differ from the frozen public release: {stats}")

    required_sections = (
        "## 🧭 Field map",
        "## 🧠 Axiologies and value spaces",
        "## 💾 Datasets, benchmarks, and instruments",
        "## 🧰 Models, scorers, and representation tools",
        "## 📚 Literature by research domain",
        "## 🧩 Independent resources",
    )
    for section in required_sections:
        if section not in readme:
            errors.append(f"README is missing {section}")
    for row in works:
        if row["title"] not in readme:
            errors.append(f"README is missing work title: {row['title']}")

    literature = readme.split("## 📚 Literature by research domain", 1)[-1].split(
        "## 🧩 Independent resources", 1
    )[0]
    expected_domain_entries = sum(len(row.get("domains", [])) for row in works)
    listed_domain_entries = len(re.findall(r"^- [⭐📄] ", literature, flags=re.M))
    if listed_domain_entries != expected_domain_entries:
        errors.append(
            f"README lists {listed_domain_entries} domain entries; "
            f"expected all {expected_domain_entries}"
        )
    if re.search(r"^\s{2,}- ", literature, flags=re.M):
        errors.append("README literature list contains nested editorial descriptions")
    if "<details>" in literature:
        errors.append("README literature list is collapsed")

    independent = readme.split("## 🧩 Independent resources", 1)[-1].split(
        "## 🤝 Contributing", 1
    )[0]
    listed_resources = len(re.findall(r"^- .+, \[\[[a-z ]+\]\(https?://", independent, flags=re.M))
    if listed_resources != len(resources):
        errors.append(
            f"README lists {listed_resources} independent resources; expected {len(resources)}"
        )

    public_files = [
        ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "site" / "index.html",
        ROOT / "site" / "app.js", ROOT / "site" / "styles.css", WORKS_PATH,
        RESOURCES_PATH, SITE_DATA_PATH,
    ]
    forbidden = {
        "internal stage M1": r"\bM1\b",
        "internal stage M2": r"\bM2\b",
        "internal stage M3": r"\bM3\b",
        "featured label": r"\bfeatured\b",
        "metadata-check label": r"metadata (?:checked|verified)",
        "editorial score label": r"(?:domain|contribution|relevance|influence) score|/\s*100",
        "collapsed literature list": r"Show all \d+ works in this domain",
    }
    for path in public_files:
        text = path.read_text()
        for label, pattern in forbidden.items():
            if re.search(pattern, text, flags=re.I):
                errors.append(f"{path.relative_to(ROOT)} contains forbidden {label}")

    for local_path in (ROOT / "site" / "index.html", ROOT / "site" / "app.js", ROOT / "site" / "styles.css"):
        if not local_path.exists() or local_path.stat().st_size == 0:
            errors.append(f"Missing site asset: {local_path.relative_to(ROOT)}")

    if errors:
        print("PUBLIC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PUBLIC VALIDATION PASSED: "
        f"{len(works)} works, {len(domains)} domains, {len(resources)} independent resources, "
        f"{stats['work_resource_relations']} work-resource relations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
