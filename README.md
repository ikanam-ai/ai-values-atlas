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
- [Scope, evidence, and entry format](#scope-evidence-and-entry-format)
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
| [Functional Theory of Human Values](https://doi.org/10.1016/j.paid.2013.07.043) | 18 values in six motivational subfunctions | profiling with an alternative named human-value theory |
| [Helpful, Honest, and Harmless](https://arxiv.org/abs/2112.00861) | principle set | assistant behavior and preference modeling |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | written constitution or principle space | critique, revision, and alignment targets |

## Scope, evidence, and entry format

The atlas has two deliberately separate layers:

| Layer | What it contains | What inclusion means |
|---|---|---|
| **Curated field guide** | selected papers, axiologies, instruments, datasets, and measurement tools | the record has been read closely enough to place it in the field map |
| **Discovery index** | 1018 deduplicated URLs collected from ten public catalogs and the STONIC bibliography | the resource is discoverable and provenance-preserved; its methods are not necessarily audited |

`Core` records directly study values in AI. `Adjacent` records cover constructs
such as morality, culture, opinions, preferences, or alignment when their data or
methods are useful for value research. Inclusion is not an endorsement, and a
missing artifact link means “not yet verified,” not “does not exist.”

Publication entries use one stable order:

> `(subdomain or value model)` **Title** — venue — date — [paper] [code] [dataset]

The parenthetical label names the paper's operative value space, instrument, or
nearest research subdomain. Links are always last. Venue and artifact links are
shown only when the source metadata supports them.

## Literature by research question

### Surveys and field overviews

- (Psychometrics) **A Systematic Review of Psychometric Evaluation of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.08245) [catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- (Values and attitudes) **Large Language Models as Mirrors of Human Attitudes, Opinions, and Values** — Findings of EMNLP — 2024 — [paper](https://aclanthology.org/2024.findings-emnlp.513/)
- (Human values) **Human Values and Alignment in Artificial Intelligence: A Survey** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.10636)

#### Related living catalogs

- (Values and pluralism) **Awesome LLM Values and Pluralistic Alignment** — GitHub — continuously updated — [catalog](https://github.com/AIDASLab/Awesome-LLM-Values-and-Pluralistic-Alignment)
- (Psychometrics) **Awesome LLM Psychometrics** — GitHub — continuously updated — [catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- (Pluralistic alignment) **Towards Pluralistic Alignment of LLMs: A Comprehensive Survey** — GitHub — continuously updated — [catalog](https://github.com/anudeex/Awesome-Pluralistic-Alignment)
- (Alignment targets) **Alignment Goal Survey** — GitHub — continuously updated — [catalog](https://github.com/ValueCompass/Alignment-Goal-Survey)

### Questionnaires and elicited profiles

- (Schwartz / HEXACO) **Who is GPT-3? An Exploration of Personality, Values and Demographics** — NLP+CSS at EMNLP — 2022 — [paper](https://aclanthology.org/2022.nlpcss-1.24/)
- (Schwartz) **Stick to Your Role! Stability of Personal Values Expressed in Large Language Models** — PLOS ONE — 2024 — [paper](https://doi.org/10.1371/journal.pone.0309114)
- (Schwartz) **Do LLMs Have Consistent Values?** — ICLR — 2025 — [paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)
- (Survey instruments) **On the Credibility of Evaluating LLMs Using Survey Questions** — MME — 2026 — [paper](https://aclanthology.org/2026.mme-main.2/)
- (Schwartz) **Assessing the Alignment of LLMs With Human Values for Mental Health Integration** — JMIR Mental Health — 2024 — [paper](https://doi.org/10.2196/55988)
- (Schwartz) **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.838/)
- (Adaptive measurement) **Raising the Bar: Investigating the Values of LLMs via Generative Evolving Testing** — OpenReview — 2025 — [paper](https://openreview.net/forum?id=0REM9ydeLZ)
- (Adaptive measurement) **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=qNlTH4kYJZ)
- (Schwartz) **Cultural Value Alignment in LLMs: A Prompt-based Analysis of Schwartz Values** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.17112)

### Value understanding and benchmark tasks

- (ETHICS) **Aligning AI With Shared Human Values** — ICLR — 2021 — [paper](https://openreview.net/forum?id=dNy_RKzJacY) [code](https://github.com/hendrycks/ethics)
- (Social norms) **Social Chemistry 101** — EMNLP — 2020 — [paper](https://aclanthology.org/2020.emnlp-main.48/) [dataset](https://maxwellforbes.com/social-chemistry/)
- (Social norms) **Moral Stories** — EMNLP — 2021 — [paper](https://aclanthology.org/2021.emnlp-main.54/) [code](https://github.com/demelin/moral_stories)
- (Delphi) **Can Machines Learn Morality? The Delphi Experiment** — arXiv — 2021 — [paper](https://arxiv.org/abs/2110.07574) [project](https://delphi.allenai.org/)
- (Schwartz) **ValueNet** — AAAI — 2022 — [paper](https://doi.org/10.1609/aaai.v36i10.21368) [dataset](https://liang-qiu.github.io/ValueNet/)
- (ValueEval) **The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments** — SemEval — 2023 — [paper](https://aclanthology.org/2023.semeval-1.313/)
- (Multiple instruments) **ValueBench** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.111/) [code](https://github.com/Value4AI/ValueBench)
- (Cultural values) **WorldValuesBench** — LREC-COLING — 2024 — [paper](https://aclanthology.org/2024.lrec-main.1539/)
- (Generative / pluralistic) **Value Compass Benchmarks** — ACL Demo — 2025 — [paper](https://aclanthology.org/2025.acl-demo.64/)
- (Moral values) **Structured Moral Reasoning in Language Models** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.1541/)
- (Schwartz) **The Staircase of Ethics** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.806/)

### Values in generated text

- (Schwartz) **Value FULCRA** — NAACL — 2024 — [paper](https://aclanthology.org/2024.naacl-long.486/)
- (GPV / supplied values) **Measuring Human and AI Values Based on Generative Psychometrics** — AAAI — 2025 — [paper](https://doi.org/10.1609/aaai.v39i25.34839) [code](https://github.com/Value4AI/gpv) [model](https://huggingface.co/Value4AI/ValueLlama-3-8B)
- (Adaptive values) **CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.10725)
- (Values, rights, and duties) **Value Kaleidoscope** — AAAI — 2024 — [paper](https://doi.org/10.1609/aaai.v38i18.29970) [code](https://github.com/tsor13/kaleido)
- (MFT) **MoralBERT** — arXiv — 2024 — [paper](https://arxiv.org/abs/2403.07678) [code](https://github.com/vjosapreniqi/MoralBERT)
- (Schwartz) **ValueNet** — AAAI — 2022 — [paper](https://doi.org/10.1609/aaai.v36i10.21368) [dataset](https://liang-qiu.github.io/ValueNet/)

### Choice, action, and cross-interface gaps

- (Schwartz / INVP) **What's the Most Important Value? INVP** — COLING — 2025 — [paper](https://aclanthology.org/2025.coling-main.317/)
- (Value–action gap) **Mind the Value–Action Gap: Do LLMs Act in Alignment with Their Values?** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.154/)
- (Schwartz / ValueCompass) **ValueCompass: Measuring Contextual Value Alignment Between Human and LLMs** — WiNLP — 2025 — [paper](https://aclanthology.org/2025.winlp-main.15/)
- (Structural values) **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective** — Findings of ACL — 2025 — [paper](https://aclanthology.org/2025.findings-acl.1188/)
- (Behavioral theory) **The Theory of Planned Behavior** — Organizational Behavior and Human Decision Processes — 1991 — [paper](https://www.sciencedirect.com/science/article/pii/074959789190020T)
- (Value–belief–norm theory) **A Value–Belief–Norm Theory of Support for Social Movements** — Human Ecology Review — 1999 — [paper](http://www.jstor.org/stable/24707060)

### Culture, language, and pluralism

- (Cross-lingual morality) **Ethical Reasoning and Moral Value Alignment Depend on the Language We Prompt In** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.18460)
- (Cultural alignment) **Cultural Bias and Cultural Alignment of Large Language Models** — PNAS Nexus — 2024 — [paper](https://doi.org/10.1093/pnasnexus/pgae346)
- (Cultural alignment) **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.2/)
- (Cultural values) **WorldValuesBench** — LREC-COLING — 2024 — [paper](https://aclanthology.org/2024.lrec-main.1539/)
- (Values, rights, and duties) **Value Kaleidoscope** — AAAI — 2024 — [paper](https://doi.org/10.1609/aaai.v38i18.29970) [code](https://github.com/tsor13/kaleido)
- (Political pluralism) **Aligning Large Language Models with Diverse Political Viewpoints** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.412/)
- (MFT) **Moral Foundations of Large Language Models** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.982/)
- (Cultural NLP) **Awesome Cultural NLP** — GitHub — continuously updated — [catalog](https://github.com/simran-khanuja/awesome-cultural-nlp)
- (Personalized alignment) **Awesome Personalized Alignment** — GitHub — continuously updated — [catalog](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)

### Representations, internals, and steering

- (GPLA) **Generative Psycho-Lexical Approach for Constructing Value Systems in LLMs** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.585/)
- (UniVaR) **High-Dimension Human Value Representation in LLMs** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.274/) [code](https://github.com/HLTCHKUST/UniVaR) [model](https://huggingface.co/CAiRE/UniVaR-lambda-1)
- (Value vectors) **Internal Value Alignment through Controlled Value Vector Activation** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1326/)
- (Value neurons) **Understanding How Value Neurons Shape the Generation of Specified Values** — Findings of EMNLP — 2025 — [paper](https://aclanthology.org/2025.findings-emnlp.501/)
- (Principle sets) **Towards Better Value Principles for LLM Alignment** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1408/)
- (Value alignment) **Unintended Harms of Value-Aligned LLMs** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1532/)
- (Constitutional AI) **Constitutional AI: Harmlessness from AI Feedback** — arXiv — 2022 — [paper](https://arxiv.org/abs/2212.08073) [code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)

### Reliability, validity, and reporting

- (Measurement theory) **Measurement and Fairness** — FAccT — 2021 — [paper](https://doi.org/10.1145/3442188.3445901)
- (Prompt sensitivity) **POSIX: A Prompt Sensitivity Index for Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.02185)
- (Survey validity) **On the Credibility of Evaluating LLMs Using Survey Questions** — MME — 2026 — [paper](https://aclanthology.org/2026.mme-main.2/)
- (Evaluator bias) **Large Language Models Are Not Fair Evaluators** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.511/)
- (Evaluation design) **AI Evaluation Should Learn from How We Test Humans** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.10512)
- (Holistic evaluation) **Holistic Evaluation of Language Models** — TMLR — 2023 — [paper](https://openreview.net/forum?id=iO4LZibEqW)
- (Reporting) **Model Cards for Model Reporting** — FAT* — 2019 — [paper](https://doi.org/10.1145/3287560.3287596)
- (Dataset documentation) **Datasheets for Datasets** — Communications of the ACM — 2021 — [paper](https://doi.org/10.1145/3458723)
- (Dataset documentation) **Data Statements for NLP** — TACL — 2018 — [paper](https://aclanthology.org/Q18-1041/)
- (Internal auditing) **Closing the AI Accountability Gap** — FAT* — 2020 — [paper](https://doi.org/10.1145/3351095.3372873)

## Datasets, benchmarks, and instruments

| Resource | Kind | Value space or construct | Primary link |
|---|---|---|---|
| Value Portrait | scenario item bank | Schwartz-10 | [paper](https://aclanthology.org/2025.acl-long.838/) |
| ValueBench | benchmark and code | value orientation and understanding | [paper](https://aclanthology.org/2024.acl-long.111/) [code](https://github.com/Value4AI/ValueBench) |
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
| UniVaR lambda-1 | value-relevant embedding encoder | dense model–language representation | [model](https://huggingface.co/CAiRE/UniVaR-lambda-1) [code](https://github.com/HLTCHKUST/UniVaR) |
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
> URL appears exactly once. Provenance and scope remain available in the
> downloadable data and on the interactive site rather than after each link.

**Entry format:** `(subdomain) Title — venue — date — [paper] [code] [dataset]`.
When the source does not name a value model, the parenthetical label falls
back to the nearest research subdomain rather than inventing one.

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

### 📚 Publications by research topic

<a id="catalog-surveys-reviews-and-field-overviews"></a>

#### 🗺️ Surveys, reviews, and field overviews · 49

- (Surveys, reviews, and field overviews) **A roadmap for evaluating moral competence in large language models** — Nature — 2026 — [paper](https://nature.com/articles/s41586-025-10021-1)
- (Surveys, reviews, and field overviews) **A Survey of Progress in LLM Alignment from the Perspective of Reward Design** — IEEE Xplore — 2026 — [paper](https://ieeexplore.ieee.org/abstract/document/11361384)
- (Surveys, reviews, and field overviews) **A Survey on Evaluation of Large Language Models** — arXiv — 2023.07 — [paper](https://arxiv.org/abs/2307.03109) [code](https://github.com/MLGroupJLU/LLM-eval-survey)
- (Surveys, reviews, and field overviews) **A Survey on Human-Centric LLMs** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.14491)
- (Surveys, reviews, and field overviews) **A Survey on Large Language Model based Autonomous Agents** — arXiv — 2023 — [paper](https://arxiv.org/abs/2308.11432) [code](https://github.com/Paitesanshi/LLM-Agent-Survey)
- (Surveys, reviews, and field overviews) **A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.17003)
- (Surveys, reviews, and field overviews) **A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.07070)
- (Surveys, reviews, and field overviews) **AI Alignment and Social Choice: Fundamental Limitations and Policy Implications** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.16048)
- (Surveys, reviews, and field overviews) **AI Alignment From Social Choice Perspectives** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.21550)
- (Surveys, reviews, and field overviews) **AI Alignment: A Comprehensive Survey** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.19852) [project](https://alignmentsurvey.com/)
- (Surveys, reviews, and field overviews) **Aligning Large Language Models with Human: A Survey** — arXiv — 2023 — [paper](https://arxiv.org/abs/2307.12966) [code](https://github.com/GaryYufei/AlignLLMHumanSurvey)
- (Surveys, reviews, and field overviews) **Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap** — arXiv — 2025 — [paper](https://arxiv.org/abs/2508.18646)
- (Surveys, reviews, and field overviews) **Cultural Bias and Cultural Alignment of Large Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.14096)
- (Surveys, reviews, and field overviews) **Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.08858)
- (Surveys, reviews, and field overviews) **Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens** — arXiv — 2025 — [paper](https://arxiv.org/abs/2508.16982)
- (Surveys, reviews, and field overviews) **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents** — arXiv — 2024 — [paper](https://arxiv.org/abs/2412.03563) [code](https://github.com/FudanDISC/SocialAgent)
- (Surveys, reviews, and field overviews) **From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2308.12014) [code](https://github.com/ValueCompass/Alignment-Goal-Survey)
- (Surveys, reviews, and field overviews) **Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications** — arXiv — 2025.04 — [paper](https://arxiv.org/abs/2505.00049)
- (Surveys, reviews, and field overviews) **Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.19364)
- (Surveys, reviews, and field overviews) **Large Language Model based Multi-Agents: A Survey of Progress and Challenges** — arXiv — 2024.01 — [paper](https://arxiv.org/abs/2402.01680) [code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)
- (Surveys, reviews, and field overviews) **Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.08245)
- (Surveys, reviews, and field overviews) **Large language models empowered agent-based modeling and simulation: a survey and perspectives** — Humanities and Social Sciences Communications — 2024 — [paper](https://nature.com/articles/s41599-024-03611-3)
- (Surveys, reviews, and field overviews) **Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.07629)
- (Surveys, reviews, and field overviews) **LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency** — Springer journal or proceedings — 2026 — [paper](https://link.springer.com/article/10.1007/s12559-026-10568-9)
- (Surveys, reviews, and field overviews) **LLM Social Simulations Are a Promising Research Method** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.02234)
- (Surveys, reviews, and field overviews) **LLM-Based Social Simulations Require a Boundary** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.19806)
- (Surveys, reviews, and field overviews) **LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.05579)
- (Surveys, reviews, and field overviews) **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs** — Findings of ACL — 2025 — [paper](https://aclanthology.org/2025.findings-acl.1246/) [code](https://github.com/Indiiigo/LLM_rep_review)
- (Surveys, reviews, and field overviews) **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.01864)
- (Surveys, reviews, and field overviews) **Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.03003)
- (Surveys, reviews, and field overviews) **Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.14476)
- (Surveys, reviews, and field overviews) **Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback** — arXiv — 2023 — [paper](https://arxiv.org/abs/2303.05453)
- (Surveys, reviews, and field overviews) **Personalization of Large Language Models: A Survey** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.00027)
- (Surveys, reviews, and field overviews) **Personalized Multimodal Large Language Models: A Survey** — arXiv — 2024 — [paper](https://arxiv.org/abs/2412.02142)
- (Surveys, reviews, and field overviews) **Position: A Roadmap to Pluralistic Alignment** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=gQpBnRHwxM)
- (Surveys, reviews, and field overviews) **Position: AI Agents Are Not (Yet) a Panacea for Social Simulation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.00113)
- (Surveys, reviews, and field overviews) **Position: Towards Bidirectional Human-AI Alignment** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.09264)
- (Surveys, reviews, and field overviews) **Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations** — LREC-COLING — 2024 — [paper](https://aclanthology.org/2024.lrec-main.1192/)
- (Surveys, reviews, and field overviews) **Simulating Society Requires Simulating Thought** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.06958)
- (Surveys, reviews, and field overviews) **Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.10271)
- (Surveys, reviews, and field overviews) **Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.18890)
- (Surveys, reviews, and field overviews) **The benefits, risks and bounds of personalizing the alignment of large language models to individuals** — Nature Machine Intelligence — 2024 — [paper](https://nature.com/articles/s42256-024-00820-y)
- (Surveys, reviews, and field overviews) **The Mind in the Machine: A Survey of Incorporating Psychological Theories in LLMs** — arXiv — 2025.05 — [paper](https://arxiv.org/abs/2505.00003)
- (Surveys, reviews, and field overviews) **The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.18682)
- (Surveys, reviews, and field overviews) **The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.16468)
- (Surveys, reviews, and field overviews) **The threat of analytic flexibility in using large language models to simulate human data: A call to attention** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.13397)
- (Surveys, reviews, and field overviews) **Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents** — arXiv — 2025.03 — [paper](https://arxiv.org/abs/2503.24047)
- (Surveys, reviews, and field overviews) **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization** — Findings of EMNLP — 2024 — [paper](https://aclanthology.org/2024.findings-emnlp.969/)
- (Surveys, reviews, and field overviews) **When large language models meet personalization: perspectives of challenges and opportunities** — Springer journal or proceedings — 2024 — [paper](https://doi.org/10.1007/s11280-024-01276-1)

<a id="catalog-foundations-and-value-theory"></a>

#### 🧭 Foundations and value theory · 7

- (Foundations and value theory) **Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values** — JMIR — 2024 — [paper](https://doi.org/10.2196/55988) [link](https://mental.jmir.org/2024/1/e55988)
- (Foundations and value theory) **Axioms for AI Alignment from Human Feedback** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.14758)
- (Foundations and value theory) **Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement** — SAGE journal — 2001 — [paper](https://doi.org/10.1177/0022022101032005001)
- (Foundations and value theory) **Moral foundations theory: The pragmatic validity of moral pluralism. Graham et al. Advances in experimental social psychology, 2013.** — Elsevier journal or book — 2013 — [paper](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)
- (Foundations and value theory) **Optimized Distortion in Linear Social Choice** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.20020)
- (Foundations and value theory) **Representative Social Choice: From Learning Theory to AI Alignment** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.23953)
- (Foundations and value theory) **Strategy-proofness and Arrow's Conditions** — Elsevier journal or book — 1975 — [paper](https://sciencedirect.com/science/article/pii/0022053175900502)

<a id="catalog-datasets-and-benchmarks"></a>

#### 🗂️ Datasets and benchmarks · 103

- (ETHICS) **Aligning AI With Shared Human Values** — arXiv — 2020 — [paper](https://arxiv.org/abs/2008.02275) [code](https://github.com/hendrycks/ethics)
- (MoralChoice) **Evaluating the Moral Beliefs Encoded in LLMs** — arXiv — 2023 — [paper](https://arxiv.org/abs/2307.14324)
- (NYTBookOpinions) **Benchmarking Distributional Alignment of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.05403)
- (Valueeval) **The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments** — arXiv — 2023 — [paper](https://arxiv.org/abs/2301.13771)
- (Datasets and benchmarks) **A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values** — OpenReview — 2025 — [paper](https://openreview.net/forum?id=oSRqZO2O2O)
- (Datasets and benchmarks) **A Unified Moral-Value Dataset for Instruction Tuning** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.21279)
- (Datasets and benchmarks) **Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.13300)
- (Datasets and benchmarks) **Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.10365)
- (Datasets and benchmarks) **An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.01247) [code](https://github.com/simran-khanuja/image-transcreation)
- (Datasets and benchmarks) **Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.14083)
- (Datasets and benchmarks) **Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models** — NeurIPS — 2024 — [paper](https://arxiv.org/abs/2402.11894)
- (Datasets and benchmarks) **BBQ: A hand-built bias benchmark for question answering** — Findings of ACL — 2022 — [paper](https://aclanthology.org/2022.findings-acl.165/)
- (Datasets and benchmarks) **Benchmarking Distributional Alignment of Large Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.2/)
- (Datasets and benchmarks) **Benchmarking Multi-National Value Alignment for Large Language Models** — arXiv — 2025.04 — [paper](https://arxiv.org/abs/2504.12911)
- (Datasets and benchmarks) **Benchmarking Overton Pluralism in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2512.01351)
- (Datasets and benchmarks) **Beyond Aesthetics: Cultural Competence in Text-to-Image Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.06863) [code](https://github.com/google-research-datasets/cube)
- (Datasets and benchmarks) **Big-Math 2025-2** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.17387) [dataset](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified) [code](https://github.com/SynthLabsAI/big-math)
- (Datasets and benchmarks) **Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys** — arXiv — 2024 — [paper](https://arxiv.org/abs/2401.10352) [code](https://github.com/yongcaoplus/cuDialog)
- (Datasets and benchmarks) **C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.01495)
- (Datasets and benchmarks) **Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.05154)
- (Datasets and benchmarks) **Can Language Models Reason about Individualistic Human Values and Preferences?** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.336/)
- (Datasets and benchmarks) **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.13974)
- (Datasets and benchmarks) **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models** — AIES — 2024 — [paper](https://ojs.aaai.org/index.php/AIES/article/view/31710)
- (Datasets and benchmarks) **CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.10823)
- (Datasets and benchmarks) **CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean** — arXiv — 2024 — [paper](https://arxiv.org/abs/2403.06412) [code](https://github.com/rladmstn1714/CLIcK)
- (Datasets and benchmarks) **COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values** — arXiv — 2025.04 — [paper](https://arxiv.org/abs/2504.05535)
- (Datasets and benchmarks) **ComPO: Community Preferences for Language Model Personalization** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.419/)
- (Datasets and benchmarks) **Cultural Commonsense Knowledge for Intercultural Dialogues** — CIKM — 2024 — [paper](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768) [dataset](https://mango.mpi-inf.mpg.de/)
- (Datasets and benchmarks) **Culturally Aware Natural Language Inference** — Findings of EMNLP — 2023 — [paper](https://aclanthology.org/2023.findings-emnlp.509/) [code](https://github.com/SALT-NLP/CulturallyAwareNLI)
- (Datasets and benchmarks) **D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.19834)
- (Datasets and benchmarks) **Datasheets for datasets** — ACM proceedings or journal — 2021 — [paper](https://doi.org/10.1145/3458723)
- (Datasets and benchmarks) **DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.17399) [dataset](https://huggingface.co/datasets/nlip/DIWALI) [project](https://nlip-lab.github.io/nlip/publications/diwali/) [code](https://github.com/pramitsahoo/culture-evaluation)
- (Datasets and benchmarks) **DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures** — arXiv — 2024 — [paper](https://arxiv.org/abs/2403.14651) [code](https://github.com/microsoft/DOSA)
- (Datasets and benchmarks) **EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English** — arXiv — 2022 — [paper](https://arxiv.org/abs/2203.14498)
- (Datasets and benchmarks) **Evaluating and Inducing Personality in Pre-trained Language Models** — arXiv — 2022 — [paper](https://arxiv.org/abs/2206.07550)
- (Datasets and benchmarks) **Evaluating the Prompt Steerability of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.12405)
- (Datasets and benchmarks) **EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.06370)
- (Datasets and benchmarks) **Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.17838)
- (Datasets and benchmarks) **Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis** — arXiv — 2024 — [paper](https://arxiv.org/abs/2308.16705) [code](https://github.com/nlee0212/CREHate)
- (Datasets and benchmarks) **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.1063/) [dataset](https://huggingface.co/datasets/lyan62/FoodieQA) [code](https://github.com/lyan62/FoodieQA)
- (Datasets and benchmarks) **FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models** — Findings of ACL — 2023 — [paper](https://aclanthology.org/2023.findings-acl.631/) [code](https://github.com/shramay-palta/FORK_ACL2023)
- (Datasets and benchmarks) **GeoDE: a Geographically Diverse Evaluation Dataset for Object Recognition** — arXiv — 2023 — [paper](https://arxiv.org/abs/2301.02560) [link](https://geodiverse-data-collection.cs.princeton.edu/)
- (Datasets and benchmarks) **GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.13766) [model](https://huggingface.co/floschne) [code](https://github.com/floschne/gimmick)
- (Datasets and benchmarks) **Global Voices, Local Biases: Socio-Cultural Prejudices across Languages** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.17586) [code](https://github.com/iamshnoo/weathub)
- (Datasets and benchmarks) **HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter** — ACL Outstanding Paper — 2025 — [paper](https://arxiv.org/abs/2411.15462)
- (Datasets and benchmarks) **HelpSteer 2: Open-source dataset for training top-performing reward models** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)
- (Datasets and benchmarks) **KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge** — Findings of ACL — 2024 — [paper](https://aclanthology.org/2024.findings-acl.666/)
- (Datasets and benchmarks) **LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.01894)
- (Datasets and benchmarks) **LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.00853)
- (Datasets and benchmarks) **M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.03791) [code](https://github.com/floschne/m5b)
- (Datasets and benchmarks) **Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.09369) [code](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)
- (Datasets and benchmarks) **MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.19073)
- (Datasets and benchmarks) **MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=kyfkMRT4Ao)
- (Datasets and benchmarks) **Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment** — SAGE journal — 2020 — [paper](https://journals.sagepub.com/doi/10.1177/1948550619876629)
- (Datasets and benchmarks) **Moral foundations twitter corpus: A collection of 35k tweets annotated for moral sentiment. Hoover et al. Social Psychological and Personality Science 2020.** — SAGE journal — 2020 — [paper](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)
- (Datasets and benchmarks) **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences** — arXiv — 2020 — [paper](https://arxiv.org/abs/2012.15738) [code](https://github.com/demelin/moral_stories)
- (Datasets and benchmarks) **MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.16380)
- (Datasets and benchmarks) **Multi-lingual and Multi-cultural Figurative Language Understanding** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.16171) [code](https://github.com/simran-khanuja/Multilingual-Fig-QA)
- (Datasets and benchmarks) **Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision-Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.490/) [dataset](https://huggingface.co/datasets/MinhDucBui/Multi3Hate) [code](https://github.com/MinhDucBui/Multi3Hate)
- (Datasets and benchmarks) **Navigating the Cultural Kaleidoscope: A Hitchhiker’s Guide to Sensitivity in Large Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.388/)
- (Datasets and benchmarks) **NLPositionality: Characterizing Design Biases of Datasets and Models** — ACL — 2023 — [paper](https://aclanthology.org/2023.acl-long.505/) [project](https://nlpositionality.cs.washington.edu/)
- (Datasets and benchmarks) **NormBank: A Knowledge Bank of Situational Social Norms** — ACL — 2023 — [paper](https://aclanthology.org/2023.acl-long.429/)
- (Datasets and benchmarks) **NormBank: A Knowledge Bank of Situational Social Norms** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.17008)
- (Datasets and benchmarks) **NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly** — arXiv — 2023 — [paper](https://arxiv.org/abs/2210.08604) [code](https://github.com/yrf1/NormSage)
- (Datasets and benchmarks) **NoveltyBench: Evaluating Language Models for Humanlike Diversity** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.05228)
- (Datasets and benchmarks) **PerSpectra: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.08716)
- (Datasets and benchmarks) **PLURAL: A Global Dataset for Value Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.08034)
- (Datasets and benchmarks) **PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.08951)
- (Datasets and benchmarks) **Polar: A Benchmark for Evaluating Political Bias in LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.12922)
- (Datasets and benchmarks) **Process for adapting language models to society (palms) with values-targeted datasets. Solaiman et al. Neurips 2021.** — NeurIPS — 2021 — [paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)
- (Datasets and benchmarks) **ProsocialDialog: A Prosocial Backbone for Conversational Agents** — arXiv — 2022 — [paper](https://arxiv.org/abs/2205.12688)
- (Datasets and benchmarks) **Re-contextualizing Fairness in NLP: The Case of India** — arXiv — 2022 — [paper](https://arxiv.org/abs/2209.12226) [code](https://github.com/google-research-datasets/nlp-fairness-for-india)
- (Datasets and benchmarks) **RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations** — Findings of NAACL — 2024 — [paper](https://aclanthology.org/2024.findings-naacl.196/) [code](https://github.com/zhanhl316/ReNoVi)
- (Datasets and benchmarks) **SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.** — arXiv — 2022 — [paper](https://arxiv.org/abs/2210.10045) [code](https://github.com/sharonlevy/SafeText)
- (Datasets and benchmarks) **SafeWorld: Geo-Diverse Safety Alignment** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)
- (Datasets and benchmarks) **Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes** — arXiv — 2020 — [paper](https://arxiv.org/abs/2008.09094)
- (Datasets and benchmarks) **Scruples: A corpus of community ethical judgments on 32** — 000 real-life anecdotes. Lourie et al. AAAI. — 2021 — [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396) [code](https://github.com/allenai/scruples)
- (Datasets and benchmarks) **SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.11840) [code](https://github.com/google-research-datasets/seegull)
- (Datasets and benchmarks) **Social Chemistry 101: Learning to Reason about Social and Moral Norms** — arXiv — 2020 — [paper](https://arxiv.org/abs/2011.00620) [link](https://maxwellforbes.com/social-chemistry/)
- (Datasets and benchmarks) **SocialDial: A Benchmark for Socially-Aware Dialogue Systems** — ACM Digital Library — 2023 — [paper](https://dl.acm.org/doi/10.1145/3539618.3591877) [code](https://github.com/zhanhl316/SocialDial)
- (Datasets and benchmarks) **STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.20645)
- (Datasets and benchmarks) **The Moral Foundations Reddit Corpus** — arXiv — 2022 — [paper](https://arxiv.org/abs/2208.05545)
- (Datasets and benchmarks) **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems** — ACL — 2022 — [paper](https://aclanthology.org/2022.acl-long.261/)
- (Datasets and benchmarks) **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems** — arXiv — 2022 — [paper](https://arxiv.org/abs/2204.03021) [code](https://github.com/SALT-NLP/mic)
- (Datasets and benchmarks) **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)
- (Datasets and benchmarks) **Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.17283)
- (Datasets and benchmarks) **VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.05465)
- (Datasets and benchmarks) **Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation** — ACL-DEMO — 2025 — [paper](https://aclanthology.org/2025.acl-demo.64/)
- (Datasets and benchmarks) **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.111/)
- (Datasets and benchmarks) **ValueNet: A New Dataset for Human Value Driven Dialogue System** — AAAI — 2022 — [paper](https://doi.org/10.1609/aaai.v36i10.21368)
- (Datasets and benchmarks) **ValueNet: A New Dataset for Human Value Driven Dialogue System** — AAAI — 2022 — [paper](https://ojs.aaai.org/index.php/AAAI/article/view/21368) [dataset](https://liang-qiu.github.io/ValueNet/)
- (Datasets and benchmarks) **Valuenet: A new dataset for human value driven dialogue system. Qiu et al. AAAI 2022.** — AAAI — 2022 — [paper](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)
- (Datasets and benchmarks) **Vision-Language Models under Cultural and Inclusive Considerations** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.06177)
- (Datasets and benchmarks) **Visually Grounded Reasoning across Languages and Cultures** — arXiv — 2021 — [paper](https://arxiv.org/abs/2109.13238) [project](https://marvl-challenge.github.io/)
- (Datasets and benchmarks) **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1119/)
- (Datasets and benchmarks) **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.13775)
- (Datasets and benchmarks) **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.26348)
- (Datasets and benchmarks) **Whose Opinions Do Language Models Reflect?** — arXiv — 2023 — [paper](https://arxiv.org/abs/2303.17548) [link](https://proceedings.mlr.press/v202/santurkar23a.html)
- (Datasets and benchmarks) **Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.13383)
- (Datasets and benchmarks) **WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.12705) [link](https://worldcuisines.github.io/)
- (Datasets and benchmarks) **WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models** — LREC-COLING — 2024 — [paper](https://aclanthology.org/2024.lrec-main.1539/)
- (Datasets and benchmarks) **Would you Rather? A New Benchmark for Learning Machine Alignment with Cultural Values and Social Preferences** — ACL — 2020 — [paper](https://aclanthology.org/2020.acl-main.477/)
- (Datasets and benchmarks) **XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.14063)

<a id="catalog-reliability-validity-and-auditing"></a>

#### 🔬 Reliability, validity, and auditing · 17

- (Reliability, validity, and auditing) **A large-scale replication of scenario-based experiments in psychology and management using large language models** — Nature Computational Science — 2025.08 — [paper](https://nature.com/articles/s43588-025-00840-7)
- (Reliability, validity, and auditing) **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive** — ACL 2025 Best Paper — 2025.07 — [paper](https://aclanthology.org/2025.acl-long.1454/)
- (Reliability, validity, and auditing) **A validity-guided workflow for robust large language model research in psychology** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.04491)
- (Reliability, validity, and auditing) **Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.18462)
- (Reliability, validity, and auditing) **Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing** — ACM proceedings or journal — 2020 — [paper](https://doi.org/10.1145/3351095.3372873)
- (Reliability, validity, and auditing) **Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.11254)
- (Reliability, validity, and auditing) **EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.30258)
- (Reliability, validity, and auditing) **From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.16697)
- (Reliability, validity, and auditing) **Large Language Models are not Fair Evaluators** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.511/)
- (Reliability, validity, and auditing) **Large language models that replace human participants can harmfully misportray and flatten identity groups** — Nature Machine Intelligence — 2025.03 — [paper](https://nature.com/articles/s42256-025-00986-z)
- (Reliability, validity, and auditing) **Larger and more instructable language models become less reliable** — Nature — 2024.10 — [paper](https://nature.com/articles/s41586-024-07930-y)
- (Reliability, validity, and auditing) **Model Cards for Model Reporting** — ACM proceedings or journal — 2019 — [paper](https://doi.org/10.1145/3287560.3287596)
- (Reliability, validity, and auditing) **Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History** — arXiv — 2025 — [paper](https://arxiv.org/abs/2508.04826)
- (Reliability, validity, and auditing) **POSIX: A Prompt Sensitivity Index For Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.02185)
- (Reliability, validity, and auditing) **Psychometric item validation using virtual respondents with trait-response mediators** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.05890)
- (Reliability, validity, and auditing) **Revisiting the Reliability of Psychological Scales on Large Language Models** — EMNLP — 2024 — [paper](https://arxiv.org/abs/2305.19926)
- (Reliability, validity, and auditing) **You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments** — NAACL — 2024 — [paper](https://arxiv.org/abs/2311.09718)

<a id="catalog-choice-action-and-behavioral-consistency"></a>

#### 🎯 Choice, action, and behavioral consistency · 15

- (Norm) **Align on the Fly: Adapting Chatbot Behavior to Established Norms** — arXiv — 2023.12 — [paper](https://arxiv.org/abs/2312.15907) [code](https://github.com/GAIR-NLP/OPO)
- (Choice, action, and behavioral consistency) **Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.27699)
- (Choice, action, and behavioral consistency) **How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior** — Nature Human Behaviour — 2024 — [paper](https://nature.com/articles/s41562-024-01938-0.pdf)
- (Choice, action, and behavioral consistency) **How large language models can reshape collective intelligence** — Nature Human Behavior — 2024.09 — [paper](https://nature.com/articles/s41562-024-01959-9)
- (Choice, action, and behavioral consistency) **Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.1562/)
- (Choice, action, and behavioral consistency) **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.154/)
- (Choice, action, and behavioral consistency) **Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.05018)
- (Choice, action, and behavioral consistency) **Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned** — arXiv — 2022 — [paper](https://arxiv.org/abs/2209.07858) [dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- (Choice, action, and behavioral consistency) **Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.12369)
- (Choice, action, and behavioral consistency) **Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.** — arXiv — 2019 — [paper](https://arxiv.org/abs/1911.03891) [link](https://maartensap.com/social-bias-frames/)
- (Choice, action, and behavioral consistency) **The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.806/)
- (Choice, action, and behavioral consistency) **The theory of planned behavior** — Elsevier journal or book — 1991 — [paper](https://sciencedirect.com/science/article/pii/074959789190020T)
- (Choice, action, and behavioral consistency) **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback** — arXiv — 2022 — [paper](https://arxiv.org/abs/2204.05862) [code](https://github.com/anthropics/hh-rlhf)
- (Choice, action, and behavioral consistency) **Training language models to follow instructions with human feedback. Ouyang et al. Neurips 2022.** — NeurIPS — 2022 — [paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)
- (Choice, action, and behavioral consistency) **What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios** — COLING — 2025 — [paper](https://aclanthology.org/2025.coling-main.317/)

<a id="catalog-culture-language-and-pluralism"></a>

#### 🌍 Culture, language, and pluralism · 103

- (Culture, language, and pluralism) **'Too much alignment; not enough culture': Re-balancing Cultural Alignment Practices in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.26167)
- (GlobalOpinionQA) **Towards Measuring the Representation of Subjective Global Opinions in Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.16388) [dataset](https://huggingface.co/datasets/Anthropic/llm_global_opinions) [project](https://llmglobalvalues.anthropic.com/)
- (Culture, language, and pluralism) **ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.12962)
- (Culture, language, and pluralism) **An Evaluation of Cultural Value Alignment in LLM** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.08863)
- (Culture, language, and pluralism) **Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.23820)
- (Culture, language, and pluralism) **Assessing Cross-Cultural Alignment between ChatGPT and Human Societies** — arXiv — 2023 — [paper](https://arxiv.org/abs/2303.17466)
- (Culture, language, and pluralism) **Assessing LLMs for Moral Value Pluralism** — arXiv — 2023 — [paper](https://arxiv.org/abs/2312.10075)
- (Culture, language, and pluralism) **Attributing Culture-Conditioned Generations to Pretraining Corpora** — arXiv — 2025 — [paper](https://arxiv.org/abs/2412.20760) [code](https://github.com/huihanlhh/CultureGenAttr)
- (Culture, language, and pluralism) **Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.15755)
- (Culture, language, and pluralism) **BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.09948) [code](https://github.com/nlee0212/BLEnD)
- (Culture, language, and pluralism) **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.2/)
- (Culture, language, and pluralism) **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.08045)
- (Culture, language, and pluralism) **Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.01127)
- (Culture, language, and pluralism) **CARE: Multilingual Human Preference Learning for Cultural Awareness** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.05154)
- (Culture, language, and pluralism) **CAReDiO: Enhancing Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.08820)
- (Culture, language, and pluralism) **CCBench: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.05405)
- (Culture, language, and pluralism) **CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.16421)
- (Culture, language, and pluralism) **Challenges and Strategies in Cross-Cultural NLP** — arXiv — 2022 — [paper](https://arxiv.org/abs/2203.10020)
- (Culture, language, and pluralism) **Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.20229)
- (Culture, language, and pluralism) **code and data** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.12880) [code](https://github.com/NeuralSentinel/CulturalKaleidoscope)
- (Culture, language, and pluralism) **Coherence Maximization Improves Pluralistic Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.03110)
- (Culture, language, and pluralism) **Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.17256)
- (Culture, language, and pluralism) **CulFiT: Fine-grained Cultural-aware LLM Training via Multilingual Critique Data Synthesis** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.19484)
- (Culture, language, and pluralism) **Cultural Adaptation in Large Language Models for Political Discourse** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.23332)
- (Culture, language, and pluralism) **Cultural Alignment in Large Language Models Using Soft Prompt Tuning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.16094)
- (Culture, language, and pluralism) **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions** — arXiv — 2023 — [paper](https://arxiv.org/abs/2309.12342)
- (Culture, language, and pluralism) **Cultural bias and cultural alignment of large language models** — PNAS Nexus — 2024 — [paper](https://doi.org/10.1093/pnasnexus/pgae346)
- (Culture, language, and pluralism) **Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.11661)
- (Culture, language, and pluralism) **Cultural Learning-Based Culture Adaptation of Language Models** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.156/)
- (Culture, language, and pluralism) **Cultural Learning-Based Culture Adaptation of Language Models (CLCA)** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.02953)
- (Culture, language, and pluralism) **Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette** — arXiv — 2024 — [paper](https://arxiv.org/abs/2412.11167)
- (Culture, language, and pluralism) **Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.17112)
- (Culture, language, and pluralism) **Cultural Value Alignment Via Latent Activation Steering in Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.26365)
- (Culture, language, and pluralism) **CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.02677)
- (Culture, language, and pluralism) **Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.03930)
- (Culture, language, and pluralism) **CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.06664)
- (Culture, language, and pluralism) **Culture is Not Trivia: Sociocultural Theory for Cultural NLP** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.12057)
- (Culture, language, and pluralism) **CultureBank: An Online Community-Driven Knowledge Base toward Culturally Aware Language Technologies** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.15238)
- (Culture, language, and pluralism) **CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.01879)
- (Culture, language, and pluralism) **CultureLLM: Incorporating Cultural Differences into Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.10946) [code](https://github.com/Scarelette/CultureLLM)
- (Culture, language, and pluralism) **CulturePark: Boosting Cross-cultural Understanding in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.15145)
- (Culture, language, and pluralism) **CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.10886)
- (Culture, language, and pluralism) **CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.04885)
- (Culture, language, and pluralism) **CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.12014)
- (Culture, language, and pluralism) **Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.21977)
- (Culture, language, and pluralism) **Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.06210)
- (Culture, language, and pluralism) **DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained LMs** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.05076)
- (Culture, language, and pluralism) **EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.20264)
- (Culture, language, and pluralism) **Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.18460)
- (Culture, language, and pluralism) **EtiCor: Corpus for Analyzing LLMs for Etiquettes** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.18974)
- (Culture, language, and pluralism) **Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.21798)
- (Culture, language, and pluralism) **Evaluating Pluralism in LLMs through Latent Perspectives** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.13254)
- (Culture, language, and pluralism) **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.04045)
- (Culture, language, and pluralism) **Exploring Cultural Variations in Moral Judgments with Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.12433)
- (Culture, language, and pluralism) **Extrinsic Evaluation of Cultural Competence in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.11565)
- (Culture, language, and pluralism) **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.17692)
- (Culture, language, and pluralism) **From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.16408)
- (Culture, language, and pluralism) **Having Beer after Prayer? Measuring Cultural Bias in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2305.14456) [code](https://github.com/tareknaous/camel)
- (Culture, language, and pluralism) **Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.05931)
- (Culture, language, and pluralism) **How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.17773)
- (Culture, language, and pluralism) **How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.14805)
- (Culture, language, and pluralism) **Improving Cross-Cultural Survey Simulation with Calibrated Value Personas** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.16193)
- (Culture, language, and pluralism) **Investigating Cultural Alignment of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.13231)
- (Culture, language, and pluralism) **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.16761)
- (Culture, language, and pluralism) **Large Language Models as Superpositions of Cultural Perspectives** — arXiv — 2023 — [paper](https://arxiv.org/abs/2307.07870) [link](https://gitlab.inria.fr/gkovac/value_stability)
- (Culture, language, and pluralism) **Legal Theory for Pluralistic Alignment** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.17271)
- (Culture, language, and pluralism) **Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.08797)
- (Culture, language, and pluralism) **LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.15003)
- (Culture, language, and pluralism) **LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.06032)
- (Culture, language, and pluralism) **Made-in China, Thinking in America: U.S. Values Persist in Chinese LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2512.13723)
- (Culture, language, and pluralism) **Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.09637)
- (Culture, language, and pluralism) **Meta-Learning Preferences for Multilingual LLM Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.13315)
- (Culture, language, and pluralism) **Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.22475)
- (Culture, language, and pluralism) **Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.12091)
- (Culture, language, and pluralism) **Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.16534)
- (Culture, language, and pluralism) **Multilingual Language Models are not Multicultural: A Case Study in Emotion** — arXiv — 2023 — [paper](https://arxiv.org/abs/2307.01370)
- (Culture, language, and pluralism) **NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.18383)
- (Culture, language, and pluralism) **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.12464) [code](https://github.com/Akhila-Yerukola/NormAd)
- (Culture, language, and pluralism) **On the steerability of large language models toward data-driven personas** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.04978)
- (Culture, language, and pluralism) **Overton Pluralistic Reinforcement Learning for Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.20759)
- (Culture, language, and pluralism) **Pluralistic Alignment for Healthcare: A Role-Driven Framework** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.10685)
- (Culture, language, and pluralism) **Plurals: A System for Guiding LLMs Via Simulated Social Ensembles** — arXiv — 2024 — [paper](https://arxiv.org/abs/2409.17213)
- (Culture, language, and pluralism) **POW: Political Overton Windows of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.08853)
- (Culture, language, and pluralism) **Probing Pre-Trained Language Models for Cross-Cultural Differences in Values** — arXiv — 2022 — [paper](https://arxiv.org/abs/2203.13722)
- (Culture, language, and pluralism) **Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.11311)
- (Culture, language, and pluralism) **Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.08688)
- (Culture, language, and pluralism) **RLHF: A Comprehensive Survey for Cultural, Multimodal and Low-Latency Alignment Methods** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.03939)
- (Culture, language, and pluralism) **Self-Pluralising Culture Alignment for Large Language Models (CultureSPA)** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.12971)
- (Culture, language, and pluralism) **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.07068)
- (Culture, language, and pluralism) **Steerable Cultural Preference Optimization of Reward Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.18606)
- (Culture, language, and pluralism) **Steering LLMs for Culturally Localized Generation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.23301)
- (Culture, language, and pluralism) **Survey of Cultural Awareness in Language Models: Text and Beyond** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.00860)
- (Culture, language, and pluralism) **The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.12744)
- (Culture, language, and pluralism) **The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.20225)
- (Culture, language, and pluralism) **Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.21700)
- (Culture, language, and pluralism) **Toward Culturally Grounded Natural Language Processing** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.26013)
- (Culture, language, and pluralism) **Towards Measuring and Modeling "Culture" in LLMs: A Survey** — arXiv — 2024 — [paper](https://arxiv.org/abs/2403.15412) [code](https://github.com/faridlazuarda/cultural-llm-papers)
- (Culture, language, and pluralism) **Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation** — Elsevier journal or book — 2025 — [paper](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)
- (Culture, language, and pluralism) **Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.12878)
- (Culture, language, and pluralism) **Value kaleidoscope: engaging AI with pluralistic human values, rights, and duties** — AAAI — 2024 — [paper](https://doi.org/10.1609/aaai.v38i18.29970)
- (Culture, language, and pluralism) **Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.00242)
- (Culture, language, and pluralism) **WorldValuesBench: A Large-Scale Benchmark for Multi-Cultural Value Awareness of Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.16308)
- (Culture, language, and pluralism) **XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.05662)

<a id="catalog-preferences-opinions-and-social-simulation"></a>

#### 🗣️ Preferences, opinions, and social simulation · 120

- (ANES) **CommunityLM: Probing Partisan Worldviews from Language Models** — COLING — 2022 — [paper](https://arxiv.org/abs/2209.07065)
- (ANES) **Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information** — arXiv — 2024.02 — [paper](https://arxiv.org/abs/2402.18144)
- (ANES) **Representation Bias in Political Sample Simulations with Large Language Models** — arXiv — 2024.07 — [paper](https://arxiv.org/abs/2407.11409)
- (ANES) **Unpacking Political Bias in Large Language Models: A Cross-Model Comparison on U.S. Politics** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.16746)
- (Culture) **Cultural tendencies in generative AI** — Nature Human Behaviour — 2025.06 — [paper](https://nature.com/articles/s41562-025-02242-1)
- (GLES) **Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.13169)
- (GLES) **Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.16280)
- (GLES) **Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion** — arXiv — 2024.07 — [paper](https://arxiv.org/abs/2407.08563)
- (Other / custom) **AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction** — arXiv — 2023.05 — [paper](https://arxiv.org/abs/2305.09620)
- (Other / custom) **Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys** — arXiv — 2024.05 — [paper](https://arxiv.org/abs/2405.19323)
- (Other / custom) **Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs** — arXiv — 2025.05 — [paper](https://arxiv.org/abs/2503.13149)
- (Other / custom) **Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.18282)
- (Other / custom) **Demonstrations of the Potential of AI-based Political Issue Polling** — Harvard Data Science Review (HDSR) — 2023.07 — [paper](https://arxiv.org/abs/2307.04781)
- (Other / custom) **From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models** — ACL — 2023 — [paper](https://arxiv.org/abs/2305.08283)
- (Other / custom) **How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?** — Digital Society — 2023.07 — [paper](https://link.springer.com/article/10.1007/s44206-023-00054-2)
- (Other / custom) **IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.08395)
- (Other / custom) **Large Language Models Can Be Used to Estimate the Latent Positions of Politicians** — arXiv — 2023.03 — [paper](https://arxiv.org/abs/2303.12057)
- (Other / custom) **Linear Representations of Political Perspective Emerge in Large Language Models** — arXiv — 2025.03 — [paper](https://arxiv.org/abs/2503.02080)
- (Other / custom) **Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs** — NAACL (Short Paper — 2024 — [paper](https://arxiv.org/abs/2403.13592)
- (Other / custom) **Questioning the Survey Responses of Large Language Models** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)
- (PCT) **Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.14843)
- (PCT) **Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias** — arXiv — 2026.01 — [paper](https://arxiv.org/abs/2601.06194)
- (PCT) **Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models** — ACL — 2024 — [paper](https://arxiv.org/abs/2402.16786)
- (PCT) **PRISM: A Methodology for Auditing Biases in Large Language Models** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.18906)
- (PCT) **Revealing Fine-Grained Values and Opinions in Large Language Models** — EMNLP Findings — 2024 — [paper](https://arxiv.org/abs/2406.19238)
- (PCT) **The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation** — arXiv — 2023.01 — [paper](https://arxiv.org/abs/2301.01768)
- (PCT) **The Self-Perception and Political Biases of ChatGPT** — Human Behavior and Emerging Technologies — 2024.07 — [paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)
- (Preferences, opinions, and social simulation) **A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.14106)
- (Preferences, opinions, and social simulation) **AI PERSONA: Towards Life-long Personalization of LLMs** — arXiv — 2024 — [paper](https://arxiv.org/abs/2412.13103)
- (Preferences, opinions, and social simulation) **Aligning Language Models from User Interactions** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.12273)
- (Preferences, opinions, and social simulation) **Aligning Large Language Models with Diverse Political Viewpoints** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.412/)
- (Preferences, opinions, and social simulation) **Aligning LLMs with Individual Preferences via Interaction** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.03642)
- (Preferences, opinions, and social simulation) **Aligning to Thousands of Preferences via System Message Generalization** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.17977)
- (Preferences, opinions, and social simulation) **Aligning VLM Assistants with Personalized Situated Cognition** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.00930)
- (Preferences, opinions, and social simulation) **AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.26680)
- (Preferences, opinions, and social simulation) **Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.19148)
- (Preferences, opinions, and social simulation) **APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.21063)
- (Preferences, opinions, and social simulation) **APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.27419)
- (Preferences, opinions, and social simulation) **BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization** — Findings of EMNLP — 2024 — [paper](https://aclanthology.org/2024.findings-emnlp.398/)
- (Preferences, opinions, and social simulation) **Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.02300)
- (Preferences, opinions, and social simulation) **COMPO: Community Preferences for Language Model Personalization** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.16027)
- (Preferences, opinions, and social simulation) **Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.08968)
- (Preferences, opinions, and social simulation) **CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.14773)
- (Preferences, opinions, and social simulation) **CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.04756)
- (Preferences, opinions, and social simulation) **Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.18310)
- (Preferences, opinions, and social simulation) **Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2309.03126)
- (Preferences, opinions, and social simulation) **Drift: Decoding-time Personalized Alignments with Implicit User Preferences** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.14289)
- (Preferences, opinions, and social simulation) **EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.26883)
- (Preferences, opinions, and social simulation) **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.16348)
- (Preferences, opinions, and social simulation) **EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.16545)
- (Preferences, opinions, and social simulation) **Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.20589)
- (Preferences, opinions, and social simulation) **Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.18071)
- (Preferences, opinions, and social simulation) **Few-shot Personalization of LLMs with Mis-aligned Responses** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.18678)
- (Preferences, opinions, and social simulation) **From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.15463)
- (Preferences, opinions, and social simulation) **From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.23382)
- (Preferences, opinions, and social simulation) **From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.16303)
- (Preferences, opinions, and social simulation) **From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.00728)
- (Preferences, opinions, and social simulation) **From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.16610)
- (Preferences, opinions, and social simulation) **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.20006)
- (Preferences, opinions, and social simulation) **From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.18271)
- (Preferences, opinions, and social simulation) **Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.24647)
- (Preferences, opinions, and social simulation) **Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.16120)
- (Preferences, opinions, and social simulation) **Large Language Models Empowered Personalized Web Agents** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.17236)
- (Preferences, opinions, and social simulation) **Learning to summarize user information for personalized reinforcement learning from human feedback** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=Ar078WR3um)
- (Preferences, opinions, and social simulation) **LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.14012)
- (Preferences, opinions, and social simulation) **MAP: Multi-Human-Value Alignment Palette** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=NN6QHwgRrQ)
- (Preferences, opinions, and social simulation) **MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.25342)
- (Preferences, opinions, and social simulation) **MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.14184)
- (Preferences, opinions, and social simulation) **MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.24846)
- (Preferences, opinions, and social simulation) **More human than human: measuring ChatGPT political bias** — Springer journal or proceedings — 2023 — [paper](https://link.springer.com/article/10.1007/s11127-023-01097-2)
- (Preferences, opinions, and social simulation) **NextQuill: Causal Preference Modeling for Enhancing LLM Personalization** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=xYpVlKMFqv)
- (Preferences, opinions, and social simulation) **Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1529/)
- (Preferences, opinions, and social simulation) **Opinion dynamics and mutual influence with LLM agents through dialog simulation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.12583)
- (Preferences, opinions, and social simulation) **P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=hXNApWLBZG)
- (Preferences, opinions, and social simulation) **PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=1kFDrYCuSu)
- (Preferences, opinions, and social simulation) **PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2608.04003)
- (Preferences, opinions, and social simulation) **Persona-Based Simulation of Human Opinion at Population Scale** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.27056)
- (Preferences, opinions, and social simulation) **Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.11060)
- (Preferences, opinions, and social simulation) **Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.12663)
- (Preferences, opinions, and social simulation) **PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.06254)
- (Preferences, opinions, and social simulation) **PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.12915)
- (Preferences, opinions, and social simulation) **PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.09902)
- (Preferences, opinions, and social simulation) **Personalized Adaptation via In-Context Preference Learning** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.14001)
- (Preferences, opinions, and social simulation) **Personalized Benchmarking: Evaluating LLMs by Individual Preferences** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.18943)
- (Preferences, opinions, and social simulation) **Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.10009)
- (Preferences, opinions, and social simulation) **Personalized Language Modeling from Personalized Human Feedback** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.05133)
- (Preferences, opinions, and social simulation) **Personalized LLM Decoding via Contrasting Personal Preference** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.12109)
- (Preferences, opinions, and social simulation) **Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=O1hfVE0UxG)
- (Preferences, opinions, and social simulation) **Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.07343)
- (Preferences, opinions, and social simulation) **Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.11564)
- (Preferences, opinions, and social simulation) **Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.10075)
- (Preferences, opinions, and social simulation) **PersonalLLM: Tailoring LLMs to Individual Preferences** — arXiv — 2024 — [paper](https://arxiv.org/abs/2409.20296)
- (Preferences, opinions, and social simulation) **PersonaVLM: Long-Term Personalized Multimodal LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.13074)
- (Preferences, opinions, and social simulation) **PEToolLLM: Towards Personalized Tool Learning in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.18980)
- (Preferences, opinions, and social simulation) **Political-LLM: Large Language Models in Political Science** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.06864) [project](https://political-llm.org/)
- (Preferences, opinions, and social simulation) **POPI: Personalizing LLMs via Optimized Natural Language Preference Inference** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.17881)
- (Preferences, opinions, and social simulation) **Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.22345)
- (Preferences, opinions, and social simulation) **Preference-Aware Rubric Learning for Personalized Evaluation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.31545)
- (Preferences, opinions, and social simulation) **PrefPalette: Personalized Preference Modeling with Latent Attributes** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.13541)
- (Preferences, opinions, and social simulation) **PRIME: Large Language Model Personalization with Cognitive Memory and Thought Processes** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.04607)
- (Preferences, opinions, and social simulation) **Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.17571)
- (Preferences, opinions, and social simulation) **RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.00254)
- (Preferences, opinions, and social simulation) **Show, Don't Tell: Aligning Language Models with Demonstrated Feedback** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.00888)
- (Preferences, opinions, and social simulation) **Silicon Sampling via Cross-Survey Transfer** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.03091)
- (Preferences, opinions, and social simulation) **Steering Large Language Models for Machine Translation Personalization** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.16612)
- (Preferences, opinions, and social simulation) **Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=nc28mSbyVG)
- (Preferences, opinions, and social simulation) **SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.05598)
- (Preferences, opinions, and social simulation) **Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.15456)
- (Preferences, opinions, and social simulation) **Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.10991)
- (Preferences, opinions, and social simulation) **The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads** — arXiv — 2026 — [paper](https://arxiv.org/abs/2608.04570)
- (Preferences, opinions, and social simulation) **The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.11096)
- (Preferences, opinions, and social simulation) **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.16019) [code](https://github.com/HannahKirk/prism-alignment)
- (Preferences, opinions, and social simulation) **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=DFr5hteojx)
- (Preferences, opinions, and social simulation) **Think-While-Generating: On-the-Fly Reasoning for Personalized Long-Form Generation** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=lle0aGQyQb)
- (Preferences, opinions, and social simulation) **Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.07018)
- (Preferences, opinions, and social simulation) **Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.18849)
- (Preferences, opinions, and social simulation) **TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.01755)
- (Preferences, opinions, and social simulation) **What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=sC6A1bFDUt)
- (Preferences, opinions, and social simulation) **When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.24613)
- (Preferences, opinions, and social simulation) **When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.19158)

<a id="catalog-moral-reasoning-and-value-understanding"></a>

#### ⚖️ Moral reasoning and value understanding · 63

- (DIT) **Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test** — arXiv — 2024.02 — [paper](https://arxiv.org/abs/2402.02135)
- (DIT) **Probing the Moral Development of Large Language Models through Defining Issues Test** — arXiv — 2023.09 — [paper](https://arxiv.org/abs/2309.13356)
- (ETHICS) **An Evaluation of GPT-4 on the ETHICS Dataset** — arXiv — 2023.09 — [paper](https://arxiv.org/abs/2309.10492)
- (ETHICS) **Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety** — NeurIPS Workshop — 2022 — [paper](https://arxiv.org/abs/2212.06295)
- (ETHICS) **EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval** — SIGIR-AP — 2023 — [paper](https://dl.acm.org/doi/abs/10.1145/3624918.3625327) [code](https://github.com/wanng-ide/ealm)
- (ETHICS) **Inducing Human-like Biases in Moral Reasoning Language Models** — arXiv — 2024.11 — [paper](https://arxiv.org/abs/2411.15386)
- (MFT) **Analyzing the Ethical Logic of Six Large Language Models** — arXiv — 2025.01 — [paper](https://arxiv.org/abs/2501.08951)
- (MFT) **Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations** — AIES — 2024 — [paper](https://ojs.aaai.org/index.php/AIES/article/view/31704)
- (MFT) **Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy** — NAACL Workshop — 2022 — [paper](https://arxiv.org/abs/2205.12771)
- (MFT) **Exploring and steering the moral compass of Large Language Models** — ICPR — 2024 — [paper](https://arxiv.org/abs/2405.17345)
- (MFT) **M3oralBench: A MultiModal Moral Benchmark for LVLMs** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.20718)
- (MFT) **Moral Foundations of Large Language Models** — EMNLP — 2024 — [paper](https://arxiv.org/abs/2310.15337)
- (MFT) **Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity** — ACL Workshop — 2023 — [paper](https://arxiv.org/abs/2209.12106)
- (MFT) **MoralBench: Moral Evaluation of LLMs** — arXiv — 2024.06 — [paper](https://arxiv.org/abs/2406.04428) [code](https://github.com/agiresearch/MoralBench)
- (MFT) **Towards "Differential AI Psychology" and in-context Value-driven Statement Alignment with Moral Foundations Theory** — arXiv — 2024.08 — [paper](https://arxiv.org/abs/2408.11415)
- (MFT) **Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.18863)
- (Other / custom) **Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral** — ACL 2025 Best Resource Paper — 2025.07 — [paper](https://aclanthology.org/2025.acl-long.294/)
- (Other / custom) **Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment** — AIES — 2024 — [paper](https://ojs.aaai.org/index.php/AIES/article/view/31741)
- (Other / custom) **Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?** — C3NLP — 2024 — [paper](https://arxiv.org/abs/2406.16316)
- (Other / custom) **Evaluating Moral Beliefs across LLMs through a Pluralistic Framework** — arXiv — 2024.11 — [paper](https://arxiv.org/abs/2411.03665)
- (Other / custom) **Evaluating the Moral Beliefs Encoded in LLMs** — NeurIPS — 2023 — [paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)
- (Other / custom) **Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper)** — ACM Digital Library — 2024 — [paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)
- (Other / custom) **Knowledge of cultural moral norms in large language models** — ACL — 2023 — [paper](https://arxiv.org/abs/2306.01857)
- (Other / custom) **Large-scale moral machine experiment on large language models** — arXiv — 2024.11 — [paper](https://arxiv.org/abs/2411.06790)
- (Other / custom) **LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.00962)
- (Other / custom) **Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment** — arXiv — 2024.11 — [paper](https://arxiv.org/abs/2411.11731)
- (Other / custom) **Normative Evaluation of Large Language Models with Everyday Moral Dilemmas** — arXiv — 2025.01 — [paper](https://arxiv.org/abs/2501.18081)
- (Other / custom) **Potential benefits of employing large language models in research in moral education and development** — Journal of Moral Education — 2023.01 — [paper](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)
- (Other / custom) **Right vs. Right: Can LLMs Make Tough Choices?** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.19926)
- (Other / custom) **SaGE: Evaluating Moral Consistency in Large Language Models** — LREC-COLING — 2024 — [paper](https://arxiv.org/abs/2402.13709)
- (Other / custom) **The Moral Mind(s) of Large Language Models** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.04476)
- (Other / custom) **The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.07304)
- (Other / custom) **Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models** — arXiv — 2023.11 — [paper](https://arxiv.org/abs/2311.07792)
- (Other / custom) **What does AI consider praiseworthy?** — AI and Ethics — 2025.02 — [paper](https://link.springer.com/article/10.1007/s43681-025-00682-z)
- (Other / custom) **When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment** — NeurIPS — 2022 — [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)
- (Moral reasoning and value understanding) **Aditi Khandelwal et al. EACL 2024.** — EACL — 2024 — [paper](https://aclanthology.org/2024.eacl-long.176/)
- (Moral reasoning and value understanding) **Agent Alignment in Evolving Social Norms** — arXiv — 2024.01 — [paper](https://arxiv.org/abs/2401.04620)
- (Moral reasoning and value understanding) **Can Machines Learn Morality? The Delphi Experiment** — arXiv — 2021 — [paper](https://arxiv.org/abs/2110.07574) [project](https://delphi.allenai.org/)
- (Moral reasoning and value understanding) **CrowS-Pairs** — EMNLP — 2020 — [paper](https://aclanthology.org/2020.emnlp-main.154/) [code](https://github.com/nyu-mll/crows-pairs)
- (Moral reasoning and value understanding) **DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.02683)
- (Moral reasoning and value understanding) **Exploring the psychology of GPT-4's Moral and Legal Reasoning** — arXiv — 2023.08 — [paper](https://arxiv.org/abs/2308.01264)
- (Moral reasoning and value understanding) **How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation** — ACL Main — 2026 — [paper](https://arxiv.org/abs/2603.13876) [code](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)
- (Moral reasoning and value understanding) **Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence** — Nature Machine Intelligence — 2025.01 — [paper](https://nature.com/articles/s42256-024-00969-6)
- (Moral reasoning and value understanding) **Irene Solaiman and Christy Dennison. NeurIPS 2021.** — arXiv — 2021 — [paper](https://arxiv.org/abs/2106.10328)
- (Moral reasoning and value understanding) **Joshua Landau et al. arXiv 2023.** — arXiv — 2023 — [paper](https://arxiv.org/abs/2302.07459)
- (Moral reasoning and value understanding) **Laura Weidinger et al. arXiv 2021.** — arXiv — 2021 — [paper](https://arxiv.org/abs/2112.04359)
- (Moral reasoning and value understanding) **Learning norms from stories: A prior for value aligned agents. Nahian et al. AIES 2020.** — arXiv — 2020 — [paper](https://arxiv.org/abs/1912.03553)
- (Moral reasoning and value understanding) **Moral Foundations of Large Language Models** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.982/)
- (Moral reasoning and value understanding) **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences** — EMNLP — 2021 — [paper](https://aclanthology.org/2021.emnlp-main.54/)
- (Moral reasoning and value understanding) **MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.** — arXiv — 2023 — [paper](https://arxiv.org/abs/2212.10720) [code](https://github.com/thu-coai/MoralDial)
- (Moral reasoning and value understanding) **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.03047) [dataset](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0) [code](https://github.com/IBM/Dromedary)
- (Moral reasoning and value understanding) **Revealing the Pragmatic Dilemma for Moral Reasoning Acquisition in Language Models** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.16600)
- (Moral reasoning and value understanding) **Safety Assessment of Chinese Large Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2304.10436) [link](http://115.182.62.166:18000/) [code](https://github.com/thu-coai/Safety-Prompts)
- (Moral reasoning and value understanding) **SafetyBench 2023-9** — arXiv — 2023 — [paper](https://arxiv.org/abs/2309.07045) [dataset](https://huggingface.co/datasets/thu-coai/SafetyBench) [project](https://llmbench.ai/safety) [code](https://github.com/thu-coai/SafetyBench)
- (Moral reasoning and value understanding) **Shamik Roy et al. arXiv 2023.** — NLP+CSS — 2023 — [paper](https://aclanthology.org/2022.nlpcss-1.20/)
- (Moral reasoning and value understanding) **Shitong Duan et al. ICLR 2024.** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=m3RRWWFaVe)
- (Moral reasoning and value understanding) **Social Chemistry 101: Learning to Reason about Social and Moral Norms** — EMNLP — 2020 — [paper](https://aclanthology.org/2020.emnlp-main.48/)
- (Moral reasoning and value understanding) **Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.1541/)
- (Moral reasoning and value understanding) **TRUSTGPT 2023-6** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.11507) [code](https://github.com/HowieHwong/TrustGPT)
- (Moral reasoning and value understanding) **Utkarsh Agarwal et al. LREC/COLING 2024.** — LREC-COLING — 2024 — [paper](https://aclanthology.org/2024.lrec-main.560/)
- (Moral reasoning and value understanding) **When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.** — NeurIPS — 2022 — [paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf) [dataset](https://huggingface.co/datasets/feradauto/MoralExceptQA)
- (Moral reasoning and value understanding) **Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution** — ACL Main (Oral — 2026 — [paper](https://arxiv.org/abs/2509.17703) [code](https://github.com/MoralAgentSim/Simulation-Engine)
- (Moral reasoning and value understanding) **Xi Zhiheng et al. CCL 2023.** — CCL — 2023 — [paper](https://aclanthology.org/2023.ccl-4.2/)

<a id="catalog-alignment-steering-and-preferences"></a>

#### 🧰 Alignment, steering, and preferences · 133

- (MBTI) **Machine Mindset: An MBTI Exploration of Large Language Models** — arXiv — 2023.12 — [paper](https://arxiv.org/abs/2312.12999) [code](https://github.com/PKU-YuanGroup/Machine-Mindset)
- (Alignment, steering, and preferences) **A general language assistant as a laboratory for alignment. Askell et al. arXiv 2021.** — arXiv — 2021 — [paper](https://arxiv.org/abs/2112.00861) [dataset](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)
- (Alignment, steering, and preferences) **A Roadmap to Pluralistic Alignment** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.05070) [code](https://github.com/jfisher52/AI_Pluralistic_Alignment)
- (Alignment, steering, and preferences) **Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.01642)
- (Alignment, steering, and preferences) **AI Alignment Breaks at the Edge** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.20042)
- (Alignment, steering, and preferences) **Aligning \AI\ With Shared Human Values** — OpenReview — 2021 — [paper](https://openreview.net/forum?id=dNy_RKzJacY)
- (Alignment, steering, and preferences) **Aligning Crowd Feedback via Distributional Preference Reward Modeling** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.09764)
- (Alignment, steering, and preferences) **Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.08385)
- (Alignment, steering, and preferences) **Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping** — AAAI — 2026 — [paper](https://ojs.aaai.org/index.php/AAAI/article/view/41109)
- (Alignment, steering, and preferences) **Aligning Multimodal LLM with Human Preference: A Survey** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.14504)
- (Alignment, steering, and preferences) **Aligning to Thousands of Preferences via System Message Generalization** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)
- (Alignment, steering, and preferences) **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective** — Findings of ACL — 2025 — [paper](https://aclanthology.org/2025.findings-acl.1188/)
- (Alignment, steering, and preferences) **Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.468/)
- (Alignment, steering, and preferences) **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** — NeurIPS D&B Track Best Paper — 2025 — [paper](https://arxiv.org/abs/2510.22954)
- (Alignment, steering, and preferences) **Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.13705)
- (Alignment, steering, and preferences) **Black-Box Prompt Optimization: Aligning Large Language Models without Model Training** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.176/)
- (Alignment, steering, and preferences) **Communication-Efficient Desire Alignment for Proactive Embodied Human–Agent Interaction** — ACL Main (Oral — 2026 — [paper](https://arxiv.org/abs/2505.22503)
- (Alignment, steering, and preferences) **Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.** — arXiv — 2022 — [paper](https://arxiv.org/abs/2212.08073) [code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)
- (Alignment, steering, and preferences) **Constitutional Value Potentials: reading and steering internal priority margins in language models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.15420)
- (Alignment, steering, and preferences) **Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.85/)
- (Alignment, steering, and preferences) **Controllable Value Alignment in Large Language Models through Neuron-Level Editing** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.07356)
- (Alignment, steering, and preferences) **Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.18526)
- (Alignment, steering, and preferences) **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede’s Cultural Dimensions** — COLING — 2025 — [paper](https://aclanthology.org/2025.coling-main.567/)
- (Alignment, steering, and preferences) **CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.10199) [code](https://github.com/huihanlhh/Culture-Gen)
- (Alignment, steering, and preferences) **CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies** — Findings of EMNLP — 2024 — [paper](https://aclanthology.org/2024.findings-emnlp.288/)
- (Alignment, steering, and preferences) **CultureLLM: Incorporating Cultural Differences into Large Language Models** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)
- (Alignment, steering, and preferences) **CulturePark: Boosting Cross-cultural Understanding in Large Language Models** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)
- (Alignment, steering, and preferences) **Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.23749)
- (Alignment, steering, and preferences) **Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach** — OpenReview — 2025 — [paper](https://openreview.net/forum?id=6KM1siLL8a)
- (Alignment, steering, and preferences) **Diverging Preferences: When do Annotators Disagree and do Models Know?** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.14632)
- (Alignment, steering, and preferences) **Diverse Human Value Alignment for Large Language Models via Ethical Reasoning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.00379)
- (Alignment, steering, and preferences) **Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.10588)
- (Alignment, steering, and preferences) **DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.14420)
- (Alignment, steering, and preferences) **Evaluating and Inducing Personality in Pre-trained Language Models** — NeurIPS — 2023 — [paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)
- (Alignment, steering, and preferences) **Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.06929)
- (Alignment, steering, and preferences) **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.1301/)
- (Alignment, steering, and preferences) **Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes** — arXiv — 2024 — [paper](https://arxiv.org/abs/2412.13998)
- (Alignment, steering, and preferences) **Fine-tuning language models to find agreement among humans with diverse preferences** — arXiv — 2022 — [paper](https://arxiv.org/abs/2211.15006)
- (Alignment, steering, and preferences) **Foundational Challenges in Assuring Alignment and Safety of Large Language Models** — arXiv — 2024.04 — [paper](https://arxiv.org/abs/2404.09932)
- (Alignment, steering, and preferences) **Foundational Moral Values for AI Alignment** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.17017)
- (Alignment, steering, and preferences) **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.346/)
- (Alignment, steering, and preferences) **From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.14912)
- (Alignment, steering, and preferences) **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models** — EMNLP — 2023 — [paper](https://aclanthology.org/2023.emnlp-main.961/)
- (Alignment, steering, and preferences) **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.17857)
- (Alignment, steering, and preferences) **Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=JI6j4NUGHv)
- (Alignment, steering, and preferences) **Group Robust Preference Optimization in Reward-free RLHF** — NeurIPS — 2024 — [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)
- (Alignment, steering, and preferences) **HelpSteer2 2024-6** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.08673) [dataset](https://huggingface.co/datasets/nvidia/HelpSteer2) [code](https://github.com/NVIDIA/NeMo-Aligner)
- (Alignment, steering, and preferences) **Imitation Beyond Expectation Using Pluralistic Stochastic Dominance** — OpenReview — 2025 — [paper](https://openreview.net/forum?id=YX5DHa9OfX)
- (Alignment, steering, and preferences) **Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.** — arXiv — 2022 — [paper](https://arxiv.org/abs/2209.14375) [link](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)
- (Alignment, steering, and preferences) **Improving the Distributional Alignment of LLMs using Supervision** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.00439)
- (Alignment, steering, and preferences) **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1326/)
- (Alignment, steering, and preferences) **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.11316)
- (Alignment, steering, and preferences) **Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts** — Findings of EMNLP — 2024 — [paper](https://aclanthology.org/2024.findings-emnlp.620/)
- (Alignment, steering, and preferences) **Justifications for Democratizing AI Alignment and Their Prospects** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.19548)
- (Alignment, steering, and preferences) **Language Model Alignment in Multilingual Trolley Problems** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.02273)
- (Alignment, steering, and preferences) **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1028/)
- (Alignment, steering, and preferences) **Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain** — NAACL-INDUSTRY — 2024 — [paper](https://aclanthology.org/2024.naacl-industry.18/)
- (Alignment, steering, and preferences) **Language Models Resist Alignment: Evidence From Data Compression** — ACL Best Paper — 2025 — [paper](https://arxiv.org/abs/2406.06144)
- (Alignment, steering, and preferences) **Large Language Model Alignment: A Survey** — arXiv — 2023 — [paper](https://arxiv.org/abs/2309.15025)
- (Alignment, steering, and preferences) **Large Language Models as Optimizers** — OpenReview — 2024 — [paper](https://openreview.net/forum?id=Bb4VGOWELI)
- (Alignment, steering, and preferences) **Large pre-trained language models contain human-like biases of what is right and wrong to do. Schramowski et al. Nature Machine Intelligence 2022.** — arXiv — 2022 — [paper](https://arxiv.org/abs/2103.11790)
- (Alignment, steering, and preferences) **Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability** — ANTHOLOGY-FILES — 2025 — [paper](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.90/)
- (Alignment, steering, and preferences) **LoRe: Personalizing LLMs via Low-Rank Reward Modeling** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.14439)
- (Alignment, steering, and preferences) **MallowsPO: Fine-Tune Your LLM with Preference Dispersions** — arXiv — 2024 — [paper](https://arxiv.org/abs/2405.14953)
- (Alignment, steering, and preferences) **MAP: Multi-Human-Value Alignment Palette** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.19198)
- (Alignment, steering, and preferences) **MaxMin-RLHF: Alignment with Diverse Human Preferences** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.08925)
- (Alignment, steering, and preferences) **MixDPO: Modeling Preference Strength for Pluralistic Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.06180)
- (Alignment, steering, and preferences) **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration** — EMNLP — 2024 — [paper](https://aclanthology.org/2024.emnlp-main.240/)
- (Alignment, steering, and preferences) **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.15951)
- (Alignment, steering, and preferences) **Moral Alignment for LLM Agents** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.01639)
- (Alignment, steering, and preferences) **MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.12271)
- (Alignment, steering, and preferences) **Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.17579)
- (Alignment, steering, and preferences) **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.120/)
- (Alignment, steering, and preferences) **Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.345/)
- (Alignment, steering, and preferences) **OASIS: Open Agent Social Interaction Simulations with One Million Agents** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.11581)
- (Alignment, steering, and preferences) **Optimizing generative AI by backpropagating language model feedback, Nature** — Nature — 2025.03 — [paper](https://nature.com/articles/s41586-025-08661-4)
- (Alignment, steering, and preferences) **PAD: Personalized Alignment of LLMs at Decoding-Time** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.04070)
- (Alignment, steering, and preferences) **Pairwise Calibrated Rewards for Pluralistic Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.06298)
- (Alignment, steering, and preferences) **PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.08469)
- (Alignment, steering, and preferences) **Parametric Social Identity Injection and Diversification in Public Opinion Simulation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.16142)
- (Alignment, steering, and preferences) **PERSONA: A Reproducible Testbed for Pluralistic Alignment** — COLING — 2025 — [paper](https://aclanthology.org/2025.coling-main.752/)
- (Alignment, steering, and preferences) **Personality Alignment of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.11779)
- (Alignment, steering, and preferences) **PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.16679)
- (Alignment, steering, and preferences) **PKU-SafeRLHF 2023-7** — arXiv — 2023 — [paper](https://arxiv.org/abs/2307.04657) [dataset](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF) [code](https://github.com/PKU-Alignment/safe-rlhf)
- (Alignment, steering, and preferences) **Pluralistic Alignment for Healthcare: A Role-Driven Framework** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.1596/)
- (Alignment, steering, and preferences) **PluralLLM: Pluralistic Alignment in LLMs via Federated Learning** — ACM Digital Library — 2025 — [paper](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)
- (Alignment, steering, and preferences) **Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking** — arXiv — 2024.09 — [paper](https://arxiv.org/abs/2409.08622)
- (Alignment, steering, and preferences) **Position: A Roadmap to Impactful Pluralistic Alignment Research** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.22305)
- (Alignment, steering, and preferences) **Position: Align AI to Our Aspirations, Not Our Flaws** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.13755)
- (Alignment, steering, and preferences) **Position: The Alignment Community is Unintentionally Building a Censor's Toolkit** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=dy2HwmOvFX)
- (Alignment, steering, and preferences) **Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.06059)
- (Alignment, steering, and preferences) **ProgressGym: Alignment with a Millennium of Moral Progress** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.20087) [code](https://github.com/PKU-Alignment/ProgressGym)
- (Alignment, steering, and preferences) **ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs** — ACL — 2024 — [paper](https://aclanthology.org/2024.acl-long.381/)
- (Alignment, steering, and preferences) **Reflective Verbal Reward Design for Pluralistic Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.17834)
- (Alignment, steering, and preferences) **Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.20805)
- (Alignment, steering, and preferences) **Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?** — arXiv — 2023 — [paper](https://arxiv.org/abs/2308.15399)
- (Alignment, steering, and preferences) **Reward Model Perspectives: Whose Opinions Do Reward Models Reward?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.06391)
- (Alignment, steering, and preferences) **Robust Multi-Objective Controlled Decoding of Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.08796)
- (Alignment, steering, and preferences) **Role Steering of Language Models for Social Simulations** — arXiv — 2026 — [paper](https://arxiv.org/abs/2608.00023)
- (Alignment, steering, and preferences) **SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.16665)
- (Alignment, steering, and preferences) **Scopes of Alignment** — AAAI 2025 workshop — 2025.01 — [paper](https://arxiv.org/abs/2501.12405)
- (Alignment, steering, and preferences) **Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.16482)
- (Alignment, steering, and preferences) **Self-Pluralising Culture Alignment for Large Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.350/)
- (Alignment, steering, and preferences) **Simple Role Assignment is Extraordinarily Effective for Safety Alignment** — ACL Findings — 2026 — [paper](https://arxiv.org/abs/2602.00061)
- (Alignment, steering, and preferences) **Social Simulacra: Creating Populated Prototypes for Social Computing Systems** — ACM Digital Library — 2022 — [paper](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)
- (Alignment, steering, and preferences) **Societal Alignment Frameworks Can Improve LLM Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.00069)
- (Alignment, steering, and preferences) **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.162/)
- (Alignment, steering, and preferences) **SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment** — Findings of ACL — 2025 — [paper](https://aclanthology.org/2025.findings-acl.41/)
- (Alignment, steering, and preferences) **Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression** — arXiv — 2025 — [paper](https://arxiv.org/abs/2508.08509)
- (Alignment, steering, and preferences) **SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF** — Findings of EMNLP — 2023 — [paper](https://aclanthology.org/2023.findings-emnlp.754/)
- (Alignment, steering, and preferences) **STELA: a community-centred approach to norm elicitation for AI alignment** — Nature Scientific Reports — 2024.03 — [paper](https://nature.com/articles/s41598-024-56648-4)
- (Alignment, steering, and preferences) **Strong and weak alignment of large language models with human values** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.04655)
- (Alignment, steering, and preferences) **Strong and weak alignment of large language models with human values** — Nature Scientific Reports — 2024.08 — [paper](https://nature.com/articles/s41598-024-70031-3)
- (Alignment, steering, and preferences) **Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions** — arXiv — 2025 — [paper](https://arxiv.org/abs/2508.11414)
- (Alignment, steering, and preferences) **The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models** — EACL — 2026 — [paper](https://aclanthology.org/2026.eacl-long.305/)
- (Alignment, steering, and preferences) **The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.23965)
- (Alignment, steering, and preferences) **The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment** — arXiv — 2025 — [paper](https://arxiv.org/abs/2512.03048)
- (Alignment, steering, and preferences) **The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning** — arXiv — 2023 — [paper](https://arxiv.org/abs/2312.01552)
- (Alignment, steering, and preferences) **Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1408/)
- (Alignment, steering, and preferences) **Towards Scalable Automated Alignment of LLMs: A Survey** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.01252)
- (Alignment, steering, and preferences) **Training Socially Aligned Language Models in Simulated Human Society** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.16960) [code](https://github.com/agi-templar/Stable-Alignment)
- (Alignment, steering, and preferences) **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.1532/)
- (Alignment, steering, and preferences) **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.06404)
- (Alignment, steering, and preferences) **Unintended Impacts of LLM Alignment on Global Representation** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.15018)
- (Alignment, steering, and preferences) **Value Alignment from Unstructured Text** — EMNLP-INDUSTRY — 2024 — [paper](https://aclanthology.org/2024.emnlp-industry.81/)
- (Alignment, steering, and preferences) **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value** — NAACL — 2024 — [paper](https://aclanthology.org/2024.naacl-long.486/)
- (Alignment, steering, and preferences) **ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs** — WINLP — 2025 — [paper](https://aclanthology.org/2025.winlp-main.15/)
- (Alignment, steering, and preferences) **ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.04569)
- (Alignment, steering, and preferences) **VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.18113)
- (Alignment, steering, and preferences) **VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.04822)
- (Alignment, steering, and preferences) **VISPA: Pluralistic Alignment via Automatic Value Selection and Activation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.12758)
- (Alignment, steering, and preferences) **What are human values, and how do we align AI to them?** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.10636)
- (Alignment, steering, and preferences) **Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.00415)

<a id="catalog-value-representation-and-model-internals"></a>

#### 📐 Value representation and model internals · 44

- (Value representation and model internals) **A Method for Learning Value Systems in Generative AI** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.16903)
- (Value representation and model internals) **AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.22440)
- (Value representation and model internals) **Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.05052)
- (Value representation and model internals) **Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.12851)
- (Value representation and model internals) **Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.22396)
- (Value representation and model internals) **Do Differences in Values Influence Disagreements in Online Discussions?** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.15757)
- (Value representation and model internals) **Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.00913)
- (Value representation and model internals) **EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.12792)
- (Value representation and model internals) **Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure** — Research Square — 2025 — [paper](https://doi.org/10.21203/rs.3.rs-8270539/v1)
- (Value representation and model internals) **Enhancing Stance Classification on Social Media Using Quantified Moral Foundations** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.09848)
- (Value representation and model internals) **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.585/)
- (Value representation and model internals) **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.02444)
- (Value representation and model internals) **Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.04456)
- (Value representation and model internals) **High-Dimension Human Value Representation in Large Language Models** — NAACL — 2025 — [paper](https://aclanthology.org/2025.naacl-long.274/)
- (Value representation and model internals) **High-Dimension Human Value Representation in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.07900) [code](https://github.com/HLTCHKUST/UniVaR)
- (Value representation and model internals) **Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.14172)
- (Value representation and model internals) **Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.27373)
- (Value representation and model internals) **Investigating Human Values in Online Communities** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.14177)
- (Value representation and model internals) **Learning the Value Systems of Societies from Preferences** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.20728)
- (Value representation and model internals) **Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.08835)
- (Value representation and model internals) **Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.11018)
- (Value representation and model internals) **Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.22660)
- (Value representation and model internals) **MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions** — arXiv — 2024 — [paper](https://arxiv.org/abs/2403.07678)
- (Value representation and model internals) **Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning** — arXiv — 2024 — [paper](https://arxiv.org/abs/2401.17228)
- (Value representation and model internals) **More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.22641)
- (Value representation and model internals) **MoVa: Towards Generalizable Classification of Human Morals and Values** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.24216)
- (Value representation and model internals) **Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.23659)
- (Value representation and model internals) **SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments** — SemEval — 2023 — [paper](https://aclanthology.org/2023.semeval-1.313/)
- (Value representation and model internals) **SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.12633)
- (Value representation and model internals) **The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers** — arXiv — 2025 — [paper](https://arxiv.org/abs/2501.11770)
- (Value representation and model internals) **Tracing Moral Foundations in Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.05437)
- (Value representation and model internals) **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs** — Findings of EMNLP — 2025 — [paper](https://aclanthology.org/2025.findings-emnlp.501/)
- (Value representation and model internals) **Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2502.08640)
- (Value representation and model internals) **Value Alignment of Social Media Ranking Algorithms** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.14434)
- (Value representation and model internals) **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.10766)
- (Value representation and model internals) **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties** — arXiv — 2023 — [paper](https://arxiv.org/abs/2309.00779) [code](https://github.com/tsor13/kaleido)
- (Value representation and model internals) **Value Lens: Using Large Language Models to Understand Human Values** — arXiv — 2025 — [paper](https://arxiv.org/abs/2512.15722)
- (Value representation and model internals) **Value Profiles for Encoding Human Variation** — arXiv — 2025 — [paper](https://arxiv.org/abs/2503.15484)
- (Value representation and model internals) **VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.03160)
- (Value representation and model internals) **ValueNet: A New Dataset for Human Value Driven Dialogue System** — arXiv — 2021 — [paper](https://arxiv.org/abs/2112.06346)
- (Value representation and model internals) **Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.15236)
- (Value representation and model internals) **What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric** — ACL — 2023 — [paper](https://aclanthology.org/2023.acl-long.789/)
- (Value representation and model internals) **Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.20270)
- (Value representation and model internals) **Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.08453)

<a id="catalog-measurement-and-profiling"></a>

#### 📏 Measurement and profiling · 87

- (GLOBE) **Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models** — arXiv — 2024.06 — [paper](https://arxiv.org/abs/2406.17675)
- (Other / custom) **Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches** — arXiv — 2024.04 — [paper](https://arxiv.org/abs/2404.12744)
- (Other / custom) **CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility** — arXiv — 2023.07 — [paper](https://arxiv.org/abs/2307.09705) [dataset](https://modelscope.cn/datasets/damo/CValues-Comparison/summary) [code](https://github.com/X-PLUG/CValues)
- (Other / custom) **Measurement of LLM’s Philosophies of Human Nature** — arXiv — 2025.04 — [paper](https://arxiv.org/abs/2504.02304) [code](https://github.com/kodenii/M-PHNS)
- (Other / custom) **Measuring Spiritual Values and Bias of Large Language Models** — arXiv — 2024.10 — [paper](https://arxiv.org/abs/2410.11647)
- (Other / custom) **Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas** — arXiv — 2025.05 — [paper](https://arxiv.org/abs/2505.14633)
- (Schwartz) **AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories** — Perspectives on Psychological Science — 2023.01 — [paper](https://journals.sagepub.com/doi/full/10.1177/17456916231214460) [code](https://github.com/feradauto/MoralCoT)
- (Schwartz) **Improving Language Model Personas via Rationalization with Psychological Scaffolds** — arXiv — 2025.04 — [paper](https://arxiv.org/abs/2504.17993)
- (Schwartz) **Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models** — AAAI — 2025 — [paper](https://ojs.aaai.org/index.php/AAAI/article/view/34839)
- (Schwartz) **The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas** — arXiv — 2025.05 — [paper](https://arxiv.org/abs/2505.18154)
- (Schwartz) **ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs** — arXiv — 2024.09 — [paper](https://arxiv.org/abs/2409.09586)
- (Schwartz) **What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory** — arXiv — 2023.04 — [paper](https://arxiv.org/abs/2304.03612)
- (Schwartz) **When Prompting Fails to Sway: Inertia in Moral and Value Judgments of Large Language Models** — NeurIPS — 2022 — [paper](https://arxiv.org/abs/2408.09049)
- (Schwartz) **Who is GPT-3? An Exploration of Personality, Values and Demographics** — EMNLP NLP+CSS workshop — 2022 — [paper](https://arxiv.org/abs/2209.14338)
- (VSM) **Cultural Value Differences of LLMs: Prompt, Language, and Model Size** — arXiv — 2024.07 — [paper](https://arxiv.org/abs/2407.16891)
- (WVS) **Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.08846)
- (WVS) **On the Alignment of Large Language Models with Global Human Opinion** — AAAI 2026 Best Paper (AI Alignment Track) — 2026.01 — [paper](https://arxiv.org/abs/2509.01418) [code](https://github.com/ku-nlp/global-opinion-alignment)
- (WVS) **Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models** — arXiv — 2025.03 — [paper](https://arxiv.org/abs/2503.16148)
- (Measurement and profiling) **A Scalable Approach to Evaluating Moral Sensitivity in LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.02972)
- (Measurement and profiling) **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.13531)
- (Measurement and profiling) **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference** — OpenReview — 2026 — [paper](https://openreview.net/forum?id=qNlTH4kYJZ)
- (Measurement and profiling) **Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.00751)
- (Measurement and profiling) **Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.20205)
- (Measurement and profiling) **Are Language Models Sensitive to Morally Irrelevant Distractors?** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.09416)
- (Measurement and profiling) **Are Large Language Models Consistent over Value-laden Questions?** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.02996)
- (Measurement and profiling) **Are LLMs Bad at Moral Reasoning?** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.11635)
- (Measurement and profiling) **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective** — arXiv — 2024 — [paper](https://arxiv.org/abs/2501.00581)
- (Measurement and profiling) **Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.21939)
- (Measurement and profiling) **Can Language Models Reason about Individualistic Human Values and Preferences?** — arXiv — 2024 — [paper](https://arxiv.org/abs/2410.03868)
- (Measurement and profiling) **Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.31213)
- (Measurement and profiling) **Can Revealed Preferences Clarify LLM Alignment and Steering?** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.08556)
- (Measurement and profiling) **CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.10725)
- (Measurement and profiling) **Context-Value-Action Architecture for Value-Driven Large Language Model Agents** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.05939)
- (Measurement and profiling) **Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.02109)
- (Measurement and profiling) **Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths** — arXiv — 2025 — [paper](https://arxiv.org/abs/2506.02481)
- (Measurement and profiling) **Do LLMs have Consistent Values?** — arXiv — 2024 — [paper](https://arxiv.org/abs/2407.12878) [link](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)
- (Measurement and profiling) **Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.02197)
- (Measurement and profiling) **Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.24319)
- (Measurement and profiling) **Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.11232)
- (Measurement and profiling) **Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?** — arXiv — 2024 — [paper](https://arxiv.org/abs/2402.18120)
- (Measurement and profiling) **Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.04994)
- (Measurement and profiling) **From Stability to Inconsistency: A Study of Moral Preferences in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2504.06324)
- (Measurement and profiling) **Generative Value Conflicts Reveal LLM Priorities** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.25369)
- (Measurement and profiling) **Heterogeneous Value Alignment Evaluation for Large Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.17147) [code](https://github.com/zowiezhang/HVAE) [code](https://github.com/zowiezhang/A2EHV)
- (Measurement and profiling) **How do LLMs reflect human moral foundations? a study using the moral foundations framework** — Taylor & Francis journal — 2026 — [paper](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)
- (Measurement and profiling) **Human Psychometric Questionnaires Mischaracterize LLM Behavior** — arXiv — 2025 — [paper](https://arxiv.org/abs/2509.10078)
- (Measurement and profiling) **Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.03384)
- (Measurement and profiling) **Incoherent Values? Probing LLM Preferences Through Parametric Variation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.21102)
- (Measurement and profiling) **Investigating Value-Reasoning Reliability in Small Large Language Models** — EMNLP — 2025 — [paper](https://aclanthology.org/2025.emnlp-main.395/)
- (Measurement and profiling) **LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.13944)
- (Measurement and profiling) **LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2408.01460)
- (Measurement and profiling) **Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.22170)
- (Measurement and profiling) **Measurement and Fairness** — ACM proceedings or journal — 2021 — [paper](https://doi.org/10.1145/3442188.3445901)
- (Measurement and profiling) **Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2409.12106) [code](https://github.com/Value4AI/gpv)
- (Measurement and profiling) **Measuring human and AI values based on generative psychometrics with large language models** — AAAI — 2025 — [paper](https://doi.org/10.1609/aaai.v39i25.34839)
- (Measurement and profiling) **Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2604.11216)
- (Measurement and profiling) **Mechanistic Origin of Moral Indifference in Language Models** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.15615)
- (Measurement and profiling) **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2501.15463)
- (Measurement and profiling) **Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.12515)
- (Measurement and profiling) **Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.08634)
- (Measurement and profiling) **Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.03217)
- (Measurement and profiling) **Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2511.08565)
- (Measurement and profiling) **Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method** — Elsevier journal or book — 2025 — [paper](https://sciencedirect.com/science/article/pii/S0925231225008422)
- (Measurement and profiling) **Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.12731)
- (Measurement and profiling) **On the Credibility of Evaluating LLMs using Survey Questions** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.04033)
- (Measurement and profiling) **Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.28911)
- (Measurement and profiling) **Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses** — arXiv — 2026 — [paper](https://arxiv.org/abs/2507.07188)
- (Measurement and profiling) **Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation** — arXiv — 2026 — [paper](https://arxiv.org/abs/2607.05554)
- (Measurement and profiling) **Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.09893)
- (Measurement and profiling) **Quantifying Data Contamination in Psychometric Evaluations of LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.07175)
- (Measurement and profiling) **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.14230)
- (Measurement and profiling) **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing** — OpenReview — 2025 — [paper](https://openreview.net/forum?id=0REM9ydeLZ)
- (Measurement and profiling) **Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?** — arXiv — 2025 — [paper](https://arxiv.org/abs/2507.13490)
- (Measurement and profiling) **Superficial Beliefs in LLM Decision-Making** — arXiv — 2026 — [paper](https://arxiv.org/abs/2606.11016)
- (Measurement and profiling) **The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models** — arXiv — 2025 — [paper](https://arxiv.org/abs/2512.03026)
- (Measurement and profiling) **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.17712)
- (Measurement and profiling) **Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability** — arXiv — 2026 — [paper](https://arxiv.org/abs/2603.16017)
- (Measurement and profiling) **Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs** — arXiv — 2026 — [paper](https://arxiv.org/abs/2601.10257)
- (Measurement and profiling) **Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values** — arXiv — 2025 — [paper](https://arxiv.org/abs/2501.07071)
- (Measurement and profiling) **Value Drifts: Tracing Value Alignment During LLM Post-Training** — arXiv — 2025 — [paper](https://arxiv.org/abs/2510.26707)
- (Measurement and profiling) **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items** — ACL — 2025 — [paper](https://aclanthology.org/2025.acl-long.838/)
- (Measurement and profiling) **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items** — arXiv — 2025 — [paper](https://arxiv.org/abs/2505.01015)
- (Measurement and profiling) **Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts** — arXiv — 2024 — [paper](https://arxiv.org/abs/2411.11479)
- (Measurement and profiling) **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.04214) [code](https://github.com/Value4AI/ValueBench)
- (Measurement and profiling) **ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.00378)
- (Measurement and profiling) **ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems** — arXiv — 2026 — [paper](https://arxiv.org/abs/2602.08567)
- (Measurement and profiling) **Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts** — arXiv — 2026 — [paper](https://arxiv.org/abs/2605.25256)

<a id="catalog-other-and-adjacent-value-research"></a>

#### 📎 Other and adjacent value research · 45

- (Other and adjacent value research) **10.1186/s40537-024-00986-7** — Springer journal or proceedings — 2024 — [paper](https://link.springer.com/article/10.1186/s40537-024-00986-7)
- (Other and adjacent value research) **A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle** — ACM proceedings or journal — 2021 — [paper](https://doi.org/10.1145/3465416.3483305)
- (Other and adjacent value research) **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive** — ACL Best Paper — 2025 — [paper](https://arxiv.org/abs/2402.11005)
- (Other and adjacent value research) **Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective** — arXiv — 2024.07 — [paper](https://arxiv.org/abs/2408.04638)
- (Other and adjacent value research) **Automated Mining of Structured Knowledge from Text in the Era of Large Language Models** — KDD 2024 — 2024.08 — [paper](https://dl.acm.org/doi/pdf/10.1145/3637528.3671469)
- (Other and adjacent value research) **Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions** — AAMAS Oral — 2026 — [paper](https://arxiv.org/abs/2603.13890) [code](https://github.com/jingzhe-lin/ASVO)
- (Other and adjacent value research) **Chatbotarenaconversations 2023-6** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.05685) [dataset](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) [dataset](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments) [model](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) [code](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)
- (Other and adjacent value research) **Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science** — TACL — 2018 — [paper](https://aclanthology.org/Q18-1041/)
- (Other and adjacent value research) **EMNLP Main 18** — EMNLP — 2023 — [paper](https://aclanthology.org/2023.emnlp-main.18/)
- (Other and adjacent value research) **Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs** — arXiv — 2024 — [paper](https://arxiv.org/abs/2406.13993)
- (Other and adjacent value research) **Fairness and Abstraction in Sociotechnical Systems** — ACM proceedings or journal — 2019 — [paper](https://doi.org/10.1145/3287560.3287598)
- (Other and adjacent value research) **Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs** — ACL Best Paper — 2025 — [paper](https://arxiv.org/abs/2502.01926)
- (Other and adjacent value research) **Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization** — Sociological Methods & Research — 2025.05 — [paper](https://journals.sagepub.com/doi/10.1177/00491241251327130)
- (Other and adjacent value research) **Generative language models exhibit social identity biases, Nature Computational Science** — Nature Computational Science — 2025.01 — [paper](https://nature.com/articles/s43588-024-00741-1)
- (Other and adjacent value research) **GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods** — arXiv — 2023 — [paper](https://arxiv.org/abs/2301.01893) [code](https://github.com/WadeYin9712/GIVL)
- (Other and adjacent value research) **HG & CI & MC** — arXiv — 2023 — [paper](https://arxiv.org/abs/2311.09528) [dataset](https://huggingface.co/datasets/nvidia/HelpSteer)
- (Other and adjacent value research) **Holistic Evaluation of Language Models** — OpenReview — 2023 — [paper](https://openreview.net/forum?id=iO4LZibEqW)
- (Other and adjacent value research) **Large Language Model Safety: A Holistic Survey** — arXiv — 2024.12 — [paper](https://arxiv.org/abs/2412.17686)
- (Other and adjacent value research) **Large language models (LLM) in computational social science: prospects, current state, and challenges** — Social Network Analysis and Mining — 2025.03 — [paper](https://link.springer.com/article/10.1007/s13278-025-01428-9)
- (Other and adjacent value research) **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives** — Nature humanities and social sciences communications — 2023.12 — [paper](https://arxiv.org/abs/2312.11970)
- (Other and adjacent value research) **Linhao Yu et al. ACL Findings 2024.** — Findings of ACL — 2024 — [paper](https://aclanthology.org/2024.findings-acl.703/)
- (Other and adjacent value research) **Machine Bias. How Do Generative Language Models Answer Opinion Polls?** — Sociological Methods & Research — 2025.04 — [paper](https://doi.org/10.1177/00491241251330582)
- (Other and adjacent value research) **Nicholas Botzer et al. arXiv 2021.** — arXiv — 2021 — [paper](https://arxiv.org/abs/2101.07664)
- (Other and adjacent value research) **On the Credibility of Evaluating LLMs using Survey Questions** — MME — 2026 — [paper](https://aclanthology.org/2026.mme-main.2/)
- (Other and adjacent value research) **On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?** — ACM proceedings or journal — 2021 — [paper](https://doi.org/10.1145/3442188.3445922)
- (Other and adjacent value research) **On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective** — arXiv — 2025.02 — [paper](https://arxiv.org/abs/2502.14296)
- (Other and adjacent value research) **Persuading voters using human–artificial intelligence dialogues, Nature** — Nature — 2025.12 — [paper](https://nature.com/articles/s41586-025-09771-9)
- (Other and adjacent value research) **Position: AI Evaluation Should Learn from How We Test Humans** — arXiv — 2023 — [paper](https://arxiv.org/abs/2306.10512)
- (Other and adjacent value research) **PRM800K 2023-5** — arXiv — 2023 — [paper](https://arxiv.org/abs/2305.20050) [code](https://github.com/openai/prm800k)
- (Other and adjacent value research) **Questioning the Survey Responses of Large Language Models** — NeurIPS Oral — 2024 — [paper](https://arxiv.org/abs/2306.07951)
- (Other and adjacent value research) **RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models** — Findings of EMNLP — 2020 — [paper](https://aclanthology.org/2020.findings-emnlp.301/)
- (Other and adjacent value research) **SHP 2021-10 — All — EN — HG** — arXiv — 2021 — [paper](https://arxiv.org/abs/2110.08420) [dataset](https://huggingface.co/datasets/stanfordnlp/SHP) [code](https://github.com/kawine/dataset_difficulty)
- (Other and adjacent value research) **Simulating Human-like Daily Activities with Desire-driven Autonomy** — ICLR — 2025 — [paper](https://arxiv.org/abs/2412.06435)
- (Other and adjacent value research) **Simulating Human-like Daily Activities with Desire-driven Autonomy** — ICLR — 2025 — [paper](https://openreview.net/forum?id=3ms8EQY7f8) [code](https://github.com/zfw1226/D2A)
- (Other and adjacent value research) **Stick to your role! Stability of personal values expressed in large language models** — PLOS ONE — 2024 — [paper](https://doi.org/10.1371/journal.pone.0309114) [model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309114)
- (Other and adjacent value research) **SummarizefromFeedback 2020-9** — arXiv — 2020 — [paper](https://arxiv.org/abs/2009.01325) [dataset](https://huggingface.co/datasets/openai/summarize_from_feedback)
- (Other and adjacent value research) **The AI Gap: How Socioeconomic Status Affects Language Technology Interactions** — ACL Best Social Impact Paper — 2025 — [paper](https://arxiv.org/abs/2505.12158)
- (Other and adjacent value research) **The Rise and Potential of Large Language Model Based Agents: A Survey** — arXiv — 2023 — [paper](https://arxiv.org/abs/2309.07864) [code](https://github.com/WooooDyy/LLM-Agent-Paper-List)
- (Other and adjacent value research) **UltraFeedback** — arXiv — 2023 — [paper](https://arxiv.org/abs/2310.01377) [dataset](https://huggingface.co/datasets/openbmb/UltraFeedback) [code](https://github.com/OpenBMB/UltraFeedback)
- (Other and adjacent value research) **UltraInteract 2024-4** — arXiv — 2024 — [paper](https://arxiv.org/abs/2404.02078) [dataset](https://huggingface.co/datasets/openbmb/UltraInteract_pair)
- (Other and adjacent value research) **Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries** — Elsevier journal or book — 1992 — [paper](https://sciencedirect.com/science/article/pii/S0065260108602816) [link](https://psycnet.apa.org/record/2003-00370-001)
- (Other and adjacent value research) **Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents** — Springer journal or proceedings — 2026 — [paper](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)
- (Other and adjacent value research) **WebGPT: Browser-assisted question-answering with human feedback** — arXiv — 2021 — [paper](https://arxiv.org/abs/2112.09332) [dataset](https://huggingface.co/datasets/openai/webgpt_comparisons)
- (Other and adjacent value research) **Who is GPT-3? An exploration of personality, values and demographics** — NLP+CSS — 2022 — [paper](https://aclanthology.org/2022.nlpcss-1.24/)
- (Other and adjacent value research) **Zhijing Jin et al. NeurIPS 2022.** — arXiv — 2022 — [paper](https://arxiv.org/abs/2210.01478)

### 🧩 Standalone data, models, code, and additional resources

<a id="catalog-dataset-and-benchmark-artifacts"></a>

#### 💾 Dataset and benchmark artifacts · 5

- **A Systematic Survey of Cultural Datasets for Equitable LLM Alignment** — [dataset](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)
- **Medical-rlhf 2023-5** — [dataset](https://huggingface.co/datasets/shibing624/medical)
- **OASST1pairwiserlhfreward 2023-5** — [dataset](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)
- **OpenHermesPreferences 2024-3** — [dataset](https://huggingface.co/datasets/argilla/OpenHermesPreferences)
- **Zhihurlhf3k 2023-4** — [dataset](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)

<a id="catalog-model-checkpoints-and-scorers"></a>

#### 🧠 Model checkpoints and scorers · 2

- **Exploring Universal Human Values with Large Language Models: The AWARE-Value Model** — [model](https://researchsquare.com/article/rs-8188052/v1)
- **Robustness of large language models in moral judgements** — [model](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)

<a id="catalog-code-repositories"></a>

#### 🧰 Code repositories · 17

- **<a href="** — [code](https://github.com/sindresorhus/awesome)
- **AI Job Displacement Tracker** — [code](https://github.com/noahaust2/ai-displacement-tracker)
- **Alpacacomparisondata 2023-3** — [code](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
- **Awesome-LLM-in-Social-Science** — [code](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)
- **Awesome-LLM-Psychometrics** — [code](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- **awesome-llm-social-simulation** — [code](https://github.com/Wanying-He/awesome-llm-social-simulation)
- **Awesome-Personalized-Alignment** — [code](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)
- **Awesome-Pluralistic-Alignment** — [code](https://github.com/anudeex/Awesome-Pluralistic-Alignment)
- **Concerns on the use of generative AI in social science research** — [code](https://github.com/uh-dcm/genai-concerns)
- **culture-awareness-llms** — [code](https://github.com/siddheshih/culture-awareness-llms)
- **Datasets for depression detection using data posted on online platforms** — [code](https://github.com/bucuram/depression-datasets-nlp)
- **github.com** — [code](https://github.com/CLUEbenchmark/CLUEDatasetSearch)
- **huozirlhfdata 2024-2** — [code](https://github.com/HIT-SCIR/huozi)
- **huozirlhfdata 2024-2** — [code](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)
- **Medical-rlhf 2023-5** — [code](https://github.com/shibing624/MedicalGPT)
- **Mental Health Datasets** — [code](https://github.com/kharrigian/mental-health-datasets)
- **SuperCLUE-Safety 2023-9** — [code](https://github.com/CLUEbenchmark/SuperCLUE-safety)

<a id="catalog-project-pages"></a>

#### 🌐 Project pages · 2

- **Concerns on the use of generative AI in social science research** — [project](https://uh-dcm.github.io/genai-concerns/)
- **SuperCLUE-Safety 2023-9** — [project](https://cluebenchmarks.com/superclue_safety.html)

<a id="catalog-survey-resources"></a>

#### 📋 Survey resources · 4

- **EVS — European Values Survey** — [survey](https://europeanvaluesstudy.eu/)
- **GSS — General Social Survey** — [survey](https://gss.norc.org/)
- **World Values Survey Wave 7 (2017-2022).** — [survey](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)
- **WVS — World Values Survey** — [survey](https://worldvaluessurvey.org/)

<a id="catalog-additional-resources"></a>

#### 🔗 Additional resources · 77

- **!\[Awesome** — [link](https://awesome.re)
- **(ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis** — [link](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)
- **(ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis** — [link](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)
- **(ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL)** — [link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)
- **(Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL)** — [link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)
- **(Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate** — [link](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000429)
- **(Others & custom) DO MINDFULNESS ACTIVITIES IMPROVE HANDGRIP STRENGTH AMONG OLDER ADULTS: A PROPENSITY SCORE MATCHING APPROACH, 2024.12, Innovation in Aging** — [link](https://academic.oup.com/innovateage/article/8/Supplement_1/1010/7939280)
- **(Others & custom) Improving GPT Generated Synthetic Samples with Sampling-Permutation Algorithm** — [link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4548937)
- **(Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science** — [link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)
- **(PCT) The Political Biases of ChatGPT, 2023.01, Social Sciences** — [link](https://mdpi.com/2076-0760/12/3/148)
- **<a href="** — [link](https://git.io/typing-svg)
- **<img src="** — [link](https://capsule-render.vercel.app/api)
- **<img src="** — [link](https://readme-typing-svg.demolab.com)
- **A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights** — [link](https://unesdoc.unesco.org/ark:/48223/pf0000048063)
- **A review of automatic item generation techniques leveraging large language models** — [link](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)
- **A theory of justice.** — [link](https://jstor.org/stable/j.ctvjf9z6v)
- **A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism** — [link](http://jstor.org/stable/24707060)
- **Aggregating Sets of Judgments: An Impossibility Result** — [link](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)
- **An Overview of the Schwartz Theory of Basic Values** — [link](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)
- **An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012.** — [link](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)
- **Basic human values: Theory, measurement, and applications** — [link](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)
- **Can Generative AI improve social science?, 2024.05, PNAS** — [link](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)
- **Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023** — [link](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)
- **Citizenship and Social Class** — [link](https://books.google.co.kr/books?id=99v4JQAACAAJ)
- **Collective Choice and Social Welfare** — [link](https://jstor.org/stable/j.ctv2sp3dqx)
- **Conflicts of Values (in Moral Luck)** — [link](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)
- **Creating Capabilities: The Human Development Approach and Its Implementation** — [link](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)
- **Cultural Value Orientations** — [link](https://researchgate.net/publication/265997557)
- **Culture's consequences: International differences in work-related values** — [link](https://philpapers.org/rec/HOFCCI-2)
- **Culture's consequences: International differences in work-related values. Hofstede et al. 1984.** — [link](https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC)
- **Cultures and organizations: software of the mind** — [link](https://books.google.co.kr/books?id=o4OqTgV3V00C)
- **ESS — European Social Survey** — [link](https://europeansocialsurvey.org/data-portal)
- **Functional theory of human values** — [link](https://researchgate.net/publication/259486885)
- **Handbook of Computational Social Choice** — [link](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)
- **If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task** — [link](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)
- **Kush R. Varshney. XRDS 2019.** — [link](https://krvarshney.github.io/)
- **Kush R. Varshney. XRDS 2019.** — [link](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)
- **Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice** — [link](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)
- **Liberals and conservatives rely on different sets of moral foundations** — [link](https://pubmed.ncbi.nlm.nih.gov/19379034/)
- **Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002.** — [link](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)
- **lit.eecs.umich.edu** — [link](https://lit.eecs.umich.edu/downloads.html)
- **Manipulation of Voting Schemes: A General Result** — [link](https://jstor.org/stable/1914083)
- **Mapping and interpreting cultural differences around the world** — [link](https://researchgate.net/publication/265596552)
- **Measuring Perceived Slant in Large Language Models Through User Evaluations** — [link](https://modelslant.com/paper.pdf)
- **Measuring the Refined Theory of Individual Values in 49 Cultural Groups** — [link](https://researchgate.net/publication/349058866)
- **Mental representations of social values.** — [link](https://psycnet.apa.org/record/2012-14612-001)
- **Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies** — [link](https://jstor.org/stable/j.ctv10vm2ns)
- **Modernization, Cultural Change, and Democracy** — [link](https://researchgate.net/publication/230557603)
- **Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism** — [link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2184440)
- **NeurIPS 2025 Tutorial: Human-AI Alignment** — [link](https://hai-alignment-course.github.io/tutorial/)
- **On the Rationale of Group Decision-making** — [link](https://jstor.org/stable/1825026)
- **Perils and opportunities in using large language models in psychological research** — [link](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)
- **Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science** — [link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)
- **Pew Researcj Center's Global Attitudes Surveys (GAS)** — [link](https://pewresearch.org/)
- **Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449** — [link](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)
- **Refining the theory of basic individual values** — [link](https://pubmed.ncbi.nlm.nih.gov/22823292/)
- **Rokeach value survey. Rokeach et al. The nature of human values. 1967.** — [link](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)
- **Social Choice and Individual Values** — [link](https://jstor.org/stable/j.ctt1nqb90)
- **Social Choice Theory (in Stanford Encyclopedia of Philosophy)** — [link](https://plato.stanford.edu/entries/social-choice/)
- **Stanford 2025: Human-Centered LLMs (CS329X)** — [link](https://web.stanford.edu/class/cs329x/)
- **Stanford 2025: Machine Learning from Human Preferences (CS329H)** — [link](https://web.stanford.edu/class/cs329h/)
- **Steerable Alignment with Conditional Multiobjective Preference Optimization** — [link](https://dspace.mit.edu/handle/1721.1/156747)
- **Survey of Cultural Awareness in Language Models: Text and Beyond Open Access** — [link](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)
- **The Impossibility of a Paretian Liberal** — [link](https://jstor.org/stable/1829633)
- **The Morality of Freedom** — [link](https://academic.oup.com/book/9926)
- **The Morality of Pluralism** — [link](https://jstor.org/stable/j.ctt7smh7)
- **The Morals of Modernity** — [link](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)
- **The nature of human values.** — [link](https://psycnet.apa.org/record/2011-15663-000)
- **The Right and the Good** — [link](https://academic.oup.com/book/27608)
- **The Righteous Mind** — [link](https://righteousmind.com/)
- **The Theory of Communicative Action** — [link](https://philpapers.org/rec/HABTTO)
- **The theory of dyadic morality: Reinventing moral judgment by redefining harm.** — [link](https://psycnet.apa.org/record/2018-02142-002)
- **Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022.** — [link](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)
- **Towards Pluralistic Alignment of LLMs: A Comprehensive Survey** — [link](https://preprints.org/manuscript/202603.1876)
- **Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop** — [link](https://openaccess.city.ac.uk/id/eprint/31381/)
- **Two Concepts of Liberty** — [link](https://academic.oup.com/book/7968/chapter-abstract/153281672)
- **Value Pluralism (in Stanford Encyclopedia of Philosophy)** — [link](https://plato.stanford.edu/entries/value-pluralism/)

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
