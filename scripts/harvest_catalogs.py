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
TITLE_OVERRIDES = ROOT / "data" / "title_overrides.json"
YEAR_OVERRIDES = ROOT / "data" / "year_overrides.json"

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
    "awesome.re",
    "capsule-render.vercel.app",
    "readme-typing-svg.demolab.com",
}

SKIP_URLS = {
    "https://git.io/typing-svg",
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


def looks_like_markup_fragment(value: str) -> bool:
    """Reject incomplete README decoration accidentally parsed as a title."""
    value = html.unescape(value).strip()
    return bool(
        re.search(
            r"<\s*(?:a|img|picture|source)\b[^>]*(?:href|src)\s*=\s*[\"'][^\"'>]*$",
            value,
            re.I,
        )
        or re.fullmatch(r"(?:href|src)\s*=\s*[\"']?", value, re.I)
    )


def normalize_heading(value: str) -> str:
    value = clean_text(value)
    value = re.sub(r"<a\s+name=.*?</a>", "", value, flags=re.I)
    value = re.sub(r"[^a-zA-Z0-9&+]+", " ", value).strip().lower()
    value = re.sub(r"^\d+(?:\s+\d+)*\s+", "", value)
    return value


def canonicalize_url(raw: str) -> str:
    # Decode escaped ampersands without applying HTML named-entity parsing to
    # query keys such as `noteId` (`&not...` would otherwise become `¬...`).
    raw = raw.replace("&amp;", "&").replace("&#38;", "&").replace("&#x26;", "&")
    raw = raw.strip().rstrip(".,;\\")
    parsed = urllib.parse.urlsplit(raw)
    scheme = parsed.scheme.lower()
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    if host == "browse.arxiv.org":
        host = "arxiv.org"
    if host == "dx.doi.org":
        host = "doi.org"
    if host in {"doi.org", "arxiv.org", "aclanthology.org", "openreview.net"}:
        scheme = "https"
    path = re.sub(r"/{2,}", "/", parsed.path)
    query = ""

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

    query_values = urllib.parse.parse_qs(parsed.query)
    if host == "openreview.net" and query_values.get("id"):
        path = "/forum"
        query = urllib.parse.urlencode({"id": query_values["id"][0]})
    elif host == "papers.ssrn.com" and query_values.get("abstract_id"):
        query = urllib.parse.urlencode({"abstract_id": query_values["abstract_id"][0]})
    elif host.endswith("journals.plos.org") and query_values.get("id"):
        query = urllib.parse.urlencode({"id": query_values["id"][0]})
    elif host in {"books.google.com", "books.google.co.kr"} and query_values.get("id"):
        query = urllib.parse.urlencode({"id": query_values["id"][0]})
    elif host == "microsoft.com" and query_values.get("id"):
        query = urllib.parse.urlencode({"id": query_values["id"][0]})
    elif host == "aeaweb.org" and query_values.get("id"):
        query = urllib.parse.urlencode({"id": query_values["id"][0]})

    return urllib.parse.urlunsplit((scheme, host, path, query, ""))


def infer_publication_year(record: dict, overrides: dict[str, int]) -> int | None:
    if record.get("link_type_guess") != "publication":
        return None
    url = record["url"]
    if url in overrides:
        return int(overrides[url])
    if record.get("year_hint"):
        return int(record["year_hint"])

    match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{2})\d{2}\.", url)
    if match:
        return 2000 + int(match.group(1))
    match = re.search(r"aclanthology\.org/(20\d{2})\.", url)
    if match:
        return int(match.group(1))
    match = re.search(r"aclanthology\.org/[A-Z](\d{2})-", url, re.I)
    if match:
        return 2000 + int(match.group(1))

    text = " ".join((record.get("context_title", ""), record.get("label", "")))
    years = [int(value) for value in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", text)]
    years = [year for year in years if 1950 <= year <= 2026]
    if years:
        return max(years)
    url_years = [int(value) for value in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", url)]
    url_years = [year for year in url_years if 1950 <= year <= 2026]
    if url_years:
        return max(url_years)
    short_year = re.search(r"(?:^|[\s(])['’](\d{2})(?:\D|$)", text)
    if short_year:
        value = int(short_year.group(1))
        return 2000 + value if value <= 26 else 1900 + value

    host = urllib.parse.urlsplit(url).netloc
    if host in {"nature.com", "link.springer.com"}:
        match = re.search(r"-[0]?((?:19|20)?\d{2})-", url)
        if match:
            value = int(match.group(1))
            return value if value >= 1900 else (2000 + value if value <= 26 else 1900 + value)
    return None


def should_skip(url: str) -> bool:
    if url in SKIP_URLS:
        return True
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
    if any(key in host for key in ("springer", "nature.com", "sciencedirect", "wiley", "tandfonline", "sagepub", "aaai.org", "neurips.cc", "jmlr.org", "acm.org", "ieee.org", "mdpi.com")):
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
        looks_like_host = bool(re.fullmatch(r"[\w.-]+\.[a-zA-Z]{2,}", cleaned))
        looks_like_url = cleaned.lower().startswith(("http://", "https://"))
        if cleaned and cleaned.lower() not in GENERIC_LABELS and len(cleaned) > 5 and not looks_like_host and not looks_like_url:
            return cleaned
    return ""


def row_title(raw: str, links: list[tuple[str, str]]) -> str:
    """Recover an unlinked paper title that precedes generic paper/code links."""
    linked_title = context_title(links)
    if linked_title:
        return linked_title

    starts = [match.start() for pattern in (MARKDOWN_LINK_RE, HTML_LINK_RE, BARE_URL_RE) for match in pattern.finditer(raw)]
    prefix = raw[: min(starts)] if starts else raw
    prefix = re.sub(r"^\s*[-*+]\s*", "", prefix)
    prefix = clean_text(prefix)

    # Awesome-list tables frequently keep the title as plain text in the first
    # substantial cell and attach a generic [paper] link in a later cell.
    cells = [re.sub(r"\b(?:19|20)\d{2}(?:-\d{2})?\s*$", "", cell).strip(" :-") for cell in prefix.split("|")]
    candidates = [cell for cell in cells if len(cell) > 5 and re.search(r"[A-Za-z]", cell)]
    if candidates:
        return max(candidates, key=len)
    return prefix if len(prefix) > 5 else ""


def year_hint(raw: str) -> int | None:
    years = [int(value) for value in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", raw)]
    years = [year for year in years if 1950 <= year <= 2026]
    return max(years) if years else None


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
        recovered_title = row_title(raw, links)

        # Decorative HTML in awesome-list headers can expose attribute URLs to
        # the bare-URL fallback.  In that case the recovered "title" is only a
        # broken tag such as ``<a href="`` or ``<img src="``.
        if looks_like_markup_fragment(recovered_title):
            continue

        for label, raw_url in links:
            url = canonicalize_url(raw_url)
            if should_skip(url):
                continue
            harvested.append(
                {
                    "url": url,
                    "label": label,
                    "context_title": recovered_title,
                    "link_type_guess": classify_link(url, label),
                    "scope_tier_guess": source["scope_tier_guess"],
                    "year_hint": year_hint(raw),
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
                "year_hint": item.get("publication_year"),
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
    loaded_titles = json.loads(TITLE_OVERRIDES.read_text()) if TITLE_OVERRIDES.exists() else {}
    loaded_years = json.loads(YEAR_OVERRIDES.read_text()) if YEAR_OVERRIDES.exists() else {}
    title_overrides = {canonicalize_url(url): title for url, title in loaded_titles.items()}
    year_overrides = {canonicalize_url(url): year for url, year in loaded_years.items()}
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
            if not record.get("year_hint") and row.get("year_hint"):
                record["year_hint"] = row["year_hint"]

    records = sorted(by_url.values(), key=lambda item: (item["link_type_guess"], item["context_title"].lower(), item["url"]))
    for record in records:
        if record["url"] in title_overrides:
            record["context_title"] = title_overrides[record["url"]]
        record["publication_year"] = infer_publication_year(record, year_overrides)
        record.pop("year_hint", None)
    records.sort(key=lambda item: (item["link_type_guess"], item["context_title"].lower(), item["url"]))
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
