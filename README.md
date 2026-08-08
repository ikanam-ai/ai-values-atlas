<div align="center">

<img src="assets/atlas-header.svg" width="100%" alt="AI Values Atlas — open research field guide" />

<h1>AI Values Atlas</h1>

<p><strong>A field guide to how values are represented, elicited, expressed, chosen, and evaluated in AI systems.</strong></p>

<p>
  <a href="https://ikanam-ai.github.io/ai-values-atlas/">Explore the atlas</a> ·
  <a href="#field-map">Field map</a> ·
  <a href="#literature-by-research-question">Literature</a> ·
  <a href="#axiologies-and-value-spaces">Axiologies</a> ·
  <a href="#datasets-benchmarks-and-instruments">Datasets & benchmarks</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p>
  <a href="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml"><img alt="validation" src="https://img.shields.io/github/actions/workflow/status/ikanam-ai/ai-values-atlas/validate.yml?style=for-the-badge&label=validated"></a>
  <a href="#complete-catalog"><img alt="resources" src="https://img.shields.io/badge/resources-1013-136f58?style=for-the-badge"></a>
  <a href="#complete-catalog"><img alt="publications" src="https://img.shields.io/badge/publication%20links-787-0d3f35?style=for-the-badge"></a>
  <a href="CONTRIBUTING.md"><img alt="pull requests welcome" src="https://img.shields.io/badge/PRs-welcome-e9b44c?style=for-the-badge"></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/metadata-CC%20BY%204.0-7665d8?style=for-the-badge"></a>
</p>

</div>

| [🧭 **Field map**](#field-map) | [📚 **Literature**](#literature-by-research-question) | [🧠 **Axiologies**](#axiologies-and-value-spaces) | [💾 **Datasets**](#datasets-benchmarks-and-instruments) | [🧰 **Models & tools**](#models-scorers-and-representation-tools) |
|:---:|:---:|:---:|:---:|:---:|

AI Values Atlas is an open map of research on values in language models and
other AI systems. It connects theories, papers, benchmarks, datasets,
questionnaires, scenarios, scorers, representation models, and validation
evidence without pretending that they measure the same thing.

> **The central rule:** a value framework is not an instrument; an instrument
> is not a scorer; endorsement is not choice; generated text is not behavior;
> and a reliable profile is not automatically a valid or model-specific one.

Browse all 1018 resources on the [interactive atlas](https://ikanam-ai.github.io/ai-values-atlas/),
or start with the curated reading list below.

## 📚 Contents

- [🧭 Field map](#field-map)
  - [🧠 Axiologies and value spaces](#axiologies-and-value-spaces)
- [📖 Literature by research question](#literature-by-research-question)
- [💾 Datasets, benchmarks, and instruments](#datasets-benchmarks-and-instruments)
- [🧰 Models, scorers, and representation tools](#models-scorers-and-representation-tools)
- [📚 Complete catalog](#complete-catalog)
- [🤝 Contributing](#contributing)

## 🧭 Field map

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

### 🧠 Axiologies and value spaces

An axiology describes which values exist and how they relate. It can be a named
theory, a survey space, an ontology, an induced factor system, a latent
representation, or a set of alignment principles. It is not the questionnaire,
prompt, scorer, or benchmark used to measure it.

| Axiology or value space | Dimensions and named structure | Typical use in AI research |
|---|---|---|
| [Schwartz Theory of Basic Human Values](https://doi.org/10.1016/S0065-2601(08)60281-6) | **10 values:** Self-Direction, Stimulation, Hedonism, Achievement, Power, Security, Conformity, Tradition, Benevolence, Universalism; **4 higher-order groups:** Openness to Change, Conservation, Self-Enhancement, Self-Transcendence | questionnaires, scenario mapping, generated-text scoring, value conflict |
| [Refined Schwartz Theory](https://doi.org/10.1037/a0029393) | **19 values:** Self-Direction–Thought, Self-Direction–Action, Stimulation, Hedonism, Achievement, Power–Dominance, Power–Resources, Face, Security–Personal, Security–Societal, Tradition, Conformity–Rules, Conformity–Interpersonal, Humility, Benevolence–Dependability, Benevolence–Caring, Universalism–Concern, Universalism–Nature, Universalism–Tolerance | higher-granularity human and AI profiling |
| [Moral Foundations Theory](https://doi.org/10.1037/a0015141) | **6 foundations:** Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, Liberty/Oppression; the original formulation used the first **5** | moral-language classification and model profiling |
| [World Values Survey](https://www.worldvaluessurvey.org/) | Wave-specific multilingual item bank, **no fixed dimension count**; **7 completed waves** since 1981, almost **120 countries/societies**, and **300+ indicators** in Wave 7 | human–AI comparison, cultural and political attitudes |
| [Inglehart–Welzel Cultural Map](https://www.worldvaluessurvey.org/WVSContents.jsp) | **2 dimensions:** Traditional ↔ Secular-Rational, Survival ↔ Self-Expression | country and culture-level comparison |
| [Hofstede cultural dimensions](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/) | **6 dimensions:** Power Distance, Individualism, Masculinity, Uncertainty Avoidance, Long-Term Orientation, Indulgence | cultural alignment and language/persona audits |
| [GLOBE cultural dimensions](https://globeproject.com/study_2004_2007) | **9 dimensions:** Performance Orientation, Assertiveness, Future Orientation, Humane Orientation, Institutional Collectivism, In-Group Collectivism, Gender Egalitarianism, Power Distance, Uncertainty Avoidance | cross-cultural model evaluation |
| [Rokeach Value System](https://psycnet.apa.org/record/2011-15663-000) | **18 terminal values:** A Comfortable Life, An Exciting Life, A Sense of Accomplishment, A World at Peace, A World of Beauty, Equality, Family Security, Freedom, Happiness, Inner Harmony, Mature Love, National Security, Pleasure, Salvation, Self-Respect, Social Recognition, True Friendship, Wisdom; **18 instrumental values:** Ambitious, Broad-Minded, Capable, Cheerful, Clean, Courageous, Forgiving, Helpful, Honest, Imaginative, Independent, Intellectual, Logical, Loving, Obedient, Polite, Responsible, Self-Controlled | ranked value priorities |
| [Social Value Orientation](https://doi.org/10.1002/ejsp.1773) | **1 allocation-preference continuum**, from competitive/individualistic to prosocial/altruistic; the common Slider Measure uses **6 primary items** | social decisions and behavioral games |
| [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) | **3 entity types:** values, rights, duties; an open ontology rather than a fixed-dimensional profile | pluralistic reasoning and conflict-aware alignment |
| [GPLA](https://aclanthology.org/2025.acl-long.585/) | **123 atomic values** induce **5 factors:** Social Responsibility, Risk-Taking, Rule-Following, Self-Competence, Rationality | AI-native value-system construction |
| [UniVaR](https://aclanthology.org/2025.naacl-long.274/) | Continuous latent representation with **no named value axes**; learned from **8 LLMs** and evaluated on **15 models** across **25 languages/cultures** | model–language value embeddings and comparison |
| [Generative Psychometrics](https://doi.org/10.1609/aaai.v39i25.34839) | Values are supplied at measurement time, so there is **no fixed dimension count**; outputs can later be aggregated into Schwartz, Hofstede, or another named space | free-response perception extraction and value scoring |
| [Functional Theory of Human Values](https://doi.org/10.1016/j.paid.2013.07.043) | **18 marker values** in **6 subfunctions:** Excitement (Emotion, Pleasure, Sexuality), Promotion (Power, Prestige, Success), Existence (Personal Stability, Health, Survival), Suprapersonal (Beauty, Knowledge, Maturity), Interactive (Affectivity, Belonging, Social Support), Normative (Obedience, Religiosity, Tradition) | profiling with an alternative named human-value theory |
| [Helpful, Honest, and Harmless](https://arxiv.org/abs/2112.00861) | **3 principles:** Helpful, Honest, Harmless | assistant behavior and preference modeling |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | Configurable natural-language constitution, **no fixed principle count or universal dimensions** | critique, revision, and alignment targets |

## 📖 Literature by research question

### 🗺️ Surveys and field overviews

- (Psychometrics) A Systematic Review of Psychometric Evaluation of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.08245)] [[catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)]
- (Values and attitudes) Large Language Models as Mirrors of Human Attitudes, Opinions, and Values, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.513/)]
- (Human values) Human Values and Alignment in Artificial Intelligence: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10636)]

#### 🔗 Related living catalogs

- (Values and pluralism) Awesome LLM Values and Pluralistic Alignment, GitHub, continuously updated, [[catalog](https://github.com/AIDASLab/Awesome-LLM-Values-and-Pluralistic-Alignment)]
- (Psychometrics) Awesome LLM Psychometrics, GitHub, continuously updated, [[catalog](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)]
- (Pluralistic alignment) Towards Pluralistic Alignment of LLMs: A Comprehensive Survey, GitHub, continuously updated, [[catalog](https://github.com/anudeex/Awesome-Pluralistic-Alignment)]
- (Alignment targets) Alignment Goal Survey, GitHub, continuously updated, [[catalog](https://github.com/ValueCompass/Alignment-Goal-Survey)]

### 📋 Questionnaires and elicited profiles

- (Schwartz / HEXACO) Who is GPT-3? An Exploration of Personality, Values and Demographics, NLP+CSS at EMNLP, 2022, [[paper](https://aclanthology.org/2022.nlpcss-1.24/)]
- (Schwartz) Stick to Your Role! Stability of Personal Values Expressed in Large Language Models, PLOS ONE, 2024, [[paper](https://doi.org/10.1371/journal.pone.0309114)]
- (Schwartz) Do LLMs Have Consistent Values?, ICLR, 2025, [[paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)]
- (Survey instruments) On the Credibility of Evaluating LLMs Using Survey Questions, MME, 2026, [[paper](https://aclanthology.org/2026.mme-main.2/)]
- (Schwartz) Assessing the Alignment of LLMs With Human Values for Mental Health Integration, JMIR Mental Health, 2024, [[paper](https://doi.org/10.2196/55988)]
- (Schwartz) Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.838/)]
- (Adaptive measurement) Raising the Bar: Investigating the Values of LLMs via Generative Evolving Testing, OpenReview, 2025, [[paper](https://openreview.net/forum?id=0REM9ydeLZ)]
- (Adaptive measurement) AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference, OpenReview, 2026, [[paper](https://openreview.net/forum?id=qNlTH4kYJZ)]
- (Schwartz) Cultural Value Alignment in LLMs: A Prompt-based Analysis of Schwartz Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17112)]

### 🧪 Value understanding and benchmark tasks

- (ETHICS) Aligning AI With Shared Human Values, ICLR, 2021, [[paper](https://openreview.net/forum?id=dNy_RKzJacY)] [[code](https://github.com/hendrycks/ethics)]
- (Social norms) Social Chemistry 101, EMNLP, 2020, [[paper](https://aclanthology.org/2020.emnlp-main.48/)] [[dataset](https://maxwellforbes.com/social-chemistry/)]
- (Social norms) Moral Stories, EMNLP, 2021, [[paper](https://aclanthology.org/2021.emnlp-main.54/)] [[code](https://github.com/demelin/moral_stories)]
- (Delphi) Can Machines Learn Morality? The Delphi Experiment, arXiv, 2021, [[paper](https://arxiv.org/abs/2110.07574)] [[project](https://delphi.allenai.org/)]
- (Schwartz) ValueNet, AAAI, 2022, [[paper](https://doi.org/10.1609/aaai.v36i10.21368)] [[dataset](https://liang-qiu.github.io/ValueNet/)]
- (ValueEval) The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments, SemEval, 2023, [[paper](https://aclanthology.org/2023.semeval-1.313/)]
- (Multiple instruments) ValueBench, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.111/)] [[code](https://github.com/Value4AI/ValueBench)]
- (Cultural values) WorldValuesBench, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1539/)]
- (Generative / pluralistic) Value Compass Benchmarks, ACL Demo, 2025, [[paper](https://aclanthology.org/2025.acl-demo.64/)]
- (Moral values) Structured Moral Reasoning in Language Models, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1541/)]
- (Schwartz) The Staircase of Ethics, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.806/)]

### ✍️ Values in generated text

- (Schwartz) Value FULCRA, NAACL, 2024, [[paper](https://aclanthology.org/2024.naacl-long.486/)]
- (GPV / supplied values) Measuring Human and AI Values Based on Generative Psychometrics, AAAI, 2025, [[paper](https://doi.org/10.1609/aaai.v39i25.34839)] [[code](https://github.com/Value4AI/gpv)] [[model](https://huggingface.co/Value4AI/ValueLlama-3-8B)]
- (Adaptive values) CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.10725)]
- (Values, rights, and duties) Value Kaleidoscope, AAAI, 2024, [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] [[code](https://github.com/tsor13/kaleido)]
- (MFT) MoralBERT, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.07678)] [[code](https://github.com/vjosapreniqi/MoralBERT)]
- (Schwartz) ValueNet, AAAI, 2022, [[paper](https://doi.org/10.1609/aaai.v36i10.21368)] [[dataset](https://liang-qiu.github.io/ValueNet/)]

### ⚖️ Choice, action, and cross-interface gaps

- (Schwartz / INVP) What's the Most Important Value? INVP, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.317/)]
- (Value–action gap) Mind the Value–Action Gap: Do LLMs Act in Alignment with Their Values?, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.154/)]
- (Schwartz / ValueCompass) ValueCompass: Measuring Contextual Value Alignment Between Human and LLMs, WiNLP, 2025, [[paper](https://aclanthology.org/2025.winlp-main.15/)]
- (Structural values) Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1188/)]
- (Behavioral theory) The Theory of Planned Behavior, Organizational Behavior and Human Decision Processes, 1991, [[paper](https://www.sciencedirect.com/science/article/pii/074959789190020T)]
- (Value–belief–norm theory) A Value–Belief–Norm Theory of Support for Social Movements, Human Ecology Review, 1999, [[paper](http://www.jstor.org/stable/24707060)]

### 🌍 Culture, language, and pluralism

- (Cross-lingual morality) Ethical Reasoning and Moral Value Alignment Depend on the Language We Prompt In, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.18460)]
- (Cultural alignment) Cultural Bias and Cultural Alignment of Large Language Models, PNAS Nexus, 2024, [[paper](https://doi.org/10.1093/pnasnexus/pgae346)]
- (Cultural alignment) Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.2/)]
- (Cultural values) WorldValuesBench, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1539/)]
- (Values, rights, and duties) Value Kaleidoscope, AAAI, 2024, [[paper](https://doi.org/10.1609/aaai.v38i18.29970)] [[code](https://github.com/tsor13/kaleido)]
- (Political pluralism) Aligning Large Language Models with Diverse Political Viewpoints, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.412/)]
- (MFT) Moral Foundations of Large Language Models, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.982/)]
- (Cultural NLP) Awesome Cultural NLP, GitHub, continuously updated, [[catalog](https://github.com/simran-khanuja/awesome-cultural-nlp)]
- (Personalized alignment) Awesome Personalized Alignment, GitHub, continuously updated, [[catalog](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)]

### 🧠 Representations, internals, and steering

- (GPLA) Generative Psycho-Lexical Approach for Constructing Value Systems in LLMs, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.585/)]
- (UniVaR) High-Dimension Human Value Representation in LLMs, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.274/)] [[code](https://github.com/HLTCHKUST/UniVaR)] [[model](https://huggingface.co/CAiRE/UniVaR-lambda-1)]
- (Value vectors) Internal Value Alignment through Controlled Value Vector Activation, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1326/)]
- (Value neurons) Understanding How Value Neurons Shape the Generation of Specified Values, Findings of EMNLP, 2025, [[paper](https://aclanthology.org/2025.findings-emnlp.501/)]
- (Principle sets) Towards Better Value Principles for LLM Alignment, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1408/)]
- (Value alignment) Unintended Harms of Value-Aligned LLMs, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1532/)]
- (Constitutional AI) Constitutional AI: Harmlessness from AI Feedback, arXiv, 2022, [[paper](https://arxiv.org/abs/2212.08073)] [[code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)]

### 🔬 Reliability, validity, and reporting

- (Measurement theory) Measurement and Fairness, FAccT, 2021, [[paper](https://doi.org/10.1145/3442188.3445901)]
- (Prompt sensitivity) POSIX: A Prompt Sensitivity Index for Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02185)]
- (Survey validity) On the Credibility of Evaluating LLMs Using Survey Questions, MME, 2026, [[paper](https://aclanthology.org/2026.mme-main.2/)]
- (Evaluator bias) Large Language Models Are Not Fair Evaluators, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.511/)]
- (Evaluation design) AI Evaluation Should Learn from How We Test Humans, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.10512)]
- (Holistic evaluation) Holistic Evaluation of Language Models, TMLR, 2023, [[paper](https://openreview.net/forum?id=iO4LZibEqW)]
- (Reporting) Model Cards for Model Reporting, FAT*, 2019, [[paper](https://doi.org/10.1145/3287560.3287596)]
- (Dataset documentation) Datasheets for Datasets, Communications of the ACM, 2021, [[paper](https://doi.org/10.1145/3458723)]
- (Dataset documentation) Data Statements for NLP, TACL, 2018, [[paper](https://aclanthology.org/Q18-1041/)]
- (Internal auditing) Closing the AI Accountability Gap, FAT*, 2020, [[paper](https://doi.org/10.1145/3351095.3372873)]

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

| Tool | Scale and construction | Exact output | Links |
|---|---|---|---|
| ValueLlama-3-8B | **8B-parameter** Llama-3 model fine-tuned on ValueBench and ValuePrism; English | **2 tasks:** binary relevance, then **3-way valence** (supports / opposes / neutral-context-dependent) for any supplied value | [[model](https://huggingface.co/Value4AI/ValueLlama-3-8B)] [[code](https://github.com/Value4AI/gpv)] |
| UniVaR lambda-1 | **137M-parameter** Nomic-BERT encoder; trained contrastively from value-eliciting QA sets produced by **8 source LLMs** | one dense model–language embedding with **no named value coordinates**; paper evaluates **15 models × 25 languages/cultures** | [[model](https://huggingface.co/CAiRE/UniVaR-lambda-1)] [[code](https://github.com/HLTCHKUST/UniVaR)] |
| MoralBERT | BERT-family classifiers fine-tuned on Twitter, Reddit, and Facebook corpora | **10 separate binary classifiers** for virtue/vice poles of the original **5 MFT foundations**; Liberty/Oppression weights are not released | [[code](https://github.com/vjosapreniqi/MoralBERT)] |
| Kaleido | **5 released model sizes:** small, base, large, XL, XXL; trained from **218k** ValuePrism records | candidate generation, explanation, binary relevance, and **3-way valence** over value / right / duty entities | [[code](https://github.com/tsor13/kaleido)] |
| FULCRA / BaseAlign | pipeline trained on **20k output–vector pairs** | a **10-dimensional** Schwartz profile plus **58 item-level** priorities for generated text | [[paper](https://aclanthology.org/2024.naacl-long.486/)] |
| CLAVE | two-model evaluator calibrated with **<100 human labels per value type**; evaluated on **13k+ tuples**, **3 value systems**, and **12+ evaluators** | adaptable reference-free label for a supplied value definition | [[paper](https://arxiv.org/abs/2407.10725)] |

## 📚 Complete catalog

The catalog below contains every unique URL in the repository. Publications are
grouped by research topic; datasets, models, repositories, projects, and survey
resources have dedicated sections. All entries are visible and searchable
directly on GitHub.

<!-- complete-catalog:start -->

Every resource appears once. Parenthetical tags are shown only when a source
identifies a concrete framework, instrument, or subdomain.

**Browse the taxonomy**

| Research area | Publications |
|---|---:|
| [🗺️ Surveys, reviews, and field overviews](#catalog-surveys-reviews-and-field-overviews) | 49 |
| [🧭 Foundations and value theory](#catalog-foundations-and-value-theory) | 7 |
| [🗂️ Datasets and benchmarks](#catalog-datasets-and-benchmarks) | 104 |
| [🔬 Reliability, validity, and auditing](#catalog-reliability-validity-and-auditing) | 17 |
| [🎯 Choice, action, and behavioral consistency](#catalog-choice-action-and-behavioral-consistency) | 15 |
| [🌍 Culture, language, and pluralism](#catalog-culture-language-and-pluralism) | 103 |
| [🗣️ Preferences, opinions, and social simulation](#catalog-preferences-opinions-and-social-simulation) | 121 |
| [⚖️ Moral reasoning and value understanding](#catalog-moral-reasoning-and-value-understanding) | 63 |
| [🧰 Alignment, steering, and preferences](#catalog-alignment-steering-and-preferences) | 133 |
| [📐 Value representation and model internals](#catalog-value-representation-and-model-internals) | 44 |
| [📏 Measurement and profiling](#catalog-measurement-and-profiling) | 87 |
| [📎 Other and adjacent value research](#catalog-other-and-adjacent-value-research) | 44 |

### 📚 Publications by topic

<a id="catalog-surveys-reviews-and-field-overviews"></a>

#### 🗺️ Surveys, reviews, and field overviews (49)

- A roadmap for evaluating moral competence in large language models, Nature, 2026, [[paper](https://nature.com/articles/s41586-025-10021-1)]
- A Survey of Progress in LLM Alignment from the Perspective of Reward Design, IEEE Xplore, 2026, [[paper](https://ieeexplore.ieee.org/abstract/document/11361384)]
- A Survey on Evaluation of Large Language Models, arXiv, 2023.07, [[paper](https://arxiv.org/abs/2307.03109)] [[code](https://github.com/MLGroupJLU/LLM-eval-survey)]
- A Survey on Human-Centric LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.14491)]
- A Survey on Large Language Model based Autonomous Agents, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.11432)] [[code](https://github.com/Paitesanshi/LLM-Agent-Survey)]
- A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.17003)]
- A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.07070)]
- AI Alignment and Social Choice: Fundamental Limitations and Policy Implications, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.16048)]
- AI Alignment From Social Choice Perspectives, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21550)]
- AI Alignment: A Comprehensive Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.19852)] [[project](https://alignmentsurvey.com/)]
- Aligning Large Language Models with Human: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.12966)] [[code](https://github.com/GaryYufei/AlignLLMHumanSurvey)]
- Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.18646)]
- Cultural Bias and Cultural Alignment of Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.14096)]
- Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.08858)]
- Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.16982)]
- From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.03563)] [[code](https://github.com/FudanDISC/SocialAgent)]
- From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.12014)] [[code](https://github.com/ValueCompass/Alignment-Goal-Survey)]
- Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications, arXiv, 2025.04, [[paper](https://arxiv.org/abs/2505.00049)]
- Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.19364)]
- Large Language Model based Multi-Agents: A Survey of Progress and Challenges, arXiv, 2024.01, [[paper](https://arxiv.org/abs/2402.01680)] [[code](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)]
- Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.08245)]
- Large language models empowered agent-based modeling and simulation: a survey and perspectives, Humanities and Social Sciences Communications, 2024, [[paper](https://nature.com/articles/s41599-024-03611-3)]
- Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.07629)]
- LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency, Springer journal or proceedings, 2026, [[paper](https://link.springer.com/article/10.1007/s12559-026-10568-9)]
- LLM Social Simulations Are a Promising Research Method, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.02234)]
- LLM-Based Social Simulations Require a Boundary, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.19806)]
- LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.05579)]
- Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1246/)] [[code](https://github.com/Indiiigo/LLM_rep_review)]
- Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.01864)]
- Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.03003)]
- Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.14476)]
- Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.05453)]
- Personalization of Large Language Models: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.00027)]
- Personalized Multimodal Large Language Models: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.02142)]
- Position: A Roadmap to Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=gQpBnRHwxM)]
- Position: AI Agents Are Not (Yet) a Panacea for Social Simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.00113)]
- Position: Towards Bidirectional Human-AI Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.09264)]
- Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1192/)]
- Simulating Society Requires Simulating Thought, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06958)]
- Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10271)]
- Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.18890)]
- The benefits, risks and bounds of personalizing the alignment of large language models to individuals, Nature Machine Intelligence, 2024, [[paper](https://nature.com/articles/s42256-024-00820-y)]
- The Mind in the Machine: A Survey of Incorporating Psychological Theories in LLMs, arXiv, 2025.05, [[paper](https://arxiv.org/abs/2505.00003)]
- The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.18682)]
- The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.16468)]
- The threat of analytic flexibility in using large language models to simulate human data: A call to attention, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.13397)]
- Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents, arXiv, 2025.03, [[paper](https://arxiv.org/abs/2503.24047)]
- Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.969/)]
- When large language models meet personalization: perspectives of challenges and opportunities, Springer journal or proceedings, 2024, [[paper](https://doi.org/10.1007/s11280-024-01276-1)]

<a id="catalog-foundations-and-value-theory"></a>

#### 🧭 Foundations and value theory (7)

- Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values, JMIR, 2024, [[paper](https://doi.org/10.2196/55988)] [[link](https://mental.jmir.org/2024/1/e55988)]
- Axioms for AI Alignment from Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.14758)]
- Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement, SAGE journal, 2001, [[paper](https://doi.org/10.1177/0022022101032005001)]
- Moral foundations theory: The pragmatic validity of moral pluralism. Graham et al. Advances in experimental social psychology, 2013., Elsevier journal or book, 2013, [[paper](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)]
- Optimized Distortion in Linear Social Choice, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.20020)]
- Representative Social Choice: From Learning Theory to AI Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.23953)]
- Strategy-proofness and Arrow's Conditions, Elsevier journal or book, 1975, [[paper](https://sciencedirect.com/science/article/pii/0022053175900502)]

<a id="catalog-datasets-and-benchmarks"></a>

#### 🗂️ Datasets and benchmarks (104)

- (ETHICS) Aligning AI With Shared Human Values, arXiv, 2020, [[paper](https://arxiv.org/abs/2008.02275)] [[code](https://github.com/hendrycks/ethics)]
- (MoralChoice) Evaluating the Moral Beliefs Encoded in LLMs, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.14324)]
- (NYTBookOpinions) Benchmarking Distributional Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.05403)]
- (Valueeval) The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.13771)]
- A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values, OpenReview, 2025, [[paper](https://openreview.net/forum?id=oSRqZO2O2O)]
- A Unified Moral-Value Dataset for Instruction Tuning, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.21279)]
- Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.13300)]
- Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.10365)]
- An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.01247)] [[code](https://github.com/simran-khanuja/image-transcreation)]
- Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.14083)]
- Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models, NeurIPS, 2024, [[paper](https://arxiv.org/abs/2402.11894)]
- BBQ: A hand-built bias benchmark for question answering, Findings of ACL, 2022, [[paper](https://aclanthology.org/2022.findings-acl.165/)]
- Benchmarking Distributional Alignment of Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.2/)]
- Benchmarking Multi-National Value Alignment for Large Language Models, arXiv, 2025.04, [[paper](https://arxiv.org/abs/2504.12911)]
- Benchmarking Overton Pluralism in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.01351)]
- Beyond Aesthetics: Cultural Competence in Text-to-Image Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.06863)] [[code](https://github.com/google-research-datasets/cube)]
- Big-Math 2025-2, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.17387)] [[dataset](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified)] [[code](https://github.com/SynthLabsAI/big-math)]
- Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys, arXiv, 2024, [[paper](https://arxiv.org/abs/2401.10352)] [[code](https://github.com/yongcaoplus/cuDialog)]
- C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.01495)]
- Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05154)]
- Can Language Models Reason about Individualistic Human Values and Preferences?, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.336/)]
- CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.13974)]
- CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31710)]
- CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.10823)]
- CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.06412)] [[code](https://github.com/rladmstn1714/CLIcK)]
- COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values, arXiv, 2025.04, [[paper](https://arxiv.org/abs/2504.05535)]
- ComPO: Community Preferences for Language Model Personalization, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.419/)]
- Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM, 2024, [[paper](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768)] [[dataset](https://mango.mpi-inf.mpg.de/)]
- Culturally Aware Natural Language Inference, Findings of EMNLP, 2023, [[paper](https://aclanthology.org/2023.findings-emnlp.509/)] [[code](https://github.com/SALT-NLP/CulturallyAwareNLI)]
- D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.19834)]
- Datasheets for datasets, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3458723)]
- DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.17399)] [[dataset](https://huggingface.co/datasets/nlip/DIWALI)] [[project](https://nlip-lab.github.io/nlip/publications/diwali/)] [[code](https://github.com/pramitsahoo/culture-evaluation)]
- DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.14651)] [[code](https://github.com/microsoft/DOSA)]
- EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.14498)]
- Evaluating and Inducing Personality in Pre-trained Language Models, arXiv, 2022, [[paper](https://arxiv.org/abs/2206.07550)]
- Evaluating the Prompt Steerability of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.12405)]
- EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.06370)]
- Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.17838)]
- Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis, arXiv, 2024, [[paper](https://arxiv.org/abs/2308.16705)] [[code](https://github.com/nlee0212/CREHate)]
- FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.1063/)] [[dataset](https://huggingface.co/datasets/lyan62/FoodieQA)] [[code](https://github.com/lyan62/FoodieQA)]
- FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models, Findings of ACL, 2023, [[paper](https://aclanthology.org/2023.findings-acl.631/)] [[code](https://github.com/shramay-palta/FORK_ACL2023)]
- GeoDE: a Geographically Diverse Evaluation Dataset for Object Recognition, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.02560)] [[link](https://geodiverse-data-collection.cs.princeton.edu/)]
- GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.13766)] [[model](https://huggingface.co/floschne)] [[code](https://github.com/floschne/gimmick)]
- Global Voices, Local Biases: Socio-Cultural Prejudices across Languages, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.17586)] [[code](https://github.com/iamshnoo/weathub)]
- HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter, ACL Outstanding Paper, 2025, [[paper](https://arxiv.org/abs/2411.15462)]
- HelpSteer 2: Open-source dataset for training top-performing reward models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)]
- KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge, Findings of ACL, 2024, [[paper](https://aclanthology.org/2024.findings-acl.666/)]
- LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.01894)]
- LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.00853)]
- M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.03791)] [[code](https://github.com/floschne/m5b)]
- Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.09369)] [[code](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)]
- MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.19073)]
- MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces, OpenReview, 2024, [[paper](https://openreview.net/forum?id=kyfkMRT4Ao)]
- Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment, SAGE journal, 2020, [[paper](https://journals.sagepub.com/doi/10.1177/1948550619876629)]
- Moral foundations twitter corpus: A collection of 35k tweets annotated for moral sentiment. Hoover et al. Social Psychological and Personality Science 2020., SAGE journal, 2020, [[paper](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)]
- Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences, arXiv, 2020, [[paper](https://arxiv.org/abs/2012.15738)] [[code](https://github.com/demelin/moral_stories)]
- MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.16380)]
- Multi-lingual and Multi-cultural Figurative Language Understanding, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.16171)] [[code](https://github.com/simran-khanuja/Multilingual-Fig-QA)]
- Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision-Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.490/)] [[dataset](https://huggingface.co/datasets/MinhDucBui/Multi3Hate)] [[code](https://github.com/MinhDucBui/Multi3Hate)]
- Navigating the Cultural Kaleidoscope: A Hitchhiker’s Guide to Sensitivity in Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.388/)]
- NLPositionality: Characterizing Design Biases of Datasets and Models, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.505/)] [[project](https://nlpositionality.cs.washington.edu/)]
- NormBank: A Knowledge Bank of Situational Social Norms, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.429/)]
- NormBank: A Knowledge Bank of Situational Social Norms, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.17008)]
- NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly, arXiv, 2023, [[paper](https://arxiv.org/abs/2210.08604)] [[code](https://github.com/yrf1/NormSage)]
- NoveltyBench: Evaluating Language Models for Humanlike Diversity, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.05228)]
- PerSpectra: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08716)]
- PLURAL: A Global Dataset for Value Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.08034)]
- PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.08951)]
- Polar: A Benchmark for Evaluating Political Bias in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12922)]
- Process for adapting language models to society (palms) with values-targeted datasets. Solaiman et al. Neurips 2021., NeurIPS, 2021, [[paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)]
- ProsocialDialog: A Prosocial Backbone for Conversational Agents, arXiv, 2022, [[paper](https://arxiv.org/abs/2205.12688)]
- Re-contextualizing Fairness in NLP: The Case of India, arXiv, 2022, [[paper](https://arxiv.org/abs/2209.12226)] [[code](https://github.com/google-research-datasets/nlp-fairness-for-india)]
- RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations, Findings of NAACL, 2024, [[paper](https://aclanthology.org/2024.findings-naacl.196/)] [[code](https://github.com/zhanhl316/ReNoVi)]
- SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022., arXiv, 2022, [[paper](https://arxiv.org/abs/2210.10045)] [[code](https://github.com/sharonlevy/SafeText)]
- SafeWorld: Geo-Diverse Safety Alignment, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)]
- Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes, arXiv, 2020, [[paper](https://arxiv.org/abs/2008.09094)]
- Scruples: A corpus of community ethical judgments on 32, 000 real-life anecdotes. Lourie et al. AAAI., 2021, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396)] [[code](https://github.com/allenai/scruples)]
- SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.11840)] [[code](https://github.com/google-research-datasets/seegull)]
- Social Chemistry 101: Learning to Reason about Social and Moral Norms, arXiv, 2020, [[paper](https://arxiv.org/abs/2011.00620)] [[link](https://maxwellforbes.com/social-chemistry/)]
- SocialDial: A Benchmark for Socially-Aware Dialogue Systems, ACM Digital Library, 2023, [[paper](https://dl.acm.org/doi/10.1145/3539618.3591877)] [[code](https://github.com/zhanhl316/SocialDial)]
- STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.20645)]
- The Moral Foundations Reddit Corpus, arXiv, 2022, [[paper](https://arxiv.org/abs/2208.05545)]
- The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems, ACL, 2022, [[paper](https://aclanthology.org/2022.acl-long.261/)]
- The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems, arXiv, 2022, [[paper](https://arxiv.org/abs/2204.03021)] [[code](https://github.com/SALT-NLP/mic)]
- The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)]
- Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.17283)]
- Understanding Dataset Difficulty with V-Usable Information, arXiv, 2021, [[paper](https://arxiv.org/abs/2110.08420)] [[dataset](https://huggingface.co/datasets/stanfordnlp/SHP)] [[code](https://github.com/kawine/dataset_difficulty)]
- VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05465)]
- Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation, ACL-DEMO, 2025, [[paper](https://aclanthology.org/2025.acl-demo.64/)]
- ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.111/)]
- ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI, 2022, [[paper](https://doi.org/10.1609/aaai.v36i10.21368)]
- ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI, 2022, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/21368)] [[dataset](https://liang-qiu.github.io/ValueNet/)]
- Valuenet: A new dataset for human value driven dialogue system. Qiu et al. AAAI 2022., AAAI, 2022, [[paper](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)]
- Vision-Language Models under Cultural and Inclusive Considerations, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.06177)]
- Visually Grounded Reasoning across Languages and Cultures, arXiv, 2021, [[paper](https://arxiv.org/abs/2109.13238)] [[project](https://marvl-challenge.github.io/)]
- VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1119/)]
- VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.13775)]
- When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.26348)]
- Whose Opinions Do Language Models Reflect?, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.17548)] [[link](https://proceedings.mlr.press/v202/santurkar23a.html)]
- Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13383)]
- WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.12705)] [[link](https://worldcuisines.github.io/)]
- WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models, LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.1539/)]
- Would you Rather? A New Benchmark for Learning Machine Alignment with Cultural Values and Social Preferences, ACL, 2020, [[paper](https://aclanthology.org/2020.acl-main.477/)]
- XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.14063)]

<a id="catalog-reliability-validity-and-auditing"></a>

#### 🔬 Reliability, validity, and auditing (17)

- A large-scale replication of scenario-based experiments in psychology and management using large language models, Nature Computational Science, 2025.08, [[paper](https://nature.com/articles/s43588-025-00840-7)]
- A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL 2025 Best Paper, 2025.07, [[paper](https://aclanthology.org/2025.acl-long.1454/)]
- A validity-guided workflow for robust large language model research in psychology, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.04491)]
- Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.18462)]
- Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing, ACM proceedings or journal, 2020, [[paper](https://doi.org/10.1145/3351095.3372873)]
- Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.11254)]
- EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.30258)]
- From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.16697)]
- Large Language Models are not Fair Evaluators, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.511/)]
- Large language models that replace human participants can harmfully misportray and flatten identity groups, Nature Machine Intelligence, 2025.03, [[paper](https://nature.com/articles/s42256-025-00986-z)]
- Larger and more instructable language models become less reliable, Nature, 2024.10, [[paper](https://nature.com/articles/s41586-024-07930-y)]
- Model Cards for Model Reporting, ACM proceedings or journal, 2019, [[paper](https://doi.org/10.1145/3287560.3287596)]
- Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.04826)]
- POSIX: A Prompt Sensitivity Index For Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02185)]
- Psychometric item validation using virtual respondents with trait-response mediators, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.05890)]
- Revisiting the Reliability of Psychological Scales on Large Language Models, EMNLP, 2024, [[paper](https://arxiv.org/abs/2305.19926)]
- You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments, NAACL, 2024, [[paper](https://arxiv.org/abs/2311.09718)]

<a id="catalog-choice-action-and-behavioral-consistency"></a>

#### 🎯 Choice, action, and behavioral consistency (15)

- (Norm) Align on the Fly: Adapting Chatbot Behavior to Established Norms, arXiv, 2023.12, [[paper](https://arxiv.org/abs/2312.15907)] [[code](https://github.com/GAIR-NLP/OPO)]
- Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.27699)]
- How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior, Nature Human Behaviour, 2024, [[paper](https://nature.com/articles/s41562-024-01938-0.pdf)]
- How large language models can reshape collective intelligence, Nature Human Behavior, 2024.09, [[paper](https://nature.com/articles/s41562-024-01959-9)]
- Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1562/)]
- Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.154/)]
- Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.05018)]
- Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned, arXiv, 2022, [[paper](https://arxiv.org/abs/2209.07858)] [[dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)]
- Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12369)]
- Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019., arXiv, 2019, [[paper](https://arxiv.org/abs/1911.03891)] [[link](https://maartensap.com/social-bias-frames/)]
- The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.806/)]
- The theory of planned behavior, Elsevier journal or book, 1991, [[paper](https://sciencedirect.com/science/article/pii/074959789190020T)]
- Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback, arXiv, 2022, [[paper](https://arxiv.org/abs/2204.05862)] [[code](https://github.com/anthropics/hh-rlhf)]
- Training language models to follow instructions with human feedback. Ouyang et al. Neurips 2022., NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)]
- What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.317/)]

<a id="catalog-culture-language-and-pluralism"></a>

#### 🌍 Culture, language, and pluralism (103)

- 'Too much alignment; not enough culture': Re-balancing Cultural Alignment Practices in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.26167)]
- (GlobalOpinionQA) Towards Measuring the Representation of Subjective Global Opinions in Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.16388)] [[dataset](https://huggingface.co/datasets/Anthropic/llm_global_opinions)] [[project](https://llmglobalvalues.anthropic.com/)]
- ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12962)]
- An Evaluation of Cultural Value Alignment in LLM, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.08863)]
- Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.23820)]
- Assessing Cross-Cultural Alignment between ChatGPT and Human Societies, arXiv, 2023, [[paper](https://arxiv.org/abs/2303.17466)]
- Assessing LLMs for Moral Value Pluralism, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.10075)]
- Attributing Culture-Conditioned Generations to Pretraining Corpora, arXiv, 2025, [[paper](https://arxiv.org/abs/2412.20760)] [[code](https://github.com/huihanlhh/CultureGenAttr)]
- Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.15755)]
- BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.09948)] [[code](https://github.com/nlee0212/BLEnD)]
- Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.2/)]
- Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.08045)]
- Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.01127)]
- CARE: Multilingual Human Preference Learning for Cultural Awareness, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.05154)]
- CAReDiO: Enhancing Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.08820)]
- CCBench: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05405)]
- CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.16421)]
- Challenges and Strategies in Cross-Cultural NLP, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.10020)]
- Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.20229)]
- code and data, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.12880)] [[code](https://github.com/NeuralSentinel/CulturalKaleidoscope)]
- Coherence Maximization Improves Pluralistic Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.03110)]
- Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.17256)]
- CulFiT: Fine-grained Cultural-aware LLM Training via Multilingual Critique Data Synthesis, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.19484)]
- Cultural Adaptation in Large Language Models for Political Discourse, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.23332)]
- Cultural Alignment in Large Language Models Using Soft Prompt Tuning, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.16094)]
- Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.12342)]
- Cultural bias and cultural alignment of large language models, PNAS Nexus, 2024, [[paper](https://doi.org/10.1093/pnasnexus/pgae346)]
- Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11661)]
- Cultural Learning-Based Culture Adaptation of Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.156/)]
- Cultural Learning-Based Culture Adaptation of Language Models (CLCA), arXiv, 2025, [[paper](https://arxiv.org/abs/2504.02953)]
- Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.11167)]
- Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17112)]
- Cultural Value Alignment Via Latent Activation Steering in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.26365)]
- CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02677)]
- Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.03930)]
- CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.06664)]
- Culture is Not Trivia: Sociocultural Theory for Cultural NLP, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.12057)]
- CultureBank: An Online Community-Driven Knowledge Base toward Culturally Aware Language Technologies, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.15238)]
- CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.01879)]
- CultureLLM: Incorporating Cultural Differences into Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.10946)] [[code](https://github.com/Scarelette/CultureLLM)]
- CulturePark: Boosting Cross-cultural Understanding in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.15145)]
- CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.10886)]
- CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.04885)]
- CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.12014)]
- Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.21977)]
- Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.06210)]
- DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained LMs, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.05076)]
- EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.20264)]
- Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.18460)]
- EtiCor: Corpus for Analyzing LLMs for Etiquettes, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.18974)]
- Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.21798)]
- Evaluating Pluralism in LLMs through Latent Perspectives, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13254)]
- Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.04045)]
- Exploring Cultural Variations in Moral Judgments with Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12433)]
- Extrinsic Evaluation of Cultural Competence in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11565)]
- From Distributional to Overton Pluralism: Investigating Large Language Model Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.17692)]
- From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16408)]
- Having Beer after Prayer? Measuring Cultural Bias in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2305.14456)] [[code](https://github.com/tareknaous/camel)]
- Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.05931)]
- How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.17773)]
- How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.14805)]
- Improving Cross-Cultural Survey Simulation with Calibrated Value Personas, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.16193)]
- Investigating Cultural Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.13231)]
- Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.16761)]
- Large Language Models as Superpositions of Cultural Perspectives, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.07870)] [[link](https://gitlab.inria.fr/gkovac/value_stability)]
- Legal Theory for Pluralistic Alignment, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.17271)]
- Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.08797)]
- LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15003)]
- LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.06032)]
- Made-in China, Thinking in America: U.S. Values Persist in Chinese LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.13723)]
- Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.09637)]
- Meta-Learning Preferences for Multilingual LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.13315)]
- Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.22475)]
- Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12091)]
- Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.16534)]
- Multilingual Language Models are not Multicultural: A Case Study in Emotion, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.01370)]
- NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.18383)]
- NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.12464)] [[code](https://github.com/Akhila-Yerukola/NormAd)]
- On the steerability of large language models toward data-driven personas, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.04978)]
- Overton Pluralistic Reinforcement Learning for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.20759)]
- Pluralistic Alignment for Healthcare: A Role-Driven Framework, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.10685)]
- Plurals: A System for Guiding LLMs Via Simulated Social Ensembles, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.17213)]
- POW: Political Overton Windows of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.08853)]
- Probing Pre-Trained Language Models for Cross-Cultural Differences in Values, arXiv, 2022, [[paper](https://arxiv.org/abs/2203.13722)]
- Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.11311)]
- Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.08688)]
- RLHF: A Comprehensive Survey for Cultural, Multimodal and Low-Latency Alignment Methods, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.03939)]
- Self-Pluralising Culture Alignment for Large Language Models (CultureSPA), arXiv, 2024, [[paper](https://arxiv.org/abs/2410.12971)]
- Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.07068)]
- Steerable Cultural Preference Optimization of Reward Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.18606)]
- Steering LLMs for Culturally Localized Generation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.23301)]
- Survey of Cultural Awareness in Language Models: Text and Beyond, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.00860)]
- The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.12744)]
- The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20225)]
- Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.21700)]
- Toward Culturally Grounded Natural Language Processing, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.26013)]
- Towards Measuring and Modeling "Culture" in LLMs: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.15412)] [[code](https://github.com/faridlazuarda/cultural-llm-papers)]
- Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation, Elsevier journal or book, 2025, [[paper](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)]
- Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.12878)]
- Value kaleidoscope: engaging AI with pluralistic human values, rights, and duties, AAAI, 2024, [[paper](https://doi.org/10.1609/aaai.v38i18.29970)]
- Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00242)]
- WorldValuesBench: A Large-Scale Benchmark for Multi-Cultural Value Awareness of Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.16308)]
- XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.05662)]

<a id="catalog-preferences-opinions-and-social-simulation"></a>

#### 🗣️ Preferences, opinions, and social simulation (121)

- (ANES) CommunityLM: Probing Partisan Worldviews from Language Models, COLING, 2022, [[paper](https://arxiv.org/abs/2209.07065)]
- (ANES) Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information, arXiv, 2024.02, [[paper](https://arxiv.org/abs/2402.18144)]
- (ANES) Representation Bias in Political Sample Simulations with Large Language Models, arXiv, 2024.07, [[paper](https://arxiv.org/abs/2407.11409)]
- (ANES) Unpacking Political Bias in Large Language Models: A Cross-Model Comparison on U.S. Politics, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.16746)]
- (Culture) Cultural tendencies in generative AI, Nature Human Behaviour, 2025.06, [[paper](https://nature.com/articles/s41562-025-02242-1)]
- (GLES) Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.13169)]
- (GLES) Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.16280)]
- (GLES) Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion, arXiv, 2024.07, [[paper](https://arxiv.org/abs/2407.08563)]
- (Other / custom) AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction, arXiv, 2023.05, [[paper](https://arxiv.org/abs/2305.09620)]
- (Other / custom) Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys, arXiv, 2024.05, [[paper](https://arxiv.org/abs/2405.19323)]
- (Other / custom) Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs, arXiv, 2025.05, [[paper](https://arxiv.org/abs/2503.13149)]
- (Other / custom) Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.18282)]
- (Other / custom) Demonstrations of the Potential of AI-based Political Issue Polling, Harvard Data Science Review (HDSR), 2023.07, [[paper](https://arxiv.org/abs/2307.04781)]
- (Other / custom) From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models, ACL, 2023, [[paper](https://arxiv.org/abs/2305.08283)]
- (Other / custom) How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?, Digital Society, 2023.07, [[paper](https://link.springer.com/article/10.1007/s44206-023-00054-2)]
- (Other / custom) IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.08395)]
- (Other / custom) Large Language Models Can Be Used to Estimate the Latent Positions of Politicians, arXiv, 2023.03, [[paper](https://arxiv.org/abs/2303.12057)]
- (Other / custom) Linear Representations of Political Perspective Emerge in Large Language Models, arXiv, 2025.03, [[paper](https://arxiv.org/abs/2503.02080)]
- (Other / custom) Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs, NAACL (Short Paper, 2024, [[paper](https://arxiv.org/abs/2403.13592)]
- (Other / custom) Questioning the Survey Responses of Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)]
- (PCT) Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.14843)]
- (PCT) Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias, arXiv, 2026.01, [[paper](https://arxiv.org/abs/2601.06194)]
- (PCT) Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models, ACL, 2024, [[paper](https://arxiv.org/abs/2402.16786)]
- (PCT) PRISM: A Methodology for Auditing Biases in Large Language Models, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.18906)]
- (PCT) Revealing Fine-Grained Values and Opinions in Large Language Models, EMNLP Findings, 2024, [[paper](https://arxiv.org/abs/2406.19238)]
- (PCT) The Political Biases of ChatGPT, Social Sciences, 2023.03, [[paper](https://mdpi.com/2076-0760/12/3/148)]
- (PCT) The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation, arXiv, 2023.01, [[paper](https://arxiv.org/abs/2301.01768)]
- (PCT) The Self-Perception and Political Biases of ChatGPT, Human Behavior and Emerging Technologies, 2024.07, [[paper](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)]
- A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.14106)]
- AI PERSONA: Towards Life-long Personalization of LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.13103)]
- Aligning Language Models from User Interactions, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.12273)]
- Aligning Large Language Models with Diverse Political Viewpoints, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.412/)]
- Aligning LLMs with Individual Preferences via Interaction, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.03642)]
- Aligning to Thousands of Preferences via System Message Generalization, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.17977)]
- Aligning VLM Assistants with Personalized Situated Cognition, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00930)]
- AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.26680)]
- Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.19148)]
- APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.21063)]
- APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.27419)]
- BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.398/)]
- Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.02300)]
- COMPO: Community Preferences for Language Model Personalization, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.16027)]
- Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.08968)]
- CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.14773)]
- CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.04756)]
- Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.18310)]
- Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2309.03126)]
- Drift: Decoding-time Personalized Alignments with Implicit User Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.14289)]
- EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.26883)]
- Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16348)]
- EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.16545)]
- Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.20589)]
- Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.18071)]
- Few-shot Personalization of LLMs with Mis-aligned Responses, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.18678)]
- From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15463)]
- From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.23382)]
- From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.16303)]
- From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.00728)]
- From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16610)]
- From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20006)]
- From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.18271)]
- Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.24647)]
- Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16120)]
- Large Language Models Empowered Personalized Web Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.17236)]
- Learning to summarize user information for personalized reinforcement learning from human feedback, OpenReview, 2026, [[paper](https://openreview.net/forum?id=Ar078WR3um)]
- LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14012)]
- MAP: Multi-Human-Value Alignment Palette, OpenReview, 2024, [[paper](https://openreview.net/forum?id=NN6QHwgRrQ)]
- MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.25342)]
- MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14184)]
- MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.24846)]
- More human than human: measuring ChatGPT political bias, Springer journal or proceedings, 2023, [[paper](https://link.springer.com/article/10.1007/s11127-023-01097-2)]
- NextQuill: Causal Preference Modeling for Enhancing LLM Personalization, OpenReview, 2026, [[paper](https://openreview.net/forum?id=xYpVlKMFqv)]
- Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1529/)]
- Opinion dynamics and mutual influence with LLM agents through dialog simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.12583)]
- P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling, OpenReview, 2026, [[paper](https://openreview.net/forum?id=hXNApWLBZG)]
- PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=1kFDrYCuSu)]
- PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.04003)]
- Persona-Based Simulation of Human Opinion at Population Scale, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.27056)]
- Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.11060)]
- Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.12663)]
- PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06254)]
- PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12915)]
- PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.09902)]
- Personalized Adaptation via In-Context Preference Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.14001)]
- Personalized Benchmarking: Evaluating LLMs by Individual Preferences, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.18943)]
- Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.10009)]
- Personalized Language Modeling from Personalized Human Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.05133)]
- Personalized LLM Decoding via Contrasting Personal Preference, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.12109)]
- Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It, OpenReview, 2026, [[paper](https://openreview.net/forum?id=O1hfVE0UxG)]
- Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.07343)]
- Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.11564)]
- Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.10075)]
- PersonalLLM: Tailoring LLMs to Individual Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.20296)]
- PersonaVLM: Long-Term Personalized Multimodal LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.13074)]
- PEToolLLM: Towards Personalized Tool Learning in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.18980)]
- Political-LLM: Large Language Models in Political Science, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.06864)] [[project](https://political-llm.org/)]
- POPI: Personalizing LLMs via Optimized Natural Language Preference Inference, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.17881)]
- Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.22345)]
- Preference-Aware Rubric Learning for Personalized Evaluation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.31545)]
- PrefPalette: Personalized Preference Modeling with Latent Attributes, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13541)]
- PRIME: Large Language Model Personalization with Cognitive Memory and Thought Processes, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.04607)]
- Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17571)]
- RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.00254)]
- Show, Don't Tell: Aligning Language Models with Demonstrated Feedback, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.00888)]
- Silicon Sampling via Cross-Survey Transfer, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.03091)]
- Steering Large Language Models for Machine Translation Personalization, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.16612)]
- Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback, OpenReview, 2026, [[paper](https://openreview.net/forum?id=nc28mSbyVG)]
- SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.05598)]
- Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.15456)]
- Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.10991)]
- The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.04570)]
- The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.11096)]
- The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.16019)] [[code](https://github.com/HannahKirk/prism-alignment)]
- The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models, OpenReview, 2024, [[paper](https://openreview.net/forum?id=DFr5hteojx)]
- Think-While-Generating: On-the-Fly Reasoning for Personalized Long-Form Generation, OpenReview, 2026, [[paper](https://openreview.net/forum?id=lle0aGQyQb)]
- Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.07018)]
- Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.18849)]
- TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.01755)]
- What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data, OpenReview, 2026, [[paper](https://openreview.net/forum?id=sC6A1bFDUt)]
- When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.24613)]
- When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.19158)]

<a id="catalog-moral-reasoning-and-value-understanding"></a>

#### ⚖️ Moral reasoning and value understanding (63)

- (DIT) Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test, arXiv, 2024.02, [[paper](https://arxiv.org/abs/2402.02135)]
- (DIT) Probing the Moral Development of Large Language Models through Defining Issues Test, arXiv, 2023.09, [[paper](https://arxiv.org/abs/2309.13356)]
- (ETHICS) An Evaluation of GPT-4 on the ETHICS Dataset, arXiv, 2023.09, [[paper](https://arxiv.org/abs/2309.10492)]
- (ETHICS) Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety, NeurIPS Workshop, 2022, [[paper](https://arxiv.org/abs/2212.06295)]
- (ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP, 2023, [[paper](https://dl.acm.org/doi/abs/10.1145/3624918.3625327)] [[code](https://github.com/wanng-ide/ealm)]
- (ETHICS) Inducing Human-like Biases in Moral Reasoning Language Models, arXiv, 2024.11, [[paper](https://arxiv.org/abs/2411.15386)]
- (MFT) Analyzing the Ethical Logic of Six Large Language Models, arXiv, 2025.01, [[paper](https://arxiv.org/abs/2501.08951)]
- (MFT) Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31704)]
- (MFT) Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy, NAACL Workshop, 2022, [[paper](https://arxiv.org/abs/2205.12771)]
- (MFT) Exploring and steering the moral compass of Large Language Models, ICPR, 2024, [[paper](https://arxiv.org/abs/2405.17345)]
- (MFT) M3oralBench: A MultiModal Moral Benchmark for LVLMs, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.20718)]
- (MFT) Moral Foundations of Large Language Models, EMNLP, 2024, [[paper](https://arxiv.org/abs/2310.15337)]
- (MFT) Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity, ACL Workshop, 2023, [[paper](https://arxiv.org/abs/2209.12106)]
- (MFT) MoralBench: Moral Evaluation of LLMs, arXiv, 2024.06, [[paper](https://arxiv.org/abs/2406.04428)] [[code](https://github.com/agiresearch/MoralBench)]
- (MFT) Towards "Differential AI Psychology" and in-context Value-driven Statement Alignment with Moral Foundations Theory, arXiv, 2024.08, [[paper](https://arxiv.org/abs/2408.11415)]
- (MFT) Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.18863)]
- (Other / custom) Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, ACL 2025 Best Resource Paper, 2025.07, [[paper](https://aclanthology.org/2025.acl-long.294/)]
- (Other / custom) Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment, AIES, 2024, [[paper](https://ojs.aaai.org/index.php/AIES/article/view/31741)]
- (Other / custom) Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?, C3NLP, 2024, [[paper](https://arxiv.org/abs/2406.16316)]
- (Other / custom) Evaluating Moral Beliefs across LLMs through a Pluralistic Framework, arXiv, 2024.11, [[paper](https://arxiv.org/abs/2411.03665)]
- (Other / custom) Evaluating the Moral Beliefs Encoded in LLMs, NeurIPS, 2023, [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)]
- (Other / custom) Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper), ACM Digital Library, 2024, [[paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)]
- (Other / custom) Knowledge of cultural moral norms in large language models, ACL, 2023, [[paper](https://arxiv.org/abs/2306.01857)]
- (Other / custom) Large-scale moral machine experiment on large language models, arXiv, 2024.11, [[paper](https://arxiv.org/abs/2411.06790)]
- (Other / custom) LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.00962)]
- (Other / custom) Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment, arXiv, 2024.11, [[paper](https://arxiv.org/abs/2411.11731)]
- (Other / custom) Normative Evaluation of Large Language Models with Everyday Moral Dilemmas, arXiv, 2025.01, [[paper](https://arxiv.org/abs/2501.18081)]
- (Other / custom) Potential benefits of employing large language models in research in moral education and development, Journal of Moral Education, 2023.01, [[paper](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)]
- (Other / custom) Right vs. Right: Can LLMs Make Tough Choices?, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.19926)]
- (Other / custom) SaGE: Evaluating Moral Consistency in Large Language Models, LREC-COLING, 2024, [[paper](https://arxiv.org/abs/2402.13709)]
- (Other / custom) The Moral Mind(s) of Large Language Models, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.04476)]
- (Other / custom) The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.07304)]
- (Other / custom) Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models, arXiv, 2023.11, [[paper](https://arxiv.org/abs/2311.07792)]
- (Other / custom) What does AI consider praiseworthy?, AI and Ethics, 2025.02, [[paper](https://link.springer.com/article/10.1007/s43681-025-00682-z)]
- (Other / custom) When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment, NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)]
- Aditi Khandelwal et al. EACL 2024., EACL, 2024, [[paper](https://aclanthology.org/2024.eacl-long.176/)]
- Agent Alignment in Evolving Social Norms, arXiv, 2024.01, [[paper](https://arxiv.org/abs/2401.04620)]
- Can Machines Learn Morality? The Delphi Experiment, arXiv, 2021, [[paper](https://arxiv.org/abs/2110.07574)] [[project](https://delphi.allenai.org/)]
- CrowS-Pairs, EMNLP, 2020, [[paper](https://aclanthology.org/2020.emnlp-main.154/)] [[code](https://github.com/nyu-mll/crows-pairs)]
- DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.02683)]
- Exploring the psychology of GPT-4's Moral and Legal Reasoning, arXiv, 2023.08, [[paper](https://arxiv.org/abs/2308.01264)]
- How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL Main, 2026, [[paper](https://arxiv.org/abs/2603.13876)] [[code](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)]
- Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence, Nature Machine Intelligence, 2025.01, [[paper](https://nature.com/articles/s42256-024-00969-6)]
- Irene Solaiman and Christy Dennison. NeurIPS 2021., arXiv, 2021, [[paper](https://arxiv.org/abs/2106.10328)]
- Joshua Landau et al. arXiv 2023., arXiv, 2023, [[paper](https://arxiv.org/abs/2302.07459)]
- Laura Weidinger et al. arXiv 2021., arXiv, 2021, [[paper](https://arxiv.org/abs/2112.04359)]
- Learning norms from stories: A prior for value aligned agents. Nahian et al. AIES 2020., arXiv, 2020, [[paper](https://arxiv.org/abs/1912.03553)]
- Moral Foundations of Large Language Models, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.982/)]
- Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences, EMNLP, 2021, [[paper](https://aclanthology.org/2021.emnlp-main.54/)]
- MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023., arXiv, 2023, [[paper](https://arxiv.org/abs/2212.10720)] [[code](https://github.com/thu-coai/MoralDial)]
- Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023., arXiv, 2023, [[paper](https://arxiv.org/abs/2305.03047)] [[dataset](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)] [[code](https://github.com/IBM/Dromedary)]
- Revealing the Pragmatic Dilemma for Moral Reasoning Acquisition in Language Models, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.16600)]
- Safety Assessment of Chinese Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2304.10436)] [[link](http://115.182.62.166:18000/)] [[code](https://github.com/thu-coai/Safety-Prompts)]
- SafetyBench 2023-9, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.07045)] [[dataset](https://huggingface.co/datasets/thu-coai/SafetyBench)] [[project](https://llmbench.ai/safety)] [[code](https://github.com/thu-coai/SafetyBench)]
- Shamik Roy et al. arXiv 2023., NLP+CSS, 2023, [[paper](https://aclanthology.org/2022.nlpcss-1.20/)]
- Shitong Duan et al. ICLR 2024., OpenReview, 2024, [[paper](https://openreview.net/forum?id=m3RRWWFaVe)]
- Social Chemistry 101: Learning to Reason about Social and Moral Norms, EMNLP, 2020, [[paper](https://aclanthology.org/2020.emnlp-main.48/)]
- Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1541/)]
- TRUSTGPT 2023-6, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.11507)] [[code](https://github.com/HowieHwong/TrustGPT)]
- Utkarsh Agarwal et al. LREC/COLING 2024., LREC-COLING, 2024, [[paper](https://aclanthology.org/2024.lrec-main.560/)]
- When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022., NeurIPS, 2022, [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf)] [[dataset](https://huggingface.co/datasets/feradauto/MoralExceptQA)]
- Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL Main (Oral, 2026, [[paper](https://arxiv.org/abs/2509.17703)] [[code](https://github.com/MoralAgentSim/Simulation-Engine)]
- Xi Zhiheng et al. CCL 2023., CCL, 2023, [[paper](https://aclanthology.org/2023.ccl-4.2/)]

<a id="catalog-alignment-steering-and-preferences"></a>

#### 🧰 Alignment, steering, and preferences (133)

- (MBTI) Machine Mindset: An MBTI Exploration of Large Language Models, arXiv, 2023.12, [[paper](https://arxiv.org/abs/2312.12999)] [[code](https://github.com/PKU-YuanGroup/Machine-Mindset)]
- A general language assistant as a laboratory for alignment. Askell et al. arXiv 2021., arXiv, 2021, [[paper](https://arxiv.org/abs/2112.00861)] [[dataset](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)]
- A Roadmap to Pluralistic Alignment, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.05070)] [[code](https://github.com/jfisher52/AI_Pluralistic_Alignment)]
- Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.01642)]
- AI Alignment Breaks at the Edge, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.20042)]
- Aligning \AI\ With Shared Human Values, OpenReview, 2021, [[paper](https://openreview.net/forum?id=dNy_RKzJacY)]
- Aligning Crowd Feedback via Distributional Preference Reward Modeling, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.09764)]
- Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.08385)]
- Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping, AAAI, 2026, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41109)]
- Aligning Multimodal LLM with Human Preference: A Survey, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.14504)]
- Aligning to Thousands of Preferences via System Message Generalization, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)]
- Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.1188/)]
- Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.468/)]
- Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS D&B Track Best Paper, 2025, [[paper](https://arxiv.org/abs/2510.22954)]
- Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.13705)]
- Black-Box Prompt Optimization: Aligning Large Language Models without Model Training, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.176/)]
- Communication-Efficient Desire Alignment for Proactive Embodied Human–Agent Interaction, ACL Main (Oral, 2026, [[paper](https://arxiv.org/abs/2505.22503)]
- Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022., arXiv, 2022, [[paper](https://arxiv.org/abs/2212.08073)] [[code](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)]
- Constitutional Value Potentials: reading and steering internal priority margins in language models, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.15420)]
- Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.85/)]
- Controllable Value Alignment in Large Language Models through Neuron-Level Editing, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.07356)]
- Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.18526)]
- Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede’s Cultural Dimensions, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.567/)]
- CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10199)] [[code](https://github.com/huihanlhh/Culture-Gen)]
- CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.288/)]
- CultureLLM: Incorporating Cultural Differences into Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)]
- CulturePark: Boosting Cross-cultural Understanding in Large Language Models, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)]
- Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.23749)]
- Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach, OpenReview, 2025, [[paper](https://openreview.net/forum?id=6KM1siLL8a)]
- Diverging Preferences: When do Annotators Disagree and do Models Know?, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.14632)]
- Diverse Human Value Alignment for Large Language Models via Ethical Reasoning, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.00379)]
- Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.10588)]
- DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.14420)]
- Evaluating and Inducing Personality in Pre-trained Language Models, NeurIPS, 2023, [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)]
- Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.06929)]
- Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1301/)]
- Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes, arXiv, 2024, [[paper](https://arxiv.org/abs/2412.13998)]
- Fine-tuning language models to find agreement among humans with diverse preferences, arXiv, 2022, [[paper](https://arxiv.org/abs/2211.15006)]
- Foundational Challenges in Assuring Alignment and Safety of Large Language Models, arXiv, 2024.04, [[paper](https://arxiv.org/abs/2404.09932)]
- Foundational Moral Values for AI Alignment, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.17017)]
- From Distributional to Overton Pluralism: Investigating Large Language Model Alignment, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.346/)]
- From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.14912)]
- From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models, EMNLP, 2023, [[paper](https://aclanthology.org/2023.emnlp-main.961/)]
- From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.17857)]
- Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment, OpenReview, 2024, [[paper](https://openreview.net/forum?id=JI6j4NUGHv)]
- Group Robust Preference Optimization in Reward-free RLHF, NeurIPS, 2024, [[paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)]
- HelpSteer2 2024-6, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.08673)] [[dataset](https://huggingface.co/datasets/nvidia/HelpSteer2)] [[code](https://github.com/NVIDIA/NeMo-Aligner)]
- Imitation Beyond Expectation Using Pluralistic Stochastic Dominance, OpenReview, 2025, [[paper](https://openreview.net/forum?id=YX5DHa9OfX)]
- Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022., arXiv, 2022, [[paper](https://arxiv.org/abs/2209.14375)] [[link](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)]
- Improving the Distributional Alignment of LLMs using Supervision, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.00439)]
- Internal Value Alignment in Large Language Models through Controlled Value Vector Activation, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1326/)]
- Internal Value Alignment in Large Language Models through Controlled Value Vector Activation, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.11316)]
- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts, Findings of EMNLP, 2024, [[paper](https://aclanthology.org/2024.findings-emnlp.620/)]
- Justifications for Democratizing AI Alignment and Their Prospects, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.19548)]
- Language Model Alignment in Multilingual Trolley Problems, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02273)]
- Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1028/)]
- Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain, NAACL-INDUSTRY, 2024, [[paper](https://aclanthology.org/2024.naacl-industry.18/)]
- Language Models Resist Alignment: Evidence From Data Compression, ACL Best Paper, 2025, [[paper](https://arxiv.org/abs/2406.06144)]
- Large Language Model Alignment: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.15025)]
- Large Language Models as Optimizers, OpenReview, 2024, [[paper](https://openreview.net/forum?id=Bb4VGOWELI)]
- Large pre-trained language models contain human-like biases of what is right and wrong to do. Schramowski et al. Nature Machine Intelligence 2022., arXiv, 2022, [[paper](https://arxiv.org/abs/2103.11790)]
- Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability, ANTHOLOGY-FILES, 2025, [[paper](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.90/)]
- LoRe: Personalizing LLMs via Low-Rank Reward Modeling, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.14439)]
- MallowsPO: Fine-Tune Your LLM with Preference Dispersions, arXiv, 2024, [[paper](https://arxiv.org/abs/2405.14953)]
- MAP: Multi-Human-Value Alignment Palette, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.19198)]
- MaxMin-RLHF: Alignment with Diverse Human Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.08925)]
- MixDPO: Modeling Preference Strength for Pluralistic Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.06180)]
- Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration, EMNLP, 2024, [[paper](https://aclanthology.org/2024.emnlp-main.240/)]
- Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.15951)]
- Moral Alignment for LLM Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.01639)]
- MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.12271)]
- Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.17579)]
- NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.120/)]
- Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.345/)]
- OASIS: Open Agent Social Interaction Simulations with One Million Agents, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.11581)]
- Optimizing generative AI by backpropagating language model feedback, Nature, Nature, 2025.03, [[paper](https://nature.com/articles/s41586-025-08661-4)]
- PAD: Personalized Alignment of LLMs at Decoding-Time, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.04070)]
- Pairwise Calibrated Rewards for Pluralistic Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06298)]
- PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.08469)]
- Parametric Social Identity Injection and Diversification in Public Opinion Simulation, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16142)]
- PERSONA: A Reproducible Testbed for Pluralistic Alignment, COLING, 2025, [[paper](https://aclanthology.org/2025.coling-main.752/)]
- Personality Alignment of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.11779)]
- PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.16679)]
- PKU-SafeRLHF 2023-7, arXiv, 2023, [[paper](https://arxiv.org/abs/2307.04657)] [[dataset](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)] [[code](https://github.com/PKU-Alignment/safe-rlhf)]
- Pluralistic Alignment for Healthcare: A Role-Driven Framework, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.1596/)]
- PluralLLM: Pluralistic Alignment in LLMs via Federated Learning, ACM Digital Library, 2025, [[paper](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)]
- Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking, arXiv, 2024.09, [[paper](https://arxiv.org/abs/2409.08622)]
- Position: A Roadmap to Impactful Pluralistic Alignment Research, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.22305)]
- Position: Align AI to Our Aspirations, Not Our Flaws, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13755)]
- Position: The Alignment Community is Unintentionally Building a Censor's Toolkit, OpenReview, 2026, [[paper](https://openreview.net/forum?id=dy2HwmOvFX)]
- Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.06059)]
- ProgressGym: Alignment with a Millennium of Moral Progress, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.20087)] [[code](https://github.com/PKU-Alignment/ProgressGym)]
- ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs, ACL, 2024, [[paper](https://aclanthology.org/2024.acl-long.381/)]
- Reflective Verbal Reward Design for Pluralistic Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.17834)]
- Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.20805)]
- Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?, arXiv, 2023, [[paper](https://arxiv.org/abs/2308.15399)]
- Reward Model Perspectives: Whose Opinions Do Reward Models Reward?, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.06391)]
- Robust Multi-Objective Controlled Decoding of Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.08796)]
- Role Steering of Language Models for Social Simulations, arXiv, 2026, [[paper](https://arxiv.org/abs/2608.00023)]
- SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.16665)]
- Scopes of Alignment, AAAI 2025 workshop, 2025.01, [[paper](https://arxiv.org/abs/2501.12405)]
- Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.16482)]
- Self-Pluralising Culture Alignment for Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.350/)]
- Simple Role Assignment is Extraordinarily Effective for Safety Alignment, ACL Findings, 2026, [[paper](https://arxiv.org/abs/2602.00061)]
- Social Simulacra: Creating Populated Prototypes for Social Computing Systems, ACM Digital Library, 2022, [[paper](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)]
- Societal Alignment Frameworks Can Improve LLM Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.00069)]
- Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.162/)]
- SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment, Findings of ACL, 2025, [[paper](https://aclanthology.org/2025.findings-acl.41/)]
- Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.08509)]
- SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF, Findings of EMNLP, 2023, [[paper](https://aclanthology.org/2023.findings-emnlp.754/)]
- STELA: a community-centred approach to norm elicitation for AI alignment, Nature Scientific Reports, 2024.03, [[paper](https://nature.com/articles/s41598-024-56648-4)]
- Strong and weak alignment of large language models with human values, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.04655)]
- Strong and weak alignment of large language models with human values, Nature Scientific Reports, 2024.08, [[paper](https://nature.com/articles/s41598-024-70031-3)]
- Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions, arXiv, 2025, [[paper](https://arxiv.org/abs/2508.11414)]
- The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models, EACL, 2026, [[paper](https://aclanthology.org/2026.eacl-long.305/)]
- The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.23965)]
- The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.03048)]
- The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning, arXiv, 2023, [[paper](https://arxiv.org/abs/2312.01552)]
- Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1408/)]
- Towards Scalable Automated Alignment of LLMs: A Survey, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.01252)]
- Training Socially Aligned Language Models in Simulated Human Society, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.16960)] [[code](https://github.com/agi-templar/Stable-Alignment)]
- Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.1532/)]
- Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.06404)]
- Unintended Impacts of LLM Alignment on Global Representation, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.15018)]
- Value Alignment from Unstructured Text, EMNLP-INDUSTRY, 2024, [[paper](https://aclanthology.org/2024.emnlp-industry.81/)]
- Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value, NAACL, 2024, [[paper](https://aclanthology.org/2024.naacl-long.486/)]
- ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs, WINLP, 2025, [[paper](https://aclanthology.org/2025.winlp-main.15/)]
- ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.04569)]
- VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.18113)]
- VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.04822)]
- VISPA: Pluralistic Alignment via Automatic Value Selection and Activation, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.12758)]
- What are human values, and how do we align AI to them?, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.10636)]
- Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00415)]

<a id="catalog-value-representation-and-model-internals"></a>

#### 📐 Value representation and model internals (44)

- A Method for Learning Value Systems in Generative AI, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.16903)]
- AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.22440)]
- Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05052)]
- Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.12851)]
- Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.22396)]
- Do Differences in Values Influence Disagreements in Online Discussions?, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.15757)]
- Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.00913)]
- EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.12792)]
- Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure, Research Square, 2025, [[paper](https://doi.org/10.21203/rs.3.rs-8270539/v1)]
- Enhancing Stance Classification on Social Media Using Quantified Moral Foundations, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.09848)]
- Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.585/)]
- Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.02444)]
- Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.04456)]
- High-Dimension Human Value Representation in Large Language Models, NAACL, 2025, [[paper](https://aclanthology.org/2025.naacl-long.274/)]
- High-Dimension Human Value Representation in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.07900)] [[code](https://github.com/HLTCHKUST/UniVaR)]
- Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.14172)]
- Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.27373)]
- Investigating Human Values in Online Communities, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.14177)]
- Learning the Value Systems of Societies from Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.20728)]
- Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08835)]
- Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11018)]
- Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.22660)]
- MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions, arXiv, 2024, [[paper](https://arxiv.org/abs/2403.07678)]
- Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning, arXiv, 2024, [[paper](https://arxiv.org/abs/2401.17228)]
- More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.22641)]
- MoVa: Towards Generalizable Classification of Human Morals and Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.24216)]
- Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.23659)]
- SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments, SemEval, 2023, [[paper](https://aclanthology.org/2023.semeval-1.313/)]
- SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.12633)]
- The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.11770)]
- Tracing Moral Foundations in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.05437)]
- Understanding How Value Neurons Shape the Generation of Specified Values in LLMs, Findings of EMNLP, 2025, [[paper](https://aclanthology.org/2025.findings-emnlp.501/)]
- Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs, arXiv, 2025, [[paper](https://arxiv.org/abs/2502.08640)]
- Value Alignment of Social Media Ranking Algorithms, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.14434)]
- Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.10766)]
- Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.00779)] [[code](https://github.com/tsor13/kaleido)]
- Value Lens: Using Large Language Models to Understand Human Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.15722)]
- Value Profiles for Encoding Human Variation, arXiv, 2025, [[paper](https://arxiv.org/abs/2503.15484)]
- VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.03160)]
- ValueNet: A New Dataset for Human Value Driven Dialogue System, arXiv, 2021, [[paper](https://arxiv.org/abs/2112.06346)]
- Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.15236)]
- What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric, ACL, 2023, [[paper](https://aclanthology.org/2023.acl-long.789/)]
- Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.20270)]
- Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.08453)]

<a id="catalog-measurement-and-profiling"></a>

#### 📏 Measurement and profiling (87)

- (GLOBE) Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models, arXiv, 2024.06, [[paper](https://arxiv.org/abs/2406.17675)]
- (Other / custom) Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches, arXiv, 2024.04, [[paper](https://arxiv.org/abs/2404.12744)]
- (Other / custom) CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility, arXiv, 2023.07, [[paper](https://arxiv.org/abs/2307.09705)] [[dataset](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)] [[code](https://github.com/X-PLUG/CValues)]
- (Other / custom) Measurement of LLM’s Philosophies of Human Nature, arXiv, 2025.04, [[paper](https://arxiv.org/abs/2504.02304)] [[code](https://github.com/kodenii/M-PHNS)]
- (Other / custom) Measuring Spiritual Values and Bias of Large Language Models, arXiv, 2024.10, [[paper](https://arxiv.org/abs/2410.11647)]
- (Other / custom) Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas, arXiv, 2025.05, [[paper](https://arxiv.org/abs/2505.14633)]
- (Schwartz) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, Perspectives on Psychological Science, 2023.01, [[paper](https://journals.sagepub.com/doi/full/10.1177/17456916231214460)] [[code](https://github.com/feradauto/MoralCoT)]
- (Schwartz) Improving Language Model Personas via Rationalization with Psychological Scaffolds, arXiv, 2025.04, [[paper](https://arxiv.org/abs/2504.17993)]
- (Schwartz) Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI, 2025, [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/34839)]
- (Schwartz) The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas, arXiv, 2025.05, [[paper](https://arxiv.org/abs/2505.18154)]
- (Schwartz) ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs, arXiv, 2024.09, [[paper](https://arxiv.org/abs/2409.09586)]
- (Schwartz) What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory, arXiv, 2023.04, [[paper](https://arxiv.org/abs/2304.03612)]
- (Schwartz) When Prompting Fails to Sway: Inertia in Moral and Value Judgments of Large Language Models, NeurIPS, 2022, [[paper](https://arxiv.org/abs/2408.09049)]
- (Schwartz) Who is GPT-3? An Exploration of Personality, Values and Demographics, EMNLP NLP+CSS workshop, 2022, [[paper](https://arxiv.org/abs/2209.14338)]
- (VSM) Cultural Value Differences of LLMs: Prompt, Language, and Model Size, arXiv, 2024.07, [[paper](https://arxiv.org/abs/2407.16891)]
- (WVS) Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.08846)]
- (WVS) On the Alignment of Large Language Models with Global Human Opinion, AAAI 2026 Best Paper (AI Alignment Track), 2026.01, [[paper](https://arxiv.org/abs/2509.01418)] [[code](https://github.com/ku-nlp/global-opinion-alignment)]
- (WVS) Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, arXiv, 2025.03, [[paper](https://arxiv.org/abs/2503.16148)]
- A Scalable Approach to Evaluating Moral Sensitivity in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.02972)]
- AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.13531)]
- AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference, OpenReview, 2026, [[paper](https://openreview.net/forum?id=qNlTH4kYJZ)]
- Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.00751)]
- Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.20205)]
- Are Language Models Sensitive to Morally Irrelevant Distractors?, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.09416)]
- Are Large Language Models Consistent over Value-laden Questions?, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.02996)]
- Are LLMs Bad at Moral Reasoning?, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11635)]
- Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective, arXiv, 2024, [[paper](https://arxiv.org/abs/2501.00581)]
- Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21939)]
- Can Language Models Reason about Individualistic Human Values and Preferences?, arXiv, 2024, [[paper](https://arxiv.org/abs/2410.03868)]
- Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.31213)]
- Can Revealed Preferences Clarify LLM Alignment and Steering?, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.08556)]
- CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.10725)]
- Context-Value-Action Architecture for Value-Driven Large Language Model Agents, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.05939)]
- Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.02109)]
- Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths, arXiv, 2025, [[paper](https://arxiv.org/abs/2506.02481)]
- Do LLMs have Consistent Values?, arXiv, 2024, [[paper](https://arxiv.org/abs/2407.12878)] [[link](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)]
- Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.02197)]
- Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.24319)]
- Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11232)]
- Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?, arXiv, 2024, [[paper](https://arxiv.org/abs/2402.18120)]
- Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.04994)]
- From Stability to Inconsistency: A Study of Moral Preferences in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2504.06324)]
- Generative Value Conflicts Reveal LLM Priorities, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.25369)]
- Heterogeneous Value Alignment Evaluation for Large Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.17147)] [[code](https://github.com/zowiezhang/HVAE)] [[code](https://github.com/zowiezhang/A2EHV)]
- How do LLMs reflect human moral foundations? a study using the moral foundations framework, Taylor & Francis journal, 2026, [[paper](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)]
- Human Psychometric Questionnaires Mischaracterize LLM Behavior, arXiv, 2025, [[paper](https://arxiv.org/abs/2509.10078)]
- Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.03384)]
- Incoherent Values? Probing LLM Preferences Through Parametric Variation, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.21102)]
- Investigating Value-Reasoning Reliability in Small Large Language Models, EMNLP, 2025, [[paper](https://aclanthology.org/2025.emnlp-main.395/)]
- LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.13944)]
- LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2408.01460)]
- Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.22170)]
- Measurement and Fairness, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3442188.3445901)]
- Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2409.12106)] [[code](https://github.com/Value4AI/gpv)]
- Measuring human and AI values based on generative psychometrics with large language models, AAAI, 2025, [[paper](https://doi.org/10.1609/aaai.v39i25.34839)]
- Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2604.11216)]
- Mechanistic Origin of Moral Indifference in Language Models, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.15615)]
- Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.15463)]
- Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.12515)]
- Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.08634)]
- Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.03217)]
- Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2511.08565)]
- Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method, Elsevier journal or book, 2025, [[paper](https://sciencedirect.com/science/article/pii/S0925231225008422)]
- Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.12731)]
- On the Credibility of Evaluating LLMs using Survey Questions, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.04033)]
- Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.28911)]
- Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses, arXiv, 2026, [[paper](https://arxiv.org/abs/2507.07188)]
- Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation, arXiv, 2026, [[paper](https://arxiv.org/abs/2607.05554)]
- Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.09893)]
- Quantifying Data Contamination in Psychometric Evaluations of LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.07175)]
- Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.14230)]
- Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing, OpenReview, 2025, [[paper](https://openreview.net/forum?id=0REM9ydeLZ)]
- Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?, arXiv, 2025, [[paper](https://arxiv.org/abs/2507.13490)]
- Superficial Beliefs in LLM Decision-Making, arXiv, 2026, [[paper](https://arxiv.org/abs/2606.11016)]
- The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models, arXiv, 2025, [[paper](https://arxiv.org/abs/2512.03026)]
- Understanding How Value Neurons Shape the Generation of Specified Values in LLMs, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.17712)]
- Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability, arXiv, 2026, [[paper](https://arxiv.org/abs/2603.16017)]
- Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs, arXiv, 2026, [[paper](https://arxiv.org/abs/2601.10257)]
- Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values, arXiv, 2025, [[paper](https://arxiv.org/abs/2501.07071)]
- Value Drifts: Tracing Value Alignment During LLM Post-Training, arXiv, 2025, [[paper](https://arxiv.org/abs/2510.26707)]
- Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items, ACL, 2025, [[paper](https://aclanthology.org/2025.acl-long.838/)]
- Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items, arXiv, 2025, [[paper](https://arxiv.org/abs/2505.01015)]
- Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts, arXiv, 2024, [[paper](https://arxiv.org/abs/2411.11479)]
- ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.04214)] [[code](https://github.com/Value4AI/ValueBench)]
- ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.00378)]
- ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems, arXiv, 2026, [[paper](https://arxiv.org/abs/2602.08567)]
- Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts, arXiv, 2026, [[paper](https://arxiv.org/abs/2605.25256)]

<a id="catalog-other-and-adjacent-value-research"></a>

#### 📎 Other and adjacent value research (44)

- 10.1186/s40537-024-00986-7, Springer journal or proceedings, 2024, [[paper](https://link.springer.com/article/10.1186/s40537-024-00986-7)]
- A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3465416.3483305)]
- A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL Best Paper, 2025, [[paper](https://arxiv.org/abs/2402.11005)]
- Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective, arXiv, 2024.07, [[paper](https://arxiv.org/abs/2408.04638)]
- Automated Mining of Structured Knowledge from Text in the Era of Large Language Models, KDD 2024, 2024.08, [[paper](https://dl.acm.org/doi/pdf/10.1145/3637528.3671469)]
- Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS Oral, 2026, [[paper](https://arxiv.org/abs/2603.13890)] [[code](https://github.com/jingzhe-lin/ASVO)]
- Chatbotarenaconversations 2023-6, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.05685)] [[dataset](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)] [[dataset](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)] [[model](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)] [[code](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)]
- Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science, TACL, 2018, [[paper](https://aclanthology.org/Q18-1041/)]
- EMNLP Main 18, EMNLP, 2023, [[paper](https://aclanthology.org/2023.emnlp-main.18/)]
- Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs, arXiv, 2024, [[paper](https://arxiv.org/abs/2406.13993)]
- Fairness and Abstraction in Sociotechnical Systems, ACM proceedings or journal, 2019, [[paper](https://doi.org/10.1145/3287560.3287598)]
- Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs, ACL Best Paper, 2025, [[paper](https://arxiv.org/abs/2502.01926)]
- Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization, Sociological Methods & Research, 2025.05, [[paper](https://journals.sagepub.com/doi/10.1177/00491241251327130)]
- Generative language models exhibit social identity biases, Nature Computational Science, Nature Computational Science, 2025.01, [[paper](https://nature.com/articles/s43588-024-00741-1)]
- GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods, arXiv, 2023, [[paper](https://arxiv.org/abs/2301.01893)] [[code](https://github.com/WadeYin9712/GIVL)]
- HG & CI & MC, arXiv, 2023, [[paper](https://arxiv.org/abs/2311.09528)] [[dataset](https://huggingface.co/datasets/nvidia/HelpSteer)]
- Holistic Evaluation of Language Models, OpenReview, 2023, [[paper](https://openreview.net/forum?id=iO4LZibEqW)]
- Large Language Model Safety: A Holistic Survey, arXiv, 2024.12, [[paper](https://arxiv.org/abs/2412.17686)]
- Large language models (LLM) in computational social science: prospects, current state, and challenges, Social Network Analysis and Mining, 2025.03, [[paper](https://link.springer.com/article/10.1007/s13278-025-01428-9)]
- Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, Nature humanities and social sciences communications, 2023.12, [[paper](https://arxiv.org/abs/2312.11970)]
- Linhao Yu et al. ACL Findings 2024., Findings of ACL, 2024, [[paper](https://aclanthology.org/2024.findings-acl.703/)]
- Machine Bias. How Do Generative Language Models Answer Opinion Polls?, Sociological Methods & Research, 2025.04, [[paper](https://doi.org/10.1177/00491241251330582)]
- Nicholas Botzer et al. arXiv 2021., arXiv, 2021, [[paper](https://arxiv.org/abs/2101.07664)]
- On the Credibility of Evaluating LLMs using Survey Questions, MME, 2026, [[paper](https://aclanthology.org/2026.mme-main.2/)]
- On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?, ACM proceedings or journal, 2021, [[paper](https://doi.org/10.1145/3442188.3445922)]
- On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective, arXiv, 2025.02, [[paper](https://arxiv.org/abs/2502.14296)]
- Persuading voters using human–artificial intelligence dialogues, Nature, Nature, 2025.12, [[paper](https://nature.com/articles/s41586-025-09771-9)]
- Position: AI Evaluation Should Learn from How We Test Humans, arXiv, 2023, [[paper](https://arxiv.org/abs/2306.10512)]
- PRM800K 2023-5, arXiv, 2023, [[paper](https://arxiv.org/abs/2305.20050)] [[code](https://github.com/openai/prm800k)]
- Questioning the Survey Responses of Large Language Models, NeurIPS Oral, 2024, [[paper](https://arxiv.org/abs/2306.07951)]
- RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models, Findings of EMNLP, 2020, [[paper](https://aclanthology.org/2020.findings-emnlp.301/)]
- Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR, 2025, [[paper](https://arxiv.org/abs/2412.06435)]
- Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR, 2025, [[paper](https://openreview.net/forum?id=3ms8EQY7f8)] [[code](https://github.com/zfw1226/D2A)]
- Stick to your role! Stability of personal values expressed in large language models, PLOS ONE, 2024, [[paper](https://doi.org/10.1371/journal.pone.0309114)] [[model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309114)]
- SummarizefromFeedback 2020-9, arXiv, 2020, [[paper](https://arxiv.org/abs/2009.01325)] [[dataset](https://huggingface.co/datasets/openai/summarize_from_feedback)]
- The AI Gap: How Socioeconomic Status Affects Language Technology Interactions, ACL Best Social Impact Paper, 2025, [[paper](https://arxiv.org/abs/2505.12158)]
- The Rise and Potential of Large Language Model Based Agents: A Survey, arXiv, 2023, [[paper](https://arxiv.org/abs/2309.07864)] [[code](https://github.com/WooooDyy/LLM-Agent-Paper-List)]
- UltraFeedback, arXiv, 2023, [[paper](https://arxiv.org/abs/2310.01377)] [[dataset](https://huggingface.co/datasets/openbmb/UltraFeedback)] [[code](https://github.com/OpenBMB/UltraFeedback)]
- UltraInteract 2024-4, arXiv, 2024, [[paper](https://arxiv.org/abs/2404.02078)] [[dataset](https://huggingface.co/datasets/openbmb/UltraInteract_pair)]
- Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries, Elsevier journal or book, 1992, [[paper](https://sciencedirect.com/science/article/pii/S0065260108602816)] [[link](https://psycnet.apa.org/record/2003-00370-001)]
- Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents, Springer journal or proceedings, 2026, [[paper](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)]
- WebGPT: Browser-assisted question-answering with human feedback, arXiv, 2021, [[paper](https://arxiv.org/abs/2112.09332)] [[dataset](https://huggingface.co/datasets/openai/webgpt_comparisons)]
- Who is GPT-3? An exploration of personality, values and demographics, NLP+CSS, 2022, [[paper](https://aclanthology.org/2022.nlpcss-1.24/)]
- Zhijing Jin et al. NeurIPS 2022., arXiv, 2022, [[paper](https://arxiv.org/abs/2210.01478)]

### 🧩 Standalone data, models, code, and additional resources

<a id="catalog-dataset-and-benchmark-artifacts"></a>

#### 💾 Dataset and benchmark artifacts (5)

- A Systematic Survey of Cultural Datasets for Equitable LLM Alignment, [[dataset](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)]
- Medical-rlhf 2023-5, [[dataset](https://huggingface.co/datasets/shibing624/medical)]
- OASST1pairwiserlhfreward 2023-5, [[dataset](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)]
- OpenHermesPreferences 2024-3, [[dataset](https://huggingface.co/datasets/argilla/OpenHermesPreferences)]
- Zhihurlhf3k 2023-4, [[dataset](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)]

<a id="catalog-model-checkpoints-and-scorers"></a>

#### 🧠 Model checkpoints and scorers (2)

- Exploring Universal Human Values with Large Language Models: The AWARE-Value Model, [[model](https://researchsquare.com/article/rs-8188052/v1)]
- Robustness of large language models in moral judgements, [[model](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)]

<a id="catalog-code-repositories"></a>

#### 🧰 Code repositories (16)

- AI Job Displacement Tracker, [[code](https://github.com/noahaust2/ai-displacement-tracker)]
- Alpacacomparisondata 2023-3, [[code](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)]
- Awesome-LLM-in-Social-Science, [[code](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)]
- Awesome-LLM-Psychometrics, [[code](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)]
- awesome-llm-social-simulation, [[code](https://github.com/Wanying-He/awesome-llm-social-simulation)]
- Awesome-Personalized-Alignment, [[code](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)]
- Awesome-Pluralistic-Alignment, [[code](https://github.com/anudeex/Awesome-Pluralistic-Alignment)]
- Concerns on the use of generative AI in social science research, [[code](https://github.com/uh-dcm/genai-concerns)]
- culture-awareness-llms, [[code](https://github.com/siddheshih/culture-awareness-llms)]
- Datasets for depression detection using data posted on online platforms, [[code](https://github.com/bucuram/depression-datasets-nlp)]
- github.com, [[code](https://github.com/CLUEbenchmark/CLUEDatasetSearch)]
- huozirlhfdata 2024-2, [[code](https://github.com/HIT-SCIR/huozi)]
- huozirlhfdata 2024-2, [[code](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)]
- Medical-rlhf 2023-5, [[code](https://github.com/shibing624/MedicalGPT)]
- Mental Health Datasets, [[code](https://github.com/kharrigian/mental-health-datasets)]
- SuperCLUE-Safety 2023-9, [[code](https://github.com/CLUEbenchmark/SuperCLUE-safety)]

<a id="catalog-project-pages"></a>

#### 🌐 Project pages (2)

- Concerns on the use of generative AI in social science research, [[project](https://uh-dcm.github.io/genai-concerns/)]
- SuperCLUE-Safety 2023-9, [[project](https://cluebenchmarks.com/superclue_safety.html)]

<a id="catalog-survey-resources"></a>

#### 📋 Survey resources (4)

- EVS — European Values Survey, [[survey](https://europeanvaluesstudy.eu/)]
- GSS — General Social Survey, [[survey](https://gss.norc.org/)]
- World Values Survey Wave 7 (2017-2022)., [[survey](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)]
- WVS — World Values Survey, [[survey](https://worldvaluessurvey.org/)]

<a id="catalog-additional-resources"></a>

#### 🔗 Additional resources (72)

- (ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis, [[link](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)]
- (ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis, [[link](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)]
- (ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL), [[link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)]
- (Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL), [[link](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)]
- (Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate, [[link](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000429)]
- (Others & custom) DO MINDFULNESS ACTIVITIES IMPROVE HANDGRIP STRENGTH AMONG OLDER ADULTS: A PROPENSITY SCORE MATCHING APPROACH, 2024.12, Innovation in Aging, [[link](https://academic.oup.com/innovateage/article/8/Supplement_1/1010/7939280)]
- (Others & custom) Improving GPT Generated Synthetic Samples with Sampling-Permutation Algorithm, [[link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4548937)]
- (Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science, [[link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)]
- A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights, [[link](https://unesdoc.unesco.org/ark:/48223/pf0000048063)]
- A review of automatic item generation techniques leveraging large language models, [[link](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)]
- A theory of justice., [[link](https://jstor.org/stable/j.ctvjf9z6v)]
- A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism, [[link](http://jstor.org/stable/24707060)]
- Aggregating Sets of Judgments: An Impossibility Result, [[link](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)]
- An Overview of the Schwartz Theory of Basic Values, [[link](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)]
- An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012., [[link](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)]
- Basic human values: Theory, measurement, and applications, [[link](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)]
- Can Generative AI improve social science?, 2024.05, PNAS, [[link](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)]
- Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023, [[link](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)]
- Citizenship and Social Class, [[link](https://books.google.co.kr/books?id=99v4JQAACAAJ)]
- Collective Choice and Social Welfare, [[link](https://jstor.org/stable/j.ctv2sp3dqx)]
- Conflicts of Values (in Moral Luck), [[link](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)]
- Creating Capabilities: The Human Development Approach and Its Implementation, [[link](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)]
- Cultural Value Orientations, [[link](https://researchgate.net/publication/265997557)]
- Culture's consequences: International differences in work-related values, [[link](https://philpapers.org/rec/HOFCCI-2)]
- Culture's consequences: International differences in work-related values. Hofstede et al. 1984., [[link](https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC)]
- Cultures and organizations: software of the mind, [[link](https://books.google.co.kr/books?id=o4OqTgV3V00C)]
- ESS — European Social Survey, [[link](https://europeansocialsurvey.org/data-portal)]
- Functional theory of human values, [[link](https://researchgate.net/publication/259486885)]
- Handbook of Computational Social Choice, [[link](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)]
- If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task, [[link](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)]
- Kush R. Varshney. XRDS 2019., [[link](https://krvarshney.github.io/)]
- Kush R. Varshney. XRDS 2019., [[link](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)]
- Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice, [[link](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)]
- Liberals and conservatives rely on different sets of moral foundations, [[link](https://pubmed.ncbi.nlm.nih.gov/19379034/)]
- Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002., [[link](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)]
- lit.eecs.umich.edu, [[link](https://lit.eecs.umich.edu/downloads.html)]
- Manipulation of Voting Schemes: A General Result, [[link](https://jstor.org/stable/1914083)]
- Mapping and interpreting cultural differences around the world, [[link](https://researchgate.net/publication/265596552)]
- Measuring Perceived Slant in Large Language Models Through User Evaluations, [[link](https://modelslant.com/paper.pdf)]
- Measuring the Refined Theory of Individual Values in 49 Cultural Groups, [[link](https://researchgate.net/publication/349058866)]
- Mental representations of social values., [[link](https://psycnet.apa.org/record/2012-14612-001)]
- Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies, [[link](https://jstor.org/stable/j.ctv10vm2ns)]
- Modernization, Cultural Change, and Democracy, [[link](https://researchgate.net/publication/230557603)]
- Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism, [[link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2184440)]
- NeurIPS 2025 Tutorial: Human-AI Alignment, [[link](https://hai-alignment-course.github.io/tutorial/)]
- On the Rationale of Group Decision-making, [[link](https://jstor.org/stable/1825026)]
- Perils and opportunities in using large language models in psychological research, [[link](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)]
- Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science, [[link](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)]
- Pew Researcj Center's Global Attitudes Surveys (GAS), [[link](https://pewresearch.org/)]
- Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449, [[link](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)]
- Refining the theory of basic individual values, [[link](https://pubmed.ncbi.nlm.nih.gov/22823292/)]
- Rokeach value survey. Rokeach et al. The nature of human values. 1967., [[link](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)]
- Social Choice and Individual Values, [[link](https://jstor.org/stable/j.ctt1nqb90)]
- Social Choice Theory (in Stanford Encyclopedia of Philosophy), [[link](https://plato.stanford.edu/entries/social-choice/)]
- Stanford 2025: Human-Centered LLMs (CS329X), [[link](https://web.stanford.edu/class/cs329x/)]
- Stanford 2025: Machine Learning from Human Preferences (CS329H), [[link](https://web.stanford.edu/class/cs329h/)]
- Steerable Alignment with Conditional Multiobjective Preference Optimization, [[link](https://dspace.mit.edu/handle/1721.1/156747)]
- Survey of Cultural Awareness in Language Models: Text and Beyond Open Access, [[link](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)]
- The Impossibility of a Paretian Liberal, [[link](https://jstor.org/stable/1829633)]
- The Morality of Freedom, [[link](https://academic.oup.com/book/9926)]
- The Morality of Pluralism, [[link](https://jstor.org/stable/j.ctt7smh7)]
- The Morals of Modernity, [[link](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)]
- The nature of human values., [[link](https://psycnet.apa.org/record/2011-15663-000)]
- The Right and the Good, [[link](https://academic.oup.com/book/27608)]
- The Righteous Mind, [[link](https://righteousmind.com/)]
- The Theory of Communicative Action, [[link](https://philpapers.org/rec/HABTTO)]
- The theory of dyadic morality: Reinventing moral judgment by redefining harm., [[link](https://psycnet.apa.org/record/2018-02142-002)]
- Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022., [[link](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)]
- Towards Pluralistic Alignment of LLMs: A Comprehensive Survey, [[link](https://preprints.org/manuscript/202603.1876)]
- Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop, [[link](https://openaccess.city.ac.uk/id/eprint/31381/)]
- Two Concepts of Liberty, [[link](https://academic.oup.com/book/7968/chapter-abstract/153281672)]
- Value Pluralism (in Stanford Encyclopedia of Philosophy), [[link](https://plato.stanford.edu/entries/value-pluralism/)]

<!-- complete-catalog:end -->

## 🤝 Contributing

Found a missing paper, dataset, model, benchmark, or code release? Open an
[issue](https://github.com/ikanam-ai/ai-values-atlas/issues) or follow the
[contribution guide](CONTRIBUTING.md). Atlas metadata is released under CC BY
4.0; linked resources retain their original licenses.
