<div align="center">

<img src="assets/atlas-header.svg" width="100%" alt="AI Values Atlas" />

# AI Values Atlas

**A field guide to how values are represented, measured, expressed, chosen, and steered in AI systems.**

[Explore the atlas](https://ikanam-ai.github.io/ai-values-atlas/) · [Wiki](https://ikanam-ai.github.io/ai-values-atlas/learn/) · [Field map](#-field-map) · [Axiologies](#-axiologies-and-value-spaces) · [Literature](#-literature-by-research-domain) · [Datasets & benchmarks](#-datasets-benchmarks-and-instruments) · [Contribute](CONTRIBUTING.md)

**703 works · 10 research domains · 1,019 source links · 94 standalone resources**

</div>

The Atlas separates value theories, measurement interfaces, benchmarks, scorers, model behavior, and alignment targets instead of treating them as one interchangeable construct.

The [research Wiki](https://ikanam-ai.github.io/ai-values-atlas/learn/) gives every mapped value space a stable evidence page: construct and unit of analysis, numerical structure, measurement protocol, AI literature, cautions, primary sources, and a structural diagram.

## 🧭 Field map

| Domain | Research question | Works |
|---|---|---:|
| 🧭 **Value theory and axiologies** | Which values exist, and how are they structured? | 4 |
| 📏 **Measurement and profiling** | How are AI values elicited and summarized? | 106 |
| 🔬 **Reliability, validity, and auditing** | When is a reported value result stable and valid? | 19 |
| ⚖️ **Moral and value understanding** | Can systems identify, explain, or reason about values and norms? | 72 |
| 🎯 **Choice, action, and behavior** | Which values govern choices and behavior under conflict? | 17 |
| 🌍 **Culture, opinions, and social representation** | Whose cultures, opinions, and social perspectives are represented? | 265 |
| 🗣️ **Pluralism and preference aggregation** | How should heterogeneous values and preferences be represented or aggregated? | 57 |
| 🧰 **Alignment and steering** | How are normative targets used to train or steer systems? | 105 |
| 📐 **Value representations and model internals** | How is value information represented, learned, or causally encoded? | 43 |
| 🗺️ **Field reviews, reporting, and governance** | How is the field organized, documented, and governed? | 50 |

## 🧠 Axiologies and value spaces

An axiology describes which values exist and how they relate. The registry currently
contains **17 representations across 7 classes**. Counts and representation classes
stay visible below; the long lists of named dimensions are collapsed for readability.
An axiology is not the questionnaire, prompt, scorer, or benchmark used to measure it.

| Axiology or value space | Class | Numerical structure | Typical use in AI research |
|---|---|---:|---|
| [Schwartz Theory of Basic Human Values](https://doi.org/10.1016/S0065-2601(08)60281-6) | 🧭 Basic human values | **10 values** | questionnaires, scenarios, text scoring, value conflict |
| [Schwartz higher-order dimensions](https://doi.org/10.1016/S0065-2601(08)60281-6) | 🧭 Basic human values | **4 groups** | aggregated profiles and trade-off analysis |
| [Refined Schwartz Theory](https://doi.org/10.1037/a0029393) | 🧭 Basic human values | **19 values** | higher-granularity human and AI profiling |
| [Moral Foundations Theory](https://doi.org/10.1037/a0015141) | ⚖️ Moral framework | **5 in MFQ-1**; **6 in MFQ-2**; Liberty is a separate extension | moral-language classification and profiling |
| [World Values Survey](https://www.worldvaluessurvey.org/) | 🌍 Cultural values | open item space; **7 waves**, **300+ indicators** in Wave 7 | human–AI comparison and political attitudes |
| [Inglehart–Welzel Cultural Map](https://www.worldvaluessurvey.org/WVSContents.jsp) | 🌍 Cultural values | **2 dimensions** | country- and culture-level comparison |
| [Hofstede cultural dimensions](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/) | 🌍 Cultural values | **6 dimensions** | cultural alignment and language/persona audits |
| [GLOBE cultural dimensions](https://globeproject.com/study_2004_2007) | 🌍 Cultural values | **9 dimensions** | cross-cultural model evaluation |
| [Rokeach Value System](https://psycnet.apa.org/record/2011-15663-000) | 🧭 Basic human values | **36 values**: 18 terminal + 18 instrumental | ranked value priorities |
| [Social Value Orientation](https://doi.org/10.1002/ejsp.1773) | 🤝 Social preferences | **1 continuum**; **6 primary items** | allocation choices and behavioral games |
| [Functional Theory of Human Values](https://doi.org/10.1016/j.paid.2013.12.012) | 🧭 Basic human values | **18 values**, **6 subfunctions** | alternative named human-value profiling |
| [GPLA](https://aclanthology.org/2025.acl-long.585/) | 🧠 AI-native values | **123 atomic values → 5 factors** | AI-native value-system construction |
| [UniVaR](https://aclanthology.org/2025.naacl-long.274/) | 🧠 AI-native values | latent space; **8 source LLMs**, **15 evaluated models**, **25 languages/cultures** | model–language embeddings and comparison |
| [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) | 📜 Rights, duties & principles | **3 entity types** | pluralistic reasoning and conflict-aware alignment |
| [Helpful, Honest, and Harmless](https://arxiv.org/abs/2112.00861) | 📜 Rights, duties & principles | **3 principles** | assistant behavior and preference modeling |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | 📜 Rights, duties & principles | configurable; **no fixed count** | critique, revision, and alignment targets |
| [Generative Psychometrics / GPV](https://doi.org/10.1609/aaai.v39i25.34839) | ✨ Open value space | supplied dynamically; **no fixed count** | free-response extraction and value scoring |

<details>
<summary><strong>🔎 Show named dimensions and structural details</strong></summary>

- **Schwartz-10:** Self-Direction, Stimulation, Hedonism, Achievement, Power, Security, Conformity, Tradition, Benevolence, Universalism.
- **Schwartz-4:** Openness to Change, Conservation, Self-Enhancement, Self-Transcendence.
- **Refined Schwartz-19:** Self-Direction–Thought, Self-Direction–Action, Stimulation, Hedonism, Achievement, Power–Dominance, Power–Resources, Face, Security–Personal, Security–Societal, Tradition, Conformity–Rules, Conformity–Interpersonal, Humility, Benevolence–Dependability, Benevolence–Caring, Universalism–Concern, Universalism–Nature, Universalism–Tolerance.
- **Moral Foundations Theory:** classic MFQ-1 uses Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation. Liberty/Oppression is a proposed extension. The 36-item MFQ-2 instead uses Care, Equality, Proportionality, Loyalty, Authority, and Purity.
- **World Values Survey:** a changing multilingual item bank rather than a fixed vector; seven completed waves since 1981, coverage of almost 120 countries/societies, and 300+ indicators in Wave 7.
- **Inglehart–Welzel:** Traditional ↔ Secular-Rational; Survival ↔ Self-Expression.
- **Hofstede-6:** Power Distance, Individualism, Masculinity, Uncertainty Avoidance, Long-Term Orientation, Indulgence.
- **GLOBE-9:** Performance Orientation, Assertiveness, Future Orientation, Humane Orientation, Institutional Collectivism, In-Group Collectivism, Gender Egalitarianism, Power Distance, Uncertainty Avoidance.
- **Rokeach terminal values (18):** A Comfortable Life, An Exciting Life, A Sense of Accomplishment, A World at Peace, A World of Beauty, Equality, Family Security, Freedom, Happiness, Inner Harmony, Mature Love, National Security, Pleasure, Salvation, Self-Respect, Social Recognition, True Friendship, Wisdom.
- **Rokeach instrumental values (18):** Ambitious, Broad-Minded, Capable, Cheerful, Clean, Courageous, Forgiving, Helpful, Honest, Imaginative, Independent, Intellectual, Logical, Loving, Obedient, Polite, Responsible, Self-Controlled.
- **Social Value Orientation:** allocation preference from competitive/individualistic to prosocial/altruistic; the common Slider Measure uses six primary items.
- **Functional Theory (18):** Excitement — Emotion, Pleasure, Sexuality; Promotion — Power, Prestige, Success; Existence — Personal Stability, Health, Survival; Suprapersonal — Beauty, Knowledge, Maturity; Interactive — Affectivity, Belonging, Social Support; Normative — Obedience, Religiosity, Tradition.
- **GPLA-5:** Social Responsibility, Risk-Taking, Rule-Following, Self-Competence, Rationality, induced from 123 atomic values.
- **UniVaR:** a continuous latent representation without named value axes, learned contrastively from value-eliciting question–answer sets.
- **Value Kaleidoscope:** Values, Rights, Duties; an ontology rather than a fixed-dimensional profile.
- **HHH:** Helpful, Honest, Harmless.
- **Constitutional AI:** a configurable collection of natural-language normative principles, not a universal fixed-dimensional axiology.
- **GPV:** values are supplied at measurement time and may later be aggregated into Schwartz, Hofstede, or another named space.

</details>

## 💾 Datasets, benchmarks, and instruments

Numbers refer to the released resource or the primary paper. A count is omitted
when it changes by release and the authors do not identify one canonical size.

| Resource | Scale | Labels, dimensions, or task | Links |
|---|---|---|---|
| Value Portrait | **104 queries × 5 responses = 520 items**, rated by **681 people**; benchmarked on **44 LLMs** | correlations with **10 Schwartz values** and **5 Big Five traits**; **549 + 287** significant item–trait correlations retained | [[paper](https://aclanthology.org/2025.acl-long.838/)] |
| ValueBench | **44 psychometric inventories**, **453 dimensions**, evaluation on **6 LLMs** | orientation plus value-to-item and item-to-value understanding tasks | [[paper](https://aclanthology.org/2024.acl-long.111/)] [[code](https://github.com/Value4AI/ValueBench)] |
| WorldValuesBench | **21,492,393 examples**, **93,278 respondents**, **239 value questions**, **42 demographic variables**; probe: **8,280 examples / 36 questions** | demographic context + value question → ordinal human response distribution | [[paper](https://aclanthology.org/2024.lrec-main.1539/)] |
| ValueNet | **21,374 text scenarios** | human attitudes scored across **10 Schwartz values** | [[dataset](https://liang-qiu.github.io/ValueNet/)] |
| ValueEval | **9,324 arguments** from **6 sources**, each labeled by **3 annotators** | **54 fine-grained values** mapped to **20** multi-label categories | [[paper](https://aclanthology.org/2023.semeval-1.313/)] |
| Value FULCRA | **20,000 (LLM output, value vector) pairs** | **10 Schwartz dimensions** and **58 fine-grained value items** | [[paper](https://aclanthology.org/2024.naacl-long.486/)] |
| ValuePrism / Value Kaleidoscope | **218,000 values, rights, and duties** linked to **31,000 situations**; human quality acceptance **91%** | generation, explanation, relevance, and **3-way valence**: supports / opposes / either | [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] [[code](https://github.com/tsor13/kaleido)] |
| ETHICS | **130,000+ examples** in **5 sub-benchmarks** | Justice, Virtue Ethics, Deontology, Utilitarianism, Commonsense Morality | [[paper](https://openreview.net/forum?id=dNy_RKzJacY)] [[code](https://github.com/hendrycks/ethics)] |
| Social Chemistry 101 | **104,000 situations**, **292,000 rules-of-thumb**, **4.5M+ annotations** | **12 judgment dimensions**, including moral foundation, legality, pressure, and social approval | [[paper](https://aclanthology.org/2020.emnlp-main.48/)] |
| Moral Stories | **12,000 narratives × 7 sentences** | norm, situation, intention, moral/immoral action, and corresponding consequences | [[paper](https://aclanthology.org/2021.emnlp-main.54/)] [[code](https://github.com/demelin/moral_stories)] |
| World Values Survey | **7 completed waves** since 1981; almost **120 countries/societies**; Wave 7: **97,220 cases, 66 countries, 606 variables** | changing multilingual batteries on social, political, cultural, moral, and religious values | [[project](https://www.worldvaluessurvey.org/)] |
| PVQ-40 / PVQ-RR | **40 items / 10 values** and **57 items / 19 values** | self-report portrait questionnaires for the original and refined Schwartz spaces | [[measurement source](https://doi.org/10.1177/0022022101032005001)] |

## 🧰 Models, scorers, and representation tools

These are computational components, not value theories. Their output only has
meaning together with the prompt, input unit, value space, aggregation policy,
coverage, and validation evidence.

Hidden-state probes and interventions provide a complementary evidence family:
[structural value features](https://aclanthology.org/2025.findings-acl.1188/),
[controlled value vectors](https://aclanthology.org/2025.acl-long.1326/), and
[value neurons](https://aclanthology.org/2025.findings-emnlp.501/) inspect or alter
internal representations instead of inferring values only from outputs. Linear
decodability is correlational evidence; causal claims additionally need held-out
transfer, matched and random-label controls, and checks for collateral output shifts.

| Tool | Scale and construction | Exact output | Links |
|---|---|---|---|
| ValueLlama-3-8B | **8B-parameter** Llama-3 model fine-tuned on ValueBench and ValuePrism; English | **2 tasks:** binary relevance, then **3-way valence** (supports / opposes / neutral-context-dependent) for any supplied value | [[model](https://huggingface.co/Value4AI/ValueLlama-3-8B)] [[code](https://github.com/Value4AI/gpv)] |
| UniVaR lambda-1 | **137M-parameter** Nomic-BERT encoder; trained contrastively from value-eliciting QA sets produced by **8 source LLMs** | one dense model–language embedding with **no named value coordinates**; paper evaluates **15 models × 25 languages/cultures** | [[model](https://huggingface.co/CAiRE/UniVaR-lambda-1)] [[code](https://github.com/HLTCHKUST/UniVaR)] |
| MoralBERT | BERT-family classifiers fine-tuned on Twitter, Reddit, and Facebook corpora | **10 separate binary classifiers** for virtue/vice poles of the original **5 MFT foundations**; Liberty/Oppression weights are not released | [[code](https://github.com/vjosapreniqi/MoralBERT)] |
| Kaleido | **5 released model sizes:** small, base, large, XL, XXL; trained from **218k** ValuePrism records | candidate generation, explanation, binary relevance, and **3-way valence** over value / right / duty entities | [[code](https://github.com/tsor13/kaleido)] |
| FULCRA / BaseAlign | pipeline trained on **20k output–vector pairs** | a **10-dimensional** Schwartz profile plus **58 item-level** priorities for generated text | [[paper](https://aclanthology.org/2024.naacl-long.486/)] |
| CLAVE | two-model evaluator calibrated with **<100 human labels per value type**; evaluated on **13k+ tuples**, **3 value systems**, and **12+ evaluators** | adaptable reference-free label for a supplied value definition | [[paper](https://arxiv.org/abs/2407.10725)] |

## 🔎 How the domain lists are organized

The Atlas does not score or rank papers. Works are grouped by research question and listed by publication year (newest first), then alphabetically. Contribution types and released artifacts are filters, not quality judgments.

## 📚 Literature by research domain

### 🧭 Value theory and axiologies

Which values exist, and how are they structured?

- ⭐ Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism, Elsevier journal or book, 2013, [[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2184440)] [[paper version](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)]
- ⭐ Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement, SAGE journal, 2001, [[paper](https://doi.org/10.1177/0022022101032005001)]
- ⭐ Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries, Elsevier journal or book, 1992, [[paper](https://psycnet.apa.org/record/2003-00370-001)] [[paper version](https://sciencedirect.com/science/article/pii/S0065260108602816)]
- ⭐ Strategy-Proofness and Arrow's Conditions: Existence and Correspondence Theorems for Voting Procedures and Social Welfare Functions, Elsevier journal or book, 1975, [[paper](https://sciencedirect.com/science/article/pii/0022053175900502)]

### 📏 Measurement and profiling

How are AI values elicited and summarized?

- 📄 A Scalable Approach to Evaluating Moral Sensitivity in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.02972)]
- 📄 Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.10365)]
- 📄 AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.22440)]
- 📄 Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.20205)]
- 📄 Are Language Models Sensitive to Morally Irrelevant Distractors?, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.09416)]
- 📄 Are LLMs Bad at Moral Reasoning?, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11635)]
- ⭐ Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS Oral, 2026, [[paper](https://arxiv.org/abs/2603.13890)] [[code](https://github.com/jingzhe-lin/ASVO)]
- 📄 Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21939)]
- 📄 Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.31213)]
- 📄 Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.12851)]
- 📄 Can Revealed Preferences Clarify LLM Alignment and Steering?, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.08556)]
- 📄 Context-Value-Action Architecture for Value-Driven Large Language Model Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.05939)]
- 📄 Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.22396)]
- 📄 Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.17838)]
- 📄 Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11232)]
- ⭐ How do LLMs reflect human moral foundations? a study using the moral foundations framework, Taylor & Francis journal, 2026, [[paper](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)]
- 📄 Incoherent Values? Probing LLM Preferences Through Parametric Variation, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21102)]
- 📄 LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13944)]
- 📄 Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.11216)]
- 📄 Mechanistic Origin of Moral Indifference in Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.15615)]
- 📄 Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.12515)]
- 📄 Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.08634)]
- 📄 Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.03217)]
- 📄 Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12731)]
- ⭐ On the Alignment of Large Language Models with Global Human Opinion, AAAI 2026 Best Paper (AI Alignment Track), 2026, [[paper](https://arxiv.org/abs/2509.01418)] [[code](https://github.com/ku-nlp/global-opinion-alignment)]
- ⭐ On the Credibility of Evaluating LLMs using Survey Questions, MME, 2026, [[paper](https://aclanthology.org/2026.mme-main.2/)] [[preprint](https://arxiv.org/abs/2602.04033)]
- 📄 Polar: A Benchmark for Evaluating Political Bias in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12922)]
- 📄 Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.28911)]
- 📄 Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2507.07188)]
- 📄 Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05554)]
- 📄 Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.09893)]
- 📄 Superficial Beliefs in LLM Decision-Making, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11016)]
- 📄 Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16017)]
- 📄 Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.10257)]
- 📄 ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08567)]
- 📄 Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.25256)]
- 📄 AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference, OpenReview, 2025, [[paper](https://openreview.net/forum?id=qNlTH4kYJZ)] [[preprint](https://arxiv.org/abs/2505.13531)]
- 📄 Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00751)]
- ⭐ Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1188/)] [[preprint](https://arxiv.org/abs/2501.00581)]
- ⭐ Can Language Models Reason about Individualistic Human Values and Preferences?, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.336/)] [[preprint](https://arxiv.org/abs/2410.03868)]
- 📄 Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.02109)]
- 📄 Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.02481)]
- 📄 Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.02197)]
- ⭐ Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs, ACL Best Paper, 2025, [[paper](https://arxiv.org/abs/2502.01926)]
- 📄 Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.04994)]
- 📄 From Stability to Inconsistency: A Study of Moral Preferences in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.06324)]
- 📄 Generative Value Conflicts Reveal LLM Priorities, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.25369)]
- 📄 Human Psychometric Questionnaires Mischaracterize LLM Behavior, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.10078)]
- 📄 Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.03384)]
- 📄 Improving Language Model Personas via Rationalization with Psychological Scaffolds, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.17993)]
- ⭐ Investigating Value-Reasoning Reliability in Small Large Language Models, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.395/)]
- 📄 Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.22170)]
- 📄 Measurement of LLM's Philosophies of Human Nature, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.02304)] [[code](https://github.com/kodenii/M-PHNS)]
- ⭐ Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.154/)] [[preprint](https://arxiv.org/abs/2501.15463)]
- 📄 Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.08565)]
- ⭐ Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method, Elsevier journal or book, 2025, [[paper](https://sciencedirect.com/science/article/pii/S0925231225008422)]
- 📄 On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.14296)]
- ⭐ Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1529/)] [[preprint](https://arxiv.org/abs/2503.16148)]
- ⭐ Persuading voters using human–artificial intelligence dialogues, Nature, Nature, 2025, [[paper](https://nature.com/articles/s41586-025-09771-9)]
- 📄 Quantifying Data Contamination in Psychometric Evaluations of LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.07175)]
- 📄 Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13490)]
- ⭐ Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR, 2025, [[paper](https://openreview.net/forum?id=3ms8EQY7f8)] [[preprint](https://arxiv.org/abs/2412.06435)] [[code](https://github.com/zfw1226/D2A)]
- 📄 The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.03026)]
- ⭐ The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.806/)] [[preprint](https://arxiv.org/abs/2505.18154)]
- ⭐ Understanding How Value Neurons Shape the Generation of Specified Values in LLMs, Findings of EMNLP, 2025, [[paper](https://aclanthology.org/2025.findings-emnlp.501/)] [[preprint](https://arxiv.org/abs/2505.17712)]
- ⭐ Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation, ACL-DEMO, 2025, [[paper](https://aclanthology.org/2025.acl-demo.64/)]
- 📄 Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.07071)]
- 📄 Value Drifts: Tracing Value Alignment During LLM Post-Training, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.26707)]
- ⭐ Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.838/)] [[preprint](https://arxiv.org/abs/2505.01015)] [[code](https://github.com/holi-lab/ValuePortrait)] [[dataset](https://github.com/holi-lab/ValuePortrait)] [[outputs](https://github.com/holi-lab/ValuePortrait)] [[project](https://holi-lab.github.io/ValuePortrait/)]
- 📄 Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.14633)]
- ⭐ AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, Perspectives on Psychological Science, 2024, [[paper](https://journals.sagepub.com/doi/full/10.1177/17456916231214460)] [[code](https://github.com/feradauto/MoralCoT)]
- 📄 Are Large Language Models Consistent over Value-laden Questions?, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02996)] [[code](https://github.com/jlcmoore/ValueConsistency)] [[dataset](https://github.com/jlcmoore/ValueConsistency)] [[analysis](https://github.com/jlcmoore/ValueConsistency)] [[dataset](https://huggingface.co/datasets/jlcmoore/ValueConsistency)] [[outputs](https://drive.google.com/drive/folders/1SIduLOYD1YOhE8fdu6VuY2PMaeh31h3R)]
- ⭐ Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz’s Theory of Basic Values, JMIR, 2024, [[paper](https://doi.org/10.2196/55988)] [[paper version](https://mental.jmir.org/2024/1/e55988)]
- 📄 Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.12744)]
- 📄 CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.10725)]
- 📄 Cultural Value Differences of LLMs: Prompt, Language, and Model Size, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.16891)]
- 📄 Do LLMs have Consistent Values?, arXiv, 2024, [[paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)] [[preprint](https://arxiv.org/abs/2407.12878)]
- 📄 Evaluating Large Language Models with Psychometrics, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.17675)]
- 📄 Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.08846)]
- 📄 Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.18120)]
- 📄 LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.01460)]
- ⭐ Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI, 2024, [[paper](https://doi.org/10.1609/aaai.v39i25.34839)] [[paper version](https://ojs.aaai.org/index.php/AAAI/article/view/34839)] [[preprint](https://arxiv.org/abs/2409.12106)] [[code](https://github.com/Value4AI/gpv)]
- 📄 Measuring Spiritual Values and Bias of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.11647)]
- ⭐ NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.120/)] [[preprint](https://arxiv.org/abs/2404.12464)] [[code](https://github.com/Akhila-Yerukola/NormAd)]
- 📄 Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing, OpenReview, 2024, [[paper](https://openreview.net/forum?id=0REM9ydeLZ)] [[preprint](https://arxiv.org/abs/2406.14230)]
- 📄 Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.11479)]
- ⭐ ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.111/)] [[preprint](https://arxiv.org/abs/2406.04214)] [[code](https://github.com/Value4AI/ValueBench)]
- ⭐ ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs, WINLP, 2024, [[paper](https://aclanthology.org/2025.winlp-main.15/)] [[preprint](https://arxiv.org/abs/2409.09586)]
- 📄 CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.09705)] [[code](https://github.com/X-PLUG/CValues)] [[dataset](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)]
- 📄 Heterogeneous Value Alignment Evaluation for Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.17147)] [[code](https://github.com/zowiezhang/A2EHV)] [[code](https://github.com/zowiezhang/HVAE)]
- 📄 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.05685)] [[code](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)] [[dataset](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)] [[dataset](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)] [[model](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)]
- ⭐ NLPositionality: Characterizing Design Biases of Datasets and Models, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.505/)] [[project](https://nlpositionality.cs.washington.edu/)]
- 📄 Position: AI Evaluation Should Learn from How We Test Humans, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.10512)]
- ⭐ SocialDial: A Benchmark for Socially-Aware Dialogue Systems, ACM Digital Library, 2023, [[paper](https://dl.acm.org/doi/10.1145/3539618.3591877)] [[code](https://github.com/zhanhl316/SocialDial)]
- 📄 The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.13771)]
- 📄 ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.00378)]
- 📄 What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory, arXiv, 2023, [[paper](https://arxiv.org/abs/2304.03612)]
- ⭐ BBQ: A hand-built bias benchmark for question answering, Findings of ACL, 2022, [[paper](https://aclanthology.org/2022.findings-acl.165/)]
- ⭐ Inertia in Moral and Value Judgments of Large Language Models, NeurIPS, 2022, [[paper](https://arxiv.org/abs/2408.09049)]
- 📄 ProsocialDialog: A Prosocial Backbone for Conversational Agents, arXiv, 2022, [[paper](https://arxiv.org/abs/2205.12688)]
- 📄 Re-contextualizing Fairness in NLP: The Case of India, arXiv, 2022, [[paper](https://arxiv.org/abs/2209.12226)] [[code](https://github.com/google-research-datasets/nlp-fairness-for-india)]
- ⭐ Who is GPT-3? An Exploration of Personality, Values and Demographics, EMNLP NLP+CSS workshop, 2022, [[paper](https://aclanthology.org/2022.nlpcss-1.24/)] [[preprint](https://arxiv.org/abs/2209.14338)] [[code](https://github.com/ben-aaron188/who_is_gpt3)] [[dataset](https://github.com/ben-aaron188/who_is_gpt3)]
- ⭐ Measurement and Fairness, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3442188.3445901)]
- 📄 WebGPT: Browser-assisted question-answering with human feedback, arXiv, 2021, [[paper](https://arxiv.org/abs/2112.09332)] [[dataset](https://huggingface.co/datasets/openai/webgpt_comparisons)]
- 📄 Learning to summarize from human feedback, arXiv, 2020, [[paper](https://arxiv.org/abs/2009.01325)] [[dataset](https://huggingface.co/datasets/openai/summarize_from_feedback)]
- ⭐ Fairness and Abstraction in Sociotechnical Systems, ACM proceedings or journal, 2019, [[paper](https://doi.org/10.1145/3287560.3287598)]

### 🔬 Reliability, validity, and auditing

When is a reported value result stable and valid?

- 📄 A validity-guided workflow for robust large language model research in psychology, arXiv, 2026, [[paper](https://arxiv.org/abs/2507.04491)]
- 📄 Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.18462)]
- 📄 EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.30258)]
- ⭐ A large-scale replication of scenario-based experiments in psychology and management using large language models, Nature Computational Science, 2025, [[paper](https://nature.com/articles/s43588-025-00840-7)]
- ⭐ A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL 2025 Best Paper, 2025, [[paper](https://aclanthology.org/2025.acl-long.1454/)] [[preprint](https://arxiv.org/abs/2402.11005)]
- 📄 Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.11254)]
- 📄 From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.16697)]
- ⭐ Large language models that replace human participants can harmfully misportray and flatten identity groups, Nature Machine Intelligence, 2025, [[paper](https://nature.com/articles/s42256-025-00986-z)]
- 📄 Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.04826)]
- 📄 Psychometric Item Validation Using Virtual Respondents with Trait-Response Mediators, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.05890)]
- 📄 VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05465)]
- ⭐ Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models, NeurIPS, 2024, [[paper](https://arxiv.org/abs/2402.11894)]
- ⭐ Large Language Models are not Fair Evaluators, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.511/)] [[code](https://github.com/i-Eval/FairEval)] [[dataset](https://github.com/i-Eval/FairEval)]
- ⭐ Larger and more instructable language models become less reliable, Nature, 2024, [[paper](https://nature.com/articles/s41586-024-07930-y)]
- 📄 POSIX: A Prompt Sensitivity Index For Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02185)]
- ⭐ Revisiting the Reliability of Psychological Scales on Large Language Models, EMNLP, 2024, [[paper](https://arxiv.org/abs/2305.19926)]
- ⭐ You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments, NAACL, 2024, [[paper](https://arxiv.org/abs/2311.09718)] [[code](https://github.com/orange0629/llm-personas)] [[dataset](https://github.com/orange0629/llm-personas)] [[outputs](https://drive.google.com/file/d/1IL839rl0_qs8jXuLy23IqwLdCYOADeJJ/view?usp=sharing)]
- ⭐ Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing, ACM proceedings or journal, 2020, [[paper](https://doi.org/10.1145/3351095.3372873)]
- ⭐ Model Cards for Model Reporting, ACM proceedings or journal, 2019, [[paper](https://doi.org/10.1145/3287560.3287596)]

### ⚖️ Moral and value understanding

Can systems identify, explain, or reason about values and norms?

- 📄 A Unified Moral-Value Dataset for Instruction Tuning, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.21279)]
- ⭐ How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL Main, 2026, [[paper](https://arxiv.org/abs/2603.13876)] [[code](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)]
- 📄 PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.08951)]
- ⭐ Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL Main (Oral, 2026, [[paper](https://arxiv.org/abs/2509.17703)] [[code](https://github.com/MoralAgentSim/Simulation-Engine)]
- 📄 Analyzing the Ethical Logic of Eight Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.08951)]
- ⭐ Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, ACL 2025 Best Resource Paper, 2025, [[paper](https://aclanthology.org/2025.acl-long.294/)] [[preprint](https://arxiv.org/abs/2502.14083)]
- 📄 Diagnosing Moral Reasoning Acquisition in Language Models: Pragmatics and Generalization, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.16600)]
- ⭐ Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence, Nature Machine Intelligence, 2025, [[paper](https://nature.com/articles/s42256-024-00969-6)]
- 📄 Normative Evaluation of Large Language Models with Everyday Moral Dilemmas, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.18081)]
- ⭐ Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1541/)]
- ⭐ What does AI consider praiseworthy?, AI and Ethics, 2025, [[paper](https://link.springer.com/article/10.1007/s43681-025-00682-z)]
- 📄 Agent Alignment in Evolving Social Norms, arXiv, 2024, [[paper](https://arxiv.org/abs/2401.04620)]
- ⭐ Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31704)]
- 📄 DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02683)] [[code](https://github.com/kellycyy/daily_dilemmas)] [[dataset](https://github.com/kellycyy/daily_dilemmas)] [[outputs](https://github.com/kellycyy/daily_dilemmas)] [[dataset](https://huggingface.co/datasets/kellycyy/daily_dilemmas)]
- ⭐ Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31741)]
- 📄 DeNEVIL: Towards Deciphering and Navigating the Ethical Values of Large Language Models via Instruction Learning, OpenReview, 2024, [[paper](https://openreview.net/forum?id=m3RRWWFaVe)]
- ⭐ Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test, EACL, 2024, [[paper](https://aclanthology.org/2024.eacl-long.176/)] [[preprint](https://arxiv.org/abs/2402.02135)]
- ⭐ Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?, C3NLP, 2024, [[paper](https://arxiv.org/abs/2406.16316)]
- ⭐ Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.560/)] [[preprint](https://arxiv.org/abs/2404.18460)]
- 📄 Evaluating Moral Beliefs across LLMs through a Pluralistic Framework, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.03665)]
- ⭐ Exploring and steering the moral compass of Large Language Models, ICPR, 2024, [[paper](https://arxiv.org/abs/2405.17345)]
- ⭐ Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper), ACM Digital Library, 2024, [[paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)]
- 📄 Inducing Human-like Biases in Moral Reasoning Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.15386)]
- ⭐ Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal Mechanisms and the Superficial Hypothesis, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.918/)]
- 📄 Language Model Alignment in Multilingual Trolley Problems, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02273)]
- 📄 Large-scale moral machine experiment on large language models, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.06790)]
- 📄 LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.00962)]
- 📄 MM-MoralBench: A MultiModal Moral Evaluation Benchmark for Large Vision-Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.20718)]
- ⭐ Moral Foundations of Large Language Models, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.982/)] [[preprint](https://arxiv.org/abs/2310.15337)]
- 📄 Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.11731)]
- 📄 MoralBench: Moral Evaluation of LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.04428)] [[code](https://github.com/agiresearch/MoralBench)]
- 📄 Political Bias in LLMs: Unaligned Moral Values in Agent-centric Simulations, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.11415)]
- 📄 Right vs. Right: Can LLMs Make Tough Choices?, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.19926)]
- ⭐ SaGE: Evaluating Moral Consistency in Large Language Models, LREC-COLING, 2024, [[paper](https://arxiv.org/abs/2402.13709)]
- 📄 The Moral Mind(s) of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.04476)]
- 📄 The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.07304)]
- 📄 Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.18863)]
- 📄 An Evaluation of GPT-4 on the ETHICS Dataset, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.10492)]
- ⭐ EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP, 2023, [[paper](https://dl.acm.org/doi/abs/10.1145/3624918.3625327)] [[code](https://github.com/wanng-ide/ealm)]
- ⭐ Evaluating the Moral Beliefs Encoded in LLMs, NeurIPS, 2023, [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2307.14324)]
- 📄 Exploring the psychology of LLMs' Moral and Legal Reasoning, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.01264)]
- ⭐ Knowledge of cultural moral norms in large language models, ACL, 2023, [[paper](https://arxiv.org/abs/2306.01857)]
- ⭐ Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity, ACL Workshop, 2023, [[paper](https://arxiv.org/abs/2209.12106)]
- 📄 MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions, arXiv, 2023, [[paper](https://arxiv.org/abs/2212.10720)] [[code](https://github.com/thu-coai/MoralDial)]
- ⭐ NormBank: A Knowledge Bank of Situational Social Norms, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.429/)] [[preprint](https://arxiv.org/abs/2305.17008)]
- ⭐ Potential benefits of employing large language models in research in moral education and development, Journal of Moral Education, 2023, [[paper](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)]
- 📄 Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.03047)] [[code](https://github.com/IBM/Dromedary)] [[dataset](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)]
- 📄 Probing the Moral Development of Large Language Models through Defining Issues Test, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.13356)]
- ⭐ Safety and Ethical Concerns of Large Language Models, CCL, 2023, [[paper](https://aclanthology.org/2023.ccl-4.2/)]
- 📄 Safety Assessment of Chinese Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2304.10436)] [[code](https://github.com/thu-coai/Safety-Prompts)] [[project](http://115.182.62.166:18000/)]
- 📄 SafetyBench: Evaluating the Safety of Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.07045)] [[code](https://github.com/thu-coai/SafetyBench)] [[dataset](https://huggingface.co/datasets/thu-coai/SafetyBench)] [[project](https://llmbench.ai/safety)]
- 📄 The Capacity for Moral Self-Correction in Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2302.07459)]
- ⭐ Towards Few-Shot Identification of Morality Frames using In-Context Learning, NLP+CSS, 2023, [[paper](https://aclanthology.org/2022.nlpcss-1.20/)]
- 📄 TrustGPT: A Benchmark for Trustworthy and Responsible Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.11507)] [[code](https://github.com/HowieHwong/TrustGPT)]
- 📄 Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.07792)]
- ⭐ Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety, NeurIPS Workshop, 2022, [[paper](https://arxiv.org/abs/2212.06295)]
- ⭐ Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy, NAACL Workshop, 2022, [[paper](https://arxiv.org/abs/2205.12771)]
- 📄 Large Pre-trained Language Models Contain Human-like Biases of What is Right and Wrong to Do, arXiv, 2022, [[paper](https://arxiv.org/abs/2103.11790)]
- 📄 The Moral Foundations Reddit Corpus, arXiv, 2022, [[paper](https://arxiv.org/abs/2208.05545)]
- ⭐ The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems, ACL, 2022, [[paper](https://aclanthology.org/2022.acl-long.261/)] [[preprint](https://arxiv.org/abs/2204.03021)] [[code](https://github.com/SALT-NLP/mic)]
- ⭐ When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment, NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf)] [[paper version](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2210.01478)] [[dataset](https://huggingface.co/datasets/feradauto/MoralExceptQA)]
- ⭐ A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3465416.3483305)]
- 📄 Analysis of Moral Judgement on Reddit, arXiv, 2021, [[paper](https://arxiv.org/abs/2101.07664)]
- 📄 Can Machines Learn Morality? The Delphi Experiment, arXiv, 2021, [[paper](https://arxiv.org/abs/2110.07574)] [[project](https://delphi.allenai.org/)]
- 📄 Ethical and social risks of harm from Language Models, arXiv, 2021, [[paper](https://arxiv.org/abs/2112.04359)]
- ⭐ Process for Adapting Language Models to Society (PALMS) with Values-Targeted Datasets, NeurIPS, 2021, [[paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)] [[preprint](https://arxiv.org/abs/2106.10328)]
- ⭐ CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models, EMNLP, 2020, [[paper](https://aclanthology.org/2020.emnlp-main.154/)] [[code](https://github.com/nyu-mll/crows-pairs)]
- 📄 Learning Norms from Stories: A Prior for Value Aligned Agents, arXiv, 2020, [[paper](https://arxiv.org/abs/1912.03553)]
- ⭐ Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment, SAGE journal, 2020, [[paper](https://journals.sagepub.com/doi/10.1177/1948550619876629)] [[paper version](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)]
- ⭐ Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences, EMNLP, 2020, [[paper](https://aclanthology.org/2021.emnlp-main.54/)] [[preprint](https://arxiv.org/abs/2012.15738)] [[code](https://github.com/demelin/moral_stories)]
- ⭐ Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes, 000 real-life anecdotes. Lourie et al. AAAI., 2020, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396)] [[preprint](https://arxiv.org/abs/2008.09094)] [[code](https://github.com/allenai/scruples)]
- ⭐ Social Chemistry 101: Learning to Reason about Social and Moral Norms, EMNLP, 2020, [[paper](https://aclanthology.org/2020.emnlp-main.48/)] [[preprint](https://arxiv.org/abs/2011.00620)] [[dataset](https://maxwellforbes.com/social-chemistry/)] [[project](https://maxwellforbes.com/social-chemistry/)]

### 🎯 Choice, action, and behavior

Which values govern choices and behavior under conflict?

- 📄 Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.27699)]
- 📄 D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.19834)]
- 📄 Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12369)]
- ⭐ Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents, Springer journal or proceedings, 2026, [[paper](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)]
- 📄 CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.10823)]
- ⭐ Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1562/)]
- ⭐ Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.154/)] [[preprint](https://arxiv.org/abs/2501.15463)]
- 📄 Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.05018)]
- ⭐ The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.806/)] [[preprint](https://arxiv.org/abs/2505.18154)]
- ⭐ What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.317/)]
- ⭐ How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior, Nature Human Behaviour, 2024, [[paper](https://nature.com/articles/s41562-024-01938-0.pdf)]
- ⭐ How large language models can reshape collective intelligence, Nature Human Behavior, 2024, [[paper](https://nature.com/articles/s41562-024-01959-9)]
- 📄 Language Model Alignment in Multilingual Trolley Problems, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02273)]
- 📄 Align on the Fly: Adapting Chatbot Behavior to Established Norms, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.15907)] [[code](https://github.com/GAIR-NLP/OPO)]
- 📄 Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned, arXiv, 2022, [[paper](https://arxiv.org/abs/2209.07858)] [[dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)]
- 📄 Social Bias Frames: Reasoning about Social and Power Implications of Language, arXiv, 2019, [[paper](https://arxiv.org/abs/1911.03891)] [[dataset](https://maartensap.com/social-bias-frames/)] [[project](https://maartensap.com/social-bias-frames/)]
- ⭐ The theory of planned behavior, Elsevier journal or book, 1991, [[paper](https://sciencedirect.com/science/article/pii/074959789190020T)]

### 🌍 Culture, opinions, and social representation

Whose cultures, opinions, and social perspectives are represented?

- 📄 ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12962)]
- 📄 Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective, arXiv, 2026, [[paper](https://arxiv.org/abs/2408.04638)]
- 📄 Aligning Language Models from User Interactions, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.12273)]
- 📄 AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.26680)]
- 📄 APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.21063)]
- 📄 APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.27419)]
- 📄 Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.02300)]
- 📄 Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.15755)]
- 📄 Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.12851)]
- 📄 CCBENCH: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05405)]
- 📄 Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.20229)]
- 📄 CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.14773)]
- 📄 Cultural Adaptation in Large Language Models for Political Discourse, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.23332)]
- 📄 Cultural Value Alignment Via Latent Activation Steering in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.26365)]
- 📄 Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.22396)]
- 📄 CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.01879)]
- 📄 CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.04885)]
- 📄 Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.18310)]
- 📄 Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.06210)]
- 📄 EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.26883)]
- 📄 Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.20589)]
- 📄 From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.23382)]
- 📄 From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.16303)]
- 📄 From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.00728)]
- 📄 From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20006)]
- 📄 From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.18271)]
- 📄 Improving Cross-Cultural Survey Simulation with Calibrated Value Personas, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.16193)]
- 📄 Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.24647)]
- 📄 Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16120)]
- 📄 Learning to summarize user information for personalized reinforcement learning from human feedback, OpenReview, 2026, [[paper](https://openreview.net/forum?id=Ar078WR3um)]
- 📄 Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.08797)]
- 📄 MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.25342)]
- 📄 Meta-Learning Preferences for Multilingual LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.13315)]
- 📄 Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.22475)]
- 📄 Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12091)]
- 📄 NextQuill: Causal Preference Modeling for Enhancing LLM Personalization, OpenReview, 2026, [[paper](https://openreview.net/forum?id=xYpVlKMFqv)]
- 📄 Opinion dynamics and mutual influence with LLM agents through dialog simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.12583)]
- 📄 P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling, OpenReview, 2026, [[paper](https://openreview.net/forum?id=hXNApWLBZG)]
- 📄 PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.04003)]
- 📄 Persona-Based Simulation of Human Opinion at Population Scale, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.27056)]
- 📄 Personalized Benchmarking: Evaluating LLMs by Individual Preferences, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.18943)]
- 📄 Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.10009)]
- 📄 Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It, OpenReview, 2026, [[paper](https://openreview.net/forum?id=O1hfVE0UxG)]
- 📄 Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.07343)]
- 📄 PersonaVLM: Long-Term Personalized Multimodal LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.13074)]
- 📄 Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.06194)]
- 📄 Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.22345)]
- 📄 Preference-Aware Rubric Learning for Personalized Evaluation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.31545)]
- 📄 Silicon Sampling via Cross-Survey Transfer, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.03091)]
- 📄 Steerable Cultural Preference Optimization of Reward Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.18606)]
- 📄 Steering LLMs for Culturally Localized Generation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.23301)]
- 📄 Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback, OpenReview, 2026, [[paper](https://openreview.net/forum?id=nc28mSbyVG)]
- 📄 Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.10991)]
- 📄 The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20225)]
- 📄 The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.04570)]
- 📄 Think-While-Generating: On-the-Fly Reasoning for Personalized Long-Form Generation, OpenReview, 2026, [[paper](https://openreview.net/forum?id=lle0aGQyQb)]
- 📄 Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.21700)]
- 📄 Toward Culturally Grounded Natural Language Processing, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.26013)]
- 📄 TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.01755)]
- 📄 Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.12878)]
- 📄 What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data, OpenReview, 2026, [[paper](https://openreview.net/forum?id=sC6A1bFDUt)]
- 📄 XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.14063)]
- 📄 XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.05662)]
- 📄 'Too much alignment; not enough culture': Re-balancing cultural alignment practices in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.26167)]
- 📄 A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.14106)]
- 📄 Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study, arXiv, 2025, [[paper](https://arxiv.org/abs/2412.13169)]
- 📄 Aligning VLM Assistants with Personalized Situated Cognition, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00930)]
- 📄 Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.19148)]
- 📄 An Evaluation of Cultural Value Alignment in LLM, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.08863)]
- 📄 Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.13149)]
- ⭐ Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS D&B Track Best Paper, 2025, [[paper](https://arxiv.org/abs/2510.22954)]
- ⭐ Benchmarking Distributional Alignment of Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.2/)] [[preprint](https://arxiv.org/abs/2411.05403)]
- 📄 Benchmarking Multi-National Value Alignment for Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.12911)]
- 📄 Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.18282)]
- ⭐ Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.2/)] [[preprint](https://arxiv.org/abs/2502.08045)]
- 📄 C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.01495)]
- 📄 Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.01127)]
- 📄 CARE: Multilingual Human Preference Learning for Cultural Awareness, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.05154)]
- 📄 CAReDiO: Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.08820)]
- 📄 CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.04756)]
- 📄 Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.17256)]
- 📄 CulFiT: A Fine-grained Cultural-aware LLM Training Paradigm via Multilingual Critique Data Synthesis, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.19484)]
- 📄 Cultural Alignment in Large Language Models Using Soft Prompt Tuning, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.16094)]
- ⭐ Cultural Learning-Based Culture Adaptation of Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.156/)] [[preprint](https://arxiv.org/abs/2504.02953)]
- ⭐ Cultural tendencies in generative AI, Nature Human Behaviour, 2025, [[paper](https://nature.com/articles/s41562-025-02242-1)]
- 📄 Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17112)]
- 📄 Culture is Not Trivia: Sociocultural Theory for Cultural NLP, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.12057)]
- 📄 CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.10886)]
- 📄 CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.12014)]
- 📄 Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.21977)]
- 📄 DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.17399)] [[code](https://github.com/pramitsahoo/culture-evaluation)] [[dataset](https://huggingface.co/datasets/nlip/DIWALI)] [[project](https://nlip-lab.github.io/nlip/publications/diwali/)]
- 📄 Drift: Decoding-time Personalized Alignments with Implicit User Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.14289)]
- 📄 Embodied Agents Meet Personalization: Investigating Challenges and Solutions Through the Lens of Memory Utilization, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16348)]
- 📄 EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.20264)]
- 📄 EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.16545)]
- 📄 Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.21798)]
- 📄 Everyone Deserves A Reward: Learning Customized Human Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2309.03126)]
- 📄 Exploring Cultural Variations in Moral Judgments with Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12433)]
- 📄 Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.18071)]
- 📄 From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15463)]
- 📄 From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16610)]
- 📄 From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16408)]
- ⭐ Generative language models exhibit social identity biases, Nature Computational Science, Nature Computational Science, 2025, [[paper](https://nature.com/articles/s43588-024-00741-1)]
- 📄 GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.13766)] [[code](https://github.com/floschne/gimmick)] [[model](https://huggingface.co/floschne)]
- 📄 Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05931)]
- 📄 How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.17773)]
- 📄 Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.16280)]
- 📄 IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.08395)]
- ⭐ Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1028/)] [[preprint](https://arxiv.org/abs/2502.16761)]
- ⭐ Large language models (LLM) in computational social science: prospects, current state, and challenges, Social Network Analysis and Mining, 2025, [[paper](https://link.springer.com/article/10.1007/s13278-025-01428-9)]
- 📄 Linear Representations of Political Perspective Emerge in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.02080)]
- 📄 LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15003)]
- 📄 LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.00853)]
- ⭐ Machine Bias. How Do Generative Language Models Answer Opinion Polls?, Sociological Methods & Research, 2025, [[paper](https://doi.org/10.1177/00491241251330582)]
- 📄 Made-in China, Thinking in America:U.S. Values Persist in Chinese LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.13723)]
- 📄 Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.09637)]
- 📄 MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.19073)]
- 📄 MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.24846)]
- ⭐ Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision–Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.490/)] [[code](https://github.com/MinhDucBui/Multi3Hate)] [[dataset](https://huggingface.co/datasets/MinhDucBui/Multi3Hate)]
- 📄 Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.16534)]
- 📄 NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.18383)]
- 📄 NoveltyBench: Evaluating Language Models for Humanlike Diversity, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.05228)]
- ⭐ Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1529/)] [[preprint](https://arxiv.org/abs/2503.16148)]
- 📄 Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.12663)]
- 📄 PersonaAgent: Bridging Memory and Action for Personalized LLM Agents, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06254)]
- 📄 PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12915)]
- 📄 PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.09902)]
- 📄 Personalized LLM Decoding via Contrasting Personal Preference, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12109)]
- 📄 PEToolLLM: Towards Personalized Tool Learning in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.18980)]
- 📄 POPI: Personalizing LLMs via Optimized Natural Language Preference Inference, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.17881)]
- 📄 POW: Political Overton Windows of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.08853)]
- 📄 PrefPalette: Personalized Preference Modeling with Latent Attributes, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13541)]
- 📄 PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.04607)]
- 📄 Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.11311)]
- 📄 Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.08688)] [[code](https://github.com/ariba-k/llm-cultural-alignment-evaluation)] [[dataset](https://github.com/ariba-k/llm-cultural-alignment-evaluation)] [[dataset](https://huggingface.co/datasets/akhan02/cultural-dimension-cover-letters)]
- 📄 Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17571)]
- 📄 RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.03939)]
- ⭐ Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.162/)] [[preprint](https://arxiv.org/abs/2502.07068)]
- 📄 STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.20645)]
- 📄 Steering Large Language Models for Machine Translation Personalization, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16612)]
- ⭐ Survey of Cultural Awareness in Language Models: Text and Beyond, Computational Linguistics, 2025, [[paper](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)] [[preprint](https://arxiv.org/abs/2411.00860)] [[code](https://github.com/siddheshih/culture-awareness-llms)] [[project](https://github.com/siddheshih/culture-awareness-llms)]
- 📄 SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.05598)]
- 📄 Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.15456)]
- ⭐ The AI Gap: How Socioeconomic Status Affects Language Technology Interactions, ACL Best Social Impact Paper, 2025, [[paper](https://arxiv.org/abs/2505.12158)]
- ⭐ The discordance between embedded ethics and cultural inference in large language models, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.743/)] [[code](https://github.com/AidaRamezani/ethics_culture)]
- 📄 Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.07018)]
- 📄 Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.18849)]
- ⭐ Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation, Elsevier journal or book, 2025, [[paper](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)]
- 📄 When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.24613)]
- 📄 When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.19158)]
- 📄 Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00242)]
- 📄 AI PERSONA: Towards Life-long Personalization of LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.13103)]
- 📄 Aligning Language Models with Demonstrated Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.00888)]
- ⭐ Aligning Large Language Models with Diverse Political Viewpoints, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.412/)]
- 📄 Aligning LLMs with Individual Preferences via Interaction, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.03642)]
- 📄 An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.01247)] [[code](https://github.com/simran-khanuja/image-transcreation)]
- 📄 Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.19323)]
- 📄 Attributing Culture-Conditioned Generations to Pretraining Corpora, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.20760)] [[code](https://github.com/huihanlhh/CultureGenAttr)]
- ⭐ BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.398/)]
- 📄 Beyond Aesthetics: Cultural Competence in Text-to-Image Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.06863)] [[code](https://github.com/google-research-datasets/cube)]
- 📄 Beyond Partisan Leaning: A Comparative Analysis of Political Bias in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.16746)]
- 📄 BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.09948)] [[code](https://github.com/nlee0212/BLEnD)]
- 📄 Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys, arXiv, 2024, [[paper](https://arxiv.org/abs/2401.10352)] [[code](https://github.com/yongcaoplus/cuDialog)]
- ⭐ CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31710)] [[preprint](https://arxiv.org/abs/2405.13974)]
- 📄 CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.06412)] [[code](https://github.com/rladmstn1714/CLIcK)]
- ⭐ CMoralEval: A Moral Evaluation Benchmark for Chinese Large Language Models, Findings of ACL, 2024, [[paper](https://aclanthology.org/2024.findings-acl.703/)]
- ⭐ ComPO: Community Preferences for Language Model Personalization, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.419/)] [[preprint](https://arxiv.org/abs/2410.16027)]
- 📄 Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.08968)]
- ⭐ Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM, 2024, [[paper](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768)] [[dataset](https://mango.mpi-inf.mpg.de/)]
- 📄 Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11661)]
- 📄 CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02677)]
- 📄 Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.03930)]
- 📄 CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.06664)]
- ⭐ CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.288/)] [[preprint](https://arxiv.org/abs/2404.15238)]
- ⭐ CultureLLM: Incorporating Cultural Differences into Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2402.10946)] [[code](https://github.com/Scarelette/CultureLLM)]
- ⭐ CulturePark: Boosting Cross-cultural Understanding in Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2405.15145)]
- 📄 DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.14651)] [[code](https://github.com/microsoft/DOSA)]
- ⭐ Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.560/)] [[preprint](https://arxiv.org/abs/2404.18460)]
- 📄 Evaluating the Prompt Steerability of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.12405)]
- 📄 Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.13993)]
- 📄 Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis, arXiv, 2024, [[paper](https://arxiv.org/abs/2308.16705)] [[code](https://github.com/nlee0212/CREHate)]
- 📄 Extrinsic Evaluation of Cultural Competence in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11565)]
- 📄 Few-shot Personalization of LLMs with Mis-aligned Responses, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.18678)]
- ⭐ FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.1063/)] [[code](https://github.com/lyan62/FoodieQA)] [[dataset](https://huggingface.co/datasets/lyan62/FoodieQA)]
- 📄 Having Beer after Prayer? Measuring Cultural Bias in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2305.14456)] [[code](https://github.com/tareknaous/camel)]
- 📄 How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.14805)]
- 📄 Investigating Cultural Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.13231)]
- 📄 Language Model Alignment in Multilingual Trolley Problems, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02273)]
- 📄 Large Language Model Safety: A Holistic Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.17686)]
- 📄 Large Language Models Empowered Personalized Web Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.17236)]
- ⭐ Large language models, social demography, and hegemony: comparing authorship in human and synthetic text, Springer journal or proceedings, 2024, [[paper](https://link.springer.com/article/10.1186/s40537-024-00986-7)]
- ⭐ Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs, NAACL (Short Paper, 2024, [[paper](https://arxiv.org/abs/2403.13592)]
- 📄 LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.06032)]
- 📄 LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14012)]
- 📄 M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.03791)] [[code](https://github.com/floschne/m5b)]
- 📄 MAP: Multi-Human-Value Alignment Palette, OpenReview, 2024, [[paper](https://openreview.net/forum?id=NN6QHwgRrQ)] [[preprint](https://arxiv.org/abs/2410.19198)]
- 📄 Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.14843)]
- 📄 Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.09369)] [[code](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)]
- 📄 MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14184)]
- ⭐ Navigating the Cultural Kaleidoscope: A Hitchhiker's Guide to Sensitivity in Large Language Models, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.388/)] [[preprint](https://arxiv.org/abs/2410.12880)] [[code](https://github.com/NeuralSentinel/CulturalKaleidoscope)]
- ⭐ NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.120/)] [[preprint](https://arxiv.org/abs/2404.12464)] [[code](https://github.com/Akhila-Yerukola/NormAd)]
- 📄 PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=1kFDrYCuSu)]
- 📄 Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.11060)]
- 📄 Personalized Adaptation via In-Context Preference Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14001)]
- 📄 Personalized Language Modeling from Personalized Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.05133)]
- 📄 PersonalLLM: Tailoring LLMs to Individual Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.20296)]
- ⭐ Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models, ACL, 2024, [[paper](https://arxiv.org/abs/2402.16786)] [[code](https://github.com/paul-rottger/llm-values-pct)] [[dataset](https://github.com/paul-rottger/llm-values-pct)] [[outputs](https://github.com/paul-rottger/llm-values-pct)]
- 📄 Political-LLM: Large Language Models in Political Science, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.06864)] [[project](https://political-llm.org/)]
- 📄 PRISM: A Methodology for Auditing Biases in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.18906)]
- ⭐ Questioning the Survey Responses of Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2306.07951)] [[code](https://github.com/socialfoundations/surveying-language-models)] [[analysis](https://github.com/socialfoundations/surveying-language-models)] [[outputs](https://keeper.mpdl.mpg.de/d/b8090e1c552d45cebb68/)]
- 📄 Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.18144)]
- ⭐ RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations, Findings of NAACL, 2024, [[paper](https://aclanthology.org/2024.findings-naacl.196/)] [[code](https://github.com/zhanhl316/ReNoVi)]
- 📄 Representation Bias in Political Sample Simulations with Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.11409)]
- ⭐ Revealing Fine-Grained Values and Opinions in Large Language Models, EMNLP Findings, 2024, [[paper](https://arxiv.org/abs/2406.19238)]
- ⭐ Stick to your role! Stability of personal values expressed in large language models, PLOS ONE, 2024, [[paper](https://doi.org/10.1371/journal.pone.0309114)] [[model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309114)]
- 📄 The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.12744)]
- 📄 The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11096)]
- ⭐ The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models, NeurIPS, 2024, [[paper](https://openreview.net/forum?id=DFr5hteojx)] [[paper version](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)] [[preprint](https://arxiv.org/abs/2404.16019)] [[code](https://github.com/HannahKirk/prism-alignment)]
- ⭐ The Self-Perception and Political Biases of ChatGPT, Human Behavior and Emerging Technologies, 2024, [[paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)]
- 📄 Towards Measuring and Modeling "Culture" in LLMs: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.15412)] [[code](https://github.com/faridlazuarda/cultural-llm-papers)]
- 📄 Vision-Language Models under Cultural and Inclusive Considerations, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.06177)]
- 📄 Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.08563)]
- 📄 WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.12705)] [[dataset](https://worldcuisines.github.io/)] [[project](https://worldcuisines.github.io/)]
- ⭐ WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1539/)] [[preprint](https://arxiv.org/abs/2404.16308)]
- 📄 AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.09620)]
- 📄 Assessing Cross-Cultural Alignment between ChatGPT and Human Societies: An Empirical Study, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.17466)]
- 📄 CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.16421)]
- ⭐ Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions, COLING, 2023, [[paper](https://aclanthology.org/2025.coling-main.567/)] [[preprint](https://arxiv.org/abs/2309.12342)]
- ⭐ Cultural Bias and Cultural Alignment of Large Language Models, PNAS Nexus, 2023, [[paper](https://doi.org/10.1093/pnasnexus/pgae346)] [[preprint](https://arxiv.org/abs/2311.14096)]
- ⭐ Cultural Concept Adaptation on Multimodal Reasoning, EMNLP, 2023, [[paper](https://aclanthology.org/2023.emnlp-main.18/)]
- ⭐ Culturally Aware Natural Language Inference, Findings of EMNLP, 2023, [[paper](https://aclanthology.org/2023.findings-emnlp.509/)] [[code](https://github.com/SALT-NLP/CulturallyAwareNLI)]
- ⭐ Demonstrations of the Potential of AI-based Political Issue Polling, Harvard Data Science Review (HDSR), 2023, [[paper](https://arxiv.org/abs/2307.04781)]
- 📄 DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.05076)]
- 📄 EtiCor: Corpus for Analyzing LLMs for Etiquettes, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.18974)]
- ⭐ FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models, Findings of ACL, 2023, [[paper](https://aclanthology.org/2023.findings-acl.631/)] [[code](https://github.com/shramay-palta/FORK_ACL2023)]
- ⭐ From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models, ACL, 2023, [[paper](https://arxiv.org/abs/2305.08283)]
- 📄 GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.01893)] [[code](https://github.com/WadeYin9712/GIVL)]
- 📄 Global Voices, Local Biases: Socio-Cultural Prejudices across Languages, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.17586)] [[code](https://github.com/iamshnoo/weathub)]
- 📄 Holistic Evaluation of Language Models, OpenReview, 2023, [[paper](https://openreview.net/forum?id=iO4LZibEqW)]
- ⭐ How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?, Digital Society, 2023, [[paper](https://link.springer.com/article/10.1007/s44206-023-00054-2)]
- 📄 Large Language Models as Superpositions of Cultural Perspectives, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.07870)] [[code](https://gitlab.inria.fr/gkovac/value_stability)]
- 📄 Large Language Models Can Be Used to Estimate the Latent Positions of Politicians, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.12057)]
- ⭐ More human than human: measuring ChatGPT political bias, Springer journal or proceedings, 2023, [[paper](https://link.springer.com/article/10.1007/s11127-023-01097-2)]
- 📄 Multi-lingual and Multi-cultural Figurative Language Understanding, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.16171)] [[code](https://github.com/simran-khanuja/Multilingual-Fig-QA)]
- 📄 Multilingual Language Models are not Multicultural: A Case Study in Emotion, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.01370)]
- 📄 NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly, arXiv, 2023, [[paper](https://arxiv.org/abs/2210.08604)] [[code](https://github.com/yrf1/NormSage)]
- 📄 On the steerability of large language models toward data-driven personas, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.04978)]
- 📄 Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.11564)]
- 📄 SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.11840)] [[code](https://github.com/google-research-datasets/seegull)]
- ⭐ The Political Biases of ChatGPT, Social Sciences, 2023, [[paper](https://mdpi.com/2076-0760/12/3/148)]
- 📄 The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.01768)]
- 📄 The Rise and Potential of Large Language Model Based Agents: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.07864)] [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)]
- 📄 Towards Measuring the Representation of Subjective Global Opinions in Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.16388)] [[dataset](https://huggingface.co/datasets/Anthropic/llm_global_opinions)] [[project](https://llmglobalvalues.anthropic.com/)]
- 📄 UltraFeedback: Boosting Language Models with Scaled AI Feedback, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.01377)] [[code](https://github.com/OpenBMB/UltraFeedback)] [[dataset](https://huggingface.co/datasets/openbmb/UltraFeedback)]
- 📄 Whose Opinions Do Language Models Reflect?, arXiv, 2023, [[paper](https://proceedings.mlr.press/v202/santurkar23a.html)] [[preprint](https://arxiv.org/abs/2303.17548)] [[code](https://github.com/tatsu-lab/opinions_qa)] [[analysis](https://github.com/tatsu-lab/opinions_qa)] [[dataset](https://worksheets.codalab.org/worksheets/0x6fb693719477478aac73fc07db333f69)] [[outputs](https://worksheets.codalab.org/worksheets/0x6fb693719477478aac73fc07db333f69)]
- 📄 Challenges and Strategies in Cross-Cultural NLP, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.10020)]
- ⭐ CommunityLM: Probing Partisan Worldviews from Language Models, COLING, 2022, [[paper](https://arxiv.org/abs/2209.07065)]
- 📄 EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.14498)]
- 📄 Probing Pre-Trained Language Models for Cross-Cultural Differences in Values, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.13722)]
- 📄 SafeText: A Benchmark for Exploring Physical Safety in Language Models, arXiv, 2022, [[paper](https://arxiv.org/abs/2210.10045)] [[code](https://github.com/sharonlevy/SafeText)]
- ⭐ On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3442188.3445922)]
- 📄 Visually Grounded Reasoning across Languages and Cultures, arXiv, 2021, [[paper](https://arxiv.org/abs/2109.13238)] [[project](https://marvl-challenge.github.io/)]
- ⭐ RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models, Findings of EMNLP, 2020, [[paper](https://aclanthology.org/2020.findings-emnlp.301/)]
- ⭐ Would you Rather? A New Benchmark for Learning Machine Alignment with Cultural Values and Social Preferences, ACL, 2020, [[paper](https://aclanthology.org/2020.acl-main.477/)]
- ⭐ Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science, TACL, 2018, [[paper](https://aclanthology.org/Q18-1041/)]

### 🗣️ Pluralism and preference aggregation

How should heterogeneous values and preferences be represented or aggregated?

- 📄 A Roadmap to Impactful Pluralistic Alignment Research, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.22305)]
- 📄 Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.01642)]
- 📄 Coherence Maximization Improves Pluralistic Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.03110)]
- 📄 DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.14420)]
- 📄 Evaluating Pluralism in LLMs through Latent Perspectives, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13254)]
- 📄 From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.14912)]
- 📄 MixDPO: Modeling Preference Strength for Pluralistic Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.06180)]
- 📄 Overton Pluralistic Reinforcement Learning for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.20759)]
- 📄 PERSPECTRA: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08716)]
- 📄 PLURAL: A Global Dataset for Value Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.08034)]
- 📄 Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20805)]
- ⭐ The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models, EACL, 2026, [[paper](https://aclanthology.org/2026.eacl-long.305/)]
- 📄 Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.17283)]
- 📄 VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.04822)]
- 📄 VISPA: Pluralistic Alignment via Automatic Value Selection and Activation, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12758)]
- 📄 A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values, OpenReview, 2025, [[paper](https://openreview.net/forum?id=oSRqZO2O2O)]
- 📄 Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.23820)]
- ⭐ Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS D&B Track Best Paper, 2025, [[paper](https://arxiv.org/abs/2510.22954)]
- 📄 Benchmarking Overton Pluralism in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.01351)]
- 📄 Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05154)]
- 📄 Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.18526)]
- ⭐ Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1301/)] [[preprint](https://arxiv.org/abs/2510.04045)]
- 📄 Imitation Beyond Expectation Using Pluralistic Stochastic Dominance, OpenReview, 2025, [[paper](https://openreview.net/forum?id=YX5DHa9OfX)]
- 📄 LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.01894)]
- 📄 LoRe: Personalizing LLMs via Low-Rank Reward Modeling, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.14439)]
- 📄 MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.16380)]
- 📄 Optimized Distortion in Linear Social Choice, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.20020)]
- 📄 Pairwise Calibrated Rewards for Pluralistic Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06298)]
- ⭐ PERSONA: A Reproducible Testbed for Pluralistic Alignment, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.752/)]
- 📄 PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.16679)]
- ⭐ Pluralistic Alignment for Healthcare: A Role-Driven Framework, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1596/)] [[preprint](https://arxiv.org/abs/2509.10685)]
- ⭐ PluralLLM: Pluralistic Alignment in LLMs via Federated Learning, ACM Digital Library, 2025, [[paper](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)]
- 📄 Reflective Verbal Reward Design for Pluralistic Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.17834)]
- ⭐ SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.41/)]
- 📄 Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.08509)]
- 📄 Value Alignment of Social Media Ranking Algorithms, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.14434)]
- ⭐ VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1119/)] [[preprint](https://arxiv.org/abs/2502.13775)]
- 📄 Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13383)]
- 📄 A Roadmap to Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=gQpBnRHwxM)] [[preprint](https://arxiv.org/abs/2402.05070)] [[code](https://github.com/jfisher52/AI_Pluralistic_Alignment)] [[dataset](https://github.com/jfisher52/AI_Pluralistic_Alignment)] [[dataset](https://drive.google.com/file/d/1MOE4y_nGJiYU_vxCqnWSiYIKCk-dqPJE/view?usp=sharing)] [[dataset](https://huggingface.co/datasets/Anthropic/llm_global_opinions)]
- ⭐ Aligning to Thousands of Preferences via System Message Generalization, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2405.17977)]
- 📄 Axioms for AI Alignment from Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.14758)]
- 📄 Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.11167)]
- ⭐ From Distributional to Overton Pluralism: Investigating Large Language Model Alignment, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.346/)] [[preprint](https://arxiv.org/abs/2406.17692)]
- 📄 Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=JI6j4NUGHv)]
- ⭐ Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.240/)] [[preprint](https://arxiv.org/abs/2406.15951)]
- 📄 PAD: Personalized Alignment of LLMs at Decoding-Time, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.04070)]
- 📄 PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.08469)]
- 📄 Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.10075)]
- 📄 Plurals: A System for Guiding LLMs Via Simulated Social Ensembles, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.17213)]
- 📄 Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.08622)]
- 📄 Representative Social Choice: From Learning Theory to AI Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.23953)]
- 📄 RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.00254)]
- 📄 Rules, Cases, and Reasoning: Positivist Legal Theory as a Framework for Pluralistic AI Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.17271)]
- ⭐ Self-Pluralising Culture Alignment for Large Language Models, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.350/)] [[preprint](https://arxiv.org/abs/2410.12971)]
- 📄 Assessing LLMs for Moral Value Pluralism, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.10075)]
- ⭐ Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, AAAI, 2023, [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] [[preprint](https://arxiv.org/abs/2309.00779)] [[code](https://github.com/tsor13/kaleido)]
- 📄 Fine-tuning language models to find agreement among humans with diverse preferences, arXiv, 2022, [[paper](https://arxiv.org/abs/2211.15006)]

### 🧰 Alignment and steering

How are normative targets used to train or steer systems?

- 📄 AI Alignment Breaks at the Edge, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.20042)]
- ⭐ Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping, AAAI, 2026, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41109)]
- 📄 Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.13705)]
- ⭐ Communication-Efficient Desire Alignment for Embodied Agent-Human Adaptation, ACL Main (Oral, 2026, [[paper](https://arxiv.org/abs/2505.22503)]
- 📄 Constitutional Value Potentials: reading and steering internal priority margins in language models, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.15420)]
- 📄 Controllable Value Alignment in Large Language Models through Neuron-Level Editing, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.07356)]
- 📄 Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.10588)]
- ⭐ Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models, ICML, 2026, [[paper](https://arxiv.org/abs/2509.24319)] [[code](https://github.com/holi-lab/ValueMechanism)] [[project](https://holi-lab.github.io/ValueMechanism/)]
- 📄 Parametric Social Identity Injection and Diversification in Public Opinion Simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16142)]
- 📄 Position: Align AI to Our Aspirations, Not Our Flaws, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13755)]
- 📄 Position: The Alignment Community is Unintentionally Building a Censor's Toolkit, OpenReview, 2026, [[paper](https://openreview.net/forum?id=dy2HwmOvFX)]
- 📄 Role Steering of Language Models for Social Simulations, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.00023)]
- ⭐ Simple Role Assignment is Extraordinarily Effective for Safety Alignment, ACL Findings, 2026, [[paper](https://arxiv.org/abs/2602.00061)]
- ⭐ Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents, Springer journal or proceedings, 2026, [[paper](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)]
- 📄 VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.18113)]
- 📄 Aligning Multimodal LLM with Human Preference: A Survey, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.14504)]
- ⭐ Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1188/)] [[preprint](https://arxiv.org/abs/2501.00581)]
- 📄 COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.05535)]
- 📄 Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.23749)]
- 📄 Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach, OpenReview, 2025, [[paper](https://openreview.net/forum?id=6KM1siLL8a)]
- 📄 Diverse Human Value Alignment for Large Language Models via Ethical Reasoning, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.00379)]
- 📄 EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.06370)]
- 📄 Improving the Distributional Alignment of LLMs using Supervision, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.00439)]
- ⭐ Internal Value Alignment in Large Language Models through Controlled Value Vector Activation, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1326/)] [[preprint](https://arxiv.org/abs/2507.11316)] [[code](https://github.com/hr-jin/ConVA)]
- 📄 Justifications for Democratizing AI Alignment and Their Prospects, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.19548)]
- ⭐ Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1028/)] [[preprint](https://arxiv.org/abs/2502.16761)]
- ⭐ Language Models Resist Alignment: Evidence From Data Compression, ACL Best Paper, 2025, [[paper](https://arxiv.org/abs/2406.06144)]
- 📄 MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.12271)]
- 📄 Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.17579)]
- 📄 Prioritization First, Principles Second: An Adaptive Interpretation of Helpful, Honest, and Harmless Principles, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.06059)]
- 📄 Reward Model Perspectives: Whose Opinions Do Reward Models Reward?, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.06391)]
- 📄 Robust Multi-Objective Controlled Decoding of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.08796)]
- ⭐ Scopes of Alignment, AAAI 2025 workshop, 2025, [[paper](https://arxiv.org/abs/2501.12405)]
- 📄 Societal Alignment Frameworks Can Improve LLM Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.00069)]
- ⭐ Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.162/)] [[preprint](https://arxiv.org/abs/2502.07068)]
- 📄 Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.11414)]
- 📄 The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.23965)]
- 📄 The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.03048)]
- ⭐ Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1408/)]
- ⭐ Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1532/)] [[preprint](https://arxiv.org/abs/2506.06404)]
- 📄 Value Alignment of Social Media Ranking Algorithms, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.14434)]
- 📄 ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.04569)]
- 📄 Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00415)]
- 📄 Aligning Crowd Feedback via Distributional Preference Reward Modeling, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.09764)]
- ⭐ Aligning to Thousands of Preferences via System Message Generalization, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2405.17977)]
- ⭐ Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.468/)]
- ⭐ Black-Box Prompt Optimization: Aligning Large Language Models without Model Training, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.176/)]
- ⭐ Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.85/)]
- 📄 CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10199)] [[code](https://github.com/huihanlhh/Culture-Gen)]
- ⭐ CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.288/)] [[preprint](https://arxiv.org/abs/2404.15238)]
- ⭐ CultureLLM: Incorporating Cultural Differences into Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2402.10946)] [[code](https://github.com/Scarelette/CultureLLM)]
- ⭐ CulturePark: Boosting Cross-cultural Understanding in Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2405.15145)]
- 📄 Diverging Preferences: When do Annotators Disagree and do Models Know?, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14632)]
- 📄 Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.06929)]
- 📄 Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.13998)]
- 📄 Foundational Challenges in Assuring Alignment and Safety of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.09932)]
- ⭐ Group Robust Preference Optimization in Reward-free RLHF, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)]
- ⭐ HelpSteer2: Open-source dataset for training top-performing reward models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)] [[preprint](https://arxiv.org/abs/2406.08673)] [[code](https://github.com/NVIDIA/NeMo-Aligner)] [[dataset](https://huggingface.co/datasets/nvidia/HelpSteer2)]
- ⭐ Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.620/)]
- ⭐ KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge, Findings of ACL, 2024, [[paper](https://aclanthology.org/2024.findings-acl.666/)]
- ⭐ Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain, NAACL-INDUSTRY, 2024, [[paper](https://aclanthology.org/2024.naacl-industry.18/)]
- 📄 MallowsPO: Fine-Tune Your LLM with Preference Dispersions, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.14953)]
- 📄 MAP: Multi-Human-Value Alignment Palette, OpenReview, 2024, [[paper](https://openreview.net/forum?id=NN6QHwgRrQ)] [[preprint](https://arxiv.org/abs/2410.19198)]
- 📄 MaxMin-RLHF: Alignment with Diverse Human Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.08925)]
- 📄 MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces, OpenReview, 2024, [[paper](https://openreview.net/forum?id=kyfkMRT4Ao)]
- 📄 Moral Alignment for LLM Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.01639)]
- ⭐ Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.345/)]
- 📄 OASIS: Open Agent Social Interaction Simulations with One Million Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.11581)]
- 📄 Personality Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.11779)]
- 📄 Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.10075)]
- 📄 ProgressGym: Alignment with a Millennium of Moral Progress, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.20087)] [[code](https://github.com/PKU-Alignment/ProgressGym)]
- 📄 RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.00254)]
- 📄 SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.16665)]
- ⭐ SafeWorld: Geo-Diverse Safety Alignment, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)]
- 📄 Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.16482)]
- ⭐ STELA: a community-centred approach to norm elicitation for AI alignment, Nature Scientific Reports, 2024, [[paper](https://nature.com/articles/s41598-024-56648-4)]
- ⭐ Strong and weak alignment of large language models with human values, Nature Scientific Reports, 2024, [[paper](https://nature.com/articles/s41598-024-70031-3)] [[preprint](https://arxiv.org/abs/2408.04655)]
- 📄 Towards Scalable Automated Alignment of LLMs: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.01252)]
- 📄 Unintended Impacts of LLM Alignment on Global Representation, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.15018)]
- ⭐ Value Alignment from Unstructured Text, EMNLP-INDUSTRY, 2024, [[paper](https://aclanthology.org/2024.emnlp-industry.81/)]
- ⭐ ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs, WINLP, 2024, [[paper](https://aclanthology.org/2025.winlp-main.15/)] [[preprint](https://arxiv.org/abs/2409.09586)]
- 📄 What are human values, and how do we align AI to them?, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10636)]
- 📄 Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.08385)]
- 📄 BeaverTails: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.04657)] [[code](https://github.com/PKU-Alignment/safe-rlhf)] [[dataset](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)]
- ⭐ Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions, COLING, 2023, [[paper](https://aclanthology.org/2025.coling-main.567/)] [[preprint](https://arxiv.org/abs/2309.12342)]
- 📄 Foundational Moral Values for AI Alignment, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.17017)]
- ⭐ From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models, EMNLP, 2023, [[paper](https://aclanthology.org/2023.emnlp-main.961/)] [[preprint](https://arxiv.org/abs/2310.17857)]
- 📄 HelpSteer: Multi-attribute Helpfulness Dataset for SteerLM, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.09528)] [[dataset](https://huggingface.co/datasets/nvidia/HelpSteer)]
- 📄 Large Language Model Alignment: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.15025)]
- 📄 Machine Mindset: An MBTI Exploration of Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.12999)] [[code](https://github.com/PKU-YuanGroup/Machine-Mindset)]
- 📄 Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.03047)] [[code](https://github.com/IBM/Dromedary)] [[dataset](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)]
- 📄 Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.15399)]
- ⭐ SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF, Findings of EMNLP, 2023, [[paper](https://aclanthology.org/2023.findings-emnlp.754/)]
- 📄 The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.01552)]
- 📄 Training Socially Aligned Language Models on Simulated Social Interactions, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.16960)] [[code](https://github.com/agi-templar/Stable-Alignment)]
- ⭐ Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values, NAACL, 2023, [[paper](https://aclanthology.org/2024.naacl-long.486/)] [[preprint](https://arxiv.org/abs/2311.10766)] [[code](https://github.com/microsoft/ValueCompass/tree/main/Value_FULCRA)] [[dataset](https://github.com/microsoft/ValueCompass/tree/main/Value_FULCRA)] [[project](https://valuecompass.github.io/)]
- 📄 Constitutional AI: Harmlessness from AI Feedback, arXiv, 2022, [[paper](https://arxiv.org/abs/2212.08073)] [[code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)]
- ⭐ Evaluating and Inducing Personality in Pre-trained Language Models, NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)] [[preprint](https://arxiv.org/abs/2206.07550)]
- 📄 Improving alignment of dialogue agents via targeted human judgements, arXiv, 2022, [[paper](https://arxiv.org/abs/2209.14375)] [[project](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)]
- ⭐ Social Simulacra: Creating Populated Prototypes for Social Computing Systems, ACM Digital Library, 2022, [[paper](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)]
- 📄 Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback, arXiv, 2022, [[paper](https://arxiv.org/abs/2204.05862)] [[code](https://github.com/anthropics/hh-rlhf)] [[dataset](https://github.com/anthropics/hh-rlhf)] [[dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)]
- ⭐ Training language models to follow instructions with human feedback, NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)]
- 📄 A General Language Assistant as a Laboratory for Alignment, arXiv, 2021, [[paper](https://arxiv.org/abs/2112.00861)] [[dataset](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)] [[prompts](https://gist.github.com/jareddk/2509330f8ef3d787fc5aaac67aab5f11)] [[supplement](https://gist.github.com/jareddk/2509330f8ef3d787fc5aaac67aab5f11)]
- ⭐ Process for Adapting Language Models to Society (PALMS) with Values-Targeted Datasets, NeurIPS, 2021, [[paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)] [[preprint](https://arxiv.org/abs/2106.10328)]
- 📄 Aligning AI With Shared Human Values, OpenReview, 2020, [[paper](https://openreview.net/forum?id=dNy_RKzJacY)] [[preprint](https://arxiv.org/abs/2008.02275)] [[code](https://github.com/hendrycks/ethics)]

### 📐 Value representations and model internals

How is value information represented, learned, or causally encoded?

- 📄 A Method for Learning Value Systems in Generative AI, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.16903)]
- 📄 Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05052)]
- 📄 Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.00913)]
- ⭐ Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models, ICML, 2026, [[paper](https://arxiv.org/abs/2509.24319)] [[code](https://github.com/holi-lab/ValueMechanism)] [[project](https://holi-lab.github.io/ValueMechanism/)]
- 📄 Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.04456)]
- 📄 Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.14172)]
- 📄 Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.27373)]
- 📄 Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08835)]
- 📄 Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11018)]
- 📄 Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.22660)]
- 📄 More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.22641)]
- 📄 Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.23659)]
- 📄 Tracing Moral Foundations in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.05437)]
- 📄 VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.03160)]
- 📄 Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.20270)]
- ⭐ Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1188/)] [[preprint](https://arxiv.org/abs/2501.00581)]
- 📄 EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.12792)]
- 📄 Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure, Research Square, 2025, [[paper](https://doi.org/10.21203/rs.3.rs-8270539/v1)]
- ⭐ Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.585/)] [[preprint](https://arxiv.org/abs/2502.02444)] [[code](https://github.com/ValueByte-AI/gpv)] [[dataset](https://github.com/ValueByte-AI/ValueBench)] [[dataset](https://huggingface.co/datasets/PKU-Alignment/BeaverTails)] [[model](https://huggingface.co/Value4AI/ValueLlama-3-8B)]
- ⭐ HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter, ACL Outstanding Paper, 2025, [[paper](https://arxiv.org/abs/2411.15462)]
- 📄 Learning the Value Systems of Societies from Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.20728)]
- 📄 MoVa: Towards Generalizable Classification of Human Morals and Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.24216)]
- 📄 SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.12633)]
- ⭐ The discordance between embedded ethics and cultural inference in large language models, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.743/)] [[code](https://github.com/AidaRamezani/ethics_culture)]
- 📄 The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.11770)]
- ⭐ Understanding How Value Neurons Shape the Generation of Specified Values in LLMs, Findings of EMNLP, 2025, [[paper](https://aclanthology.org/2025.findings-emnlp.501/)] [[preprint](https://arxiv.org/abs/2505.17712)]
- 📄 Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.08640)]
- 📄 Value Lens: Using Large Language Models to Understand Human Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.15722)]
- 📄 Value Profiles for Encoding Human Variation, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15484)]
- 📄 Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.15236)]
- 📄 Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.08453)]
- ⭐ High-Dimension Human Value Representation in Large Language Models, NAACL, 2024, [[paper](https://aclanthology.org/2025.naacl-long.274/)] [[preprint](https://arxiv.org/abs/2404.07900)] [[code](https://github.com/HLTCHKUST/UniVaR)]
- ⭐ Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal Mechanisms and the Superficial Hypothesis, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.918/)]
- 📄 Investigating Human Values in Online Communities, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.14177)]
- 📄 MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.07678)]
- 📄 Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2401.17228)]
- 📄 Do Differences in Values Influence Disagreements in Online Discussions?, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.15757)]
- 📄 Enhancing Stance Classification on Social Media Using Quantified Moral Foundations, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.09848)]
- ⭐ SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments, SemEval, 2023, [[paper](https://aclanthology.org/2023.semeval-1.313/)]
- ⭐ Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values, NAACL, 2023, [[paper](https://aclanthology.org/2024.naacl-long.486/)] [[preprint](https://arxiv.org/abs/2311.10766)] [[code](https://github.com/microsoft/ValueCompass/tree/main/Value_FULCRA)] [[dataset](https://github.com/microsoft/ValueCompass/tree/main/Value_FULCRA)] [[project](https://valuecompass.github.io/)]
- ⭐ Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, AAAI, 2023, [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] [[preprint](https://arxiv.org/abs/2309.00779)] [[code](https://github.com/tsor13/kaleido)]
- ⭐ What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.789/)]
- ⭐ ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI, 2021, [[paper](https://doi.org/10.1609/aaai.v36i10.21368)] [[paper version](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)] [[paper version](https://ojs.aaai.org/index.php/AAAI/article/view/21368)] [[preprint](https://arxiv.org/abs/2112.06346)] [[dataset](https://liang-qiu.github.io/ValueNet/)]

### 🗺️ Field reviews, reporting, and governance

How is the field organized, documented, and governed?

- ⭐ A roadmap for evaluating moral competence in large language models, Nature, 2026, [[paper](https://nature.com/articles/s41586-025-10021-1)]
- ⭐ A Survey of Progress in LLM Alignment From the Perspective of Reward Design, IEEE Xplore, 2026, [[paper](https://ieeexplore.ieee.org/abstract/document/11361384)]
- 📄 AI Agents Alone Are Not (Yet) Sufficient for Social Simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.00113)]
- 📄 AI Alignment From Social Choice Perspectives, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21550)]
- 📄 Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.07629)]
- ⭐ LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency, Springer journal or proceedings, 2026, [[paper](https://link.springer.com/article/10.1007/s12559-026-10568-9)]
- 📄 Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.03003)]
- 📄 Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.18890)]
- 📄 When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.26348)]
- 📄 A Review of Incorporating Psychological Theories in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.00003)]
- 📄 A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.17003)]
- 📄 A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.07070)]
- 📄 Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.18646)]
- 📄 Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.08858)]
- 📄 Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.16982)]
- ⭐ Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization, Sociological Methods & Research, 2025, [[paper](https://journals.sagepub.com/doi/10.1177/00491241251327130)]
- 📄 Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.00049)]
- 📄 Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.19364)]
- 📄 Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.08245)]
- 📄 LLM Social Simulations Are a Promising Research Method, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.02234)]
- 📄 LLM-Based Social Simulations Require a Boundary, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.19806)]
- ⭐ Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1246/)] [[preprint](https://arxiv.org/abs/2511.01864)] [[code](https://github.com/Indiiigo/LLM_rep_review)]
- 📄 Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.14476)]
- 📄 Simulating Society Requires Simulating Thought, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06958)]
- 📄 The threat of analytic flexibility in using large language models to simulate human data, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.13397)]
- 📄 A Roadmap to Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=gQpBnRHwxM)] [[preprint](https://arxiv.org/abs/2402.05070)] [[code](https://github.com/jfisher52/AI_Pluralistic_Alignment)] [[dataset](https://github.com/jfisher52/AI_Pluralistic_Alignment)] [[dataset](https://drive.google.com/file/d/1MOE4y_nGJiYU_vxCqnWSiYIKCk-dqPJE/view?usp=sharing)] [[dataset](https://huggingface.co/datasets/Anthropic/llm_global_opinions)]
- 📄 A Survey on Evaluation of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2307.03109)] [[code](https://github.com/MLGroupJLU/LLM-eval-survey)]
- 📄 A Survey on Human-Centric LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.14491)]
- 📄 A Survey on Large Language Model based Autonomous Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2308.11432)] [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)]
- 📄 From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.03563)] [[code](https://github.com/FudanDISC/SocialAgent)]
- 📄 Large Language Model based Multi-Agents: A Survey of Progress and Challenges, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.01680)] [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)]
- 📄 LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.05579)]
- 📄 Personalization of Large Language Models: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.00027)]
- 📄 Personalized Multimodal Large Language Models: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.02142)]
- 📄 Position: Towards Bidirectional Human-AI Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.09264)]
- ⭐ Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1192/)]
- 📄 Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10271)]
- ⭐ The benefits, risks and bounds of personalizing the alignment of large language models to individuals, Nature Machine Intelligence, 2024, [[paper](https://nature.com/articles/s42256-024-00820-y)]
- 📄 The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.18682)]
- 📄 The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.16468)]
- ⭐ Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.969/)]
- ⭐ When large language models meet personalization: perspectives of challenges and opportunities, Springer journal or proceedings, 2024, [[paper](https://doi.org/10.1007/s11280-024-01276-1)]
- 📄 AI Alignment and Social Choice: Fundamental Limitations and Policy Implications, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.16048)]
- 📄 AI Alignment: A Comprehensive Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.19852)] [[project](https://alignmentsurvey.com/)]
- 📄 Aligning Large Language Models with Human: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.12966)] [[code](https://github.com/GaryYufei/AlignLLMHumanSurvey)]
- ⭐ Cultural Bias and Cultural Alignment of Large Language Models, PNAS Nexus, 2023, [[paper](https://doi.org/10.1093/pnasnexus/pgae346)] [[preprint](https://arxiv.org/abs/2311.14096)]
- 📄 From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.12014)] [[code](https://github.com/ValueCompass/Alignment-Goal-Survey)]
- ⭐ Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, Humanities and Social Sciences Communications, 2023, [[paper](https://nature.com/articles/s41599-024-03611-3)] [[preprint](https://arxiv.org/abs/2312.11970)]
- 📄 Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.05453)]
- ⭐ Datasheets for Datasets, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3458723)]

## 🧩 Independent resources

These are useful field resources that are not presented as artifacts of a particular paper.

### 🎓 Courses and tutorials (3)

- NeurIPS 2025 Tutorial: Human-AI Alignment, [[course](https://hai-alignment-course.github.io/tutorial/)]
- Stanford 2025: Human-Centered LLMs (CS329X), [[course](https://web.stanford.edu/class/cs329x/)]
- Stanford 2025: Machine Learning from Human Preferences (CS329H), [[course](https://web.stanford.edu/class/cs329h/)]

### 💾 Datasets (4)

- Medical-rlhf 2023-5, [[dataset](https://huggingface.co/datasets/shibing624/medical)]
- OASST1pairwiserlhfreward 2023-5, [[dataset](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)]
- OpenHermesPreferences 2024-3, [[dataset](https://huggingface.co/datasets/argilla/OpenHermesPreferences)]
- Zhihurlhf3k 2023-4, [[dataset](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)]

### 🧪 Dataset and tool repositories (6)

- Alpacacomparisondata 2023-3, [[code](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)]
- github.com, [[code](https://github.com/CLUEbenchmark/CLUEDatasetSearch)]
- huozirlhfdata 2024-2, [[code](https://github.com/HIT-SCIR/huozi)]
- huozirlhfdata 2024-2, [[code](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)]
- Medical-rlhf 2023-5, [[code](https://github.com/shibing624/MedicalGPT)]
- SuperCLUE-Safety 2023-9, [[code](https://github.com/CLUEbenchmark/SuperCLUE-safety)]

### 🧭 Living catalogs (5)

- Awesome-LLM-in-Social-Science, [[catalog](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)]
- Awesome-LLM-Psychometrics, [[catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)]
- awesome-llm-social-simulation, [[catalog](https://github.com/Wanying-He/awesome-llm-social-simulation)]
- Awesome-Personalized-Alignment, [[catalog](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)]
- Awesome-Pluralistic-Alignment, [[catalog](https://github.com/anudeex/Awesome-Pluralistic-Alignment)]

### 🏛️ Policy sources (2)

- A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights, [[policy](https://unesdoc.unesco.org/ark:/48223/pf0000048063)]
- Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449, [[policy](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)]

### 🌐 Project pages (2)

- Concerns on the use of generative AI in social science research, [[project](https://uh-dcm.github.io/genai-concerns/)]
- SuperCLUE-Safety 2023-9, [[project](https://cluebenchmarks.com/superclue_safety.html)]

### 🧰 Software and projects (1)

- Concerns on the use of generative AI in social science research, [[code](https://github.com/uh-dcm/genai-concerns)]

### 📋 Surveys and instruments (8)

- Rokeach value survey. Rokeach et al. The nature of human values. 1967, [[instrument](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)]
- Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002, [[instrument](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)]
- World Values Survey Wave 7 (2017-2022), [[instrument](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)]
- Pew Researcj Center's Global Attitudes Surveys (GAS), [[instrument](https://pewresearch.org/)]
- ESS — European Social Survey, [[instrument](https://europeansocialsurvey.org/data-portal)]
- EVS — European Values Survey, [[instrument](https://europeanvaluesstudy.eu/)]
- GSS — General Social Survey, [[instrument](https://gss.norc.org/)]
- WVS — World Values Survey, [[instrument](https://worldvaluessurvey.org/)]

### 📚 References and books (6)

- Culture's consequences: International differences in work-related values. Hofstede et al. 1984, [[book](https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC)]
- Citizenship and Social Class, [[book](https://books.google.co.kr/books?id=99v4JQAACAAJ)]
- Cultures and organizations: software of the mind, [[book](https://books.google.co.kr/books?id=o4OqTgV3V00C)]
- Social Choice Theory (in Stanford Encyclopedia of Philosophy), [[book](https://plato.stanford.edu/entries/social-choice/)]
- The Righteous Mind, [[book](https://righteousmind.com/)]
- Value Pluralism (in Stanford Encyclopedia of Philosophy), [[book](https://plato.stanford.edu/entries/value-pluralism/)]

### 📄 Additional publications (55)

- (ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis, [[paper](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)]
- (ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis, [[paper](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)]
- (ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL), [[paper](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)]
- (Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL), [[paper](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)]
- (Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate, [[paper](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000429)]
- (Others & custom) Improving GPT Generated Synthetic Samples with Sampling-Permutation Algorithm, 2023.08, [[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4548937)]
- (Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science, [[paper](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)]
- An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012, [[paper](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)]
- Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022, [[paper](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)]
- A review of automatic item generation techniques leveraging large language models, 2025.06, [[paper](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)]
- A Systematic Survey of Cultural Datasets for Equitable LLM Alignment, [[paper](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)]
- A theory of justice, [[paper](https://jstor.org/stable/j.ctvjf9z6v)]
- A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism, [[paper](http://jstor.org/stable/24707060)]
- Aggregating Sets of Judgments: An Impossibility Result, [[paper](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)]
- An Overview of the Schwartz Theory of Basic Values, [[paper](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)]
- Basic human values: Theory, measurement, and applications, [[paper](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)]
- Can Generative AI improve social science?, 2024.05, PNAS, [[paper](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)]
- Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023, [[paper](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)]
- Collective Choice and Social Welfare, [[paper](https://jstor.org/stable/j.ctv2sp3dqx)]
- Conflicts of Values (in Moral Luck), [[paper](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)]
- Creating Capabilities: The Human Development Approach and Its Implementation, [[paper](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)]
- Cultural Value Orientations, [[paper](https://researchgate.net/publication/265997557)]
- Culture's consequences: International differences in work-related values, [[paper](https://philpapers.org/rec/HOFCCI-2)]
- Exploring Universal Human Values with Large Language Models: The AWARE-Value Model, [[paper](https://researchsquare.com/article/rs-8188052/v1)]
- Functional theory of human values, [[paper](https://researchgate.net/publication/259486885)]
- Handbook of Computational Social Choice, [[paper](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)]
- If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task, [[paper](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)]
- Kush R. Varshney. XRDS 2019, [[paper](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)]
- Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice, [[paper](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)]
- Liberals and conservatives rely on different sets of moral foundations, [[paper](https://pubmed.ncbi.nlm.nih.gov/19379034/)]
- Manipulation of Voting Schemes: A General Result, [[paper](https://jstor.org/stable/1914083)]
- Mapping and interpreting cultural differences around the world, [[paper](https://researchgate.net/publication/265596552)]
- Measuring Perceived Slant in Large Language Models Through User Evaluations, [[paper](https://modelslant.com/paper.pdf)]
- Measuring the Refined Theory of Individual Values in 49 Cultural Groups, [[paper](https://researchgate.net/publication/349058866)]
- Mental representations of social values, [[paper](https://psycnet.apa.org/record/2012-14612-001)]
- Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies, [[paper](https://jstor.org/stable/j.ctv10vm2ns)]
- Modernization, Cultural Change, and Democracy, [[paper](https://researchgate.net/publication/230557603)]
- On the Rationale of Group Decision-making, [[paper](https://jstor.org/stable/1825026)]
- Perils and opportunities in using large language models in psychological research, 2024.07, [[paper](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)]
- Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science, [[paper](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)]
- Refining the theory of basic individual values, [[paper](https://pubmed.ncbi.nlm.nih.gov/22823292/)]
- Robustness of large language models in moral judgements, [[paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)]
- Social Choice and Individual Values, [[paper](https://jstor.org/stable/j.ctt1nqb90)]
- Steerable Alignment with Conditional Multiobjective Preference Optimization, [[paper](https://dspace.mit.edu/handle/1721.1/156747)]
- The Impossibility of a Paretian Liberal, [[paper](https://jstor.org/stable/1829633)]
- The Morality of Freedom, [[paper](https://academic.oup.com/book/9926)]
- The Morality of Pluralism, [[paper](https://jstor.org/stable/j.ctt7smh7)]
- The Morals of Modernity, [[paper](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)]
- The nature of human values, [[paper](https://psycnet.apa.org/record/2011-15663-000)]
- The Right and the Good, [[paper](https://academic.oup.com/book/27608)]
- The Theory of Communicative Action, [[paper](https://philpapers.org/rec/HABTTO)]
- The theory of dyadic morality: Reinventing moral judgment by redefining harm, [[paper](https://psycnet.apa.org/record/2018-02142-002)]
- Towards Pluralistic Alignment of LLMs: A Comprehensive Survey, [[paper](https://preprints.org/manuscript/202603.1876)]
- Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop, [[paper](https://openaccess.city.ac.uk/id/eprint/31381/)]
- Two Concepts of Liberty, [[paper](https://academic.oup.com/book/7968/chapter-abstract/153281672)]

### 🔗 Web resources (2)

- Kush R. Varshney. XRDS 2019, [[reference](https://krvarshney.github.io/)]
- lit.eecs.umich.edu, [[reference](https://lit.eecs.umich.edu/downloads.html)]

## 🤝 Contributing

Open an issue or pull request to add a work, correct a domain assignment, supply a missing artifact, or improve the taxonomy with concrete evidence.
