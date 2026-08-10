#!/usr/bin/env python3
"""Build the dependency-free AI Values Atlas wiki from curated source data."""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import sys
from collections import defaultdict


ROOT = pathlib.Path(__file__).resolve().parents[1]
LEARN_ROOT = ROOT / "site" / "learn"
AXIOLOGIES_PATH = ROOT / "data" / "curated" / "axiologies.json"
CONTENT_PATH = ROOT / "data" / "wiki_content.json"

REPRESENTATION_LABELS = {
    "named_dimensions": "Named dimensions",
    "hierarchy": "Hierarchy",
    "circumplex": "Circumplex",
    "survey_item_space": "Survey item space",
    "lexicon_or_ontology": "Ontology",
    "principle_set": "Principle set",
    "induced_factors": "Induced factors",
    "latent_embedding": "Latent embedding",
    "open_ended": "Open value set",
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_data() -> tuple[list[dict], dict]:
    axiologies = json.loads(AXIOLOGIES_PATH.read_text())["axiologies"]
    content = json.loads(CONTENT_PATH.read_text())
    notes = content["axiologies"]
    ids = {item["id"] for item in axiologies}
    missing = ids - set(notes)
    extra = set(notes) - ids
    if missing or extra:
        raise ValueError(f"Wiki axiology coverage mismatch: missing={sorted(missing)}, extra={sorted(extra)}")
    return axiologies, content


def page_records(axiologies: list[dict], content: dict) -> list[dict]:
    records = []
    for page in content["guide_pages"]:
        records.append({**page, "kind": "guide"})
    by_id = {item["id"]: item for item in axiologies}
    for axiology_id, note in content["axiologies"].items():
        item = by_id[axiology_id]
        records.append({
            "id": axiology_id,
            "path": f"axiologies/{axiology_id}",
            "group": note["group"],
            "title": item["name"],
            "short_title": note["short_title"],
            "summary": note["lead"],
            "kind": "axiology",
            "axiology": item,
            "note": note,
        })
    return records


def group_map(content: dict) -> dict[str, dict]:
    return {group["id"]: group for group in content["groups"]}


def navigation(records: list[dict], content: dict, root: str, current_id: str | None) -> str:
    groups = group_map(content)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["group"]].append(record)
    blocks = []
    for group in content["groups"]:
        items = grouped.get(group["id"], [])
        if not items:
            continue
        links = "".join(
            f'<a href="{root}{esc(item["path"])}/" class="{"active" if item["id"] == current_id else ""}">'
            f'{esc(item["short_title"])}</a>' for item in items
        )
        blocks.append(
            f'<section class="nav-group"><h2>{esc(groups[group["id"]]["title"])}</h2>{links}</section>'
        )
    home_active = "active" if current_id is None else ""
    return (
        f'<a class="wiki-home-link {home_active}" href="{root}">Wiki home</a>'
        + "".join(blocks)
    )


def topbar(root: str, atlas_root: str) -> str:
    return f"""<header class="wiki-topbar">
      <a class="wiki-brand" href="{root}"><span>A</span><b>AI Values Atlas</b><small>Wiki</small></a>
      <div class="top-actions">
        <div class="wiki-search">
          <label class="sr-only" for="wikiSearch">Search the wiki</label>
          <input id="wikiSearch" type="search" placeholder="Search concepts and models…" autocomplete="off" />
          <div id="searchResults" class="search-results" hidden></div>
        </div>
        <a href="{atlas_root}#explorer">Research index</a>
        <button id="searchButton" class="search-button" type="button" aria-expanded="false" aria-controls="wikiSearch">Search</button>
        <button id="menuButton" class="menu-button" type="button" aria-expanded="false" aria-controls="wikiSidebar">Menu</button>
      </div>
    </header>"""


def layout(*, title: str, description: str, body: str, nav: str, toc: str, root: str,
           atlas_root: str, path: str, page_id: str, page_class: str = "") -> str:
    canonical = "https://ikanam-ai.github.io/ai-values-atlas/learn/" + (f"{path}/" if path else "")
    css = f"{root}styles.css"
    css_v2 = f"{root}wiki-v2.css"
    js = f"{root}app.js"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{canonical}" />
  <title>{esc(title)} · AI Values Atlas Wiki</title>
  <link rel="stylesheet" href="{css}" />
  <link rel="stylesheet" href="{css_v2}" />
</head>
<body data-wiki-root="{root}" data-page-id="{esc(page_id)}">
  <div class="reading-progress" aria-hidden="true"><span id="readingProgress"></span></div>
  {topbar(root, atlas_root)}
  <div class="wiki-layout {page_class}">
    <aside id="wikiSidebar" class="wiki-sidebar" aria-label="Wiki navigation">{nav}</aside>
    <main class="wiki-main">{body}</main>
    <aside class="article-toc" aria-label="On this page">{toc}</aside>
  </div>
  <footer><a href="{root}">AI Values Atlas Wiki</a><span>Concepts, representations, and measurement methods</span><a href="https://github.com/ikanam-ai/ai-values-atlas">GitHub</a></footer>
  <script src="{js}"></script>
</body>
</html>
"""


def breadcrumbs(root: str, group: dict, record: dict) -> str:
    return (
        '<nav class="breadcrumbs" aria-label="Breadcrumb">'
        f'<a href="{root}">Wiki</a><span>›</span><span>{esc(group["title"])}</span>'
        f'<span>›</span><b>{esc(record["short_title"])}</b></nav>'
    )


def toc_html(items: list[tuple[str, str]]) -> str:
    links = "".join(f'<a href="#{esc(item_id)}">{esc(label)}</a>' for item_id, label in items)
    return f'<p>On this page</p>{links}<a class="toc-top" href="#top">Back to top ↑</a>'


def related_html(related_ids: list[str], records_by_id: dict[str, dict], root: str) -> str:
    cards = []
    for related_id in related_ids:
        item = records_by_id.get(related_id)
        if not item:
            continue
        cards.append(
            f'<a class="related-row" href="{root}{esc(item["path"])}/">'
            f'<span>{esc(item["short_title"])}</span><small>{esc(item["summary"])}</small><i>→</i></a>'
        )
    return '<section class="related" id="related"><h2>Related pages</h2>' + "".join(cards) + "</section>"


def prev_next(record: dict, records: list[dict], root: str) -> str:
    index = next(i for i, item in enumerate(records) if item["id"] == record["id"])
    previous = records[index - 1] if index else None
    following = records[index + 1] if index + 1 < len(records) else None
    def link(item: dict | None, label: str) -> str:
        if not item:
            return "<span></span>"
        return f'<a href="{root}{esc(item["path"])}/"><small>{label}</small><b>{esc(item["short_title"])}</b></a>'
    return f'<nav class="prev-next" aria-label="Adjacent wiki pages">{link(previous, "Previous")}{link(following, "Next")}</nav>'


def widget_html(widget: str, record: dict | None = None) -> str:
    dimensions = []
    if record and record.get("axiology"):
        dimensions = record["axiology"].get("dimensions", [])
    data_dimensions = esc(json.dumps(dimensions, ensure_ascii=False))
    page_id = esc(record["id"] if record else "")
    return (
        f'<figure class="visual-module" data-widget="{esc(widget)}" '
        f'data-page="{page_id}" data-dimensions="{data_dimensions}">'
        '<div class="widget-canvas"></div>'
        '<figcaption class="widget-note">Structural diagram—not an estimated person, culture, or model profile.</figcaption>'
        '</figure>'
    )


def guide_page(record: dict, records: list[dict], content: dict) -> str:
    root = "../../"
    atlas_root = "../../../"
    groups = group_map(content)
    group = groups[record["group"]]
    records_by_id = {item["id"]: item for item in records}
    section_items = [(section["id"], section["title"]) for section in record["sections"]]
    section_items += [("related", "Related pages")]
    sections = []
    for section in record["sections"]:
        paragraphs = "".join(f"<p>{esc(text)}</p>" for text in section.get("paragraphs", []))
        bullets = section.get("bullets", [])
        bullet_html = "<ul>" + "".join(f"<li>{esc(text)}</li>" for text in bullets) + "</ul>" if bullets else ""
        sections.append(f'<section class="article-section" id="{esc(section["id"])}"><h2>{esc(section["title"])}</h2>{paragraphs}{bullet_html}</section>')
    body = f"""
      <article id="top" class="wiki-article">
        {breadcrumbs(root, group, record)}
        <header class="article-header"><p class="article-kind">{esc(group["title"])}</p><h1>{esc(record["title"])}</h1><p>{esc(record["summary"])}</p></header>
        {widget_html(record["widget"], record)}
        {''.join(sections)}
        {related_html(record.get("related", []), records_by_id, root)}
        {prev_next(record, records, root)}
      </article>"""
    return layout(
        title=record["title"], description=record["summary"], body=body,
        nav=navigation(records, content, root, record["id"]), toc=toc_html(section_items),
        root=root, atlas_root=atlas_root, path=record["path"], page_id=record["id"],
    )


def dimensions_html(dimensions: list[str]) -> str:
    if not dimensions:
        return '<p class="empty-dimensions">No fixed named dimensions. The representation is open, changing, relational, or latent.</p>'
    return '<div class="dimension-list">' + "".join(
        f'<span><b>{index:02d}</b>{esc(name)}</span>' for index, name in enumerate(dimensions, start=1)
    ) + "</div>"


def scope_html(scope: dict) -> str:
    labels = [("Unit", "unit"), ("Construct", "construct"), ("Output", "output"), ("Evidence base", "evidence")]
    return '<dl class="scope-grid">' + "".join(
        f'<div><dt>{esc(label)}</dt><dd>{esc(scope.get(key, "—"))}</dd></div>'
        for label, key in labels
    ) + "</dl>"


def numbers_html(rows: list[dict]) -> str:
    return '<div class="number-ribbon">' + "".join(
        f'<div><b>{esc(row["value"])}</b><span>{esc(row["label"])}</span></div>'
        for row in rows
    ) + "</div>"


def evidence_html(rows: list[dict]) -> str:
    return '<div class="evidence-list">' + "".join(
        f'<article class="evidence-row"><p>{esc(row["meta"])}</p>'
        f'<h3><a href="{esc(row["url"])}">{esc(row["title"])}</a></h3>'
        f'<span>{esc(row["detail"])}</span></article>'
        for row in rows
    ) + "</div>"


def axiology_page(record: dict, records: list[dict], content: dict) -> str:
    root = "../../"
    atlas_root = "../../../"
    group = group_map(content)[record["group"]]
    item = record["axiology"]
    note = record["note"]
    records_by_id = {candidate["id"]: candidate for candidate in records}
    count = item.get("dimension_count")
    count_text = str(count) if count is not None else "Open / variable"
    aliases = " · ".join(item.get("aliases", [])) or "—"
    representation = REPRESENTATION_LABELS.get(item["representation_type"], item["representation_type"])
    source_links = "".join(
        f'<li><a href="{esc(url)}">Primary source {index} ↗</a></li>'
        for index, url in enumerate(item["primary_sources"], start=1)
    )
    uses = "".join(f"<li>{esc(text)}</li>" for text in note["uses"])
    cautions = "".join(f"<li>{esc(text)}</li>" for text in note["cautions"])
    toc = [
        ("at-a-glance", "At a glance"), ("structure", "Structure"),
        ("measurement", "Measurement"), ("ai-evidence", "Evidence in AI"),
        ("ai-use", "Best uses"), ("limits", "What not to infer"),
        ("sources", "Primary sources"), ("related", "Related pages"),
    ]
    body = f"""
      <article id="top" class="wiki-article">
        {breadcrumbs(root, group, record)}
        <header class="article-header axiology-header">
          <p class="article-kind">{esc(note["classification"])}</p>
          <h1>{esc(record["short_title"])}</h1>
          <p>{esc(note["lead"])}</p>
        </header>
        <aside class="verdict"><b>Atlas verdict</b><p>{esc(note["verdict"])}</p></aside>
        <dl class="fact-strip">
          <div><dt>Full name</dt><dd>{esc(item["name"])}</dd></div>
          <div><dt>Discipline</dt><dd>{esc(note["discipline"])}</dd></div>
          <div><dt>Representation</dt><dd>{esc(representation)}</dd></div>
          <div><dt>Coordinates</dt><dd>{esc(count_text)}</dd></div>
          <div><dt>Aliases</dt><dd>{esc(aliases)}</dd></div>
        </dl>
        <section class="article-section glance-section" id="at-a-glance"><h2>At a glance</h2>{scope_html(note["scope"])}{numbers_html(note.get("numbers", []))}</section>
        {widget_html(note["widget"], record)}
        <section class="article-section" id="structure"><h2>Structure</h2><p>{esc(item["structure_notes"])}</p>{dimensions_html(item.get("dimensions", []))}</section>
        <section class="article-section" id="measurement"><h2>How it is measured</h2><p>{esc(note["measurement"])}</p></section>
        <section class="article-section" id="ai-evidence"><h2>Evidence in AI research</h2>{evidence_html(note.get("ai_evidence", []))}</section>
        <section class="article-section" id="ai-use"><h2>Best uses</h2><ul>{uses}</ul></section>
        <section class="article-section caution-section" id="limits"><h2>What not to infer</h2><ul>{cautions}</ul></section>
        <section class="article-section sources" id="sources"><h2>Primary sources</h2><ol>{source_links}</ol><p>See the <a href="{atlas_root}#explorer">research index</a> for studies, datasets, code, and related artifacts.</p></section>
        {related_html(note.get("related", []), records_by_id, root)}
        {prev_next(record, records, root)}
      </article>"""
    return layout(
        title=record["short_title"], description=note["lead"], body=body,
        nav=navigation(records, content, root, record["id"]), toc=toc_html(toc),
        root=root, atlas_root=atlas_root, path=record["path"], page_id=record["id"],
    )


def home_page(records: list[dict], content: dict) -> str:
    groups = group_map(content)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["group"]].append(record)
    directories = []
    for group in content["groups"]:
        items = grouped.get(group["id"], [])
        if not items:
            continue
        rows = "".join(
            f'<a class="directory-row" href="{esc(item["path"])}/"><b>{esc(item["short_title"])}</b>'
            f'<span>{esc(item["summary"])}</span><i>→</i></a>' for item in items
        )
        directories.append(
            f'<section class="directory-group" id="group-{esc(group["id"])}"><header><p>{len(items):02d}</p>'
            f'<div><h2>{esc(group["title"])}</h2><span>{esc(group["description"])}</span></div></header>{rows}</section>'
        )
    toc = '<p>Wiki contents</p><a href="#landscape">Framework landscape</a>' + "".join(
        f'<a href="#group-{esc(group["id"])}">{esc(group["title"])}</a>'
        for group in content["groups"] if grouped.get(group["id"])
    )
    axiology_count = sum(record["kind"] == "axiology" for record in records)
    guide_count = sum(record["kind"] == "guide" for record in records)
    body = f"""
      <section id="top" class="wiki-home">
        <header class="wiki-hero">
          <p class="article-kind">RESEARCH WIKI · {axiology_count} REPRESENTATIONS · {guide_count} GUIDES</p>
          <h1>Values in AI,<br /><em>without category errors.</em></h1>
          <p>A compact textbook for choosing value frameworks, reading their geometry, tracing their instruments, and judging what evidence about an AI system actually supports.</p>
          <div class="hero-actions"><a class="button primary" href="concepts/what-is-an-axiology/">Start with the foundations</a><a class="button secondary" href="axiologies/schwartz-tbv-10/">Why Schwartz is the default</a></div>
        </header>
        <div class="wiki-principle"><b>The organizing rule</b><p>A theory is not an instrument. An instrument is not an interface. An interface is not a scorer. A score is not automatically a stable model identity.</p></div>
        <section class="quick-compare" aria-label="Wiki coverage"><div><b>{axiology_count}</b><span>mapped representations</span></div><div><b>7</b><span>representation shapes</span></div><div><b>{guide_count}</b><span>measurement guides</span></div><div><b>701</b><span>works in the linked index</span></div></section>
        <section class="home-landscape" id="landscape">
          <header><p class="article-kind">THE LANDSCAPE</p><h2>Choose by question, not familiarity.</h2><p>Only three families below aim at a broad named profile. The others change the construct, the unit of analysis, or the kind of output.</p></header>
          <div class="landscape-table">
            <div class="landscape-head"><span>Research question</span><span>Best starting point</span><span>Do not claim</span></div>
            <div><b>Broad individual priorities</b><span>Schwartz · Functional Theory · Rokeach</span><small>that endorsement is behavior</small></div>
            <div><b>Moral concerns</b><span>MFT</span><small>a complete value profile</small></div>
            <div><b>Self–other allocation</b><span>SVO</span><small>general morality or personality</small></div>
            <div><b>Population and culture</b><span>WVS · Inglehart–Welzel · Hofstede · GLOBE</span><small>country scores are individual traits</small></div>
            <div><b>Named LLM-native factors</b><span>GPLA-5</span><small>universal human categories</small></div>
            <div><b>Model/language similarity</b><span>UniVaR</span><small>latent axes have fixed meanings</small></div>
            <div><b>Contextual conflict</b><span>Value Kaleidoscope · GPV</span><small>a global profile from relevance</small></div>
            <div><b>Desired assistant behavior</b><span>HHH · Constitutional AI</span><small>a policy reveals intrinsic values</small></div>
          </div>
        </section>
        <aside class="schwartz-default"><p class="article-kind">BOTTOM LINE</p><h2>Schwartz is the default—not the winner of every task.</h2><p>It currently offers the strongest package for a broad, interpretable, individual-level profile: explicit motivational geometry, 4/10/19 granularities, reusable instruments, cross-cultural validation, and substantial AI adoption. MFT is better for moral concerns; WVS-family spaces for culture; GPLA for an LLM-native named alternative; UniVaR for identity and similarity; Value Kaleidoscope and GPV for contextual text.</p></aside>
        <div class="directory">{''.join(directories)}</div>
      </section>"""
    return layout(
        title="Wiki", description="A visual reference to axiologies, value spaces, and AI value measurement.",
        body=body, nav=navigation(records, content, "", None), toc=toc,
        root="", atlas_root="../", path="", page_id="wiki-home", page_class="home-layout",
    )


def outputs() -> dict[pathlib.Path, str]:
    axiologies, content = load_data()
    records = page_records(axiologies, content)
    generated: dict[pathlib.Path, str] = {
        LEARN_ROOT / "index.html": home_page(records, content),
    }
    for record in records:
        destination = LEARN_ROOT / record["path"] / "index.html"
        generated[destination] = (
            axiology_page(record, records, content)
            if record["kind"] == "axiology" else guide_page(record, records, content)
        )
    search_rows = [
        {
            "id": record["id"], "title": record["short_title"], "path": record["path"],
            "summary": record["summary"], "group": group_map(content)[record["group"]]["title"],
        }
        for record in records
    ]
    generated[LEARN_ROOT / "search.json"] = json.dumps(search_rows, ensure_ascii=False, indent=2) + "\n"
    manifest = {
        "schema_version": "1.0.0", "updated": content["updated"],
        "pages": [str(path.relative_to(LEARN_ROOT)) for path in generated if path.suffix == ".html"],
    }
    generated[LEARN_ROOT / "wiki-manifest.json"] = json.dumps(manifest, indent=2) + "\n"
    return generated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when committed wiki output is stale")
    args = parser.parse_args()
    generated = outputs()
    stale = []
    for path, expected in generated.items():
        if args.check:
            if not path.exists() or path.read_text() != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected)
    if stale:
        print("WIKI BUILD STALE")
        for path in stale:
            print(f"- {path}")
        return 1
    if args.check:
        print(f"WIKI BUILD CURRENT: {sum(path.suffix == '.html' for path in generated)} pages")
    else:
        print(f"WROTE WIKI: {sum(path.suffix == '.html' for path in generated)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
