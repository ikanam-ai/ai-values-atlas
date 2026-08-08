<div align="center">

<img src="assets/atlas-header.svg" width="100%" alt="AI Values Atlas — open research field guide" />

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
  <a href="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml"><img alt="validation" src="https://img.shields.io/github/actions/workflow/status/ikanam-ai/ai-values-atlas/validate.yml?style=for-the-badge&label=validated"></a>
  <a href="#complete-catalog"><img alt="resources" src="https://img.shields.io/badge/resources-997-136f58?style=for-the-badge"></a>
  <a href="#complete-catalog"><img alt="publications" src="https://img.shields.io/badge/publication%20links-760-0d3f35?style=for-the-badge"></a>
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
- [Complete catalog — all 997 links](#complete-catalog)
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
| [🗺️ Surveys, reviews, and field overviews](#catalog-surveys-reviews-and-field-overviews) | 48 |
| [🧭 Foundations and value theory](#catalog-foundations-and-value-theory) | 7 |
| [🗂️ Datasets and benchmarks](#catalog-datasets-and-benchmarks) | 100 |
| [🔬 Reliability, validity, and auditing](#catalog-reliability-validity-and-auditing) | 17 |
| [🎯 Choice, action, and behavioral consistency](#catalog-choice-action-and-behavioral-consistency) | 15 |
| [🌍 Culture, language, and pluralism](#catalog-culture-language-and-pluralism) | 103 |
| [🗣️ Preferences, opinions, and social simulation](#catalog-preferences-opinions-and-social-simulation) | 111 |
| [⚖️ Moral reasoning and value understanding](#catalog-moral-reasoning-and-value-understanding) | 63 |
| [🧰 Alignment, steering, and preferences](#catalog-alignment-steering-and-preferences) | 127 |
| [📐 Value representation and model internals](#catalog-value-representation-and-model-internals) | 44 |
| [📏 Measurement and profiling](#catalog-measurement-and-profiling) | 85 |
| [📎 Other and adjacent value research](#catalog-other-and-adjacent-value-research) | 40 |

<sub>Scope labels distinguish value-focused `core` records from broader `adjacent` work. The final label lists the source catalogs in which each record was discovered.</sub>

### 📚 Publications by research topic

<a id="catalog-surveys-reviews-and-field-overviews"></a>

#### 🗺️ Surveys, reviews, and field overviews

<sub>48 publications</sub>

- **[A roadmap for evaluating moral competence in large language models](https://nature.com/articles/s41586-025-10021-1)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[A Survey of Progress in LLM Alignment from the Perspective of Reward Design](https://ieeexplore.ieee.org/abstract/document/11361384)** <sub>publication · core · pluralistic-alignment</sub>
- **[A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[A Survey on Human-Centric LLMs](https://arxiv.org/abs/2411.14491)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications](https://arxiv.org/abs/2503.17003)** <sub>publication · adjacent · personalized-alignment</sub>
- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)** <sub>publication · core · aidas-llm-values-pluralism, personalized-alignment, pluralistic-alignment</sub>
- **[AI Alignment and Social Choice: Fundamental Limitations and Policy Implications](https://arxiv.org/abs/2310.16048)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[AI Alignment From Social Choice Perspectives](https://arxiv.org/abs/2606.21550)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment, valuebyte-llm-social-science</sub>
- **[Aligning Large Language Models with Human: A Survey](https://arxiv.org/abs/2307.12966)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap](https://arxiv.org/abs/2508.18646)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural Bias and Cultural Alignment of Large Language Models](https://arxiv.org/abs/2311.14096)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation](https://arxiv.org/abs/2509.08858)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens](https://arxiv.org/abs/2508.16982)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents](https://arxiv.org/abs/2412.03563)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models](https://arxiv.org/abs/2308.12014)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications](https://arxiv.org/abs/2505.00049)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges](https://arxiv.org/abs/2507.19364)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://arxiv.org/abs/2402.01680)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement](https://arxiv.org/abs/2505.08245)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Large language models empowered agent-based modeling and simulation: a survey and perspectives](https://nature.com/articles/s41599-024-03611-3)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences](https://arxiv.org/abs/2606.07629)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency](https://link.springer.com/article/10.1007/s12559-026-10568-9)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLM Social Simulations Are a Promising Research Method](https://arxiv.org/abs/2504.02234)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLM-Based Social Simulations Require a Boundary](https://arxiv.org/abs/2506.19806)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods](https://arxiv.org/abs/2412.05579)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs](https://aclanthology.org/2025.findings-acl.1246/)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs](https://arxiv.org/abs/2511.01864)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment](https://arxiv.org/abs/2602.03003)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior](https://arxiv.org/abs/2511.14476)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback](https://arxiv.org/abs/2303.05453)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)** <sub>publication · core · personalized-alignment, pluralistic-alignment</sub>
- **[Personalized Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2412.02142)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Position: AI Agents Are Not (Yet) a Panacea for Social Simulation](https://arxiv.org/abs/2603.00113)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Position: Towards Bidirectional Human-AI Alignment](https://arxiv.org/abs/2406.09264)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations](https://aclanthology.org/2024.lrec-main.1192/)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Simulating Society Requires Simulating Thought](https://arxiv.org/abs/2506.06958)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback](https://arxiv.org/abs/2404.10271)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits](https://arxiv.org/abs/2605.18890)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The benefits, risks and bounds of personalizing the alignment of large language models to individuals](https://nature.com/articles/s42256-024-00820-y)** <sub>publication · adjacent · personalized-alignment</sub>
- **[The Mind in the Machine: A Survey of Incorporating Psychological Theories in LLMs](https://arxiv.org/abs/2505.00003)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm](https://arxiv.org/abs/2406.18682)** <sub>publication · adjacent · personalized-alignment</sub>
- **[The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment](https://arxiv.org/abs/2412.16468)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[The threat of analytic flexibility in using large language models to simulate human data: A call to attention](https://arxiv.org/abs/2509.13397)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://aclanthology.org/2024.findings-emnlp.969/)** <sub>publication · adjacent · personalized-alignment</sub>
- **[When large language models meet personalization: perspectives of challenges and opportunities](https://doi.org/10.1007/s11280-024-01276-1)** <sub>publication · adjacent · personalized-alignment</sub>

<a id="catalog-foundations-and-value-theory"></a>

#### 🧭 Foundations and value theory

<sub>7 publications</sub>

- **[Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values](https://doi.org/10.2196/55988)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Axioms for AI Alignment from Human Feedback](https://arxiv.org/abs/2405.14758)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement](https://doi.org/10.1177/0022022101032005001)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Moral foundations theory: The pragmatic validity of moral pluralism. Graham et al. Advances in experimental social psychology, 2013.](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)** <sub>publication · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[Optimized Distortion in Linear Social Choice](https://arxiv.org/abs/2510.20020)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Representative Social Choice: From Learning Theory to AI Alignment](https://arxiv.org/abs/2410.23953)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Strategy-proofness and Arrow's Conditions](https://sciencedirect.com/science/article/pii/0022053175900502)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-datasets-and-benchmarks"></a>

#### 🗂️ Datasets and benchmarks

<sub>100 publications</sub>

- **[(ETHICS) Aligning AI With Shared Human Values](https://arxiv.org/abs/2008.02275)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey, awesome-llm-safety</sub>
- **[(MoralChoice) Evaluating the Moral Beliefs Encoded in LLMs](https://arxiv.org/abs/2307.14324)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[(NYTBookOpinions) Benchmarking Distributional Alignment of Large Language Models](https://arxiv.org/abs/2411.05403)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[(Valueeval) The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments](https://arxiv.org/abs/2301.13771)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[2020.acl-main.477/](https://aclanthology.org/2020.acl-main.477/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[3539618.3591877](https://dl.acm.org/doi/10.1145/3539618.3591877)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[A Unified Moral-Value Dataset for Instruction Tuning](https://arxiv.org/abs/2607.21279)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://arxiv.org/abs/2305.13300)** <sub>publication · core · pluralistic-alignment</sub>
- **[Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values](https://arxiv.org/abs/2605.10365)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance](https://arxiv.org/abs/2404.01247)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](https://arxiv.org/abs/2502.14083)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models, NeurIPS 2024](https://arxiv.org/abs/2402.11894)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[BBQ: A hand-built bias benchmark for question answering](https://aclanthology.org/2022.findings-acl.165/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Benchmarking Multi-National Value Alignment for Large Language Models](https://arxiv.org/abs/2504.12911)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Benchmarking Overton Pluralism in LLMs](https://arxiv.org/abs/2512.01351)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[Beyond Aesthetics: Cultural Competence in Text-to-Image Models](https://arxiv.org/abs/2407.06863)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Big-Math 2025-2](https://arxiv.org/abs/2502.17387)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys](https://arxiv.org/abs/2401.10352)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models](https://arxiv.org/abs/2506.01495)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs](https://arxiv.org/abs/2510.05154)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can Language Models Reason about Individualistic Human Values and Preferences?](https://aclanthology.org/2025.acl-long.336/)** <sub>publication · core · pluralistic-alignment</sub>
- **[CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models](https://arxiv.org/abs/2405.13974)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models](https://ojs.aaai.org/index.php/AIES/article/view/31710)** <sub>publication · core · pluralistic-alignment</sub>
- **[CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives](https://arxiv.org/abs/2504.10823)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean](https://arxiv.org/abs/2403.06412)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values](https://arxiv.org/abs/2504.05535)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[ComPO: Community Preferences for Language Model Personalization](https://aclanthology.org/2025.naacl-long.419/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Culturally Aware Natural Language Inference](https://aclanthology.org/2023.findings-emnlp.509/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios](https://arxiv.org/abs/2607.19834)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Datasheets for datasets](https://doi.org/10.1145/3458723)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://arxiv.org/abs/2509.17399)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures](https://arxiv.org/abs/2403.14651)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English](https://arxiv.org/abs/2203.14498)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Evaluating and Inducing Personality in Pre-trained Language Models](https://arxiv.org/abs/2206.07550)** <sub>publication · core · pluralistic-alignment</sub>
- **[Evaluating the Prompt Steerability of Large Language Models](https://arxiv.org/abs/2411.12405)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370)** <sub>publication · core · pluralistic-alignment</sub>
- **[Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark](https://arxiv.org/abs/2603.17838)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis](https://arxiv.org/abs/2308.16705)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture](https://aclanthology.org/2024.emnlp-main.1063/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models](https://aclanthology.org/2023.findings-acl.631/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[GeoDE: a Geographically Diverse Evaluation Dataset for Object Recognition](https://arxiv.org/abs/2301.02560)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking](https://arxiv.org/abs/2502.13766)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Global Voices, Local Biases: Socio-Cultural Prejudices across Languages](https://arxiv.org/abs/2310.17586)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter, ACL 2025 Outstanding Paper](https://arxiv.org/abs/2411.15462)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge](https://aclanthology.org/2024.findings-acl.666/)** <sub>publication · core · pluralistic-alignment</sub>
- **[LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces](https://arxiv.org/abs/2503.01894)** <sub>publication · core · pluralistic-alignment</sub>
- **[LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models](https://arxiv.org/abs/2505.00853)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks](https://arxiv.org/abs/2407.03791)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking](https://arxiv.org/abs/2402.09369)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation](https://arxiv.org/abs/2506.19073)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment](https://journals.sagepub.com/doi/10.1177/1948550619876629)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral foundations twitter corpus: A collection of 35k tweets annotated for moral sentiment. Hoover et al. Social Psychological and Personality Science 2020.](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)** <sub>publication · core · alignment-goal-survey</sub>
- **[Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences](https://arxiv.org/abs/2012.15738)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey</sub>
- **[MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes](https://arxiv.org/abs/2510.16380)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Multi-lingual and Multi-cultural Figurative Language Understanding](https://arxiv.org/abs/2305.16171)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision-Language Models](https://aclanthology.org/2025.naacl-long.490/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Navigating the Cultural Kaleidoscope: A Hitchhiker’s Guide to Sensitivity in Large Language Models](https://aclanthology.org/2025.naacl-long.388/)** <sub>publication · core · pluralistic-alignment</sub>
- **[NLPositionality: Characterizing Design Biases of Datasets and Models](https://aclanthology.org/2023.acl-long.505/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[NormBank: A Knowledge Bank of Situational Social Norms](https://aclanthology.org/2023.acl-long.429/)** <sub>publication · core · pluralistic-alignment</sub>
- **[NormBank: A Knowledge Bank of Situational Social Norms](https://arxiv.org/abs/2305.17008)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly](https://arxiv.org/abs/2210.08604)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[NoveltyBench: Evaluating Language Models for Humanlike Diversity](https://arxiv.org/abs/2504.05228)** <sub>publication · core · pluralistic-alignment</sub>
- **[PerSpectra: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments](https://arxiv.org/abs/2602.08716)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[PLURAL: A Global Dataset for Value Alignment](https://arxiv.org/abs/2607.08034)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm](https://arxiv.org/abs/2601.08951)** <sub>publication · core · pluralistic-alignment</sub>
- **[Polar: A Benchmark for Evaluating Political Bias in LLMs](https://arxiv.org/abs/2606.12922)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Process for adapting language models to society (palms) with values-targeted datasets. Solaiman et al. Neurips 2021.](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)** <sub>publication · core · alignment-goal-survey</sub>
- **[ProsocialDialog: A Prosocial Backbone for Conversational Agents](https://arxiv.org/abs/2205.12688)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Re-contextualizing Fairness in NLP: The Case of India](https://arxiv.org/abs/2209.12226)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations](https://aclanthology.org/2024.findings-naacl.196/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.](https://arxiv.org/abs/2210.10045)** <sub>publication · core · alignment-goal-survey</sub>
- **[SafeWorld: Geo-Diverse Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes](https://arxiv.org/abs/2008.09094)** <sub>publication · core · aidas-llm-values-pluralism, awesome-llm-safety</sub>
- **[Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396)** <sub>publication · core · alignment-goal-survey</sub>
- **[SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models](https://arxiv.org/abs/2305.11840)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Social Chemistry 101: Learning to Reason about Social and Moral Norms](https://arxiv.org/abs/2011.00620)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey, awesome-llm-safety</sub>
- **[STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models](https://arxiv.org/abs/2505.20645)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Moral Foundations Reddit Corpus](https://arxiv.org/abs/2208.05545)** <sub>publication · core · aidas-llm-values-pluralism, awesome-llm-safety</sub>
- **[The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems](https://aclanthology.org/2022.acl-long.261/)** <sub>publication · core · pluralistic-alignment</sub>
- **[The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems](https://arxiv.org/abs/2204.03021)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey, awesome-llm-safety</sub>
- **[The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective](https://arxiv.org/abs/2602.17283)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models](https://arxiv.org/abs/2510.05465)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation](https://aclanthology.org/2025.acl-demo.64/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models](https://aclanthology.org/2024.acl-long.111/)** <sub>publication · core · pluralistic-alignment, stonic-manuscript-bibliography</sub>
- **[ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022](https://ojs.aaai.org/index.php/AAAI/article/view/21368)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Valuenet: A new dataset for human value driven dialogue system. Qiu et al. AAAI 2022.](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)** <sub>publication · core · alignment-goal-survey</sub>
- **[Vision-Language Models under Cultural and Inclusive Considerations](https://arxiv.org/abs/2407.06177)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Visually Grounded Reasoning across Languages and Cultures](https://arxiv.org/abs/2109.13238)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](https://aclanthology.org/2025.acl-long.1119/)** <sub>publication · core · pluralistic-alignment</sub>
- **[VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](https://arxiv.org/abs/2502.13775)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses](https://arxiv.org/abs/2607.26348)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548)** <sub>publication · core · pluralistic-alignment</sub>
- **[Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models](https://arxiv.org/abs/2507.13383)** <sub>publication · core · pluralistic-alignment</sub>
- **[WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://arxiv.org/abs/2410.12705)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models](https://aclanthology.org/2024.lrec-main.1539/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad](https://arxiv.org/abs/2601.14063)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-reliability-validity-and-auditing"></a>

#### 🔬 Reliability, validity, and auditing

<sub>17 publications</sub>

- **[A large-scale replication of scenario-based experiments in psychology and management using large language models, 2025.08, Nature Computational Science](https://nature.com/articles/s43588-025-00840-7)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, 2025.07, ACL 2025 Best Paper](https://aclanthology.org/2025.acl-long.1454/)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[A validity-guided workflow for robust large language model research in psychology](https://arxiv.org/abs/2507.04491)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents](https://arxiv.org/abs/2602.18462)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing](https://doi.org/10.1145/3351095.3372873)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality](https://arxiv.org/abs/2510.11254)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations](https://arxiv.org/abs/2605.30258)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology](https://arxiv.org/abs/2506.16697)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Large Language Models are not Fair Evaluators](https://aclanthology.org/2024.acl-long.511/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Large language models that replace human participants can harmfully misportray and flatten identity groups, 2025.03, Nature Machine Intelligence](https://nature.com/articles/s42256-025-00986-z)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Larger and more instructable language models become less reliable, 2024.10, Nature](https://nature.com/articles/s41586-024-07930-y)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History](https://arxiv.org/abs/2508.04826)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[POSIX: A Prompt Sensitivity Index For Large Language Models](https://arxiv.org/abs/2410.02185)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Psychometric item validation using virtual respondents with trait-response mediators](https://arxiv.org/abs/2507.05890)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Revisiting the Reliability of Psychological Scales on Large Language Models, EMNLP 2024](https://arxiv.org/abs/2305.19926)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments, NAACL 2024](https://arxiv.org/abs/2311.09718)** <sub>publication · core · valuebyte-llm-psychometrics</sub>

<a id="catalog-choice-action-and-behavioral-consistency"></a>

#### 🎯 Choice, action, and behavioral consistency

<sub>15 publications</sub>

- **[\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms](https://arxiv.org/abs/2312.15907)** <sub>publication · adjacent · awesome-llm-safety, valuebyte-llm-social-science</sub>
- **[Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents](https://arxiv.org/abs/2604.27699)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior](https://nature.com/articles/s41562-024-01938-0.pdf)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[How large language models can reshape collective intelligence, 2024.09, Nature Human Behavior](https://nature.com/articles/s41562-024-01959-9)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1562/)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?](https://aclanthology.org/2025.emnlp-main.154/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies](https://arxiv.org/abs/2511.05018)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned. Ganguliet al. arXiv 2022.](https://arxiv.org/abs/2209.07858)** <sub>publication · core · alignment-goal-survey</sub>
- **[Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies](https://arxiv.org/abs/2606.12369)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.](https://arxiv.org/abs/1911.03891)** <sub>publication · core · alignment-goal-survey</sub>
- **[The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas](https://aclanthology.org/2025.emnlp-main.806/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[The theory of planned behavior](https://sciencedirect.com/science/article/pii/074959789190020T)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Training a helpful and harmless assistant with reinforcement learning from human feedback. Bai et al. arXiv 2022.](https://arxiv.org/abs/2204.05862)** <sub>publication · core · alignment-goal-survey</sub>
- **[Training language models to follow instructions with human feedback. Ouyang et al. Neurips 2022.](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)** <sub>publication · core · alignment-goal-survey</sub>
- **[What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios](https://aclanthology.org/2025.coling-main.317/)** <sub>publication · core · stonic-manuscript-bibliography</sub>

<a id="catalog-culture-language-and-pluralism"></a>

#### 🌍 Culture, language, and pluralism

<sub>103 publications</sub>

- **['Too much alignment; not enough culture': Re-balancing Cultural Alignment Practices in LLMs](https://arxiv.org/abs/2509.26167)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[(GlobalOpinionQA) Towards Measuring the Representation of Subjective Global Opinions in Language Models](https://arxiv.org/abs/2306.16388)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey, pluralistic-alignment, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities](https://arxiv.org/abs/2601.12962)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[An Evaluation of Cultural Value Alignment in LLM](https://arxiv.org/abs/2504.08863)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks](https://arxiv.org/abs/2505.23820)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Assessing Cross-Cultural Alignment between ChatGPT and Human Societies](https://arxiv.org/abs/2303.17466)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[Assessing LLMs for Moral Value Pluralism](https://arxiv.org/abs/2312.10075)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Attributing Culture-Conditioned Generations to Pretraining Corpora](https://arxiv.org/abs/2412.20760)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs](https://arxiv.org/abs/2601.15755)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages](https://arxiv.org/abs/2406.09948)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://aclanthology.org/2025.emnlp-main.2/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://arxiv.org/abs/2502.08045)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench](https://arxiv.org/abs/2504.01127)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CARE: Multilingual Human Preference Learning for Cultural Awareness](https://arxiv.org/abs/2504.05154)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CAReDiO: Enhancing Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization](https://arxiv.org/abs/2504.08820)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CCBench: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries](https://arxiv.org/abs/2607.05405)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models](https://arxiv.org/abs/2311.16421)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Challenges and Strategies in Cross-Cultural NLP](https://arxiv.org/abs/2203.10020)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues](https://arxiv.org/abs/2603.20229)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[code and data](https://arxiv.org/abs/2410.12880)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Coherence Maximization Improves Pluralistic Alignment](https://arxiv.org/abs/2606.03110)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis](https://arxiv.org/abs/2511.17256)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CulFiT: Fine-grained Cultural-aware LLM Training via Multilingual Critique Data Synthesis](https://arxiv.org/abs/2505.19484)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural Adaptation in Large Language Models for Political Discourse](https://arxiv.org/abs/2605.23332)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural Alignment in Large Language Models Using Soft Prompt Tuning](https://arxiv.org/abs/2503.16094)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions](https://arxiv.org/abs/2309.12342)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural bias and cultural alignment of large language models](https://doi.org/10.1093/pnasnexus/pgae346)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting](https://arxiv.org/abs/2406.11661)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Cultural Learning-Based Culture Adaptation of Language Models](https://aclanthology.org/2025.acl-long.156/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Cultural Learning-Based Culture Adaptation of Language Models (CLCA)](https://arxiv.org/abs/2504.02953)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette](https://arxiv.org/abs/2412.11167)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment, valuebyte-llm-social-science</sub>
- **[Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek](https://arxiv.org/abs/2505.17112)** <sub>publication · core · aidas-llm-values-pluralism, stonic-manuscript-bibliography, valuebyte-llm-psychometrics</sub>
- **[Cultural Value Alignment Via Latent Activation Steering in Large Language Models](https://arxiv.org/abs/2605.26365)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark](https://arxiv.org/abs/2410.02677)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art](https://arxiv.org/abs/2406.03930)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge](https://arxiv.org/abs/2404.06664)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Culture is Not Trivia: Sociocultural Theory for Cultural NLP](https://arxiv.org/abs/2502.12057)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CultureBank: An Online Community-Driven Knowledge Base toward Culturally Aware Language Technologies](https://arxiv.org/abs/2404.15238)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs](https://arxiv.org/abs/2606.01879)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://arxiv.org/abs/2402.10946)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://arxiv.org/abs/2405.15145)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis](https://arxiv.org/abs/2509.10886)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters](https://arxiv.org/abs/2601.04885)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs](https://arxiv.org/abs/2511.12014)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions](https://arxiv.org/abs/2510.21977)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook](https://arxiv.org/abs/2604.06210)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained LMs](https://arxiv.org/abs/2306.05076)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms](https://arxiv.org/abs/2507.20264)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in](https://arxiv.org/abs/2404.18460)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[EtiCor: Corpus for Analyzing LLMs for Etiquettes](https://arxiv.org/abs/2310.18974)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment](https://arxiv.org/abs/2509.21798)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Evaluating Pluralism in LLMs through Latent Perspectives](https://arxiv.org/abs/2606.13254)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://arxiv.org/abs/2510.04045)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Exploring Cultural Variations in Moral Judgments with Large Language Models](https://arxiv.org/abs/2506.12433)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Extrinsic Evaluation of Cultural Competence in Large Language Models](https://arxiv.org/abs/2406.11565)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://arxiv.org/abs/2406.17692)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs](https://arxiv.org/abs/2505.16408)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Having Beer after Prayer? Measuring Cultural Bias in Large Language Models](https://arxiv.org/abs/2305.14456)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens](https://arxiv.org/abs/2510.05931)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective](https://arxiv.org/abs/2502.17773)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions](https://arxiv.org/abs/2406.14805)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Improving Cross-Cultural Survey Simulation with Calibrated Value Personas](https://arxiv.org/abs/2605.16193)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Investigating Cultural Alignment of Large Language Models](https://arxiv.org/abs/2402.13231)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions](https://arxiv.org/abs/2502.16761)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Large Language Models as Superpositions of Cultural Perspectives](https://arxiv.org/abs/2307.07870)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Legal Theory for Pluralistic Alignment](https://arxiv.org/abs/2410.17271)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation](https://arxiv.org/abs/2604.08797)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?](https://arxiv.org/abs/2503.15003)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output](https://arxiv.org/abs/2411.06032)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Made-in China, Thinking in America: U.S. Values Persist in Chinese LLMs](https://arxiv.org/abs/2512.13723)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness](https://arxiv.org/abs/2502.09637)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Meta-Learning Preferences for Multilingual LLM Alignment](https://arxiv.org/abs/2607.13315)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models](https://arxiv.org/abs/2602.22475)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate](https://arxiv.org/abs/2601.12091)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs](https://arxiv.org/abs/2502.16534)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Multilingual Language Models are not Multicultural: A Case Study in Emotion](https://arxiv.org/abs/2307.01370)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities](https://arxiv.org/abs/2505.18383)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://arxiv.org/abs/2404.12464)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp, valuebyte-llm-social-science</sub>
- **[On the steerability of large language models toward data-driven personas](https://arxiv.org/abs/2311.04978)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Overton Pluralistic Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2602.20759)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://arxiv.org/abs/2509.10685)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Plurals: A System for Guiding LLMs Via Simulated Social Ensembles](https://arxiv.org/abs/2409.17213)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[POW: Political Overton Windows of Large Language Models](https://arxiv.org/abs/2509.08853)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Probing Pre-Trained Language Models for Cross-Cultural Differences in Values](https://arxiv.org/abs/2203.13722)** <sub>publication · core · aidas-llm-values-pluralism, alignment-goal-survey, awesome-cultural-nlp</sub>
- **[Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble](https://arxiv.org/abs/2509.11311)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs](https://arxiv.org/abs/2503.08688)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[RLHF: A Comprehensive Survey for Cultural, Multimodal and Low-Latency Alignment Methods](https://arxiv.org/abs/2511.03939)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Self-Pluralising Culture Alignment for Large Language Models (CultureSPA)](https://arxiv.org/abs/2410.12971)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://arxiv.org/abs/2502.07068)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Steerable Cultural Preference Optimization of Reward Models](https://arxiv.org/abs/2606.18606)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Steering LLMs for Culturally Localized Generation](https://arxiv.org/abs/2603.23301)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Survey of Cultural Awareness in Language Models: Text and Beyond](https://arxiv.org/abs/2411.00860)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp, valuebyte-llm-social-science</sub>
- **[The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning](https://arxiv.org/abs/2405.12744)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models](https://arxiv.org/abs/2604.20225)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning](https://arxiv.org/abs/2601.21700)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Toward Culturally Grounded Natural Language Processing](https://arxiv.org/abs/2603.26013)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Towards Measuring and Modeling "Culture" in LLMs: A Survey](https://arxiv.org/abs/2403.15412)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements](https://arxiv.org/abs/2602.12878)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value kaleidoscope: engaging AI with pluralistic human values, rights, and duties](https://doi.org/10.1609/aaai.v38i18.29970)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise](https://arxiv.org/abs/2506.00242)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[WorldValuesBench: A Large-Scale Benchmark for Multi-Cultural Value Awareness of Language Models](https://arxiv.org/abs/2404.16308)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity](https://arxiv.org/abs/2605.05662)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-preferences-opinions-and-social-simulation"></a>

#### 🗣️ Preferences, opinions, and social simulation

<sub>111 publications</sub>

- **[(ANES) CommunityLM: Probing Partisan Worldviews from Language Models, COLING 2022](https://arxiv.org/abs/2209.07065)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ANES) Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information](https://arxiv.org/abs/2402.18144)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ANES) Representation Bias in Political Sample Simulations with Large Language Models](https://arxiv.org/abs/2407.11409)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ANES) Unpacking Political Bias in Large Language Models: A Cross-Model Comparison on U.S. Politics](https://arxiv.org/abs/2412.16746)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Culture) Cultural tendencies in generative AI, 2025.06, Nature Human Behaviour](https://nature.com/articles/s41562-025-02242-1)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(GLES) Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study](https://arxiv.org/abs/2412.13169)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(GLES) Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction](https://arxiv.org/abs/2502.16280)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(GLES) Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion](https://arxiv.org/abs/2407.08563)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction](https://arxiv.org/abs/2305.09620)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys](https://arxiv.org/abs/2405.19323)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs](https://arxiv.org/abs/2503.13149)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases](https://arxiv.org/abs/2502.18282)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Demonstrations of the Potential of AI-based Political Issue Polling, 2023.07, Harvard Data Science Review (HDSR)](https://arxiv.org/abs/2307.04781)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models, ACL 2023](https://arxiv.org/abs/2305.08283)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?, 2023.07, Digital Society](https://link.springer.com/article/10.1007/s44206-023-00054-2)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance](https://arxiv.org/abs/2502.08395)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Large Language Models Can Be Used to Estimate the Latent Positions of Politicians](https://arxiv.org/abs/2303.12057)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Linear Representations of Political Perspective Emerge in Large Language Models](https://arxiv.org/abs/2503.02080)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs, NAACL 2024 (Short Paper)](https://arxiv.org/abs/2403.13592)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Questioning the Survey Responses of Large Language Models, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas](https://arxiv.org/abs/2412.14843)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias, arXiv 2026.01](https://arxiv.org/abs/2601.06194)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models, ACL 2024](https://arxiv.org/abs/2402.16786)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(PCT) PRISM: A Methodology for Auditing Biases in Large Language Models](https://arxiv.org/abs/2410.18906)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) Revealing Fine-Grained Values and Opinions in Large Language Models, EMNLP 2024 Findings](https://arxiv.org/abs/2406.19238)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation](https://arxiv.org/abs/2301.01768)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) The Self-Perception and Political Biases of ChatGPT](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations](https://arxiv.org/abs/2505.14106)** <sub>publication · adjacent · personalized-alignment</sub>
- **[AI PERSONA: Towards Life-long Personalization of LLMs](https://arxiv.org/abs/2412.13103)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Aligning Language Models from User Interactions](https://arxiv.org/abs/2603.12273)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Aligning Large Language Models with Diverse Political Viewpoints](https://aclanthology.org/2024.emnlp-main.412/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Aligning LLMs with Individual Preferences via Interaction](http://arxiv.org/abs/2410.03642)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Aligning to Thousands of Preferences via System Message Generalization](https://arxiv.org/abs/2405.17977)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Aligning VLM Assistants with Personalized Situated Cognition](https://arxiv.org/abs/2506.00930)** <sub>publication · adjacent · personalized-alignment</sub>
- **[AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment](https://arxiv.org/abs/2603.26680)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://arxiv.org/abs/2502.19148)** <sub>publication · adjacent · personalized-alignment</sub>
- **[APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings](https://arxiv.org/abs/2605.21063)** <sub>publication · adjacent · personalized-alignment</sub>
- **[APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents](https://arxiv.org/abs/2605.27419)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization](https://aclanthology.org/2024.findings-emnlp.398/)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization](https://arxiv.org/abs/2606.02300)** <sub>publication · adjacent · personalized-alignment</sub>
- **[COMPO: Community Preferences for Language Model Personalization](https://arxiv.org/abs/2410.16027)** <sub>publication · adjacent · personalized-alignment, valuebyte-llm-social-science</sub>
- **[Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements](http://arxiv.org/abs/2410.08968)** <sub>publication · adjacent · personalized-alignment</sub>
- **[CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors](https://arxiv.org/abs/2604.14773)** <sub>publication · adjacent · personalized-alignment</sub>
- **[CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering](https://arxiv.org/abs/2507.04756)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling](https://arxiv.org/abs/2607.18310)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://arxiv.org/abs/2309.03126)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Drift: Decoding-time Personalized Alignments with Implicit User Preferences](https://arxiv.org/abs/2502.14289)** <sub>publication · adjacent · personalized-alignment</sub>
- **[EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents](https://arxiv.org/abs/2606.26883)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance](https://arxiv.org/abs/2505.16348)** <sub>publication · adjacent · personalized-alignment</sub>
- **[EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?](https://arxiv.org/abs/2503.16545)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1](https://arxiv.org/abs/2607.20589)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals](https://arxiv.org/abs/2505.18071)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Few-shot Personalization of LLMs with Mis-aligned Responses](http://arxiv.org/abs/2406.18678)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment](https://arxiv.org/abs/2503.15463)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning](https://arxiv.org/abs/2605.23382)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes](https://arxiv.org/abs/2605.16303)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users](https://arxiv.org/abs/2606.00728)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment](https://arxiv.org/abs/2505.16610)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](https://arxiv.org/abs/2604.20006)** <sub>publication · adjacent · personalized-alignment</sub>
- **[From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG](https://arxiv.org/abs/2605.18271)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation](https://arxiv.org/abs/2605.24647)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://arxiv.org/abs/2603.16120)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Large Language Models Empowered Personalized Web Agents](https://arxiv.org/abs/2410.17236)** <sub>publication · adjacent · personalized-alignment</sub>
- **[LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education](https://arxiv.org/abs/2410.14012)** <sub>publication · adjacent · personalized-alignment</sub>
- **[MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models](https://arxiv.org/abs/2605.25342)** <sub>publication · adjacent · personalized-alignment</sub>
- **[MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time](https://arxiv.org/abs/2410.14184)** <sub>publication · adjacent · personalized-alignment</sub>
- **[MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning](https://arxiv.org/abs/2505.24846)** <sub>publication · adjacent · personalized-alignment</sub>
- **[More human than human: measuring ChatGPT political bias](https://link.springer.com/article/10.1007/s11127-023-01097-2)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL 2025](https://aclanthology.org/2025.acl-long.1529/)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Opinion dynamics and mutual influence with LLM agents through dialog simulation](https://arxiv.org/abs/2602.12583)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[PAD: Personalized Alignment at Decoding-Time](http://arxiv.org/abs/2410.04070)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](https://arxiv.org/abs/2608.04003)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Persona-Based Simulation of Human Opinion at Population Scale](https://arxiv.org/abs/2603.27056)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement](https://arxiv.org/abs/2402.11060)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment](https://arxiv.org/abs/2504.12663)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time](https://arxiv.org/abs/2506.06254)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization](https://arxiv.org/abs/2506.12915)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants](https://arxiv.org/abs/2506.09902)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized Adaptation via In-Context Preference Learning](https://arxiv.org/abs/2410.14001)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/abs/2604.18943)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment](https://arxiv.org/abs/2603.10009)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/abs/2402.05133)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized LLM Decoding via Contrasting Personal Preference](https://arxiv.org/abs/2506.12109)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization](https://arxiv.org/abs/2604.07343)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging](https://arxiv.org/abs/2310.11564)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning](http://arxiv.org/abs/2408.10075)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PersonalLLM: Tailoring LLMs to Individual Preferences](http://arxiv.org/abs/2409.20296)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PersonaVLM: Long-Term Personalized Multimodal LLMs](https://arxiv.org/abs/2604.13074)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PEToolLLM: Towards Personalized Tool Learning in Large Language Models](https://arxiv.org/abs/2502.18980)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Political-LLM: Large Language Models in Political Science](https://arxiv.org/abs/2412.06864)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[POPI: Personalizing LLMs via Optimized Natural Language Preference Inference](https://arxiv.org/abs/2510.17881)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization](https://arxiv.org/abs/2604.22345)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Preference-Aware Rubric Learning for Personalized Evaluation](https://arxiv.org/abs/2605.31545)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PrefPalette: Personalized Preference Modeling with Latent Attributes](https://arxiv.org/abs/2507.13541)** <sub>publication · adjacent · personalized-alignment</sub>
- **[PRIME: Large Language Model Personalization with Cognitive Memory and Thought Processes](https://arxiv.org/abs/2507.04607)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation](https://arxiv.org/abs/2505.17571)** <sub>publication · adjacent · personalized-alignment</sub>
- **[RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation](https://arxiv.org/abs/2405.00254)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Show, Don't Tell: Aligning Language Models with Demonstrated Feedback](https://arxiv.org/abs/2406.00888)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Silicon Sampling via Cross-Survey Transfer](https://arxiv.org/abs/2607.03091)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Steering Large Language Models for Machine Translation Personalization](https://arxiv.org/abs/2505.16612)** <sub>publication · adjacent · personalized-alignment</sub>
- **[SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs](https://arxiv.org/abs/2506.05598)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment](https://arxiv.org/abs/2505.15456)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures](https://arxiv.org/abs/2605.10991)** <sub>publication · adjacent · personalized-alignment</sub>
- **[The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads](https://arxiv.org/abs/2608.04570)** <sub>publication · adjacent · personalized-alignment</sub>
- **[The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models](https://arxiv.org/abs/2406.11096)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models](https://arxiv.org/abs/2404.16019)** <sub>publication · core · aidas-llm-values-pluralism, awesome-cultural-nlp, personalized-alignment, valuebyte-llm-social-science</sub>
- **[Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning](https://arxiv.org/abs/2503.07018)** <sub>publication · adjacent · personalized-alignment</sub>
- **[Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning](https://arxiv.org/abs/2510.18849)** <sub>publication · adjacent · personalized-alignment</sub>
- **[TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment](https://arxiv.org/abs/2606.01755)** <sub>publication · adjacent · personalized-alignment</sub>
- **[When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation](https://arxiv.org/abs/2505.24613)** <sub>publication · adjacent · personalized-alignment</sub>
- **[When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning](https://arxiv.org/abs/2502.19158)** <sub>publication · adjacent · personalized-alignment</sub>

<a id="catalog-moral-reasoning-and-value-understanding"></a>

#### ⚖️ Moral reasoning and value understanding

<sub>63 publications</sub>

- **[(DIT) Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test](https://arxiv.org/abs/2402.02135)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(DIT) Probing the Moral Development of Large Language Models through Defining Issues Test](https://arxiv.org/abs/2309.13356)** <sub>publication · core · awesome-llm-safety, valuebyte-llm-psychometrics</sub>
- **[(ETHICS) An Evaluation of GPT-4 on the ETHICS Dataset](https://arxiv.org/abs/2309.10492)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ETHICS) Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety, NeurIPS 2022 Workshop](https://arxiv.org/abs/2212.06295)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023](https://dl.acm.org/doi/abs/10.1145/3624918.3625327)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(ETHICS) Inducing Human-like Biases in Moral Reasoning Language Models](https://arxiv.org/abs/2411.15386)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Analyzing the Ethical Logic of Six Large Language Models](https://arxiv.org/abs/2501.08951)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations, AIES 2024](https://ojs.aaai.org/index.php/AIES/article/view/31704)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy, NAACL 2022 Workshop](https://arxiv.org/abs/2205.12771)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Exploring and steering the moral compass of Large Language Models, ICPR 2024](https://arxiv.org/abs/2405.17345)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) M3oralBench: A MultiModal Moral Benchmark for LVLMs](https://arxiv.org/abs/2412.20718)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Moral Foundations of Large Language Models, EMNLP 2024](https://arxiv.org/abs/2310.15337)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(MFT) Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity, ACL 2023 Workshop](https://arxiv.org/abs/2209.12106)** <sub>publication · core · alignment-goal-survey, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(MFT) MoralBench: Moral Evaluation of LLMs](https://arxiv.org/abs/2406.04428)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Towards "Differential AI Psychology" and in-context Value-driven Statement Alignment with Moral Foundations Theory](https://arxiv.org/abs/2408.11415)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models](https://arxiv.org/abs/2412.18863)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, 2025.07, ACL 2025 Best Resource Paper](https://aclanthology.org/2025.acl-long.294/)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment, AIES 2024](https://ojs.aaai.org/index.php/AIES/article/view/31741)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?, C3NLP 2024](https://arxiv.org/abs/2406.16316)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Evaluating Moral Beliefs across LLMs through a Pluralistic Framework](https://arxiv.org/abs/2411.03665)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Evaluating the Moral Beliefs Encoded in LLMs, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper)](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Knowledge of cultural moral norms in large language models, ACL 2023](https://arxiv.org/abs/2306.01857)** <sub>publication · core · awesome-cultural-nlp, valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Large-scale moral machine experiment on large language models](https://arxiv.org/abs/2411.06790)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics](https://arxiv.org/abs/2412.00962)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment](https://arxiv.org/abs/2411.11731)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Normative Evaluation of Large Language Models with Everyday Moral Dilemmas](https://arxiv.org/abs/2501.18081)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(Others & Custom) Potential benefits of employing large language models in research in moral education and development, 2023.01, Journal of Moral Education](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Right vs. Right: Can LLMs Make Tough Choices?](https://arxiv.org/abs/2412.19926)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) SaGE: Evaluating Moral Consistency in Large Language Models, LREC-COLING 2024](https://arxiv.org/abs/2402.13709)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) The Moral Mind(s) of Large Language Models](https://arxiv.org/abs/2412.04476)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making](https://arxiv.org/abs/2410.07304)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models](https://arxiv.org/abs/2311.07792)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) What does AI consider praiseworthy?, 2025.02, AI and Ethics](https://link.springer.com/article/10.1007/s43681-025-00682-z)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment, NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[Aditi Khandelwal et al. EACL 2024.](https://aclanthology.org/2024.eacl-long.176/)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Agent Alignment in Evolving Social Norms](https://arxiv.org/abs/2401.04620)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Can Machines Learn Morality? The Delphi Experiment](https://arxiv.org/abs/2110.07574)** <sub>publication · core · alignment-goal-survey, stonic-manuscript-bibliography</sub>
- **[CrowS-Pairs](https://aclanthology.org/2020.emnlp-main.154/)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life](https://arxiv.org/abs/2410.02683)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment, valuebyte-llm-psychometrics</sub>
- **[Exploring the psychology of GPT-4's Moral and Legal Reasoning](https://arxiv.org/abs/2308.01264)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main](https://arxiv.org/abs/2603.13876)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence](https://nature.com/articles/s42256-024-00969-6)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Irene Solaiman and Christy Dennison. NeurIPS 2021.](https://arxiv.org/abs/2106.10328)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Joshua Landau et al. arXiv 2023.](https://arxiv.org/abs/2302.07459)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Laura Weidinger et al. arXiv 2021.](https://arxiv.org/abs/2112.04359)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Learning norms from stories: A prior for value aligned agents. Nahian et al. AIES 2020.](https://arxiv.org/abs/1912.03553)** <sub>publication · core · alignment-goal-survey</sub>
- **[Moral Foundations of Large Language Models](https://aclanthology.org/2024.emnlp-main.982/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences](https://aclanthology.org/2021.emnlp-main.54/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.](https://arxiv.org/abs/2212.10720)** <sub>publication · core · alignment-goal-survey</sub>
- **[Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.](https://arxiv.org/abs/2305.03047)** <sub>publication · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[Revealing the Pragmatic Dilemma for Moral Reasoning Acquisition in Language Models](https://arxiv.org/abs/2502.16600)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Safety Assessment of Chinese Large Language Models](https://arxiv.org/abs/2304.10436)** <sub>publication · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[SafetyBench 2023-9](https://arxiv.org/abs/2309.07045)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Shamik Roy et al. arXiv 2023.](https://aclanthology.org/2022.nlpcss-1.20/)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Shitong Duan et al. ICLR 2024.](https://openreview.net/pdf)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Social Chemistry 101: Learning to Reason about Social and Moral Norms](https://aclanthology.org/2020.emnlp-main.48/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework](https://aclanthology.org/2025.emnlp-main.1541/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[TRUSTGPT 2023-6](https://arxiv.org/abs/2306.11507)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Utkarsh Agarwal et al. LREC/COLING 2024.](https://aclanthology.org/2024.lrec-main.560/)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf)** <sub>publication · core · alignment-goal-survey</sub>
- **[Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)](https://arxiv.org/abs/2509.17703)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Xi Zhiheng et al. CCL 2023.](https://aclanthology.org/2023.ccl-4.2/)** <sub>publication · adjacent · awesome-llm-safety</sub>

<a id="catalog-alignment-steering-and-preferences"></a>

#### 🧰 Alignment, steering, and preferences

<sub>127 publications</sub>

- **[\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models](https://arxiv.org/abs/2312.12999)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[A general language assistant as a laboratory for alignment. Askell et al. arXiv 2021.](https://arxiv.org/abs/2112.00861)** <sub>publication · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[A Roadmap to Pluralistic Alignment](https://arxiv.org/abs/2402.05070)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy](https://arxiv.org/abs/2605.01642)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[AI Alignment Breaks at the Edge](https://arxiv.org/abs/2602.20042)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Aligning \AI\ With Shared Human Values](https://openreview.net/forum)** <sub>publication · core · aidas-llm-values-pluralism, personalized-alignment, pluralistic-alignment, stonic-manuscript-bibliography, valuebyte-llm-social-science</sub>
- **[Aligning Crowd Feedback via Distributional Preference Reward Modeling](https://arxiv.org/abs/2402.09764)** <sub>publication · core · pluralistic-alignment</sub>
- **[Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning](https://arxiv.org/abs/2311.08385)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping](https://ojs.aaai.org/index.php/AAAI/article/view/41109)** <sub>publication · core · pluralistic-alignment</sub>
- **[Aligning Multimodal LLM with Human Preference: A Survey](https://arxiv.org/abs/2503.14504)** <sub>publication · core · pluralistic-alignment</sub>
- **[Aligning to Thousands of Preferences via System Message Generalization](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective](https://aclanthology.org/2025.findings-acl.1188/)** <sub>publication · core · pluralistic-alignment, stonic-manuscript-bibliography, valuebyte-llm-social-science</sub>
- **[Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards](https://aclanthology.org/2024.acl-long.468/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS 2025 D&B Track Best Paper](https://arxiv.org/abs/2510.22954)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration](https://arxiv.org/abs/2604.13705)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Black-Box Prompt Optimization: Aligning Large Language Models without Model Training](https://aclanthology.org/2024.acl-long.176/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Communication-Efficient Desire Alignment for Proactive Embodied Human–Agent Interaction, ACL 2026 Main (Oral)](https://arxiv.org/abs/2505.22503)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.](https://arxiv.org/abs/2212.08073)** <sub>publication · core · alignment-goal-survey</sub>
- **[Constitutional Value Potentials: reading and steering internal priority margins in language models](https://arxiv.org/abs/2606.15420)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment](https://aclanthology.org/2024.emnlp-main.85/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Controllable Value Alignment in Large Language Models through Neuron-Level Editing](https://arxiv.org/abs/2602.07356)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models](https://arxiv.org/abs/2510.18526)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede’s Cultural Dimensions](https://aclanthology.org/2025.coling-main.567/)** <sub>publication · core · pluralistic-alignment</sub>
- **[CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting](https://arxiv.org/abs/2404.10199)** <sub>publication · core · awesome-cultural-nlp, pluralistic-alignment</sub>
- **[CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies](https://aclanthology.org/2024.findings-emnlp.288/)** <sub>publication · core · pluralistic-alignment</sub>
- **[CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?](https://arxiv.org/abs/2505.23749)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Diverging Preferences: When do Annotators Disagree and do Models Know?](https://arxiv.org/abs/2410.14632)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Diverse Human Value Alignment for Large Language Models via Ethical Reasoning](https://arxiv.org/abs/2511.00379)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning](https://arxiv.org/abs/2603.10588)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping](https://arxiv.org/abs/2605.14420)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Evaluating and Inducing Personality in Pre-trained Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas](https://arxiv.org/abs/2408.06929)** <sub>publication · core · pluralistic-alignment</sub>
- **[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1301/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes](https://arxiv.org/abs/2412.13998)** <sub>publication · core · pluralistic-alignment</sub>
- **[Fine-tuning language models to find agreement among humans with diverse preferences](https://arxiv.org/abs/2211.15006)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Foundational Challenges in Assuring Alignment and Safety of Large Language Models](https://arxiv.org/abs/2404.09932)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Foundational Moral Values for AI Alignment](https://arxiv.org/abs/2311.17017)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346/)** <sub>publication · core · pluralistic-alignment</sub>
- **[From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement](https://arxiv.org/abs/2605.14912)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models](https://aclanthology.org/2023.emnlp-main.961/)** <sub>publication · core · pluralistic-alignment</sub>
- **[From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models](https://arxiv.org/abs/2310.17857)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Group Robust Preference Optimization in Reward-free RLHF](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)** <sub>publication · core · pluralistic-alignment</sub>
- **[HelpSteer2 2024-6](https://arxiv.org/abs/2406.08673)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.](https://arxiv.org/abs/2209.14375)** <sub>publication · core · alignment-goal-survey</sub>
- **[Improving the Distributional Alignment of LLMs using Supervision](https://arxiv.org/abs/2507.00439)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[Internal Value Alignment in Large Language Models through Controlled Value Vector Activation](https://aclanthology.org/2025.acl-long.1326/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Internal Value Alignment in Large Language Models through Controlled Value Vector Activation](https://arxiv.org/abs/2507.11316)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://aclanthology.org/2024.findings-emnlp.620/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Justifications for Democratizing AI Alignment and Their Prospects](https://arxiv.org/abs/2507.19548)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Language Model Alignment in Multilingual Trolley Problems](https://arxiv.org/abs/2407.02273)** <sub>publication · core · pluralistic-alignment</sub>
- **[Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions](https://aclanthology.org/2025.acl-long.1028/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain](https://aclanthology.org/2024.naacl-industry.18/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Language Models Resist Alignment: Evidence From Data Compression, ACL 2025 Best Paper](https://arxiv.org/abs/2406.06144)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025)** <sub>publication · core · pluralistic-alignment, valuebyte-llm-social-science</sub>
- **[Large pre-trained language models contain human-like biases of what is right and wrong to do. Schramowski et al. Nature Machine Intelligence 2022.](https://arxiv.org/abs/2103.11790)** <sub>publication · core · alignment-goal-survey</sub>
- **[Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.90/)** <sub>publication · core · pluralistic-alignment</sub>
- **[LoRe: Personalizing LLMs via Low-Rank Reward Modeling](https://arxiv.org/abs/2504.14439)** <sub>publication · core · personalized-alignment, pluralistic-alignment</sub>
- **[MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://arxiv.org/abs/2405.14953)** <sub>publication · core · pluralistic-alignment</sub>
- **[MAP: Multi-Human-Value Alignment Palette](https://arxiv.org/abs/2410.19198)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[MaxMin-RLHF: Alignment with Diverse Human Preferences](https://arxiv.org/abs/2402.08925)** <sub>publication · core · pluralistic-alignment</sub>
- **[MixDPO: Modeling Preference Strength for Pluralistic Alignment](https://arxiv.org/abs/2601.06180)** <sub>publication · core · pluralistic-alignment</sub>
- **[Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration](https://aclanthology.org/2024.emnlp-main.240/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration](https://arxiv.org/abs/2406.15951)** <sub>publication · core · aidas-llm-values-pluralism, personalized-alignment, valuebyte-llm-social-science</sub>
- **[Moral Alignment for LLM Agents](https://arxiv.org/abs/2410.01639)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning](https://arxiv.org/abs/2511.12271)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation](https://arxiv.org/abs/2511.17579)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://aclanthology.org/2025.naacl-long.120/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models](https://aclanthology.org/2024.acl-long.345/)** <sub>publication · core · pluralistic-alignment</sub>
- **[OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581)** <sub>publication · core · pluralistic-alignment</sub>
- **[Optimizing generative AI by backpropagating language model feedback, Nature](https://nature.com/articles/s41586-025-08661-4)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[PAD: Personalized Alignment of LLMs at Decoding-Time](https://arxiv.org/abs/2410.04070)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Pairwise Calibrated Rewards for Pluralistic Alignment](https://arxiv.org/abs/2506.06298)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences](https://arxiv.org/abs/2406.08469)** <sub>publication · core · pluralistic-alignment</sub>
- **[Parametric Social Identity Injection and Diversification in Public Opinion Simulation](https://arxiv.org/abs/2603.16142)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[PERSONA: A Reproducible Testbed for Pluralistic Alignment](https://aclanthology.org/2025.coling-main.752/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Personality Alignment of Large Language Models](https://arxiv.org/abs/2408.11779)** <sub>publication · core · pluralistic-alignment</sub>
- **[PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization](https://arxiv.org/abs/2507.16679)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://aclanthology.org/2025.emnlp-main.1596/)** <sub>publication · core · pluralistic-alignment</sub>
- **[PluralLLM: Pluralistic Alignment in LLMs via Federated Learning](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)** <sub>publication · core · pluralistic-alignment</sub>
- **[Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking](https://arxiv.org/abs/2409.08622)** <sub>publication · core · pluralistic-alignment, valuebyte-llm-social-science</sub>
- **[Position: A Roadmap to Impactful Pluralistic Alignment Research](https://arxiv.org/abs/2607.22305)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Position: Align AI to Our Aspirations, Not Our Flaws](https://arxiv.org/abs/2606.13755)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles](https://arxiv.org/abs/2502.06059)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[ProgressGym: Alignment with a Millennium of Moral Progress](https://arxiv.org/abs/2406.20087)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs](https://aclanthology.org/2024.acl-long.381/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Reflective Verbal Reward Design for Pluralistic Alignment](https://arxiv.org/abs/2506.17834)** <sub>publication · core · pluralistic-alignment</sub>
- **[Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem](https://arxiv.org/abs/2604.20805)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?](https://arxiv.org/abs/2308.15399)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://arxiv.org/abs/2510.06391)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Robust Multi-Objective Controlled Decoding of Large Language Models](https://arxiv.org/abs/2503.08796)** <sub>publication · core · pluralistic-alignment</sub>
- **[Role Steering of Language Models for Social Simulations](https://arxiv.org/abs/2608.00023)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation](https://arxiv.org/abs/2410.16665)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Scopes of Alignment, 2025.01, AAAI 2025 workshop](https://arxiv.org/abs/2501.12405)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning](https://arxiv.org/abs/2408.16482)** <sub>publication · core · pluralistic-alignment</sub>
- **[Self-Pluralising Culture Alignment for Large Language Models](https://aclanthology.org/2025.naacl-long.350/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Simple Role Assignment is Extraordinarily Effective for Safety Alignment, ACL 2026 Findings](https://arxiv.org/abs/2602.00061)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Social Simulacra: Creating Populated Prototypes for Social Computing Systems](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)** <sub>publication · core · pluralistic-alignment</sub>
- **[Societal Alignment Frameworks Can Improve LLM Alignment](https://arxiv.org/abs/2503.00069)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations](https://aclanthology.org/2025.naacl-long.162/)** <sub>publication · core · pluralistic-alignment</sub>
- **[SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment](https://aclanthology.org/2025.findings-acl.41/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression](https://arxiv.org/abs/2508.08509)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF](https://aclanthology.org/2023.findings-emnlp.754/)** <sub>publication · core · pluralistic-alignment</sub>
- **[STELA: a community-centred approach to norm elicitation for AI alignment, 2024.03, Nature Scientific Reports](https://nature.com/articles/s41598-024-56648-4)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Strong and weak alignment of large language models with human values](https://arxiv.org/abs/2408.04655)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Strong and weak alignment of large language models with human values, 2024.08, Nature Scientific Reports](https://nature.com/articles/s41598-024-70031-3)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions](https://arxiv.org/abs/2508.11414)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models](https://aclanthology.org/2026.eacl-long.305/)** <sub>publication · core · pluralistic-alignment</sub>
- **[The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity](https://arxiv.org/abs/2510.23965)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment](https://arxiv.org/abs/2512.03048)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning](https://arxiv.org/abs/2312.01552)** <sub>publication · core · pluralistic-alignment</sub>
- **[Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement](https://aclanthology.org/2025.acl-long.1408/)** <sub>publication · core · aidas-llm-values-pluralism, stonic-manuscript-bibliography, valuebyte-llm-social-science</sub>
- **[Towards Scalable Automated Alignment of LLMs: A Survey](https://arxiv.org/abs/2406.01252)** <sub>publication · core · pluralistic-alignment</sub>
- **[Training Socially Aligned Language Models in Simulated Human Society](https://arxiv.org/abs/2305.16960)** <sub>publication · adjacent · awesome-llm-datasets, valuebyte-llm-social-science</sub>
- **[Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](https://aclanthology.org/2025.acl-long.1532/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](https://arxiv.org/abs/2506.06404)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Unintended Impacts of LLM Alignment on Global Representation](https://arxiv.org/abs/2402.15018)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Value Alignment from Unstructured Text](https://aclanthology.org/2024.emnlp-industry.81/)** <sub>publication · core · pluralistic-alignment</sub>
- **[Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value](https://aclanthology.org/2024.naacl-long.486/)** <sub>publication · core · pluralistic-alignment, stonic-manuscript-bibliography</sub>
- **[ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs](https://aclanthology.org/2025.winlp-main.15/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making](https://arxiv.org/abs/2503.04569)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models](https://arxiv.org/abs/2603.18113)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment](https://arxiv.org/abs/2603.04822)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[VISPA: Pluralistic Alignment via Automatic Value Selection and Activation](https://arxiv.org/abs/2601.12758)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment</sub>
- **[What are human values, and how do we align AI to them?](https://arxiv.org/abs/2404.10636)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety](https://arxiv.org/abs/2506.00415)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-value-representation-and-model-internals"></a>

#### 📐 Value representation and model internals

<sub>44 publications</sub>

- **[A Method for Learning Value Systems in Generative AI](https://arxiv.org/abs/2607.16903)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations](https://arxiv.org/abs/2601.22440)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection](https://arxiv.org/abs/2607.05052)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment](https://arxiv.org/abs/2604.12851)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks](https://arxiv.org/abs/2601.22396)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Do Differences in Values Influence Disagreements in Online Discussions?](https://arxiv.org/abs/2310.15757)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration](https://arxiv.org/abs/2602.00913)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs](https://arxiv.org/abs/2505.12792)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure](https://doi.org/10.21203/rs.3.rs-8270539/v1)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Enhancing Stance Classification on Social Media Using Quantified Moral Foundations](https://arxiv.org/abs/2310.09848)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models](https://aclanthology.org/2025.acl-long.585/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models](https://arxiv.org/abs/2502.02444)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas](https://arxiv.org/abs/2602.04456)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[High-Dimension Human Value Representation in Large Language Models](https://aclanthology.org/2025.naacl-long.274/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[High-Dimension Human Value Representation in Large Language Models](https://arxiv.org/abs/2404.07900)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum](https://arxiv.org/abs/2601.14172)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture](https://arxiv.org/abs/2605.27373)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Investigating Human Values in Online Communities](https://arxiv.org/abs/2402.14177)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Learning the Value Systems of Societies from Preferences](https://arxiv.org/abs/2507.20728)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning](https://arxiv.org/abs/2602.08835)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer](https://arxiv.org/abs/2606.11018)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora](https://arxiv.org/abs/2605.22660)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions](https://arxiv.org/abs/2403.07678)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning](https://arxiv.org/abs/2401.17228)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts](https://arxiv.org/abs/2605.22641)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[MoVa: Towards Generalizable Classification of Human Morals and Values](https://arxiv.org/abs/2509.24216)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges](https://arxiv.org/abs/2603.23659)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments](https://aclanthology.org/2023.semeval-1.313/)** <sub>publication · core · aidas-llm-values-pluralism, stonic-manuscript-bibliography</sub>
- **[SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs](https://arxiv.org/abs/2504.12633)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers](https://arxiv.org/abs/2501.11770)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Tracing Moral Foundations in Large Language Models](https://arxiv.org/abs/2601.05437)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Understanding How Value Neurons Shape the Generation of Specified Values in LLMs](https://aclanthology.org/2025.findings-emnlp.501/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs](https://arxiv.org/abs/2502.08640)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value Alignment of Social Media Ranking Algorithms](https://arxiv.org/abs/2509.14434)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values](https://arxiv.org/abs/2311.10766)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779)** <sub>publication · core · aidas-llm-values-pluralism, pluralistic-alignment, valuebyte-llm-social-science</sub>
- **[Value Lens: Using Large Language Models to Understand Human Values](https://arxiv.org/abs/2512.15722)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value Profiles for Encoding Human Variation](https://arxiv.org/abs/2503.15484)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models](https://arxiv.org/abs/2602.03160)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[ValueNet: A New Dataset for Human Value Driven Dialogue System](https://arxiv.org/abs/2112.06346)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions](https://arxiv.org/abs/2504.15236)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric](https://aclanthology.org/2023.acl-long.789/)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study](https://arxiv.org/abs/2607.20270)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media](https://arxiv.org/abs/2511.08453)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-measurement-and-profiling"></a>

#### 📏 Measurement and profiling

<sub>85 publications</sub>

- **[(GLOBE) Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models](https://arxiv.org/abs/2406.17675)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches](https://arxiv.org/abs/2404.12744)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(Others & custom) CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility](https://arxiv.org/abs/2307.09705)** <sub>publication · core · alignment-goal-survey, awesome-llm-datasets, valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Measurement of LLM’s Philosophies of Human Nature](https://arxiv.org/abs/2504.02304)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Measuring Spiritual Values and Bias of Large Language Models](https://arxiv.org/abs/2410.11647)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas](https://arxiv.org/abs/2505.14633)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science](https://journals.sagepub.com/doi/full/10.1177/17456916231214460)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) Improving Language Model Personas via Rationalization with Psychological Scaffolds](https://arxiv.org/abs/2504.17993)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025](https://ojs.aaai.org/index.php/AAAI/article/view/34839)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas](https://arxiv.org/abs/2505.18154)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs](https://arxiv.org/abs/2409.09586)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(Schwartz) What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory](https://arxiv.org/abs/2304.03612)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) When Prompting Fails to Sway: Inertia in Moral and Value Judgments of Large Language Models, NeurIPS 2022](https://arxiv.org/abs/2408.09049)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) Who is GPT-3? An Exploration of Personality, Values and Demographics, EMNLP 2022 NLP+CSS workshop](https://arxiv.org/abs/2209.14338)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(VSM) Cultural Value Differences of LLMs: Prompt, Language, and Model Size](https://arxiv.org/abs/2407.16891)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(WVS) Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology](https://arxiv.org/abs/2412.08846)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)](https://arxiv.org/abs/2509.01418)** <sub>publication · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(WVS) Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models](https://arxiv.org/abs/2503.16148)** <sub>publication · core · valuebyte-llm-psychometrics</sub>
- **[A Scalable Approach to Evaluating Moral Sensitivity in LLMs](https://arxiv.org/abs/2607.02972)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference](https://arxiv.org/abs/2505.13531)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?](https://arxiv.org/abs/2506.00751)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact](https://arxiv.org/abs/2606.20205)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Are Language Models Sensitive to Morally Irrelevant Distractors?](https://arxiv.org/abs/2602.09416)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Are Large Language Models Consistent over Value-laden Questions?](https://arxiv.org/abs/2407.02996)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Are LLMs Bad at Moral Reasoning?](https://arxiv.org/abs/2606.11635)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective](https://arxiv.org/abs/2501.00581)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts](https://arxiv.org/abs/2606.21939)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can Language Models Reason about Individualistic Human Values and Preferences?](https://arxiv.org/abs/2410.03868)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?](https://arxiv.org/abs/2606.31213)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Can Revealed Preferences Clarify LLM Alignment and Steering?](https://arxiv.org/abs/2605.08556)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses](https://arxiv.org/abs/2407.10725)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Context-Value-Action Architecture for Value-Driven Large Language Model Agents](https://arxiv.org/abs/2604.05939)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences](https://arxiv.org/abs/2511.02109)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths](https://arxiv.org/abs/2506.02481)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Do LLMs have Consistent Values?](https://arxiv.org/abs/2407.12878)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust](https://arxiv.org/abs/2507.02197)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models](https://arxiv.org/abs/2509.24319)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs](https://arxiv.org/abs/2606.11232)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?](https://arxiv.org/abs/2402.18120)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs](https://arxiv.org/abs/2504.04994)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[From Stability to Inconsistency: A Study of Moral Preferences in LLMs](https://arxiv.org/abs/2504.06324)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Generative Value Conflicts Reveal LLM Priorities](https://arxiv.org/abs/2509.25369)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Heterogeneous Value Alignment Evaluation for Large Language Models](https://arxiv.org/abs/2305.17147)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[How do LLMs reflect human moral foundations? a study using the moral foundations framework](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Human Psychometric Questionnaires Mischaracterize LLM Behavior](https://arxiv.org/abs/2509.10078)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks](https://arxiv.org/abs/2510.03384)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Incoherent Values? Probing LLM Preferences Through Parametric Variation](https://arxiv.org/abs/2606.21102)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Investigating Value-Reasoning Reliability in Small Large Language Models](https://aclanthology.org/2025.emnlp-main.395/)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values](https://arxiv.org/abs/2606.13944)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models](https://arxiv.org/abs/2408.01460)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests](https://arxiv.org/abs/2510.22170)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Measurement and Fairness](https://doi.org/10.1145/3442188.3445901)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models](https://arxiv.org/abs/2409.12106)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Measuring human and AI values based on generative psychometrics with large language models](https://doi.org/10.1609/aaai.v39i25.34839)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models](https://arxiv.org/abs/2604.11216)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Mechanistic Origin of Moral Indifference in Language Models](https://arxiv.org/abs/2603.15615)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?](https://arxiv.org/abs/2501.15463)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation](https://arxiv.org/abs/2605.12515)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs](https://arxiv.org/abs/2601.08634)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability](https://arxiv.org/abs/2605.03217)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models](https://arxiv.org/abs/2511.08565)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method](https://sciencedirect.com/science/article/pii/S0925231225008422)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs](https://arxiv.org/abs/2606.12731)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[On the Credibility of Evaluating LLMs using Survey Questions](https://arxiv.org/abs/2602.04033)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses](https://arxiv.org/abs/2605.28911)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses](https://arxiv.org/abs/2507.07188)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation](https://arxiv.org/abs/2607.05554)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions](https://arxiv.org/abs/2605.09893)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://arxiv.org/abs/2406.14230)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?](https://arxiv.org/abs/2507.13490)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Superficial Beliefs in LLM Decision-Making](https://arxiv.org/abs/2606.11016)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models](https://arxiv.org/abs/2512.03026)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Understanding How Value Neurons Shape the Generation of Specified Values in LLMs](https://arxiv.org/abs/2505.17712)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability](https://arxiv.org/abs/2603.16017)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs](https://arxiv.org/abs/2601.10257)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values](https://arxiv.org/abs/2501.07071)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[Value Drifts: Tracing Value Alignment During LLM Post-Training](https://arxiv.org/abs/2510.26707)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items](https://aclanthology.org/2025.acl-long.838/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items](https://arxiv.org/abs/2505.01015)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts](https://arxiv.org/abs/2411.11479)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models](https://arxiv.org/abs/2406.04214)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models](https://arxiv.org/abs/2310.00378)** <sub>publication · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems](https://arxiv.org/abs/2602.08567)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts](https://arxiv.org/abs/2605.25256)** <sub>publication · core · aidas-llm-values-pluralism</sub>

<a id="catalog-other-and-adjacent-value-research"></a>

#### 📎 Other and adjacent value research

<sub>40 publications</sub>

- **[10.1186/s40537-024-00986-7](https://link.springer.com/article/10.1186/s40537-024-00986-7)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle](https://doi.org/10.1145/3465416.3483305)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL 2025 Best Paper](https://arxiv.org/abs/2402.11005)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective](https://arxiv.org/abs/2408.04638)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Automated Mining of Structured Knowledge from Text in the Era of Large Language Models, 2024.08, KDD 2024](https://dl.acm.org/doi/pdf/10.1145/3637528.3671469)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral](https://arxiv.org/abs/2603.13890)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science](https://aclanthology.org/Q18-1041/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[EMNLP Main 18](https://aclanthology.org/2023.emnlp-main.18/)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs](https://arxiv.org/abs/2406.13993)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[Fairness and Abstraction in Sociotechnical Systems](https://doi.org/10.1145/3287560.3287598)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs, ACL 2025 Best Paper](https://arxiv.org/abs/2502.01926)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization, 2025.05, Sociological Methods & Research](https://journals.sagepub.com/doi/10.1177/00491241251327130)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Generative language models exhibit social identity biases, Nature Computational Science](https://nature.com/articles/s43588-024-00741-1)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods](https://arxiv.org/abs/2301.01893)** <sub>publication · adjacent · awesome-cultural-nlp</sub>
- **[HG & CI & MC](https://arxiv.org/abs/2311.09528)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Large Language Model Safety: A Holistic Survey](https://arxiv.org/abs/2412.17686)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Large language models (LLM) in computational social science: prospects, current state, and challenges, 2025.03, Social Network Analysis and Mining](https://link.springer.com/article/10.1007/s13278-025-01428-9)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, 2023.12, Nature humanities and social sciences communications](https://arxiv.org/abs/2312.11970)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Linhao Yu et al. ACL Findings 2024.](https://aclanthology.org/2024.findings-acl.703/)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[Machine Bias. How Do Generative Language Models Answer Opinion Polls?, 2025.04, Sociological Methods & Research](https://doi.org/10.1177/00491241251330582)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Nicholas Botzer et al. arXiv 2021.](https://arxiv.org/abs/2101.07664)** <sub>publication · adjacent · awesome-llm-safety</sub>
- **[On the Credibility of Evaluating LLMs using Survey Questions](https://aclanthology.org/2026.mme-main.2/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective](https://arxiv.org/abs/2502.14296)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Persuading voters using human–artificial intelligence dialogues, Nature](https://nature.com/articles/s41586-025-09771-9)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[Position: AI Evaluation Should Learn from How We Test Humans](https://arxiv.org/abs/2306.10512)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[PRM800K 2023-5](https://arxiv.org/abs/2305.20050)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Questioning the Survey Responses of Large Language Models, NeurIPS 2024 Oral](https://arxiv.org/abs/2306.07951)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models](https://aclanthology.org/2020.findings-emnlp.301/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025](https://arxiv.org/abs/2412.06435)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[SummarizefromFeedback 2020-9](https://arxiv.org/abs/2009.01325)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[The AI Gap: How Socioeconomic Status Affects Language Technology Interactions, ACL 2025 Best Social Impact Paper](https://arxiv.org/abs/2505.12158)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)** <sub>publication · adjacent · valuebyte-llm-social-science</sub>
- **[UltraFeedback](https://arxiv.org/abs/2310.01377)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[UltraInteract 2024-4](https://arxiv.org/abs/2404.02078)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries](https://sciencedirect.com/science/article/pii/S0065260108602816)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)** <sub>publication · core · aidas-llm-values-pluralism</sub>
- **[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)** <sub>publication · adjacent · awesome-llm-datasets</sub>
- **[Who is GPT-3? An exploration of personality, values and demographics](https://aclanthology.org/2022.nlpcss-1.24/)** <sub>publication · core · stonic-manuscript-bibliography</sub>
- **[Zhijing Jin et al. NeurIPS 2022.](https://arxiv.org/abs/2210.01478)** <sub>publication · adjacent · awesome-llm-safety</sub>

### 🧩 Data, models, code, and additional resources

<a id="catalog-dataset-and-benchmark-artifacts"></a>

#### 💾 Dataset and benchmark artifacts

<sub>28 resources</sub>

- **[(Others & custom) Towards Measuring the Representation of Subjective Global Opinions in Language Models](https://huggingface.co/datasets/Anthropic/llm_global_opinions)** <sub>dataset · core · alignment-goal-survey, valuebyte-llm-psychometrics</sub>
- **[2509.17399](https://huggingface.co/datasets/nlip/DIWALI)** <sub>dataset · adjacent · awesome-cultural-nlp</sub>
- **[A Systematic Survey of Cultural Datasets for Equitable LLM Alignment](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)** <sub>dataset · core · aidas-llm-values-pluralism</sub>
- **[Big-Math 2025-2](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Chatbotarenaconversations 2023-6](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024](https://mango.mpi-inf.mpg.de/)** <sub>dataset · adjacent · valuebyte-llm-social-science</sub>
- **[CValues 2023-7](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture](https://huggingface.co/datasets/lyan62/FoodieQA)** <sub>dataset · adjacent · awesome-cultural-nlp</sub>
- **[HelpSteer2 2024-6](https://huggingface.co/datasets/nvidia/HelpSteer2)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[HF Datasets](https://huggingface.co/datasets/MinhDucBui/Multi3Hate)** <sub>dataset · adjacent · awesome-cultural-nlp</sub>
- **[HG & CI](https://huggingface.co/datasets/openai/webgpt_comparisons)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[HG & CI & MC](https://huggingface.co/datasets/nvidia/HelpSteer)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Medical-rlhf 2023-5](https://huggingface.co/datasets/shibing624/medical)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[MT-Benchhumanjudgments 2023-6](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[OASST1pairwiserlhfreward 2023-5](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[OpenHermesPreferences 2024-3](https://huggingface.co/datasets/argilla/OpenHermesPreferences)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Paper1](https://huggingface.co/datasets/Anthropic/hh-rlhf)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[PKU-SafeRLHF 2023-7](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)** <sub>dataset · core · alignment-goal-survey</sub>
- **[SafetyBench 2023-9](https://huggingface.co/datasets/thu-coai/SafetyBench)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[SHP 2021-10 — All — EN — HG](https://huggingface.co/datasets/stanfordnlp/SHP)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[Stack-Exchange-Preferences](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[SummarizefromFeedback 2020-9](https://huggingface.co/datasets/openai/summarize_from_feedback)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[UltraInteract 2024-4](https://huggingface.co/datasets/openbmb/UltraInteract_pair)** <sub>dataset · adjacent · awesome-llm-datasets</sub>
- **[ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022](https://liang-qiu.github.io/ValueNet/)** <sub>dataset · core · alignment-goal-survey, valuebyte-llm-social-science</sub>
- **[When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.](https://huggingface.co/datasets/feradauto/MoralExceptQA)** <sub>dataset · core · alignment-goal-survey</sub>
- **[Zhihurlhf3k 2023-4](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)** <sub>dataset · adjacent · awesome-llm-datasets</sub>

<a id="catalog-model-checkpoints-and-scorers"></a>

#### 🧠 Model checkpoints and scorers

<sub>5 resources</sub>

- **[2502.13766](https://huggingface.co/floschne)** <sub>model · adjacent · awesome-cultural-nlp</sub>
- **[Exploring Universal Human Values with Large Language Models: The AWARE-Value Model](https://researchsquare.com/article/rs-8188052/v1)** <sub>model · core · aidas-llm-values-pluralism</sub>
- **[MT-Benchhumanjudgments 2023-6](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)** <sub>model · adjacent · awesome-llm-datasets</sub>
- **[Robustness of large language models in moral judgements](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)** <sub>model · core · aidas-llm-values-pluralism</sub>
- **[Stick to your role! Stability of personal values expressed in large language models](https://journals.plos.org/plosone/article)** <sub>model · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>

<a id="catalog-code-repositories"></a>

#### 🧰 Code repositories

<sub>97 resources</sub>

- **[(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023](https://github.com/wanng-ide/ealm)** <sub>repository · core · valuebyte-llm-psychometrics</sub>
- **[(MFT) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science](https://github.com/feradauto/MoralCoT)** <sub>repository · core · alignment-goal-survey, awesome-llm-safety, valuebyte-llm-psychometrics</sub>
- **[(MFT) MoralBench: Moral Evaluation of LLMs](https://github.com/agiresearch/MoralBench)** <sub>repository · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Measurement of LLM’s Philosophies of Human Nature](https://github.com/kodenii/M-PHNS)** <sub>repository · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, ACL 2024](https://github.com/Value4AI/ValueBench)** <sub>repository · core · valuebyte-llm-psychometrics, valuebyte-llm-social-science</sub>
- **[(SVO) Heterogeneous Value Alignment Evaluation for Large Language Models, AAAI 2024 Workshop](https://github.com/zowiezhang/HVAE)** <sub>repository · core · valuebyte-llm-psychometrics</sub>
- **[(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)](https://github.com/ku-nlp/global-opinion-alignment)** <sub>repository · core · valuebyte-llm-psychometrics</sub>
- **[2023.findings-acl.631](https://github.com/shramay-palta/FORK_ACL2023)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2023.findings-emnlp.509](https://github.com/SALT-NLP/CulturallyAwareNLI)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2024.findings-naacl.196](https://github.com/zhanhl316/ReNoVi)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2209.12226](https://github.com/google-research-datasets/nlp-fairness-for-india)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2210.08604](https://github.com/yrf1/NormSage)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2301.01893](https://github.com/WadeYin9712/GIVL)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2305.11840](https://github.com/google-research-datasets/seegull)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2305.14456](https://github.com/tareknaous/camel)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2305.16171](https://github.com/simran-khanuja/Multilingual-Fig-QA)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2308.16705](https://github.com/nlee0212/CREHate)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2310.17586](https://github.com/iamshnoo/weathub)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2401.10352](https://github.com/yongcaoplus/cuDialog)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2402.09369v1](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2402.10946](https://github.com/Scarelette/CultureLLM)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2403.14651](https://github.com/microsoft/DOSA)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2404.01247](https://github.com/simran-khanuja/image-transcreation)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2404.10199v1](https://github.com/huihanlhh/Culture-Gen)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2404.12464](https://github.com/Akhila-Yerukola/NormAd)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2404.16019](https://github.com/HannahKirk/prism-alignment)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2406.09948](https://github.com/nlee0212/BLEnD)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2407.03791](https://github.com/floschne/m5b)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2407.06863](https://github.com/google-research-datasets/cube)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2412.20760](https://github.com/huihanlhh/CultureGenAttr)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2502.13766](https://github.com/floschne/gimmick)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[2509.17399](https://github.com/pramitsahoo/culture-evaluation)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[3539618.3591877](https://github.com/zhanhl316/SocialDial)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[<a href="](https://github.com/sindresorhus/awesome)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models](https://github.com/PKU-YuanGroup/Machine-Mindset)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms](https://github.com/GAIR-NLP/OPO)** <sub>repository · adjacent · awesome-llm-safety, valuebyte-llm-social-science</sub>
- **[A Roadmap to Pluralistic Alignment, ICML 2024](https://github.com/jfisher52/AI_Pluralistic_Alignment)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[A Survey on Evaluation of Large Language Models](https://github.com/MLGroupJLU/LLM-eval-survey)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[A Survey on Large Language Model based Autonomous Agents](https://github.com/Paitesanshi/LLM-Agent-Survey)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[AI Job Displacement Tracker](https://github.com/noahaust2/ai-displacement-tracker)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Aligning ai with shared human values. Hendrycks et al. arXiv 2020.](https://github.com/hendrycks/ethics)** <sub>repository · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[Aligning Large Language Models with Human: A Survey](https://github.com/GaryYufei/AlignLLMHumanSurvey)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Alignment-Goal-Survey](https://github.com/ValueCompass/Alignment-Goal-Survey)** <sub>repository · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[Alpacacomparisondata 2023-3](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[awesome-llm-social-simulation](https://github.com/Wanying-He/awesome-llm-social-simulation)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[Awesome-Personalized-Alignment](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[Awesome-Pluralistic-Alignment](https://github.com/anudeex/Awesome-Pluralistic-Alignment)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral](https://github.com/jingzhe-lin/ASVO)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Big-Math 2025-2](https://github.com/SynthLabsAI/big-math)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[code and data](https://github.com/NeuralSentinel/CulturalKaleidoscope)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[collection](https://github.com/Indiiigo/LLM_rep_review)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Concerns on the use of generative AI in social science research](https://github.com/uh-dcm/genai-concerns)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)** <sub>repository · core · alignment-goal-survey</sub>
- **[CrowS-Pairs](https://github.com/nyu-mll/crows-pairs)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[cultural-llm-papers](https://github.com/faridlazuarda/cultural-llm-papers)** <sub>repository · core · aidas-llm-values-pluralism, awesome-cultural-nlp</sub>
- **[culture-awareness-llms](https://github.com/siddheshih/culture-awareness-llms)** <sub>repository · core · aidas-llm-values-pluralism</sub>
- **[CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility. Xu et al. arXiv 2023.](https://github.com/X-PLUG/CValues)** <sub>repository · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[Datasets for depression detection using data posted on online platforms](https://github.com/bucuram/depression-datasets-nlp)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture](https://github.com/lyan62/FoodieQA)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[github.com](https://github.com/CLUEbenchmark/CLUEDatasetSearch)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[HelpSteer2 2024-6](https://github.com/NVIDIA/NeMo-Aligner)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Heterogeneous Value Evaluation for Large Language Models](https://github.com/zowiezhang/A2EHV)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[HF Datasets](https://github.com/MinhDucBui/Multi3Hate)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[High-Dimension Human Value Representation in Large Language Models](https://github.com/HLTCHKUST/UniVaR)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[huozirlhfdata 2024-2](https://github.com/HIT-SCIR/huozi)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[huozirlhfdata 2024-2](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Large Language Model based Multi-Agents: A Survey of Progress and Challenges](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Leaderboard](https://github.com/thu-coai/Safety-Prompts)** <sub>repository · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[Medical-rlhf 2023-5](https://github.com/shibing624/MedicalGPT)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Mental Health Datasets](https://github.com/kharrigian/mental-health-datasets)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Moral stories: Situated reasoning about norms, intents, actions, and their consequences. Emelin et al. arXiv 2020.](https://github.com/demelin/moral_stories)** <sub>repository · core · alignment-goal-survey</sub>
- **[MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.](https://github.com/thu-coai/MoralDial)** <sub>repository · core · alignment-goal-survey</sub>
- **[MT-Benchhumanjudgments 2023-6](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[PKU-SafeRLHF 2023-7](https://github.com/PKU-Alignment/safe-rlhf)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.](https://github.com/IBM/Dromedary)** <sub>repository · core · alignment-goal-survey</sub>
- **[PRM800K 2023-5](https://github.com/openai/prm800k)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[ProgressGym: Alignment with a Millennium of Moral Progress, NeurIPS 2024 D&B Track Spotlight](https://github.com/PKU-Alignment/ProgressGym)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[rladmstn1714/CLIcK](https://github.com/rladmstn1714/CLIcK)** <sub>repository · adjacent · awesome-cultural-nlp</sub>
- **[SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.](https://github.com/sharonlevy/SafeText)** <sub>repository · core · alignment-goal-survey</sub>
- **[SafetyBench 2023-9](https://github.com/thu-coai/SafetyBench)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.](https://github.com/allenai/scruples)** <sub>repository · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[SHP 2021-10 — All — EN — HG](https://github.com/kawine/dataset_difficulty)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025](https://github.com/zfw1226/D2A)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[SocialAgent](https://github.com/FudanDISC/SocialAgent)** <sub>repository · core · aidas-llm-values-pluralism, valuebyte-llm-social-science</sub>
- **[SuperCLUE-Safety 2023-9](https://github.com/CLUEbenchmark/SuperCLUE-safety)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[The moral integrity corpus: A benchmark for ethical dialogue systems. Ziems et al. arXiv 2022.](https://github.com/SALT-NLP/mic)** <sub>repository · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[The Rise and Potential of Large Language Model Based Agents: A Survey](https://github.com/WooooDyy/LLM-Agent-Paper-List)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Training a helpful and harmless assistant with reinforcement learning from human feedback. Bai et al. arXiv 2022.](https://github.com/anthropics/hh-rlhf)** <sub>repository · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[Training Socially Aligned Language Models in Simulated Human Society](https://github.com/agi-templar/Stable-Alignment)** <sub>repository · adjacent · awesome-llm-datasets, valuebyte-llm-social-science</sub>
- **[TRUSTGPT 2023-6](https://github.com/HowieHwong/TrustGPT)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[UltraFeedback](https://github.com/OpenBMB/UltraFeedback)** <sub>repository · adjacent · awesome-llm-datasets</sub>
- **[Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, AAAI24](https://github.com/tsor13/kaleido)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)](https://github.com/MoralAgentSim/Simulation-Engine)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>
- **[⭐️ Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025](https://github.com/Value4AI/gpv)** <sub>repository · adjacent · valuebyte-llm-social-science</sub>

<a id="catalog-project-pages"></a>

#### 🌐 Project pages

<sub>10 resources</sub>

- **[2109.13238](https://marvl-challenge.github.io/)** <sub>project · adjacent · awesome-cultural-nlp</sub>
- **[2509.17399](https://nlip-lab.github.io/nlip/publications/diwali/)** <sub>project · adjacent · awesome-cultural-nlp</sub>
- **[AI Alignment: A Comprehensive Survey](https://alignmentsurvey.com/)** <sub>project · adjacent · valuebyte-llm-social-science</sub>
- **[Can machines learn morality? the delphi experiment. Jiang et al. arXiv 2021.](https://delphi.allenai.org/)** <sub>project · core · alignment-goal-survey</sub>
- **[Concerns on the use of generative AI in social science research](https://uh-dcm.github.io/genai-concerns/)** <sub>project · adjacent · valuebyte-llm-social-science</sub>
- **[NLPositionality: Characterizing Design Biases of Datasets and Models](https://nlpositionality.cs.washington.edu/)** <sub>project · adjacent · awesome-cultural-nlp</sub>
- **[Political-LLM: Large Language Models in Political Science](https://political-llm.org/)** <sub>project · adjacent · valuebyte-llm-social-science</sub>
- **[SafetyBench 2023-9](https://llmbench.ai/safety)** <sub>project · adjacent · awesome-llm-datasets</sub>
- **[SuperCLUE-Safety 2023-9](https://cluebenchmarks.com/superclue_safety.html)** <sub>project · adjacent · awesome-llm-datasets</sub>
- **[Towards Measuring the Representation of Subjective Global Opinions in Language Models](https://llmglobalvalues.anthropic.com/)** <sub>project · adjacent · valuebyte-llm-social-science</sub>

<a id="catalog-survey-resources"></a>

#### 📋 Survey resources

<sub>4 resources</sub>

- **[EVS — European Values Survey](https://europeanvaluesstudy.eu/)** <sub>survey_resource · core · aidas-llm-values-pluralism, alignment-goal-survey</sub>
- **[GSS — General Social Survey](https://gss.norc.org/)** <sub>survey_resource · core · aidas-llm-values-pluralism</sub>
- **[World Values Survey Wave 7 (2017-2022).](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)** <sub>survey_resource · core · alignment-goal-survey</sub>
- **[WVS — World Values Survey](https://worldvaluessurvey.org/)** <sub>survey_resource · core · aidas-llm-values-pluralism</sub>

<a id="catalog-additional-resources"></a>

#### 🔗 Additional resources

<sub>93 resources</sub>

- **[!\[Awesome](https://awesome.re)** <sub>other · core · pluralistic-alignment</sub>
- **[(ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(ATP) Whose Opinions Do Language Models Reflect?, ICML 2023](https://proceedings.mlr.press/v202/santurkar23a.html)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate](https://journals.plos.org/climate/article)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(Others & custom) DO MINDFULNESS ACTIVITIES IMPROVE HANDGRIP STRENGTH AMONG OLDER ADULTS: A PROPENSITY SCORE MATCHING APPROACH, 2024.12, Innovation in Aging](https://academic.oup.com/innovateage/article/8/Supplement_1/1010/7939280)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(PCT) The Political Biases of ChatGPT, 2023.01, Social Sciences](https://mdpi.com/2076-0760/12/3/148)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(Schwartz) Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz’s Theory of Basic Values, 2024.01, JMIR Mental Health](https://mental.jmir.org/2024/1/e55988)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[(VSM) Large Language Models as Superpositions of Cultural Perspectives](https://gitlab.inria.fr/gkovac/value_stability)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[2301.02560](https://geodiverse-data-collection.cs.princeton.edu/)** <sub>other · adjacent · awesome-cultural-nlp</sub>
- **[2410.12705](https://worldcuisines.github.io/)** <sub>other · adjacent · awesome-cultural-nlp</sub>
- **[<a href="](https://git.io/typing-svg)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[<img src="](https://capsule-render.vercel.app/api)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[<img src="](https://readme-typing-svg.demolab.com)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights](https://unesdoc.unesco.org/ark:/48223/pf0000048063)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[A review of automatic item generation techniques leveraging large language models](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[A theory of justice.](https://jstor.org/stable/j.ctvjf9z6v)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism](http://jstor.org/stable/24707060)** <sub>other · core · stonic-manuscript-bibliography</sub>
- **[Aggregating Sets of Judgments: An Impossibility Result](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[An Overview of the Schwartz Theory of Basic Values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012.](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)** <sub>other · core · alignment-goal-survey</sub>
- **[Basic human values: Theory, measurement, and applications](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Can Generative AI improve social science?, 2024.05, PNAS](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)** <sub>other · adjacent · valuebyte-llm-social-science</sub>
- **[Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[Chatbotarenaconversations 2023-6](https://browse.arxiv.org/pdf/2306.05685.pdf)** <sub>other · adjacent · awesome-llm-datasets</sub>
- **[Collective Choice and Social Welfare](https://jstor.org/stable/j.ctv2sp3dqx)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Conflicts of Values (in Moral Luck)](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Creating Capabilities: The Human Development Approach and Its Implementation](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Cultural Value Orientations](https://researchgate.net/publication/265997557)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Culture's consequences: International differences in work-related values](https://philpapers.org/rec/HOFCCI-2)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Culture's consequences: International differences in work-related values. Hofstede et al. 1984.](https://books.google.com/books/about/Culture_s_Consequences.html)** <sub>other · core · alignment-goal-survey</sub>
- **[Cultures and organizations: software of the mind](https://books.google.co.kr/books)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Do LLMs have Consistent Values?](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)** <sub>other · core · stonic-manuscript-bibliography</sub>
- **[ESS — European Social Survey](https://europeansocialsurvey.org/data-portal)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Functional theory of human values](https://researchgate.net/publication/259486885)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Handbook of Computational Social Choice](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)** <sub>other · core · alignment-goal-survey</sub>
- **[Kush R. Varshney. XRDS 2019.](https://krvarshney.github.io/)** <sub>other · adjacent · awesome-llm-safety</sub>
- **[Kush R. Varshney. XRDS 2019.](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)** <sub>other · adjacent · awesome-llm-safety</sub>
- **[Leaderboard](http://115.182.62.166:18000/)** <sub>other · core · alignment-goal-survey, awesome-llm-datasets</sub>
- **[Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Liberals and conservatives rely on different sets of moral foundations](https://pubmed.ncbi.nlm.nih.gov/19379034/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002.](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)** <sub>other · core · alignment-goal-survey</sub>
- **[lit.eecs.umich.edu](https://lit.eecs.umich.edu/downloads.html)** <sub>other · adjacent · valuebyte-llm-social-science</sub>
- **[Manipulation of Voting Schemes: A General Result](https://jstor.org/stable/1914083)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Mapping and interpreting cultural differences around the world](https://researchgate.net/publication/265596552)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Measuring Perceived Slant in Large Language Models Through User Evaluations](https://modelslant.com/paper.pdf)** <sub>other · core · pluralistic-alignment</sub>
- **[Measuring the Refined Theory of Individual Values in 49 Cultural Groups](https://researchgate.net/publication/349058866)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Mental representations of social values.](https://psycnet.apa.org/record/2012-14612-001)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies](https://jstor.org/stable/j.ctv10vm2ns)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Modernization, Cultural Change, and Democracy](https://researchgate.net/publication/230557603)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism](https://papers.ssrn.com/sol3/papers.cfm)** <sub>other · core · aidas-llm-values-pluralism, valuebyte-llm-psychometrics</sub>
- **[NeurIPS 2025 Tutorial: Human-AI Alignment](https://hai-alignment-course.github.io/tutorial/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[On the Rationale of Group Decision-making](https://jstor.org/stable/1825026)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Perils and opportunities in using large language models in psychological research](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)** <sub>other · adjacent · valuebyte-llm-social-science</sub>
- **[Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)** <sub>other · core · valuebyte-llm-psychometrics</sub>
- **[Pew Researcj Center's Global Attitudes Surveys (GAS)](https://pewresearch.org/)** <sub>other · core · alignment-goal-survey</sub>
- **[PKU-SafeRLHF 2023-7](https://browse.arxiv.org/pdf/2307.04657.pdf)** <sub>other · adjacent · awesome-llm-datasets</sub>
- **[Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)** <sub>other · core · stonic-manuscript-bibliography</sub>
- **[Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://browse.arxiv.org/pdf/2209.07858.pdf)** <sub>other · adjacent · awesome-llm-datasets</sub>
- **[Refining the theory of basic individual values](https://pubmed.ncbi.nlm.nih.gov/22823292/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Rokeach value survey. Rokeach et al. The nature of human values. 1967.](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)** <sub>other · core · alignment-goal-survey</sub>
- **[SHP 2021-10 — All — EN — HG](https://browse.arxiv.org/pdf/2110.08420.pdf)** <sub>other · adjacent · awesome-llm-datasets</sub>
- **[Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.](https://maartensap.com/social-bias-frames/)** <sub>other · core · alignment-goal-survey</sub>
- **[Social chemistry 101: Learning to reason about social and moral norms. Forbes et al. arXiv 2020.](https://maxwellforbes.com/social-chemistry/)** <sub>other · core · alignment-goal-survey, awesome-llm-safety</sub>
- **[Social Choice and Individual Values](https://jstor.org/stable/j.ctt1nqb90)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Social Choice Theory (in Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/social-choice/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Stanford 2025: Human-Centered LLMs (CS329X)](https://web.stanford.edu/class/cs329x/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Stanford 2025: Machine Learning from Human Preferences (CS329H)](https://web.stanford.edu/class/cs329h/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Steerable Alignment with Conditional Multiobjective Preference Optimization](https://dspace.mit.edu/handle/1721.1/156747)** <sub>other · core · pluralistic-alignment</sub>
- **[Stick to your role! Stability of personal values expressed in large language models](http://dx.doi.org/10.1371/journal.pone.0309114)** <sub>other · core · stonic-manuscript-bibliography</sub>
- **[Survey of Cultural Awareness in Language Models: Text and Beyond Open Access](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)** <sub>other · core · pluralistic-alignment</sub>
- **[The Impossibility of a Paretian Liberal](https://jstor.org/stable/1829633)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Morality of Freedom](https://academic.oup.com/book/9926)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Morality of Pluralism](https://jstor.org/stable/j.ctt7smh7)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Morals of Modernity](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The nature of human values.](https://psycnet.apa.org/record/2011-15663-000)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Right and the Good](https://academic.oup.com/book/27608)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Righteous Mind](https://righteousmind.com/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The Theory of Communicative Action](https://philpapers.org/rec/HABTTO)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[The theory of dyadic morality: Reinventing moral judgment by redefining harm.](https://psycnet.apa.org/record/2018-02142-002)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022.](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)** <sub>other · core · alignment-goal-survey</sub>
- **[Towards Pluralistic Alignment of LLMs: A Comprehensive Survey](https://preprints.org/manuscript/202603.1876)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop](https://openaccess.city.ac.uk/id/eprint/31381/)** <sub>other · adjacent · valuebyte-llm-social-science</sub>
- **[Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://browse.arxiv.org/pdf/2204.05862.pdf)** <sub>other · adjacent · awesome-llm-datasets</sub>
- **[Two Concepts of Liberty](https://academic.oup.com/book/7968/chapter-abstract/153281672)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Universals in the content and structure of values: Theoretical advances and empirical tests in 20 countries.](https://psycnet.apa.org/record/2003-00370-001)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[Value Pluralism (in Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/value-pluralism/)** <sub>other · core · aidas-llm-values-pluralism</sub>
- **[ValueNet: A New Dataset for Human Value Driven Dialogue System](http://dx.doi.org/10.1609/aaai.v36i10.21368)** <sub>other · core · stonic-manuscript-bibliography</sub>

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
