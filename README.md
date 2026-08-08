# LLM Values Atlas

An open, structured evidence map of research on values in artificial intelligence.

The atlas connects papers, studies, datasets, instruments, axiological frameworks,
measurement models, evaluated systems, and validation evidence. It covers named
value theories such as Schwartz, Moral Foundations Theory, Hofstede, and GPLA,
but it also records studies that induce latent value spaces, use open-ended value
definitions, or invoke "values" without an explicit axiological model.

## Why this is not just another awesome list

Existing reading lists are useful for discovery, but they usually flatten a paper
into one citation. Value research needs more structure:

- one paper may contain several experiments;
- one experiment may compare several value frameworks;
- a framework is not the same thing as an instrument or scorer;
- a model can be the subject, generator, parser, scorer, judge, or encoder;
- reliability, human validation, order controls, and cross-interface evidence are
  distinct forms of support;
- some studies have no explicit value model, which is itself important metadata.

The atlas therefore separates `work` (a publication) from `study` (an empirical
design inside the publication) and links both to reusable entities.

## Coverage

Core scope:

- measuring values expressed or enacted by AI systems;
- value understanding, prioritization, consistency, and value-action gaps;
- value identification and representation in text or model internals;
- moral, cultural, political, civic, spiritual, organizational, and pluralistic
  value frameworks used with AI;
- value alignment and steering when the target values are made explicit;
- datasets, benchmarks, instruments, scorers, encoders, and checkpoints used by
  these studies.

Adjacent work is retained with a scope label when it concerns preferences,
norms, opinions, culture, morality, or personalization but does not directly
measure a value construct.

## Data layers

| Layer | Location | Meaning |
|---|---|---|
| Discovered links | `data/raw/catalog_links.jsonl` | Harvested from public research catalogs; not yet treated as verified papers |
| Curated works | `data/curated/works.jsonl` | Bibliographic records checked against a primary publication page |
| Studies | `data/curated/studies.jsonl` | Experiment-level measurement and validation metadata |
| Axiologies | `data/curated/axiologies.json` | Named, proposed, induced, latent, or open-ended value representations |
| Instruments | `data/curated/instruments.json` | Questionnaires, item banks, scenarios, and elicitation protocols |
| Models | `data/curated/models.jsonl` | Scorers, encoders, judges, parsers, generators, and evaluated systems |
| Datasets | `data/curated/datasets.jsonl` | Item banks, response corpora, annotations, and benchmark releases |
| Provenance | Embedded in every record | Source catalogs, primary URLs, curator status, and last verification date |

## Axiology is a first-class entity

`Schwartz-10` is not stored as a loose tag. It is an axiological framework with
its own structure, dimensionality, instruments, and relations to other variants.
The same applies to MFT, WVS/Inglehart-Welzel, Hofstede, GLOBE, Rokeach,
GPLA-5, UniVaR, and newly induced systems.

Each study declares how it uses an axiology:

- `primary`: the principal value representation;
- `baseline`: a comparison system;
- `mapping_target`: labels or coordinates used by a scorer;
- `alignment_target`: values the system is steered toward;
- `discovered_output`: a value system induced by the study.

It also declares a `model_status`:

- `explicit_existing`: an established named framework is used;
- `explicit_proposed`: the paper proposes a named framework;
- `induced_interpretable`: factors or categories are learned from data;
- `induced_latent`: a dense value representation is learned;
- `open_ended`: arbitrary values can be supplied at measurement time;
- `implicit`: values are discussed but not operationalized as a model;
- `none`: the study explicitly has no axiological model.

This avoids silently treating every use of the word “value” as Schwartz-style
psychometrics.

## Repository layout

```text
data/
  catalog_sources.json
  raw/catalog_links.jsonl
  curated/
schema/
scripts/
docs/
site/
```

Detailed definitions are in [DATA_MODEL.md](docs/DATA_MODEL.md), inclusion rules
in [SCOPE.md](docs/SCOPE.md), review rules in [CURATION.md](docs/CURATION.md),
and the entity-design rationale in [TAXONOMY_DECISIONS.md](docs/TAXONOMY_DECISIONS.md).

## Rebuild the discovered-link catalog

The harvester only copies public URLs, link labels, section paths, and source
provenance. It does not copy third-party summaries or taxonomic prose.

```bash
python3 scripts/sync_sources.py
python3 scripts/import_bibtex.py /path/to/references.bib
python3 scripts/harvest_catalogs.py
python3 scripts/validate.py
python3 scripts/build_catalog.py
```

Source repositories are cloned into `.cache/catalog-sources/`, which is ignored
by Git. Every harvested link retains the catalog and section where it was found.

## Contributing

Pull requests and issues are welcome. A new citation can enter as `catalogued`,
but claims about methodology or validation require a primary-source citation.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing

- original code: MIT;
- original structured metadata and documentation: CC BY 4.0;
- linked papers, datasets, models, and third-party repositories retain their own
  licenses and copyright;
- source catalogs are attribution/provenance sources, not copied content.
