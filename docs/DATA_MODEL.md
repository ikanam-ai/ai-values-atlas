# Data model

## Design principles

The model is relational even though the source files are JSON and JSONL. Stable
IDs connect entities. Publication-level facts are not mixed with experiment-level
facts, and conceptual value systems are not conflated with instruments or models.

## Entity graph

```text
work 1 ──* study *──* axiology
             │          │
             │          └──* instrument
             ├──* dataset
             ├──* instrument
             ├──* model (with a role)
             └──* validation evidence

work ──* artifact (code, data, checkpoint, prompts, project page)
```

## Work

A citable publication or report. A work contains bibliographic information and
artifact links, but not a single flattened “methodology” field.

Important fields:

- `work_type`: empirical, benchmark, dataset, measurement_method, model,
  representation, alignment_method, survey, position, theory;
- `research_roles`: measure_ai_values, measure_human_values,
  identify_values_in_text, test_value_understanding, compare_human_ai,
  study_value_action_gap, learn_value_representation, construct_axiology,
  align_or_steer, aggregate_plural_values;
- `scope_tier`: core, adjacent, background;
- `curation.status`: discovered, catalogued, verified, audited.

## Study

An empirical design or analysis inside a work. This is the correct unit for:

- subject population and evaluated model panel;
- elicitation interface and task format;
- datasets and prompts;
- axiological models and their roles;
- scoring pipeline;
- reliability and validity evidence;
- results and limitations.

### Axiology usage

An axiology relation contains:

```json
{
  "axiology_id": "schwartz-tbv-10",
  "role": "primary",
  "model_status": "explicit_existing",
  "operationalization": "ValueLlama semantic mapping"
}
```

When no named framework exists:

```json
{
  "axiology_id": null,
  "role": "primary",
  "model_status": "implicit",
  "operationalization": "Value alignment is discussed without defined dimensions"
}
```

Null therefore never means “forgotten”; the status explains why no framework ID
is present.

## Axiology

An axiology is a representation of what values exist and, optionally, how they
relate. It can be human-theoretical, survey-derived, AI-native, induced, latent,
or open-ended.

`representation_type` values:

- `named_dimensions`: fixed labeled dimensions;
- `hierarchy`: values organized into levels;
- `circumplex`: values organized by compatibility and opposition;
- `survey_item_space`: a survey bank treated as the operative value space;
- `lexicon_or_ontology`: terms or relations without a single fixed vector;
- `principle_set`: constitutions, rights, duties, or normative principles;
- `induced_factors`: interpretable factors learned from data;
- `latent_embedding`: dense unnamed representation;
- `open_ended`: values supplied dynamically at measurement time.

An instrument such as PVQ-40 is linked to Schwartz but remains a separate entity.
ValueLlama is a measurement model, not an axiology. UniVaR is represented twice:
its latent value space is an axiology, while its released encoder is a model.

## Instrument

A reusable elicitation object or protocol: PVQ, WVS questionnaire, scenario bank,
pairwise conflict task, free-text prompt bank, or behavioral environment.

## Dataset

A released collection of items, outputs, responses, annotations, preferences, or
trajectories. Dataset metadata includes unit of observation, size, languages,
construction, annotation, access, and license.

## Model

One model record can have several study-level roles:

- `evaluated_subject`;
- `response_generator`;
- `perception_parser`;
- `value_scorer`;
- `judge`;
- `embedding_encoder`;
- `annotation_assistant`;
- `alignment_target`.

Exact version or revision belongs on the study-model relation when it varies by
experiment.

## Validation evidence

Validation is recorded as evidence objects rather than one yes/no field:

- test-retest and internal consistency;
- prompt, template, language, persona, and decoding sensitivity;
- order and position counterbalancing;
- scorer calibration and task-local human validation;
- convergent, discriminant, predictive, and ecological validity;
- cross-interface transfer;
- shuffled, permutation, or chance nulls;
- model identity or self-specificity;
- coverage, parsing failures, missingness, and zero-evidence policy.

