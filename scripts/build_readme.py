#!/usr/bin/env python3
"""Generate the complete, taxonomy-grouped link catalog inside README.md."""

from __future__ import annotations

import collections
import json
import pathlib
import re
import urllib.parse


ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
LINKS = ROOT / "data" / "raw" / "catalog_links.jsonl"
START = "<!-- complete-catalog:start -->"
END = "<!-- complete-catalog:end -->"

GENERIC = {"paper", "pdf", "code", "github", "dataset", "data", "model", "project", "website", "link", "repository"}

LINK_LABELS = {
    "publication": "paper",
    "dataset": "dataset",
    "model": "model",
    "repository": "code",
    "project": "project",
    "survey_resource": "survey",
    "other": "link",
}

PUBLICATION_GROUPS = [
    ("🗺️ Surveys, reviews, and field overviews", r"systematic (?:literature )?review|\bsurvey (?:of|on|about|paper)|field overview|perspective paper|position paper|survey & perspective papers|related survey|position and survey"),
    ("🧭 Foundations and value theory", r"value theory|theoretical foundation|basic value theory|axiolog|schwartz|rokeach|moral foundations theory|theory of basic"),
    ("🗂️ Datasets and benchmarks", r"dataset|benchmark|corpus|item bank|shared task|test set|leaderboard|data collection|evaluation suite|annotation datasets|survey datasets"),
    ("🔬 Reliability, validity, and auditing", r"reliability|validity|sensitivity|evaluator|evaluation bias|order bias|robustness|reproduc|audit|reporting|fair evaluator|valuebyte-llm-psychometrics:reliability and validity"),
    ("🎯 Choice, action, and behavioral consistency", r"decision|value.action|action gap|behavior|behaviour|choice|priority|priorities|social scenario|game"),
    ("🌍 Culture, language, and pluralism", r"cultur|multilingual|cross.lingual|cross.language|across languages|instruction language|language-specific|language we prompt|prompt(?:ed|ing)? (?:in|with) [a-z]+|plural|country|global opinion|multicultural alignment|non english"),
    ("🗣️ Preferences, opinions, and social simulation", r"personalized preference|attitudes.{0,3}opinions|public opinion|politic|social simulation|synthetic population|survey respondent|valuebyte-llm-psychometrics:attitudes&opinions"),
    ("⚖️ Moral reasoning and value understanding", r"moral|ethic|social norm|norm violation|justice|deontolog|virtue|value understanding|ethical reasoning|valuebyte-llm-psychometrics:morality"),
    ("🧰 Alignment, steering, and preferences", r"align|steer|preference|rlhf|reward model|constitutional|helpful.*honest|principle|overton|distributional|pluralistic-alignment:"),
    ("📐 Value representation and model internals", r"representation|extraction|embedding|latent|neuron|activation|probing|\bprobe\b|mechanism|psycho-lexical|value vector|aidas-llm-values-pluralism:value representation"),
    ("📏 Measurement and profiling", r"measurement|psychometric|questionnaire|profile|profiling|value orientation|values of (?:large )?language models|evaluating llm / value|valuebyte-llm-psychometrics:values|aidas-llm-values-pluralism:value measurement"),
]


def read_jsonl(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def display_title(row: dict) -> str:
    for value in (row.get("context_title", ""), row.get("label", "")):
        value = re.sub(r"\s+", " ", value).strip()
        if value and value.lower() not in GENERIC and not value.startswith("http"):
            value = re.sub(r"^\d+\.\s+", "", value)
            value = re.sub(r",\s*20\d{2}(?:\.\d{1,2})?,?\s*$", "", value)
            return value.strip(" ,")
    parsed = urllib.parse.urlsplit(row["url"])
    if parsed.netloc.lower() == "github.com":
        return "/".join(part for part in parsed.path.split("/") if part)[:120]
    path = parsed.path.strip("/")
    return f"{parsed.netloc.removeprefix('www.')} / {path}" if path else parsed.netloc


def markdown_text(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]").replace("|", "—")


def anchor_for(label: str) -> str:
    words = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    return f"catalog-{words}"


def publication_group(row: dict) -> str:
    tails = []
    for item in row.get("occurrences", []):
        section_path = item.get("section", "").lower()
        parts = [part.strip() for part in section_path.split(" / ") if part.strip()]
        leaf = parts[-1] if parts else ""
        source = item.get("catalog_id", "")

        # Prefer the nearest editorial category from domain-specific catalogs
        # before falling back to title keywords.
        explicit_paths = {
            "aidas-llm-values-pluralism": (
                ("value representation and extraction", "📐 Value representation and model internals"),
                ("value measurement and evaluation", "📏 Measurement and profiling"),
                ("value alignment and steering", "🧰 Alignment, steering, and preferences"),
                ("multicultural alignment", "🌍 Culture, language, and pluralism"),
            ),
            "valuebyte-llm-psychometrics": (
                ("category entries / values", "📏 Measurement and profiling"),
                ("category entries / morality", "⚖️ Moral reasoning and value understanding"),
                ("category entries / attitudes&opinions", "🗣️ Preferences, opinions, and social simulation"),
                ("category entries / reliability and validity", "🔬 Reliability, validity, and auditing"),
            ),
            "personalized-alignment": (
                ("papers / personalized preference", "🗣️ Preferences, opinions, and social simulation"),
            ),
        }
        for fragment, label in explicit_paths.get(source, ()):
            if fragment in section_path:
                return label
        if source == "pluralistic-alignment" and "pluralistic alignment methodologies" in section_path:
            return "🧰 Alignment, steering, and preferences"
        if source == "pluralistic-alignment" and "pluralistic alignment datasets and benchmarks" in section_path:
            return "🗂️ Datasets and benchmarks"
        tails.append(leaf)
    text = " ".join([display_title(row), *tails]).lower()
    for label, pattern in PUBLICATION_GROUPS:
        if re.search(pattern, text, re.I):
            return label
    return "📎 Other and adjacent value research"


def publication_metadata(row: dict) -> dict[str, str]:
    """Extract conservative display metadata without claiming full-paper audit."""
    raw = re.sub(r"\s+", " ", row.get("context_title") or display_title(row)).strip(" ,")
    raw = re.sub(r"^\d+\.\s+", "", raw)
    group_label = re.sub(r"^[^A-Za-z]+", "", publication_group(row))
    subdomain = group_label or "Other / adjacent"
    tagged = re.match(r"^[\[(]([^\])]{1,60})[\])]\s*", raw)
    if tagged:
        subdomain = tagged.group(1).strip().replace("Others & Custom", "Other / custom").replace("Others & custom", "Other / custom")
        raw = raw[tagged.end():].strip()

    # Source catalogs commonly use either ``Title, 2024.05, Venue`` or
    # ``Title, ACL 2024``.  Parse only unambiguous trailing metadata.
    title = raw
    venue = ""
    date = str(row.get("publication_year") or "")
    parts = [part.strip() for part in raw.strip(" ,").split(",")]
    date_index = next(
        (index for index, part in enumerate(parts[1:], start=1) if re.fullmatch(r"(?:19|20)\d{2}(?:\.(?:0?[1-9]|1[0-2]))?", part)),
        None,
    )
    if date_index is not None:
        title = ", ".join(parts[:date_index]).strip()
        date = parts[date_index]
        if date_index + 1 < len(parts):
            venue = ", ".join(parts[date_index + 1:]).strip(" ,")
    elif len(parts) > 1:
        tail = parts[-1]
        venue_year = re.match(r"^(.*?)(?:\s+|\b)((?:19|20)\d{2})(?:\.(0?[1-9]|1[0-2]))?(.*)$", tail)
        if venue_year and venue_year.group(1).strip():
            title = ", ".join(parts[:-1]).strip()
            venue = (venue_year.group(1) + venue_year.group(4)).strip(" ,-()")
            date = venue_year.group(2) + (f".{venue_year.group(3)}" if venue_year.group(3) else "")

    if not venue:
        url = row["url"].lower()
        anthology = re.search(r"aclanthology\.org/(?:\d{4}\.)?([a-z0-9-]+?)(?:-main|-long|-short|-\d|\.\d|/)", url)
        if anthology:
            key = anthology.group(1)
            venue = {
                "findings-acl": "Findings of ACL",
                "findings-emnlp": "Findings of EMNLP",
                "findings-naacl": "Findings of NAACL",
                "lrec": "LREC-COLING",
                "semeval": "SemEval",
                "nlpcss": "NLP+CSS",
                "ccl": "CCL",
                "q18": "TACL",
            }.get(key, key.upper())
        elif "proceedings.iclr.cc" in url:
            venue = "ICLR"
        elif "proceedings.neurips.cc" in url:
            venue = "NeurIPS"
        elif "openreview.net" in url:
            venue = "OpenReview"
        elif "arxiv.org" in url:
            venue = "arXiv"
        else:
            known_sources = (
                ("nature.com/articles/s41586", "Nature"),
                ("nature.com/articles/s41562", "Nature Human Behaviour"),
                ("nature.com/articles/s43588", "Nature Computational Science"),
                ("nature.com/articles/s42256", "Nature Machine Intelligence"),
                ("nature.com/articles/s41599", "Humanities and Social Sciences Communications"),
                ("10.1093/pnasnexus", "PNAS Nexus"),
                ("10.1371/journal.pone", "PLOS ONE"),
                ("10.2196/", "JMIR"),
                ("10.1155/2024/7115633", "Human Behavior and Emerging Technologies"),
                ("ojs.aaai.org/index.php/aaai", "AAAI"),
                ("ojs.aaai.org/index.php/aies", "AIES"),
                ("journals.sagepub.com", "SAGE journal"),
                ("dl.acm.org", "ACM Digital Library"),
                ("ieeexplore.ieee.org", "IEEE Xplore"),
                ("link.springer.com", "Springer journal or proceedings"),
                ("sciencedirect.com", "Elsevier journal or book"),
                ("tandfonline.com", "Taylor & Francis journal"),
                ("10.21203/", "Research Square"),
                ("10.1145/", "ACM proceedings or journal"),
                ("10.1609/aaai", "AAAI"),
                ("10.1177/", "SAGE journal"),
                ("10.1007/", "Springer journal or proceedings"),
            )
            venue = next((label for fragment, label in known_sources if fragment in url), "Venue not verified")

    return {
        "subdomain": subdomain,
        "title": title.strip(" ,"),
        "venue": venue,
        "date": date,
    }


def occurrence_keys(row: dict) -> set[tuple[str, int]]:
    return {(item["catalog_id"], item["line"]) for item in row.get("occurrences", [])}


def normalized_work_title(row: dict) -> str:
    title = publication_metadata(row)["title"]
    title = re.sub(r"^\s*[★⭐]+\s*", "", title)
    return re.sub(r"[^a-z0-9]+", " ", title.casefold()).strip()


def related_artifact_map(rows: list[dict]) -> tuple[dict[str, list[dict]], set[str]]:
    """Assign directly co-listed artifacts to one publication, once each."""
    publications = [row for row in rows if row["link_type_guess"] == "publication"]
    by_occurrence: dict[tuple[str, int], list[dict]] = collections.defaultdict(list)
    by_title: dict[str, list[dict]] = collections.defaultdict(list)
    for row in publications:
        for key in occurrence_keys(row):
            by_occurrence[key].append(row)
        title_key = normalized_work_title(row)
        if len(title_key) >= 16:
            by_title[title_key].append(row)

    result: dict[str, list[dict]] = collections.defaultdict(list)
    assigned: set[str] = set()
    for artifact in rows:
        if artifact["link_type_guess"] == "publication":
            continue
        candidates: dict[str, tuple[int, dict]] = {}
        artifact_occurrences = occurrence_keys(artifact)
        for key in artifact_occurrences:
            for publication in by_occurrence.get(key, []):
                overlap = len(artifact_occurrences & occurrence_keys(publication))
                candidates[publication["id"]] = (overlap, publication)
        title_key = normalized_work_title(artifact)
        if len(title_key) >= 16:
            for publication in by_title.get(title_key, []):
                overlap = len(artifact_occurrences & occurrence_keys(publication))
                candidates[publication["id"]] = (100 + overlap, publication)
        if not candidates:
            continue
        _, publication = max(candidates.values(), key=lambda item: (item[0], item[1].get("publication_year") or 0, item[1]["url"]))
        result[publication["id"]].append(artifact)
        assigned.add(artifact["id"])
    return result, assigned


def format_row(row: dict, related: list[dict] | None = None) -> str:
    links = [row, *(related or [])]
    rendered_links = " ".join(f"[{LINK_LABELS.get(item['link_type_guess'], 'link')}]({item['url']})" for item in links)
    if row["link_type_guess"] == "publication":
        metadata = publication_metadata(row)
        details = [metadata["venue"], metadata["date"]]
        details = [markdown_text(value) for value in details if value]
        middle = f" — {' — '.join(details)}" if details else ""
        return f"- ({markdown_text(metadata['subdomain'])}) **{markdown_text(metadata['title'])}**{middle} — {rendered_links}"
    return f"- **{markdown_text(display_title(row))}** — {rendered_links}"


def section(label: str, rows: list[dict], related: dict[str, list[dict]] | None = None) -> list[str]:
    rows = sorted(rows, key=lambda row: (display_title(row).casefold(), row["url"]))
    result = [f'<a id="{anchor_for(label)}"></a>', "", f"#### {label} · {len(rows)}", ""]
    result.extend(format_row(row, (related or {}).get(row["id"], [])) for row in rows)
    result.append("")
    return result


def generate(rows: list[dict]) -> str:
    publications: dict[str, list[dict]] = collections.defaultdict(list)
    artifacts: dict[str, list[dict]] = collections.defaultdict(list)
    related, assigned_artifacts = related_artifact_map(rows)
    for row in rows:
        if row["link_type_guess"] == "publication":
            publications[publication_group(row)].append(row)
        elif row["id"] not in assigned_artifacts:
            artifacts[row["link_type_guess"]].append(row)

    lines = [
        START, "",
        "> This section is generated from the deduplicated discovery index. Every",
        "> URL appears exactly once. Provenance and scope remain available in the",
        "> downloadable data and on the interactive site rather than after each link.", "",
        "**Entry format:** `(subdomain) Title — venue — date — [paper] [code] [dataset]`.",
        "When the source does not name a value model, the parenthetical label falls",
        "back to the nearest research subdomain rather than inventing one.", "",
        "**Browse the taxonomy**", "",
        "| Research area | Publications |", "|---|---:|",
    ]
    ordered_labels = [label for label, _ in PUBLICATION_GROUPS] + ["📎 Other and adjacent value research"]
    for label in ordered_labels:
        if publications[label]:
            lines.append(f"| [{label}](#{anchor_for(label)}) | {len(publications[label])} |")
    lines.extend(["", "### 📚 Publications by research topic", ""])
    for label in ordered_labels:
        if publications[label]:
            lines.extend(section(label, publications[label], related))

    artifact_labels = {
        "dataset": "💾 Dataset and benchmark artifacts",
        "model": "🧠 Model checkpoints and scorers",
        "repository": "🧰 Code repositories",
        "project": "🌐 Project pages",
        "survey_resource": "📋 Survey resources",
        "other": "🔗 Additional resources",
    }
    lines.extend(["### 🧩 Standalone data, models, code, and additional resources", ""])
    for kind in ("dataset", "model", "repository", "project", "survey_resource", "other"):
        if artifacts[kind]:
            lines.extend(section(artifact_labels[kind], artifacts[kind]))
    lines.append(END)
    return "\n".join(lines)


def update_readme(path: pathlib.Path, rows: list[dict]) -> None:
    text = path.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"{path.name} must contain {START} and {END}")
    publication_count = sum(row["link_type_guess"] == "publication" for row in rows)
    text = re.sub(r"badge/resources-\d+-136f58", f"badge/resources-{len(rows)}-136f58", text)
    text = re.sub(r"badge/publication%20links-\d+-0d3f35", f"badge/publication%20links-{publication_count}-0d3f35", text)
    text = re.sub(r"\d+ deduplicated links harvested", f"{len(rows)} deduplicated links harvested", text)
    text = re.sub(r"Complete catalog — all \d+ links", f"Complete catalog — all {len(rows)} links", text)
    generated = generate(rows)
    prefix, remainder = text.split(START, 1)
    _, suffix = remainder.split(END, 1)
    updated = prefix.rstrip() + "\n\n" + generated + suffix
    missing = [row["url"] for row in rows if row["url"] not in generated]
    if missing:
        raise SystemExit(f"Generated catalog omitted {len(missing)} URLs")
    path.write_text(updated)
    print(f"{path.name} catalog: {len(rows)} unique URLs, {publication_count} publications")


def main() -> int:
    rows = read_jsonl(LINKS)
    update_readme(README, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
