<div align="center">

<h1>AI Values Atlas</h1>

<p><strong>A field guide to how values are represented, elicited, expressed, chosen, and evaluated in AI systems.</strong></p>

<p>
  <a href="https://ikanam-ai.github.io/ai-values-atlas/">Explore the atlas</a> ·
  <a href="#field-map">Field map</a> ·
  <a href="#literature-by-research-question">Literature</a> ·
  <a href="#axiological-spaces">Axiologies</a> ·
  <a href="#datasets-benchmarks-and-instruments">Datasets & benchmarks</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p>
  <a href="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml"><img alt="validation" src="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml/badge.svg"></a>
  <a href="https://ikanam-ai.github.io/ai-values-atlas/"><img alt="resources" src="https://img.shields.io/badge/discovery%20index-997%20resources-136f58"></a>
  <a href="LICENSE"><img alt="metadata license" src="https://img.shields.io/badge/metadata-CC%20BY%204.0-7665d8"></a>
  <a href="LICENSE"><img alt="code license" src="https://img.shields.io/badge/code-MIT-f2b84b"></a>
</p>

</div>

AI Values Atlas is an open map of research on values in language models and
other AI systems. It connects theories, papers, benchmarks, datasets,
questionnaires, scenarios, scorers, representation models, and validation
evidence without pretending that they measure the same thing.

> **The central rule:** a value framework is not an instrument; an instrument
> is not a scorer; endorsement is not choice; generated text is not behavior;
> and a reliable profile is not automatically a valid or model-specific one.

The lists below are a human-oriented guide to the field. The
[full discovery index](https://ikanam-ai.github.io/ai-values-atlas/) contains
997 deduplicated links harvested from ten public research catalogs and the
current STONIC bibliography. Discovery records retain provenance but are not
automatically treated as method-verified publications.

## Contents

- [Field map](#field-map)
- [What counts as an axiology?](#what-counts-as-an-axiology)
- [Axiological spaces](#axiological-spaces)
- [Literature by research question](#literature-by-research-question)
  - [Surveys and field overviews](#surveys-and-field-overviews)
  - [Questionnaires and elicited profiles](#questionnaires-and-elicited-profiles)
  - [Value understanding and benchmark tasks](#value-understanding-and-benchmark-tasks)
  - [Values in generated text](#values-in-generated-text)
  - [Choice, action, and cross-interface gaps](#choice-action-and-cross-interface-gaps)
  - [Culture, language, and pluralism](#culture-language-and-pluralism)
  - [Representations, internals, and steering](#representations-internals-and-steering)
  - [Reliability, validity, and reporting](#reliability-validity-and-reporting)
- [Datasets, benchmarks, and instruments](#datasets-benchmarks-and-instruments)
- [Models, scorers, and representation tools](#models-scorers-and-representation-tools)
- [Data and contribution model](#data-and-contribution-model)

## Field map

The field is easier to understand by separating the **object being measured**
from the **measurement interface** and the **claim reported afterward**.

| Evidence layer | Research question | Typical interface | What it can support |
|---|---|---|---|
| Value understanding | Can the system identify or reason about a value? | classification, argument labels, moral scenarios | recognition or reasoning performance |
| Stated profile | What does the model endorse under a fixed protocol? | PVQ/SVS/WVS-style questionnaire, Likert ratings | protocol-conditioned endorsement profile |
| Conflict choice | Which value wins when motivations conflict? | forced choice, ranking, paired alternatives | choice priority under the task contract |
| Generated framing | Which values are expressed in open text? | free generation followed by mapping or scoring | textual-framing profile |
| Observed action | What value-relevant behavior occurs in an environment? | sequential decisions, games, tool use | task-bounded behavioral evidence |
| Internal representation | Where and how is value information encoded? | probes, activation interventions, embeddings | representational or causal mechanism evidence |
| Alignment target | Which values should a system follow? | constitutions, preferences, principles, plural inputs | normative target or steering objective |
| Measurement validity | Does the result survive plausible alternatives? | prompt, language, order, scorer, template, null and human checks | reliability, transfer, validity, or identity evidence |

### Six coordinates for reading any paper

| Coordinate | Ask this before comparing results |
|---|---|
| **Subject** | Is the subject an LLM, agent, model–language pair, generated corpus, or human comparison group? |
| **Axiology** | Does the work use Schwartz, MFT, WVS, an induced factor model, a latent space, open-ended values, or no explicit value model? |
| **Instrument** | Is evidence elicited through a questionnaire, scenario bank, free text, choice task, environment, or internal probe? |
| **Scorer** | Are outputs mapped by rules, embeddings, classifiers, LLM judges, human annotations, or a trained value model? |
| **Protocol** | Which prompt, system template, language, order, role, context, and decoding settings define the measurement? |
| **Validation** | Are reliability, counterbalancing, human calibration, scorer agreement, nulls, cross-interface transfer, and missingness reported? |

## What counts as an axiology?

This atlas uses **axiology** as the umbrella database entity for a representation
of what values exist and, optionally, how they relate. It does not imply that
every representation is a philosophical theory.

| Representation | Example | Interpretation |
|---|---|---|
| Named dimensions | Schwartz-10, Hofstede-6 | fixed, labeled coordinates |
| Circumplex or hierarchy | Schwartz motivational circle | compatibility and opposition are part of the model |
| Survey item space | WVS | the question bank itself defines the operative space |
| Moral ontology | Moral Foundations Theory | moral concerns rather than a general-purpose value vector |
| Principle set | HHH, Constitutional AI | normative rules or desired behaviors |
| Induced factors | GPLA-5 | interpretable factors learned from model-generated material |
| Latent embedding | UniVaR | dense value-relevant coordinates without fixed human-readable axes |
| Open-ended space | Generative Psychometrics | arbitrary values can be supplied at measurement time |
| No explicit model | many alignment and preference studies | values are invoked implicitly or not operationalized |

A paper can use several axiologies in different roles: `primary`, `baseline`,
`mapping_target`, `alignment_target`, or `discovered_output`. When no explicit
axiology exists, the atlas records `implicit` or `none` rather than silently
leaving the field blank.

## Axiological spaces

| Axiology or value space | Shape | Typical use in AI research |
|---|---|---|
| [Schwartz Theory of Basic Human Values](https://doi.org/10.1016/S0065-2601(08)60281-6) | 10 values in a motivational circumplex; also four higher-order dimensions | questionnaires, scenario mapping, generated-text scoring, value conflict |
| [Refined Schwartz Theory](https://doi.org/10.1037/a0029393) | 19 basic values | higher-granularity human and AI profiling |
| [Moral Foundations Theory](https://doi.org/10.1037/a0015141) | moral foundations such as care and fairness | moral-language classification and model profiling |
| [World Values Survey](https://www.worldvaluessurvey.org/) | multilingual survey item space | human–AI comparison, cultural and political attitudes |
| [Inglehart–Welzel Cultural Map](https://www.worldvaluessurvey.org/WVSContents.jsp) | two cultural value dimensions | country and culture-level comparison |
| [Hofstede cultural dimensions](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/) | six national-culture dimensions | cultural alignment and language/persona audits |
| [GLOBE cultural dimensions](https://globeproject.com/study_2004_2007) | nine culture and leadership dimensions | cross-cultural model evaluation |
| [Rokeach Value System](https://psycnet.apa.org/record/2011-15663-000) | terminal and instrumental values | ranked value priorities |
| [Social Value Orientation](https://doi.org/10.1002/ejsp.1773) | allocation preferences | social decisions and behavioral games |
| [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) | values, rights, and duties ontology | pluralistic reasoning and conflict-aware alignment |
| [GPLA](https://aclanthology.org/2025.acl-long.585/) | five induced, interpretable factors | AI-native value-system construction |
| [UniVaR](https://aclanthology.org/2025.naacl-long.274/) | high-dimensional latent representation | model–language value embeddings and comparison |
| [Generative Psychometrics](https://doi.org/10.1609/aaai.v39i25.34839) | open-ended supplied values | free-response perception extraction and value scoring |
| [Helpful, Honest, and Harmless](https://arxiv.org/abs/2112.00861) | principle set | assistant behavior and preference modeling |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | written constitution or principle space | critique, revision, and alignment targets |

## Literature by research question

### Surveys and field overviews

- [A Systematic Review of Psychometric Evaluation of Large Language Models](https://arxiv.org/abs/2505.08245)
- [Large Language Models as Mirrors of Human Attitudes, Opinions, and Values](https://aclanthology.org/2024.findings-emnlp.513/)
- [Human Values and Alignment in Artificial Intelligence: A Survey](https://arxiv.org/abs/2404.10636)
- [Awesome LLM Values and Pluralistic Alignment](https://github.com/AIDASLab/Awesome-LLM-Values-and-Pluralistic-Alignment) — the closest existing values-focused catalog
- [Awesome LLM Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) — broader psychometric measurement literature
- [Towards Pluralistic Alignment of LLMs: A Comprehensive Survey](https://github.com/anudeex/Awesome-Pluralistic-Alignment)
- [Alignment Goal Survey](https://github.com/ValueCompass/Alignment-Goal-Survey) — representations and evaluations of alignment targets

### Questionnaires and elicited profiles

- [Who is GPT-3? An Exploration of Personality, Values and Demographics](https://aclanthology.org/2022.nlpcss-1.24/) — early questionnaire-based profiling
- [Stick to Your Role! Stability of Personal Values Expressed in Large Language Models](https://doi.org/10.1371/journal.pone.0309114) — role-conditioned Schwartz profiles
- [Do LLMs Have Consistent Values?](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf) — consistency across elicitation conditions
- [On the Credibility of Evaluating LLMs Using Survey Questions](https://aclanthology.org/2026.mme-main.2/) — survey validity and credibility
- [Assessing the Alignment of LLMs With Human Values for Mental Health Integration](https://doi.org/10.2196/55988) — Schwartz-based domain study
- [Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items](https://aclanthology.org/2025.acl-long.838/) — situation-based value items
- [Raising the Bar: Investigating the Values of LLMs via Generative Evolving Testing](https://openreview.net/forum?id=0REM9ydeLZ) — evolving rather than fixed tests
- [AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference](https://openreview.net/forum?id=qNlTH4kYJZ) — adaptive value-difference measurement
- [Cultural Value Alignment in LLMs: A Prompt-based Analysis of Schwartz Values](https://arxiv.org/abs/2505.17112) — cross-model prompt-based profiles

### Value understanding and benchmark tasks

- [Aligning AI With Shared Human Values](https://openreview.net/forum?id=dNy_RKzJacY) — ETHICS benchmark
- [Social Chemistry 101](https://aclanthology.org/2020.emnlp-main.48/) — social and moral norms
- [Moral Stories](https://aclanthology.org/2021.emnlp-main.54/) — norms, intentions, actions, and consequences
- [Can Machines Learn Morality? The Delphi Experiment](https://arxiv.org/abs/2110.07574) — descriptive ethics model and resource
- [ValueNet](https://doi.org/10.1609/aaai.v36i10.21368) — human-value-driven dialogue data
- [ValueEval](https://aclanthology.org/2023.semeval-1.313/) — values behind arguments
- [ValueBench](https://aclanthology.org/2024.acl-long.111/) — value orientation and understanding
- [WorldValuesBench](https://aclanthology.org/2024.lrec-main.1539/) — multicultural value awareness
- [Value Compass Benchmarks](https://aclanthology.org/2025.acl-demo.64/) — generative and evolving value evaluation
- [Structured Moral Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.1541/) — value-grounded moral evaluation
- [The Staircase of Ethics](https://aclanthology.org/2025.emnlp-main.806/) — multi-step induction to value conflicts

### Values in generated text

- [Value FULCRA](https://aclanthology.org/2024.naacl-long.486/) — complete-generation mapping into a Schwartz-style profile
- [Measuring Human and AI Values Based on Generative Psychometrics](https://doi.org/10.1609/aaai.v39i25.34839) — perception extraction followed by supplied-value scoring
- [CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses](https://arxiv.org/abs/2407.10725) — reference-free generated-response evaluation
- [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) — plural values, rights, and duties in generated reasoning
- [MoralBERT](https://arxiv.org/abs/2403.07678) — Moral Foundations signals in social discourse
- [ValueNet](https://liang-qiu.github.io/ValueNet/) — value-labeled dialogue situations and responses

### Choice, action, and cross-interface gaps

- [What's the Most Important Value? INVP](https://aclanthology.org/2025.coling-main.317/) — priorities through decisions in social scenarios
- [Mind the Value–Action Gap: Do LLMs Act in Alignment with Their Values?](https://aclanthology.org/2025.emnlp-main.154/) — stated inclinations versus value-relevant action
- [ValueCompass: Measuring Contextual Value Alignment Between Human and LLMs](https://aclanthology.org/2025.winlp-main.15/) — contextual human–model alignment
- [Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective](https://aclanthology.org/2025.findings-acl.1188/) — structural and causal analysis
- [The Theory of Planned Behavior](https://www.sciencedirect.com/science/article/pii/074959789190020T) — foundational attitude–intention–behavior distinction
- [A Value–Belief–Norm Theory of Support for Social Movements](http://www.jstor.org/stable/24707060) — value-to-action theoretical background

### Culture, language, and pluralism

- [Ethical Reasoning and Moral Value Alignment Depend on the Language We Prompt In](https://arxiv.org/abs/2404.18460)
- [Cultural Bias and Cultural Alignment of Large Language Models](https://doi.org/10.1093/pnasnexus/pgae346)
- [Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment](https://aclanthology.org/2025.emnlp-main.2/)
- [WorldValuesBench](https://aclanthology.org/2024.lrec-main.1539/) — country and culture-aware benchmark
- [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) — plural values, rights, and duties
- [Aligning Large Language Models with Diverse Political Viewpoints](https://aclanthology.org/2024.emnlp-main.412/)
- [Moral Foundations of Large Language Models](https://aclanthology.org/2024.emnlp-main.982/)
- [Awesome Cultural NLP](https://github.com/simran-khanuja/awesome-cultural-nlp) — broader cultural NLP map
- [Awesome Personalized Alignment](https://github.com/liyongqi2002/Awesome-Personalized-Alignment) — preference and user-conditioned alignment

### Representations, internals, and steering

- [GPLA: Generative Psycho-Lexical Approach for Constructing Value Systems in LLMs](https://aclanthology.org/2025.acl-long.585/) — interpretable AI-native factor construction
- [UniVaR: High-Dimension Human Value Representation in LLMs](https://aclanthology.org/2025.naacl-long.274/) — dense model–language representation
- [Internal Value Alignment through Controlled Value Vector Activation](https://aclanthology.org/2025.acl-long.1326/) — activation intervention
- [Understanding How Value Neurons Shape the Generation of Specified Values](https://aclanthology.org/2025.findings-emnlp.501/) — neuron-level analysis
- [Towards Better Value Principles for LLM Alignment](https://aclanthology.org/2025.acl-long.1408/) — evaluation and enhancement of value principles
- [Unintended Harms of Value-Aligned LLMs](https://aclanthology.org/2025.acl-long.1532/) — psychological and empirical consequences
- [Constitutional AI](https://arxiv.org/abs/2212.08073) — written principles as alignment targets

### Reliability, validity, and reporting

- [Measurement and Fairness](https://doi.org/10.1145/3442188.3445901) — construct, operationalization, and validity
- [POSIX: A Prompt Sensitivity Index for Large Language Models](https://arxiv.org/abs/2410.02185) — quantifying prompt sensitivity
- [On the Credibility of Evaluating LLMs Using Survey Questions](https://aclanthology.org/2026.mme-main.2/) — limits of survey transfer
- [Large Language Models Are Not Fair Evaluators](https://aclanthology.org/2024.acl-long.511/) — order and evaluator bias
- [AI Evaluation Should Learn from How We Test Humans](https://arxiv.org/abs/2306.10512) — position on measurement design
- [Holistic Evaluation of Language Models](https://openreview.net/forum?id=iO4LZibEqW) — multidimensional evaluation
- [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596)
- [Datasheets for Datasets](https://doi.org/10.1145/3458723)
- [Data Statements for NLP](https://aclanthology.org/Q18-1041/)
- [Closing the AI Accountability Gap](https://doi.org/10.1145/3351095.3372873) — end-to-end internal auditing

## Datasets, benchmarks, and instruments

| Resource | Kind | Value space or construct | Primary link |
|---|---|---|---|
| Value Portrait | scenario item bank | Schwartz-10 | [paper](https://aclanthology.org/2025.acl-long.838/) |
| ValueBench | benchmark and code | value orientation and understanding | [paper](https://aclanthology.org/2024.acl-long.111/) · [code](https://github.com/Value4AI/ValueBench) |
| WorldValuesBench | multilingual benchmark | cultural values | [paper](https://aclanthology.org/2024.lrec-main.1539/) |
| ValueNet | dataset | Schwartz-style human values in dialogue | [dataset](https://liang-qiu.github.io/ValueNet/) |
| ValueEval | shared task | human values behind arguments | [paper](https://aclanthology.org/2023.semeval-1.313/) |
| Value FULCRA | response corpus and measurement pipeline | Schwartz-style output profiles | [paper](https://aclanthology.org/2024.naacl-long.486/) |
| Value Kaleidoscope | dataset and ontology | values, rights, and duties | [paper](https://doi.org/10.1609/aaai.v38i18.29970) |
| ETHICS | benchmark suite | justice, virtue, deontology, commonsense morality | [paper](https://openreview.net/forum?id=dNy_RKzJacY) |
| Social Chemistry 101 | norm knowledge base | rules-of-thumb and social judgments | [paper](https://aclanthology.org/2020.emnlp-main.48/) |
| Moral Stories | story corpus | norms, intentions, actions, consequences | [paper](https://aclanthology.org/2021.emnlp-main.54/) |
| World Values Survey | survey and microdata | survey item space and cultural dimensions | [project](https://www.worldvaluessurvey.org/) |
| PVQ-40 / PVQ-RR | questionnaire family | Schwartz values | [measurement source](https://doi.org/10.1177/0022022101032005001) |

## Models, scorers, and representation tools

These are computational components, not value theories. Their output only has
meaning together with the prompt, input unit, value space, aggregation policy,
coverage, and validation evidence.

| Tool | Role | Output | Link |
|---|---|---|---|
| ValueLlama-3-8B | open-ended value scorer used in Generative Psychometrics | relevance and signed orientation toward a supplied value | [model](https://huggingface.co/Value4AI/ValueLlama-3-8B) |
| UniVaR lambda-1 | value-relevant embedding encoder | dense model–language representation | [model](https://huggingface.co/CAiRE/UniVaR-lambda-1) · [code](https://github.com/HLTCHKUST/UniVaR) |
| MoralBERT | Moral Foundations classifier family | moral-foundation labels or signals | [code](https://github.com/vjosapreniqi/MoralBERT) |
| FULCRA | generated-text mapping pipeline | multidimensional basic-human-value profile | [paper](https://aclanthology.org/2024.naacl-long.486/) |
| CLAVE | adaptive generated-response evaluator | reference-free value assessment | [paper](https://arxiv.org/abs/2407.10725) |

## Data and contribution model

The README is the human entry point; the structured files support reproducible
search, deduplication, and future systematic curation.

```text
work ──< study >── axiology
           ├────── instrument
           ├────── dataset
           ├────── model + role
           └────── validation evidence
```

| Data layer | Meaning |
|---|---|
| [`data/raw/catalog_links.jsonl`](data/raw/catalog_links.jsonl) | deduplicated discovery queue with source and section provenance |
| [`data/curated/works.jsonl`](data/curated/works.jsonl) | publication records checked against a primary page |
| [`data/curated/studies.jsonl`](data/curated/studies.jsonl) | experiment-level interfaces, value spaces, scorers, and validation |
| [`data/curated/axiologies.json`](data/curated/axiologies.json) | named, induced, latent, principle-based, and open-ended value spaces |
| [`data/catalog_sources.json`](data/catalog_sources.json) | public source catalogs and inclusion rules |

Detailed definitions live in [DATA_MODEL.md](docs/DATA_MODEL.md), scope rules in
[SCOPE.md](docs/SCOPE.md), and review policy in [CURATION.md](docs/CURATION.md).

### Contributing

Contributions can add a missing work, correct a link, enrich a discovery record,
or document a study's actual measurement contract. Method claims should cite the
paper itself; awesome lists and generated summaries are discovery aids. See the
[contribution guide](CONTRIBUTING.md).

### Rebuild

```bash
python3 scripts/sync_sources.py
python3 scripts/harvest_catalogs.py
python3 scripts/validate.py
python3 scripts/build_catalog.py
```

### License

Original code is MIT. Original structured metadata and documentation are CC BY
4.0. Linked papers, datasets, models, and third-party repositories retain their
own licenses and copyright.
