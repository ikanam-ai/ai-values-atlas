#!/usr/bin/env python3
"""Import link facts from a BibTeX file into a provenance-preserving seed.

This deliberately extracts only citation keys, titles, URLs, and DOI links. It
does not copy abstracts or annotations from the manuscript or source catalogs.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data" / "seed" / "stonic_bibliography_links.jsonl"
ENTRY_START = re.compile(r"@\w+\s*\{\s*([^,]+),", re.I)
FIELD_START = re.compile(r"^\s*([A-Za-z][\w-]*)\s*=\s*(.*)$")


def split_entries(text: str) -> list[tuple[int, str, str]]:
    starts = list(ENTRY_START.finditer(text))
    result = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        line = text.count("\n", 0, match.start()) + 1
        result.append((line, match.group(1).strip(), text[match.end():end]))
    return result


def fields_from(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_name = None
    current_parts: list[str] = []
    balance = 0

    def flush() -> None:
        nonlocal current_name, current_parts, balance
        if current_name:
            value = " ".join(current_parts).strip().rstrip(",").strip()
            if value.startswith("{") and value.endswith("}"):
                value = value[1:-1]
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            value = re.sub(r"\s+", " ", value).strip()
            fields[current_name] = value
        current_name, current_parts, balance = None, [], 0

    for raw in body.splitlines():
        match = FIELD_START.match(raw)
        if match and (current_name is None or balance <= 0):
            flush()
            current_name = match.group(1).lower()
            current_parts = [match.group(2)]
            balance = match.group(2).count("{") - match.group(2).count("}")
            if balance <= 0:
                flush()
        elif current_name:
            current_parts.append(raw.strip())
            balance += raw.count("{") - raw.count("}")
            if balance <= 0:
                flush()
    flush()
    return fields


def clean_title(value: str) -> str:
    value = value.replace("{", "").replace("}", "")
    value = value.replace("\\&", "&").replace("~", " ")
    return re.sub(r"\\['\"`^~=.Hckbdrvu]\s*([A-Za-z])", r"\1", value)


def primary_url(fields: dict[str, str]) -> str | None:
    url = fields.get("url", "").strip()
    if url.startswith(("http://", "https://")):
        return url
    doi = fields.get("doi", "").strip()
    if doi.startswith("https://doi.org/"):
        return doi
    if doi:
        return f"https://doi.org/{doi}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bibtex", type=pathlib.Path)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = []
    seen = set()
    entries = split_entries(args.bibtex.read_text(errors="replace"))
    for line, citation_key, body in entries:
        fields = fields_from(body)
        url = primary_url(fields)
        if not url or url in seen:
            continue
        seen.add(url)
        rows.append(
            {
                "url": url,
                "label": "paper",
                "context_title": clean_title(fields.get("title", citation_key)),
                "citation_key": citation_key,
                "section": "STONIC references",
                "source_line": line,
                "scope_tier_guess": "core",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"Imported {len(rows)} linked citations from {len(entries)} BibTeX entries into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
