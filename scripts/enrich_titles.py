#!/usr/bin/env python3
"""Resolve weak discovery titles from primary publication pages.

The result is a small, reviewable URL-to-title map. It is committed so normal
catalog rebuilds remain deterministic and do not require network access.
"""

from __future__ import annotations

import html
import json
import pathlib
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINKS = ROOT / "data" / "raw" / "catalog_links.jsonl"
OUTPUT = ROOT / "data" / "title_overrides.json"
WEAK_RE = re.compile(r"^(?:\d{4}\.\d{4,5}(?:v\d+)?|\d{4}\.[\w.-]+|paper\d*|collection|leaderboard|hf datasets|hg & ci)$", re.I)


def read_jsonl(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def is_weak(row: dict) -> bool:
    title = (row.get("context_title") or row.get("label") or "").strip()
    publication_host = urllib.parse.urlsplit(row.get("url", "")).netloc.removeprefix("www.") in {
        "arxiv.org", "browse.arxiv.org", "aclanthology.org"
    }
    return publication_host and (bool(WEAK_RE.fullmatch(title)) or title.startswith("http"))


def request(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-Values-Atlas/1.0 (https://github.com/ikanam-ai/ai-values-atlas)"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def html_title(url: str) -> str | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.removeprefix("www.") == "browse.arxiv.org":
        identifier = pathlib.PurePosixPath(parsed.path).name.removesuffix(".pdf")
        url = f"https://arxiv.org/abs/{identifier}"
    page = request(url).decode("utf-8", errors="replace")
    patterns = [
        r'<meta[^>]+name=["\']citation_title["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)',
        r"<title[^>]*>(.*?)</title>",
    ]
    for pattern in patterns:
        match = re.search(pattern, page, re.I | re.S)
        if match:
            title = re.sub(r"\s+", " ", html.unescape(match.group(1))).strip()
            title = re.sub(r"\s*[|–—-]\s*(ACL Anthology|arXiv).*?$", "", title, flags=re.I)
            if len(title) > 8:
                return title
    return None


def main() -> int:
    rows = [row for row in read_jsonl(LINKS) if is_weak(row)]
    overrides = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {}

    def resolve(row: dict) -> tuple[str, str | None, str | None]:
        try:
            return row["url"], html_title(row["url"]), None
        except Exception as exc:  # noqa: BLE001 - keep a partial, reviewable enrichment
            return row["url"], None, str(exc)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(resolve, row) for row in rows]
        for future in as_completed(futures):
            url, title, error = future.result()
            if title:
                overrides[url] = title
            elif error:
                print(f"WARN {url}: {error}")

    OUTPUT.write_text(json.dumps(dict(sorted(overrides.items())), indent=2, ensure_ascii=False) + "\n")
    unresolved = [row["url"] for row in rows if row["url"] not in overrides]
    print(f"Resolved {len(rows) - len(unresolved)}/{len(rows)} weak titles; {len(overrides)} overrides stored")
    for url in unresolved:
        print(f"UNRESOLVED {url}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
