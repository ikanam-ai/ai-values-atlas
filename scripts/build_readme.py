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


def source_ids(row: dict) -> list[str]:
    return sorted({item["catalog_id"] for item in row.get("occurrences", [])})


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


def format_row(row: dict) -> str:
    title = markdown_text(display_title(row))
    sources = ", ".join(source_ids(row)) or "direct source"
    metadata = f"{row['link_type_guess']} · {row['scope_tier_guess']} · {sources}"
    return f"- **[{title}]({row['url']})** <sub>{metadata}</sub>"


def section(label: str, rows: list[dict], noun: str = "resources") -> list[str]:
    rows = sorted(rows, key=lambda row: (display_title(row).casefold(), row["url"]))
    count_noun = noun.removesuffix("s") if len(rows) == 1 else noun
    result = [f'<a id="{anchor_for(label)}"></a>', "", f"#### {label}", "", f"<sub>{len(rows)} {count_noun}</sub>", ""]
    result.extend(format_row(row) for row in rows)
    result.append("")
    return result


def generate(rows: list[dict]) -> str:
    publications: dict[str, list[dict]] = collections.defaultdict(list)
    artifacts: dict[str, list[dict]] = collections.defaultdict(list)
    for row in rows:
        if row["link_type_guess"] == "publication":
            publications[publication_group(row)].append(row)
        else:
            artifacts[row["link_type_guess"]].append(row)

    lines = [
        START,
        "",
        "> This section is generated from the deduplicated discovery index. Every",
        "> URL appears exactly once here; provenance and scope labels remain visible.",
        "",
        "**Browse the taxonomy**",
        "",
        "| Research area | Publications |",
        "|---|---:|",
    ]
    ordered_labels = [label for label, _ in PUBLICATION_GROUPS] + ["📎 Other and adjacent value research"]
    for label in ordered_labels:
        if publications[label]:
            lines.append(f"| [{label}](#{anchor_for(label)}) | {len(publications[label])} |")
    lines.extend([
        "",
        "<sub>Scope labels distinguish value-focused `core` records from broader `adjacent` work. "
        "The final label lists the source catalogs in which each record was discovered.</sub>",
        "",
        "### 📚 Publications by research topic",
        "",
    ])
    for label in ordered_labels:
        if publications[label]:
            lines.extend(section(label, publications[label], "publications"))

    artifact_labels = {
        "dataset": "💾 Dataset and benchmark artifacts",
        "model": "🧠 Model checkpoints and scorers",
        "repository": "🧰 Code repositories",
        "project": "🌐 Project pages",
        "survey_resource": "📋 Survey resources",
        "other": "🔗 Additional resources",
    }
    lines.extend(["### 🧩 Data, models, code, and additional resources", ""])
    for kind in ("dataset", "model", "repository", "project", "survey_resource", "other"):
        if artifacts[kind]:
            lines.extend(section(artifact_labels[kind], artifacts[kind]))
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    text = README.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"README must contain {START} and {END}")
    rows = read_jsonl(LINKS)
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
    README.write_text(updated)
    print(f"README catalog: {len(rows)} unique URLs, {sum(row['link_type_guess'] == 'publication' for row in rows)} publications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
