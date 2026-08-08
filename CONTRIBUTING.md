# Contributing

## Ways to contribute

- add a missing paper, dataset, instrument, model, or axiological framework;
- enrich a discovered link into a verified work;
- describe an empirical study within an existing work;
- correct artifact availability, licensing, or model revisions;
- report a broken link or duplicate.

## Evidence policy

Bibliographic fields should be checked against an official publisher, DOI,
OpenReview, or arXiv page. Methodological fields should be supported by the paper
itself. Repository descriptions and generated summaries are discovery aids, not
methodological evidence.

Use the following statuses:

- `discovered`: imported from a source catalog;
- `catalogued`: title and primary URL checked;
- `verified`: methodology checked against the publication;
- `audited`: artifacts and reproducibility claims checked as well.

Automated or LLM-assisted extraction must be disclosed in `curation.notes` and
cannot by itself assign `verified` or `audited`.

## Pull-request checklist

- Use a stable identifier: DOI, arXiv ID, ACL Anthology ID, or a deterministic
  fallback.
- Do not copy an abstract or summary unless its license permits redistribution.
- Add primary links before mirrors or aggregators.
- Record an explicit `scope_tier`.
- For every study, state whether an axiological model is explicit, induced,
  open-ended, implicit, or absent.
- Record artifact licenses as `unknown` instead of guessing.
- Run `python3 scripts/validate.py` before submitting.

