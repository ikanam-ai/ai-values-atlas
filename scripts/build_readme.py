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
README_RU = ROOT / "README_RU.md"
LINKS = ROOT / "data" / "raw" / "catalog_links.jsonl"
START = "<!-- complete-catalog:start -->"
END = "<!-- complete-catalog:end -->"

GENERIC = {"paper", "pdf", "code", "github", "dataset", "data", "model", "project", "website", "link", "repository"}

RU_LABELS = {
    "🗺️ Surveys, reviews, and field overviews": "🗺️ Обзоры и карты исследовательского поля",
    "🧭 Foundations and value theory": "🧭 Основания и теории ценностей",
    "🗂️ Datasets and benchmarks": "🗂️ Датасеты и бенчмарки",
    "🔬 Reliability, validity, and auditing": "🔬 Надёжность, валидность и аудит",
    "🎯 Choice, action, and behavioral consistency": "🎯 Выбор, действие и поведенческая согласованность",
    "🌍 Culture, language, and pluralism": "🌍 Культура, язык и плюрализм",
    "🗣️ Preferences, opinions, and social simulation": "🗣️ Предпочтения, мнения и социальные симуляции",
    "⚖️ Moral reasoning and value understanding": "⚖️ Моральное рассуждение и понимание ценностей",
    "🧰 Alignment, steering, and preferences": "🧰 Алайнмент, управление и предпочтения",
    "📐 Value representation and model internals": "📐 Представления ценностей и внутренние механизмы моделей",
    "📏 Measurement and profiling": "📏 Измерение и профилирование",
    "📎 Other and adjacent value research": "📎 Другие и смежные исследования ценностей",
    "💾 Dataset and benchmark artifacts": "💾 Датасеты и артефакты бенчмарков",
    "🧠 Model checkpoints and scorers": "🧠 Чекпойнты моделей и скореры",
    "🧰 Code repositories": "🧰 Репозитории с кодом",
    "🌐 Project pages": "🌐 Страницы проектов",
    "📋 Survey resources": "📋 Опросные ресурсы",
    "🔗 Additional resources": "🔗 Дополнительные ресурсы",
}

LINK_LABELS = {
    "publication": ("paper", "статья"),
    "dataset": ("data", "данные"),
    "model": ("model", "модель"),
    "repository": ("code", "код"),
    "project": ("project", "проект"),
    "survey_resource": ("survey", "опрос"),
    "other": ("link", "ссылка"),
}

SOURCE_NAMES = {
    "aidas-llm-values-pluralism": "AIDAS Values & Pluralism",
    "alignment-goal-survey": "Alignment Goal Survey",
    "awesome-cultural-nlp": "Awesome Cultural NLP",
    "awesome-llm-datasets": "Awesome LLM Datasets",
    "awesome-llm-safety": "Awesome LLM Safety",
    "personalized-alignment": "Personalized Alignment",
    "pluralistic-alignment": "Pluralistic Alignment",
    "stonic-manuscript-bibliography": "STONIC bibliography",
    "valuebyte-llm-psychometrics": "LLM Psychometrics",
    "valuebyte-llm-social-science": "LLM Social Science",
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


def localized_label(label: str, language: str) -> str:
    return RU_LABELS.get(label, label) if language == "ru" else label


def format_row(row: dict, language: str) -> str:
    title = markdown_text(display_title(row))
    sources = ", ".join(SOURCE_NAMES.get(source, source) for source in source_ids(row))
    sources = sources or ("прямой источник" if language == "ru" else "direct source")
    link_label = LINK_LABELS.get(row["link_type_guess"], LINK_LABELS["other"])[language == "ru"]
    scope = {"core": "ядро", "adjacent": "смежная тема"}.get(row["scope_tier_guess"], row["scope_tier_guess"]) if language == "ru" else row["scope_tier_guess"]
    via = "источник" if language == "ru" else "via"
    year = f", {row['publication_year']}" if row.get("publication_year") else ""
    return f"- **{title}**{year} — [[{link_label}]({row['url']})] · {scope} · {via}: {sources}"


def section(label: str, rows: list[dict], language: str) -> list[str]:
    rows = sorted(rows, key=lambda row: (display_title(row).casefold(), row["url"]))
    result = [f'<a id="{anchor_for(label)}"></a>', "", f"#### {localized_label(label, language)} · {len(rows)}", ""]
    result.extend(format_row(row, language) for row in rows)
    result.append("")
    return result


def generate(rows: list[dict], language: str) -> str:
    publications: dict[str, list[dict]] = collections.defaultdict(list)
    artifacts: dict[str, list[dict]] = collections.defaultdict(list)
    for row in rows:
        if row["link_type_guess"] == "publication":
            publications[publication_group(row)].append(row)
        else:
            artifacts[row["link_type_guess"]].append(row)

    if language == "ru":
        lines = [
            START, "",
            "> Раздел генерируется из дедуплицированного индекса. Каждый URL приведён",
            "> ровно один раз; для записи сохранены тематический охват и происхождение.", "",
            "**Навигация по таксономии**", "",
            "| Направление | Публикации |", "|---|---:|",
        ]
    else:
        lines = [
            START, "",
            "> This section is generated from the deduplicated discovery index. Every",
            "> URL appears exactly once here; provenance and scope labels remain visible.", "",
            "**Browse the taxonomy**", "",
            "| Research area | Publications |", "|---|---:|",
        ]
    ordered_labels = [label for label, _ in PUBLICATION_GROUPS] + ["📎 Other and adjacent value research"]
    for label in ordered_labels:
        if publications[label]:
            lines.append(f"| [{localized_label(label, language)}](#{anchor_for(label)}) | {len(publications[label])} |")
    if language == "ru":
        lines.extend(["", "> **Легенда:** `ядро` — работа непосредственно о ценностях; `смежная тема` — более широкий контекст. После ссылки указаны каталоги-источники.", "", "### 📚 Публикации по направлениям", ""])
    else:
        lines.extend(["", "> **Legend:** `core` records focus directly on values; `adjacent` records provide broader context. Source catalogs follow each link.", "", "### 📚 Publications by research topic", ""])
    for label in ordered_labels:
        if publications[label]:
            lines.extend(section(label, publications[label], language))

    artifact_labels = {
        "dataset": "💾 Dataset and benchmark artifacts",
        "model": "🧠 Model checkpoints and scorers",
        "repository": "🧰 Code repositories",
        "project": "🌐 Project pages",
        "survey_resource": "📋 Survey resources",
        "other": "🔗 Additional resources",
    }
    heading = "### 🧩 Данные, модели, код и дополнительные ресурсы" if language == "ru" else "### 🧩 Data, models, code, and additional resources"
    lines.extend([heading, ""])
    for kind in ("dataset", "model", "repository", "project", "survey_resource", "other"):
        if artifacts[kind]:
            lines.extend(section(artifact_labels[kind], artifacts[kind], language))
    lines.append(END)
    return "\n".join(lines)


def add_curated_years(text: str, rows: list[dict]) -> str:
    years = {}
    for row in rows:
        if not row.get("publication_year"):
            continue
        url = row["url"]
        variants = {
            url,
            re.sub(r"^http://", "https://", url),
            url.replace("https://doi.org/", "https://dx.doi.org/"),
            url.replace("https://arxiv.org/abs/", "https://browse.arxiv.org/pdf/") + (".pdf" if "arxiv.org/abs/" in url else ""),
        }
        for variant in variants:
            years[variant] = row["publication_year"]
    pattern = re.compile(r"(- \*\*[^\n]+?\*\*)(?:, (\d{4}))? (\[\[(?:paper|статья)\]\((https?://[^)]+)\)\])")

    def replace(match: re.Match) -> str:
        year = years.get(match.group(4)) or match.group(2)
        if not year:
            url_years = [int(value) for value in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", match.group(4))]
            url_years = [value for value in url_years if 1950 <= value <= 2026]
            year = max(url_years) if url_years else None
        suffix = f", {year}" if year else ""
        return f"{match.group(1)}{suffix} {match.group(3)}"

    return pattern.sub(replace, text)


def update_readme(path: pathlib.Path, rows: list[dict], language: str) -> None:
    text = path.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"{path.name} must contain {START} and {END}")
    text = add_curated_years(text, rows)
    publication_count = sum(row["link_type_guess"] == "publication" for row in rows)
    text = re.sub(r"badge/resources-\d+-136f58", f"badge/resources-{len(rows)}-136f58", text)
    text = re.sub(r"badge/publication%20links-\d+-0d3f35", f"badge/publication%20links-{publication_count}-0d3f35", text)
    text = re.sub(r"\d+ deduplicated links harvested", f"{len(rows)} deduplicated links harvested", text)
    text = re.sub(r"Complete catalog — all \d+ links", f"Complete catalog — all {len(rows)} links", text)
    generated = generate(rows, language)
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
    update_readme(README, rows, "en")
    update_readme(README_RU, rows, "ru")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
