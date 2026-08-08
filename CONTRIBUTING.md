# Contributing

AI Values Atlas welcomes additions and corrections that make the field map more
useful to researchers.

## What to contribute

- a missing paper, book, dataset, benchmark, instrument, model, or living catalog;
- a better research-domain assignment or contribution type;
- an official paper, code, dataset, model, prompt, output, or project link;
- a correction to a year, venue, license, released artifact, or scientific limitation;
- a concrete challenge to a domain assignment, supported by the paper or another primary source;
- a broken-link, duplicate-work, or version-identity correction.

## Entry requirements

For a research work, provide:

- a stable identifier or primary URL;
- title, publication year, and venue where applicable;
- one or more research domains and contribution types;
- a short description of the work's actual contribution;
- separate links for every available artifact;
- a source for any numerical dataset, benchmark, or model claim.

Artifact availability is shown separately from scientific contribution. A paper
without code is not automatically weak, and a polished repository does not by
itself establish scientific importance.

## Pull-request checklist

- Prefer publisher, DOI, ACL Anthology, OpenReview, arXiv, official GitHub, or
  official Hugging Face links.
- Do not copy abstracts or other text unless redistribution is permitted.
- Do not infer a license when none is stated.
- Keep theories, instruments, scorers, model outputs, and observed behavior as
  separate entities.
- Explain proposed domain or taxonomy changes with concrete scientific evidence.
- Run `python3 scripts/validate_public.py` and `node --check site/app.js`.
