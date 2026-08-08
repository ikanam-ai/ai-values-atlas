#!/usr/bin/env python3
"""Harvest links and section provenance from selected public catalog sections.

Only link facts are collected: URL, link label, source catalog, section, and line.
Third-party summaries and descriptions are deliberately not copied.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import pathlib
import re
import urllib.parse
from collections import defaultdict


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "data" / "catalog_sources.json"
DEFAULT_CACHE = ROOT / ".cache" / "catalog-sources"
OUTPUT = ROOT / "data" / "raw" / "catalog_links.jsonl"
REPORT = ROOT / "data" / "raw" / "harvest_report.json"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[{1,2}([^\]]+)\]\]?\((https?://[^\s)]+)\)")
HTML_LINK_RE = re.compile(r"<a\s+[^>]*href=[\"'](https?://[^\"']+)[\"'][^>]*>(.*?)</a>", re.I)
BARE_URL_RE = re.compile(r"https?://[^\s<>)\]]+")
TAG_RE = re.compile(r"<[^>]+>")
MARKUP_RE = re.compile(r"[*_`~]+")

SKIP_DOMAINS = {
    "img.shields.io",
    "cdn.rawgit.com",
    "raw.githubusercontent.com",
    "camo.githubusercontent.com",
    "user-images.githubusercontent.com",
}

GENERIC_LABELS = {
    "paper", "pdf", "code", "github", "dataset", "data", "model", "project",
    "project page", "website", "source", "link", "homepage", "repo", "repository",
}


def clean_text(value: str) -> str:
    value = html.unescape(TAG_RE.sub(" ", value))
    value = MARKUP_RE.sub("", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" |:-\t")


def normalize_heading(value: str) -> str:
    value = clean_text(value)
    value = re.sub(r"<a\s+name=.*?</a>", "", value, flags=re.I)
    value = re.sub(r"[^a-zA-Z0-9&+]+", " ", value).strip().lower()
    value = re.sub(r"^\d+(?:\s+\d+)*\s+", "", value)
    return value


def canonicalize_url(raw: str) -> str:
    raw = html.unescape(raw).strip().rstrip(".,;")
    parsed = urllib.parse.urlsplit(raw)
    scheme = parsed.scheme.lower()
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/{2,}", "/", parsed.path)

    if host == "arxiv.org":
        match = re.match(r"/(?:abs|pdf)/([^/]+?)(?:\.pdf)?$", path)
        if match:
            identifier = re.sub(r"v\d+$", "", match.group(1))
            path = f"/abs/{identifier}"
    elif host == "aclanthology.org":
        path = re.sub(r"\.pdf$", "", path).rstrip("/") + "/"
    elif host == "doi.org":
        path = path.lower().rstrip("/")
    elif host == "github.com":
        path = path.rstrip("/")

    return urllib.parse.urlunsplit((scheme, host, path, "", ""))


def should_skip(url: str) -> bool:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower().removeprefix("www.")
    if host in SKIP_DOMAINS:
        return True
    lowered = parsed.path.lower()
    return lowered.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"))


def classify_link(url: str, label: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.lower()
    low_label = label.lower()

    if host == "huggingface.co":
        return "dataset" if path.startswith("/datasets/") else "model"
    if host == "github.com" or host == "gitlab.com":
        return "repository"
    if host in {"arxiv.org", "doi.org", "aclanthology.org", "openreview.net"}:
        return "publication"
    if any(key in host for key in ("springer", "nature.com", "sciencedirect", "wiley", "tandfonline", "sagepub", "aaai.org", "neurips.cc", "jmlr.org", "acm.org", "ieee.org")):
        return "publication"
    if "dataset" in low_label or "/dataset" in path:
        return "dataset"
    if "model" in low_label or "/models/" in path:
        return "model"
    if any(key in host for key in ("worldvaluessurvey", "europeanvaluesstudy", "gss.norc", "globeproject")):
        return "survey_resource"
    if "project" in low_label or "website" in low_label:
        return "project"
    return "other"


def included(section: str, source: dict) -> bool:
    include = source.get("include_heading_patterns", [".*"])
    exclude = source.get("exclude_heading_patterns", [])
    if any(re.search(pattern, section, re.I) for pattern in exclude):
        return False
    return any(re.search(pattern, section, re.I) for pattern in include)


def context_title(links: list[tuple[str, str]]) -> str:
    for label, _ in links:
        cleaned = clean_text(label)
        if cleaned and cleaned.lower() not in GENERIC_LABELS and len(cleaned) > 5:
            return cleaned
    return ""


def extract_links(line: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    seen = set()
    for match in MARKDOWN_LINK_RE.finditer(line):
        pair = (clean_text(match.group(1)), match.group(2))
        if pair[1] not in seen:
            result.append(pair)
            seen.add(pair[1])
    for match in HTML_LINK_RE.finditer(line):
        pair = (clean_text(match.group(2)), match.group(1))
        if pair[1] not in seen:
            result.append(pair)
            seen.add(pair[1])
    for match in BARE_URL_RE.finditer(line):
        url = match.group(0).rstrip(".,;\"'")
        if url not in seen:
            host = urllib.parse.urlsplit(url).netloc.removeprefix("www.")
            result.append((host, url))
            seen.add(url)
    return result


def harvest_source(source: dict, cache: pathlib.Path) -> list[dict]:
    readme = cache / source["id"] / source["readme"]
    if not readme.exists():
        raise FileNotFoundError(f"Missing {readme}; run scripts/sync_sources.py first")

    headings: dict[int, str] = {}
    harvested = []
    for line_number, raw in enumerate(readme.read_text(errors="replace").splitlines(), start=1):
        heading_match = HEADING_RE.match(raw.strip())
        if heading_match:
            level = len(heading_match.group(1))
            headings = {key: value for key, value in headings.items() if key < level}
            headings[level] = normalize_heading(heading_match.group(2))
            continue

        section = " / ".join(headings[key] for key in sorted(headings) if headings[key])
        if not included(section, source):
            continue

        links = extract_links(raw)
        if not links:
            continue
        row_title = context_title(links)

        for label, raw_url in links:
            url = canonicalize_url(raw_url)
            if should_skip(url):
                continue
            harvested.append(
                {
                    "url": url,
                    "label": label,
                    "context_title": row_title,
                    "link_type_guess": classify_link(url, label),
                    "scope_tier_guess": source["scope_tier_guess"],
                    "occurrence": {
                        "catalog_id": source["id"],
                        "section": section,
                        "line": line_number,
                    },
                }
            )
    return harvested


def harvest_snapshot(source: dict) -> list[dict]:
    path = ROOT / source["seed_file"]
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}; import the bibliography snapshot first")
    rows = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        item = json.loads(line)
        url = canonicalize_url(item["url"])
        if should_skip(url):
            continue
        rows.append(
            {
                "url": url,
                "label": item.get("label", "paper"),
                "context_title": item.get("context_title", ""),
                "link_type_guess": item.get("link_type_guess") or classify_link(url, item.get("label", "paper")),
                "scope_tier_guess": item.get("scope_tier_guess", source["scope_tier_guess"]),
                "occurrence": {
                    "catalog_id": source["id"],
                    "section": item.get("section", "references"),
                    "line": item.get("source_line", line_number),
                },
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=pathlib.Path, default=DEFAULT_CACHE)
    args = parser.parse_args()

    config = json.loads(CONFIG.read_text())
    by_url: dict[str, dict] = {}
    per_source = defaultdict(int)

    for source in config["sources"]:
        if source.get("kind", "git_readme") == "local_bibliography_snapshot":
            rows = harvest_snapshot(source)
        else:
            rows = harvest_source(source, args.cache)
        per_source[source["id"]] += len(rows)
        for row in rows:
            url = row.pop("url")
            occurrence = row.pop("occurrence")
            if url not in by_url:
                digest = hashlib.sha256(url.encode()).hexdigest()[:16]
                by_url[url] = {"id": f"link-{digest}", "url": url, **row, "occurrences": []}
            record = by_url[url]
            record["occurrences"].append(occurrence)
            if record["label"].lower() in GENERIC_LABELS and row["label"].lower() not in GENERIC_LABELS:
                record["label"] = row["label"]
            if not record["context_title"] and row["context_title"]:
                record["context_title"] = row["context_title"]
            if row["scope_tier_guess"] == "core":
                record["scope_tier_guess"] = "core"

    records = sorted(by_url.values(), key=lambda item: (item["link_type_guess"], item["context_title"].lower(), item["url"]))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    report = {
        "schema_version": "1.0.0",
        "unique_links": len(records),
        "by_type": dict(sorted((key, sum(r["link_type_guess"] == key for r in records)) for key in {r["link_type_guess"] for r in records})),
        "by_scope": dict(sorted((key, sum(r["scope_tier_guess"] == key for r in records)) for key in {r["scope_tier_guess"] for r in records})),
        "harvested_occurrences_by_source": dict(sorted(per_source.items())),
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
