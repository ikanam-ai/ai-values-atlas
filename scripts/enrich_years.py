#!/usr/bin/env python3
"""Resolve missing publication years from primary metadata endpoints."""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import difflib
import json
import pathlib
import re
import urllib.parse
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINKS = ROOT / "data" / "raw" / "catalog_links.jsonl"
OVERRIDES = ROOT / "data" / "year_overrides.json"
USER_AGENT = "AI-Values-Atlas/1.0 (https://github.com/ikanam-ai/ai-values-atlas)"


def fetch(url: str, accept: str = "text/html,application/json") -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    with urllib.request.urlopen(request, timeout=18) as response:
        return response.read(2_000_000), response.headers.get("content-type", "")


def valid_year(value: object) -> int | None:
    try:
        year = int(str(value)[:4])
    except (TypeError, ValueError):
        return None
    return year if 1950 <= year <= dt.date.today().year else None


def year_from_crossref_message(message: dict) -> int | None:
    for key in ("published-print", "published-online", "published", "issued", "created"):
        parts = message.get(key, {}).get("date-parts", [])
        if parts and parts[0]:
            year = valid_year(parts[0][0])
            if year:
                return year
    return None


def doi_from_url(url: str) -> str | None:
    decoded = urllib.parse.unquote(url)
    match = re.search(r"(?:doi\.org/|/doi/(?:abs/|full/)?)(10\.\d{4,9}/[^?#]+)", decoded, re.I)
    return match.group(1).rstrip("/") if match else None


def crossref_doi_year(doi: str) -> int | None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    body, _ = fetch(url, "application/json")
    return year_from_crossref_message(json.loads(body)["message"])


def openreview_year(url: str) -> int | None:
    paper_id = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).get("id", [None])[0]
    if not paper_id:
        return None
    api = "https://api2.openreview.net/notes?id=" + urllib.parse.quote(paper_id)
    body, _ = fetch(api, "application/json")
    notes = json.loads(body).get("notes", [])
    for note in notes:
        for key in ("pdate", "cdate", "tcdate"):
            stamp = note.get(key)
            if stamp:
                return dt.datetime.fromtimestamp(stamp / 1000, tz=dt.timezone.utc).year
    return None


def html_year(url: str) -> int | None:
    body, content_type = fetch(url)
    if "html" not in content_type and not body.lstrip().startswith(b"<"):
        return None
    text = body.decode("utf-8", errors="replace")
    patterns = (
        r'<meta[^>]+(?:name|property)=["\'](?:citation_publication_date|citation_date|dc\.date|article:published_time|date)["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:name|property)=["\'](?:citation_publication_date|citation_date|dc\.date|article:published_time|date)["\']',
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'<time[^>]+datetime=["\']([^"\']+)',
    )
    for pattern in patterns:
        for value in re.findall(pattern, text, re.I):
            year = valid_year(value)
            if year:
                return year
    return None


def crossref_title_year(title: str) -> int | None:
    query = urllib.parse.urlencode({"query.title": title, "rows": 3, "select": "title,published-print,published-online,published,issued,created"})
    body, _ = fetch("https://api.crossref.org/works?" + query, "application/json")
    target = re.sub(r"\W+", " ", title).lower().strip()
    for item in json.loads(body)["message"]["items"]:
        candidate = " ".join(item.get("title", []))
        normalized = re.sub(r"\W+", " ", candidate).lower().strip()
        if difflib.SequenceMatcher(None, target, normalized).ratio() >= 0.82:
            year = year_from_crossref_message(item)
            if year:
                return year
    return None


def resolve(row: dict) -> tuple[str, int | None, str]:
    url = row["url"]
    title = row.get("context_title") or row.get("label") or ""
    methods = []
    doi = doi_from_url(url)
    if doi:
        methods.append(("crossref-doi", lambda: crossref_doi_year(doi)))
    if urllib.parse.urlsplit(url).netloc == "openreview.net":
        methods.append(("openreview", lambda: openreview_year(url)))
    methods.extend((("html", lambda: html_year(url)), ("crossref-title", lambda: crossref_title_year(title))))
    for method, operation in methods:
        try:
            year = operation()
        except Exception:  # noqa: BLE001 - continue through independent metadata sources
            continue
        if year:
            return url, year, method
    return url, None, "unresolved"


def main() -> int:
    rows = [json.loads(line) for line in LINKS.read_text().splitlines() if line.strip()]
    overrides = json.loads(OVERRIDES.read_text()) if OVERRIDES.exists() else {}
    missing = [row for row in rows if row.get("link_type_guess") == "publication" and not row.get("publication_year") and row["url"] not in overrides]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(resolve, missing))
    for url, year, method in results:
        print(f"{year or '?'}\t{method}\t{url}")
        if year:
            overrides[url] = year
    OVERRIDES.write_text(json.dumps(dict(sorted(overrides.items())), indent=2, ensure_ascii=False) + "\n")
    print(f"Resolved {sum(year is not None for _, year, _ in results)}/{len(results)}; {len(overrides)} overrides stored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
