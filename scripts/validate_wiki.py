#!/usr/bin/env python3
"""Validate generated wiki coverage, navigation, anchors, and local links."""

from __future__ import annotations

import json
import pathlib
import urllib.parse
from html.parser import HTMLParser


ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
LEARN = SITE / "learn"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()
        self.title_parts: list[str] = []
        self.in_title = False
        self.canonical: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        if tag == "title":
            self.in_title = True
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def target_file(page: pathlib.Path, href: str) -> pathlib.Path | None:
    parsed = urllib.parse.urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    if not parsed.path:
        return page
    target = (page.parent / urllib.parse.unquote(parsed.path)).resolve()
    if parsed.path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    manifest = json.loads((LEARN / "wiki-manifest.json").read_text())
    search = json.loads((LEARN / "search.json").read_text())
    axiologies = json.loads((ROOT / "data" / "curated" / "axiologies.json").read_text())["axiologies"]
    content = json.loads((ROOT / "data" / "wiki_content.json").read_text())
    pages = [LEARN / path for path in manifest.get("pages", [])]

    expected_count = 1 + len(axiologies) + len(content["guide_pages"])
    if len(pages) != expected_count:
        errors.append(f"Expected {expected_count} wiki pages, found {len(pages)}")
    if len(search) != expected_count - 1:
        errors.append(f"Expected {expected_count - 1} searchable pages, found {len(search)}")
    axiology_pages = [path for path in pages if "axiologies" in path.parts]
    if len(axiology_pages) != len(axiologies):
        errors.append(f"Expected {len(axiologies)} axiology pages, found {len(axiology_pages)}")

    search_ids = [row.get("id") for row in search]
    expected_ids = {row["id"] for row in axiologies} | {row["id"] for row in content["guide_pages"]}
    if set(search_ids) != expected_ids:
        errors.append("Wiki search index does not cover every source page exactly")
    if len(search_ids) != len(set(search_ids)):
        errors.append("Wiki search index contains duplicate IDs")

    titles: set[str] = set()
    canonicals: set[str] = set()
    site_root = SITE.resolve()
    for page in pages:
        if not page.exists():
            errors.append(f"Missing generated page: {page.relative_to(ROOT)}")
            continue
        parser = PageParser()
        parser.feed(page.read_text())
        title = "".join(parser.title_parts).strip()
        if not title:
            errors.append(f"Missing title: {page.relative_to(ROOT)}")
        elif title in titles:
            errors.append(f"Duplicate page title: {title}")
        titles.add(title)
        if not parser.canonical:
            errors.append(f"Missing canonical link: {page.relative_to(ROOT)}")
        elif parser.canonical in canonicals:
            errors.append(f"Duplicate canonical link: {parser.canonical}")
        canonicals.add(parser.canonical or "")

        text = page.read_text()
        if page != LEARN / "index.html":
            for marker in ("breadcrumbs", "article-toc", "prev-next"):
                if marker not in text:
                    errors.append(f"{page.relative_to(ROOT)} missing {marker}")
        if "../#browse" in text or 'href="#browse"' in text:
            errors.append(f"{page.relative_to(ROOT)} contains obsolete #browse link")

        for href in parser.hrefs:
            parsed_href = urllib.parse.urlsplit(href)
            if parsed_href.path == "" and parsed_href.fragment:
                if parsed_href.fragment not in parser.ids:
                    errors.append(f"Broken anchor {href} in {page.relative_to(ROOT)}")
                continue
            target = target_file(page, href)
            if target is None:
                continue
            try:
                target.relative_to(site_root)
            except ValueError:
                errors.append(f"Local link escapes site root: {href} in {page.relative_to(ROOT)}")
                continue
            if not target.exists():
                errors.append(f"Broken local link {href} in {page.relative_to(ROOT)}")

    if errors:
        print("WIKI VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"WIKI VALIDATION PASSED: {len(pages)} pages, {len(axiology_pages)} axiologies, {len(search)} search records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
