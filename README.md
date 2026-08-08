<div align="center">

<img src="assets/atlas-header.svg" width="100%" alt="AI Values Atlas — open research field guide" />

<h1>AI Values Atlas</h1>

<p><strong>A field guide to how values are represented, elicited, expressed, chosen, and evaluated in AI systems.</strong></p>

<p><strong>English</strong> · <a href="README_RU.md">Русский</a></p>

<p>
  <a href="https://ikanam-ai.github.io/ai-values-atlas/">Explore the atlas</a> ·
  <a href="#field-map">Field map</a> ·
  <a href="#literature-by-research-question">Literature</a> ·
  <a href="#axiological-spaces">Axiologies</a> ·
  <a href="#datasets-benchmarks-and-instruments">Datasets & benchmarks</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p>
  <a href="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml"><img alt="validation" src="https://img.shields.io/github/actions/workflow/status/ikanam-ai/ai-values-atlas/validate.yml?style=for-the-badge&label=validated"></a>
  <a href="#complete-catalog"><img alt="resources" src="https://img.shields.io/badge/resources-1018-136f58?style=for-the-badge"></a>
  <a href="#complete-catalog"><img alt="publications" src="https://img.shields.io/badge/publication%20links-786-0d3f35?style=for-the-badge"></a>
  <a href="CONTRIBUTING.md"><img alt="pull requests welcome" src="https://img.shields.io/badge/PRs-welcome-e9b44c?style=for-the-badge"></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/metadata-CC%20BY%204.0-7665d8?style=for-the-badge"></a>
</p>

</div>

| [🧭 **Field map**](#field-map) | [📚 **Complete catalog**](#complete-catalog) | [🧠 **Axiologies**](#axiological-spaces) | [💾 **Datasets**](#datasets-benchmarks-and-instruments) | [🧰 **Models & tools**](#models-scorers-and-representation-tools) |
|:---:|:---:|:---:|:---:|:---:|

AI Values Atlas is an open map of research on values in language models and
other AI systems. It connects theories, papers, benchmarks, datasets,
questionnaires, scenarios, scorers, representation models, and validation
evidence without pretending that they measure the same thing.

> **The central rule:** a value framework is not an instrument; an instrument
> is not a scorer; endorsement is not choice; generated text is not behavior;
> and a reliable profile is not automatically a valid or model-specific one.

The lists below are a human-oriented guide to the field. The
[full discovery index](https://ikanam-ai.github.io/ai-values-atlas/) contains
1018 deduplicated links harvested from ten public research catalogs and the
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
- [Complete catalog — all 1018 links](#complete-catalog)
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

- **A Systematic Review of Psychometric Evaluation of Large Language Models**, 2025 [[paper](https://arxiv.org/abs/2505.08245)]
- **Large Language Models as Mirrors of Human Attitudes, Opinions, and Values**, 2024 [[paper](https://aclanthology.org/2024.findings-emnlp.513/)]
- **Human Values and Alignment in Artificial Intelligence: A Survey**, 2024 [[paper](https://arxiv.org/abs/2404.10636)]
- **Awesome LLM Values and Pluralistic Alignment** [[catalog](https://github.com/AIDASLab/Awesome-LLM-Values-and-Pluralistic-Alignment)] — the closest existing values-focused catalog
- **Awesome LLM Psychometrics** [[catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)] — broader psychometric measurement literature
- **Towards Pluralistic Alignment of LLMs: A Comprehensive Survey** [[catalog](https://github.com/anudeex/Awesome-Pluralistic-Alignment)]
- **Alignment Goal Survey** [[catalog](https://github.com/ValueCompass/Alignment-Goal-Survey)] — representations and evaluations of alignment targets

### Questionnaires and elicited profiles

- **Who is GPT-3? An Exploration of Personality, Values and Demographics**, 2022 [[paper](https://aclanthology.org/2022.nlpcss-1.24/)] — early questionnaire-based profiling
- **Stick to Your Role! Stability of Personal Values Expressed in Large Language Models**, 2024 [[paper](https://doi.org/10.1371/journal.pone.0309114)] — role-conditioned Schwartz profiles
- **Do LLMs Have Consistent Values?**, 2025 [[paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)] — consistency across elicitation conditions
- **On the Credibility of Evaluating LLMs Using Survey Questions**, 2026 [[paper](https://aclanthology.org/2026.mme-main.2/)] — survey validity and credibility
- **Assessing the Alignment of LLMs With Human Values for Mental Health Integration**, 2024 [[paper](https://doi.org/10.2196/55988)] — Schwartz-based domain study
- **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items**, 2025 [[paper](https://aclanthology.org/2025.acl-long.838/)] — situation-based value items
- **Raising the Bar: Investigating the Values of LLMs via Generative Evolving Testing**, 2025 [[paper](https://openreview.net/forum?id=0REM9ydeLZ)] — evolving rather than fixed tests
- **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference**, 2026 [[paper](https://openreview.net/forum?id=qNlTH4kYJZ)] — adaptive value-difference measurement
- **Cultural Value Alignment in LLMs: A Prompt-based Analysis of Schwartz Values**, 2025 [[paper](https://arxiv.org/abs/2505.17112)] — cross-model prompt-based profiles

### Value understanding and benchmark tasks

- **Aligning AI With Shared Human Values**, 2021 [[paper](https://openreview.net/forum?id=dNy_RKzJacY)] — ETHICS benchmark
- **Social Chemistry 101**, 2020 [[paper](https://aclanthology.org/2020.emnlp-main.48/)] — social and moral norms
- **Moral Stories**, 2021 [[paper](https://aclanthology.org/2021.emnlp-main.54/)] — norms, intentions, actions, and consequences
- **Can Machines Learn Morality? The Delphi Experiment**, 2021 [[paper](https://arxiv.org/abs/2110.07574)] — descriptive ethics model and resource
- **ValueNet**, 2022 [[paper](https://doi.org/10.1609/aaai.v36i10.21368)] — human-value-driven dialogue data
- **ValueEval**, 2023 [[paper](https://aclanthology.org/2023.semeval-1.313/)] — values behind arguments
- **ValueBench**, 2024 [[paper](https://aclanthology.org/2024.acl-long.111/)] — value orientation and understanding
- **WorldValuesBench**, 2024 [[paper](https://aclanthology.org/2024.lrec-main.1539/)] — multicultural value awareness
- **Value Compass Benchmarks**, 2025 [[paper](https://aclanthology.org/2025.acl-demo.64/)] — generative and evolving value evaluation
- **Structured Moral Reasoning in Language Models**, 2025 [[paper](https://aclanthology.org/2025.emnlp-main.1541/)] — value-grounded moral evaluation
- **The Staircase of Ethics**, 2025 [[paper](https://aclanthology.org/2025.emnlp-main.806/)] — multi-step induction to value conflicts

### Values in generated text

- **Value FULCRA**, 2024 [[paper](https://aclanthology.org/2024.naacl-long.486/)] — complete-generation mapping into a Schwartz-style profile
- **Measuring Human and AI Values Based on Generative Psychometrics**, 2025 [[paper](https://doi.org/10.1609/aaai.v39i25.34839)] — perception extraction followed by supplied-value scoring
- **CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses**, 2024 [[paper](https://arxiv.org/abs/2407.10725)] — reference-free generated-response evaluation
- **Value Kaleidoscope**, 2024 [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] — plural values, rights, and duties in generated reasoning
- **MoralBERT**, 2024 [[paper](https://arxiv.org/abs/2403.07678)] — Moral Foundations signals in social discourse
- **ValueNet**, 2022 [[paper](https://liang-qiu.github.io/ValueNet/)] — value-labeled dialogue situations and responses

### Choice, action, and cross-interface gaps

- **What's the Most Important Value? INVP**, 2025 [[paper](https://aclanthology.org/2025.coling-main.317/)] — priorities through decisions in social scenarios
- **Mind the Value–Action Gap: Do LLMs Act in Alignment with Their Values?**, 2025 [[paper](https://aclanthology.org/2025.emnlp-main.154/)] — stated inclinations versus value-relevant action
- **ValueCompass: Measuring Contextual Value Alignment Between Human and LLMs**, 2025 [[paper](https://aclanthology.org/2025.winlp-main.15/)] — contextual human–model alignment
- **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective**, 2025 [[paper](https://aclanthology.org/2025.findings-acl.1188/)] — structural and causal analysis
- **The Theory of Planned Behavior**, 1991 [[paper](https://www.sciencedirect.com/science/article/pii/074959789190020T)] — foundational attitude–intention–behavior distinction
- **A Value–Belief–Norm Theory of Support for Social Movements**, 1999 [[paper](http://www.jstor.org/stable/24707060)] — value-to-action theoretical background

### Culture, language, and pluralism

- **Ethical Reasoning and Moral Value Alignment Depend on the Language We Prompt In**, 2024 [[paper](https://arxiv.org/abs/2404.18460)]
- **Cultural Bias and Cultural Alignment of Large Language Models**, 2024 [[paper](https://doi.org/10.1093/pnasnexus/pgae346)]
- **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment**, 2025 [[paper](https://aclanthology.org/2025.emnlp-main.2/)]
- **WorldValuesBench**, 2024 [[paper](https://aclanthology.org/2024.lrec-main.1539/)] — country and culture-aware benchmark
- **Value Kaleidoscope**, 2024 [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] — plural values, rights, and duties
- **Aligning Large Language Models with Diverse Political Viewpoints**, 2024 [[paper](https://aclanthology.org/2024.emnlp-main.412/)]
- **Moral Foundations of Large Language Models**, 2024 [[paper](https://aclanthology.org/2024.emnlp-main.982/)]
- **Awesome Cultural NLP** [[catalog](https://github.com/simran-khanuja/awesome-cultural-nlp)] — broader cultural NLP map
- **Awesome Personalized Alignment** [[catalog](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)] — preference and user-conditioned alignment

### Representations, internals, and steering

- **GPLA: Generative Psycho-Lexical Approach for Constructing Value Systems in LLMs**, 2025 [[paper](https://aclanthology.org/2025.acl-long.585/)] — interpretable AI-native factor construction
- **UniVaR: High-Dimension Human Value Representation in LLMs**, 2025 [[paper](https://aclanthology.org/2025.naacl-long.274/)] — dense model–language representation
- **Internal Value Alignment through Controlled Value Vector Activation**, 2025 [[paper](https://aclanthology.org/2025.acl-long.1326/)] — activation intervention
- **Understanding How Value Neurons Shape the Generation of Specified Values**, 2025 [[paper](https://aclanthology.org/2025.findings-emnlp.501/)] — neuron-level analysis
- **Towards Better Value Principles for LLM Alignment**, 2025 [[paper](https://aclanthology.org/2025.acl-long.1408/)] — evaluation and enhancement of value principles
- **Unintended Harms of Value-Aligned LLMs**, 2025 [[paper](https://aclanthology.org/2025.acl-long.1532/)] — psychological and empirical consequences
- **Constitutional AI**, 2022 [[paper](https://arxiv.org/abs/2212.08073)] — written principles as alignment targets

### Reliability, validity, and reporting

- **Measurement and Fairness**, 2021 [[paper](https://doi.org/10.1145/3442188.3445901)] — construct, operationalization, and validity
- **POSIX: A Prompt Sensitivity Index for Large Language Models**, 2024 [[paper](https://arxiv.org/abs/2410.02185)] — quantifying prompt sensitivity
- **On the Credibility of Evaluating LLMs Using Survey Questions**, 2026 [[paper](https://aclanthology.org/2026.mme-main.2/)] — limits of survey transfer
- **Large Language Models Are Not Fair Evaluators**, 2024 [[paper](https://aclanthology.org/2024.acl-long.511/)] — order and evaluator bias
- **AI Evaluation Should Learn from How We Test Humans**, 2023 [[paper](https://arxiv.org/abs/2306.10512)] — position on measurement design
- **Holistic Evaluation of Language Models**, 2023 [[paper](https://openreview.net/forum?id=iO4LZibEqW)] — multidimensional evaluation
- **Model Cards for Model Reporting**, 2019 [[paper](https://doi.org/10.1145/3287560.3287596)]
- **Datasheets for Datasets**, 2021 [[paper](https://doi.org/10.1145/3458723)]
- **Data Statements for NLP**, 2018 [[paper](https://aclanthology.org/Q18-1041/)]
- **Closing the AI Accountability Gap**, 2020 [[paper](https://doi.org/10.1145/3351095.3372873)] — end-to-end internal auditing

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

## Complete catalog

The catalog below contains every unique URL in the repository. Publications are
grouped by research topic; datasets, models, repositories, projects, and survey
resources have dedicated sections. All entries are visible and searchable
directly on GitHub.

<!-- complete-catalog:start -->

> This section is generated from the deduplicated discovery index. Every
> URL appears exactly once here; provenance and scope labels remain visible.

**Browse the taxonomy**

| Research area | Publications |
|---|---:|
| [🗺️ Surveys, reviews, and field overviews](#catalog-surveys-reviews-and-field-overviews) | 49 |
| [🧭 Foundations and value theory](#catalog-foundations-and-value-theory) | 7 |
| [🗂️ Datasets and benchmarks](#catalog-datasets-and-benchmarks) | 103 |
| [🔬 Reliability, validity, and auditing](#catalog-reliability-validity-and-auditing) | 17 |
| [🎯 Choice, action, and behavioral consistency](#catalog-choice-action-and-behavioral-consistency) | 15 |
| [🌍 Culture, language, and pluralism](#catalog-culture-language-and-pluralism) | 103 |
| [🗣️ Preferences, opinions, and social simulation](#catalog-preferences-opinions-and-social-simulation) | 120 |
| [⚖️ Moral reasoning and value understanding](#catalog-moral-reasoning-and-value-understanding) | 63 |
| [🧰 Alignment, steering, and preferences](#catalog-alignment-steering-and-preferences) | 133 |
| [📐 Value representation and model internals](#catalog-value-representation-and-model-internals) | 44 |
| [📏 Measurement and profiling](#catalog-measurement-and-profiling) | 87 |
| [📎 Other and adjacent value research](#catalog-other-and-adjacent-value-research) | 45 |

> **Legend:** `core` records focus directly on values; `adjacent` records provide broader context. Source catalogs follow each link.

### 📚 Publications by research topic

<a id="catalog-surveys-reviews-and-field-overviews"></a>

#### 🗺️ Surveys, reviews, and field overviews · 49

- **A roadmap for evaluating moral competence in large language models**, 2026 — [[paper](https://nature.com/articles/s41586-025-10021-1)] · core · via: AIDAS Values & Pluralism
- **A Survey of Progress in LLM Alignment from the Perspective of Reward Design**, 2026 — [[paper](https://ieeexplore.ieee.org/abstract/document/11361384)] · core · via: Pluralistic Alignment
- **A Survey on Evaluation of Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2307.03109)] · adjacent · via: LLM Social Science
- **A Survey on Human-Centric LLMs**, 2024 — [[paper](https://arxiv.org/abs/2411.14491)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **A Survey on Large Language Model based Autonomous Agents**, 2023 — [[paper](https://arxiv.org/abs/2308.11432)] · adjacent · via: LLM Social Science
- **A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications**, 2025 — [[paper](https://arxiv.org/abs/2503.17003)] · adjacent · via: Personalized Alignment
- **A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2504.07070)] · core · via: AIDAS Values & Pluralism, Personalized Alignment, Pluralistic Alignment
- **AI Alignment and Social Choice: Fundamental Limitations and Policy Implications**, 2023 — [[paper](https://arxiv.org/abs/2310.16048)] · core · via: AIDAS Values & Pluralism
- **AI Alignment From Social Choice Perspectives**, 2026 — [[paper](https://arxiv.org/abs/2606.21550)] · core · via: AIDAS Values & Pluralism
- **AI Alignment: A Comprehensive Survey**, 2023 — [[paper](https://arxiv.org/abs/2310.19852)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Aligning Large Language Models with Human: A Survey**, 2023 — [[paper](https://arxiv.org/abs/2307.12966)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap**, 2025 — [[paper](https://arxiv.org/abs/2508.18646)] · core · via: AIDAS Values & Pluralism
- **Cultural Bias and Cultural Alignment of Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2311.14096)] · core · via: AIDAS Values & Pluralism
- **Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation**, 2025 — [[paper](https://arxiv.org/abs/2509.08858)] · core · via: AIDAS Values & Pluralism
- **Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens**, 2025 — [[paper](https://arxiv.org/abs/2508.16982)] · core · via: AIDAS Values & Pluralism
- **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents**, 2024 — [[paper](https://arxiv.org/abs/2412.03563)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models**, 2023 — [[paper](https://arxiv.org/abs/2308.12014)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications**, 2025 — [[paper](https://arxiv.org/abs/2505.00049)] · core · via: LLM Psychometrics
- **Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges**, 2025 — [[paper](https://arxiv.org/abs/2507.19364)] · core · via: AIDAS Values & Pluralism
- **Large Language Model based Multi-Agents: A Survey of Progress and Challenges**, 2024 — [[paper](https://arxiv.org/abs/2402.01680)] · adjacent · via: LLM Social Science
- **Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**, 2025 — [[paper](https://arxiv.org/abs/2505.08245)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Large language models empowered agent-based modeling and simulation: a survey and perspectives**, 2024 — [[paper](https://nature.com/articles/s41599-024-03611-3)] · core · via: AIDAS Values & Pluralism
- **Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences**, 2026 — [[paper](https://arxiv.org/abs/2606.07629)] · core · via: AIDAS Values & Pluralism
- **LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency**, 2026 — [[paper](https://link.springer.com/article/10.1007/s12559-026-10568-9)] · core · via: AIDAS Values & Pluralism
- **LLM Social Simulations Are a Promising Research Method**, 2025 — [[paper](https://arxiv.org/abs/2504.02234)] · core · via: AIDAS Values & Pluralism
- **LLM-Based Social Simulations Require a Boundary**, 2025 — [[paper](https://arxiv.org/abs/2506.19806)] · core · via: AIDAS Values & Pluralism
- **LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods**, 2024 — [[paper](https://arxiv.org/abs/2412.05579)] · adjacent · via: LLM Social Science
- **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs**, 2025 — [[paper](https://aclanthology.org/2025.findings-acl.1246/)] · adjacent · via: LLM Social Science
- **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs**, 2025 — [[paper](https://arxiv.org/abs/2511.01864)] · core · via: AIDAS Values & Pluralism
- **Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment**, 2026 — [[paper](https://arxiv.org/abs/2602.03003)] · core · via: AIDAS Values & Pluralism
- **Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior**, 2025 — [[paper](https://arxiv.org/abs/2511.14476)] · core · via: AIDAS Values & Pluralism
- **Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback**, 2023 — [[paper](https://arxiv.org/abs/2303.05453)] · core · via: AIDAS Values & Pluralism
- **Personalization of Large Language Models: A Survey**, 2024 — [[paper](https://arxiv.org/abs/2411.00027)] · core · via: Personalized Alignment, Pluralistic Alignment
- **Personalized Multimodal Large Language Models: A Survey**, 2024 — [[paper](https://arxiv.org/abs/2412.02142)] · adjacent · via: Personalized Alignment
- **Position: A Roadmap to Pluralistic Alignment**, 2024 — [[paper](https://openreview.net/forum?id=gQpBnRHwxM)] · adjacent · via: Personalized Alignment
- **Position: AI Agents Are Not (Yet) a Panacea for Social Simulation**, 2026 — [[paper](https://arxiv.org/abs/2603.00113)] · core · via: AIDAS Values & Pluralism
- **Position: Towards Bidirectional Human-AI Alignment**, 2024 — [[paper](https://arxiv.org/abs/2406.09264)] · core · via: AIDAS Values & Pluralism
- **Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations**, 2024 — [[paper](https://aclanthology.org/2024.lrec-main.1192/)] · adjacent · via: Personalized Alignment
- **Simulating Society Requires Simulating Thought**, 2025 — [[paper](https://arxiv.org/abs/2506.06958)] · core · via: AIDAS Values & Pluralism
- **Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback**, 2024 — [[paper](https://arxiv.org/abs/2404.10271)] · core · via: AIDAS Values & Pluralism
- **Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits**, 2026 — [[paper](https://arxiv.org/abs/2605.18890)] · core · via: AIDAS Values & Pluralism
- **The benefits, risks and bounds of personalizing the alignment of large language models to individuals**, 2024 — [[paper](https://nature.com/articles/s42256-024-00820-y)] · adjacent · via: Personalized Alignment
- **The Mind in the Machine: A Survey of Incorporating Psychological Theories in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2505.00003)] · core · via: LLM Psychometrics
- **The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm**, 2024 — [[paper](https://arxiv.org/abs/2406.18682)] · adjacent · via: Personalized Alignment
- **The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment**, 2024 — [[paper](https://arxiv.org/abs/2412.16468)] · adjacent · via: LLM Social Science
- **The threat of analytic flexibility in using large language models to simulate human data: A call to attention**, 2025 — [[paper](https://arxiv.org/abs/2509.13397)] · core · via: AIDAS Values & Pluralism
- **Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents**, 2025 — [[paper](https://arxiv.org/abs/2503.24047)] · adjacent · via: LLM Social Science
- **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization**, 2024 — [[paper](https://aclanthology.org/2024.findings-emnlp.969/)] · adjacent · via: Personalized Alignment
- **When large language models meet personalization: perspectives of challenges and opportunities**, 2024 — [[paper](https://doi.org/10.1007/s11280-024-01276-1)] · adjacent · via: Personalized Alignment

<a id="catalog-foundations-and-value-theory"></a>

#### 🧭 Foundations and value theory · 7

- **Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values**, 2024 — [[paper](https://doi.org/10.2196/55988)] · core · via: STONIC bibliography
- **Axioms for AI Alignment from Human Feedback**, 2024 — [[paper](https://arxiv.org/abs/2405.14758)] · core · via: AIDAS Values & Pluralism
- **Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement**, 2001 — [[paper](https://doi.org/10.1177/0022022101032005001)] · core · via: STONIC bibliography
- **Moral foundations theory: The pragmatic validity of moral pluralism. Graham et al. Advances in experimental social psychology, 2013.**, 2013 — [[paper](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **Optimized Distortion in Linear Social Choice**, 2025 — [[paper](https://arxiv.org/abs/2510.20020)] · core · via: AIDAS Values & Pluralism
- **Representative Social Choice: From Learning Theory to AI Alignment**, 2024 — [[paper](https://arxiv.org/abs/2410.23953)] · core · via: AIDAS Values & Pluralism
- **Strategy-proofness and Arrow's Conditions**, 1975 — [[paper](https://sciencedirect.com/science/article/pii/0022053175900502)] · core · via: AIDAS Values & Pluralism

<a id="catalog-datasets-and-benchmarks"></a>

#### 🗂️ Datasets and benchmarks · 103

- **(ETHICS) Aligning AI With Shared Human Values**, 2020 — [[paper](https://arxiv.org/abs/2008.02275)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **(MoralChoice) Evaluating the Moral Beliefs Encoded in LLMs**, 2023 — [[paper](https://arxiv.org/abs/2307.14324)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **(NYTBookOpinions) Benchmarking Distributional Alignment of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2411.05403)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **(Valueeval) The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments**, 2023 — [[paper](https://arxiv.org/abs/2301.13771)] · core · via: AIDAS Values & Pluralism
- **A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values**, 2025 — [[paper](https://openreview.net/forum?id=oSRqZO2O2O)] · core · via: Pluralistic Alignment
- **A Unified Moral-Value Dataset for Instruction Tuning**, 2026 — [[paper](https://arxiv.org/abs/2607.21279)] · core · via: AIDAS Values & Pluralism
- **Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts**, 2023 — [[paper](https://arxiv.org/abs/2305.13300)] · core · via: Pluralistic Alignment
- **Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values**, 2026 — [[paper](https://arxiv.org/abs/2605.10365)] · core · via: AIDAS Values & Pluralism
- **An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance**, 2024 — [[paper](https://arxiv.org/abs/2404.01247)] · adjacent · via: Awesome Cultural NLP
- **Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral**, 2025 — [[paper](https://arxiv.org/abs/2502.14083)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models, NeurIPS 2024**, 2024 — [[paper](https://arxiv.org/abs/2402.11894)] · adjacent · via: LLM Social Science
- **BBQ: A hand-built bias benchmark for question answering**, 2022 — [[paper](https://aclanthology.org/2022.findings-acl.165/)] · core · via: STONIC bibliography
- **Benchmarking Distributional Alignment of Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.2/)] · core · via: Pluralistic Alignment
- **Benchmarking Multi-National Value Alignment for Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2504.12911)] · adjacent · via: LLM Social Science
- **Benchmarking Overton Pluralism in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2512.01351)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **Beyond Aesthetics: Cultural Competence in Text-to-Image Models**, 2024 — [[paper](https://arxiv.org/abs/2407.06863)] · adjacent · via: Awesome Cultural NLP
- **Big-Math 2025-2**, 2025 — [[paper](https://arxiv.org/abs/2502.17387)] · adjacent · via: Awesome LLM Datasets
- **Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys**, 2024 — [[paper](https://arxiv.org/abs/2401.10352)] · adjacent · via: Awesome Cultural NLP
- **C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2506.01495)] · core · via: AIDAS Values & Pluralism
- **Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs**, 2025 — [[paper](https://arxiv.org/abs/2510.05154)] · core · via: AIDAS Values & Pluralism
- **Can Language Models Reason about Individualistic Human Values and Preferences?**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.336/)] · core · via: Pluralistic Alignment
- **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2405.13974)] · core · via: AIDAS Values & Pluralism
- **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models**, 2024 — [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31710)] · core · via: Pluralistic Alignment
- **CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives**, 2025 — [[paper](https://arxiv.org/abs/2504.10823)] · core · via: AIDAS Values & Pluralism
- **CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean**, 2024 — [[paper](https://arxiv.org/abs/2403.06412)] · adjacent · via: Awesome Cultural NLP
- **COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values**, 2025 — [[paper](https://arxiv.org/abs/2504.05535)] · adjacent · via: LLM Social Science
- **ComPO: Community Preferences for Language Model Personalization**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.419/)] · core · via: Pluralistic Alignment
- **Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024**, 2024 — [[paper](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768)] · adjacent · via: LLM Social Science
- **Culturally Aware Natural Language Inference**, 2023 — [[paper](https://aclanthology.org/2023.findings-emnlp.509/)] · adjacent · via: Awesome Cultural NLP
- **D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios**, 2026 — [[paper](https://arxiv.org/abs/2607.19834)] · core · via: AIDAS Values & Pluralism
- **Datasheets for datasets**, 2021 — [[paper](https://doi.org/10.1145/3458723)] · core · via: STONIC bibliography
- **DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context**, 2025 — [[paper](https://arxiv.org/abs/2509.17399)] · adjacent · via: Awesome Cultural NLP
- **DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures**, 2024 — [[paper](https://arxiv.org/abs/2403.14651)] · adjacent · via: Awesome Cultural NLP
- **EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English**, 2022 — [[paper](https://arxiv.org/abs/2203.14498)] · adjacent · via: Awesome Cultural NLP
- **Evaluating and Inducing Personality in Pre-trained Language Models**, 2022 — [[paper](https://arxiv.org/abs/2206.07550)] · core · via: Pluralistic Alignment
- **Evaluating the Prompt Steerability of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2411.12405)] · core · via: AIDAS Values & Pluralism
- **EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences**, 2025 — [[paper](https://arxiv.org/abs/2510.06370)] · core · via: Pluralistic Alignment
- **Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark**, 2026 — [[paper](https://arxiv.org/abs/2603.17838)] · core · via: AIDAS Values & Pluralism
- **Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis**, 2024 — [[paper](https://arxiv.org/abs/2308.16705)] · adjacent · via: Awesome Cultural NLP
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-main.1063/)] · adjacent · via: Awesome Cultural NLP
- **FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models**, 2023 — [[paper](https://aclanthology.org/2023.findings-acl.631/)] · adjacent · via: Awesome Cultural NLP
- **GeoDE: a Geographically Diverse Evaluation Dataset for Object Recognition**, 2023 — [[paper](https://arxiv.org/abs/2301.02560)] · adjacent · via: Awesome Cultural NLP
- **GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking**, 2025 — [[paper](https://arxiv.org/abs/2502.13766)] · adjacent · via: Awesome Cultural NLP
- **Global Voices, Local Biases: Socio-Cultural Prejudices across Languages**, 2023 — [[paper](https://arxiv.org/abs/2310.17586)] · adjacent · via: Awesome Cultural NLP
- **HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter, ACL 2025 Outstanding Paper**, 2025 — [[paper](https://arxiv.org/abs/2411.15462)] · adjacent · via: LLM Social Science
- **HelpSteer 2: Open-source dataset for training top-performing reward models**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)] · core · via: Pluralistic Alignment
- **KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge**, 2024 — [[paper](https://aclanthology.org/2024.findings-acl.666/)] · core · via: Pluralistic Alignment
- **LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces**, 2025 — [[paper](https://arxiv.org/abs/2503.01894)] · core · via: Pluralistic Alignment
- **LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2505.00853)] · core · via: AIDAS Values & Pluralism
- **M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks**, 2024 — [[paper](https://arxiv.org/abs/2407.03791)] · adjacent · via: Awesome Cultural NLP
- **Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking**, 2024 — [[paper](https://arxiv.org/abs/2402.09369)] · adjacent · via: Awesome Cultural NLP
- **MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation**, 2025 — [[paper](https://arxiv.org/abs/2506.19073)] · core · via: AIDAS Values & Pluralism
- **MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces**, 2024 — [[paper](https://openreview.net/forum?id=kyfkMRT4Ao)] · core · via: Pluralistic Alignment
- **Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment**, 2020 — [[paper](https://journals.sagepub.com/doi/10.1177/1948550619876629)] · core · via: AIDAS Values & Pluralism
- **Moral foundations twitter corpus: A collection of 35k tweets annotated for moral sentiment. Hoover et al. Social Psychological and Personality Science 2020.**, 2020 — [[paper](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)] · core · via: Alignment Goal Survey
- **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences**, 2020 — [[paper](https://arxiv.org/abs/2012.15738)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey
- **MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes**, 2025 — [[paper](https://arxiv.org/abs/2510.16380)] · core · via: AIDAS Values & Pluralism
- **Multi-lingual and Multi-cultural Figurative Language Understanding**, 2023 — [[paper](https://arxiv.org/abs/2305.16171)] · adjacent · via: Awesome Cultural NLP
- **Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision-Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.490/)] · adjacent · via: Awesome Cultural NLP
- **Navigating the Cultural Kaleidoscope: A Hitchhiker’s Guide to Sensitivity in Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.388/)] · core · via: Pluralistic Alignment
- **NLPositionality: Characterizing Design Biases of Datasets and Models**, 2023 — [[paper](https://aclanthology.org/2023.acl-long.505/)] · adjacent · via: Awesome Cultural NLP
- **NormBank: A Knowledge Bank of Situational Social Norms**, 2023 — [[paper](https://aclanthology.org/2023.acl-long.429/)] · core · via: Pluralistic Alignment
- **NormBank: A Knowledge Bank of Situational Social Norms**, 2023 — [[paper](https://arxiv.org/abs/2305.17008)] · core · via: AIDAS Values & Pluralism
- **NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly**, 2023 — [[paper](https://arxiv.org/abs/2210.08604)] · adjacent · via: Awesome Cultural NLP
- **NoveltyBench: Evaluating Language Models for Humanlike Diversity**, 2025 — [[paper](https://arxiv.org/abs/2504.05228)] · core · via: Pluralistic Alignment
- **PerSpectra: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments**, 2026 — [[paper](https://arxiv.org/abs/2602.08716)] · core · via: AIDAS Values & Pluralism
- **PLURAL: A Global Dataset for Value Alignment**, 2026 — [[paper](https://arxiv.org/abs/2607.08034)] · core · via: AIDAS Values & Pluralism
- **PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm**, 2026 — [[paper](https://arxiv.org/abs/2601.08951)] · core · via: Pluralistic Alignment
- **Polar: A Benchmark for Evaluating Political Bias in LLMs**, 2026 — [[paper](https://arxiv.org/abs/2606.12922)] · core · via: AIDAS Values & Pluralism
- **Process for adapting language models to society (palms) with values-targeted datasets. Solaiman et al. Neurips 2021.**, 2021 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)] · core · via: Alignment Goal Survey
- **ProsocialDialog: A Prosocial Backbone for Conversational Agents**, 2022 — [[paper](https://arxiv.org/abs/2205.12688)] · core · via: AIDAS Values & Pluralism
- **Re-contextualizing Fairness in NLP: The Case of India**, 2022 — [[paper](https://arxiv.org/abs/2209.12226)] · adjacent · via: Awesome Cultural NLP
- **RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations**, 2024 — [[paper](https://aclanthology.org/2024.findings-naacl.196/)] · adjacent · via: Awesome Cultural NLP
- **SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.**, 2022 — [[paper](https://arxiv.org/abs/2210.10045)] · core · via: Alignment Goal Survey
- **SafeWorld: Geo-Diverse Safety Alignment**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes**, 2020 — [[paper](https://arxiv.org/abs/2008.09094)] · core · via: AIDAS Values & Pluralism, Awesome LLM Safety
- **Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.**, 2021 — [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396)] · core · via: Alignment Goal Survey
- **SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models**, 2023 — [[paper](https://arxiv.org/abs/2305.11840)] · adjacent · via: Awesome Cultural NLP
- **Social Chemistry 101: Learning to Reason about Social and Moral Norms**, 2020 — [[paper](https://arxiv.org/abs/2011.00620)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **SocialDial: A Benchmark for Socially-Aware Dialogue Systems**, 2023 — [[paper](https://dl.acm.org/doi/10.1145/3539618.3591877)] · adjacent · via: Awesome Cultural NLP
- **STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2505.20645)] · core · via: AIDAS Values & Pluralism
- **The Moral Foundations Reddit Corpus**, 2022 — [[paper](https://arxiv.org/abs/2208.05545)] · core · via: AIDAS Values & Pluralism, Awesome LLM Safety
- **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems**, 2022 — [[paper](https://aclanthology.org/2022.acl-long.261/)] · core · via: Pluralistic Alignment
- **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems**, 2022 — [[paper](https://arxiv.org/abs/2204.03021)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)] · core · via: Pluralistic Alignment
- **Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective**, 2026 — [[paper](https://arxiv.org/abs/2602.17283)] · core · via: AIDAS Values & Pluralism
- **VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models**, 2025 — [[paper](https://arxiv.org/abs/2510.05465)] · core · via: AIDAS Values & Pluralism
- **Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation**, 2025 — [[paper](https://aclanthology.org/2025.acl-demo.64/)] · core · via: STONIC bibliography
- **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.111/)] · core · via: Pluralistic Alignment, STONIC bibliography
- **ValueNet: A New Dataset for Human Value Driven Dialogue System**, 2022 — [[paper](https://doi.org/10.1609/aaai.v36i10.21368)] · core · via: STONIC bibliography
- **ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022**, 2022 — [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/21368)] · adjacent · via: LLM Social Science
- **Valuenet: A new dataset for human value driven dialogue system. Qiu et al. AAAI 2022.**, 2022 — [[paper](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)] · core · via: Alignment Goal Survey
- **Vision-Language Models under Cultural and Inclusive Considerations**, 2024 — [[paper](https://arxiv.org/abs/2407.06177)] · adjacent · via: Awesome Cultural NLP
- **Visually Grounded Reasoning across Languages and Cultures**, 2021 — [[paper](https://arxiv.org/abs/2109.13238)] · adjacent · via: Awesome Cultural NLP
- **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1119/)] · core · via: Pluralistic Alignment
- **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare**, 2025 — [[paper](https://arxiv.org/abs/2502.13775)] · core · via: AIDAS Values & Pluralism
- **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses**, 2026 — [[paper](https://arxiv.org/abs/2607.26348)] · core · via: AIDAS Values & Pluralism
- **Whose Opinions Do Language Models Reflect?**, 2023 — [[paper](https://arxiv.org/abs/2303.17548)] · core · via: Pluralistic Alignment
- **Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models**, 2025 — [[paper](https://arxiv.org/abs/2507.13383)] · core · via: Pluralistic Alignment
- **WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines**, 2024 — [[paper](https://arxiv.org/abs/2410.12705)] · adjacent · via: Awesome Cultural NLP
- **WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models**, 2024 — [[paper](https://aclanthology.org/2024.lrec-main.1539/)] · core · via: STONIC bibliography
- **Would you Rather? A New Benchmark for Learning Machine Alignment with Cultural Values and Social Preferences**, 2020 — [[paper](https://aclanthology.org/2020.acl-main.477/)] · adjacent · via: Awesome Cultural NLP
- **XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad**, 2026 — [[paper](https://arxiv.org/abs/2601.14063)] · core · via: AIDAS Values & Pluralism

<a id="catalog-reliability-validity-and-auditing"></a>

#### 🔬 Reliability, validity, and auditing · 17

- **A large-scale replication of scenario-based experiments in psychology and management using large language models, 2025.08, Nature Computational Science**, 2025 — [[paper](https://nature.com/articles/s43588-025-00840-7)] · core · via: LLM Psychometrics
- **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, 2025.07, ACL 2025 Best Paper**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1454/)] · core · via: LLM Psychometrics
- **A validity-guided workflow for robust large language model research in psychology**, 2025 — [[paper](https://arxiv.org/abs/2507.04491)] · core · via: LLM Psychometrics
- **Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents**, 2026 — [[paper](https://arxiv.org/abs/2602.18462)] · core · via: AIDAS Values & Pluralism
- **Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing**, 2020 — [[paper](https://doi.org/10.1145/3351095.3372873)] · core · via: STONIC bibliography
- **Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality**, 2025 — [[paper](https://arxiv.org/abs/2510.11254)] · core · via: LLM Psychometrics
- **EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations**, 2026 — [[paper](https://arxiv.org/abs/2605.30258)] · core · via: AIDAS Values & Pluralism
- **From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology**, 2025 — [[paper](https://arxiv.org/abs/2506.16697)] · core · via: LLM Psychometrics
- **Large Language Models are not Fair Evaluators**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.511/)] · core · via: STONIC bibliography
- **Large language models that replace human participants can harmfully misportray and flatten identity groups, 2025.03, Nature Machine Intelligence**, 2025 — [[paper](https://nature.com/articles/s42256-025-00986-z)] · core · via: LLM Psychometrics, LLM Social Science
- **Larger and more instructable language models become less reliable, 2024.10, Nature**, 2024 — [[paper](https://nature.com/articles/s41586-024-07930-y)] · core · via: LLM Psychometrics
- **Model Cards for Model Reporting**, 2019 — [[paper](https://doi.org/10.1145/3287560.3287596)] · core · via: STONIC bibliography
- **Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History**, 2025 — [[paper](https://arxiv.org/abs/2508.04826)] · core · via: LLM Psychometrics
- **POSIX: A Prompt Sensitivity Index For Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2410.02185)] · core · via: STONIC bibliography
- **Psychometric item validation using virtual respondents with trait-response mediators**, 2025 — [[paper](https://arxiv.org/abs/2507.05890)] · core · via: LLM Psychometrics
- **Revisiting the Reliability of Psychological Scales on Large Language Models, EMNLP 2024**, 2024 — [[paper](https://arxiv.org/abs/2305.19926)] · core · via: LLM Psychometrics
- **You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments, NAACL 2024**, 2024 — [[paper](https://arxiv.org/abs/2311.09718)] · core · via: LLM Psychometrics

<a id="catalog-choice-action-and-behavioral-consistency"></a>

#### 🎯 Choice, action, and behavioral consistency · 15

- **\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms**, 2023 — [[paper](https://arxiv.org/abs/2312.15907)] · adjacent · via: Awesome LLM Safety, LLM Social Science
- **Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents**, 2026 — [[paper](https://arxiv.org/abs/2604.27699)] · core · via: AIDAS Values & Pluralism
- **How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior**, 2024 — [[paper](https://nature.com/articles/s41562-024-01938-0.pdf)] · adjacent · via: LLM Social Science
- **How large language models can reshape collective intelligence, 2024.09, Nature Human Behavior**, 2024 — [[paper](https://nature.com/articles/s41562-024-01959-9)] · adjacent · via: LLM Social Science
- **Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations, EMNLP 2025**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.1562/)] · adjacent · via: LLM Social Science
- **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.154/)] · core · via: STONIC bibliography
- **Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies**, 2025 — [[paper](https://arxiv.org/abs/2511.05018)] · core · via: AIDAS Values & Pluralism
- **Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned**, 2022 — [[paper](https://arxiv.org/abs/2209.07858)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies**, 2026 — [[paper](https://arxiv.org/abs/2606.12369)] · core · via: AIDAS Values & Pluralism
- **Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.**, 2019 — [[paper](https://arxiv.org/abs/1911.03891)] · core · via: Alignment Goal Survey
- **The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.806/)] · core · via: STONIC bibliography
- **The theory of planned behavior**, 1991 — [[paper](https://sciencedirect.com/science/article/pii/074959789190020T)] · core · via: STONIC bibliography
- **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback**, 2022 — [[paper](https://arxiv.org/abs/2204.05862)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Training language models to follow instructions with human feedback. Ouyang et al. Neurips 2022.**, 2022 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)] · core · via: Alignment Goal Survey
- **What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios**, 2025 — [[paper](https://aclanthology.org/2025.coling-main.317/)] · core · via: STONIC bibliography

<a id="catalog-culture-language-and-pluralism"></a>

#### 🌍 Culture, language, and pluralism · 103

- **'Too much alignment; not enough culture': Re-balancing Cultural Alignment Practices in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2509.26167)] · core · via: AIDAS Values & Pluralism
- **(GlobalOpinionQA) Towards Measuring the Representation of Subjective Global Opinions in Language Models**, 2023 — [[paper](https://arxiv.org/abs/2306.16388)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey, Pluralistic Alignment, LLM Psychometrics, LLM Social Science
- **ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities**, 2026 — [[paper](https://arxiv.org/abs/2601.12962)] · core · via: AIDAS Values & Pluralism
- **An Evaluation of Cultural Value Alignment in LLM**, 2025 — [[paper](https://arxiv.org/abs/2504.08863)] · core · via: AIDAS Values & Pluralism
- **Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks**, 2025 — [[paper](https://arxiv.org/abs/2505.23820)] · core · via: AIDAS Values & Pluralism
- **Assessing Cross-Cultural Alignment between ChatGPT and Human Societies**, 2023 — [[paper](https://arxiv.org/abs/2303.17466)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Assessing LLMs for Moral Value Pluralism**, 2023 — [[paper](https://arxiv.org/abs/2312.10075)] · core · via: AIDAS Values & Pluralism
- **Attributing Culture-Conditioned Generations to Pretraining Corpora**, 2025 — [[paper](https://arxiv.org/abs/2412.20760)] · adjacent · via: Awesome Cultural NLP
- **Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs**, 2026 — [[paper](https://arxiv.org/abs/2601.15755)] · core · via: AIDAS Values & Pluralism
- **BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages**, 2024 — [[paper](https://arxiv.org/abs/2406.09948)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.2/)] · core · via: STONIC bibliography
- **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2502.08045)] · core · via: AIDAS Values & Pluralism
- **Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench**, 2025 — [[paper](https://arxiv.org/abs/2504.01127)] · core · via: AIDAS Values & Pluralism
- **CARE: Multilingual Human Preference Learning for Cultural Awareness**, 2025 — [[paper](https://arxiv.org/abs/2504.05154)] · core · via: AIDAS Values & Pluralism
- **CAReDiO: Enhancing Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization**, 2025 — [[paper](https://arxiv.org/abs/2504.08820)] · core · via: AIDAS Values & Pluralism
- **CCBench: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries**, 2026 — [[paper](https://arxiv.org/abs/2607.05405)] · core · via: AIDAS Values & Pluralism
- **CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2311.16421)] · core · via: AIDAS Values & Pluralism
- **Challenges and Strategies in Cross-Cultural NLP**, 2022 — [[paper](https://arxiv.org/abs/2203.10020)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues**, 2026 — [[paper](https://arxiv.org/abs/2603.20229)] · core · via: AIDAS Values & Pluralism
- **code and data**, 2024 — [[paper](https://arxiv.org/abs/2410.12880)] · adjacent · via: LLM Social Science
- **Coherence Maximization Improves Pluralistic Alignment**, 2026 — [[paper](https://arxiv.org/abs/2606.03110)] · core · via: AIDAS Values & Pluralism
- **Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis**, 2025 — [[paper](https://arxiv.org/abs/2511.17256)] · core · via: AIDAS Values & Pluralism
- **CulFiT: Fine-grained Cultural-aware LLM Training via Multilingual Critique Data Synthesis**, 2025 — [[paper](https://arxiv.org/abs/2505.19484)] · core · via: AIDAS Values & Pluralism
- **Cultural Adaptation in Large Language Models for Political Discourse**, 2026 — [[paper](https://arxiv.org/abs/2605.23332)] · core · via: AIDAS Values & Pluralism
- **Cultural Alignment in Large Language Models Using Soft Prompt Tuning**, 2025 — [[paper](https://arxiv.org/abs/2503.16094)] · core · via: AIDAS Values & Pluralism
- **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions**, 2023 — [[paper](https://arxiv.org/abs/2309.12342)] · core · via: AIDAS Values & Pluralism
- **Cultural bias and cultural alignment of large language models**, 2024 — [[paper](https://doi.org/10.1093/pnasnexus/pgae346)] · core · via: STONIC bibliography
- **Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting**, 2024 — [[paper](https://arxiv.org/abs/2406.11661)] · adjacent · via: Awesome Cultural NLP
- **Cultural Learning-Based Culture Adaptation of Language Models**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.156/)] · adjacent · via: Awesome Cultural NLP
- **Cultural Learning-Based Culture Adaptation of Language Models (CLCA)**, 2025 — [[paper](https://arxiv.org/abs/2504.02953)] · core · via: AIDAS Values & Pluralism
- **Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette**, 2024 — [[paper](https://arxiv.org/abs/2412.11167)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek**, 2025 — [[paper](https://arxiv.org/abs/2505.17112)] · core · via: AIDAS Values & Pluralism, STONIC bibliography, LLM Psychometrics
- **Cultural Value Alignment Via Latent Activation Steering in Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2605.26365)] · core · via: AIDAS Values & Pluralism
- **CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark**, 2024 — [[paper](https://arxiv.org/abs/2410.02677)] · core · via: AIDAS Values & Pluralism
- **Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art**, 2024 — [[paper](https://arxiv.org/abs/2406.03930)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge**, 2024 — [[paper](https://arxiv.org/abs/2404.06664)] · adjacent · via: Awesome Cultural NLP
- **Culture is Not Trivia: Sociocultural Theory for Cultural NLP**, 2025 — [[paper](https://arxiv.org/abs/2502.12057)] · core · via: AIDAS Values & Pluralism
- **CultureBank: An Online Community-Driven Knowledge Base toward Culturally Aware Language Technologies**, 2024 — [[paper](https://arxiv.org/abs/2404.15238)] · core · via: AIDAS Values & Pluralism
- **CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs**, 2026 — [[paper](https://arxiv.org/abs/2606.01879)] · core · via: AIDAS Values & Pluralism
- **CultureLLM: Incorporating Cultural Differences into Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2402.10946)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **CulturePark: Boosting Cross-cultural Understanding in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2405.15145)] · core · via: AIDAS Values & Pluralism
- **CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis**, 2025 — [[paper](https://arxiv.org/abs/2509.10886)] · core · via: AIDAS Values & Pluralism
- **CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters**, 2026 — [[paper](https://arxiv.org/abs/2601.04885)] · core · via: AIDAS Values & Pluralism
- **CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2511.12014)] · core · via: AIDAS Values & Pluralism
- **Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions**, 2025 — [[paper](https://arxiv.org/abs/2510.21977)] · core · via: AIDAS Values & Pluralism
- **Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook**, 2026 — [[paper](https://arxiv.org/abs/2604.06210)] · core · via: AIDAS Values & Pluralism
- **DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained LMs**, 2023 — [[paper](https://arxiv.org/abs/2306.05076)] · core · via: AIDAS Values & Pluralism
- **EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms**, 2025 — [[paper](https://arxiv.org/abs/2507.20264)] · core · via: AIDAS Values & Pluralism
- **Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in**, 2024 — [[paper](https://arxiv.org/abs/2404.18460)] · core · via: STONIC bibliography
- **EtiCor: Corpus for Analyzing LLMs for Etiquettes**, 2023 — [[paper](https://arxiv.org/abs/2310.18974)] · core · via: AIDAS Values & Pluralism
- **Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment**, 2025 — [[paper](https://arxiv.org/abs/2509.21798)] · core · via: AIDAS Values & Pluralism
- **Evaluating Pluralism in LLMs through Latent Perspectives**, 2026 — [[paper](https://arxiv.org/abs/2606.13254)] · core · via: AIDAS Values & Pluralism
- **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment**, 2025 — [[paper](https://arxiv.org/abs/2510.04045)] · core · via: AIDAS Values & Pluralism
- **Exploring Cultural Variations in Moral Judgments with Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2506.12433)] · core · via: AIDAS Values & Pluralism
- **Extrinsic Evaluation of Cultural Competence in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2406.11565)] · adjacent · via: Awesome Cultural NLP
- **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment**, 2024 — [[paper](https://arxiv.org/abs/2406.17692)] · core · via: AIDAS Values & Pluralism
- **From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2505.16408)] · core · via: AIDAS Values & Pluralism
- **Having Beer after Prayer? Measuring Cultural Bias in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2305.14456)] · adjacent · via: Awesome Cultural NLP
- **Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens**, 2025 — [[paper](https://arxiv.org/abs/2510.05931)] · core · via: AIDAS Values & Pluralism
- **How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective**, 2025 — [[paper](https://arxiv.org/abs/2502.17773)] · core · via: AIDAS Values & Pluralism
- **How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions**, 2024 — [[paper](https://arxiv.org/abs/2406.14805)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Improving Cross-Cultural Survey Simulation with Calibrated Value Personas**, 2026 — [[paper](https://arxiv.org/abs/2605.16193)] · core · via: AIDAS Values & Pluralism
- **Investigating Cultural Alignment of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2402.13231)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions**, 2025 — [[paper](https://arxiv.org/abs/2502.16761)] · core · via: AIDAS Values & Pluralism
- **Large Language Models as Superpositions of Cultural Perspectives**, 2023 — [[paper](https://arxiv.org/abs/2307.07870)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Legal Theory for Pluralistic Alignment**, 2024 — [[paper](https://arxiv.org/abs/2410.17271)] · adjacent · via: LLM Social Science
- **Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation**, 2026 — [[paper](https://arxiv.org/abs/2604.08797)] · core · via: AIDAS Values & Pluralism
- **LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?**, 2025 — [[paper](https://arxiv.org/abs/2503.15003)] · core · via: AIDAS Values & Pluralism
- **LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output**, 2024 — [[paper](https://arxiv.org/abs/2411.06032)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Made-in China, Thinking in America: U.S. Values Persist in Chinese LLMs**, 2025 — [[paper](https://arxiv.org/abs/2512.13723)] · core · via: AIDAS Values & Pluralism
- **Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness**, 2025 — [[paper](https://arxiv.org/abs/2502.09637)] · core · via: AIDAS Values & Pluralism
- **Meta-Learning Preferences for Multilingual LLM Alignment**, 2026 — [[paper](https://arxiv.org/abs/2607.13315)] · core · via: AIDAS Values & Pluralism
- **Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2602.22475)] · core · via: AIDAS Values & Pluralism
- **Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate**, 2026 — [[paper](https://arxiv.org/abs/2601.12091)] · core · via: AIDAS Values & Pluralism
- **Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2502.16534)] · core · via: AIDAS Values & Pluralism
- **Multilingual Language Models are not Multicultural: A Case Study in Emotion**, 2023 — [[paper](https://arxiv.org/abs/2307.01370)] · adjacent · via: Awesome Cultural NLP
- **NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities**, 2025 — [[paper](https://arxiv.org/abs/2505.18383)] · core · via: AIDAS Values & Pluralism
- **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2404.12464)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP, LLM Social Science
- **On the steerability of large language models toward data-driven personas**, 2023 — [[paper](https://arxiv.org/abs/2311.04978)] · core · via: AIDAS Values & Pluralism
- **Overton Pluralistic Reinforcement Learning for Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2602.20759)] · core · via: AIDAS Values & Pluralism
- **Pluralistic Alignment for Healthcare: A Role-Driven Framework**, 2025 — [[paper](https://arxiv.org/abs/2509.10685)] · core · via: AIDAS Values & Pluralism
- **Plurals: A System for Guiding LLMs Via Simulated Social Ensembles**, 2024 — [[paper](https://arxiv.org/abs/2409.17213)] · core · via: AIDAS Values & Pluralism
- **POW: Political Overton Windows of Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2509.08853)] · core · via: AIDAS Values & Pluralism
- **Probing Pre-Trained Language Models for Cross-Cultural Differences in Values**, 2022 — [[paper](https://arxiv.org/abs/2203.13722)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome Cultural NLP
- **Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble**, 2025 — [[paper](https://arxiv.org/abs/2509.11311)] · core · via: AIDAS Values & Pluralism
- **Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2503.08688)] · core · via: AIDAS Values & Pluralism
- **RLHF: A Comprehensive Survey for Cultural, Multimodal and Low-Latency Alignment Methods**, 2025 — [[paper](https://arxiv.org/abs/2511.03939)] · core · via: AIDAS Values & Pluralism
- **Self-Pluralising Culture Alignment for Large Language Models (CultureSPA)**, 2024 — [[paper](https://arxiv.org/abs/2410.12971)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations**, 2025 — [[paper](https://arxiv.org/abs/2502.07068)] · core · via: AIDAS Values & Pluralism
- **Steerable Cultural Preference Optimization of Reward Models**, 2026 — [[paper](https://arxiv.org/abs/2606.18606)] · core · via: AIDAS Values & Pluralism
- **Steering LLMs for Culturally Localized Generation**, 2026 — [[paper](https://arxiv.org/abs/2603.23301)] · core · via: AIDAS Values & Pluralism
- **Survey of Cultural Awareness in Language Models: Text and Beyond**, 2024 — [[paper](https://arxiv.org/abs/2411.00860)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP, LLM Social Science
- **The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning**, 2024 — [[paper](https://arxiv.org/abs/2405.12744)] · adjacent · via: Awesome Cultural NLP
- **The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2604.20225)] · core · via: AIDAS Values & Pluralism
- **Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning**, 2026 — [[paper](https://arxiv.org/abs/2601.21700)] · core · via: AIDAS Values & Pluralism
- **Toward Culturally Grounded Natural Language Processing**, 2026 — [[paper](https://arxiv.org/abs/2603.26013)] · core · via: AIDAS Values & Pluralism
- **Towards Measuring and Modeling "Culture" in LLMs: A Survey**, 2024 — [[paper](https://arxiv.org/abs/2403.15412)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation**, 2025 — [[paper](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)] · core · via: AIDAS Values & Pluralism
- **Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements**, 2026 — [[paper](https://arxiv.org/abs/2602.12878)] · core · via: AIDAS Values & Pluralism
- **Value kaleidoscope: engaging AI with pluralistic human values, rights, and duties**, 2024 — [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] · core · via: STONIC bibliography
- **Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise**, 2025 — [[paper](https://arxiv.org/abs/2506.00242)] · core · via: AIDAS Values & Pluralism
- **WorldValuesBench: A Large-Scale Benchmark for Multi-Cultural Value Awareness of Language Models**, 2024 — [[paper](https://arxiv.org/abs/2404.16308)] · core · via: AIDAS Values & Pluralism
- **XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity**, 2026 — [[paper](https://arxiv.org/abs/2605.05662)] · core · via: AIDAS Values & Pluralism

<a id="catalog-preferences-opinions-and-social-simulation"></a>

#### 🗣️ Preferences, opinions, and social simulation · 120

- **(ANES) CommunityLM: Probing Partisan Worldviews from Language Models, COLING 2022**, 2022 — [[paper](https://arxiv.org/abs/2209.07065)] · core · via: LLM Psychometrics
- **(ANES) Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information**, 2024 — [[paper](https://arxiv.org/abs/2402.18144)] · core · via: LLM Psychometrics
- **(ANES) Representation Bias in Political Sample Simulations with Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2407.11409)] · core · via: LLM Psychometrics
- **(ANES) Unpacking Political Bias in Large Language Models: A Cross-Model Comparison on U.S. Politics**, 2024 — [[paper](https://arxiv.org/abs/2412.16746)] · core · via: LLM Psychometrics
- **(Culture) Cultural tendencies in generative AI, 2025.06, Nature Human Behaviour**, 2025 — [[paper](https://nature.com/articles/s41562-025-02242-1)] · core · via: LLM Psychometrics
- **(GLES) Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study**, 2024 — [[paper](https://arxiv.org/abs/2412.13169)] · core · via: LLM Psychometrics
- **(GLES) Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction**, 2025 — [[paper](https://arxiv.org/abs/2502.16280)] · core · via: LLM Psychometrics
- **(GLES) Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion**, 2024 — [[paper](https://arxiv.org/abs/2407.08563)] · core · via: LLM Psychometrics
- **(Others & custom) AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction**, 2023 — [[paper](https://arxiv.org/abs/2305.09620)] · core · via: LLM Psychometrics
- **(Others & custom) Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys**, 2024 — [[paper](https://arxiv.org/abs/2405.19323)] · core · via: LLM Psychometrics
- **(Others & custom) Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2503.13149)] · core · via: LLM Psychometrics
- **(Others & custom) Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases**, 2025 — [[paper](https://arxiv.org/abs/2502.18282)] · core · via: LLM Psychometrics
- **(Others & custom) Demonstrations of the Potential of AI-based Political Issue Polling, 2023.07, Harvard Data Science Review (HDSR)**, 2023 — [[paper](https://arxiv.org/abs/2307.04781)] · core · via: LLM Psychometrics
- **(Others & custom) From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models, ACL 2023**, 2023 — [[paper](https://arxiv.org/abs/2305.08283)] · core · via: LLM Psychometrics
- **(Others & custom) How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?, 2023.07, Digital Society**, 2023 — [[paper](https://link.springer.com/article/10.1007/s44206-023-00054-2)] · core · via: LLM Psychometrics
- **(Others & custom) IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance**, 2025 — [[paper](https://arxiv.org/abs/2502.08395)] · core · via: LLM Psychometrics
- **(Others & custom) Large Language Models Can Be Used to Estimate the Latent Positions of Politicians**, 2023 — [[paper](https://arxiv.org/abs/2303.12057)] · core · via: LLM Psychometrics
- **(Others & custom) Linear Representations of Political Perspective Emerge in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2503.02080)] · core · via: LLM Psychometrics
- **(Others & custom) Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs, NAACL 2024 (Short Paper)**, 2024 — [[paper](https://arxiv.org/abs/2403.13592)] · core · via: LLM Psychometrics
- **(Others & custom) Questioning the Survey Responses of Large Language Models, NeurIPS 2024**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)] · core · via: LLM Psychometrics
- **(PCT) Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas**, 2024 — [[paper](https://arxiv.org/abs/2412.14843)] · core · via: LLM Psychometrics
- **(PCT) Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias, arXiv 2026.01**, 2026 — [[paper](https://arxiv.org/abs/2601.06194)] · core · via: LLM Psychometrics
- **(PCT) Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models, ACL 2024**, 2024 — [[paper](https://arxiv.org/abs/2402.16786)] · core · via: LLM Psychometrics, LLM Social Science
- **(PCT) PRISM: A Methodology for Auditing Biases in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2410.18906)] · core · via: LLM Psychometrics
- **(PCT) Revealing Fine-Grained Values and Opinions in Large Language Models, EMNLP 2024 Findings**, 2024 — [[paper](https://arxiv.org/abs/2406.19238)] · core · via: LLM Psychometrics
- **(PCT) The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation**, 2023 — [[paper](https://arxiv.org/abs/2301.01768)] · core · via: LLM Psychometrics
- **(PCT) The Self-Perception and Political Biases of ChatGPT**, 2024 — [[paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)] · core · via: LLM Psychometrics
- **A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations**, 2025 — [[paper](https://arxiv.org/abs/2505.14106)] · adjacent · via: Personalized Alignment
- **AI PERSONA: Towards Life-long Personalization of LLMs**, 2024 — [[paper](https://arxiv.org/abs/2412.13103)] · adjacent · via: Personalized Alignment
- **Aligning Language Models from User Interactions**, 2026 — [[paper](https://arxiv.org/abs/2603.12273)] · adjacent · via: Personalized Alignment
- **Aligning Large Language Models with Diverse Political Viewpoints**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-main.412/)] · core · via: STONIC bibliography
- **Aligning LLMs with Individual Preferences via Interaction**, 2024 — [[paper](https://arxiv.org/abs/2410.03642)] · adjacent · via: Personalized Alignment
- **Aligning to Thousands of Preferences via System Message Generalization**, 2024 — [[paper](https://arxiv.org/abs/2405.17977)] · adjacent · via: Personalized Alignment
- **Aligning VLM Assistants with Personalized Situated Cognition**, 2025 — [[paper](https://arxiv.org/abs/2506.00930)] · adjacent · via: Personalized Alignment
- **AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment**, 2026 — [[paper](https://arxiv.org/abs/2603.26680)] · adjacent · via: Personalized Alignment
- **Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs**, 2025 — [[paper](https://arxiv.org/abs/2502.19148)] · adjacent · via: Personalized Alignment
- **APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings**, 2026 — [[paper](https://arxiv.org/abs/2605.21063)] · adjacent · via: Personalized Alignment
- **APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents**, 2026 — [[paper](https://arxiv.org/abs/2605.27419)] · core · via: AIDAS Values & Pluralism
- **BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization**, 2024 — [[paper](https://aclanthology.org/2024.findings-emnlp.398/)] · adjacent · via: Personalized Alignment
- **Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization**, 2026 — [[paper](https://arxiv.org/abs/2606.02300)] · adjacent · via: Personalized Alignment
- **COMPO: Community Preferences for Language Model Personalization**, 2024 — [[paper](https://arxiv.org/abs/2410.16027)] · adjacent · via: Personalized Alignment, LLM Social Science
- **Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements**, 2024 — [[paper](https://arxiv.org/abs/2410.08968)] · adjacent · via: Personalized Alignment
- **CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors**, 2026 — [[paper](https://arxiv.org/abs/2604.14773)] · adjacent · via: Personalized Alignment
- **CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering**, 2025 — [[paper](https://arxiv.org/abs/2507.04756)] · adjacent · via: Personalized Alignment
- **Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling**, 2026 — [[paper](https://arxiv.org/abs/2607.18310)] · core · via: AIDAS Values & Pluralism
- **Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2309.03126)] · adjacent · via: Personalized Alignment
- **Drift: Decoding-time Personalized Alignments with Implicit User Preferences**, 2025 — [[paper](https://arxiv.org/abs/2502.14289)] · adjacent · via: Personalized Alignment
- **EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents**, 2026 — [[paper](https://arxiv.org/abs/2606.26883)] · core · via: AIDAS Values & Pluralism
- **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance**, 2025 — [[paper](https://arxiv.org/abs/2505.16348)] · adjacent · via: Personalized Alignment
- **EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?**, 2025 — [[paper](https://arxiv.org/abs/2503.16545)] · adjacent · via: Personalized Alignment
- **Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1**, 2026 — [[paper](https://arxiv.org/abs/2607.20589)] · core · via: AIDAS Values & Pluralism
- **Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals**, 2025 — [[paper](https://arxiv.org/abs/2505.18071)] · adjacent · via: Personalized Alignment
- **Few-shot Personalization of LLMs with Mis-aligned Responses**, 2024 — [[paper](https://arxiv.org/abs/2406.18678)] · adjacent · via: Personalized Alignment
- **From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment**, 2025 — [[paper](https://arxiv.org/abs/2503.15463)] · adjacent · via: Personalized Alignment
- **From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning**, 2026 — [[paper](https://arxiv.org/abs/2605.23382)] · adjacent · via: Personalized Alignment
- **From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes**, 2026 — [[paper](https://arxiv.org/abs/2605.16303)] · core · via: AIDAS Values & Pluralism
- **From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users**, 2026 — [[paper](https://arxiv.org/abs/2606.00728)] · adjacent · via: Personalized Alignment
- **From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment**, 2025 — [[paper](https://arxiv.org/abs/2505.16610)] · adjacent · via: Personalized Alignment
- **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents**, 2026 — [[paper](https://arxiv.org/abs/2604.20006)] · adjacent · via: Personalized Alignment
- **From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG**, 2026 — [[paper](https://arxiv.org/abs/2605.18271)] · adjacent · via: Personalized Alignment
- **Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation**, 2026 — [[paper](https://arxiv.org/abs/2605.24647)] · adjacent · via: Personalized Alignment
- **Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users**, 2026 — [[paper](https://arxiv.org/abs/2603.16120)] · adjacent · via: Personalized Alignment
- **Large Language Models Empowered Personalized Web Agents**, 2024 — [[paper](https://arxiv.org/abs/2410.17236)] · adjacent · via: Personalized Alignment
- **Learning to summarize user information for personalized reinforcement learning from human feedback**, 2026 — [[paper](https://openreview.net/forum?id=Ar078WR3um)] · adjacent · via: Personalized Alignment
- **LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education**, 2024 — [[paper](https://arxiv.org/abs/2410.14012)] · adjacent · via: Personalized Alignment
- **MAP: Multi-Human-Value Alignment Palette**, 2024 — [[paper](https://openreview.net/forum?id=NN6QHwgRrQ)] · adjacent · via: Personalized Alignment
- **MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2605.25342)] · adjacent · via: Personalized Alignment
- **MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time**, 2024 — [[paper](https://arxiv.org/abs/2410.14184)] · adjacent · via: Personalized Alignment
- **MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning**, 2025 — [[paper](https://arxiv.org/abs/2505.24846)] · adjacent · via: Personalized Alignment
- **More human than human: measuring ChatGPT political bias**, 2023 — [[paper](https://link.springer.com/article/10.1007/s11127-023-01097-2)] · adjacent · via: LLM Social Science
- **NextQuill: Causal Preference Modeling for Enhancing LLM Personalization**, 2026 — [[paper](https://openreview.net/forum?id=xYpVlKMFqv)] · adjacent · via: Personalized Alignment
- **Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL 2025**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1529/)] · adjacent · via: LLM Social Science
- **Opinion dynamics and mutual influence with LLM agents through dialog simulation**, 2026 — [[paper](https://arxiv.org/abs/2602.12583)] · core · via: AIDAS Values & Pluralism
- **P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling**, 2026 — [[paper](https://openreview.net/forum?id=hXNApWLBZG)] · adjacent · via: Personalized Alignment
- **PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment**, 2024 — [[paper](https://openreview.net/forum?id=1kFDrYCuSu)] · adjacent · via: Personalized Alignment
- **PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents**, 2026 — [[paper](https://arxiv.org/abs/2608.04003)] · adjacent · via: Personalized Alignment
- **Persona-Based Simulation of Human Opinion at Population Scale**, 2026 — [[paper](https://arxiv.org/abs/2603.27056)] · core · via: AIDAS Values & Pluralism
- **Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement**, 2024 — [[paper](https://arxiv.org/abs/2402.11060)] · adjacent · via: Personalized Alignment
- **Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment**, 2025 — [[paper](https://arxiv.org/abs/2504.12663)] · adjacent · via: Personalized Alignment
- **PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time**, 2025 — [[paper](https://arxiv.org/abs/2506.06254)] · adjacent · via: Personalized Alignment
- **PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization**, 2025 — [[paper](https://arxiv.org/abs/2506.12915)] · adjacent · via: Personalized Alignment
- **PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants**, 2025 — [[paper](https://arxiv.org/abs/2506.09902)] · adjacent · via: Personalized Alignment
- **Personalized Adaptation via In-Context Preference Learning**, 2024 — [[paper](https://arxiv.org/abs/2410.14001)] · adjacent · via: Personalized Alignment
- **Personalized Benchmarking: Evaluating LLMs by Individual Preferences**, 2026 — [[paper](https://arxiv.org/abs/2604.18943)] · adjacent · via: Personalized Alignment
- **Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment**, 2026 — [[paper](https://arxiv.org/abs/2603.10009)] · adjacent · via: Personalized Alignment
- **Personalized Language Modeling from Personalized Human Feedback**, 2024 — [[paper](https://arxiv.org/abs/2402.05133)] · adjacent · via: Personalized Alignment
- **Personalized LLM Decoding via Contrasting Personal Preference**, 2025 — [[paper](https://arxiv.org/abs/2506.12109)] · adjacent · via: Personalized Alignment
- **Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It**, 2026 — [[paper](https://openreview.net/forum?id=O1hfVE0UxG)] · adjacent · via: Personalized Alignment
- **Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization**, 2026 — [[paper](https://arxiv.org/abs/2604.07343)] · adjacent · via: Personalized Alignment
- **Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging**, 2023 — [[paper](https://arxiv.org/abs/2310.11564)] · adjacent · via: Personalized Alignment
- **Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning**, 2024 — [[paper](https://arxiv.org/abs/2408.10075)] · adjacent · via: Personalized Alignment
- **PersonalLLM: Tailoring LLMs to Individual Preferences**, 2024 — [[paper](https://arxiv.org/abs/2409.20296)] · adjacent · via: Personalized Alignment
- **PersonaVLM: Long-Term Personalized Multimodal LLMs**, 2026 — [[paper](https://arxiv.org/abs/2604.13074)] · adjacent · via: Personalized Alignment
- **PEToolLLM: Towards Personalized Tool Learning in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2502.18980)] · adjacent · via: Personalized Alignment
- **Political-LLM: Large Language Models in Political Science**, 2024 — [[paper](https://arxiv.org/abs/2412.06864)] · adjacent · via: LLM Social Science
- **POPI: Personalizing LLMs via Optimized Natural Language Preference Inference**, 2025 — [[paper](https://arxiv.org/abs/2510.17881)] · adjacent · via: Personalized Alignment
- **Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization**, 2026 — [[paper](https://arxiv.org/abs/2604.22345)] · adjacent · via: Personalized Alignment
- **Preference-Aware Rubric Learning for Personalized Evaluation**, 2026 — [[paper](https://arxiv.org/abs/2605.31545)] · adjacent · via: Personalized Alignment
- **PrefPalette: Personalized Preference Modeling with Latent Attributes**, 2025 — [[paper](https://arxiv.org/abs/2507.13541)] · adjacent · via: Personalized Alignment
- **PRIME: Large Language Model Personalization with Cognitive Memory and Thought Processes**, 2025 — [[paper](https://arxiv.org/abs/2507.04607)] · adjacent · via: Personalized Alignment
- **Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation**, 2025 — [[paper](https://arxiv.org/abs/2505.17571)] · adjacent · via: Personalized Alignment
- **RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation**, 2024 — [[paper](https://arxiv.org/abs/2405.00254)] · adjacent · via: Personalized Alignment
- **Show, Don't Tell: Aligning Language Models with Demonstrated Feedback**, 2024 — [[paper](https://arxiv.org/abs/2406.00888)] · adjacent · via: Personalized Alignment
- **Silicon Sampling via Cross-Survey Transfer**, 2026 — [[paper](https://arxiv.org/abs/2607.03091)] · core · via: AIDAS Values & Pluralism
- **Steering Large Language Models for Machine Translation Personalization**, 2025 — [[paper](https://arxiv.org/abs/2505.16612)] · adjacent · via: Personalized Alignment
- **Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback**, 2026 — [[paper](https://openreview.net/forum?id=nc28mSbyVG)] · adjacent · via: Personalized Alignment
- **SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2506.05598)] · adjacent · via: Personalized Alignment
- **Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment**, 2025 — [[paper](https://arxiv.org/abs/2505.15456)] · adjacent · via: Personalized Alignment
- **Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures**, 2026 — [[paper](https://arxiv.org/abs/2605.10991)] · adjacent · via: Personalized Alignment
- **The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads**, 2026 — [[paper](https://arxiv.org/abs/2608.04570)] · adjacent · via: Personalized Alignment
- **The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2406.11096)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2404.16019)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP, Personalized Alignment, LLM Social Science
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[paper](https://openreview.net/forum?id=DFr5hteojx)] · adjacent · via: Personalized Alignment
- **Think-While-Generating: On-the-Fly Reasoning for Personalized Long-Form Generation**, 2026 — [[paper](https://openreview.net/forum?id=lle0aGQyQb)] · adjacent · via: Personalized Alignment
- **Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning**, 2025 — [[paper](https://arxiv.org/abs/2503.07018)] · adjacent · via: Personalized Alignment
- **Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning**, 2025 — [[paper](https://arxiv.org/abs/2510.18849)] · adjacent · via: Personalized Alignment
- **TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment**, 2026 — [[paper](https://arxiv.org/abs/2606.01755)] · adjacent · via: Personalized Alignment
- **What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data**, 2026 — [[paper](https://openreview.net/forum?id=sC6A1bFDUt)] · adjacent · via: Personalized Alignment
- **When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation**, 2025 — [[paper](https://arxiv.org/abs/2505.24613)] · adjacent · via: Personalized Alignment
- **When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning**, 2025 — [[paper](https://arxiv.org/abs/2502.19158)] · adjacent · via: Personalized Alignment

<a id="catalog-moral-reasoning-and-value-understanding"></a>

#### ⚖️ Moral reasoning and value understanding · 63

- **(DIT) Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test**, 2024 — [[paper](https://arxiv.org/abs/2402.02135)] · core · via: LLM Psychometrics
- **(DIT) Probing the Moral Development of Large Language Models through Defining Issues Test**, 2023 — [[paper](https://arxiv.org/abs/2309.13356)] · core · via: Awesome LLM Safety, LLM Psychometrics
- **(ETHICS) An Evaluation of GPT-4 on the ETHICS Dataset**, 2023 — [[paper](https://arxiv.org/abs/2309.10492)] · core · via: LLM Psychometrics
- **(ETHICS) Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety, NeurIPS 2022 Workshop**, 2022 — [[paper](https://arxiv.org/abs/2212.06295)] · core · via: LLM Psychometrics
- **(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023**, 2023 — [[paper](https://dl.acm.org/doi/abs/10.1145/3624918.3625327)] · core · via: LLM Psychometrics
- **(ETHICS) Inducing Human-like Biases in Moral Reasoning Language Models**, 2024 — [[paper](https://arxiv.org/abs/2411.15386)] · core · via: LLM Psychometrics
- **(MFT) Analyzing the Ethical Logic of Six Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2501.08951)] · core · via: LLM Psychometrics
- **(MFT) Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations, AIES 2024**, 2024 — [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31704)] · core · via: LLM Psychometrics
- **(MFT) Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy, NAACL 2022 Workshop**, 2022 — [[paper](https://arxiv.org/abs/2205.12771)] · core · via: LLM Psychometrics
- **(MFT) Exploring and steering the moral compass of Large Language Models, ICPR 2024**, 2024 — [[paper](https://arxiv.org/abs/2405.17345)] · core · via: LLM Psychometrics
- **(MFT) M3oralBench: A MultiModal Moral Benchmark for LVLMs**, 2024 — [[paper](https://arxiv.org/abs/2412.20718)] · core · via: LLM Psychometrics
- **(MFT) Moral Foundations of Large Language Models, EMNLP 2024**, 2024 — [[paper](https://arxiv.org/abs/2310.15337)] · core · via: LLM Psychometrics, LLM Social Science
- **(MFT) Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity, ACL 2023 Workshop**, 2023 — [[paper](https://arxiv.org/abs/2209.12106)] · core · via: Alignment Goal Survey, LLM Psychometrics, LLM Social Science
- **(MFT) MoralBench: Moral Evaluation of LLMs**, 2024 — [[paper](https://arxiv.org/abs/2406.04428)] · core · via: LLM Psychometrics
- **(MFT) Towards "Differential AI Psychology" and in-context Value-driven Statement Alignment with Moral Foundations Theory**, 2024 — [[paper](https://arxiv.org/abs/2408.11415)] · core · via: LLM Psychometrics
- **(MFT) Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models**, 2024 — [[paper](https://arxiv.org/abs/2412.18863)] · core · via: LLM Psychometrics
- **(Others & Custom) Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, 2025.07, ACL 2025 Best Resource Paper**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.294/)] · core · via: LLM Psychometrics
- **(Others & Custom) Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment, AIES 2024**, 2024 — [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31741)] · core · via: LLM Psychometrics
- **(Others & Custom) Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?, C3NLP 2024**, 2024 — [[paper](https://arxiv.org/abs/2406.16316)] · core · via: LLM Psychometrics
- **(Others & Custom) Evaluating Moral Beliefs across LLMs through a Pluralistic Framework**, 2024 — [[paper](https://arxiv.org/abs/2411.03665)] · core · via: LLM Psychometrics
- **(Others & Custom) Evaluating the Moral Beliefs Encoded in LLMs, NeurIPS 2023**, 2023 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)] · core · via: LLM Psychometrics
- **(Others & Custom) Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper)**, 2024 — [[paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)] · core · via: LLM Psychometrics
- **(Others & Custom) Knowledge of cultural moral norms in large language models, ACL 2023**, 2023 — [[paper](https://arxiv.org/abs/2306.01857)] · core · via: Awesome Cultural NLP, LLM Psychometrics
- **(Others & Custom) Large-scale moral machine experiment on large language models**, 2024 — [[paper](https://arxiv.org/abs/2411.06790)] · core · via: LLM Psychometrics
- **(Others & Custom) LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics**, 2024 — [[paper](https://arxiv.org/abs/2412.00962)] · core · via: LLM Psychometrics
- **(Others & Custom) Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment**, 2024 — [[paper](https://arxiv.org/abs/2411.11731)] · core · via: LLM Psychometrics
- **(Others & Custom) Normative Evaluation of Large Language Models with Everyday Moral Dilemmas**, 2025 — [[paper](https://arxiv.org/abs/2501.18081)] · core · via: LLM Psychometrics, LLM Social Science
- **(Others & Custom) Potential benefits of employing large language models in research in moral education and development, 2023.01, Journal of Moral Education**, 2023 — [[paper](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)] · core · via: LLM Psychometrics
- **(Others & Custom) Right vs. Right: Can LLMs Make Tough Choices?**, 2024 — [[paper](https://arxiv.org/abs/2412.19926)] · core · via: LLM Psychometrics
- **(Others & Custom) SaGE: Evaluating Moral Consistency in Large Language Models, LREC-COLING 2024**, 2024 — [[paper](https://arxiv.org/abs/2402.13709)] · core · via: LLM Psychometrics
- **(Others & Custom) The Moral Mind(s) of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2412.04476)] · core · via: LLM Psychometrics
- **(Others & Custom) The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making**, 2024 — [[paper](https://arxiv.org/abs/2410.07304)] · core · via: LLM Psychometrics
- **(Others & Custom) Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2311.07792)] · core · via: LLM Psychometrics
- **(Others & Custom) What does AI consider praiseworthy?, 2025.02, AI and Ethics**, 2025 — [[paper](https://link.springer.com/article/10.1007/s43681-025-00682-z)] · core · via: LLM Psychometrics
- **(Others & Custom) When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment, NeurIPS 2022**, 2022 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)] · core · via: LLM Psychometrics
- **Aditi Khandelwal et al. EACL 2024.**, 2024 — [[paper](https://aclanthology.org/2024.eacl-long.176/)] · adjacent · via: Awesome LLM Safety
- **Agent Alignment in Evolving Social Norms**, 2024 — [[paper](https://arxiv.org/abs/2401.04620)] · adjacent · via: LLM Social Science
- **Can Machines Learn Morality? The Delphi Experiment**, 2021 — [[paper](https://arxiv.org/abs/2110.07574)] · core · via: Alignment Goal Survey, STONIC bibliography
- **CrowS-Pairs**, 2020 — [[paper](https://aclanthology.org/2020.emnlp-main.154/)] · adjacent · via: Awesome LLM Datasets
- **DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life**, 2024 — [[paper](https://arxiv.org/abs/2410.02683)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Psychometrics
- **Exploring the psychology of GPT-4's Moral and Legal Reasoning**, 2023 — [[paper](https://arxiv.org/abs/2308.01264)] · adjacent · via: LLM Social Science
- **How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main**, 2026 — [[paper](https://arxiv.org/abs/2603.13876)] · adjacent · via: LLM Social Science
- **Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence**, 2025 — [[paper](https://nature.com/articles/s42256-024-00969-6)] · adjacent · via: LLM Social Science
- **Irene Solaiman and Christy Dennison. NeurIPS 2021.**, 2021 — [[paper](https://arxiv.org/abs/2106.10328)] · adjacent · via: Awesome LLM Safety
- **Joshua Landau et al. arXiv 2023.**, 2023 — [[paper](https://arxiv.org/abs/2302.07459)] · adjacent · via: Awesome LLM Safety
- **Laura Weidinger et al. arXiv 2021.**, 2021 — [[paper](https://arxiv.org/abs/2112.04359)] · adjacent · via: Awesome LLM Safety
- **Learning norms from stories: A prior for value aligned agents. Nahian et al. AIES 2020.**, 2020 — [[paper](https://arxiv.org/abs/1912.03553)] · core · via: Alignment Goal Survey
- **Moral Foundations of Large Language Models**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-main.982/)] · core · via: STONIC bibliography
- **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences**, 2021 — [[paper](https://aclanthology.org/2021.emnlp-main.54/)] · core · via: STONIC bibliography
- **MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.**, 2023 — [[paper](https://arxiv.org/abs/2212.10720)] · core · via: Alignment Goal Survey
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.**, 2023 — [[paper](https://arxiv.org/abs/2305.03047)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **Revealing the Pragmatic Dilemma for Moral Reasoning Acquisition in Language Models**, 2025 — [[paper](https://arxiv.org/abs/2502.16600)] · adjacent · via: LLM Social Science
- **Safety Assessment of Chinese Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2304.10436)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **SafetyBench 2023-9**, 2023 — [[paper](https://arxiv.org/abs/2309.07045)] · adjacent · via: Awesome LLM Datasets
- **Shamik Roy et al. arXiv 2023.**, 2023 — [[paper](https://aclanthology.org/2022.nlpcss-1.20/)] · adjacent · via: Awesome LLM Safety
- **Shitong Duan et al. ICLR 2024.**, 2024 — [[paper](https://openreview.net/forum?id=m3RRWWFaVe)] · adjacent · via: Awesome LLM Safety
- **Social Chemistry 101: Learning to Reason about Social and Moral Norms**, 2020 — [[paper](https://aclanthology.org/2020.emnlp-main.48/)] · core · via: STONIC bibliography
- **Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.1541/)] · core · via: STONIC bibliography
- **TRUSTGPT 2023-6**, 2023 — [[paper](https://arxiv.org/abs/2306.11507)] · adjacent · via: Awesome LLM Datasets
- **Utkarsh Agarwal et al. LREC/COLING 2024.**, 2024 — [[paper](https://aclanthology.org/2024.lrec-main.560/)] · adjacent · via: Awesome LLM Safety
- **When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.**, 2022 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf)] · core · via: Alignment Goal Survey
- **Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)**, 2026 — [[paper](https://arxiv.org/abs/2509.17703)] · adjacent · via: LLM Social Science
- **Xi Zhiheng et al. CCL 2023.**, 2023 — [[paper](https://aclanthology.org/2023.ccl-4.2/)] · adjacent · via: Awesome LLM Safety

<a id="catalog-alignment-steering-and-preferences"></a>

#### 🧰 Alignment, steering, and preferences · 133

- **\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2312.12999)] · adjacent · via: LLM Social Science
- **A general language assistant as a laboratory for alignment. Askell et al. arXiv 2021.**, 2021 — [[paper](https://arxiv.org/abs/2112.00861)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **A Roadmap to Pluralistic Alignment**, 2024 — [[paper](https://arxiv.org/abs/2402.05070)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy**, 2026 — [[paper](https://arxiv.org/abs/2605.01642)] · core · via: AIDAS Values & Pluralism
- **AI Alignment Breaks at the Edge**, 2026 — [[paper](https://arxiv.org/abs/2602.20042)] · core · via: AIDAS Values & Pluralism
- **Aligning \AI\ With Shared Human Values**, 2021 — [[paper](https://openreview.net/forum?id=dNy_RKzJacY)] · core · via: STONIC bibliography
- **Aligning Crowd Feedback via Distributional Preference Reward Modeling**, 2024 — [[paper](https://arxiv.org/abs/2402.09764)] · core · via: Pluralistic Alignment
- **Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning**, 2023 — [[paper](https://arxiv.org/abs/2311.08385)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping**, 2026 — [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41109)] · core · via: Pluralistic Alignment
- **Aligning Multimodal LLM with Human Preference: A Survey**, 2025 — [[paper](https://arxiv.org/abs/2503.14504)] · core · via: Pluralistic Alignment
- **Aligning to Thousands of Preferences via System Message Generalization**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective**, 2025 — [[paper](https://aclanthology.org/2025.findings-acl.1188/)] · core · via: Pluralistic Alignment, STONIC bibliography, LLM Social Science
- **Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.468/)] · core · via: Pluralistic Alignment
- **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS 2025 D&B Track Best Paper**, 2025 — [[paper](https://arxiv.org/abs/2510.22954)] · adjacent · via: LLM Social Science
- **Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration**, 2026 — [[paper](https://arxiv.org/abs/2604.13705)] · core · via: AIDAS Values & Pluralism
- **Black-Box Prompt Optimization: Aligning Large Language Models without Model Training**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.176/)] · core · via: Pluralistic Alignment
- **Communication-Efficient Desire Alignment for Proactive Embodied Human–Agent Interaction, ACL 2026 Main (Oral)**, 2026 — [[paper](https://arxiv.org/abs/2505.22503)] · adjacent · via: LLM Social Science
- **Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.**, 2022 — [[paper](https://arxiv.org/abs/2212.08073)] · core · via: Alignment Goal Survey
- **Constitutional Value Potentials: reading and steering internal priority margins in language models**, 2026 — [[paper](https://arxiv.org/abs/2606.15420)] · core · via: AIDAS Values & Pluralism
- **Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-main.85/)] · core · via: Pluralistic Alignment
- **Controllable Value Alignment in Large Language Models through Neuron-Level Editing**, 2026 — [[paper](https://arxiv.org/abs/2602.07356)] · core · via: AIDAS Values & Pluralism
- **Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2510.18526)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede’s Cultural Dimensions**, 2025 — [[paper](https://aclanthology.org/2025.coling-main.567/)] · core · via: Pluralistic Alignment
- **CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting**, 2024 — [[paper](https://arxiv.org/abs/2404.10199)] · core · via: Awesome Cultural NLP, Pluralistic Alignment
- **CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies**, 2024 — [[paper](https://aclanthology.org/2024.findings-emnlp.288/)] · core · via: Pluralistic Alignment
- **CultureLLM: Incorporating Cultural Differences into Large Language Models**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **CulturePark: Boosting Cross-cultural Understanding in Large Language Models**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?**, 2025 — [[paper](https://arxiv.org/abs/2505.23749)] · core · via: AIDAS Values & Pluralism
- **Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach**, 2025 — [[paper](https://openreview.net/forum?id=6KM1siLL8a)] · core · via: Pluralistic Alignment
- **Diverging Preferences: When do Annotators Disagree and do Models Know?**, 2024 — [[paper](https://arxiv.org/abs/2410.14632)] · adjacent · via: LLM Social Science
- **Diverse Human Value Alignment for Large Language Models via Ethical Reasoning**, 2025 — [[paper](https://arxiv.org/abs/2511.00379)] · core · via: AIDAS Values & Pluralism
- **Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning**, 2026 — [[paper](https://arxiv.org/abs/2603.10588)] · core · via: AIDAS Values & Pluralism
- **DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping**, 2026 — [[paper](https://arxiv.org/abs/2605.14420)] · core · via: AIDAS Values & Pluralism
- **Evaluating and Inducing Personality in Pre-trained Language Models**, 2023 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas**, 2024 — [[paper](https://arxiv.org/abs/2408.06929)] · core · via: Pluralistic Alignment
- **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.1301/)] · core · via: Pluralistic Alignment
- **Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes**, 2024 — [[paper](https://arxiv.org/abs/2412.13998)] · core · via: Pluralistic Alignment
- **Fine-tuning language models to find agreement among humans with diverse preferences**, 2022 — [[paper](https://arxiv.org/abs/2211.15006)] · adjacent · via: LLM Social Science
- **Foundational Challenges in Assuring Alignment and Safety of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2404.09932)] · adjacent · via: LLM Social Science
- **Foundational Moral Values for AI Alignment**, 2023 — [[paper](https://arxiv.org/abs/2311.17017)] · core · via: AIDAS Values & Pluralism
- **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.346/)] · core · via: Pluralistic Alignment
- **From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement**, 2026 — [[paper](https://arxiv.org/abs/2605.14912)] · core · via: AIDAS Values & Pluralism
- **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models**, 2023 — [[paper](https://aclanthology.org/2023.emnlp-main.961/)] · core · via: Pluralistic Alignment
- **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2310.17857)] · core · via: AIDAS Values & Pluralism
- **Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment**, 2024 — [[paper](https://openreview.net/forum?id=JI6j4NUGHv)] · core · via: Pluralistic Alignment
- **Group Robust Preference Optimization in Reward-free RLHF**, 2024 — [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)] · core · via: Pluralistic Alignment
- **HelpSteer2 2024-6**, 2024 — [[paper](https://arxiv.org/abs/2406.08673)] · adjacent · via: Awesome LLM Datasets
- **Imitation Beyond Expectation Using Pluralistic Stochastic Dominance**, 2025 — [[paper](https://openreview.net/forum?id=YX5DHa9OfX)] · core · via: Pluralistic Alignment
- **Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.**, 2022 — [[paper](https://arxiv.org/abs/2209.14375)] · core · via: Alignment Goal Survey
- **Improving the Distributional Alignment of LLMs using Supervision**, 2025 — [[paper](https://arxiv.org/abs/2507.00439)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1326/)] · core · via: STONIC bibliography
- **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation**, 2025 — [[paper](https://arxiv.org/abs/2507.11316)] · core · via: AIDAS Values & Pluralism
- **Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts**, 2024 — [[paper](https://aclanthology.org/2024.findings-emnlp.620/)] · core · via: Pluralistic Alignment
- **Justifications for Democratizing AI Alignment and Their Prospects**, 2025 — [[paper](https://arxiv.org/abs/2507.19548)] · core · via: AIDAS Values & Pluralism
- **Language Model Alignment in Multilingual Trolley Problems**, 2024 — [[paper](https://arxiv.org/abs/2407.02273)] · core · via: Pluralistic Alignment
- **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1028/)] · core · via: Pluralistic Alignment
- **Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain**, 2024 — [[paper](https://aclanthology.org/2024.naacl-industry.18/)] · core · via: Pluralistic Alignment
- **Language Models Resist Alignment: Evidence From Data Compression, ACL 2025 Best Paper**, 2025 — [[paper](https://arxiv.org/abs/2406.06144)] · adjacent · via: LLM Social Science
- **Large Language Model Alignment: A Survey**, 2023 — [[paper](https://arxiv.org/abs/2309.15025)] · core · via: Pluralistic Alignment, LLM Social Science
- **Large Language Models as Optimizers**, 2024 — [[paper](https://openreview.net/forum?id=Bb4VGOWELI)] · core · via: Pluralistic Alignment
- **Large pre-trained language models contain human-like biases of what is right and wrong to do. Schramowski et al. Nature Machine Intelligence 2022.**, 2022 — [[paper](https://arxiv.org/abs/2103.11790)] · core · via: Alignment Goal Survey
- **Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability**, 2025 — [[paper](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.90/)] · core · via: Pluralistic Alignment
- **LoRe: Personalizing LLMs via Low-Rank Reward Modeling**, 2025 — [[paper](https://arxiv.org/abs/2504.14439)] · core · via: Personalized Alignment, Pluralistic Alignment
- **MallowsPO: Fine-Tune Your LLM with Preference Dispersions**, 2024 — [[paper](https://arxiv.org/abs/2405.14953)] · core · via: Pluralistic Alignment
- **MAP: Multi-Human-Value Alignment Palette**, 2024 — [[paper](https://arxiv.org/abs/2410.19198)] · core · via: AIDAS Values & Pluralism
- **MaxMin-RLHF: Alignment with Diverse Human Preferences**, 2024 — [[paper](https://arxiv.org/abs/2402.08925)] · core · via: Pluralistic Alignment
- **MixDPO: Modeling Preference Strength for Pluralistic Alignment**, 2026 — [[paper](https://arxiv.org/abs/2601.06180)] · core · via: Pluralistic Alignment
- **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-main.240/)] · core · via: Pluralistic Alignment
- **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration**, 2024 — [[paper](https://arxiv.org/abs/2406.15951)] · core · via: AIDAS Values & Pluralism, Personalized Alignment, LLM Social Science
- **Moral Alignment for LLM Agents**, 2024 — [[paper](https://arxiv.org/abs/2410.01639)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning**, 2025 — [[paper](https://arxiv.org/abs/2511.12271)] · core · via: AIDAS Values & Pluralism
- **Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation**, 2025 — [[paper](https://arxiv.org/abs/2511.17579)] · core · via: AIDAS Values & Pluralism
- **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.120/)] · core · via: Pluralistic Alignment
- **Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.345/)] · core · via: Pluralistic Alignment
- **OASIS: Open Agent Social Interaction Simulations with One Million Agents**, 2024 — [[paper](https://arxiv.org/abs/2411.11581)] · core · via: Pluralistic Alignment
- **Optimizing generative AI by backpropagating language model feedback, Nature**, 2025 — [[paper](https://nature.com/articles/s41586-025-08661-4)] · adjacent · via: LLM Social Science
- **PAD: Personalized Alignment of LLMs at Decoding-Time**, 2024 — [[paper](https://arxiv.org/abs/2410.04070)] · core · via: AIDAS Values & Pluralism, Personalized Alignment, LLM Social Science
- **Pairwise Calibrated Rewards for Pluralistic Alignment**, 2025 — [[paper](https://arxiv.org/abs/2506.06298)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences**, 2024 — [[paper](https://arxiv.org/abs/2406.08469)] · core · via: Pluralistic Alignment
- **Parametric Social Identity Injection and Diversification in Public Opinion Simulation**, 2026 — [[paper](https://arxiv.org/abs/2603.16142)] · core · via: AIDAS Values & Pluralism
- **PERSONA: A Reproducible Testbed for Pluralistic Alignment**, 2025 — [[paper](https://aclanthology.org/2025.coling-main.752/)] · core · via: Pluralistic Alignment
- **Personality Alignment of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2408.11779)] · core · via: Pluralistic Alignment
- **PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization**, 2025 — [[paper](https://arxiv.org/abs/2507.16679)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **PKU-SafeRLHF 2023-7**, 2023 — [[paper](https://arxiv.org/abs/2307.04657)] · adjacent · via: Awesome LLM Datasets
- **Pluralistic Alignment for Healthcare: A Role-Driven Framework**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.1596/)] · core · via: Pluralistic Alignment
- **PluralLLM: Pluralistic Alignment in LLMs via Federated Learning**, 2025 — [[paper](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)] · core · via: Pluralistic Alignment
- **Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking**, 2024 — [[paper](https://arxiv.org/abs/2409.08622)] · core · via: Pluralistic Alignment, LLM Social Science
- **Position: A Roadmap to Impactful Pluralistic Alignment Research**, 2026 — [[paper](https://arxiv.org/abs/2607.22305)] · core · via: AIDAS Values & Pluralism
- **Position: Align AI to Our Aspirations, Not Our Flaws**, 2026 — [[paper](https://arxiv.org/abs/2606.13755)] · core · via: AIDAS Values & Pluralism
- **Position: The Alignment Community is Unintentionally Building a Censor's Toolkit**, 2026 — [[paper](https://openreview.net/forum?id=dy2HwmOvFX)] · core · via: AIDAS Values & Pluralism
- **Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles**, 2025 — [[paper](https://arxiv.org/abs/2502.06059)] · adjacent · via: LLM Social Science
- **ProgressGym: Alignment with a Millennium of Moral Progress**, 2024 — [[paper](https://arxiv.org/abs/2406.20087)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs**, 2024 — [[paper](https://aclanthology.org/2024.acl-long.381/)] · core · via: Pluralistic Alignment
- **Reflective Verbal Reward Design for Pluralistic Alignment**, 2025 — [[paper](https://arxiv.org/abs/2506.17834)] · core · via: Pluralistic Alignment
- **Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem**, 2026 — [[paper](https://arxiv.org/abs/2604.20805)] · core · via: AIDAS Values & Pluralism
- **Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?**, 2023 — [[paper](https://arxiv.org/abs/2308.15399)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Reward Model Perspectives: Whose Opinions Do Reward Models Reward?**, 2025 — [[paper](https://arxiv.org/abs/2510.06391)] · core · via: AIDAS Values & Pluralism
- **Robust Multi-Objective Controlled Decoding of Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2503.08796)] · core · via: Pluralistic Alignment
- **Role Steering of Language Models for Social Simulations**, 2026 — [[paper](https://arxiv.org/abs/2608.00023)] · core · via: AIDAS Values & Pluralism
- **SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation**, 2024 — [[paper](https://arxiv.org/abs/2410.16665)] · adjacent · via: LLM Social Science
- **Scopes of Alignment, 2025.01, AAAI 2025 workshop**, 2025 — [[paper](https://arxiv.org/abs/2501.12405)] · adjacent · via: LLM Social Science
- **Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning**, 2024 — [[paper](https://arxiv.org/abs/2408.16482)] · core · via: Pluralistic Alignment
- **Self-Pluralising Culture Alignment for Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.350/)] · core · via: Pluralistic Alignment
- **Simple Role Assignment is Extraordinarily Effective for Safety Alignment, ACL 2026 Findings**, 2026 — [[paper](https://arxiv.org/abs/2602.00061)] · adjacent · via: LLM Social Science
- **Social Simulacra: Creating Populated Prototypes for Social Computing Systems**, 2022 — [[paper](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)] · core · via: Pluralistic Alignment
- **Societal Alignment Frameworks Can Improve LLM Alignment**, 2025 — [[paper](https://arxiv.org/abs/2503.00069)] · core · via: AIDAS Values & Pluralism
- **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.162/)] · core · via: Pluralistic Alignment
- **SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment**, 2025 — [[paper](https://aclanthology.org/2025.findings-acl.41/)] · core · via: Pluralistic Alignment
- **Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression**, 2025 — [[paper](https://arxiv.org/abs/2508.08509)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF**, 2023 — [[paper](https://aclanthology.org/2023.findings-emnlp.754/)] · core · via: Pluralistic Alignment
- **STELA: a community-centred approach to norm elicitation for AI alignment, 2024.03, Nature Scientific Reports**, 2024 — [[paper](https://nature.com/articles/s41598-024-56648-4)] · adjacent · via: LLM Social Science
- **Strong and weak alignment of large language models with human values**, 2024 — [[paper](https://arxiv.org/abs/2408.04655)] · core · via: AIDAS Values & Pluralism
- **Strong and weak alignment of large language models with human values, 2024.08, Nature Scientific Reports**, 2024 — [[paper](https://nature.com/articles/s41598-024-70031-3)] · adjacent · via: LLM Social Science
- **Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions**, 2025 — [[paper](https://arxiv.org/abs/2508.11414)] · core · via: AIDAS Values & Pluralism
- **The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models**, 2026 — [[paper](https://aclanthology.org/2026.eacl-long.305/)] · core · via: Pluralistic Alignment
- **The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity**, 2025 — [[paper](https://arxiv.org/abs/2510.23965)] · core · via: AIDAS Values & Pluralism
- **The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment**, 2025 — [[paper](https://arxiv.org/abs/2512.03048)] · core · via: AIDAS Values & Pluralism
- **The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning**, 2023 — [[paper](https://arxiv.org/abs/2312.01552)] · core · via: Pluralistic Alignment
- **Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1408/)] · core · via: AIDAS Values & Pluralism, STONIC bibliography, LLM Social Science
- **Towards Scalable Automated Alignment of LLMs: A Survey**, 2024 — [[paper](https://arxiv.org/abs/2406.01252)] · core · via: Pluralistic Alignment
- **Training Socially Aligned Language Models in Simulated Human Society**, 2023 — [[paper](https://arxiv.org/abs/2305.16960)] · adjacent · via: Awesome LLM Datasets, LLM Social Science
- **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.1532/)] · core · via: STONIC bibliography
- **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights**, 2025 — [[paper](https://arxiv.org/abs/2506.06404)] · core · via: AIDAS Values & Pluralism
- **Unintended Impacts of LLM Alignment on Global Representation**, 2024 — [[paper](https://arxiv.org/abs/2402.15018)] · adjacent · via: Awesome Cultural NLP
- **Value Alignment from Unstructured Text**, 2024 — [[paper](https://aclanthology.org/2024.emnlp-industry.81/)] · core · via: Pluralistic Alignment
- **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value**, 2024 — [[paper](https://aclanthology.org/2024.naacl-long.486/)] · core · via: Pluralistic Alignment, STONIC bibliography
- **ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs**, 2025 — [[paper](https://aclanthology.org/2025.winlp-main.15/)] · core · via: STONIC bibliography
- **ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making**, 2025 — [[paper](https://arxiv.org/abs/2503.04569)] · core · via: AIDAS Values & Pluralism
- **VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2603.18113)] · core · via: AIDAS Values & Pluralism
- **VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment**, 2026 — [[paper](https://arxiv.org/abs/2603.04822)] · core · via: AIDAS Values & Pluralism
- **VISPA: Pluralistic Alignment via Automatic Value Selection and Activation**, 2026 — [[paper](https://arxiv.org/abs/2601.12758)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment
- **What are human values, and how do we align AI to them?**, 2024 — [[paper](https://arxiv.org/abs/2404.10636)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety**, 2025 — [[paper](https://arxiv.org/abs/2506.00415)] · core · via: AIDAS Values & Pluralism

<a id="catalog-value-representation-and-model-internals"></a>

#### 📐 Value representation and model internals · 44

- **A Method for Learning Value Systems in Generative AI**, 2026 — [[paper](https://arxiv.org/abs/2607.16903)] · core · via: AIDAS Values & Pluralism
- **AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations**, 2026 — [[paper](https://arxiv.org/abs/2601.22440)] · core · via: AIDAS Values & Pluralism
- **Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection**, 2026 — [[paper](https://arxiv.org/abs/2607.05052)] · core · via: AIDAS Values & Pluralism
- **Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment**, 2026 — [[paper](https://arxiv.org/abs/2604.12851)] · core · via: AIDAS Values & Pluralism
- **Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks**, 2026 — [[paper](https://arxiv.org/abs/2601.22396)] · core · via: AIDAS Values & Pluralism
- **Do Differences in Values Influence Disagreements in Online Discussions?**, 2023 — [[paper](https://arxiv.org/abs/2310.15757)] · core · via: AIDAS Values & Pluralism
- **Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration**, 2026 — [[paper](https://arxiv.org/abs/2602.00913)] · core · via: AIDAS Values & Pluralism
- **EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs**, 2025 — [[paper](https://arxiv.org/abs/2505.12792)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure**, 2025 — [[paper](https://doi.org/10.21203/rs.3.rs-8270539/v1)] · core · via: AIDAS Values & Pluralism
- **Enhancing Stance Classification on Social Media Using Quantified Moral Foundations**, 2023 — [[paper](https://arxiv.org/abs/2310.09848)] · core · via: AIDAS Values & Pluralism
- **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.585/)] · core · via: STONIC bibliography
- **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2502.02444)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas**, 2026 — [[paper](https://arxiv.org/abs/2602.04456)] · core · via: AIDAS Values & Pluralism
- **High-Dimension Human Value Representation in Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.naacl-long.274/)] · core · via: STONIC bibliography
- **High-Dimension Human Value Representation in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2404.07900)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum**, 2026 — [[paper](https://arxiv.org/abs/2601.14172)] · core · via: AIDAS Values & Pluralism
- **Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture**, 2026 — [[paper](https://arxiv.org/abs/2605.27373)] · core · via: AIDAS Values & Pluralism
- **Investigating Human Values in Online Communities**, 2024 — [[paper](https://arxiv.org/abs/2402.14177)] · core · via: AIDAS Values & Pluralism
- **Learning the Value Systems of Societies from Preferences**, 2025 — [[paper](https://arxiv.org/abs/2507.20728)] · core · via: AIDAS Values & Pluralism
- **Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning**, 2026 — [[paper](https://arxiv.org/abs/2602.08835)] · core · via: AIDAS Values & Pluralism
- **Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer**, 2026 — [[paper](https://arxiv.org/abs/2606.11018)] · core · via: AIDAS Values & Pluralism
- **Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora**, 2026 — [[paper](https://arxiv.org/abs/2605.22660)] · core · via: AIDAS Values & Pluralism
- **MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions**, 2024 — [[paper](https://arxiv.org/abs/2403.07678)] · core · via: AIDAS Values & Pluralism
- **Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning**, 2024 — [[paper](https://arxiv.org/abs/2401.17228)] · core · via: AIDAS Values & Pluralism
- **More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts**, 2026 — [[paper](https://arxiv.org/abs/2605.22641)] · core · via: AIDAS Values & Pluralism
- **MoVa: Towards Generalizable Classification of Human Morals and Values**, 2025 — [[paper](https://arxiv.org/abs/2509.24216)] · core · via: AIDAS Values & Pluralism
- **Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges**, 2026 — [[paper](https://arxiv.org/abs/2603.23659)] · core · via: AIDAS Values & Pluralism
- **SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments**, 2023 — [[paper](https://aclanthology.org/2023.semeval-1.313/)] · core · via: AIDAS Values & Pluralism, STONIC bibliography
- **SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs**, 2025 — [[paper](https://arxiv.org/abs/2504.12633)] · core · via: AIDAS Values & Pluralism
- **The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers**, 2025 — [[paper](https://arxiv.org/abs/2501.11770)] · core · via: AIDAS Values & Pluralism
- **Tracing Moral Foundations in Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2601.05437)] · core · via: AIDAS Values & Pluralism
- **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs**, 2025 — [[paper](https://aclanthology.org/2025.findings-emnlp.501/)] · core · via: STONIC bibliography
- **Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs**, 2025 — [[paper](https://arxiv.org/abs/2502.08640)] · core · via: AIDAS Values & Pluralism
- **Value Alignment of Social Media Ranking Algorithms**, 2025 — [[paper](https://arxiv.org/abs/2509.14434)] · core · via: AIDAS Values & Pluralism
- **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values**, 2023 — [[paper](https://arxiv.org/abs/2311.10766)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties**, 2023 — [[paper](https://arxiv.org/abs/2309.00779)] · core · via: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Value Lens: Using Large Language Models to Understand Human Values**, 2025 — [[paper](https://arxiv.org/abs/2512.15722)] · core · via: AIDAS Values & Pluralism
- **Value Profiles for Encoding Human Variation**, 2025 — [[paper](https://arxiv.org/abs/2503.15484)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models**, 2026 — [[paper](https://arxiv.org/abs/2602.03160)] · core · via: AIDAS Values & Pluralism
- **ValueNet: A New Dataset for Human Value Driven Dialogue System**, 2021 — [[paper](https://arxiv.org/abs/2112.06346)] · core · via: AIDAS Values & Pluralism
- **Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions**, 2025 — [[paper](https://arxiv.org/abs/2504.15236)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric**, 2023 — [[paper](https://aclanthology.org/2023.acl-long.789/)] · core · via: AIDAS Values & Pluralism
- **Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study**, 2026 — [[paper](https://arxiv.org/abs/2607.20270)] · core · via: AIDAS Values & Pluralism
- **Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media**, 2025 — [[paper](https://arxiv.org/abs/2511.08453)] · core · via: AIDAS Values & Pluralism

<a id="catalog-measurement-and-profiling"></a>

#### 📏 Measurement and profiling · 87

- **(GLOBE) Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2406.17675)] · core · via: LLM Psychometrics
- **(Others & custom) Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches**, 2024 — [[paper](https://arxiv.org/abs/2404.12744)] · core · via: LLM Psychometrics, LLM Social Science
- **(Others & custom) CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility**, 2023 — [[paper](https://arxiv.org/abs/2307.09705)] · core · via: Alignment Goal Survey, Awesome LLM Datasets, LLM Psychometrics
- **(Others & custom) Measurement of LLM’s Philosophies of Human Nature**, 2025 — [[paper](https://arxiv.org/abs/2504.02304)] · core · via: LLM Psychometrics
- **(Others & custom) Measuring Spiritual Values and Bias of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2410.11647)] · core · via: LLM Psychometrics
- **(Others & custom) Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas**, 2025 — [[paper](https://arxiv.org/abs/2505.14633)] · core · via: LLM Psychometrics
- **(Schwartz) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science**, 2023 — [[paper](https://journals.sagepub.com/doi/full/10.1177/17456916231214460)] · core · via: LLM Psychometrics
- **(Schwartz) Improving Language Model Personas via Rationalization with Psychological Scaffolds**, 2025 — [[paper](https://arxiv.org/abs/2504.17993)] · core · via: LLM Psychometrics
- **(Schwartz) Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025**, 2025 — [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/34839)] · core · via: LLM Psychometrics
- **(Schwartz) The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas**, 2025 — [[paper](https://arxiv.org/abs/2505.18154)] · core · via: LLM Psychometrics
- **(Schwartz) ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs**, 2024 — [[paper](https://arxiv.org/abs/2409.09586)] · core · via: LLM Psychometrics, LLM Social Science
- **(Schwartz) What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory**, 2023 — [[paper](https://arxiv.org/abs/2304.03612)] · core · via: LLM Psychometrics
- **(Schwartz) When Prompting Fails to Sway: Inertia in Moral and Value Judgments of Large Language Models, NeurIPS 2022**, 2022 — [[paper](https://arxiv.org/abs/2408.09049)] · core · via: LLM Psychometrics
- **(Schwartz) Who is GPT-3? An Exploration of Personality, Values and Demographics, EMNLP 2022 NLP+CSS workshop**, 2022 — [[paper](https://arxiv.org/abs/2209.14338)] · core · via: LLM Psychometrics
- **(VSM) Cultural Value Differences of LLMs: Prompt, Language, and Model Size**, 2024 — [[paper](https://arxiv.org/abs/2407.16891)] · core · via: LLM Psychometrics
- **(WVS) Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology**, 2024 — [[paper](https://arxiv.org/abs/2412.08846)] · core · via: LLM Psychometrics
- **(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)**, 2026 — [[paper](https://arxiv.org/abs/2509.01418)] · core · via: LLM Psychometrics, LLM Social Science
- **(WVS) Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2503.16148)] · core · via: LLM Psychometrics
- **A Scalable Approach to Evaluating Moral Sensitivity in LLMs**, 2026 — [[paper](https://arxiv.org/abs/2607.02972)] · core · via: AIDAS Values & Pluralism
- **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference**, 2025 — [[paper](https://arxiv.org/abs/2505.13531)] · core · via: AIDAS Values & Pluralism
- **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference**, 2026 — [[paper](https://openreview.net/forum?id=qNlTH4kYJZ)] · core · via: STONIC bibliography
- **Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?**, 2025 — [[paper](https://arxiv.org/abs/2506.00751)] · core · via: AIDAS Values & Pluralism
- **Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact**, 2026 — [[paper](https://arxiv.org/abs/2606.20205)] · core · via: AIDAS Values & Pluralism
- **Are Language Models Sensitive to Morally Irrelevant Distractors?**, 2026 — [[paper](https://arxiv.org/abs/2602.09416)] · core · via: AIDAS Values & Pluralism
- **Are Large Language Models Consistent over Value-laden Questions?**, 2024 — [[paper](https://arxiv.org/abs/2407.02996)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Are LLMs Bad at Moral Reasoning?**, 2026 — [[paper](https://arxiv.org/abs/2606.11635)] · core · via: AIDAS Values & Pluralism
- **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective**, 2024 — [[paper](https://arxiv.org/abs/2501.00581)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts**, 2026 — [[paper](https://arxiv.org/abs/2606.21939)] · core · via: AIDAS Values & Pluralism
- **Can Language Models Reason about Individualistic Human Values and Preferences?**, 2024 — [[paper](https://arxiv.org/abs/2410.03868)] · core · via: AIDAS Values & Pluralism
- **Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?**, 2026 — [[paper](https://arxiv.org/abs/2606.31213)] · core · via: AIDAS Values & Pluralism
- **Can Revealed Preferences Clarify LLM Alignment and Steering?**, 2026 — [[paper](https://arxiv.org/abs/2605.08556)] · core · via: AIDAS Values & Pluralism
- **CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses**, 2024 — [[paper](https://arxiv.org/abs/2407.10725)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Context-Value-Action Architecture for Value-Driven Large Language Model Agents**, 2026 — [[paper](https://arxiv.org/abs/2604.05939)] · core · via: AIDAS Values & Pluralism
- **Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences**, 2025 — [[paper](https://arxiv.org/abs/2511.02109)] · core · via: AIDAS Values & Pluralism
- **Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths**, 2025 — [[paper](https://arxiv.org/abs/2506.02481)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Do LLMs have Consistent Values?**, 2024 — [[paper](https://arxiv.org/abs/2407.12878)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust**, 2025 — [[paper](https://arxiv.org/abs/2507.02197)] · core · via: AIDAS Values & Pluralism
- **Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2509.24319)] · core · via: AIDAS Values & Pluralism
- **Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs**, 2026 — [[paper](https://arxiv.org/abs/2606.11232)] · core · via: AIDAS Values & Pluralism
- **Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?**, 2024 — [[paper](https://arxiv.org/abs/2402.18120)] · core · via: AIDAS Values & Pluralism
- **Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2504.04994)] · core · via: AIDAS Values & Pluralism
- **From Stability to Inconsistency: A Study of Moral Preferences in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2504.06324)] · core · via: AIDAS Values & Pluralism
- **Generative Value Conflicts Reveal LLM Priorities**, 2025 — [[paper](https://arxiv.org/abs/2509.25369)] · core · via: AIDAS Values & Pluralism
- **Heterogeneous Value Alignment Evaluation for Large Language Models**, 2023 — [[paper](https://arxiv.org/abs/2305.17147)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **How do LLMs reflect human moral foundations? a study using the moral foundations framework**, 2026 — [[paper](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)] · core · via: AIDAS Values & Pluralism
- **Human Psychometric Questionnaires Mischaracterize LLM Behavior**, 2025 — [[paper](https://arxiv.org/abs/2509.10078)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks**, 2025 — [[paper](https://arxiv.org/abs/2510.03384)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Incoherent Values? Probing LLM Preferences Through Parametric Variation**, 2026 — [[paper](https://arxiv.org/abs/2606.21102)] · core · via: AIDAS Values & Pluralism
- **Investigating Value-Reasoning Reliability in Small Large Language Models**, 2025 — [[paper](https://aclanthology.org/2025.emnlp-main.395/)] · core · via: AIDAS Values & Pluralism
- **LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values**, 2026 — [[paper](https://arxiv.org/abs/2606.13944)] · core · via: AIDAS Values & Pluralism
- **LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2408.01460)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests**, 2025 — [[paper](https://arxiv.org/abs/2510.22170)] · core · via: AIDAS Values & Pluralism
- **Measurement and Fairness**, 2021 — [[paper](https://doi.org/10.1145/3442188.3445901)] · core · via: STONIC bibliography
- **Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2409.12106)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Measuring human and AI values based on generative psychometrics with large language models**, 2025 — [[paper](https://doi.org/10.1609/aaai.v39i25.34839)] · core · via: STONIC bibliography
- **Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models**, 2026 — [[paper](https://arxiv.org/abs/2604.11216)] · core · via: AIDAS Values & Pluralism
- **Mechanistic Origin of Moral Indifference in Language Models**, 2026 — [[paper](https://arxiv.org/abs/2603.15615)] · core · via: AIDAS Values & Pluralism
- **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**, 2025 — [[paper](https://arxiv.org/abs/2501.15463)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation**, 2026 — [[paper](https://arxiv.org/abs/2605.12515)] · core · via: AIDAS Values & Pluralism
- **Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs**, 2026 — [[paper](https://arxiv.org/abs/2601.08634)] · core · via: AIDAS Values & Pluralism
- **Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability**, 2026 — [[paper](https://arxiv.org/abs/2605.03217)] · core · via: AIDAS Values & Pluralism
- **Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2511.08565)] · core · via: AIDAS Values & Pluralism
- **Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method**, 2025 — [[paper](https://sciencedirect.com/science/article/pii/S0925231225008422)] · core · via: AIDAS Values & Pluralism
- **Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs**, 2026 — [[paper](https://arxiv.org/abs/2606.12731)] · core · via: AIDAS Values & Pluralism
- **On the Credibility of Evaluating LLMs using Survey Questions**, 2026 — [[paper](https://arxiv.org/abs/2602.04033)] · core · via: AIDAS Values & Pluralism
- **Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses**, 2026 — [[paper](https://arxiv.org/abs/2605.28911)] · core · via: AIDAS Values & Pluralism
- **Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses**, 2026 — [[paper](https://arxiv.org/abs/2507.07188)] · core · via: AIDAS Values & Pluralism
- **Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation**, 2026 — [[paper](https://arxiv.org/abs/2607.05554)] · core · via: AIDAS Values & Pluralism
- **Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions**, 2026 — [[paper](https://arxiv.org/abs/2605.09893)] · core · via: AIDAS Values & Pluralism
- **Quantifying Data Contamination in Psychometric Evaluations of LLMs**, 2025 — [[paper](https://arxiv.org/abs/2510.07175)] · core · via: AIDAS Values & Pluralism
- **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing**, 2024 — [[paper](https://arxiv.org/abs/2406.14230)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing**, 2025 — [[paper](https://openreview.net/forum?id=0REM9ydeLZ)] · core · via: STONIC bibliography
- **Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?**, 2025 — [[paper](https://arxiv.org/abs/2507.13490)] · core · via: AIDAS Values & Pluralism
- **Superficial Beliefs in LLM Decision-Making**, 2026 — [[paper](https://arxiv.org/abs/2606.11016)] · core · via: AIDAS Values & Pluralism
- **The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models**, 2025 — [[paper](https://arxiv.org/abs/2512.03026)] · core · via: AIDAS Values & Pluralism
- **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs**, 2025 — [[paper](https://arxiv.org/abs/2505.17712)] · core · via: AIDAS Values & Pluralism
- **Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability**, 2026 — [[paper](https://arxiv.org/abs/2603.16017)] · core · via: AIDAS Values & Pluralism
- **Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs**, 2026 — [[paper](https://arxiv.org/abs/2601.10257)] · core · via: AIDAS Values & Pluralism
- **Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values**, 2025 — [[paper](https://arxiv.org/abs/2501.07071)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Value Drifts: Tracing Value Alignment During LLM Post-Training**, 2025 — [[paper](https://arxiv.org/abs/2510.26707)] · core · via: AIDAS Values & Pluralism
- **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items**, 2025 — [[paper](https://aclanthology.org/2025.acl-long.838/)] · core · via: STONIC bibliography
- **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items**, 2025 — [[paper](https://arxiv.org/abs/2505.01015)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts**, 2024 — [[paper](https://arxiv.org/abs/2411.11479)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics
- **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models**, 2024 — [[paper](https://arxiv.org/abs/2406.04214)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models**, 2023 — [[paper](https://arxiv.org/abs/2310.00378)] · core · via: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems**, 2026 — [[paper](https://arxiv.org/abs/2602.08567)] · core · via: AIDAS Values & Pluralism
- **Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts**, 2026 — [[paper](https://arxiv.org/abs/2605.25256)] · core · via: AIDAS Values & Pluralism

<a id="catalog-other-and-adjacent-value-research"></a>

#### 📎 Other and adjacent value research · 45

- **10.1186/s40537-024-00986-7**, 2024 — [[paper](https://link.springer.com/article/10.1186/s40537-024-00986-7)] · adjacent · via: Awesome Cultural NLP
- **A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle**, 2021 — [[paper](https://doi.org/10.1145/3465416.3483305)] · core · via: STONIC bibliography
- **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL 2025 Best Paper**, 2025 — [[paper](https://arxiv.org/abs/2402.11005)] · adjacent · via: LLM Social Science
- **Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective**, 2024 — [[paper](https://arxiv.org/abs/2408.04638)] · adjacent · via: LLM Social Science
- **Automated Mining of Structured Knowledge from Text in the Era of Large Language Models, 2024.08, KDD 2024**, 2024 — [[paper](https://dl.acm.org/doi/pdf/10.1145/3637528.3671469)] · adjacent · via: LLM Social Science
- **Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral**, 2026 — [[paper](https://arxiv.org/abs/2603.13890)] · adjacent · via: LLM Social Science
- **Chatbotarenaconversations 2023-6**, 2023 — [[paper](https://arxiv.org/abs/2306.05685)] · adjacent · via: Awesome LLM Datasets
- **Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science**, 2018 — [[paper](https://aclanthology.org/Q18-1041/)] · core · via: STONIC bibliography
- **EMNLP Main 18**, 2023 — [[paper](https://aclanthology.org/2023.emnlp-main.18/)] · adjacent · via: Awesome Cultural NLP
- **Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs**, 2024 — [[paper](https://arxiv.org/abs/2406.13993)] · adjacent · via: Awesome Cultural NLP
- **Fairness and Abstraction in Sociotechnical Systems**, 2019 — [[paper](https://doi.org/10.1145/3287560.3287598)] · core · via: STONIC bibliography
- **Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs, ACL 2025 Best Paper**, 2025 — [[paper](https://arxiv.org/abs/2502.01926)] · adjacent · via: LLM Social Science
- **Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization, 2025.05, Sociological Methods & Research**, 2025 — [[paper](https://journals.sagepub.com/doi/10.1177/00491241251327130)] · adjacent · via: LLM Social Science
- **Generative language models exhibit social identity biases, Nature Computational Science**, 2025 — [[paper](https://nature.com/articles/s43588-024-00741-1)] · adjacent · via: LLM Social Science
- **GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods**, 2023 — [[paper](https://arxiv.org/abs/2301.01893)] · adjacent · via: Awesome Cultural NLP
- **HG & CI & MC**, 2023 — [[paper](https://arxiv.org/abs/2311.09528)] · adjacent · via: Awesome LLM Datasets
- **Holistic Evaluation of Language Models**, 2023 — [[paper](https://openreview.net/forum?id=iO4LZibEqW)] · core · via: STONIC bibliography
- **Large Language Model Safety: A Holistic Survey**, 2024 — [[paper](https://arxiv.org/abs/2412.17686)] · adjacent · via: LLM Social Science
- **Large language models (LLM) in computational social science: prospects, current state, and challenges, 2025.03, Social Network Analysis and Mining**, 2025 — [[paper](https://link.springer.com/article/10.1007/s13278-025-01428-9)] · adjacent · via: LLM Social Science
- **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, 2023.12, Nature humanities and social sciences communications**, 2023 — [[paper](https://arxiv.org/abs/2312.11970)] · adjacent · via: LLM Social Science
- **Linhao Yu et al. ACL Findings 2024.**, 2024 — [[paper](https://aclanthology.org/2024.findings-acl.703/)] · adjacent · via: Awesome LLM Safety
- **Machine Bias. How Do Generative Language Models Answer Opinion Polls?, 2025.04, Sociological Methods & Research**, 2025 — [[paper](https://doi.org/10.1177/00491241251330582)] · adjacent · via: LLM Social Science
- **Nicholas Botzer et al. arXiv 2021.**, 2021 — [[paper](https://arxiv.org/abs/2101.07664)] · adjacent · via: Awesome LLM Safety
- **On the Credibility of Evaluating LLMs using Survey Questions**, 2026 — [[paper](https://aclanthology.org/2026.mme-main.2/)] · core · via: STONIC bibliography
- **On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?**, 2021 — [[paper](https://doi.org/10.1145/3442188.3445922)] · core · via: STONIC bibliography
- **On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective**, 2025 — [[paper](https://arxiv.org/abs/2502.14296)] · adjacent · via: LLM Social Science
- **Persuading voters using human–artificial intelligence dialogues, Nature**, 2025 — [[paper](https://nature.com/articles/s41586-025-09771-9)] · adjacent · via: LLM Social Science
- **Position: AI Evaluation Should Learn from How We Test Humans**, 2023 — [[paper](https://arxiv.org/abs/2306.10512)] · core · via: STONIC bibliography
- **PRM800K 2023-5**, 2023 — [[paper](https://arxiv.org/abs/2305.20050)] · adjacent · via: Awesome LLM Datasets
- **Questioning the Survey Responses of Large Language Models, NeurIPS 2024 Oral**, 2024 — [[paper](https://arxiv.org/abs/2306.07951)] · adjacent · via: LLM Social Science
- **RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models**, 2020 — [[paper](https://aclanthology.org/2020.findings-emnlp.301/)] · core · via: STONIC bibliography
- **SHP 2021-10 — All — EN — HG**, 2021 — [[paper](https://arxiv.org/abs/2110.08420)] · adjacent · via: Awesome LLM Datasets
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025**, 2025 — [[paper](https://arxiv.org/abs/2412.06435)] · adjacent · via: LLM Social Science
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025**, 2025 — [[paper](https://openreview.net/forum?id=3ms8EQY7f8)] · adjacent · via: LLM Social Science
- **Stick to your role! Stability of personal values expressed in large language models**, 2024 — [[paper](https://doi.org/10.1371/journal.pone.0309114)] · core · via: STONIC bibliography
- **SummarizefromFeedback 2020-9**, 2020 — [[paper](https://arxiv.org/abs/2009.01325)] · adjacent · via: Awesome LLM Datasets
- **The AI Gap: How Socioeconomic Status Affects Language Technology Interactions, ACL 2025 Best Social Impact Paper**, 2025 — [[paper](https://arxiv.org/abs/2505.12158)] · adjacent · via: LLM Social Science
- **The Rise and Potential of Large Language Model Based Agents: A Survey**, 2023 — [[paper](https://arxiv.org/abs/2309.07864)] · adjacent · via: LLM Social Science
- **UltraFeedback**, 2023 — [[paper](https://arxiv.org/abs/2310.01377)] · adjacent · via: Awesome LLM Datasets
- **UltraInteract 2024-4**, 2024 — [[paper](https://arxiv.org/abs/2404.02078)] · adjacent · via: Awesome LLM Datasets
- **Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries**, 1992 — [[paper](https://sciencedirect.com/science/article/pii/S0065260108602816)] · core · via: STONIC bibliography
- **Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents**, 2026 — [[paper](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)] · core · via: AIDAS Values & Pluralism
- **WebGPT: Browser-assisted question-answering with human feedback**, 2021 — [[paper](https://arxiv.org/abs/2112.09332)] · adjacent · via: Awesome LLM Datasets
- **Who is GPT-3? An exploration of personality, values and demographics**, 2022 — [[paper](https://aclanthology.org/2022.nlpcss-1.24/)] · core · via: STONIC bibliography
- **Zhijing Jin et al. NeurIPS 2022.**, 2022 — [[paper](https://arxiv.org/abs/2210.01478)] · adjacent · via: Awesome LLM Safety

### 🧩 Data, models, code, and additional resources

<a id="catalog-dataset-and-benchmark-artifacts"></a>

#### 💾 Dataset and benchmark artifacts · 28

- **(Others & custom) Towards Measuring the Representation of Subjective Global Opinions in Language Models** — [[data](https://huggingface.co/datasets/Anthropic/llm_global_opinions)] · core · via: Alignment Goal Survey, LLM Psychometrics
- **2509.17399** — [[data](https://huggingface.co/datasets/nlip/DIWALI)] · adjacent · via: Awesome Cultural NLP
- **A Systematic Survey of Cultural Datasets for Equitable LLM Alignment** — [[data](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)] · core · via: AIDAS Values & Pluralism
- **Big-Math 2025-2** — [[data](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified)] · adjacent · via: Awesome LLM Datasets
- **Chatbotarenaconversations 2023-6** — [[data](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)] · adjacent · via: Awesome LLM Datasets
- **Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024** — [[data](https://mango.mpi-inf.mpg.de/)] · adjacent · via: LLM Social Science
- **CValues 2023-7** — [[data](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)] · adjacent · via: Awesome LLM Datasets
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture** — [[data](https://huggingface.co/datasets/lyan62/FoodieQA)] · adjacent · via: Awesome Cultural NLP
- **HelpSteer2 2024-6** — [[data](https://huggingface.co/datasets/nvidia/HelpSteer2)] · adjacent · via: Awesome LLM Datasets
- **HF Datasets** — [[data](https://huggingface.co/datasets/MinhDucBui/Multi3Hate)] · adjacent · via: Awesome Cultural NLP
- **HG & CI** — [[data](https://huggingface.co/datasets/openai/webgpt_comparisons)] · adjacent · via: Awesome LLM Datasets
- **HG & CI & MC** — [[data](https://huggingface.co/datasets/nvidia/HelpSteer)] · adjacent · via: Awesome LLM Datasets
- **Medical-rlhf 2023-5** — [[data](https://huggingface.co/datasets/shibing624/medical)] · adjacent · via: Awesome LLM Datasets
- **MT-Benchhumanjudgments 2023-6** — [[data](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)] · adjacent · via: Awesome LLM Datasets
- **OASST1pairwiserlhfreward 2023-5** — [[data](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)] · adjacent · via: Awesome LLM Datasets
- **OpenHermesPreferences 2024-3** — [[data](https://huggingface.co/datasets/argilla/OpenHermesPreferences)] · adjacent · via: Awesome LLM Datasets
- **Paper1** — [[data](https://huggingface.co/datasets/Anthropic/hh-rlhf)] · adjacent · via: Awesome LLM Datasets
- **PKU-SafeRLHF 2023-7** — [[data](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)] · adjacent · via: Awesome LLM Datasets
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.** — [[data](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)] · core · via: Alignment Goal Survey
- **SafetyBench 2023-9** — [[data](https://huggingface.co/datasets/thu-coai/SafetyBench)] · adjacent · via: Awesome LLM Datasets
- **SHP 2021-10 — All — EN — HG** — [[data](https://huggingface.co/datasets/stanfordnlp/SHP)] · adjacent · via: Awesome LLM Datasets
- **Stack-Exchange-Preferences** — [[data](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)] · adjacent · via: Awesome LLM Datasets
- **SummarizefromFeedback 2020-9** — [[data](https://huggingface.co/datasets/openai/summarize_from_feedback)] · adjacent · via: Awesome LLM Datasets
- **UltraFeedback** — [[data](https://huggingface.co/datasets/openbmb/UltraFeedback)] · adjacent · via: Awesome LLM Datasets
- **UltraInteract 2024-4** — [[data](https://huggingface.co/datasets/openbmb/UltraInteract_pair)] · adjacent · via: Awesome LLM Datasets
- **ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022** — [[data](https://liang-qiu.github.io/ValueNet/)] · core · via: Alignment Goal Survey, LLM Social Science
- **When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.** — [[data](https://huggingface.co/datasets/feradauto/MoralExceptQA)] · core · via: Alignment Goal Survey
- **Zhihurlhf3k 2023-4** — [[data](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)] · adjacent · via: Awesome LLM Datasets

<a id="catalog-model-checkpoints-and-scorers"></a>

#### 🧠 Model checkpoints and scorers · 5

- **2502.13766** — [[model](https://huggingface.co/floschne)] · adjacent · via: Awesome Cultural NLP
- **Exploring Universal Human Values with Large Language Models: The AWARE-Value Model** — [[model](https://researchsquare.com/article/rs-8188052/v1)] · core · via: AIDAS Values & Pluralism
- **MT-Benchhumanjudgments 2023-6** — [[model](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)] · adjacent · via: Awesome LLM Datasets
- **Robustness of large language models in moral judgements** — [[model](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)] · core · via: AIDAS Values & Pluralism
- **Stick to your role! Stability of personal values expressed in large language models** — [[model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309114)] · core · via: AIDAS Values & Pluralism, LLM Social Science

<a id="catalog-code-repositories"></a>

#### 🧰 Code repositories · 97

- **(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023** — [[code](https://github.com/wanng-ide/ealm)] · core · via: LLM Psychometrics
- **(MFT) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science** — [[code](https://github.com/feradauto/MoralCoT)] · core · via: Alignment Goal Survey, Awesome LLM Safety, LLM Psychometrics
- **(MFT) MoralBench: Moral Evaluation of LLMs** — [[code](https://github.com/agiresearch/MoralBench)] · core · via: LLM Psychometrics
- **(Others & custom) Measurement of LLM’s Philosophies of Human Nature** — [[code](https://github.com/kodenii/M-PHNS)] · core · via: LLM Psychometrics
- **(Schwartz) ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, ACL 2024** — [[code](https://github.com/Value4AI/ValueBench)] · core · via: LLM Psychometrics, LLM Social Science
- **(SVO) Heterogeneous Value Alignment Evaluation for Large Language Models, AAAI 2024 Workshop** — [[code](https://github.com/zowiezhang/HVAE)] · core · via: LLM Psychometrics
- **(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)** — [[code](https://github.com/ku-nlp/global-opinion-alignment)] · core · via: LLM Psychometrics
- **2023.findings-acl.631** — [[code](https://github.com/shramay-palta/FORK_ACL2023)] · adjacent · via: Awesome Cultural NLP
- **2023.findings-emnlp.509** — [[code](https://github.com/SALT-NLP/CulturallyAwareNLI)] · adjacent · via: Awesome Cultural NLP
- **2024.findings-naacl.196** — [[code](https://github.com/zhanhl316/ReNoVi)] · adjacent · via: Awesome Cultural NLP
- **2209.12226** — [[code](https://github.com/google-research-datasets/nlp-fairness-for-india)] · adjacent · via: Awesome Cultural NLP
- **2210.08604** — [[code](https://github.com/yrf1/NormSage)] · adjacent · via: Awesome Cultural NLP
- **2301.01893** — [[code](https://github.com/WadeYin9712/GIVL)] · adjacent · via: Awesome Cultural NLP
- **2305.11840** — [[code](https://github.com/google-research-datasets/seegull)] · adjacent · via: Awesome Cultural NLP
- **2305.14456** — [[code](https://github.com/tareknaous/camel)] · adjacent · via: Awesome Cultural NLP
- **2305.16171** — [[code](https://github.com/simran-khanuja/Multilingual-Fig-QA)] · adjacent · via: Awesome Cultural NLP
- **2308.16705** — [[code](https://github.com/nlee0212/CREHate)] · adjacent · via: Awesome Cultural NLP
- **2310.17586** — [[code](https://github.com/iamshnoo/weathub)] · adjacent · via: Awesome Cultural NLP
- **2401.10352** — [[code](https://github.com/yongcaoplus/cuDialog)] · adjacent · via: Awesome Cultural NLP
- **2402.09369v1** — [[code](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)] · adjacent · via: Awesome Cultural NLP
- **2402.10946** — [[code](https://github.com/Scarelette/CultureLLM)] · adjacent · via: Awesome Cultural NLP
- **2403.14651** — [[code](https://github.com/microsoft/DOSA)] · adjacent · via: Awesome Cultural NLP
- **2404.01247** — [[code](https://github.com/simran-khanuja/image-transcreation)] · adjacent · via: Awesome Cultural NLP
- **2404.10199v1** — [[code](https://github.com/huihanlhh/Culture-Gen)] · adjacent · via: Awesome Cultural NLP
- **2404.12464** — [[code](https://github.com/Akhila-Yerukola/NormAd)] · adjacent · via: Awesome Cultural NLP
- **2404.16019** — [[code](https://github.com/HannahKirk/prism-alignment)] · adjacent · via: Awesome Cultural NLP
- **2406.09948** — [[code](https://github.com/nlee0212/BLEnD)] · adjacent · via: Awesome Cultural NLP
- **2407.03791** — [[code](https://github.com/floschne/m5b)] · adjacent · via: Awesome Cultural NLP
- **2407.06863** — [[code](https://github.com/google-research-datasets/cube)] · adjacent · via: Awesome Cultural NLP
- **2412.20760** — [[code](https://github.com/huihanlhh/CultureGenAttr)] · adjacent · via: Awesome Cultural NLP
- **2502.13766** — [[code](https://github.com/floschne/gimmick)] · adjacent · via: Awesome Cultural NLP
- **2509.17399** — [[code](https://github.com/pramitsahoo/culture-evaluation)] · adjacent · via: Awesome Cultural NLP
- **3539618.3591877** — [[code](https://github.com/zhanhl316/SocialDial)] · adjacent · via: Awesome Cultural NLP
- **<a href="** — [[code](https://github.com/sindresorhus/awesome)] · core · via: AIDAS Values & Pluralism
- **\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models** — [[code](https://github.com/PKU-YuanGroup/Machine-Mindset)] · adjacent · via: LLM Social Science
- **\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms** — [[code](https://github.com/GAIR-NLP/OPO)] · adjacent · via: Awesome LLM Safety, LLM Social Science
- **A Roadmap to Pluralistic Alignment, ICML 2024** — [[code](https://github.com/jfisher52/AI_Pluralistic_Alignment)] · adjacent · via: LLM Social Science
- **A Survey on Evaluation of Large Language Models** — [[code](https://github.com/MLGroupJLU/LLM-eval-survey)] · adjacent · via: LLM Social Science
- **A Survey on Large Language Model based Autonomous Agents** — [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)] · adjacent · via: LLM Social Science
- **AI Job Displacement Tracker** — [[code](https://github.com/noahaust2/ai-displacement-tracker)] · adjacent · via: LLM Social Science
- **Aligning ai with shared human values. Hendrycks et al. arXiv 2020.** — [[code](https://github.com/hendrycks/ethics)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **Aligning Large Language Models with Human: A Survey** — [[code](https://github.com/GaryYufei/AlignLLMHumanSurvey)] · adjacent · via: LLM Social Science
- **Alignment-Goal-Survey** — [[code](https://github.com/ValueCompass/Alignment-Goal-Survey)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **Alpacacomparisondata 2023-3** — [[code](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)] · adjacent · via: Awesome LLM Datasets
- **Awesome-LLM-in-Social-Science** — [[code](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)] · core · via: AIDAS Values & Pluralism
- **Awesome-LLM-Psychometrics** — [[code](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)] · core · via: AIDAS Values & Pluralism
- **awesome-llm-social-simulation** — [[code](https://github.com/Wanying-He/awesome-llm-social-simulation)] · core · via: AIDAS Values & Pluralism
- **Awesome-Personalized-Alignment** — [[code](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)] · core · via: AIDAS Values & Pluralism
- **Awesome-Pluralistic-Alignment** — [[code](https://github.com/anudeex/Awesome-Pluralistic-Alignment)] · core · via: AIDAS Values & Pluralism
- **Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral** — [[code](https://github.com/jingzhe-lin/ASVO)] · adjacent · via: LLM Social Science
- **Big-Math 2025-2** — [[code](https://github.com/SynthLabsAI/big-math)] · adjacent · via: Awesome LLM Datasets
- **code and data** — [[code](https://github.com/NeuralSentinel/CulturalKaleidoscope)] · adjacent · via: LLM Social Science
- **collection** — [[code](https://github.com/Indiiigo/LLM_rep_review)] · adjacent · via: LLM Social Science
- **Concerns on the use of generative AI in social science research** — [[code](https://github.com/uh-dcm/genai-concerns)] · adjacent · via: LLM Social Science
- **Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.** — [[code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)] · core · via: Alignment Goal Survey
- **CrowS-Pairs** — [[code](https://github.com/nyu-mll/crows-pairs)] · adjacent · via: Awesome LLM Datasets
- **cultural-llm-papers** — [[code](https://github.com/faridlazuarda/cultural-llm-papers)] · core · via: AIDAS Values & Pluralism, Awesome Cultural NLP
- **culture-awareness-llms** — [[code](https://github.com/siddheshih/culture-awareness-llms)] · core · via: AIDAS Values & Pluralism
- **CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility. Xu et al. arXiv 2023.** — [[code](https://github.com/X-PLUG/CValues)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Datasets for depression detection using data posted on online platforms** — [[code](https://github.com/bucuram/depression-datasets-nlp)] · adjacent · via: LLM Social Science
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture** — [[code](https://github.com/lyan62/FoodieQA)] · adjacent · via: Awesome Cultural NLP
- **github.com** — [[code](https://github.com/CLUEbenchmark/CLUEDatasetSearch)] · adjacent · via: LLM Social Science
- **HelpSteer2 2024-6** — [[code](https://github.com/NVIDIA/NeMo-Aligner)] · adjacent · via: Awesome LLM Datasets
- **Heterogeneous Value Evaluation for Large Language Models** — [[code](https://github.com/zowiezhang/A2EHV)] · adjacent · via: LLM Social Science
- **HF Datasets** — [[code](https://github.com/MinhDucBui/Multi3Hate)] · adjacent · via: Awesome Cultural NLP
- **High-Dimension Human Value Representation in Large Language Models** — [[code](https://github.com/HLTCHKUST/UniVaR)] · adjacent · via: LLM Social Science
- **How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main** — [[code](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)] · adjacent · via: LLM Social Science
- **huozirlhfdata 2024-2** — [[code](https://github.com/HIT-SCIR/huozi)] · adjacent · via: Awesome LLM Datasets
- **huozirlhfdata 2024-2** — [[code](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)] · adjacent · via: Awesome LLM Datasets
- **Large Language Model based Multi-Agents: A Survey of Progress and Challenges** — [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)] · adjacent · via: LLM Social Science
- **Leaderboard** — [[code](https://github.com/thu-coai/Safety-Prompts)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Medical-rlhf 2023-5** — [[code](https://github.com/shibing624/MedicalGPT)] · adjacent · via: Awesome LLM Datasets
- **Mental Health Datasets** — [[code](https://github.com/kharrigian/mental-health-datasets)] · adjacent · via: LLM Social Science
- **Moral stories: Situated reasoning about norms, intents, actions, and their consequences. Emelin et al. arXiv 2020.** — [[code](https://github.com/demelin/moral_stories)] · core · via: Alignment Goal Survey
- **MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.** — [[code](https://github.com/thu-coai/MoralDial)] · core · via: Alignment Goal Survey
- **MT-Benchhumanjudgments 2023-6** — [[code](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)] · adjacent · via: Awesome LLM Datasets
- **PKU-SafeRLHF 2023-7** — [[code](https://github.com/PKU-Alignment/safe-rlhf)] · adjacent · via: Awesome LLM Datasets
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.** — [[code](https://github.com/IBM/Dromedary)] · core · via: Alignment Goal Survey
- **PRM800K 2023-5** — [[code](https://github.com/openai/prm800k)] · adjacent · via: Awesome LLM Datasets
- **ProgressGym: Alignment with a Millennium of Moral Progress, NeurIPS 2024 D&B Track Spotlight** — [[code](https://github.com/PKU-Alignment/ProgressGym)] · adjacent · via: LLM Social Science
- **rladmstn1714/CLIcK** — [[code](https://github.com/rladmstn1714/CLIcK)] · adjacent · via: Awesome Cultural NLP
- **SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.** — [[code](https://github.com/sharonlevy/SafeText)] · core · via: Alignment Goal Survey
- **SafetyBench 2023-9** — [[code](https://github.com/thu-coai/SafetyBench)] · adjacent · via: Awesome LLM Datasets
- **Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.** — [[code](https://github.com/allenai/scruples)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **SHP 2021-10 — All — EN — HG** — [[code](https://github.com/kawine/dataset_difficulty)] · adjacent · via: Awesome LLM Datasets
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025** — [[code](https://github.com/zfw1226/D2A)] · adjacent · via: LLM Social Science
- **SocialAgent** — [[code](https://github.com/FudanDISC/SocialAgent)] · core · via: AIDAS Values & Pluralism, LLM Social Science
- **SuperCLUE-Safety 2023-9** — [[code](https://github.com/CLUEbenchmark/SuperCLUE-safety)] · adjacent · via: Awesome LLM Datasets
- **The moral integrity corpus: A benchmark for ethical dialogue systems. Ziems et al. arXiv 2022.** — [[code](https://github.com/SALT-NLP/mic)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **The Rise and Potential of Large Language Model Based Agents: A Survey** — [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)] · adjacent · via: LLM Social Science
- **Training a helpful and harmless assistant with reinforcement learning from human feedback. Bai et al. arXiv 2022.** — [[code](https://github.com/anthropics/hh-rlhf)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Training Socially Aligned Language Models in Simulated Human Society** — [[code](https://github.com/agi-templar/Stable-Alignment)] · adjacent · via: Awesome LLM Datasets, LLM Social Science
- **TRUSTGPT 2023-6** — [[code](https://github.com/HowieHwong/TrustGPT)] · adjacent · via: Awesome LLM Datasets
- **UltraFeedback** — [[code](https://github.com/OpenBMB/UltraFeedback)] · adjacent · via: Awesome LLM Datasets
- **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, AAAI24** — [[code](https://github.com/tsor13/kaleido)] · adjacent · via: LLM Social Science
- **Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)** — [[code](https://github.com/MoralAgentSim/Simulation-Engine)] · adjacent · via: LLM Social Science
- **⭐️ Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025** — [[code](https://github.com/Value4AI/gpv)] · adjacent · via: LLM Social Science

<a id="catalog-project-pages"></a>

#### 🌐 Project pages · 10

- **2109.13238** — [[project](https://marvl-challenge.github.io/)] · adjacent · via: Awesome Cultural NLP
- **2509.17399** — [[project](https://nlip-lab.github.io/nlip/publications/diwali/)] · adjacent · via: Awesome Cultural NLP
- **AI Alignment: A Comprehensive Survey** — [[project](https://alignmentsurvey.com/)] · adjacent · via: LLM Social Science
- **Can machines learn morality? the delphi experiment. Jiang et al. arXiv 2021.** — [[project](https://delphi.allenai.org/)] · core · via: Alignment Goal Survey
- **Concerns on the use of generative AI in social science research** — [[project](https://uh-dcm.github.io/genai-concerns/)] · adjacent · via: LLM Social Science
- **NLPositionality: Characterizing Design Biases of Datasets and Models** — [[project](https://nlpositionality.cs.washington.edu/)] · adjacent · via: Awesome Cultural NLP
- **Political-LLM: Large Language Models in Political Science** — [[project](https://political-llm.org/)] · adjacent · via: LLM Social Science
- **SafetyBench 2023-9** — [[project](https://llmbench.ai/safety)] · adjacent · via: Awesome LLM Datasets
- **SuperCLUE-Safety 2023-9** — [[project](https://cluebenchmarks.com/superclue_safety.html)] · adjacent · via: Awesome LLM Datasets
- **Towards Measuring the Representation of Subjective Global Opinions in Language Models** — [[project](https://llmglobalvalues.anthropic.com/)] · adjacent · via: LLM Social Science

<a id="catalog-survey-resources"></a>

#### 📋 Survey resources · 4

- **EVS — European Values Survey** — [[survey](https://europeanvaluesstudy.eu/)] · core · via: AIDAS Values & Pluralism, Alignment Goal Survey
- **GSS — General Social Survey** — [[survey](https://gss.norc.org/)] · core · via: AIDAS Values & Pluralism
- **World Values Survey Wave 7 (2017-2022).** — [[survey](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)] · core · via: Alignment Goal Survey
- **WVS — World Values Survey** — [[survey](https://worldvaluessurvey.org/)] · core · via: AIDAS Values & Pluralism

<a id="catalog-additional-resources"></a>

#### 🔗 Additional resources · 88

- **!\[Awesome** — [[link](https://awesome.re)] · core · via: Pluralistic Alignment
- **(ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis** — [[link](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)] · core · via: LLM Psychometrics
- **(ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis** — [[link](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)] · core · via: LLM Psychometrics
- **(ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL)** — [[link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)] · core · via: LLM Psychometrics
- **(ATP) Whose Opinions Do Language Models Reflect?, ICML 2023** — [[link](https://proceedings.mlr.press/v202/santurkar23a.html)] · core · via: LLM Psychometrics
- **(Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL)** — [[link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)] · core · via: LLM Psychometrics
- **(Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate** — [[link](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000429)] · core · via: LLM Psychometrics
- **(Others & custom) DO MINDFULNESS ACTIVITIES IMPROVE HANDGRIP STRENGTH AMONG OLDER ADULTS: A PROPENSITY SCORE MATCHING APPROACH, 2024.12, Innovation in Aging** — [[link](https://academic.oup.com/innovateage/article/8/Supplement_1/1010/7939280)] · core · via: LLM Psychometrics
- **(Others & custom) Improving GPT Generated Synthetic Samples with Sampling-Permutation Algorithm** — [[link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4548937)] · core · via: LLM Psychometrics
- **(Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science** — [[link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)] · core · via: LLM Psychometrics
- **(PCT) The Political Biases of ChatGPT, 2023.01, Social Sciences** — [[link](https://mdpi.com/2076-0760/12/3/148)] · core · via: LLM Psychometrics
- **(Schwartz) Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz’s Theory of Basic Values, 2024.01, JMIR Mental Health** — [[link](https://mental.jmir.org/2024/1/e55988)] · core · via: LLM Psychometrics
- **(VSM) Large Language Models as Superpositions of Cultural Perspectives** — [[link](https://gitlab.inria.fr/gkovac/value_stability)] · core · via: LLM Psychometrics
- **2301.02560** — [[link](https://geodiverse-data-collection.cs.princeton.edu/)] · adjacent · via: Awesome Cultural NLP
- **2410.12705** — [[link](https://worldcuisines.github.io/)] · adjacent · via: Awesome Cultural NLP
- **<a href="** — [[link](https://git.io/typing-svg)] · core · via: AIDAS Values & Pluralism
- **<img src="** — [[link](https://capsule-render.vercel.app/api)] · core · via: AIDAS Values & Pluralism
- **<img src="** — [[link](https://readme-typing-svg.demolab.com)] · core · via: AIDAS Values & Pluralism
- **A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights** — [[link](https://unesdoc.unesco.org/ark:/48223/pf0000048063)] · core · via: AIDAS Values & Pluralism
- **A review of automatic item generation techniques leveraging large language models** — [[link](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)] · core · via: LLM Psychometrics
- **A theory of justice.** — [[link](https://jstor.org/stable/j.ctvjf9z6v)] · core · via: AIDAS Values & Pluralism
- **A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism** — [[link](http://jstor.org/stable/24707060)] · core · via: STONIC bibliography
- **Aggregating Sets of Judgments: An Impossibility Result** — [[link](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)] · core · via: AIDAS Values & Pluralism
- **An Overview of the Schwartz Theory of Basic Values** — [[link](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)] · core · via: AIDAS Values & Pluralism
- **An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012.** — [[link](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)] · core · via: Alignment Goal Survey
- **Basic human values: Theory, measurement, and applications** — [[link](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)] · core · via: AIDAS Values & Pluralism
- **Can Generative AI improve social science?, 2024.05, PNAS** — [[link](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)] · adjacent · via: LLM Social Science
- **Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023** — [[link](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)] · core · via: LLM Psychometrics
- **Citizenship and Social Class** — [[link](https://books.google.co.kr/books?id=99v4JQAACAAJ)] · core · via: AIDAS Values & Pluralism
- **Collective Choice and Social Welfare** — [[link](https://jstor.org/stable/j.ctv2sp3dqx)] · core · via: AIDAS Values & Pluralism
- **Conflicts of Values (in Moral Luck)** — [[link](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)] · core · via: AIDAS Values & Pluralism
- **Creating Capabilities: The Human Development Approach and Its Implementation** — [[link](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)] · core · via: AIDAS Values & Pluralism
- **Cultural Value Orientations** — [[link](https://researchgate.net/publication/265997557)] · core · via: AIDAS Values & Pluralism
- **Culture's consequences: International differences in work-related values** — [[link](https://philpapers.org/rec/HOFCCI-2)] · core · via: AIDAS Values & Pluralism
- **Culture's consequences: International differences in work-related values. Hofstede et al. 1984.** — [[link](https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC)] · core · via: Alignment Goal Survey
- **Cultures and organizations: software of the mind** — [[link](https://books.google.co.kr/books?id=o4OqTgV3V00C)] · core · via: AIDAS Values & Pluralism
- **Do LLMs have Consistent Values?** — [[link](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)] · core · via: STONIC bibliography
- **ESS — European Social Survey** — [[link](https://europeansocialsurvey.org/data-portal)] · core · via: AIDAS Values & Pluralism
- **Functional theory of human values** — [[link](https://researchgate.net/publication/259486885)] · core · via: AIDAS Values & Pluralism
- **Handbook of Computational Social Choice** — [[link](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)] · core · via: AIDAS Values & Pluralism
- **If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task** — [[link](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)] · core · via: AIDAS Values & Pluralism
- **Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.** — [[link](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)] · core · via: Alignment Goal Survey
- **Kush R. Varshney. XRDS 2019.** — [[link](https://krvarshney.github.io/)] · adjacent · via: Awesome LLM Safety
- **Kush R. Varshney. XRDS 2019.** — [[link](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)] · adjacent · via: Awesome LLM Safety
- **Leaderboard** — [[link](http://115.182.62.166:18000/)] · core · via: Alignment Goal Survey, Awesome LLM Datasets
- **Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice** — [[link](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)] · core · via: AIDAS Values & Pluralism
- **Liberals and conservatives rely on different sets of moral foundations** — [[link](https://pubmed.ncbi.nlm.nih.gov/19379034/)] · core · via: AIDAS Values & Pluralism
- **Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002.** — [[link](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)] · core · via: Alignment Goal Survey
- **lit.eecs.umich.edu** — [[link](https://lit.eecs.umich.edu/downloads.html)] · adjacent · via: LLM Social Science
- **Manipulation of Voting Schemes: A General Result** — [[link](https://jstor.org/stable/1914083)] · core · via: AIDAS Values & Pluralism
- **Mapping and interpreting cultural differences around the world** — [[link](https://researchgate.net/publication/265596552)] · core · via: AIDAS Values & Pluralism
- **Measuring Perceived Slant in Large Language Models Through User Evaluations** — [[link](https://modelslant.com/paper.pdf)] · core · via: Pluralistic Alignment
- **Measuring the Refined Theory of Individual Values in 49 Cultural Groups** — [[link](https://researchgate.net/publication/349058866)] · core · via: AIDAS Values & Pluralism
- **Mental representations of social values.** — [[link](https://psycnet.apa.org/record/2012-14612-001)] · core · via: AIDAS Values & Pluralism
- **Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies** — [[link](https://jstor.org/stable/j.ctv10vm2ns)] · core · via: AIDAS Values & Pluralism
- **Modernization, Cultural Change, and Democracy** — [[link](https://researchgate.net/publication/230557603)] · core · via: AIDAS Values & Pluralism
- **Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism** — [[link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2184440)] · core · via: AIDAS Values & Pluralism
- **NeurIPS 2025 Tutorial: Human-AI Alignment** — [[link](https://hai-alignment-course.github.io/tutorial/)] · core · via: AIDAS Values & Pluralism
- **On the Rationale of Group Decision-making** — [[link](https://jstor.org/stable/1825026)] · core · via: AIDAS Values & Pluralism
- **Perils and opportunities in using large language models in psychological research** — [[link](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)] · adjacent · via: LLM Social Science
- **Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science** — [[link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)] · core · via: LLM Psychometrics
- **Pew Researcj Center's Global Attitudes Surveys (GAS)** — [[link](https://pewresearch.org/)] · core · via: Alignment Goal Survey
- **Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449** — [[link](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)] · core · via: STONIC bibliography
- **Refining the theory of basic individual values** — [[link](https://pubmed.ncbi.nlm.nih.gov/22823292/)] · core · via: AIDAS Values & Pluralism
- **Rokeach value survey. Rokeach et al. The nature of human values. 1967.** — [[link](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)] · core · via: Alignment Goal Survey
- **Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.** — [[link](https://maartensap.com/social-bias-frames/)] · core · via: Alignment Goal Survey
- **Social chemistry 101: Learning to reason about social and moral norms. Forbes et al. arXiv 2020.** — [[link](https://maxwellforbes.com/social-chemistry/)] · core · via: Alignment Goal Survey, Awesome LLM Safety
- **Social Choice and Individual Values** — [[link](https://jstor.org/stable/j.ctt1nqb90)] · core · via: AIDAS Values & Pluralism
- **Social Choice Theory (in Stanford Encyclopedia of Philosophy)** — [[link](https://plato.stanford.edu/entries/social-choice/)] · core · via: AIDAS Values & Pluralism
- **Stanford 2025: Human-Centered LLMs (CS329X)** — [[link](https://web.stanford.edu/class/cs329x/)] · core · via: AIDAS Values & Pluralism
- **Stanford 2025: Machine Learning from Human Preferences (CS329H)** — [[link](https://web.stanford.edu/class/cs329h/)] · core · via: AIDAS Values & Pluralism
- **Steerable Alignment with Conditional Multiobjective Preference Optimization** — [[link](https://dspace.mit.edu/handle/1721.1/156747)] · core · via: Pluralistic Alignment
- **Survey of Cultural Awareness in Language Models: Text and Beyond Open Access** — [[link](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)] · core · via: Pluralistic Alignment
- **The Impossibility of a Paretian Liberal** — [[link](https://jstor.org/stable/1829633)] · core · via: AIDAS Values & Pluralism
- **The Morality of Freedom** — [[link](https://academic.oup.com/book/9926)] · core · via: AIDAS Values & Pluralism
- **The Morality of Pluralism** — [[link](https://jstor.org/stable/j.ctt7smh7)] · core · via: AIDAS Values & Pluralism
- **The Morals of Modernity** — [[link](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)] · core · via: AIDAS Values & Pluralism
- **The nature of human values.** — [[link](https://psycnet.apa.org/record/2011-15663-000)] · core · via: AIDAS Values & Pluralism
- **The Right and the Good** — [[link](https://academic.oup.com/book/27608)] · core · via: AIDAS Values & Pluralism
- **The Righteous Mind** — [[link](https://righteousmind.com/)] · core · via: AIDAS Values & Pluralism
- **The Theory of Communicative Action** — [[link](https://philpapers.org/rec/HABTTO)] · core · via: AIDAS Values & Pluralism
- **The theory of dyadic morality: Reinventing moral judgment by redefining harm.** — [[link](https://psycnet.apa.org/record/2018-02142-002)] · core · via: AIDAS Values & Pluralism
- **Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022.** — [[link](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)] · core · via: Alignment Goal Survey
- **Towards Pluralistic Alignment of LLMs: A Comprehensive Survey** — [[link](https://preprints.org/manuscript/202603.1876)] · core · via: AIDAS Values & Pluralism
- **Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop** — [[link](https://openaccess.city.ac.uk/id/eprint/31381/)] · adjacent · via: LLM Social Science
- **Two Concepts of Liberty** — [[link](https://academic.oup.com/book/7968/chapter-abstract/153281672)] · core · via: AIDAS Values & Pluralism
- **Universals in the content and structure of values: Theoretical advances and empirical tests in 20 countries.** — [[link](https://psycnet.apa.org/record/2003-00370-001)] · core · via: AIDAS Values & Pluralism
- **Value Pluralism (in Stanford Encyclopedia of Philosophy)** — [[link](https://plato.stanford.edu/entries/value-pluralism/)] · core · via: AIDAS Values & Pluralism

<!-- complete-catalog:end -->

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
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_catalog.py
```

### License

Original code is MIT. Original structured metadata and documentation are CC BY
4.0. Linked papers, datasets, models, and third-party repositories retain their
own licenses and copyright.
