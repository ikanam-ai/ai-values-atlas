# Taxonomy decisions

The atlas uses entities that can be checked independently. This prevents a
paper title, a psychological theory, a questionnaire, and a neural scorer from
becoming interchangeable tags.

| Entity | Question it answers | Examples | Not stored as |
|---|---|---|---|
| Work | What can be cited? | paper, report, survey | one flattened experiment |
| Study | What was actually done? | one benchmark run or validation experiment | publication metadata |
| Axiology | What counts as a value, and how is the value universe structured? | Schwartz-10, MFT, GPLA-5, UniVaR space, open-ended GPV | questionnaire or scorer |
| Instrument | How is evidence elicited? | PVQ-40, WVS questionnaire, Value Portrait | axiology |
| Dataset | What observations/items are released? | survey responses, scenarios, generated outputs | task definition alone |
| Model | What computational system acts in the pipeline? | subject LLM, ValueLlama scorer, UniVaR encoder | value framework |
| Artifact | Where is an implementation or release? | GitHub, HF checkpoint, prompts | scientific claim |
| Validation evidence | Which claim was tested, under which condition? | order counterbalance, human calibration, cross-interface transfer | one global quality score |

## Why axiology is the right entity name

“Framework” is too broad: it can refer to a benchmark, an evaluation pipeline,
or a theory. “Value taxonomy” excludes latent and open-ended representations.
The atlas therefore uses **axiology** as the umbrella for an explicit model of
the value universe. Each axiology records a `representation_type`, allowing
named dimensions, hierarchies, circumplexes, item spaces, ontologies, principle
sets, induced factors, latent embeddings, and open-ended spaces to coexist.

This does not claim that every representation is a philosophical theory. It is
a database category for the value ontology or coordinate system licensed by a
study.

## Papers with no explicit value model

Absence is represented deliberately, never as an unexplained blank:

- `implicit`: the study invokes values but does not define their dimensions;
- `none`: the study explicitly avoids or does not contain an axiological model;
- `axiology_id: null`: no named entity can be linked;
- `operationalization`: records what the study does instead.

## Multi-framework papers

A study may link to several axiologies. The relation carries one of five roles:

- `primary` — the main representation;
- `baseline` — a comparison representation;
- `mapping_target` — the labels or coordinates produced by a scorer;
- `alignment_target` — values used to steer a system;
- `discovered_output` — a representation induced by the study.

The relation is study-level because two experiments in the same paper can use
different value spaces, interfaces, scorers, and validation evidence.
