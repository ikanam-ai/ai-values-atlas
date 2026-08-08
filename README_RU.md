<div align="center">

<img src="assets/atlas-header.svg" width="100%" alt="AI Values Atlas — открытый путеводитель по исследованиям" />

<h1>AI Values Atlas</h1>

<p><strong>Путеводитель по тому, как ценности представлены, выявляются, выражаются, выбираются и оцениваются в системах ИИ.</strong></p>

<p><a href="README.md">English</a> · <strong>Русский</strong></p>

<p>
  <a href="https://ikanam-ai.github.io/ai-values-atlas/">Открыть атлас</a> ·
  <a href="#карта-поля">Карта поля</a> ·
  <a href="#литература-по-исследовательским-вопросам">Литература</a> ·
  <a href="#аксиологические-пространства">Аксиологии</a> ·
  <a href="#датасеты-бенчмарки-и-инструменты">Датасеты</a> ·
  <a href="CONTRIBUTING.md">Предложить дополнение</a>
</p>

<p>
  <a href="https://github.com/ikanam-ai/ai-values-atlas/actions/workflows/validate.yml"><img alt="validation" src="https://img.shields.io/github/actions/workflow/status/ikanam-ai/ai-values-atlas/validate.yml?style=for-the-badge&label=validated"></a>
  <a href="#полный-каталог"><img alt="resources" src="https://img.shields.io/badge/resources-1018-136f58?style=for-the-badge"></a>
  <a href="#полный-каталог"><img alt="publications" src="https://img.shields.io/badge/publication%20links-786-0d3f35?style=for-the-badge"></a>
  <a href="CONTRIBUTING.md"><img alt="pull requests welcome" src="https://img.shields.io/badge/PRs-welcome-e9b44c?style=for-the-badge"></a>
</p>

</div>

AI Values Atlas — открытая карта исследований ценностей в языковых моделях и
других системах ИИ. Она связывает теории, статьи, бенчмарки, датасеты,
опросники, сценарии, скореры, модели представлений и свидетельства валидности,
не предполагая, что все эти сущности измеряют одно и то же.

> **Главное правило:** ценностная теория — не измерительный инструмент;
> инструмент — не скорер; заявленное одобрение — не выбор; сгенерированный
> текст — не поведение; надёжный профиль не обязательно валиден или специфичен
> для конкретной модели.

Официальные названия публикаций сохранены на языке оригинала. Русифицированы
структура, таксономия, пояснения, фильтры и служебные обозначения каталога.

## Содержание

- [Карта поля](#карта-поля)
- [Что считается аксиологией?](#что-считается-аксиологией)
- [Аксиологические пространства](#аксиологические-пространства)
- [Литература по исследовательским вопросам](#литература-по-исследовательским-вопросам)
- [Датасеты, бенчмарки и инструменты](#датасеты-бенчмарки-и-инструменты)
- [Модели, скореры и инструменты представления](#модели-скореры-и-инструменты-представления)
- [Полный каталог](#полный-каталог)
- [Данные и участие](#данные-и-участие)

## Карта поля

Чтобы корректно сравнивать исследования, необходимо разделять **объект
измерения**, **интерфейс получения свидетельств** и **допустимый вывод**.

| Слой свидетельств | Исследовательский вопрос | Типичный интерфейс | Допустимый вывод |
|---|---|---|---|
| Понимание ценностей | Может ли система распознать ценность или рассуждать о ней? | классификация, аргументы, моральные сценарии | качество распознавания или рассуждения |
| Заявленный профиль | Что модель одобряет при фиксированном протоколе? | PVQ/SVS/WVS, шкалы Лайкерта | профиль одобрения, обусловленный протоколом |
| Конфликтный выбор | Какая ценность побеждает при конфликте мотивов? | вынужденный выбор, ранжирование, пары | приоритет в рамках конкретной задачи |
| Фрейминг в генерации | Какие ценности выражены в открытом тексте? | генерация с последующим маппингом или скорингом | профиль ценностного фрейминга текста |
| Наблюдаемое действие | Какое ценностно значимое поведение возникает в среде? | последовательные решения, игры, инструменты | свидетельства поведения в рамках задачи |
| Внутреннее представление | Где и как закодирована ценностная информация? | пробы, активации, эмбеддинги | репрезентационный или причинный механизм |
| Цель алайнмента | Каким ценностям должна следовать система? | конституции, предпочтения, принципы | нормативная цель или объект управления |
| Валидность измерения | Сохраняется ли результат при разумных изменениях? | промпты, язык, порядок, скорер, нулевые и человеческие проверки | надёжность, перенос, валидность или идентичность |

### Шесть координат для чтения любой статьи

| Координата | Что проверить перед сравнением результатов |
|---|---|
| **Субъект** | Измеряется LLM, агент, пара «модель–язык», корпус генераций или человеческая группа? |
| **Аксиология** | Используется Schwartz, MFT, WVS, индуцированные факторы, латентное пространство, открытый набор или неявная модель? |
| **Инструмент** | Свидетельства получены опросником, сценариями, свободным текстом, выбором, средой или внутренней пробой? |
| **Скорер** | Используются правила, эмбеддинги, классификаторы, LLM-судьи, люди или обученная ценностная модель? |
| **Протокол** | Какие промпт, системный шаблон, язык, порядок, роль, контекст и параметры декодирования фиксируют результат? |
| **Валидация** | Проверены ли надёжность, контрбалансировка, человеческая калибровка, согласие скореров, нули, перенос и пропуски? |

## Что считается аксиологией?

В атласе **аксиология** — общая сущность для представления того, какие ценности
существуют и, при необходимости, как они связаны. Это не означает, что каждое
представление является философской теорией.

| Представление | Пример | Интерпретация |
|---|---|---|
| Именованные измерения | Schwartz-10, Hofstede-6 | фиксированные интерпретируемые координаты |
| Циркумплекс или иерархия | мотивационный круг Schwartz | совместимость и конфликт входят в модель |
| Пространство опросных пунктов | WVS | рабочее пространство определяется банком вопросов |
| Моральная онтология | Moral Foundations Theory | моральные основания, а не универсальный вектор ценностей |
| Набор принципов | HHH, Constitutional AI | нормативные правила или желаемое поведение |
| Индуцированные факторы | GPLA-5 | интерпретируемые факторы из материалов, созданных моделями |
| Латентное представление | UniVaR | плотные ценностные координаты без фиксированных названий |
| Открытое пространство | Generative Psychometrics | ценности задаются во время измерения |
| Без явной модели | многие работы по предпочтениям | ценности используются неявно или не операционализированы |

## Аксиологические пространства

| Аксиология | Форма | Типичное применение в исследованиях ИИ |
|---|---|---|
| [Schwartz Theory of Basic Human Values](https://doi.org/10.1016/S0065-2601(08)60281-6) | 10 ценностей в мотивационном циркумплексе | опросники, сценарии, скоринг текста и конфликты ценностей |
| [Refined Schwartz Theory](https://doi.org/10.1037/a0029393) | 19 базовых ценностей | более детальное профилирование людей и ИИ |
| [Moral Foundations Theory](https://doi.org/10.1037/a0015141) | моральные основания | классификация морального языка и профилирование |
| [World Values Survey](https://www.worldvaluessurvey.org/) | многоязычное пространство опросных пунктов | сравнение людей и ИИ, культурные и политические установки |
| [Hofstede cultural dimensions](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/) | шесть культурных измерений | аудит культурного алайнмента, языка и персон |
| [Value Kaleidoscope](https://doi.org/10.1609/aaai.v38i18.29970) | ценности, права и обязанности | плюралистическое рассуждение и конфликт ценностей |
| [GPLA](https://aclanthology.org/2025.acl-long.585/) | пять индуцированных факторов | построение ИИ-специфичной системы ценностей |
| [UniVaR](https://aclanthology.org/2025.naacl-long.274/) | многомерное латентное представление | эмбеддинги ценностей для пар «модель–язык» |
| [Generative Psychometrics](https://doi.org/10.1609/aaai.v39i25.34839) | открытый набор заданных ценностей | выделение восприятий и скоринг свободных ответов |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | письменная конституция | критика, переписывание и цель алайнмента |

## Литература по исследовательским вопросам

### Обзоры поля

- **A Systematic Review of Psychometric Evaluation of Large Language Models**, 2025 [[статья](https://arxiv.org/abs/2505.08245)]
- **Large Language Models as Mirrors of Human Attitudes, Opinions, and Values**, 2024 [[статья](https://aclanthology.org/2024.findings-emnlp.513/)]
- **Human Values and Alignment in Artificial Intelligence: A Survey**, 2024 [[статья](https://arxiv.org/abs/2404.10636)]
- **Awesome LLM Values and Pluralistic Alignment** [[каталог](https://github.com/AIDASLab/Awesome-LLM-Values-and-Pluralistic-Alignment)]
- **Awesome LLM Psychometrics** [[каталог](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)]

### Опросники и заявленные профили

- **Who is GPT-3? An Exploration of Personality, Values and Demographics**, 2022 [[статья](https://aclanthology.org/2022.nlpcss-1.24/)] — раннее профилирование с помощью опросников
- **Do LLMs Have Consistent Values?**, 2025 [[статья](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)] — согласованность между условиями элиситации
- **Value Portrait**, 2025 [[статья](https://aclanthology.org/2025.acl-long.838/)] — ситуационные психометрические пункты

### Понимание ценностей и бенчмарки

- **Aligning AI With Shared Human Values**, 2021 [[статья](https://openreview.net/forum?id=dNy_RKzJacY)] — ETHICS
- **Social Chemistry 101**, 2020 [[статья](https://aclanthology.org/2020.emnlp-main.48/)] — социальные и моральные нормы
- **ValueBench**, 2024 [[статья](https://aclanthology.org/2024.acl-long.111/)] — ориентация и понимание ценностей
- **WorldValuesBench**, 2024 [[статья](https://aclanthology.org/2024.lrec-main.1539/)] — мультикультурная осведомлённость

### Ценности в сгенерированном тексте

- **Value FULCRA**, 2024 [[статья](https://aclanthology.org/2024.naacl-long.486/)] — маппинг полной генерации в профиль Schwartz
- **Measuring Human and AI Values Based on Generative Psychometrics**, 2025 [[статья](https://doi.org/10.1609/aaai.v39i25.34839)] — выделение утверждений и скоринг заданных ценностей
- **CLAVE**, 2024 [[статья](https://arxiv.org/abs/2407.10725)] — оценка сгенерированных ответов без эталона

### Выбор, действие и разрывы между интерфейсами

- **What's the Most Important Value? INVP**, 2025 [[статья](https://aclanthology.org/2025.coling-main.317/)] — приоритеты в социальных сценариях
- **Mind the Value–Action Gap**, 2025 [[статья](https://aclanthology.org/2025.emnlp-main.154/)] — заявленные склонности и действие
- **Are the Values of LLMs Structurally Aligned with Humans?**, 2025 [[статья](https://aclanthology.org/2025.findings-acl.1188/)] — структурный и причинный анализ

### Культура, язык и плюрализм

- **Ethical Reasoning and Moral Value Alignment Depend on the Language We Prompt In**, 2024 [[статья](https://arxiv.org/abs/2404.18460)]
- **Cultural Bias and Cultural Alignment of Large Language Models**, 2024 [[статья](https://doi.org/10.1093/pnasnexus/pgae346)]
- **Break the Checkbox**, 2025 [[статья](https://aclanthology.org/2025.emnlp-main.2/)]

### Представления, внутренние механизмы и управление

- **GPLA**, 2025 [[статья](https://aclanthology.org/2025.acl-long.585/)] — интерпретируемые ИИ-специфичные факторы
- **UniVaR**, 2025 [[статья](https://aclanthology.org/2025.naacl-long.274/)] — плотное представление для модели и языка
- **Internal Value Alignment through Controlled Value Vector Activation**, 2025 [[статья](https://aclanthology.org/2025.acl-long.1326/)] — интервенции в активации

### Надёжность, валидность и отчётность

- **Measurement and Fairness**, 2021 [[статья](https://doi.org/10.1145/3442188.3445901)] — конструкты, операционализация и валидность
- **POSIX: A Prompt Sensitivity Index for Large Language Models**, 2024 [[статья](https://arxiv.org/abs/2410.02185)] — чувствительность к промптам
- **Large Language Models Are Not Fair Evaluators**, 2024 [[статья](https://aclanthology.org/2024.acl-long.511/)] — позиционные и оценочные смещения

## Датасеты, бенчмарки и инструменты

| Ресурс | Тип | Пространство или конструкт | Ссылка |
|---|---|---|---|
| Value Portrait | банк ситуаций | Schwartz-10 | [статья](https://aclanthology.org/2025.acl-long.838/) |
| ValueBench | бенчмарк и код | ориентация и понимание ценностей | [статья](https://aclanthology.org/2024.acl-long.111/) · [код](https://github.com/Value4AI/ValueBench) |
| WorldValuesBench | многоязычный бенчмарк | культурные ценности | [статья](https://aclanthology.org/2024.lrec-main.1539/) |
| ValueNet | датасет | ценности Schwartz в диалоге | [данные](https://liang-qiu.github.io/ValueNet/) |
| Value FULCRA | корпус и измерительный пайплайн | профили сгенерированного текста | [статья](https://aclanthology.org/2024.naacl-long.486/) |
| ETHICS | набор бенчмарков | справедливость, добродетель, деонтология | [статья](https://openreview.net/forum?id=dNy_RKzJacY) |
| World Values Survey | опрос и микроданные | пункты опроса и культурные измерения | [проект](https://www.worldvaluessurvey.org/) |

## Модели, скореры и инструменты представления

Это вычислительные компоненты, а не теории ценностей. Их выход имеет смысл
только вместе с промптом, единицей входа, ценностным пространством, правилами
агрегации, покрытием и свидетельствами валидности.

| Инструмент | Роль | Выход | Ссылка |
|---|---|---|---|
| ValueLlama-3-8B | скорер открытых ответов | релевантность и направленность по заданной ценности | [модель](https://huggingface.co/Value4AI/ValueLlama-3-8B) |
| UniVaR lambda-1 | энкодер ценностных представлений | плотное представление пары «модель–язык» | [модель](https://huggingface.co/CAiRE/UniVaR-lambda-1) · [код](https://github.com/HLTCHKUST/UniVaR) |
| MoralBERT | классификатор Moral Foundations | метки или сигналы моральных оснований | [код](https://github.com/vjosapreniqi/MoralBERT) |
| FULCRA | пайплайн маппинга генераций | многомерный профиль базовых ценностей | [статья](https://aclanthology.org/2024.naacl-long.486/) |

## Полный каталог

Ниже приведён каждый уникальный URL репозитория. Публикации сгруппированы по
исследовательским направлениям; для данных, моделей, кода, проектов и опросных
ресурсов выделены отдельные разделы. Все записи видимы и доступны для поиска
прямо на GitHub.

<!-- complete-catalog:start -->

> Раздел генерируется из дедуплицированного индекса. Каждый URL приведён
> ровно один раз; для записи сохранены тематический охват и происхождение.

**Навигация по таксономии**

| Направление | Публикации |
|---|---:|
| [🗺️ Обзоры и карты исследовательского поля](#catalog-surveys-reviews-and-field-overviews) | 49 |
| [🧭 Основания и теории ценностей](#catalog-foundations-and-value-theory) | 7 |
| [🗂️ Датасеты и бенчмарки](#catalog-datasets-and-benchmarks) | 103 |
| [🔬 Надёжность, валидность и аудит](#catalog-reliability-validity-and-auditing) | 17 |
| [🎯 Выбор, действие и поведенческая согласованность](#catalog-choice-action-and-behavioral-consistency) | 15 |
| [🌍 Культура, язык и плюрализм](#catalog-culture-language-and-pluralism) | 103 |
| [🗣️ Предпочтения, мнения и социальные симуляции](#catalog-preferences-opinions-and-social-simulation) | 120 |
| [⚖️ Моральное рассуждение и понимание ценностей](#catalog-moral-reasoning-and-value-understanding) | 63 |
| [🧰 Алайнмент, управление и предпочтения](#catalog-alignment-steering-and-preferences) | 133 |
| [📐 Представления ценностей и внутренние механизмы моделей](#catalog-value-representation-and-model-internals) | 44 |
| [📏 Измерение и профилирование](#catalog-measurement-and-profiling) | 87 |
| [📎 Другие и смежные исследования ценностей](#catalog-other-and-adjacent-value-research) | 45 |

> **Легенда:** `ядро` — работа непосредственно о ценностях; `смежная тема` — более широкий контекст. После ссылки указаны каталоги-источники.

### 📚 Публикации по направлениям

<a id="catalog-surveys-reviews-and-field-overviews"></a>

#### 🗺️ Обзоры и карты исследовательского поля · 49

- **A roadmap for evaluating moral competence in large language models**, 2026 — [[статья](https://nature.com/articles/s41586-025-10021-1)] · ядро · источник: AIDAS Values & Pluralism
- **A Survey of Progress in LLM Alignment from the Perspective of Reward Design**, 2026 — [[статья](https://ieeexplore.ieee.org/abstract/document/11361384)] · ядро · источник: Pluralistic Alignment
- **A Survey on Evaluation of Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2307.03109)] · смежная тема · источник: LLM Social Science
- **A Survey on Human-Centric LLMs**, 2024 — [[статья](https://arxiv.org/abs/2411.14491)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **A Survey on Large Language Model based Autonomous Agents**, 2023 — [[статья](https://arxiv.org/abs/2308.11432)] · смежная тема · источник: LLM Social Science
- **A Survey on Personalized Alignment -- The Missing Piece for Large Language Models in Real-World Applications**, 2025 — [[статья](https://arxiv.org/abs/2503.17003)] · смежная тема · источник: Personalized Alignment
- **A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2504.07070)] · ядро · источник: AIDAS Values & Pluralism, Personalized Alignment, Pluralistic Alignment
- **AI Alignment and Social Choice: Fundamental Limitations and Policy Implications**, 2023 — [[статья](https://arxiv.org/abs/2310.16048)] · ядро · источник: AIDAS Values & Pluralism
- **AI Alignment From Social Choice Perspectives**, 2026 — [[статья](https://arxiv.org/abs/2606.21550)] · ядро · источник: AIDAS Values & Pluralism
- **AI Alignment: A Comprehensive Survey**, 2023 — [[статья](https://arxiv.org/abs/2310.19852)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Aligning Large Language Models with Human: A Survey**, 2023 — [[статья](https://arxiv.org/abs/2307.12966)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Beyond Benchmark: LLMs Evaluation with an Anthropomorphic and Value-oriented Roadmap**, 2025 — [[статья](https://arxiv.org/abs/2508.18646)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Bias and Cultural Alignment of Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2311.14096)] · ядро · источник: AIDAS Values & Pluralism
- **Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation**, 2025 — [[статья](https://arxiv.org/abs/2509.08858)] · ядро · источник: AIDAS Values & Pluralism
- **Decoding Alignment: A Critical Survey of LLM Development Initiatives through Value-setting and Data-centric Lens**, 2025 — [[статья](https://arxiv.org/abs/2508.16982)] · ядро · источник: AIDAS Values & Pluralism
- **From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents**, 2024 — [[статья](https://arxiv.org/abs/2412.03563)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **From Instructions to Intrinsic Human Values -- A Survey of Alignment Goals for Big Models**, 2023 — [[статья](https://arxiv.org/abs/2308.12014)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications**, 2025 — [[статья](https://arxiv.org/abs/2505.00049)] · ядро · источник: LLM Psychometrics
- **Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges**, 2025 — [[статья](https://arxiv.org/abs/2507.19364)] · ядро · источник: AIDAS Values & Pluralism
- **Large Language Model based Multi-Agents: A Survey of Progress and Challenges**, 2024 — [[статья](https://arxiv.org/abs/2402.01680)] · смежная тема · источник: LLM Social Science
- **Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**, 2025 — [[статья](https://arxiv.org/abs/2505.08245)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Large language models empowered agent-based modeling and simulation: a survey and perspectives**, 2024 — [[статья](https://nature.com/articles/s41599-024-03611-3)] · ядро · источник: AIDAS Values & Pluralism
- **Large Language Models Should Learn Personalized Rather Than Aggregated Human Preferences**, 2026 — [[статья](https://arxiv.org/abs/2606.07629)] · ядро · источник: AIDAS Values & Pluralism
- **LLM Alignment should go beyond Harmlessness–Helpfulness and incorporate Human Agency**, 2026 — [[статья](https://link.springer.com/article/10.1007/s12559-026-10568-9)] · ядро · источник: AIDAS Values & Pluralism
- **LLM Social Simulations Are a Promising Research Method**, 2025 — [[статья](https://arxiv.org/abs/2504.02234)] · ядро · источник: AIDAS Values & Pluralism
- **LLM-Based Social Simulations Require a Boundary**, 2025 — [[статья](https://arxiv.org/abs/2506.19806)] · ядро · источник: AIDAS Values & Pluralism
- **LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods**, 2024 — [[статья](https://arxiv.org/abs/2412.05579)] · смежная тема · источник: LLM Social Science
- **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs**, 2025 — [[статья](https://aclanthology.org/2025.findings-acl.1246/)] · смежная тема · источник: LLM Social Science
- **Missing the Margins: A Systematic Literature Review on the Demographic Representativeness of LLMs**, 2025 — [[статья](https://arxiv.org/abs/2511.01864)] · ядро · источник: AIDAS Values & Pluralism
- **Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and Alignment**, 2026 — [[статья](https://arxiv.org/abs/2602.03003)] · ядро · источник: AIDAS Values & Pluralism
- **Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior**, 2025 — [[статья](https://arxiv.org/abs/2511.14476)] · ядро · источник: AIDAS Values & Pluralism
- **Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models with personalised feedback**, 2023 — [[статья](https://arxiv.org/abs/2303.05453)] · ядро · источник: AIDAS Values & Pluralism
- **Personalization of Large Language Models: A Survey**, 2024 — [[статья](https://arxiv.org/abs/2411.00027)] · ядро · источник: Personalized Alignment, Pluralistic Alignment
- **Personalized Multimodal Large Language Models: A Survey**, 2024 — [[статья](https://arxiv.org/abs/2412.02142)] · смежная тема · источник: Personalized Alignment
- **Position: A Roadmap to Pluralistic Alignment**, 2024 — [[статья](https://openreview.net/forum?id=gQpBnRHwxM)] · смежная тема · источник: Personalized Alignment
- **Position: AI Agents Are Not (Yet) a Panacea for Social Simulation**, 2026 — [[статья](https://arxiv.org/abs/2603.00113)] · ядро · источник: AIDAS Values & Pluralism
- **Position: Towards Bidirectional Human-AI Alignment**, 2024 — [[статья](https://arxiv.org/abs/2406.09264)] · ядро · источник: AIDAS Values & Pluralism
- **Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations**, 2024 — [[статья](https://aclanthology.org/2024.lrec-main.1192/)] · смежная тема · источник: Personalized Alignment
- **Simulating Society Requires Simulating Thought**, 2025 — [[статья](https://arxiv.org/abs/2506.06958)] · ядро · источник: AIDAS Values & Pluralism
- **Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback**, 2024 — [[статья](https://arxiv.org/abs/2404.10271)] · ядро · источник: AIDAS Values & Pluralism
- **Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits**, 2026 — [[статья](https://arxiv.org/abs/2605.18890)] · ядро · источник: AIDAS Values & Pluralism
- **The benefits, risks and bounds of personalizing the alignment of large language models to individuals**, 2024 — [[статья](https://nature.com/articles/s42256-024-00820-y)] · смежная тема · источник: Personalized Alignment
- **The Mind in the Machine: A Survey of Incorporating Psychological Theories in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2505.00003)] · ядро · источник: LLM Psychometrics
- **The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm**, 2024 — [[статья](https://arxiv.org/abs/2406.18682)] · смежная тема · источник: Personalized Alignment
- **The Road to Artificial SuperIntelligence: A Comprehensive Survey of Superalignment**, 2024 — [[статья](https://arxiv.org/abs/2412.16468)] · смежная тема · источник: LLM Social Science
- **The threat of analytic flexibility in using large language models to simulate human data: A call to attention**, 2025 — [[статья](https://arxiv.org/abs/2509.13397)] · ядро · источник: AIDAS Values & Pluralism
- **Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents**, 2025 — [[статья](https://arxiv.org/abs/2503.24047)] · смежная тема · источник: LLM Social Science
- **Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization**, 2024 — [[статья](https://aclanthology.org/2024.findings-emnlp.969/)] · смежная тема · источник: Personalized Alignment
- **When large language models meet personalization: perspectives of challenges and opportunities**, 2024 — [[статья](https://doi.org/10.1007/s11280-024-01276-1)] · смежная тема · источник: Personalized Alignment

<a id="catalog-foundations-and-value-theory"></a>

#### 🧭 Основания и теории ценностей · 7

- **Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz's Theory of Basic Values**, 2024 — [[статья](https://doi.org/10.2196/55988)] · ядро · источник: STONIC bibliography
- **Axioms for AI Alignment from Human Feedback**, 2024 — [[статья](https://arxiv.org/abs/2405.14758)] · ядро · источник: AIDAS Values & Pluralism
- **Extending the Cross-Cultural Validity of the Theory of Basic Human Values with a Different Method of Measurement**, 2001 — [[статья](https://doi.org/10.1177/0022022101032005001)] · ядро · источник: STONIC bibliography
- **Moral foundations theory: The pragmatic validity of moral pluralism. Graham et al. Advances in experimental social psychology, 2013.**, 2013 — [[статья](https://sciencedirect.com/science/article/abs/pii/B9780124072367000024)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **Optimized Distortion in Linear Social Choice**, 2025 — [[статья](https://arxiv.org/abs/2510.20020)] · ядро · источник: AIDAS Values & Pluralism
- **Representative Social Choice: From Learning Theory to AI Alignment**, 2024 — [[статья](https://arxiv.org/abs/2410.23953)] · ядро · источник: AIDAS Values & Pluralism
- **Strategy-proofness and Arrow's Conditions**, 1975 — [[статья](https://sciencedirect.com/science/article/pii/0022053175900502)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-datasets-and-benchmarks"></a>

#### 🗂️ Датасеты и бенчмарки · 103

- **(ETHICS) Aligning AI With Shared Human Values**, 2020 — [[статья](https://arxiv.org/abs/2008.02275)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **(MoralChoice) Evaluating the Moral Beliefs Encoded in LLMs**, 2023 — [[статья](https://arxiv.org/abs/2307.14324)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **(NYTBookOpinions) Benchmarking Distributional Alignment of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2411.05403)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **(Valueeval) The Touché23-ValueEval Dataset for Identifying Human Values behind Arguments**, 2023 — [[статья](https://arxiv.org/abs/2301.13771)] · ядро · источник: AIDAS Values & Pluralism
- **A Sociotechnical Perspective on Aligning AI with Pluralistic Human Values**, 2025 — [[статья](https://openreview.net/forum?id=oSRqZO2O2O)] · ядро · источник: Pluralistic Alignment
- **A Unified Moral-Value Dataset for Instruction Tuning**, 2026 — [[статья](https://arxiv.org/abs/2607.21279)] · ядро · источник: AIDAS Values & Pluralism
- **Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts**, 2023 — [[статья](https://arxiv.org/abs/2305.13300)] · ядро · источник: Pluralistic Alignment
- **Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values**, 2026 — [[статья](https://arxiv.org/abs/2605.10365)] · ядро · источник: AIDAS Values & Pluralism
- **An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance**, 2024 — [[статья](https://arxiv.org/abs/2404.01247)] · смежная тема · источник: Awesome Cultural NLP
- **Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral**, 2025 — [[статья](https://arxiv.org/abs/2502.14083)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models, NeurIPS 2024**, 2024 — [[статья](https://arxiv.org/abs/2402.11894)] · смежная тема · источник: LLM Social Science
- **BBQ: A hand-built bias benchmark for question answering**, 2022 — [[статья](https://aclanthology.org/2022.findings-acl.165/)] · ядро · источник: STONIC bibliography
- **Benchmarking Distributional Alignment of Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.2/)] · ядро · источник: Pluralistic Alignment
- **Benchmarking Multi-National Value Alignment for Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2504.12911)] · смежная тема · источник: LLM Social Science
- **Benchmarking Overton Pluralism in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2512.01351)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **Beyond Aesthetics: Cultural Competence in Text-to-Image Models**, 2024 — [[статья](https://arxiv.org/abs/2407.06863)] · смежная тема · источник: Awesome Cultural NLP
- **Big-Math 2025-2**, 2025 — [[статья](https://arxiv.org/abs/2502.17387)] · смежная тема · источник: Awesome LLM Datasets
- **Bridging Cultural Nuances in Dialogue Agents through Cultural Value Surveys**, 2024 — [[статья](https://arxiv.org/abs/2401.10352)] · смежная тема · источник: Awesome Cultural NLP
- **C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2506.01495)] · ядро · источник: AIDAS Values & Pluralism
- **Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs**, 2025 — [[статья](https://arxiv.org/abs/2510.05154)] · ядро · источник: AIDAS Values & Pluralism
- **Can Language Models Reason about Individualistic Human Values and Preferences?**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.336/)] · ядро · источник: Pluralistic Alignment
- **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2405.13974)] · ядро · источник: AIDAS Values & Pluralism
- **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models**, 2024 — [[статья](https://ojs.aaai.org/index.php/AIES/article/view/31710)] · ядро · источник: Pluralistic Alignment
- **CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives**, 2025 — [[статья](https://arxiv.org/abs/2504.10823)] · ядро · источник: AIDAS Values & Pluralism
- **CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean**, 2024 — [[статья](https://arxiv.org/abs/2403.06412)] · смежная тема · источник: Awesome Cultural NLP
- **COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values**, 2025 — [[статья](https://arxiv.org/abs/2504.05535)] · смежная тема · источник: LLM Social Science
- **ComPO: Community Preferences for Language Model Personalization**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.419/)] · ядро · источник: Pluralistic Alignment
- **Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024**, 2024 — [[статья](https://dl.acm.org/doi/pdf/10.1145/3627673.3679768)] · смежная тема · источник: LLM Social Science
- **Culturally Aware Natural Language Inference**, 2023 — [[статья](https://aclanthology.org/2023.findings-emnlp.509/)] · смежная тема · источник: Awesome Cultural NLP
- **D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios**, 2026 — [[статья](https://arxiv.org/abs/2607.19834)] · ядро · источник: AIDAS Values & Pluralism
- **Datasheets for datasets**, 2021 — [[статья](https://doi.org/10.1145/3458723)] · ядро · источник: STONIC bibliography
- **DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context**, 2025 — [[статья](https://arxiv.org/abs/2509.17399)] · смежная тема · источник: Awesome Cultural NLP
- **DOSA: A Dataset of Social Artifacts from Different Indian Geographical Subcultures**, 2024 — [[статья](https://arxiv.org/abs/2403.14651)] · смежная тема · источник: Awesome Cultural NLP
- **EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English**, 2022 — [[статья](https://arxiv.org/abs/2203.14498)] · смежная тема · источник: Awesome Cultural NLP
- **Evaluating and Inducing Personality in Pre-trained Language Models**, 2022 — [[статья](https://arxiv.org/abs/2206.07550)] · ядро · источник: Pluralistic Alignment
- **Evaluating the Prompt Steerability of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2411.12405)] · ядро · источник: AIDAS Values & Pluralism
- **EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences**, 2025 — [[статья](https://arxiv.org/abs/2510.06370)] · ядро · источник: Pluralistic Alignment
- **Event-Centric Human Value Understanding in News-Domain Texts: An Actor-Conditioned, Multi-Granularity Benchmark**, 2026 — [[статья](https://arxiv.org/abs/2603.17838)] · ядро · источник: AIDAS Values & Pluralism
- **Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis**, 2024 — [[статья](https://arxiv.org/abs/2308.16705)] · смежная тема · источник: Awesome Cultural NLP
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-main.1063/)] · смежная тема · источник: Awesome Cultural NLP
- **FORK: A Bite-Sized Test Set for Probing Culinary Cultural Biases in Commonsense Reasoning Models**, 2023 — [[статья](https://aclanthology.org/2023.findings-acl.631/)] · смежная тема · источник: Awesome Cultural NLP
- **GeoDE: a Geographically Diverse Evaluation Dataset for Object Recognition**, 2023 — [[статья](https://arxiv.org/abs/2301.02560)] · смежная тема · источник: Awesome Cultural NLP
- **GIMMICK -- Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking**, 2025 — [[статья](https://arxiv.org/abs/2502.13766)] · смежная тема · источник: Awesome Cultural NLP
- **Global Voices, Local Biases: Socio-Cultural Prejudices across Languages**, 2023 — [[статья](https://arxiv.org/abs/2310.17586)] · смежная тема · источник: Awesome Cultural NLP
- **HATEDAY: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter, ACL 2025 Outstanding Paper**, 2025 — [[статья](https://arxiv.org/abs/2411.15462)] · смежная тема · источник: LLM Social Science
- **HelpSteer 2: Open-source dataset for training top-performing reward models**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/02fd91a387a6a5a5751e81b58a75af90-Abstract-Datasets_and_Benchmarks_Track.html)] · ядро · источник: Pluralistic Alignment
- **KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge**, 2024 — [[статья](https://aclanthology.org/2024.findings-acl.666/)] · ядро · источник: Pluralistic Alignment
- **LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces**, 2025 — [[статья](https://arxiv.org/abs/2503.01894)] · ядро · источник: Pluralistic Alignment
- **LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2505.00853)] · ядро · источник: AIDAS Values & Pluralism
- **M5 -- A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks**, 2024 — [[статья](https://arxiv.org/abs/2407.03791)] · смежная тема · источник: Awesome Cultural NLP
- **Massively Multi-Cultural Knowledge Acquisition & LM Benchmarking**, 2024 — [[статья](https://arxiv.org/abs/2402.09369)] · смежная тема · источник: Awesome Cultural NLP
- **MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation**, 2025 — [[статья](https://arxiv.org/abs/2506.19073)] · ядро · источник: AIDAS Values & Pluralism
- **MID-Space: Aligning Diverse Communities' Needs to Inclusive Public Spaces**, 2024 — [[статья](https://openreview.net/forum?id=kyfkMRT4Ao)] · ядро · источник: Pluralistic Alignment
- **Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment**, 2020 — [[статья](https://journals.sagepub.com/doi/10.1177/1948550619876629)] · ядро · источник: AIDAS Values & Pluralism
- **Moral foundations twitter corpus: A collection of 35k tweets annotated for moral sentiment. Hoover et al. Social Psychological and Personality Science 2020.**, 2020 — [[статья](https://journals.sagepub.com/doi/epub/10.1177/1948550619876629)] · ядро · источник: Alignment Goal Survey
- **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences**, 2020 — [[статья](https://arxiv.org/abs/2012.15738)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey
- **MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes**, 2025 — [[статья](https://arxiv.org/abs/2510.16380)] · ядро · источник: AIDAS Values & Pluralism
- **Multi-lingual and Multi-cultural Figurative Language Understanding**, 2023 — [[статья](https://arxiv.org/abs/2305.16171)] · смежная тема · источник: Awesome Cultural NLP
- **Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision-Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.490/)] · смежная тема · источник: Awesome Cultural NLP
- **Navigating the Cultural Kaleidoscope: A Hitchhiker’s Guide to Sensitivity in Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.388/)] · ядро · источник: Pluralistic Alignment
- **NLPositionality: Characterizing Design Biases of Datasets and Models**, 2023 — [[статья](https://aclanthology.org/2023.acl-long.505/)] · смежная тема · источник: Awesome Cultural NLP
- **NormBank: A Knowledge Bank of Situational Social Norms**, 2023 — [[статья](https://aclanthology.org/2023.acl-long.429/)] · ядро · источник: Pluralistic Alignment
- **NormBank: A Knowledge Bank of Situational Social Norms**, 2023 — [[статья](https://arxiv.org/abs/2305.17008)] · ядро · источник: AIDAS Values & Pluralism
- **NormSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly**, 2023 — [[статья](https://arxiv.org/abs/2210.08604)] · смежная тема · источник: Awesome Cultural NLP
- **NoveltyBench: Evaluating Language Models for Humanlike Diversity**, 2025 — [[статья](https://arxiv.org/abs/2504.05228)] · ядро · источник: Pluralistic Alignment
- **PerSpectra: A Scalable and Configurable Pluralist Benchmark of Perspectives from Arguments**, 2026 — [[статья](https://arxiv.org/abs/2602.08716)] · ядро · источник: AIDAS Values & Pluralism
- **PLURAL: A Global Dataset for Value Alignment**, 2026 — [[статья](https://arxiv.org/abs/2607.08034)] · ядро · источник: AIDAS Values & Pluralism
- **PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm**, 2026 — [[статья](https://arxiv.org/abs/2601.08951)] · ядро · источник: Pluralistic Alignment
- **Polar: A Benchmark for Evaluating Political Bias in LLMs**, 2026 — [[статья](https://arxiv.org/abs/2606.12922)] · ядро · источник: AIDAS Values & Pluralism
- **Process for adapting language models to society (palms) with values-targeted datasets. Solaiman et al. Neurips 2021.**, 2021 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2021/file/2e855f9489df0712b4bd8ea9e2848c5a-Paper.pdf)] · ядро · источник: Alignment Goal Survey
- **ProsocialDialog: A Prosocial Backbone for Conversational Agents**, 2022 — [[статья](https://arxiv.org/abs/2205.12688)] · ядро · источник: AIDAS Values & Pluralism
- **Re-contextualizing Fairness in NLP: The Case of India**, 2022 — [[статья](https://arxiv.org/abs/2209.12226)] · смежная тема · источник: Awesome Cultural NLP
- **RENOVI: A Benchmark Towards Remediating Norm Violations in Socio-Cultural Conversations**, 2024 — [[статья](https://aclanthology.org/2024.findings-naacl.196/)] · смежная тема · источник: Awesome Cultural NLP
- **SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.**, 2022 — [[статья](https://arxiv.org/abs/2210.10045)] · ядро · источник: Alignment Goal Survey
- **SafeWorld: Geo-Diverse Safety Alignment**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e8aad0aaa1309659a7d7e4c21202d9d0-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes**, 2020 — [[статья](https://arxiv.org/abs/2008.09094)] · ядро · источник: AIDAS Values & Pluralism, Awesome LLM Safety
- **Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.**, 2021 — [[статья](https://ojs.aaai.org/index.php/AAAI/article/view/17589/17396)] · ядро · источник: Alignment Goal Survey
- **SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models**, 2023 — [[статья](https://arxiv.org/abs/2305.11840)] · смежная тема · источник: Awesome Cultural NLP
- **Social Chemistry 101: Learning to Reason about Social and Moral Norms**, 2020 — [[статья](https://arxiv.org/abs/2011.00620)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **SocialDial: A Benchmark for Socially-Aware Dialogue Systems**, 2023 — [[статья](https://dl.acm.org/doi/10.1145/3539618.3591877)] · смежная тема · источник: Awesome Cultural NLP
- **STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2505.20645)] · ядро · источник: AIDAS Values & Pluralism
- **The Moral Foundations Reddit Corpus**, 2022 — [[статья](https://arxiv.org/abs/2208.05545)] · ядро · источник: AIDAS Values & Pluralism, Awesome LLM Safety
- **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems**, 2022 — [[статья](https://aclanthology.org/2022.acl-long.261/)] · ядро · источник: Pluralistic Alignment
- **The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems**, 2022 — [[статья](https://arxiv.org/abs/2204.03021)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome LLM Safety
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/be2e1b68b44f2419e19f6c35a1b8cf35-Abstract-Datasets_and_Benchmarks_Track.html)] · ядро · источник: Pluralistic Alignment
- **Towards Cross-lingual Values Judgment: A Consensus-Pluralism Perspective**, 2026 — [[статья](https://arxiv.org/abs/2602.17283)] · ядро · источник: AIDAS Values & Pluralism
- **VAL-Bench: Belief Consistency as a measure for Value Alignment in Language Models**, 2025 — [[статья](https://arxiv.org/abs/2510.05465)] · ядро · источник: AIDAS Values & Pluralism
- **Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation**, 2025 — [[статья](https://aclanthology.org/2025.acl-demo.64/)] · ядро · источник: STONIC bibliography
- **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.111/)] · ядро · источник: Pluralistic Alignment, STONIC bibliography
- **ValueNet: A New Dataset for Human Value Driven Dialogue System**, 2022 — [[статья](https://doi.org/10.1609/aaai.v36i10.21368)] · ядро · источник: STONIC bibliography
- **ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022**, 2022 — [[статья](https://ojs.aaai.org/index.php/AAAI/article/view/21368)] · смежная тема · источник: LLM Social Science
- **Valuenet: A new dataset for human value driven dialogue system. Qiu et al. AAAI 2022.**, 2022 — [[статья](https://ojs.aaai.org/index.php/AAAI/article/download/21368/21117)] · ядро · источник: Alignment Goal Survey
- **Vision-Language Models under Cultural and Inclusive Considerations**, 2024 — [[статья](https://arxiv.org/abs/2407.06177)] · смежная тема · источник: Awesome Cultural NLP
- **Visually Grounded Reasoning across Languages and Cultures**, 2021 — [[статья](https://arxiv.org/abs/2109.13238)] · смежная тема · источник: Awesome Cultural NLP
- **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1119/)] · ядро · источник: Pluralistic Alignment
- **VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare**, 2025 — [[статья](https://arxiv.org/abs/2502.13775)] · ядро · источник: AIDAS Values & Pluralism
- **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses**, 2026 — [[статья](https://arxiv.org/abs/2607.26348)] · ядро · источник: AIDAS Values & Pluralism
- **Whose Opinions Do Language Models Reflect?**, 2023 — [[статья](https://arxiv.org/abs/2303.17548)] · ядро · источник: Pluralistic Alignment
- **Whose View of Safety? A Deep DIVE Dataset for Pluralistic Alignment of Text-to-Image Models**, 2025 — [[статья](https://arxiv.org/abs/2507.13383)] · ядро · источник: Pluralistic Alignment
- **WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines**, 2024 — [[статья](https://arxiv.org/abs/2410.12705)] · смежная тема · источник: Awesome Cultural NLP
- **WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models**, 2024 — [[статья](https://aclanthology.org/2024.lrec-main.1539/)] · ядро · источник: STONIC bibliography
- **Would you Rather? A New Benchmark for Learning Machine Alignment with Cultural Values and Social Preferences**, 2020 — [[статья](https://aclanthology.org/2020.acl-main.477/)] · смежная тема · источник: Awesome Cultural NLP
- **XCR-Bench: Benchmarking Cross-Cultural Reasoning in LLMs via Culture-Specific Items and Hall's Triad**, 2026 — [[статья](https://arxiv.org/abs/2601.14063)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-reliability-validity-and-auditing"></a>

#### 🔬 Надёжность, валидность и аудит · 17

- **A large-scale replication of scenario-based experiments in psychology and management using large language models, 2025.08, Nature Computational Science**, 2025 — [[статья](https://nature.com/articles/s43588-025-00840-7)] · ядро · источник: LLM Psychometrics
- **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, 2025.07, ACL 2025 Best Paper**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1454/)] · ядро · источник: LLM Psychometrics
- **A validity-guided workflow for robust large language model research in psychology**, 2025 — [[статья](https://arxiv.org/abs/2507.04491)] · ядро · источник: LLM Psychometrics
- **Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents**, 2026 — [[статья](https://arxiv.org/abs/2602.18462)] · ядро · источник: AIDAS Values & Pluralism
- **Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing**, 2020 — [[статья](https://doi.org/10.1145/3351095.3372873)] · ядро · источник: STONIC bibliography
- **Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality**, 2025 — [[статья](https://arxiv.org/abs/2510.11254)] · ядро · источник: LLM Psychometrics
- **EASE Configuration Facilitates A Reproducible Science of LLM Social Simulations**, 2026 — [[статья](https://arxiv.org/abs/2605.30258)] · ядро · источник: AIDAS Values & Pluralism
- **From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology**, 2025 — [[статья](https://arxiv.org/abs/2506.16697)] · ядро · источник: LLM Psychometrics
- **Large Language Models are not Fair Evaluators**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.511/)] · ядро · источник: STONIC bibliography
- **Large language models that replace human participants can harmfully misportray and flatten identity groups, 2025.03, Nature Machine Intelligence**, 2025 — [[статья](https://nature.com/articles/s42256-025-00986-z)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **Larger and more instructable language models become less reliable, 2024.10, Nature**, 2024 — [[статья](https://nature.com/articles/s41586-024-07930-y)] · ядро · источник: LLM Psychometrics
- **Model Cards for Model Reporting**, 2019 — [[статья](https://doi.org/10.1145/3287560.3287596)] · ядро · источник: STONIC bibliography
- **Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History**, 2025 — [[статья](https://arxiv.org/abs/2508.04826)] · ядро · источник: LLM Psychometrics
- **POSIX: A Prompt Sensitivity Index For Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2410.02185)] · ядро · источник: STONIC bibliography
- **Psychometric item validation using virtual respondents with trait-response mediators**, 2025 — [[статья](https://arxiv.org/abs/2507.05890)] · ядро · источник: LLM Psychometrics
- **Revisiting the Reliability of Psychological Scales on Large Language Models, EMNLP 2024**, 2024 — [[статья](https://arxiv.org/abs/2305.19926)] · ядро · источник: LLM Psychometrics
- **You don't need a personality test to know these models are unreliable: Assessing the Reliability of Large Language Models on Psychometric Instruments, NAACL 2024**, 2024 — [[статья](https://arxiv.org/abs/2311.09718)] · ядро · источник: LLM Psychometrics

<a id="catalog-choice-action-and-behavioral-consistency"></a>

#### 🎯 Выбор, действие и поведенческая согласованность · 15

- **\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms**, 2023 — [[статья](https://arxiv.org/abs/2312.15907)] · смежная тема · источник: Awesome LLM Safety, LLM Social Science
- **Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents**, 2026 — [[статья](https://arxiv.org/abs/2604.27699)] · ядро · источник: AIDAS Values & Pluralism
- **How developments in natural language processing help us in understanding human behaviour, 2024.10 Nature Human Behavior**, 2024 — [[статья](https://nature.com/articles/s41562-024-01938-0.pdf)] · смежная тема · источник: LLM Social Science
- **How large language models can reshape collective intelligence, 2024.09, Nature Human Behavior**, 2024 — [[статья](https://nature.com/articles/s41562-024-01959-9)] · смежная тема · источник: LLM Social Science
- **Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations, EMNLP 2025**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.1562/)] · смежная тема · источник: LLM Social Science
- **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.154/)] · ядро · источник: STONIC bibliography
- **Pluralistic Behavior Suite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies**, 2025 — [[статья](https://arxiv.org/abs/2511.05018)] · ядро · источник: AIDAS Values & Pluralism
- **Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned**, 2022 — [[статья](https://arxiv.org/abs/2209.07858)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies**, 2026 — [[статья](https://arxiv.org/abs/2606.12369)] · ядро · источник: AIDAS Values & Pluralism
- **Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.**, 2019 — [[статья](https://arxiv.org/abs/1911.03891)] · ядро · источник: Alignment Goal Survey
- **The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.806/)] · ядро · источник: STONIC bibliography
- **The theory of planned behavior**, 1991 — [[статья](https://sciencedirect.com/science/article/pii/074959789190020T)] · ядро · источник: STONIC bibliography
- **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback**, 2022 — [[статья](https://arxiv.org/abs/2204.05862)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Training language models to follow instructions with human feedback. Ouyang et al. Neurips 2022.**, 2022 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf)] · ядро · источник: Alignment Goal Survey
- **What's the most important value? INVP: INvestigating the Value Priorities of LLMs through Decision-making in Social Scenarios**, 2025 — [[статья](https://aclanthology.org/2025.coling-main.317/)] · ядро · источник: STONIC bibliography

<a id="catalog-culture-language-and-pluralism"></a>

#### 🌍 Культура, язык и плюрализм · 103

- **'Too much alignment; not enough culture': Re-balancing Cultural Alignment Practices in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2509.26167)] · ядро · источник: AIDAS Values & Pluralism
- **(GlobalOpinionQA) Towards Measuring the Representation of Subjective Global Opinions in Language Models**, 2023 — [[статья](https://arxiv.org/abs/2306.16388)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey, Pluralistic Alignment, LLM Psychometrics, LLM Social Science
- **ACE-Align: Attribute Causal Effect Alignment for Cultural Values under Varying Persona Granularities**, 2026 — [[статья](https://arxiv.org/abs/2601.12962)] · ядро · источник: AIDAS Values & Pluralism
- **An Evaluation of Cultural Value Alignment in LLM**, 2025 — [[статья](https://arxiv.org/abs/2504.08863)] · ядро · источник: AIDAS Values & Pluralism
- **Arbiters of Ambivalence: Challenges of Using LLMs in No-Consensus Tasks**, 2025 — [[статья](https://arxiv.org/abs/2505.23820)] · ядро · источник: AIDAS Values & Pluralism
- **Assessing Cross-Cultural Alignment between ChatGPT and Human Societies**, 2023 — [[статья](https://arxiv.org/abs/2303.17466)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Assessing LLMs for Moral Value Pluralism**, 2023 — [[статья](https://arxiv.org/abs/2312.10075)] · ядро · источник: AIDAS Values & Pluralism
- **Attributing Culture-Conditioned Generations to Pretraining Corpora**, 2025 — [[статья](https://arxiv.org/abs/2412.20760)] · смежная тема · источник: Awesome Cultural NLP
- **Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs**, 2026 — [[статья](https://arxiv.org/abs/2601.15755)] · ядро · источник: AIDAS Values & Pluralism
- **BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages**, 2024 — [[статья](https://arxiv.org/abs/2406.09948)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.2/)] · ядро · источник: STONIC bibliography
- **Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2502.08045)] · ядро · источник: AIDAS Values & Pluralism
- **Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench**, 2025 — [[статья](https://arxiv.org/abs/2504.01127)] · ядро · источник: AIDAS Values & Pluralism
- **CARE: Multilingual Human Preference Learning for Cultural Awareness**, 2025 — [[статья](https://arxiv.org/abs/2504.05154)] · ядро · источник: AIDAS Values & Pluralism
- **CAReDiO: Enhancing Cultural Alignment via Representativeness and Distinctiveness Guided Data Optimization**, 2025 — [[статья](https://arxiv.org/abs/2504.08820)] · ядро · источник: AIDAS Values & Pluralism
- **CCBench: Assessing LLM Cultural Competence via Implicitly Signaled Norms using Health Queries**, 2026 — [[статья](https://arxiv.org/abs/2607.05405)] · ядро · источник: AIDAS Values & Pluralism
- **CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2311.16421)] · ядро · источник: AIDAS Values & Pluralism
- **Challenges and Strategies in Cross-Cultural NLP**, 2022 — [[статья](https://arxiv.org/abs/2203.10020)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Characterizing the ability of LLMs to recapitulate Americans' distributional responses to public opinion polling questions across political issues**, 2026 — [[статья](https://arxiv.org/abs/2603.20229)] · ядро · источник: AIDAS Values & Pluralism
- **code and data**, 2024 — [[статья](https://arxiv.org/abs/2410.12880)] · смежная тема · источник: LLM Social Science
- **Coherence Maximization Improves Pluralistic Alignment**, 2026 — [[статья](https://arxiv.org/abs/2606.03110)] · ядро · источник: AIDAS Values & Pluralism
- **Cross-cultural value alignment frameworks for responsible AI governance: Evidence from China-West comparative analysis**, 2025 — [[статья](https://arxiv.org/abs/2511.17256)] · ядро · источник: AIDAS Values & Pluralism
- **CulFiT: Fine-grained Cultural-aware LLM Training via Multilingual Critique Data Synthesis**, 2025 — [[статья](https://arxiv.org/abs/2505.19484)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Adaptation in Large Language Models for Political Discourse**, 2026 — [[статья](https://arxiv.org/abs/2605.23332)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Alignment in Large Language Models Using Soft Prompt Tuning**, 2025 — [[статья](https://arxiv.org/abs/2503.16094)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede's Cultural Dimensions**, 2023 — [[статья](https://arxiv.org/abs/2309.12342)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural bias and cultural alignment of large language models**, 2024 — [[статья](https://doi.org/10.1093/pnasnexus/pgae346)] · ядро · источник: STONIC bibliography
- **Cultural Conditioning or Placebo? On the Effectiveness of Socio-Demographic Prompting**, 2024 — [[статья](https://arxiv.org/abs/2406.11661)] · смежная тема · источник: Awesome Cultural NLP
- **Cultural Learning-Based Culture Adaptation of Language Models**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.156/)] · смежная тема · источник: Awesome Cultural NLP
- **Cultural Learning-Based Culture Adaptation of Language Models (CLCA)**, 2025 — [[статья](https://arxiv.org/abs/2504.02953)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette**, 2024 — [[статья](https://arxiv.org/abs/2412.11167)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Cultural Value Alignment in Large Language Models: A Prompt-based Analysis of Schwartz Values in Gemini, ChatGPT, and DeepSeek**, 2025 — [[статья](https://arxiv.org/abs/2505.17112)] · ядро · источник: AIDAS Values & Pluralism, STONIC bibliography, LLM Psychometrics
- **Cultural Value Alignment Via Latent Activation Steering in Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2605.26365)] · ядро · источник: AIDAS Values & Pluralism
- **CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark**, 2024 — [[статья](https://arxiv.org/abs/2410.02677)] · ядро · источник: AIDAS Values & Pluralism
- **Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art**, 2024 — [[статья](https://arxiv.org/abs/2406.03930)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **CulturalTeaming: AI-Assisted Interactive Red-Teaming for Challenging LLMs' (Lack of) Multicultural Knowledge**, 2024 — [[статья](https://arxiv.org/abs/2404.06664)] · смежная тема · источник: Awesome Cultural NLP
- **Culture is Not Trivia: Sociocultural Theory for Cultural NLP**, 2025 — [[статья](https://arxiv.org/abs/2502.12057)] · ядро · источник: AIDAS Values & Pluralism
- **CultureBank: An Online Community-Driven Knowledge Base toward Culturally Aware Language Technologies**, 2024 — [[статья](https://arxiv.org/abs/2404.15238)] · ядро · источник: AIDAS Values & Pluralism
- **CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs**, 2026 — [[статья](https://arxiv.org/abs/2606.01879)] · ядро · источник: AIDAS Values & Pluralism
- **CultureLLM: Incorporating Cultural Differences into Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2402.10946)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **CulturePark: Boosting Cross-cultural Understanding in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2405.15145)] · ядро · источник: AIDAS Values & Pluralism
- **CultureSynth: A Hierarchical Taxonomy-Guided and Retrieval-Augmented Framework for Cultural Question-Answer Synthesis**, 2025 — [[статья](https://arxiv.org/abs/2509.10886)] · ядро · источник: AIDAS Values & Pluralism
- **CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters**, 2026 — [[статья](https://arxiv.org/abs/2601.04885)] · ядро · источник: AIDAS Values & Pluralism
- **CURE: Cultural Understanding and Reasoning Evaluation - A Framework for "Thick" Culture Alignment Evaluation in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2511.12014)] · ядро · источник: AIDAS Values & Pluralism
- **Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions**, 2025 — [[статья](https://arxiv.org/abs/2510.21977)] · ядро · источник: AIDAS Values & Pluralism
- **Distributional Open-Ended Evaluation of LLM Cultural Value Alignment Based on Value Codebook**, 2026 — [[статья](https://arxiv.org/abs/2604.06210)] · ядро · источник: AIDAS Values & Pluralism
- **DLAMA: A Framework for Curating Culturally Diverse Facts for Probing the Knowledge of Pretrained LMs**, 2023 — [[статья](https://arxiv.org/abs/2306.05076)] · ядро · источник: AIDAS Values & Pluralism
- **EMBRACE: Shaping Inclusive Opinion Representation by Aligning Implicit Conversations with Social Norms**, 2025 — [[статья](https://arxiv.org/abs/2507.20264)] · ядро · источник: AIDAS Values & Pluralism
- **Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language we Prompt them in**, 2024 — [[статья](https://arxiv.org/abs/2404.18460)] · ядро · источник: STONIC bibliography
- **EtiCor: Corpus for Analyzing LLMs for Etiquettes**, 2023 — [[статья](https://arxiv.org/abs/2310.18974)] · ядро · источник: AIDAS Values & Pluralism
- **Evaluating and Improving Cultural Awareness of Reward Models for LLM Alignment**, 2025 — [[статья](https://arxiv.org/abs/2509.21798)] · ядро · источник: AIDAS Values & Pluralism
- **Evaluating Pluralism in LLMs through Latent Perspectives**, 2026 — [[статья](https://arxiv.org/abs/2606.13254)] · ядро · источник: AIDAS Values & Pluralism
- **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment**, 2025 — [[статья](https://arxiv.org/abs/2510.04045)] · ядро · источник: AIDAS Values & Pluralism
- **Exploring Cultural Variations in Moral Judgments with Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2506.12433)] · ядро · источник: AIDAS Values & Pluralism
- **Extrinsic Evaluation of Cultural Competence in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2406.11565)] · смежная тема · источник: Awesome Cultural NLP
- **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment**, 2024 — [[статья](https://arxiv.org/abs/2406.17692)] · ядро · источник: AIDAS Values & Pluralism
- **From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2505.16408)] · ядро · источник: AIDAS Values & Pluralism
- **Having Beer after Prayer? Measuring Cultural Bias in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2305.14456)] · смежная тема · источник: Awesome Cultural NLP
- **Hire Your Anthropologist! Rethinking Culture Benchmarks Through an Anthropological Lens**, 2025 — [[статья](https://arxiv.org/abs/2510.05931)] · ядро · источник: AIDAS Values & Pluralism
- **How Many Human Survey Respondents is a Large Language Model Worth? An Uncertainty Quantification Perspective**, 2025 — [[статья](https://arxiv.org/abs/2502.17773)] · ядро · источник: AIDAS Values & Pluralism
- **How Well Do LLMs Represent Values Across Cultures? Empirical Analysis of LLM Responses Based on Hofstede Cultural Dimensions**, 2024 — [[статья](https://arxiv.org/abs/2406.14805)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Improving Cross-Cultural Survey Simulation with Calibrated Value Personas**, 2026 — [[статья](https://arxiv.org/abs/2605.16193)] · ядро · источник: AIDAS Values & Pluralism
- **Investigating Cultural Alignment of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2402.13231)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions**, 2025 — [[статья](https://arxiv.org/abs/2502.16761)] · ядро · источник: AIDAS Values & Pluralism
- **Large Language Models as Superpositions of Cultural Perspectives**, 2023 — [[статья](https://arxiv.org/abs/2307.07870)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Legal Theory for Pluralistic Alignment**, 2024 — [[статья](https://arxiv.org/abs/2410.17271)] · смежная тема · источник: LLM Social Science
- **Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation**, 2026 — [[статья](https://arxiv.org/abs/2604.08797)] · ядро · источник: AIDAS Values & Pluralism
- **LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?**, 2025 — [[статья](https://arxiv.org/abs/2503.15003)] · ядро · источник: AIDAS Values & Pluralism
- **LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output**, 2024 — [[статья](https://arxiv.org/abs/2411.06032)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Made-in China, Thinking in America: U.S. Values Persist in Chinese LLMs**, 2025 — [[статья](https://arxiv.org/abs/2512.13723)] · ядро · источник: AIDAS Values & Pluralism
- **Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness**, 2025 — [[статья](https://arxiv.org/abs/2502.09637)] · ядро · источник: AIDAS Values & Pluralism
- **Meta-Learning Preferences for Multilingual LLM Alignment**, 2026 — [[статья](https://arxiv.org/abs/2607.13315)] · ядро · источник: AIDAS Values & Pluralism
- **Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2602.22475)] · ядро · источник: AIDAS Values & Pluralism
- **Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate**, 2026 — [[статья](https://arxiv.org/abs/2601.12091)] · ядро · источник: AIDAS Values & Pluralism
- **Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2502.16534)] · ядро · источник: AIDAS Values & Pluralism
- **Multilingual Language Models are not Multicultural: A Case Study in Emotion**, 2023 — [[статья](https://arxiv.org/abs/2307.01370)] · смежная тема · источник: Awesome Cultural NLP
- **NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities**, 2025 — [[статья](https://arxiv.org/abs/2505.18383)] · ядро · источник: AIDAS Values & Pluralism
- **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2404.12464)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP, LLM Social Science
- **On the steerability of large language models toward data-driven personas**, 2023 — [[статья](https://arxiv.org/abs/2311.04978)] · ядро · источник: AIDAS Values & Pluralism
- **Overton Pluralistic Reinforcement Learning for Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2602.20759)] · ядро · источник: AIDAS Values & Pluralism
- **Pluralistic Alignment for Healthcare: A Role-Driven Framework**, 2025 — [[статья](https://arxiv.org/abs/2509.10685)] · ядро · источник: AIDAS Values & Pluralism
- **Plurals: A System for Guiding LLMs Via Simulated Social Ensembles**, 2024 — [[статья](https://arxiv.org/abs/2409.17213)] · ядро · источник: AIDAS Values & Pluralism
- **POW: Political Overton Windows of Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2509.08853)] · ядро · источник: AIDAS Values & Pluralism
- **Probing Pre-Trained Language Models for Cross-Cultural Differences in Values**, 2022 — [[статья](https://arxiv.org/abs/2203.13722)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey, Awesome Cultural NLP
- **Prompts to Proxies: Emulating Human Preferences via a Compact LLM Ensemble**, 2025 — [[статья](https://arxiv.org/abs/2509.11311)] · ядро · источник: AIDAS Values & Pluralism
- **Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2503.08688)] · ядро · источник: AIDAS Values & Pluralism
- **RLHF: A Comprehensive Survey for Cultural, Multimodal and Low-Latency Alignment Methods**, 2025 — [[статья](https://arxiv.org/abs/2511.03939)] · ядро · источник: AIDAS Values & Pluralism
- **Self-Pluralising Culture Alignment for Large Language Models (CultureSPA)**, 2024 — [[статья](https://arxiv.org/abs/2410.12971)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations**, 2025 — [[статья](https://arxiv.org/abs/2502.07068)] · ядро · источник: AIDAS Values & Pluralism
- **Steerable Cultural Preference Optimization of Reward Models**, 2026 — [[статья](https://arxiv.org/abs/2606.18606)] · ядро · источник: AIDAS Values & Pluralism
- **Steering LLMs for Culturally Localized Generation**, 2026 — [[статья](https://arxiv.org/abs/2603.23301)] · ядро · источник: AIDAS Values & Pluralism
- **Survey of Cultural Awareness in Language Models: Text and Beyond**, 2024 — [[статья](https://arxiv.org/abs/2411.00860)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP, LLM Social Science
- **The Echoes of Multilinguality: Tracing Cultural Value Shifts during LM Fine-tuning**, 2024 — [[статья](https://arxiv.org/abs/2405.12744)] · смежная тема · источник: Awesome Cultural NLP
- **The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2604.20225)] · ядро · источник: AIDAS Values & Pluralism
- **Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning**, 2026 — [[статья](https://arxiv.org/abs/2601.21700)] · ядро · источник: AIDAS Values & Pluralism
- **Toward Culturally Grounded Natural Language Processing**, 2026 — [[статья](https://arxiv.org/abs/2603.26013)] · ядро · источник: AIDAS Values & Pluralism
- **Towards Measuring and Modeling "Culture" in LLMs: A Survey**, 2024 — [[статья](https://arxiv.org/abs/2403.15412)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **Towards Realistic Evaluation of Cultural Value Alignment: Diversity Enhancement for Survey Simulation**, 2025 — [[статья](https://sciencedirect.com/science/article/abs/pii/S030645732500041X)] · ядро · источник: AIDAS Values & Pluralism
- **Understanding Cultural Alignment in Multilingual LLMs via Natural Debate Statements**, 2026 — [[статья](https://arxiv.org/abs/2602.12878)] · ядро · источник: AIDAS Values & Pluralism
- **Value kaleidoscope: engaging AI with pluralistic human values, rights, and duties**, 2024 — [[статья](https://doi.org/10.1609/aaai.v38i18.29970)] · ядро · источник: STONIC bibliography
- **Whispers of Many Shores: Cultural Alignment through Collaborative Cultural Expertise**, 2025 — [[статья](https://arxiv.org/abs/2506.00242)] · ядро · источник: AIDAS Values & Pluralism
- **WorldValuesBench: A Large-Scale Benchmark for Multi-Cultural Value Awareness of Language Models**, 2024 — [[статья](https://arxiv.org/abs/2404.16308)] · ядро · источник: AIDAS Values & Pluralism
- **XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity**, 2026 — [[статья](https://arxiv.org/abs/2605.05662)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-preferences-opinions-and-social-simulation"></a>

#### 🗣️ Предпочтения, мнения и социальные симуляции · 120

- **(ANES) CommunityLM: Probing Partisan Worldviews from Language Models, COLING 2022**, 2022 — [[статья](https://arxiv.org/abs/2209.07065)] · ядро · источник: LLM Psychometrics
- **(ANES) Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information**, 2024 — [[статья](https://arxiv.org/abs/2402.18144)] · ядро · источник: LLM Psychometrics
- **(ANES) Representation Bias in Political Sample Simulations with Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2407.11409)] · ядро · источник: LLM Psychometrics
- **(ANES) Unpacking Political Bias in Large Language Models: A Cross-Model Comparison on U.S. Politics**, 2024 — [[статья](https://arxiv.org/abs/2412.16746)] · ядро · источник: LLM Psychometrics
- **(Culture) Cultural tendencies in generative AI, 2025.06, Nature Human Behaviour**, 2025 — [[статья](https://nature.com/articles/s41562-025-02242-1)] · ядро · источник: LLM Psychometrics
- **(GLES) Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study**, 2024 — [[статья](https://arxiv.org/abs/2412.13169)] · ядро · источник: LLM Psychometrics
- **(GLES) Human Preferences in Large Language Model Latent Space: A Technical Analysis on the Reliability of Synthetic Data in Voting Outcome Prediction**, 2025 — [[статья](https://arxiv.org/abs/2502.16280)] · ядро · источник: LLM Psychometrics
- **(GLES) Vox Populi, Vox AI? Using Language Models to Estimate German Public Opinion**, 2024 — [[статья](https://arxiv.org/abs/2407.08563)] · ядро · источник: LLM Psychometrics
- **(Others & custom) AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction**, 2023 — [[статья](https://arxiv.org/abs/2305.09620)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Are Large Language Models Chameleons? An Attempt to Simulate Social Surveys**, 2024 — [[статья](https://arxiv.org/abs/2405.19323)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Are LLMs (Really) Ideological? An IRT-based Analysis and Alignment Tool for Perceived Socio-Economic Bias in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2503.13149)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Better Aligned with Survey Respondents or Training Data? Unveiling Political Leanings of LLMs on U.S. Supreme Court Cases**, 2025 — [[статья](https://arxiv.org/abs/2502.18282)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Demonstrations of the Potential of AI-based Political Issue Polling, 2023.07, Harvard Data Science Review (HDSR)**, 2023 — [[статья](https://arxiv.org/abs/2307.04781)] · ядро · источник: LLM Psychometrics
- **(Others & custom) From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models, ACL 2023**, 2023 — [[статья](https://arxiv.org/abs/2305.08283)] · ядро · источник: LLM Psychometrics
- **(Others & custom) How Accurate are GPT-3’s Hypotheses About Social Science Phenomena?, 2023.07, Digital Society**, 2023 — [[статья](https://link.springer.com/article/10.1007/s44206-023-00054-2)] · ядро · источник: LLM Psychometrics
- **(Others & custom) IssueBench: Millions of Realistic Prompts for Measuring Issue Bias in LLM Writing Assistance**, 2025 — [[статья](https://arxiv.org/abs/2502.08395)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Large Language Models Can Be Used to Estimate the Latent Positions of Politicians**, 2023 — [[статья](https://arxiv.org/abs/2303.12057)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Linear Representations of Political Perspective Emerge in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2503.02080)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Llama meets EU: Investigating the European Political Spectrum through the Lens of LLMs, NAACL 2024 (Short Paper)**, 2024 — [[статья](https://arxiv.org/abs/2403.13592)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Questioning the Survey Responses of Large Language Models, NeurIPS 2024**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)] · ядро · источник: LLM Psychometrics
- **(PCT) Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas**, 2024 — [[статья](https://arxiv.org/abs/2412.14843)] · ядро · источник: LLM Psychometrics
- **(PCT) Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias, arXiv 2026.01**, 2026 — [[статья](https://arxiv.org/abs/2601.06194)] · ядро · источник: LLM Psychometrics
- **(PCT) Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models, ACL 2024**, 2024 — [[статья](https://arxiv.org/abs/2402.16786)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(PCT) PRISM: A Methodology for Auditing Biases in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2410.18906)] · ядро · источник: LLM Psychometrics
- **(PCT) Revealing Fine-Grained Values and Opinions in Large Language Models, EMNLP 2024 Findings**, 2024 — [[статья](https://arxiv.org/abs/2406.19238)] · ядро · источник: LLM Psychometrics
- **(PCT) The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation**, 2023 — [[статья](https://arxiv.org/abs/2301.01768)] · ядро · источник: LLM Psychometrics
- **(PCT) The Self-Perception and Political Biases of ChatGPT**, 2024 — [[статья](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/7115633)] · ядро · источник: LLM Psychometrics
- **A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations**, 2025 — [[статья](https://arxiv.org/abs/2505.14106)] · смежная тема · источник: Personalized Alignment
- **AI PERSONA: Towards Life-long Personalization of LLMs**, 2024 — [[статья](https://arxiv.org/abs/2412.13103)] · смежная тема · источник: Personalized Alignment
- **Aligning Language Models from User Interactions**, 2026 — [[статья](https://arxiv.org/abs/2603.12273)] · смежная тема · источник: Personalized Alignment
- **Aligning Large Language Models with Diverse Political Viewpoints**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-main.412/)] · ядро · источник: STONIC bibliography
- **Aligning LLMs with Individual Preferences via Interaction**, 2024 — [[статья](https://arxiv.org/abs/2410.03642)] · смежная тема · источник: Personalized Alignment
- **Aligning to Thousands of Preferences via System Message Generalization**, 2024 — [[статья](https://arxiv.org/abs/2405.17977)] · смежная тема · источник: Personalized Alignment
- **Aligning VLM Assistants with Personalized Situated Cognition**, 2025 — [[статья](https://arxiv.org/abs/2506.00930)] · смежная тема · источник: Personalized Alignment
- **AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment**, 2026 — [[статья](https://arxiv.org/abs/2603.26680)] · смежная тема · источник: Personalized Alignment
- **Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs**, 2025 — [[статья](https://arxiv.org/abs/2502.19148)] · смежная тема · источник: Personalized Alignment
- **APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings**, 2026 — [[статья](https://arxiv.org/abs/2605.21063)] · смежная тема · источник: Personalized Alignment
- **APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents**, 2026 — [[статья](https://arxiv.org/abs/2605.27419)] · ядро · источник: AIDAS Values & Pluralism
- **BAPO: Base-Anchored Preference Optimization for Overcoming Forgetting in Large Language Models Personalization**, 2024 — [[статья](https://aclanthology.org/2024.findings-emnlp.398/)] · смежная тема · источник: Personalized Alignment
- **Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization**, 2026 — [[статья](https://arxiv.org/abs/2606.02300)] · смежная тема · источник: Personalized Alignment
- **COMPO: Community Preferences for Language Model Personalization**, 2024 — [[статья](https://arxiv.org/abs/2410.16027)] · смежная тема · источник: Personalized Alignment, LLM Social Science
- **Controllable Safety Alignment: Inference-Time Adaptation to Diverse Safety Requirements**, 2024 — [[статья](https://arxiv.org/abs/2410.08968)] · смежная тема · источник: Personalized Alignment
- **CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors**, 2026 — [[статья](https://arxiv.org/abs/2604.14773)] · смежная тема · источник: Personalized Alignment
- **CoSteer: Collaborative Decoding-Time Personalization via Local Delta Steering**, 2025 — [[статья](https://arxiv.org/abs/2507.04756)] · смежная тема · источник: Personalized Alignment
- **Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling**, 2026 — [[статья](https://arxiv.org/abs/2607.18310)] · ядро · источник: AIDAS Values & Pluralism
- **Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2309.03126)] · смежная тема · источник: Personalized Alignment
- **Drift: Decoding-time Personalized Alignments with Implicit User Preferences**, 2025 — [[статья](https://arxiv.org/abs/2502.14289)] · смежная тема · источник: Personalized Alignment
- **EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents**, 2026 — [[статья](https://arxiv.org/abs/2606.26883)] · ядро · источник: AIDAS Values & Pluralism
- **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance**, 2025 — [[статья](https://arxiv.org/abs/2505.16348)] · смежная тема · источник: Personalized Alignment
- **EmpathyAgent: Can Embodied Agents Conduct Empathetic Actions?**, 2025 — [[статья](https://arxiv.org/abs/2503.16545)] · смежная тема · источник: Personalized Alignment
- **Evaluating the Effectiveness of Persona Simulation in Opinion Prediction with GPT-4.1**, 2026 — [[статья](https://arxiv.org/abs/2607.20589)] · ядро · источник: AIDAS Values & Pluralism
- **Extended Inductive Reasoning for Personalized Preference Inference from Behavioral Signals**, 2025 — [[статья](https://arxiv.org/abs/2505.18071)] · смежная тема · источник: Personalized Alignment
- **Few-shot Personalization of LLMs with Mis-aligned Responses**, 2024 — [[статья](https://arxiv.org/abs/2406.18678)] · смежная тема · источник: Personalized Alignment
- **From 1,000,000 Users to Every User: Scaling Up Personalized Preference for User-level Alignment**, 2025 — [[статья](https://arxiv.org/abs/2503.15463)] · смежная тема · источник: Personalized Alignment
- **From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning**, 2026 — [[статья](https://arxiv.org/abs/2605.23382)] · смежная тема · источник: Personalized Alignment
- **From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes**, 2026 — [[статья](https://arxiv.org/abs/2605.16303)] · ядро · источник: AIDAS Values & Pluralism
- **From Empathy to Personalized Empathy: Adapting Empathetic Strategies to Individual Users**, 2026 — [[статья](https://arxiv.org/abs/2606.00728)] · смежная тема · источник: Personalized Alignment
- **From Generic Empathy to Personalized Emotional Support: A Self-Evolution Framework for User Preference Alignment**, 2025 — [[статья](https://arxiv.org/abs/2505.16610)] · смежная тема · источник: Personalized Alignment
- **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents**, 2026 — [[статья](https://arxiv.org/abs/2604.20006)] · смежная тема · источник: Personalized Alignment
- **From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG**, 2026 — [[статья](https://arxiv.org/abs/2605.18271)] · смежная тема · источник: Personalized Alignment
- **Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation**, 2026 — [[статья](https://arxiv.org/abs/2605.24647)] · смежная тема · источник: Personalized Alignment
- **Language Models Don't Know What You Want: Evaluating Personalization in Deep Research Needs Real Users**, 2026 — [[статья](https://arxiv.org/abs/2603.16120)] · смежная тема · источник: Personalized Alignment
- **Large Language Models Empowered Personalized Web Agents**, 2024 — [[статья](https://arxiv.org/abs/2410.17236)] · смежная тема · источник: Personalized Alignment
- **Learning to summarize user information for personalized reinforcement learning from human feedback**, 2026 — [[статья](https://openreview.net/forum?id=Ar078WR3um)] · смежная тема · источник: Personalized Alignment
- **LLMs are Biased Teachers: Evaluating LLM Bias in Personalized Education**, 2024 — [[статья](https://arxiv.org/abs/2410.14012)] · смежная тема · источник: Personalized Alignment
- **MAP: Multi-Human-Value Alignment Palette**, 2024 — [[статья](https://openreview.net/forum?id=NN6QHwgRrQ)] · смежная тема · источник: Personalized Alignment
- **MATO: Multi-objective Personalized Alignment with Test-time Optimization for Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2605.25342)] · смежная тема · источник: Personalized Alignment
- **MetaAlign: Align Large Language Models with Diverse Preferences during Inference Time**, 2024 — [[статья](https://arxiv.org/abs/2410.14184)] · смежная тема · источник: Personalized Alignment
- **MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning**, 2025 — [[статья](https://arxiv.org/abs/2505.24846)] · смежная тема · источник: Personalized Alignment
- **More human than human: measuring ChatGPT political bias**, 2023 — [[статья](https://link.springer.com/article/10.1007/s11127-023-01097-2)] · смежная тема · источник: LLM Social Science
- **NextQuill: Causal Preference Modeling for Enhancing LLM Personalization**, 2026 — [[статья](https://openreview.net/forum?id=xYpVlKMFqv)] · смежная тема · источник: Personalized Alignment
- **Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models, ACL 2025**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1529/)] · смежная тема · источник: LLM Social Science
- **Opinion dynamics and mutual influence with LLM agents through dialog simulation**, 2026 — [[статья](https://arxiv.org/abs/2602.12583)] · ядро · источник: AIDAS Values & Pluralism
- **P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling**, 2026 — [[статья](https://openreview.net/forum?id=hXNApWLBZG)] · смежная тема · источник: Personalized Alignment
- **PAL: Sample-Efficient Personalized Reward Modeling for Pluralistic Alignment**, 2024 — [[статья](https://openreview.net/forum?id=1kFDrYCuSu)] · смежная тема · источник: Personalized Alignment
- **PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents**, 2026 — [[статья](https://arxiv.org/abs/2608.04003)] · смежная тема · источник: Personalized Alignment
- **Persona-Based Simulation of Human Opinion at Population Scale**, 2026 — [[статья](https://arxiv.org/abs/2603.27056)] · ядро · источник: AIDAS Values & Pluralism
- **Persona-DB: Efficient Large Language Model Personalization for Response Prediction with Collaborative Data Refinement**, 2024 — [[статья](https://arxiv.org/abs/2402.11060)] · смежная тема · источник: Personalized Alignment
- **Persona-judge: Personalized Alignment of Large Language Models via Token-level Self-judgment**, 2025 — [[статья](https://arxiv.org/abs/2504.12663)] · смежная тема · источник: Personalized Alignment
- **PersonaAgent: When Large Language Model Agents Meet Personalization at Test Time**, 2025 — [[статья](https://arxiv.org/abs/2506.06254)] · смежная тема · источник: Personalized Alignment
- **PersonaFeedback: A Large-scale Human-annotated Benchmark For Personalization**, 2025 — [[статья](https://arxiv.org/abs/2506.12915)] · смежная тема · источник: Personalized Alignment
- **PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants**, 2025 — [[статья](https://arxiv.org/abs/2506.09902)] · смежная тема · источник: Personalized Alignment
- **Personalized Adaptation via In-Context Preference Learning**, 2024 — [[статья](https://arxiv.org/abs/2410.14001)] · смежная тема · источник: Personalized Alignment
- **Personalized Benchmarking: Evaluating LLMs by Individual Preferences**, 2026 — [[статья](https://arxiv.org/abs/2604.18943)] · смежная тема · источник: Personalized Alignment
- **Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment**, 2026 — [[статья](https://arxiv.org/abs/2603.10009)] · смежная тема · источник: Personalized Alignment
- **Personalized Language Modeling from Personalized Human Feedback**, 2024 — [[статья](https://arxiv.org/abs/2402.05133)] · смежная тема · источник: Personalized Alignment
- **Personalized LLM Decoding via Contrasting Personal Preference**, 2025 — [[статья](https://arxiv.org/abs/2506.12109)] · смежная тема · источник: Personalized Alignment
- **Personalized Reasoning: Just-in-time Personalization and Why LLMs Fail at It**, 2026 — [[статья](https://openreview.net/forum?id=O1hfVE0UxG)] · смежная тема · источник: Personalized Alignment
- **Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization**, 2026 — [[статья](https://arxiv.org/abs/2604.07343)] · смежная тема · источник: Personalized Alignment
- **Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging**, 2023 — [[статья](https://arxiv.org/abs/2310.11564)] · смежная тема · источник: Personalized Alignment
- **Personalizing Reinforcement Learning from Human Feedback with Variational Preference Learning**, 2024 — [[статья](https://arxiv.org/abs/2408.10075)] · смежная тема · источник: Personalized Alignment
- **PersonalLLM: Tailoring LLMs to Individual Preferences**, 2024 — [[статья](https://arxiv.org/abs/2409.20296)] · смежная тема · источник: Personalized Alignment
- **PersonaVLM: Long-Term Personalized Multimodal LLMs**, 2026 — [[статья](https://arxiv.org/abs/2604.13074)] · смежная тема · источник: Personalized Alignment
- **PEToolLLM: Towards Personalized Tool Learning in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2502.18980)] · смежная тема · источник: Personalized Alignment
- **Political-LLM: Large Language Models in Political Science**, 2024 — [[статья](https://arxiv.org/abs/2412.06864)] · смежная тема · источник: LLM Social Science
- **POPI: Personalizing LLMs via Optimized Natural Language Preference Inference**, 2025 — [[статья](https://arxiv.org/abs/2510.17881)] · смежная тема · источник: Personalized Alignment
- **Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization**, 2026 — [[статья](https://arxiv.org/abs/2604.22345)] · смежная тема · источник: Personalized Alignment
- **Preference-Aware Rubric Learning for Personalized Evaluation**, 2026 — [[статья](https://arxiv.org/abs/2605.31545)] · смежная тема · источник: Personalized Alignment
- **PrefPalette: Personalized Preference Modeling with Latent Attributes**, 2025 — [[статья](https://arxiv.org/abs/2507.13541)] · смежная тема · источник: Personalized Alignment
- **PRIME: Large Language Model Personalization with Cognitive Memory and Thought Processes**, 2025 — [[статья](https://arxiv.org/abs/2507.04607)] · смежная тема · источник: Personalized Alignment
- **Reasoning Meets Personalization: Unleashing the Potential of Large Reasoning Model for Personalized Generation**, 2025 — [[статья](https://arxiv.org/abs/2505.17571)] · смежная тема · источник: Personalized Alignment
- **RLHF from Heterogeneous Feedback via Personalization and Preference Aggregation**, 2024 — [[статья](https://arxiv.org/abs/2405.00254)] · смежная тема · источник: Personalized Alignment
- **Show, Don't Tell: Aligning Language Models with Demonstrated Feedback**, 2024 — [[статья](https://arxiv.org/abs/2406.00888)] · смежная тема · источник: Personalized Alignment
- **Silicon Sampling via Cross-Survey Transfer**, 2026 — [[статья](https://arxiv.org/abs/2607.03091)] · ядро · источник: AIDAS Values & Pluralism
- **Steering Large Language Models for Machine Translation Personalization**, 2025 — [[статья](https://arxiv.org/abs/2505.16612)] · смежная тема · источник: Personalized Alignment
- **Swap-guided Preference Learning for Personalized Reinforcement Learning from Human Feedback**, 2026 — [[статья](https://openreview.net/forum?id=nc28mSbyVG)] · смежная тема · источник: Personalized Alignment
- **SynthesizeMe! Inducing Persona-Guided Prompts for Personalized Reward Models in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2506.05598)] · смежная тема · источник: Personalized Alignment
- **Teaching Language Models to Evolve with Users: Dynamic Profile Modeling for Personalized Alignment**, 2025 — [[статья](https://arxiv.org/abs/2505.15456)] · смежная тема · источник: Personalized Alignment
- **Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures**, 2026 — [[статья](https://arxiv.org/abs/2605.10991)] · смежная тема · источник: Personalized Alignment
- **The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads**, 2026 — [[статья](https://arxiv.org/abs/2608.04570)] · смежная тема · источник: Personalized Alignment
- **The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2406.11096)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2404.16019)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP, Personalized Alignment, LLM Social Science
- **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**, 2024 — [[статья](https://openreview.net/forum?id=DFr5hteojx)] · смежная тема · источник: Personalized Alignment
- **Think-While-Generating: On-the-Fly Reasoning for Personalized Long-Form Generation**, 2026 — [[статья](https://openreview.net/forum?id=lle0aGQyQb)] · смежная тема · источник: Personalized Alignment
- **Toward Multi-Session Personalized Conversation: A Large-Scale Dataset and Hierarchical Tree Framework for Implicit Reasoning**, 2025 — [[статья](https://arxiv.org/abs/2503.07018)] · смежная тема · источник: Personalized Alignment
- **Towards Faithful and Controllable Personalization via Critique-Post-Edit Reinforcement Learning**, 2025 — [[статья](https://arxiv.org/abs/2510.18849)] · смежная тема · источник: Personalized Alignment
- **TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment**, 2026 — [[статья](https://arxiv.org/abs/2606.01755)] · смежная тема · источник: Personalized Alignment
- **What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data**, 2026 — [[статья](https://openreview.net/forum?id=sC6A1bFDUt)] · смежная тема · источник: Personalized Alignment
- **When Harry Meets Superman: The Role of The Interlocutor in Persona-Based Dialogue Generation**, 2025 — [[статья](https://arxiv.org/abs/2505.24613)] · смежная тема · источник: Personalized Alignment
- **When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning**, 2025 — [[статья](https://arxiv.org/abs/2502.19158)] · смежная тема · источник: Personalized Alignment

<a id="catalog-moral-reasoning-and-value-understanding"></a>

#### ⚖️ Моральное рассуждение и понимание ценностей · 63

- **(DIT) Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test**, 2024 — [[статья](https://arxiv.org/abs/2402.02135)] · ядро · источник: LLM Psychometrics
- **(DIT) Probing the Moral Development of Large Language Models through Defining Issues Test**, 2023 — [[статья](https://arxiv.org/abs/2309.13356)] · ядро · источник: Awesome LLM Safety, LLM Psychometrics
- **(ETHICS) An Evaluation of GPT-4 on the ETHICS Dataset**, 2023 — [[статья](https://arxiv.org/abs/2309.10492)] · ядро · источник: LLM Psychometrics
- **(ETHICS) Despite "super-human" performance, current LLMs are unsuited for decisions about ethics and safety, NeurIPS 2022 Workshop**, 2022 — [[статья](https://arxiv.org/abs/2212.06295)] · ядро · источник: LLM Psychometrics
- **(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023**, 2023 — [[статья](https://dl.acm.org/doi/abs/10.1145/3624918.3625327)] · ядро · источник: LLM Psychometrics
- **(ETHICS) Inducing Human-like Biases in Moral Reasoning Language Models**, 2024 — [[статья](https://arxiv.org/abs/2411.15386)] · ядро · источник: LLM Psychometrics
- **(MFT) Analyzing the Ethical Logic of Six Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2501.08951)] · ядро · источник: LLM Psychometrics
- **(MFT) Are Large Language Models Moral Hypocrites? A Study Based on Moral Foundations, AIES 2024**, 2024 — [[статья](https://ojs.aaai.org/index.php/AIES/article/view/31704)] · ядро · источник: LLM Psychometrics
- **(MFT) Does Moral Code Have a Moral Code? Probing Delphi's Moral Philosophy, NAACL 2022 Workshop**, 2022 — [[статья](https://arxiv.org/abs/2205.12771)] · ядро · источник: LLM Psychometrics
- **(MFT) Exploring and steering the moral compass of Large Language Models, ICPR 2024**, 2024 — [[статья](https://arxiv.org/abs/2405.17345)] · ядро · источник: LLM Psychometrics
- **(MFT) M3oralBench: A MultiModal Moral Benchmark for LVLMs**, 2024 — [[статья](https://arxiv.org/abs/2412.20718)] · ядро · источник: LLM Psychometrics
- **(MFT) Moral Foundations of Large Language Models, EMNLP 2024**, 2024 — [[статья](https://arxiv.org/abs/2310.15337)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(MFT) Moral Mimicry: Large Language Models Produce Moral Rationalizations Tailored to Political Identity, ACL 2023 Workshop**, 2023 — [[статья](https://arxiv.org/abs/2209.12106)] · ядро · источник: Alignment Goal Survey, LLM Psychometrics, LLM Social Science
- **(MFT) MoralBench: Moral Evaluation of LLMs**, 2024 — [[статья](https://arxiv.org/abs/2406.04428)] · ядро · источник: LLM Psychometrics
- **(MFT) Towards "Differential AI Psychology" and in-context Value-driven Statement Alignment with Moral Foundations Theory**, 2024 — [[статья](https://arxiv.org/abs/2408.11415)] · ядро · источник: LLM Psychometrics
- **(MFT) Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models**, 2024 — [[статья](https://arxiv.org/abs/2412.18863)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral, 2025.07, ACL 2025 Best Resource Paper**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.294/)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Decoding Multilingual Moral Preferences: Unveiling LLM's Biases through the Moral Machine Experiment, AIES 2024**, 2024 — [[статья](https://ojs.aaai.org/index.php/AIES/article/view/31741)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?, C3NLP 2024**, 2024 — [[статья](https://arxiv.org/abs/2406.16316)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Evaluating Moral Beliefs across LLMs through a Pluralistic Framework**, 2024 — [[статья](https://arxiv.org/abs/2411.03665)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Evaluating the Moral Beliefs Encoded in LLMs, NeurIPS 2023**, 2023 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a2cf225ba392627529efef14dc857e22-Abstract-Conference.html)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Extended Japanese Commonsense Morality Dataset with Masked Token and Label Enhancement, CIKM '24 (Short Paper)**, 2024 — [[статья](https://dl.acm.org/doi/abs/10.1145/3627673.3679924)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Knowledge of cultural moral norms in large language models, ACL 2023**, 2023 — [[статья](https://arxiv.org/abs/2306.01857)] · ядро · источник: Awesome Cultural NLP, LLM Psychometrics
- **(Others & Custom) Large-scale moral machine experiment on large language models**, 2024 — [[статья](https://arxiv.org/abs/2411.06790)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) LLMs as mirrors of societal moral standards: reflection of cultural divergence and agreement across ethical topics**, 2024 — [[статья](https://arxiv.org/abs/2412.00962)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment**, 2024 — [[статья](https://arxiv.org/abs/2411.11731)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Normative Evaluation of Large Language Models with Everyday Moral Dilemmas**, 2025 — [[статья](https://arxiv.org/abs/2501.18081)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(Others & Custom) Potential benefits of employing large language models in research in moral education and development, 2023.01, Journal of Moral Education**, 2023 — [[статья](https://tandfonline.com/doi/abs/10.1080/03057240.2023.2250570)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Right vs. Right: Can LLMs Make Tough Choices?**, 2024 — [[статья](https://arxiv.org/abs/2412.19926)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) SaGE: Evaluating Moral Consistency in Large Language Models, LREC-COLING 2024**, 2024 — [[статья](https://arxiv.org/abs/2402.13709)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) The Moral Mind(s) of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2412.04476)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making**, 2024 — [[статья](https://arxiv.org/abs/2410.07304)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) Western, Religious or Spiritual: An Evaluation of Moral Justification in Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2311.07792)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) What does AI consider praiseworthy?, 2025.02, AI and Ethics**, 2025 — [[статья](https://link.springer.com/article/10.1007/s43681-025-00682-z)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment, NeurIPS 2022**, 2022 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b654d6150630a5ba5df7a55621390daf-Abstract-Conference.html)] · ядро · источник: LLM Psychometrics
- **Aditi Khandelwal et al. EACL 2024.**, 2024 — [[статья](https://aclanthology.org/2024.eacl-long.176/)] · смежная тема · источник: Awesome LLM Safety
- **Agent Alignment in Evolving Social Norms**, 2024 — [[статья](https://arxiv.org/abs/2401.04620)] · смежная тема · источник: LLM Social Science
- **Can Machines Learn Morality? The Delphi Experiment**, 2021 — [[статья](https://arxiv.org/abs/2110.07574)] · ядро · источник: Alignment Goal Survey, STONIC bibliography
- **CrowS-Pairs**, 2020 — [[статья](https://aclanthology.org/2020.emnlp-main.154/)] · смежная тема · источник: Awesome LLM Datasets
- **DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life**, 2024 — [[статья](https://arxiv.org/abs/2410.02683)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Psychometrics
- **Exploring the psychology of GPT-4's Moral and Legal Reasoning**, 2023 — [[статья](https://arxiv.org/abs/2308.01264)] · смежная тема · источник: LLM Social Science
- **How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main**, 2026 — [[статья](https://arxiv.org/abs/2603.13876)] · смежная тема · источник: LLM Social Science
- **Investigating machine moral judgement through the Delphi experiment, Nature Machine Intelligence**, 2025 — [[статья](https://nature.com/articles/s42256-024-00969-6)] · смежная тема · источник: LLM Social Science
- **Irene Solaiman and Christy Dennison. NeurIPS 2021.**, 2021 — [[статья](https://arxiv.org/abs/2106.10328)] · смежная тема · источник: Awesome LLM Safety
- **Joshua Landau et al. arXiv 2023.**, 2023 — [[статья](https://arxiv.org/abs/2302.07459)] · смежная тема · источник: Awesome LLM Safety
- **Laura Weidinger et al. arXiv 2021.**, 2021 — [[статья](https://arxiv.org/abs/2112.04359)] · смежная тема · источник: Awesome LLM Safety
- **Learning norms from stories: A prior for value aligned agents. Nahian et al. AIES 2020.**, 2020 — [[статья](https://arxiv.org/abs/1912.03553)] · ядро · источник: Alignment Goal Survey
- **Moral Foundations of Large Language Models**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-main.982/)] · ядро · источник: STONIC bibliography
- **Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences**, 2021 — [[статья](https://aclanthology.org/2021.emnlp-main.54/)] · ядро · источник: STONIC bibliography
- **MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.**, 2023 — [[статья](https://arxiv.org/abs/2212.10720)] · ядро · источник: Alignment Goal Survey
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.**, 2023 — [[статья](https://arxiv.org/abs/2305.03047)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **Revealing the Pragmatic Dilemma for Moral Reasoning Acquisition in Language Models**, 2025 — [[статья](https://arxiv.org/abs/2502.16600)] · смежная тема · источник: LLM Social Science
- **Safety Assessment of Chinese Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2304.10436)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **SafetyBench 2023-9**, 2023 — [[статья](https://arxiv.org/abs/2309.07045)] · смежная тема · источник: Awesome LLM Datasets
- **Shamik Roy et al. arXiv 2023.**, 2023 — [[статья](https://aclanthology.org/2022.nlpcss-1.20/)] · смежная тема · источник: Awesome LLM Safety
- **Shitong Duan et al. ICLR 2024.**, 2024 — [[статья](https://openreview.net/forum?id=m3RRWWFaVe)] · смежная тема · источник: Awesome LLM Safety
- **Social Chemistry 101: Learning to Reason about Social and Moral Norms**, 2020 — [[статья](https://aclanthology.org/2020.emnlp-main.48/)] · ядро · источник: STONIC bibliography
- **Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.1541/)] · ядро · источник: STONIC bibliography
- **TRUSTGPT 2023-6**, 2023 — [[статья](https://arxiv.org/abs/2306.11507)] · смежная тема · источник: Awesome LLM Datasets
- **Utkarsh Agarwal et al. LREC/COLING 2024.**, 2024 — [[статья](https://aclanthology.org/2024.lrec-main.560/)] · смежная тема · источник: Awesome LLM Safety
- **When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.**, 2022 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2022/file/b654d6150630a5ba5df7a55621390daf-Paper-Conference.pdf)] · ядро · источник: Alignment Goal Survey
- **Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)**, 2026 — [[статья](https://arxiv.org/abs/2509.17703)] · смежная тема · источник: LLM Social Science
- **Xi Zhiheng et al. CCL 2023.**, 2023 — [[статья](https://aclanthology.org/2023.ccl-4.2/)] · смежная тема · источник: Awesome LLM Safety

<a id="catalog-alignment-steering-and-preferences"></a>

#### 🧰 Алайнмент, управление и предпочтения · 133

- **\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2312.12999)] · смежная тема · источник: LLM Social Science
- **A general language assistant as a laboratory for alignment. Askell et al. arXiv 2021.**, 2021 — [[статья](https://arxiv.org/abs/2112.00861)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **A Roadmap to Pluralistic Alignment**, 2024 — [[статья](https://arxiv.org/abs/2402.05070)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy**, 2026 — [[статья](https://arxiv.org/abs/2605.01642)] · ядро · источник: AIDAS Values & Pluralism
- **AI Alignment Breaks at the Edge**, 2026 — [[статья](https://arxiv.org/abs/2602.20042)] · ядро · источник: AIDAS Values & Pluralism
- **Aligning \AI\ With Shared Human Values**, 2021 — [[статья](https://openreview.net/forum?id=dNy_RKzJacY)] · ядро · источник: STONIC bibliography
- **Aligning Crowd Feedback via Distributional Preference Reward Modeling**, 2024 — [[статья](https://arxiv.org/abs/2402.09764)] · ядро · источник: Pluralistic Alignment
- **Aligning Large Language Models with Human Opinions through Persona Selection and Value--Belief--Norm Reasoning**, 2023 — [[статья](https://arxiv.org/abs/2311.08385)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping**, 2026 — [[статья](https://ojs.aaai.org/index.php/AAAI/article/view/41109)] · ядро · источник: Pluralistic Alignment
- **Aligning Multimodal LLM with Human Preference: A Survey**, 2025 — [[статья](https://arxiv.org/abs/2503.14504)] · ядро · источник: Pluralistic Alignment
- **Aligning to Thousands of Preferences via System Message Generalization**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/86c9df30129f7663ad4d429b6f80d461-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective**, 2025 — [[статья](https://aclanthology.org/2025.findings-acl.1188/)] · ядро · источник: Pluralistic Alignment, STONIC bibliography, LLM Social Science
- **Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.468/)] · ядро · источник: Pluralistic Alignment
- **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond), NeurIPS 2025 D&B Track Best Paper**, 2025 — [[статья](https://arxiv.org/abs/2510.22954)] · смежная тема · источник: LLM Social Science
- **Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration**, 2026 — [[статья](https://arxiv.org/abs/2604.13705)] · ядро · источник: AIDAS Values & Pluralism
- **Black-Box Prompt Optimization: Aligning Large Language Models without Model Training**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.176/)] · ядро · источник: Pluralistic Alignment
- **Communication-Efficient Desire Alignment for Proactive Embodied Human–Agent Interaction, ACL 2026 Main (Oral)**, 2026 — [[статья](https://arxiv.org/abs/2505.22503)] · смежная тема · источник: LLM Social Science
- **Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.**, 2022 — [[статья](https://arxiv.org/abs/2212.08073)] · ядро · источник: Alignment Goal Survey
- **Constitutional Value Potentials: reading and steering internal priority margins in language models**, 2026 — [[статья](https://arxiv.org/abs/2606.15420)] · ядро · источник: AIDAS Values & Pluralism
- **Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-main.85/)] · ядро · источник: Pluralistic Alignment
- **Controllable Value Alignment in Large Language Models through Neuron-Level Editing**, 2026 — [[статья](https://arxiv.org/abs/2602.07356)] · ядро · источник: AIDAS Values & Pluralism
- **Counterfactual Reasoning for Steerable Pluralistic Value Alignment of Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2510.18526)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **Cultural Alignment in Large Language Models: An Explanatory Analysis Based on Hofstede’s Cultural Dimensions**, 2025 — [[статья](https://aclanthology.org/2025.coling-main.567/)] · ядро · источник: Pluralistic Alignment
- **CULTURE-GEN: Revealing Global Cultural Perception in Language Models through Natural Language Prompting**, 2024 — [[статья](https://arxiv.org/abs/2404.10199)] · ядро · источник: Awesome Cultural NLP, Pluralistic Alignment
- **CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies**, 2024 — [[статья](https://aclanthology.org/2024.findings-emnlp.288/)] · ядро · источник: Pluralistic Alignment
- **CultureLLM: Incorporating Cultural Differences into Large Language Models**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a16935bf54c4af233e25d998b7f4a2c-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **CulturePark: Boosting Cross-cultural Understanding in Large Language Models**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/77f089cd16dbc36ddd1caeb18446fbdd-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?**, 2025 — [[статья](https://arxiv.org/abs/2505.23749)] · ядро · источник: AIDAS Values & Pluralism
- **Distributional Alignment for Social Simulation with LLMs: A Prompt Mixture Modeling Approach**, 2025 — [[статья](https://openreview.net/forum?id=6KM1siLL8a)] · ядро · источник: Pluralistic Alignment
- **Diverging Preferences: When do Annotators Disagree and do Models Know?**, 2024 — [[статья](https://arxiv.org/abs/2410.14632)] · смежная тема · источник: LLM Social Science
- **Diverse Human Value Alignment for Large Language Models via Ethical Reasoning**, 2025 — [[статья](https://arxiv.org/abs/2511.00379)] · ядро · источник: AIDAS Values & Pluralism
- **Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning**, 2026 — [[статья](https://arxiv.org/abs/2603.10588)] · ядро · источник: AIDAS Values & Pluralism
- **DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping**, 2026 — [[статья](https://arxiv.org/abs/2605.14420)] · ядро · источник: AIDAS Values & Pluralism
- **Evaluating and Inducing Personality in Pre-trained Language Models**, 2023 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21f7b745f73ce0d1f9bcea7f40b1388e-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **Evaluating Cultural Adaptability of a Large Language Model via Simulation of Synthetic Personas**, 2024 — [[статья](https://arxiv.org/abs/2408.06929)] · ядро · источник: Pluralistic Alignment
- **Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.1301/)] · ядро · источник: Pluralistic Alignment
- **Few-shot Steerable Alignment: Adapting Rewards and LLM Policies with Neural Processes**, 2024 — [[статья](https://arxiv.org/abs/2412.13998)] · ядро · источник: Pluralistic Alignment
- **Fine-tuning language models to find agreement among humans with diverse preferences**, 2022 — [[статья](https://arxiv.org/abs/2211.15006)] · смежная тема · источник: LLM Social Science
- **Foundational Challenges in Assuring Alignment and Safety of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2404.09932)] · смежная тема · источник: LLM Social Science
- **Foundational Moral Values for AI Alignment**, 2023 — [[статья](https://arxiv.org/abs/2311.17017)] · ядро · источник: AIDAS Values & Pluralism
- **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.346/)] · ядро · источник: Pluralistic Alignment
- **From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement**, 2026 — [[статья](https://arxiv.org/abs/2605.14912)] · ядро · источник: AIDAS Values & Pluralism
- **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models**, 2023 — [[статья](https://aclanthology.org/2023.emnlp-main.961/)] · ядро · источник: Pluralistic Alignment
- **From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2310.17857)] · ядро · источник: AIDAS Values & Pluralism
- **Group Robust Best-of-K Decoding of Language Models for Pluralistic Alignment**, 2024 — [[статья](https://openreview.net/forum?id=JI6j4NUGHv)] · ядро · источник: Pluralistic Alignment
- **Group Robust Preference Optimization in Reward-free RLHF**, 2024 — [[статья](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4147dfaa46cd7e20a2aecb91097ae8cc-Abstract-Conference.html)] · ядро · источник: Pluralistic Alignment
- **HelpSteer2 2024-6**, 2024 — [[статья](https://arxiv.org/abs/2406.08673)] · смежная тема · источник: Awesome LLM Datasets
- **Imitation Beyond Expectation Using Pluralistic Stochastic Dominance**, 2025 — [[статья](https://openreview.net/forum?id=YX5DHa9OfX)] · ядро · источник: Pluralistic Alignment
- **Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.**, 2022 — [[статья](https://arxiv.org/abs/2209.14375)] · ядро · источник: Alignment Goal Survey
- **Improving the Distributional Alignment of LLMs using Supervision**, 2025 — [[статья](https://arxiv.org/abs/2507.00439)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1326/)] · ядро · источник: STONIC bibliography
- **Internal Value Alignment in Large Language Models through Controlled Value Vector Activation**, 2025 — [[статья](https://arxiv.org/abs/2507.11316)] · ядро · источник: AIDAS Values & Pluralism
- **Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts**, 2024 — [[статья](https://aclanthology.org/2024.findings-emnlp.620/)] · ядро · источник: Pluralistic Alignment
- **Justifications for Democratizing AI Alignment and Their Prospects**, 2025 — [[статья](https://arxiv.org/abs/2507.19548)] · ядро · источник: AIDAS Values & Pluralism
- **Language Model Alignment in Multilingual Trolley Problems**, 2024 — [[статья](https://arxiv.org/abs/2407.02273)] · ядро · источник: Pluralistic Alignment
- **Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1028/)] · ядро · источник: Pluralistic Alignment
- **Language Models are Alignable Decision-Makers: Dataset and Application to the Medical Triage Domain**, 2024 — [[статья](https://aclanthology.org/2024.naacl-industry.18/)] · ядро · источник: Pluralistic Alignment
- **Language Models Resist Alignment: Evidence From Data Compression, ACL 2025 Best Paper**, 2025 — [[статья](https://arxiv.org/abs/2406.06144)] · смежная тема · источник: LLM Social Science
- **Large Language Model Alignment: A Survey**, 2023 — [[статья](https://arxiv.org/abs/2309.15025)] · ядро · источник: Pluralistic Alignment, LLM Social Science
- **Large Language Models as Optimizers**, 2024 — [[статья](https://openreview.net/forum?id=Bb4VGOWELI)] · ядро · источник: Pluralistic Alignment
- **Large pre-trained language models contain human-like biases of what is right and wrong to do. Schramowski et al. Nature Machine Intelligence 2022.**, 2022 — [[статья](https://arxiv.org/abs/2103.11790)] · ядро · источник: Alignment Goal Survey
- **Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability**, 2025 — [[статья](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.90/)] · ядро · источник: Pluralistic Alignment
- **LoRe: Personalizing LLMs via Low-Rank Reward Modeling**, 2025 — [[статья](https://arxiv.org/abs/2504.14439)] · ядро · источник: Personalized Alignment, Pluralistic Alignment
- **MallowsPO: Fine-Tune Your LLM with Preference Dispersions**, 2024 — [[статья](https://arxiv.org/abs/2405.14953)] · ядро · источник: Pluralistic Alignment
- **MAP: Multi-Human-Value Alignment Palette**, 2024 — [[статья](https://arxiv.org/abs/2410.19198)] · ядро · источник: AIDAS Values & Pluralism
- **MaxMin-RLHF: Alignment with Diverse Human Preferences**, 2024 — [[статья](https://arxiv.org/abs/2402.08925)] · ядро · источник: Pluralistic Alignment
- **MixDPO: Modeling Preference Strength for Pluralistic Alignment**, 2026 — [[статья](https://arxiv.org/abs/2601.06180)] · ядро · источник: Pluralistic Alignment
- **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-main.240/)] · ядро · источник: Pluralistic Alignment
- **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration**, 2024 — [[статья](https://arxiv.org/abs/2406.15951)] · ядро · источник: AIDAS Values & Pluralism, Personalized Alignment, LLM Social Science
- **Moral Alignment for LLM Agents**, 2024 — [[статья](https://arxiv.org/abs/2410.01639)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning**, 2025 — [[статья](https://arxiv.org/abs/2511.12271)] · ядро · источник: AIDAS Values & Pluralism
- **Multi-Value Alignment for LLMs via Value Decorrelation and Extrapolation**, 2025 — [[статья](https://arxiv.org/abs/2511.17579)] · ядро · источник: AIDAS Values & Pluralism
- **NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.120/)] · ядро · источник: Pluralistic Alignment
- **Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.345/)] · ядро · источник: Pluralistic Alignment
- **OASIS: Open Agent Social Interaction Simulations with One Million Agents**, 2024 — [[статья](https://arxiv.org/abs/2411.11581)] · ядро · источник: Pluralistic Alignment
- **Optimizing generative AI by backpropagating language model feedback, Nature**, 2025 — [[статья](https://nature.com/articles/s41586-025-08661-4)] · смежная тема · источник: LLM Social Science
- **PAD: Personalized Alignment of LLMs at Decoding-Time**, 2024 — [[статья](https://arxiv.org/abs/2410.04070)] · ядро · источник: AIDAS Values & Pluralism, Personalized Alignment, LLM Social Science
- **Pairwise Calibrated Rewards for Pluralistic Alignment**, 2025 — [[статья](https://arxiv.org/abs/2506.06298)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences**, 2024 — [[статья](https://arxiv.org/abs/2406.08469)] · ядро · источник: Pluralistic Alignment
- **Parametric Social Identity Injection and Diversification in Public Opinion Simulation**, 2026 — [[статья](https://arxiv.org/abs/2603.16142)] · ядро · источник: AIDAS Values & Pluralism
- **PERSONA: A Reproducible Testbed for Pluralistic Alignment**, 2025 — [[статья](https://aclanthology.org/2025.coling-main.752/)] · ядро · источник: Pluralistic Alignment
- **Personality Alignment of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2408.11779)] · ядро · источник: Pluralistic Alignment
- **PICACO: Pluralistic In-Context Value Alignment of LLMs via Total Correlation Optimization**, 2025 — [[статья](https://arxiv.org/abs/2507.16679)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **PKU-SafeRLHF 2023-7**, 2023 — [[статья](https://arxiv.org/abs/2307.04657)] · смежная тема · источник: Awesome LLM Datasets
- **Pluralistic Alignment for Healthcare: A Role-Driven Framework**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.1596/)] · ядро · источник: Pluralistic Alignment
- **PluralLLM: Pluralistic Alignment in LLMs via Federated Learning**, 2025 — [[статья](https://dl.acm.org/doi/abs/10.1145/3722570.3726898)] · ядро · источник: Pluralistic Alignment
- **Policy Prototyping for LLMs: Pluralistic Alignment via Interactive and Collaborative Policymaking**, 2024 — [[статья](https://arxiv.org/abs/2409.08622)] · ядро · источник: Pluralistic Alignment, LLM Social Science
- **Position: A Roadmap to Impactful Pluralistic Alignment Research**, 2026 — [[статья](https://arxiv.org/abs/2607.22305)] · ядро · источник: AIDAS Values & Pluralism
- **Position: Align AI to Our Aspirations, Not Our Flaws**, 2026 — [[статья](https://arxiv.org/abs/2606.13755)] · ядро · источник: AIDAS Values & Pluralism
- **Position: The Alignment Community is Unintentionally Building a Censor's Toolkit**, 2026 — [[статья](https://openreview.net/forum?id=dy2HwmOvFX)] · ядро · источник: AIDAS Values & Pluralism
- **Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles**, 2025 — [[статья](https://arxiv.org/abs/2502.06059)] · смежная тема · источник: LLM Social Science
- **ProgressGym: Alignment with a Millennium of Moral Progress**, 2024 — [[статья](https://arxiv.org/abs/2406.20087)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs**, 2024 — [[статья](https://aclanthology.org/2024.acl-long.381/)] · ядро · источник: Pluralistic Alignment
- **Reflective Verbal Reward Design for Pluralistic Alignment**, 2025 — [[статья](https://arxiv.org/abs/2506.17834)] · ядро · источник: Pluralistic Alignment
- **Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem**, 2026 — [[статья](https://arxiv.org/abs/2604.20805)] · ядро · источник: AIDAS Values & Pluralism
- **Rethinking Machine Ethics -- Can LLMs Perform Moral Reasoning through the Lens of Moral Theories?**, 2023 — [[статья](https://arxiv.org/abs/2308.15399)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Reward Model Perspectives: Whose Opinions Do Reward Models Reward?**, 2025 — [[статья](https://arxiv.org/abs/2510.06391)] · ядро · источник: AIDAS Values & Pluralism
- **Robust Multi-Objective Controlled Decoding of Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2503.08796)] · ядро · источник: Pluralistic Alignment
- **Role Steering of Language Models for Social Simulations**, 2026 — [[статья](https://arxiv.org/abs/2608.00023)] · ядро · источник: AIDAS Values & Pluralism
- **SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation**, 2024 — [[статья](https://arxiv.org/abs/2410.16665)] · смежная тема · источник: LLM Social Science
- **Scopes of Alignment, 2025.01, AAAI 2025 workshop**, 2025 — [[статья](https://arxiv.org/abs/2501.12405)] · смежная тема · источник: LLM Social Science
- **Self-Alignment: Improving Alignment of Cultural Values in LLMs via In-Context Learning**, 2024 — [[статья](https://arxiv.org/abs/2408.16482)] · ядро · источник: Pluralistic Alignment
- **Self-Pluralising Culture Alignment for Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.350/)] · ядро · источник: Pluralistic Alignment
- **Simple Role Assignment is Extraordinarily Effective for Safety Alignment, ACL 2026 Findings**, 2026 — [[статья](https://arxiv.org/abs/2602.00061)] · смежная тема · источник: LLM Social Science
- **Social Simulacra: Creating Populated Prototypes for Social Computing Systems**, 2022 — [[статья](https://dl.acm.org/doi/abs/10.1145/3526113.3545616)] · ядро · источник: Pluralistic Alignment
- **Societal Alignment Frameworks Can Improve LLM Alignment**, 2025 — [[статья](https://arxiv.org/abs/2503.00069)] · ядро · источник: AIDAS Values & Pluralism
- **Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.162/)] · ядро · источник: Pluralistic Alignment
- **SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment**, 2025 — [[статья](https://aclanthology.org/2025.findings-acl.41/)] · ядро · источник: Pluralistic Alignment
- **Steerable Pluralism: Pluralistic Alignment via Few-Shot Comparative Regression**, 2025 — [[статья](https://arxiv.org/abs/2508.08509)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF**, 2023 — [[статья](https://aclanthology.org/2023.findings-emnlp.754/)] · ядро · источник: Pluralistic Alignment
- **STELA: a community-centred approach to norm elicitation for AI alignment, 2024.03, Nature Scientific Reports**, 2024 — [[статья](https://nature.com/articles/s41598-024-56648-4)] · смежная тема · источник: LLM Social Science
- **Strong and weak alignment of large language models with human values**, 2024 — [[статья](https://arxiv.org/abs/2408.04655)] · ядро · источник: AIDAS Values & Pluralism
- **Strong and weak alignment of large language models with human values, 2024.08, Nature Scientific Reports**, 2024 — [[статья](https://nature.com/articles/s41598-024-70031-3)] · смежная тема · источник: LLM Social Science
- **Survey-to-Behavior: Downstream Alignment of Human Values in LLMs via Survey Questions**, 2025 — [[статья](https://arxiv.org/abs/2508.11414)] · ядро · источник: AIDAS Values & Pluralism
- **The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models**, 2026 — [[статья](https://aclanthology.org/2026.eacl-long.305/)] · ядро · источник: Pluralistic Alignment
- **The Sign Estimator: LLM Alignment in the Face of Choice Heterogeneity**, 2025 — [[статья](https://arxiv.org/abs/2510.23965)] · ядро · источник: AIDAS Values & Pluralism
- **The Specification Trap: Why Static Value Alignment Alone Is Insufficient for Robust Alignment**, 2025 — [[статья](https://arxiv.org/abs/2512.03048)] · ядро · источник: AIDAS Values & Pluralism
- **The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning**, 2023 — [[статья](https://arxiv.org/abs/2312.01552)] · ядро · источник: Pluralistic Alignment
- **Towards Better Value Principles for Large Language Model Alignment: A Systematic Evaluation and Enhancement**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1408/)] · ядро · источник: AIDAS Values & Pluralism, STONIC bibliography, LLM Social Science
- **Towards Scalable Automated Alignment of LLMs: A Survey**, 2024 — [[статья](https://arxiv.org/abs/2406.01252)] · ядро · источник: Pluralistic Alignment
- **Training Socially Aligned Language Models in Simulated Human Society**, 2023 — [[статья](https://arxiv.org/abs/2305.16960)] · смежная тема · источник: Awesome LLM Datasets, LLM Social Science
- **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.1532/)] · ядро · источник: STONIC bibliography
- **Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights**, 2025 — [[статья](https://arxiv.org/abs/2506.06404)] · ядро · источник: AIDAS Values & Pluralism
- **Unintended Impacts of LLM Alignment on Global Representation**, 2024 — [[статья](https://arxiv.org/abs/2402.15018)] · смежная тема · источник: Awesome Cultural NLP
- **Value Alignment from Unstructured Text**, 2024 — [[статья](https://aclanthology.org/2024.emnlp-industry.81/)] · ядро · источник: Pluralistic Alignment
- **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value**, 2024 — [[статья](https://aclanthology.org/2024.naacl-long.486/)] · ядро · источник: Pluralistic Alignment, STONIC bibliography
- **ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs**, 2025 — [[статья](https://aclanthology.org/2025.winlp-main.15/)] · ядро · источник: STONIC bibliography
- **ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making**, 2025 — [[статья](https://arxiv.org/abs/2503.04569)] · ядро · источник: AIDAS Values & Pluralism
- **VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2603.18113)] · ядро · источник: AIDAS Values & Pluralism
- **VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment**, 2026 — [[статья](https://arxiv.org/abs/2603.04822)] · ядро · источник: AIDAS Values & Pluralism
- **VISPA: Pluralistic Alignment via Automatic Value Selection and Activation**, 2026 — [[статья](https://arxiv.org/abs/2601.12758)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment
- **What are human values, and how do we align AI to them?**, 2024 — [[статья](https://arxiv.org/abs/2404.10636)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Wide Reflective Equilibrium in LLM Alignment: Bridging Moral Epistemology and AI Safety**, 2025 — [[статья](https://arxiv.org/abs/2506.00415)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-value-representation-and-model-internals"></a>

#### 📐 Представления ценностей и внутренние механизмы моделей · 44

- **A Method for Learning Value Systems in Generative AI**, 2026 — [[статья](https://arxiv.org/abs/2607.16903)] · ядро · источник: AIDAS Values & Pluralism
- **AI and My Values: User Perceptions of LLMs' Ability to Extract, Embody, and Explain Human Values from Casual Conversations**, 2026 — [[статья](https://arxiv.org/abs/2601.22440)] · ядро · источник: AIDAS Values & Pluralism
- **Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection**, 2026 — [[статья](https://arxiv.org/abs/2607.05052)] · ядро · источник: AIDAS Values & Pluralism
- **Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment**, 2026 — [[статья](https://arxiv.org/abs/2604.12851)] · ядро · источник: AIDAS Values & Pluralism
- **Culturally Grounded Personas in Large Language Models: Characterization and Alignment with Socio-Psychological Value Frameworks**, 2026 — [[статья](https://arxiv.org/abs/2601.22396)] · ядро · источник: AIDAS Values & Pluralism
- **Do Differences in Values Influence Disagreements in Online Discussions?**, 2023 — [[статья](https://arxiv.org/abs/2310.15757)] · ядро · источник: AIDAS Values & Pluralism
- **Do Schwartz Higher-Order Values Help Sentence-Level Human Value Detection? A Study of Hierarchical Gating and Calibration**, 2026 — [[статья](https://arxiv.org/abs/2602.00913)] · ядро · источник: AIDAS Values & Pluralism
- **EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs**, 2025 — [[статья](https://arxiv.org/abs/2505.12792)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Emergent Moral Representations in Large Language Models Aligns with Human Conceptual, Neural, and Behavioral Moral Structure**, 2025 — [[статья](https://doi.org/10.21203/rs.3.rs-8270539/v1)] · ядро · источник: AIDAS Values & Pluralism
- **Enhancing Stance Classification on Social Media Using Quantified Moral Foundations**, 2023 — [[статья](https://arxiv.org/abs/2310.09848)] · ядро · источник: AIDAS Values & Pluralism
- **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.585/)] · ядро · источник: STONIC bibliography
- **Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2502.02444)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Growth First, Care Second? Tracing the Landscape of LLM Value Preferences in Everyday Dilemmas**, 2026 — [[статья](https://arxiv.org/abs/2602.04456)] · ядро · источник: AIDAS Values & Pluralism
- **High-Dimension Human Value Representation in Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.naacl-long.274/)] · ядро · источник: STONIC bibliography
- **High-Dimension Human Value Representation in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2404.07900)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum**, 2026 — [[статья](https://arxiv.org/abs/2601.14172)] · ядро · источник: AIDAS Values & Pluralism
- **Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture**, 2026 — [[статья](https://arxiv.org/abs/2605.27373)] · ядро · источник: AIDAS Values & Pluralism
- **Investigating Human Values in Online Communities**, 2024 — [[статья](https://arxiv.org/abs/2402.14177)] · ядро · источник: AIDAS Values & Pluralism
- **Learning the Value Systems of Societies from Preferences**, 2025 — [[статья](https://arxiv.org/abs/2507.20728)] · ядро · источник: AIDAS Values & Pluralism
- **Learning the Value Systems of Societies with Preference-based Multi-objective Reinforcement Learning**, 2026 — [[статья](https://arxiv.org/abs/2602.08835)] · ядро · источник: AIDAS Values & Pluralism
- **Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer**, 2026 — [[статья](https://arxiv.org/abs/2606.11018)] · ядро · источник: AIDAS Values & Pluralism
- **Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora**, 2026 — [[статья](https://arxiv.org/abs/2605.22660)] · ядро · источник: AIDAS Values & Pluralism
- **MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions**, 2024 — [[статья](https://arxiv.org/abs/2403.07678)] · ядро · источник: AIDAS Values & Pluralism
- **Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning**, 2024 — [[статья](https://arxiv.org/abs/2401.17228)] · ядро · источник: AIDAS Values & Pluralism
- **More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts**, 2026 — [[статья](https://arxiv.org/abs/2605.22641)] · ядро · источник: AIDAS Values & Pluralism
- **MoVa: Towards Generalizable Classification of Human Morals and Values**, 2025 — [[статья](https://arxiv.org/abs/2509.24216)] · ядро · источник: AIDAS Values & Pluralism
- **Probing Ethical Framework Representations in Large Language Models: Structure, Entanglement, and Methodological Challenges**, 2026 — [[статья](https://arxiv.org/abs/2603.23659)] · ядро · источник: AIDAS Values & Pluralism
- **SemEval-2023 Task 4: ValueEval: Identification of Human Values Behind Arguments**, 2023 — [[статья](https://aclanthology.org/2023.semeval-1.313/)] · ядро · источник: AIDAS Values & Pluralism, STONIC bibliography
- **SOLAR: Towards Characterizing Subjectivity of Individuals through Modeling Value Conflicts and Trade-offs**, 2025 — [[статья](https://arxiv.org/abs/2504.12633)] · ядро · источник: AIDAS Values & Pluralism
- **The Value of Nothing: Multimodal Extraction of Human Values Expressed by TikTok Influencers**, 2025 — [[статья](https://arxiv.org/abs/2501.11770)] · ядро · источник: AIDAS Values & Pluralism
- **Tracing Moral Foundations in Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2601.05437)] · ядро · источник: AIDAS Values & Pluralism
- **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs**, 2025 — [[статья](https://aclanthology.org/2025.findings-emnlp.501/)] · ядро · источник: STONIC bibliography
- **Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs**, 2025 — [[статья](https://arxiv.org/abs/2502.08640)] · ядро · источник: AIDAS Values & Pluralism
- **Value Alignment of Social Media Ranking Algorithms**, 2025 — [[статья](https://arxiv.org/abs/2509.14434)] · ядро · источник: AIDAS Values & Pluralism
- **Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values**, 2023 — [[статья](https://arxiv.org/abs/2311.10766)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties**, 2023 — [[статья](https://arxiv.org/abs/2309.00779)] · ядро · источник: AIDAS Values & Pluralism, Pluralistic Alignment, LLM Social Science
- **Value Lens: Using Large Language Models to Understand Human Values**, 2025 — [[статья](https://arxiv.org/abs/2512.15722)] · ядро · источник: AIDAS Values & Pluralism
- **Value Profiles for Encoding Human Variation**, 2025 — [[статья](https://arxiv.org/abs/2503.15484)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models**, 2026 — [[статья](https://arxiv.org/abs/2602.03160)] · ядро · источник: AIDAS Values & Pluralism
- **ValueNet: A New Dataset for Human Value Driven Dialogue System**, 2021 — [[статья](https://arxiv.org/abs/2112.06346)] · ядро · источник: AIDAS Values & Pluralism
- **Values in the Wild: Discovering and Analyzing Values in Real-World Language Model Interactions**, 2025 — [[статья](https://arxiv.org/abs/2504.15236)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **What does a Text Classifier Learn about Morality? An Explainable Method for Cross-Domain Comparison of Moral Rhetoric**, 2023 — [[статья](https://aclanthology.org/2023.acl-long.789/)] · ядро · источник: AIDAS Values & Pluralism
- **Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study**, 2026 — [[статья](https://arxiv.org/abs/2607.20270)] · ядро · источник: AIDAS Values & Pluralism
- **Whose Values? Measuring the (Subjective) Expression of Basic Human Values in Social Media**, 2025 — [[статья](https://arxiv.org/abs/2511.08453)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-measurement-and-profiling"></a>

#### 📏 Измерение и профилирование · 87

- **(GLOBE) Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2406.17675)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches**, 2024 — [[статья](https://arxiv.org/abs/2404.12744)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(Others & custom) CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility**, 2023 — [[статья](https://arxiv.org/abs/2307.09705)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets, LLM Psychometrics
- **(Others & custom) Measurement of LLM’s Philosophies of Human Nature**, 2025 — [[статья](https://arxiv.org/abs/2504.02304)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Measuring Spiritual Values and Bias of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2410.11647)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Will AI Tell Lies to Save Sick Children? Litmus-Testing AI Values Prioritization with AIRiskDilemmas**, 2025 — [[статья](https://arxiv.org/abs/2505.14633)] · ядро · источник: LLM Psychometrics
- **(Schwartz) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science**, 2023 — [[статья](https://journals.sagepub.com/doi/full/10.1177/17456916231214460)] · ядро · источник: LLM Psychometrics
- **(Schwartz) Improving Language Model Personas via Rationalization with Psychological Scaffolds**, 2025 — [[статья](https://arxiv.org/abs/2504.17993)] · ядро · источник: LLM Psychometrics
- **(Schwartz) Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025**, 2025 — [[статья](https://ojs.aaai.org/index.php/AAAI/article/view/34839)] · ядро · источник: LLM Psychometrics
- **(Schwartz) The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas**, 2025 — [[статья](https://arxiv.org/abs/2505.18154)] · ядро · источник: LLM Psychometrics
- **(Schwartz) ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs**, 2024 — [[статья](https://arxiv.org/abs/2409.09586)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(Schwartz) What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory**, 2023 — [[статья](https://arxiv.org/abs/2304.03612)] · ядро · источник: LLM Psychometrics
- **(Schwartz) When Prompting Fails to Sway: Inertia in Moral and Value Judgments of Large Language Models, NeurIPS 2022**, 2022 — [[статья](https://arxiv.org/abs/2408.09049)] · ядро · источник: LLM Psychometrics
- **(Schwartz) Who is GPT-3? An Exploration of Personality, Values and Demographics, EMNLP 2022 NLP+CSS workshop**, 2022 — [[статья](https://arxiv.org/abs/2209.14338)] · ядро · источник: LLM Psychometrics
- **(VSM) Cultural Value Differences of LLMs: Prompt, Language, and Model Size**, 2024 — [[статья](https://arxiv.org/abs/2407.16891)] · ядро · источник: LLM Psychometrics
- **(WVS) Exploring Large Language Models on Cross-Cultural Values in Connection with Training Methodology**, 2024 — [[статья](https://arxiv.org/abs/2412.08846)] · ядро · источник: LLM Psychometrics
- **(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)**, 2026 — [[статья](https://arxiv.org/abs/2509.01418)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(WVS) Only a Little to the Left: A Theory-grounded Measure of Political Bias in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2503.16148)] · ядро · источник: LLM Psychometrics
- **A Scalable Approach to Evaluating Moral Sensitivity in LLMs**, 2026 — [[статья](https://arxiv.org/abs/2607.02972)] · ядро · источник: AIDAS Values & Pluralism
- **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference**, 2025 — [[статья](https://arxiv.org/abs/2505.13531)] · ядро · источник: AIDAS Values & Pluralism
- **AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference**, 2026 — [[статья](https://openreview.net/forum?id=qNlTH4kYJZ)] · ядро · источник: STONIC bibliography
- **Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?**, 2025 — [[статья](https://arxiv.org/abs/2506.00751)] · ядро · источник: AIDAS Values & Pluralism
- **Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact**, 2026 — [[статья](https://arxiv.org/abs/2606.20205)] · ядро · источник: AIDAS Values & Pluralism
- **Are Language Models Sensitive to Morally Irrelevant Distractors?**, 2026 — [[статья](https://arxiv.org/abs/2602.09416)] · ядро · источник: AIDAS Values & Pluralism
- **Are Large Language Models Consistent over Value-laden Questions?**, 2024 — [[статья](https://arxiv.org/abs/2407.02996)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Are LLMs Bad at Moral Reasoning?**, 2026 — [[статья](https://arxiv.org/abs/2606.11635)] · ядро · источник: AIDAS Values & Pluralism
- **Are the Values of LLMs Structurally Aligned with Humans? A Causal Perspective**, 2024 — [[статья](https://arxiv.org/abs/2501.00581)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Beyond Value Benchmarks: Measuring Value-Structure Alignment in Large Language Models via Symmetric Q-Sorts**, 2026 — [[статья](https://arxiv.org/abs/2606.21939)] · ядро · источник: AIDAS Values & Pluralism
- **Can Language Models Reason about Individualistic Human Values and Preferences?**, 2024 — [[статья](https://arxiv.org/abs/2410.03868)] · ядро · источник: AIDAS Values & Pluralism
- **Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?**, 2026 — [[статья](https://arxiv.org/abs/2606.31213)] · ядро · источник: AIDAS Values & Pluralism
- **Can Revealed Preferences Clarify LLM Alignment and Steering?**, 2026 — [[статья](https://arxiv.org/abs/2605.08556)] · ядро · источник: AIDAS Values & Pluralism
- **CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses**, 2024 — [[статья](https://arxiv.org/abs/2407.10725)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Context-Value-Action Architecture for Value-Driven Large Language Model Agents**, 2026 — [[статья](https://arxiv.org/abs/2604.05939)] · ядро · источник: AIDAS Values & Pluralism
- **Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences**, 2025 — [[статья](https://arxiv.org/abs/2511.02109)] · ядро · источник: AIDAS Values & Pluralism
- **Do Language Models Think Consistently? A Study of Value Preferences Across Varying Response Lengths**, 2025 — [[статья](https://arxiv.org/abs/2506.02481)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Do LLMs have Consistent Values?**, 2024 — [[статья](https://arxiv.org/abs/2407.12878)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Do Role-Playing Agents Practice What They Preach? Belief-Behavior Consistency in LLM-Based Simulations of Human Trust**, 2025 — [[статья](https://arxiv.org/abs/2507.02197)] · ядро · источник: AIDAS Values & Pluralism
- **Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2509.24319)] · ядро · источник: AIDAS Values & Pluralism
- **Every Act Has Its Price: Compressed Moral Composition in Frontier LLMs**, 2026 — [[статья](https://arxiv.org/abs/2606.11232)] · ядро · источник: AIDAS Values & Pluralism
- **Exploring Multilingual Concepts of Human Value in Large Language Models: Is Value Alignment Consistent, Transferable and Controllable across Languages?**, 2024 — [[статья](https://arxiv.org/abs/2402.18120)] · ядро · источник: AIDAS Values & Pluralism
- **Following the Whispers of Values: Unraveling Neural Mechanisms Behind Value-Oriented Behaviors in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2504.04994)] · ядро · источник: AIDAS Values & Pluralism
- **From Stability to Inconsistency: A Study of Moral Preferences in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2504.06324)] · ядро · источник: AIDAS Values & Pluralism
- **Generative Value Conflicts Reveal LLM Priorities**, 2025 — [[статья](https://arxiv.org/abs/2509.25369)] · ядро · источник: AIDAS Values & Pluralism
- **Heterogeneous Value Alignment Evaluation for Large Language Models**, 2023 — [[статья](https://arxiv.org/abs/2305.17147)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **How do LLMs reflect human moral foundations? a study using the moral foundations framework**, 2026 — [[статья](https://tandfonline.com/doi/full/10.1080/29974100.2026.2678495)] · ядро · источник: AIDAS Values & Pluralism
- **Human Psychometric Questionnaires Mischaracterize LLM Behavior**, 2025 — [[статья](https://arxiv.org/abs/2509.10078)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Implicit Values Embedded in How Humans and LLMs Complete Subjective Everyday Tasks**, 2025 — [[статья](https://arxiv.org/abs/2510.03384)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Incoherent Values? Probing LLM Preferences Through Parametric Variation**, 2026 — [[статья](https://arxiv.org/abs/2606.21102)] · ядро · источник: AIDAS Values & Pluralism
- **Investigating Value-Reasoning Reliability in Small Large Language Models**, 2025 — [[статья](https://aclanthology.org/2025.emnlp-main.395/)] · ядро · источник: AIDAS Values & Pluralism
- **LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values**, 2026 — [[статья](https://arxiv.org/abs/2606.13944)] · ядро · источник: AIDAS Values & Pluralism
- **LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2408.01460)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests**, 2025 — [[статья](https://arxiv.org/abs/2510.22170)] · ядро · источник: AIDAS Values & Pluralism
- **Measurement and Fairness**, 2021 — [[статья](https://doi.org/10.1145/3442188.3445901)] · ядро · источник: STONIC bibliography
- **Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2409.12106)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Measuring human and AI values based on generative psychometrics with large language models**, 2025 — [[статья](https://doi.org/10.1609/aaai.v39i25.34839)] · ядро · источник: STONIC bibliography
- **Measuring the Authority Stack of AI Systems: Empirical Analysis of 366,120 Forced-Choice Responses Across 8 AI Models**, 2026 — [[статья](https://arxiv.org/abs/2604.11216)] · ядро · источник: AIDAS Values & Pluralism
- **Mechanistic Origin of Moral Indifference in Language Models**, 2026 — [[статья](https://arxiv.org/abs/2603.15615)] · ядро · источник: AIDAS Values & Pluralism
- **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**, 2025 — [[статья](https://arxiv.org/abs/2501.15463)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation**, 2026 — [[статья](https://arxiv.org/abs/2605.12515)] · ядро · источник: AIDAS Values & Pluralism
- **Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs**, 2026 — [[статья](https://arxiv.org/abs/2601.08634)] · ядро · источник: AIDAS Values & Pluralism
- **Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability**, 2026 — [[статья](https://arxiv.org/abs/2605.03217)] · ядро · источник: AIDAS Values & Pluralism
- **Moral Susceptibility and Robustness under Persona Role-Play in Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2511.08565)] · ядро · источник: AIDAS Values & Pluralism
- **Multimodal understanding of human values in videos: A benchmark dataset and PLM-based method**, 2025 — [[статья](https://sciencedirect.com/science/article/pii/S0925231225008422)] · ядро · источник: AIDAS Values & Pluralism
- **Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs**, 2026 — [[статья](https://arxiv.org/abs/2606.12731)] · ядро · источник: AIDAS Values & Pluralism
- **On the Credibility of Evaluating LLMs using Survey Questions**, 2026 — [[статья](https://arxiv.org/abs/2602.04033)] · ядро · источник: AIDAS Values & Pluralism
- **Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses**, 2026 — [[статья](https://arxiv.org/abs/2605.28911)] · ядро · источник: AIDAS Values & Pluralism
- **Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses**, 2026 — [[статья](https://arxiv.org/abs/2507.07188)] · ядро · источник: AIDAS Values & Pluralism
- **Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation**, 2026 — [[статья](https://arxiv.org/abs/2607.05554)] · ядро · источник: AIDAS Values & Pluralism
- **Pseudo-Deliberation in Language Models: When Reasoning Fails to Align Values and Actions**, 2026 — [[статья](https://arxiv.org/abs/2605.09893)] · ядро · источник: AIDAS Values & Pluralism
- **Quantifying Data Contamination in Psychometric Evaluations of LLMs**, 2025 — [[статья](https://arxiv.org/abs/2510.07175)] · ядро · источник: AIDAS Values & Pluralism
- **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing**, 2024 — [[статья](https://arxiv.org/abs/2406.14230)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing**, 2025 — [[статья](https://openreview.net/forum?id=0REM9ydeLZ)] · ядро · источник: STONIC bibliography
- **Revisiting LLM Value Probing Strategies: Are They Robust and Expressive?**, 2025 — [[статья](https://arxiv.org/abs/2507.13490)] · ядро · источник: AIDAS Values & Pluralism
- **Superficial Beliefs in LLM Decision-Making**, 2026 — [[статья](https://arxiv.org/abs/2606.11016)] · ядро · источник: AIDAS Values & Pluralism
- **The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models**, 2025 — [[статья](https://arxiv.org/abs/2512.03026)] · ядро · источник: AIDAS Values & Pluralism
- **Understanding How Value Neurons Shape the Generation of Specified Values in LLMs**, 2025 — [[статья](https://arxiv.org/abs/2505.17712)] · ядро · источник: AIDAS Values & Pluralism
- **Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability**, 2026 — [[статья](https://arxiv.org/abs/2603.16017)] · ядро · источник: AIDAS Values & Pluralism
- **Untangling Input Language from Reasoning Language: A Diagnostic Framework for Cross-Lingual Moral Alignment in LLMs**, 2026 — [[статья](https://arxiv.org/abs/2601.10257)] · ядро · источник: AIDAS Values & Pluralism
- **Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values**, 2025 — [[статья](https://arxiv.org/abs/2501.07071)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **Value Drifts: Tracing Value Alignment During LLM Post-Training**, 2025 — [[статья](https://arxiv.org/abs/2510.26707)] · ядро · источник: AIDAS Values & Pluralism
- **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items**, 2025 — [[статья](https://aclanthology.org/2025.acl-long.838/)] · ядро · источник: STONIC bibliography
- **Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items**, 2025 — [[статья](https://arxiv.org/abs/2505.01015)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts**, 2024 — [[статья](https://arxiv.org/abs/2411.11479)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics
- **ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models**, 2024 — [[статья](https://arxiv.org/abs/2406.04214)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models**, 2023 — [[статья](https://arxiv.org/abs/2310.00378)] · ядро · источник: AIDAS Values & Pluralism, LLM Psychometrics, LLM Social Science
- **ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems**, 2026 — [[статья](https://arxiv.org/abs/2602.08567)] · ядро · источник: AIDAS Values & Pluralism
- **Whose Alignment? Comparing LLM Process Alignment Across Diverse Organizational Decision Contexts**, 2026 — [[статья](https://arxiv.org/abs/2605.25256)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-other-and-adjacent-value-research"></a>

#### 📎 Другие и смежные исследования ценностей · 45

- **10.1186/s40537-024-00986-7**, 2024 — [[статья](https://link.springer.com/article/10.1186/s40537-024-00986-7)] · смежная тема · источник: Awesome Cultural NLP
- **A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle**, 2021 — [[статья](https://doi.org/10.1145/3465416.3483305)] · ядро · источник: STONIC bibliography
- **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive, ACL 2025 Best Paper**, 2025 — [[статья](https://arxiv.org/abs/2402.11005)] · смежная тема · источник: LLM Social Science
- **Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective**, 2024 — [[статья](https://arxiv.org/abs/2408.04638)] · смежная тема · источник: LLM Social Science
- **Automated Mining of Structured Knowledge from Text in the Era of Large Language Models, 2024.08, KDD 2024**, 2024 — [[статья](https://dl.acm.org/doi/pdf/10.1145/3637528.3671469)] · смежная тема · источник: LLM Social Science
- **Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral**, 2026 — [[статья](https://arxiv.org/abs/2603.13890)] · смежная тема · источник: LLM Social Science
- **Chatbotarenaconversations 2023-6**, 2023 — [[статья](https://arxiv.org/abs/2306.05685)] · смежная тема · источник: Awesome LLM Datasets
- **Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science**, 2018 — [[статья](https://aclanthology.org/Q18-1041/)] · ядро · источник: STONIC bibliography
- **EMNLP Main 18**, 2023 — [[статья](https://aclanthology.org/2023.emnlp-main.18/)] · смежная тема · источник: Awesome Cultural NLP
- **Exploring Changes in Nation Perception with Nationality-Assigned Personas in LLMs**, 2024 — [[статья](https://arxiv.org/abs/2406.13993)] · смежная тема · источник: Awesome Cultural NLP
- **Fairness and Abstraction in Sociotechnical Systems**, 2019 — [[статья](https://doi.org/10.1145/3287560.3287598)] · ядро · источник: STONIC bibliography
- **Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs, ACL 2025 Best Paper**, 2025 — [[статья](https://arxiv.org/abs/2502.01926)] · смежная тема · источник: LLM Social Science
- **Generative AI Meets Open-Ended Survey Responses: Research Participant Use of AI and Homogenization, 2025.05, Sociological Methods & Research**, 2025 — [[статья](https://journals.sagepub.com/doi/10.1177/00491241251327130)] · смежная тема · источник: LLM Social Science
- **Generative language models exhibit social identity biases, Nature Computational Science**, 2025 — [[статья](https://nature.com/articles/s43588-024-00741-1)] · смежная тема · источник: LLM Social Science
- **GIVL: Improving Geographical Inclusivity of Vision-Language Models with Pre-Training Methods**, 2023 — [[статья](https://arxiv.org/abs/2301.01893)] · смежная тема · источник: Awesome Cultural NLP
- **HG & CI & MC**, 2023 — [[статья](https://arxiv.org/abs/2311.09528)] · смежная тема · источник: Awesome LLM Datasets
- **Holistic Evaluation of Language Models**, 2023 — [[статья](https://openreview.net/forum?id=iO4LZibEqW)] · ядро · источник: STONIC bibliography
- **Large Language Model Safety: A Holistic Survey**, 2024 — [[статья](https://arxiv.org/abs/2412.17686)] · смежная тема · источник: LLM Social Science
- **Large language models (LLM) in computational social science: prospects, current state, and challenges, 2025.03, Social Network Analysis and Mining**, 2025 — [[статья](https://link.springer.com/article/10.1007/s13278-025-01428-9)] · смежная тема · источник: LLM Social Science
- **Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives, 2023.12, Nature humanities and social sciences communications**, 2023 — [[статья](https://arxiv.org/abs/2312.11970)] · смежная тема · источник: LLM Social Science
- **Linhao Yu et al. ACL Findings 2024.**, 2024 — [[статья](https://aclanthology.org/2024.findings-acl.703/)] · смежная тема · источник: Awesome LLM Safety
- **Machine Bias. How Do Generative Language Models Answer Opinion Polls?, 2025.04, Sociological Methods & Research**, 2025 — [[статья](https://doi.org/10.1177/00491241251330582)] · смежная тема · источник: LLM Social Science
- **Nicholas Botzer et al. arXiv 2021.**, 2021 — [[статья](https://arxiv.org/abs/2101.07664)] · смежная тема · источник: Awesome LLM Safety
- **On the Credibility of Evaluating LLMs using Survey Questions**, 2026 — [[статья](https://aclanthology.org/2026.mme-main.2/)] · ядро · источник: STONIC bibliography
- **On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?**, 2021 — [[статья](https://doi.org/10.1145/3442188.3445922)] · ядро · источник: STONIC bibliography
- **On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective**, 2025 — [[статья](https://arxiv.org/abs/2502.14296)] · смежная тема · источник: LLM Social Science
- **Persuading voters using human–artificial intelligence dialogues, Nature**, 2025 — [[статья](https://nature.com/articles/s41586-025-09771-9)] · смежная тема · источник: LLM Social Science
- **Position: AI Evaluation Should Learn from How We Test Humans**, 2023 — [[статья](https://arxiv.org/abs/2306.10512)] · ядро · источник: STONIC bibliography
- **PRM800K 2023-5**, 2023 — [[статья](https://arxiv.org/abs/2305.20050)] · смежная тема · источник: Awesome LLM Datasets
- **Questioning the Survey Responses of Large Language Models, NeurIPS 2024 Oral**, 2024 — [[статья](https://arxiv.org/abs/2306.07951)] · смежная тема · источник: LLM Social Science
- **RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models**, 2020 — [[статья](https://aclanthology.org/2020.findings-emnlp.301/)] · ядро · источник: STONIC bibliography
- **SHP 2021-10 — All — EN — HG**, 2021 — [[статья](https://arxiv.org/abs/2110.08420)] · смежная тема · источник: Awesome LLM Datasets
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025**, 2025 — [[статья](https://arxiv.org/abs/2412.06435)] · смежная тема · источник: LLM Social Science
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025**, 2025 — [[статья](https://openreview.net/forum?id=3ms8EQY7f8)] · смежная тема · источник: LLM Social Science
- **Stick to your role! Stability of personal values expressed in large language models**, 2024 — [[статья](https://doi.org/10.1371/journal.pone.0309114)] · ядро · источник: STONIC bibliography
- **SummarizefromFeedback 2020-9**, 2020 — [[статья](https://arxiv.org/abs/2009.01325)] · смежная тема · источник: Awesome LLM Datasets
- **The AI Gap: How Socioeconomic Status Affects Language Technology Interactions, ACL 2025 Best Social Impact Paper**, 2025 — [[статья](https://arxiv.org/abs/2505.12158)] · смежная тема · источник: LLM Social Science
- **The Rise and Potential of Large Language Model Based Agents: A Survey**, 2023 — [[статья](https://arxiv.org/abs/2309.07864)] · смежная тема · источник: LLM Social Science
- **UltraFeedback**, 2023 — [[статья](https://arxiv.org/abs/2310.01377)] · смежная тема · источник: Awesome LLM Datasets
- **UltraInteract 2024-4**, 2024 — [[статья](https://arxiv.org/abs/2404.02078)] · смежная тема · источник: Awesome LLM Datasets
- **Universals in the Content and Structure of Values: Theoretical Advances and Empirical Tests in 20 Countries**, 1992 — [[статья](https://sciencedirect.com/science/article/pii/S0065260108602816)] · ядро · источник: STONIC bibliography
- **Value-Based Human–Robot-Interaction: A Perceptual Control Theory Approach Toward Socially Intelligent Agents**, 2026 — [[статья](https://link.springer.com/chapter/10.1007/978-3-031-99290-2_7)] · ядро · источник: AIDAS Values & Pluralism
- **WebGPT: Browser-assisted question-answering with human feedback**, 2021 — [[статья](https://arxiv.org/abs/2112.09332)] · смежная тема · источник: Awesome LLM Datasets
- **Who is GPT-3? An exploration of personality, values and demographics**, 2022 — [[статья](https://aclanthology.org/2022.nlpcss-1.24/)] · ядро · источник: STONIC bibliography
- **Zhijing Jin et al. NeurIPS 2022.**, 2022 — [[статья](https://arxiv.org/abs/2210.01478)] · смежная тема · источник: Awesome LLM Safety

### 🧩 Данные, модели, код и дополнительные ресурсы

<a id="catalog-dataset-and-benchmark-artifacts"></a>

#### 💾 Датасеты и артефакты бенчмарков · 28

- **(Others & custom) Towards Measuring the Representation of Subjective Global Opinions in Language Models** — [[данные](https://huggingface.co/datasets/Anthropic/llm_global_opinions)] · ядро · источник: Alignment Goal Survey, LLM Psychometrics
- **2509.17399** — [[данные](https://huggingface.co/datasets/nlip/DIWALI)] · смежная тема · источник: Awesome Cultural NLP
- **A Systematic Survey of Cultural Datasets for Equitable LLM Alignment** — [[данные](https://researchgate.net/publication/398429883_A_Systematic_Survey_of_Cultural_Datasets_for_Equitable_LLM_Alignment)] · ядро · источник: AIDAS Values & Pluralism
- **Big-Math 2025-2** — [[данные](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified)] · смежная тема · источник: Awesome LLM Datasets
- **Chatbotarenaconversations 2023-6** — [[данные](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)] · смежная тема · источник: Awesome LLM Datasets
- **Cultural Commonsense Knowledge for Intercultural Dialogues, CIKM 2024** — [[данные](https://mango.mpi-inf.mpg.de/)] · смежная тема · источник: LLM Social Science
- **CValues 2023-7** — [[данные](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)] · смежная тема · источник: Awesome LLM Datasets
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture** — [[данные](https://huggingface.co/datasets/lyan62/FoodieQA)] · смежная тема · источник: Awesome Cultural NLP
- **HelpSteer2 2024-6** — [[данные](https://huggingface.co/datasets/nvidia/HelpSteer2)] · смежная тема · источник: Awesome LLM Datasets
- **HF Datasets** — [[данные](https://huggingface.co/datasets/MinhDucBui/Multi3Hate)] · смежная тема · источник: Awesome Cultural NLP
- **HG & CI** — [[данные](https://huggingface.co/datasets/openai/webgpt_comparisons)] · смежная тема · источник: Awesome LLM Datasets
- **HG & CI & MC** — [[данные](https://huggingface.co/datasets/nvidia/HelpSteer)] · смежная тема · источник: Awesome LLM Datasets
- **Medical-rlhf 2023-5** — [[данные](https://huggingface.co/datasets/shibing624/medical)] · смежная тема · источник: Awesome LLM Datasets
- **MT-Benchhumanjudgments 2023-6** — [[данные](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)] · смежная тема · источник: Awesome LLM Datasets
- **OASST1pairwiserlhfreward 2023-5** — [[данные](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)] · смежная тема · источник: Awesome LLM Datasets
- **OpenHermesPreferences 2024-3** — [[данные](https://huggingface.co/datasets/argilla/OpenHermesPreferences)] · смежная тема · источник: Awesome LLM Datasets
- **Paper1** — [[данные](https://huggingface.co/datasets/Anthropic/hh-rlhf)] · смежная тема · источник: Awesome LLM Datasets
- **PKU-SafeRLHF 2023-7** — [[данные](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)] · смежная тема · источник: Awesome LLM Datasets
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.** — [[данные](https://huggingface.co/datasets/zhiqings/dromedary-65b-verbose-clone-v0)] · ядро · источник: Alignment Goal Survey
- **SafetyBench 2023-9** — [[данные](https://huggingface.co/datasets/thu-coai/SafetyBench)] · смежная тема · источник: Awesome LLM Datasets
- **SHP 2021-10 — All — EN — HG** — [[данные](https://huggingface.co/datasets/stanfordnlp/SHP)] · смежная тема · источник: Awesome LLM Datasets
- **Stack-Exchange-Preferences** — [[данные](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences)] · смежная тема · источник: Awesome LLM Datasets
- **SummarizefromFeedback 2020-9** — [[данные](https://huggingface.co/datasets/openai/summarize_from_feedback)] · смежная тема · источник: Awesome LLM Datasets
- **UltraFeedback** — [[данные](https://huggingface.co/datasets/openbmb/UltraFeedback)] · смежная тема · источник: Awesome LLM Datasets
- **UltraInteract 2024-4** — [[данные](https://huggingface.co/datasets/openbmb/UltraInteract_pair)] · смежная тема · источник: Awesome LLM Datasets
- **ValueNet: A New Dataset for Human Value Driven Dialogue System, AAAI 2022** — [[данные](https://liang-qiu.github.io/ValueNet/)] · ядро · источник: Alignment Goal Survey, LLM Social Science
- **When to make exceptions: Exploring language models as accounts of human moral judgment. Jin et al. Neurips 2022.** — [[данные](https://huggingface.co/datasets/feradauto/MoralExceptQA)] · ядро · источник: Alignment Goal Survey
- **Zhihurlhf3k 2023-4** — [[данные](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k)] · смежная тема · источник: Awesome LLM Datasets

<a id="catalog-model-checkpoints-and-scorers"></a>

#### 🧠 Чекпойнты моделей и скореры · 5

- **2502.13766** — [[модель](https://huggingface.co/floschne)] · смежная тема · источник: Awesome Cultural NLP
- **Exploring Universal Human Values with Large Language Models: The AWARE-Value Model** — [[модель](https://researchsquare.com/article/rs-8188052/v1)] · ядро · источник: AIDAS Values & Pluralism
- **MT-Benchhumanjudgments 2023-6** — [[модель](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)] · смежная тема · источник: Awesome LLM Datasets
- **Robustness of large language models in moral judgements** — [[модель](https://pmc.ncbi.nlm.nih.gov/articles/PMC12015570/)] · ядро · источник: AIDAS Values & Pluralism
- **Stick to your role! Stability of personal values expressed in large language models** — [[модель](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0309114)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science

<a id="catalog-code-repositories"></a>

#### 🧰 Репозитории с кодом · 97

- **(ETHICS) EALM: Introducing Multidimensional Ethical Alignment in Conversational Information Retrieval, SIGIR-AP 2023** — [[код](https://github.com/wanng-ide/ealm)] · ядро · источник: LLM Psychometrics
- **(MFT) AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories, 2023.01, Perspectives on Psychological Science** — [[код](https://github.com/feradauto/MoralCoT)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety, LLM Psychometrics
- **(MFT) MoralBench: Moral Evaluation of LLMs** — [[код](https://github.com/agiresearch/MoralBench)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Measurement of LLM’s Philosophies of Human Nature** — [[код](https://github.com/kodenii/M-PHNS)] · ядро · источник: LLM Psychometrics
- **(Schwartz) ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models, ACL 2024** — [[код](https://github.com/Value4AI/ValueBench)] · ядро · источник: LLM Psychometrics, LLM Social Science
- **(SVO) Heterogeneous Value Alignment Evaluation for Large Language Models, AAAI 2024 Workshop** — [[код](https://github.com/zowiezhang/HVAE)] · ядро · источник: LLM Psychometrics
- **(WVS) On the Alignment of Large Language Models with Global Human Opinion, 2026.01, AAAI 2026 Best Paper (AI Alignment Track)** — [[код](https://github.com/ku-nlp/global-opinion-alignment)] · ядро · источник: LLM Psychometrics
- **2023.findings-acl.631** — [[код](https://github.com/shramay-palta/FORK_ACL2023)] · смежная тема · источник: Awesome Cultural NLP
- **2023.findings-emnlp.509** — [[код](https://github.com/SALT-NLP/CulturallyAwareNLI)] · смежная тема · источник: Awesome Cultural NLP
- **2024.findings-naacl.196** — [[код](https://github.com/zhanhl316/ReNoVi)] · смежная тема · источник: Awesome Cultural NLP
- **2209.12226** — [[код](https://github.com/google-research-datasets/nlp-fairness-for-india)] · смежная тема · источник: Awesome Cultural NLP
- **2210.08604** — [[код](https://github.com/yrf1/NormSage)] · смежная тема · источник: Awesome Cultural NLP
- **2301.01893** — [[код](https://github.com/WadeYin9712/GIVL)] · смежная тема · источник: Awesome Cultural NLP
- **2305.11840** — [[код](https://github.com/google-research-datasets/seegull)] · смежная тема · источник: Awesome Cultural NLP
- **2305.14456** — [[код](https://github.com/tareknaous/camel)] · смежная тема · источник: Awesome Cultural NLP
- **2305.16171** — [[код](https://github.com/simran-khanuja/Multilingual-Fig-QA)] · смежная тема · источник: Awesome Cultural NLP
- **2308.16705** — [[код](https://github.com/nlee0212/CREHate)] · смежная тема · источник: Awesome Cultural NLP
- **2310.17586** — [[код](https://github.com/iamshnoo/weathub)] · смежная тема · источник: Awesome Cultural NLP
- **2401.10352** — [[код](https://github.com/yongcaoplus/cuDialog)] · смежная тема · источник: Awesome Cultural NLP
- **2402.09369v1** — [[код](https://github.com/yrf1/LLM-MassiveMulticultureNormsKnowledge-NCLB)] · смежная тема · источник: Awesome Cultural NLP
- **2402.10946** — [[код](https://github.com/Scarelette/CultureLLM)] · смежная тема · источник: Awesome Cultural NLP
- **2403.14651** — [[код](https://github.com/microsoft/DOSA)] · смежная тема · источник: Awesome Cultural NLP
- **2404.01247** — [[код](https://github.com/simran-khanuja/image-transcreation)] · смежная тема · источник: Awesome Cultural NLP
- **2404.10199v1** — [[код](https://github.com/huihanlhh/Culture-Gen)] · смежная тема · источник: Awesome Cultural NLP
- **2404.12464** — [[код](https://github.com/Akhila-Yerukola/NormAd)] · смежная тема · источник: Awesome Cultural NLP
- **2404.16019** — [[код](https://github.com/HannahKirk/prism-alignment)] · смежная тема · источник: Awesome Cultural NLP
- **2406.09948** — [[код](https://github.com/nlee0212/BLEnD)] · смежная тема · источник: Awesome Cultural NLP
- **2407.03791** — [[код](https://github.com/floschne/m5b)] · смежная тема · источник: Awesome Cultural NLP
- **2407.06863** — [[код](https://github.com/google-research-datasets/cube)] · смежная тема · источник: Awesome Cultural NLP
- **2412.20760** — [[код](https://github.com/huihanlhh/CultureGenAttr)] · смежная тема · источник: Awesome Cultural NLP
- **2502.13766** — [[код](https://github.com/floschne/gimmick)] · смежная тема · источник: Awesome Cultural NLP
- **2509.17399** — [[код](https://github.com/pramitsahoo/culture-evaluation)] · смежная тема · источник: Awesome Cultural NLP
- **3539618.3591877** — [[код](https://github.com/zhanhl316/SocialDial)] · смежная тема · источник: Awesome Cultural NLP
- **<a href="** — [[код](https://github.com/sindresorhus/awesome)] · ядро · источник: AIDAS Values & Pluralism
- **\[MBTI\] Machine Mindset: An MBTI Exploration of Large Language Models** — [[код](https://github.com/PKU-YuanGroup/Machine-Mindset)] · смежная тема · источник: LLM Social Science
- **\[Norm\] Align on the Fly: Adapting Chatbot Behavior to Established Norms** — [[код](https://github.com/GAIR-NLP/OPO)] · смежная тема · источник: Awesome LLM Safety, LLM Social Science
- **A Roadmap to Pluralistic Alignment, ICML 2024** — [[код](https://github.com/jfisher52/AI_Pluralistic_Alignment)] · смежная тема · источник: LLM Social Science
- **A Survey on Evaluation of Large Language Models** — [[код](https://github.com/MLGroupJLU/LLM-eval-survey)] · смежная тема · источник: LLM Social Science
- **A Survey on Large Language Model based Autonomous Agents** — [[код](https://github.com/Paitesanshi/LLM-Agent-Survey)] · смежная тема · источник: LLM Social Science
- **AI Job Displacement Tracker** — [[код](https://github.com/noahaust2/ai-displacement-tracker)] · смежная тема · источник: LLM Social Science
- **Aligning ai with shared human values. Hendrycks et al. arXiv 2020.** — [[код](https://github.com/hendrycks/ethics)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **Aligning Large Language Models with Human: A Survey** — [[код](https://github.com/GaryYufei/AlignLLMHumanSurvey)] · смежная тема · источник: LLM Social Science
- **Alignment-Goal-Survey** — [[код](https://github.com/ValueCompass/Alignment-Goal-Survey)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **Alpacacomparisondata 2023-3** — [[код](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)] · смежная тема · источник: Awesome LLM Datasets
- **Awesome-LLM-in-Social-Science** — [[код](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science)] · ядро · источник: AIDAS Values & Pluralism
- **Awesome-LLM-Psychometrics** — [[код](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)] · ядро · источник: AIDAS Values & Pluralism
- **awesome-llm-social-simulation** — [[код](https://github.com/Wanying-He/awesome-llm-social-simulation)] · ядро · источник: AIDAS Values & Pluralism
- **Awesome-Personalized-Alignment** — [[код](https://github.com/liyongqi2002/Awesome-Personalized-Alignment)] · ядро · источник: AIDAS Values & Pluralism
- **Awesome-Pluralistic-Alignment** — [[код](https://github.com/anudeex/Awesome-Pluralistic-Alignment)] · ядро · источник: AIDAS Values & Pluralism
- **Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions, AAMAS 2026 Oral** — [[код](https://github.com/jingzhe-lin/ASVO)] · смежная тема · источник: LLM Social Science
- **Big-Math 2025-2** — [[код](https://github.com/SynthLabsAI/big-math)] · смежная тема · источник: Awesome LLM Datasets
- **code and data** — [[код](https://github.com/NeuralSentinel/CulturalKaleidoscope)] · смежная тема · источник: LLM Social Science
- **collection** — [[код](https://github.com/Indiiigo/LLM_rep_review)] · смежная тема · источник: LLM Social Science
- **Concerns on the use of generative AI in social science research** — [[код](https://github.com/uh-dcm/genai-concerns)] · смежная тема · источник: LLM Social Science
- **Constitutional ai: Harmlessness from ai feedback. Bai et al. arXiv 2022.** — [[код](https://github.com/anthropics/ConstitutionalHarmlessnessPaper)] · ядро · источник: Alignment Goal Survey
- **CrowS-Pairs** — [[код](https://github.com/nyu-mll/crows-pairs)] · смежная тема · источник: Awesome LLM Datasets
- **cultural-llm-papers** — [[код](https://github.com/faridlazuarda/cultural-llm-papers)] · ядро · источник: AIDAS Values & Pluralism, Awesome Cultural NLP
- **culture-awareness-llms** — [[код](https://github.com/siddheshih/culture-awareness-llms)] · ядро · источник: AIDAS Values & Pluralism
- **CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility. Xu et al. arXiv 2023.** — [[код](https://github.com/X-PLUG/CValues)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Datasets for depression detection using data posted on online platforms** — [[код](https://github.com/bucuram/depression-datasets-nlp)] · смежная тема · источник: LLM Social Science
- **FoodieQA: A Multimodal Dataset for Fine-Grained Understanding of Chinese Food Culture** — [[код](https://github.com/lyan62/FoodieQA)] · смежная тема · источник: Awesome Cultural NLP
- **github.com** — [[код](https://github.com/CLUEbenchmark/CLUEDatasetSearch)] · смежная тема · источник: LLM Social Science
- **HelpSteer2 2024-6** — [[код](https://github.com/NVIDIA/NeMo-Aligner)] · смежная тема · источник: Awesome LLM Datasets
- **Heterogeneous Value Evaluation for Large Language Models** — [[код](https://github.com/zowiezhang/A2EHV)] · смежная тема · источник: LLM Social Science
- **HF Datasets** — [[код](https://github.com/MinhDucBui/Multi3Hate)] · смежная тема · источник: Awesome Cultural NLP
- **High-Dimension Human Value Representation in Large Language Models** — [[код](https://github.com/HLTCHKUST/UniVaR)] · смежная тема · источник: LLM Social Science
- **How do Role Models Shape Collective Morality? Exemplar-Driven Moral Learning in Multi-Agent Simulation, ACL 2026 Main** — [[код](https://github.com/MoralAgentSim/RoleModel-Moral-Sim)] · смежная тема · источник: LLM Social Science
- **huozirlhfdata 2024-2** — [[код](https://github.com/HIT-SCIR/huozi)] · смежная тема · источник: Awesome LLM Datasets
- **huozirlhfdata 2024-2** — [[код](https://github.com/HIT-SCIR/huozi/blob/main/data/huozi-rlhf/huozi_rlhf_data.csv)] · смежная тема · источник: Awesome LLM Datasets
- **Large Language Model based Multi-Agents: A Survey of Progress and Challenges** — [[код](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers)] · смежная тема · источник: LLM Social Science
- **Leaderboard** — [[код](https://github.com/thu-coai/Safety-Prompts)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Medical-rlhf 2023-5** — [[код](https://github.com/shibing624/MedicalGPT)] · смежная тема · источник: Awesome LLM Datasets
- **Mental Health Datasets** — [[код](https://github.com/kharrigian/mental-health-datasets)] · смежная тема · источник: LLM Social Science
- **Moral stories: Situated reasoning about norms, intents, actions, and their consequences. Emelin et al. arXiv 2020.** — [[код](https://github.com/demelin/moral_stories)] · ядро · источник: Alignment Goal Survey
- **MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions. Sun et al. ACL 2023.** — [[код](https://github.com/thu-coai/MoralDial)] · ядро · источник: Alignment Goal Survey
- **MT-Benchhumanjudgments 2023-6** — [[код](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge)] · смежная тема · источник: Awesome LLM Datasets
- **PKU-SafeRLHF 2023-7** — [[код](https://github.com/PKU-Alignment/safe-rlhf)] · смежная тема · источник: Awesome LLM Datasets
- **Principle-driven self-alignment of language models from scratch with minimal human supervision. Sun et al. arXiv 2023.** — [[код](https://github.com/IBM/Dromedary)] · ядро · источник: Alignment Goal Survey
- **PRM800K 2023-5** — [[код](https://github.com/openai/prm800k)] · смежная тема · источник: Awesome LLM Datasets
- **ProgressGym: Alignment with a Millennium of Moral Progress, NeurIPS 2024 D&B Track Spotlight** — [[код](https://github.com/PKU-Alignment/ProgressGym)] · смежная тема · источник: LLM Social Science
- **rladmstn1714/CLIcK** — [[код](https://github.com/rladmstn1714/CLIcK)] · смежная тема · источник: Awesome Cultural NLP
- **SafeText: A benchmark for exploring physical safety in language models. Levy et al. arXiv 2022.** — [[код](https://github.com/sharonlevy/SafeText)] · ядро · источник: Alignment Goal Survey
- **SafetyBench 2023-9** — [[код](https://github.com/thu-coai/SafetyBench)] · смежная тема · источник: Awesome LLM Datasets
- **Scruples: A corpus of community ethical judgments on 32,000 real-life anecdotes. Lourie et al. AAAI 2021.** — [[код](https://github.com/allenai/scruples)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **SHP 2021-10 — All — EN — HG** — [[код](https://github.com/kawine/dataset_difficulty)] · смежная тема · источник: Awesome LLM Datasets
- **Simulating Human-like Daily Activities with Desire-driven Autonomy, ICLR 2025** — [[код](https://github.com/zfw1226/D2A)] · смежная тема · источник: LLM Social Science
- **SocialAgent** — [[код](https://github.com/FudanDISC/SocialAgent)] · ядро · источник: AIDAS Values & Pluralism, LLM Social Science
- **SuperCLUE-Safety 2023-9** — [[код](https://github.com/CLUEbenchmark/SuperCLUE-safety)] · смежная тема · источник: Awesome LLM Datasets
- **The moral integrity corpus: A benchmark for ethical dialogue systems. Ziems et al. arXiv 2022.** — [[код](https://github.com/SALT-NLP/mic)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **The Rise and Potential of Large Language Model Based Agents: A Survey** — [[код](https://github.com/WooooDyy/LLM-Agent-Paper-List)] · смежная тема · источник: LLM Social Science
- **Training a helpful and harmless assistant with reinforcement learning from human feedback. Bai et al. arXiv 2022.** — [[код](https://github.com/anthropics/hh-rlhf)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Training Socially Aligned Language Models in Simulated Human Society** — [[код](https://github.com/agi-templar/Stable-Alignment)] · смежная тема · источник: Awesome LLM Datasets, LLM Social Science
- **TRUSTGPT 2023-6** — [[код](https://github.com/HowieHwong/TrustGPT)] · смежная тема · источник: Awesome LLM Datasets
- **UltraFeedback** — [[код](https://github.com/OpenBMB/UltraFeedback)] · смежная тема · источник: Awesome LLM Datasets
- **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties, AAAI24** — [[код](https://github.com/tsor13/kaleido)] · смежная тема · источник: LLM Social Science
- **Why Are We Moral? An LLM-based Agent Simulation Approach to Study Moral Evolution, ACL 2026 Main (Oral)** — [[код](https://github.com/MoralAgentSim/Simulation-Engine)] · смежная тема · источник: LLM Social Science
- **⭐️ Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models, AAAI 2025** — [[код](https://github.com/Value4AI/gpv)] · смежная тема · источник: LLM Social Science

<a id="catalog-project-pages"></a>

#### 🌐 Страницы проектов · 10

- **2109.13238** — [[проект](https://marvl-challenge.github.io/)] · смежная тема · источник: Awesome Cultural NLP
- **2509.17399** — [[проект](https://nlip-lab.github.io/nlip/publications/diwali/)] · смежная тема · источник: Awesome Cultural NLP
- **AI Alignment: A Comprehensive Survey** — [[проект](https://alignmentsurvey.com/)] · смежная тема · источник: LLM Social Science
- **Can machines learn morality? the delphi experiment. Jiang et al. arXiv 2021.** — [[проект](https://delphi.allenai.org/)] · ядро · источник: Alignment Goal Survey
- **Concerns on the use of generative AI in social science research** — [[проект](https://uh-dcm.github.io/genai-concerns/)] · смежная тема · источник: LLM Social Science
- **NLPositionality: Characterizing Design Biases of Datasets and Models** — [[проект](https://nlpositionality.cs.washington.edu/)] · смежная тема · источник: Awesome Cultural NLP
- **Political-LLM: Large Language Models in Political Science** — [[проект](https://political-llm.org/)] · смежная тема · источник: LLM Social Science
- **SafetyBench 2023-9** — [[проект](https://llmbench.ai/safety)] · смежная тема · источник: Awesome LLM Datasets
- **SuperCLUE-Safety 2023-9** — [[проект](https://cluebenchmarks.com/superclue_safety.html)] · смежная тема · источник: Awesome LLM Datasets
- **Towards Measuring the Representation of Subjective Global Opinions in Language Models** — [[проект](https://llmglobalvalues.anthropic.com/)] · смежная тема · источник: LLM Social Science

<a id="catalog-survey-resources"></a>

#### 📋 Опросные ресурсы · 4

- **EVS — European Values Survey** — [[опрос](https://europeanvaluesstudy.eu/)] · ядро · источник: AIDAS Values & Pluralism, Alignment Goal Survey
- **GSS — General Social Survey** — [[опрос](https://gss.norc.org/)] · ядро · источник: AIDAS Values & Pluralism
- **World Values Survey Wave 7 (2017-2022).** — [[опрос](https://worldvaluessurvey.org/WVSDocumentationWV7.jsp)] · ядро · источник: Alignment Goal Survey
- **WVS — World Values Survey** — [[опрос](https://worldvaluessurvey.org/)] · ядро · источник: AIDAS Values & Pluralism

<a id="catalog-additional-resources"></a>

#### 🔗 Дополнительные ресурсы · 88

- **!\[Awesome** — [[ссылка](https://awesome.re)] · ядро · источник: Pluralistic Alignment
- **(ANES) Out of One, Many: Using Language Models to Simulate Human Samples, 2023.02, Political Analysis** — [[ссылка](https://cambridge.org/core/journals/political-analysis/article/abs/out-of-one-many-using-language-models-to-simulate-human-samples/035D7C8A55B237942FB6DBAD7CAA4E49)] · ядро · источник: LLM Psychometrics
- **(ANES) Synthetic Replacements for Human Survey Data? The Perils of Large Language Models, 2024.05, Political Analysis** — [[ссылка](https://cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE)] · ядро · источник: LLM Psychometrics
- **(ATP) Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design, 2024.09, Transactions of the Association for Computational Linguistics (TACL)** — [[ссылка](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00685/124261)] · ядро · источник: LLM Psychometrics
- **(ATP) Whose Opinions Do Language Models Reflect?, ICML 2023** — [[ссылка](https://proceedings.mlr.press/v202/santurkar23a.html)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Beyond Prompt Brittleness: Evaluating the Reliability and Consistency of Political Worldviews in LLMs, 2024.11, Transactions of the Association for Computational Linguistics (TACL)** — [[ссылка](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00710/125176)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias, 2024.08, PLOS Climate** — [[ссылка](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000429)] · ядро · источник: LLM Psychometrics
- **(Others & custom) DO MINDFULNESS ACTIVITIES IMPROVE HANDGRIP STRENGTH AMONG OLDER ADULTS: A PROPENSITY SCORE MATCHING APPROACH, 2024.12, Innovation in Aging** — [[ссылка](https://academic.oup.com/innovateage/article/8/Supplement_1/1010/7939280)] · ядро · источник: LLM Psychometrics
- **(Others & custom) Improving GPT Generated Synthetic Samples with Sampling-Permutation Algorithm** — [[ссылка](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4548937)] · ядро · источник: LLM Psychometrics
- **(Others & Custom) The moral machine experiment on large language models, 2024.02, Royal Society Open Science** — [[ссылка](https://royalsocietypublishing.org/doi/full/10.1098/rsos.231393)] · ядро · источник: LLM Psychometrics
- **(PCT) The Political Biases of ChatGPT, 2023.01, Social Sciences** — [[ссылка](https://mdpi.com/2076-0760/12/3/148)] · ядро · источник: LLM Psychometrics
- **(Schwartz) Assessing the Alignment of Large Language Models With Human Values for Mental Health Integration: Cross-Sectional Study Using Schwartz’s Theory of Basic Values, 2024.01, JMIR Mental Health** — [[ссылка](https://mental.jmir.org/2024/1/e55988)] · ядро · источник: LLM Psychometrics
- **(VSM) Large Language Models as Superpositions of Cultural Perspectives** — [[ссылка](https://gitlab.inria.fr/gkovac/value_stability)] · ядро · источник: LLM Psychometrics
- **2301.02560** — [[ссылка](https://geodiverse-data-collection.cs.princeton.edu/)] · смежная тема · источник: Awesome Cultural NLP
- **2410.12705** — [[ссылка](https://worldcuisines.github.io/)] · смежная тема · источник: Awesome Cultural NLP
- **<a href="** — [[ссылка](https://git.io/typing-svg)] · ядро · источник: AIDAS Values & Pluralism
- **<img src="** — [[ссылка](https://capsule-render.vercel.app/api)] · ядро · источник: AIDAS Values & Pluralism
- **<img src="** — [[ссылка](https://readme-typing-svg.demolab.com)] · ядро · источник: AIDAS Values & Pluralism
- **A 30-year struggle; the sustained efforts to give force of law to the Universal Declaration of Human Rights** — [[ссылка](https://unesdoc.unesco.org/ark:/48223/pf0000048063)] · ядро · источник: AIDAS Values & Pluralism
- **A review of automatic item generation techniques leveraging large language models** — [[ссылка](https://dergipark.org.tr/en/pub/ijate/issue/90456/1602294)] · ядро · источник: LLM Psychometrics
- **A theory of justice.** — [[ссылка](https://jstor.org/stable/j.ctvjf9z6v)] · ядро · источник: AIDAS Values & Pluralism
- **A Value-Belief-Norm Theory of Support for Social Movements: The Case of Environmentalism** — [[ссылка](http://jstor.org/stable/24707060)] · ядро · источник: STONIC bibliography
- **Aggregating Sets of Judgments: An Impossibility Result** — [[ссылка](https://cambridge.org/core/journals/economics-and-philosophy/article/abs/aggregating-sets-of-judgments-an-impossibility-result/35BB2A979DC8D2548B3040A1757B058B)] · ядро · источник: AIDAS Values & Pluralism
- **An Overview of the Schwartz Theory of Basic Values** — [[ссылка](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/)] · ядро · источник: AIDAS Values & Pluralism
- **An overview of the Schwartz theory of basic values. Schwartz et al. Online readings in Psychology and Culture 2012.** — [[ссылка](https://scholarworks.gvsu.edu/cgi/viewcontent.cgi)] · ядро · источник: Alignment Goal Survey
- **Basic human values: Theory, measurement, and applications** — [[ссылка](https://researchgate.net/publication/286951722_Basic_human_values_Theory_measurement_and_applications)] · ядро · источник: AIDAS Values & Pluralism
- **Can Generative AI improve social science?, 2024.05, PNAS** — [[ссылка](https://pnas.org/doi/pdf/10.1073/pnas.2314021121)] · смежная тема · источник: LLM Social Science
- **Challenging the Validity of Personality Tests for Large Language Models, Workshop at NeurIPS 2023** — [[ссылка](https://tomsuehr.com/wp-content/uploads/2024/06/challenging_the_validity_of_personality_tests_on_llms.pdf)] · ядро · источник: LLM Psychometrics
- **Citizenship and Social Class** — [[ссылка](https://books.google.co.kr/books?id=99v4JQAACAAJ)] · ядро · источник: AIDAS Values & Pluralism
- **Collective Choice and Social Welfare** — [[ссылка](https://jstor.org/stable/j.ctv2sp3dqx)] · ядро · источник: AIDAS Values & Pluralism
- **Conflicts of Values (in Moral Luck)** — [[ссылка](https://cambridge.org/core/books/abs/moral-luck/conflicts-of-values/652C425160A2BC6BA74E049D220E4245)] · ядро · источник: AIDAS Values & Pluralism
- **Creating Capabilities: The Human Development Approach and Its Implementation** — [[ссылка](https://cambridge.org/core/journals/hypatia/article/abs/creating-capabilities-the-human-development-approach-and-its-implementation/6774FAF6E6CEC38018F9733B188A1A6C)] · ядро · источник: AIDAS Values & Pluralism
- **Cultural Value Orientations** — [[ссылка](https://researchgate.net/publication/265997557)] · ядро · источник: AIDAS Values & Pluralism
- **Culture's consequences: International differences in work-related values** — [[ссылка](https://philpapers.org/rec/HOFCCI-2)] · ядро · источник: AIDAS Values & Pluralism
- **Culture's consequences: International differences in work-related values. Hofstede et al. 1984.** — [[ссылка](https://books.google.com/books/about/Culture_s_Consequences.html?id=Cayp_Um4O9gC)] · ядро · источник: Alignment Goal Survey
- **Cultures and organizations: software of the mind** — [[ссылка](https://books.google.co.kr/books?id=o4OqTgV3V00C)] · ядро · источник: AIDAS Values & Pluralism
- **Do LLMs have Consistent Values?** — [[ссылка](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf)] · ядро · источник: STONIC bibliography
- **ESS — European Social Survey** — [[ссылка](https://europeansocialsurvey.org/data-portal)] · ядро · источник: AIDAS Values & Pluralism
- **Functional theory of human values** — [[ссылка](https://researchgate.net/publication/259486885)] · ядро · источник: AIDAS Values & Pluralism
- **Handbook of Computational Social Choice** — [[ссылка](https://cambridge.org/core/books/handbook-of-computational-social-choice/8AF63E87F76A5FC974D5E73536C52BD6)] · ядро · источник: AIDAS Values & Pluralism
- **If they disagree, will you conform? Exploring the role of robots’ value awareness in a decision-making task** — [[ссылка](https://jbe-platform.com/content/journals/10.1075/is.25030.pus)] · ядро · источник: AIDAS Values & Pluralism
- **Improving alignment of dialogue agents via targeted human judgements. Glaese et al. arXiv 2022.** — [[ссылка](https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/sparrow.html)] · ядро · источник: Alignment Goal Survey
- **Kush R. Varshney. XRDS 2019.** — [[ссылка](https://krvarshney.github.io/)] · смежная тема · источник: Awesome LLM Safety
- **Kush R. Varshney. XRDS 2019.** — [[ссылка](https://krvarshney.github.io/pubs/Varshney_xrds2019.pdf)] · смежная тема · источник: Awesome LLM Safety
- **Leaderboard** — [[ссылка](http://115.182.62.166:18000/)] · ядро · источник: Alignment Goal Survey, Awesome LLM Datasets
- **Liberal Pluralism: The Implications of Value Pluralism for Political Theory and Practice** — [[ссылка](https://cambridge.org/core/books/liberal-pluralism/B7B1CC377F1E093457A525CDC14EA008)] · ядро · источник: AIDAS Values & Pluralism
- **Liberals and conservatives rely on different sets of moral foundations** — [[ссылка](https://pubmed.ncbi.nlm.nih.gov/19379034/)] · ядро · источник: AIDAS Values & Pluralism
- **Life values inventory: Facilitator's guide. Brown et al. Willianmsburg, VA 2002.** — [[ссылка](https://lifevaluesinventory.org/LifeValuesInventory.org%20-%20Facilitators%20Guide%20Sample.pdf)] · ядро · источник: Alignment Goal Survey
- **lit.eecs.umich.edu** — [[ссылка](https://lit.eecs.umich.edu/downloads.html)] · смежная тема · источник: LLM Social Science
- **Manipulation of Voting Schemes: A General Result** — [[ссылка](https://jstor.org/stable/1914083)] · ядро · источник: AIDAS Values & Pluralism
- **Mapping and interpreting cultural differences around the world** — [[ссылка](https://researchgate.net/publication/265596552)] · ядро · источник: AIDAS Values & Pluralism
- **Measuring Perceived Slant in Large Language Models Through User Evaluations** — [[ссылка](https://modelslant.com/paper.pdf)] · ядро · источник: Pluralistic Alignment
- **Measuring the Refined Theory of Individual Values in 49 Cultural Groups** — [[ссылка](https://researchgate.net/publication/349058866)] · ядро · источник: AIDAS Values & Pluralism
- **Mental representations of social values.** — [[ссылка](https://psycnet.apa.org/record/2012-14612-001)] · ядро · источник: AIDAS Values & Pluralism
- **Modernization and Postmodernization: Cultural, Economic, and Political Change in 43 Societies** — [[ссылка](https://jstor.org/stable/j.ctv10vm2ns)] · ядро · источник: AIDAS Values & Pluralism
- **Modernization, Cultural Change, and Democracy** — [[ссылка](https://researchgate.net/publication/230557603)] · ядро · источник: AIDAS Values & Pluralism
- **Moral Foundations Theory: The Pragmatic Validity of Moral Pluralism** — [[ссылка](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2184440)] · ядро · источник: AIDAS Values & Pluralism
- **NeurIPS 2025 Tutorial: Human-AI Alignment** — [[ссылка](https://hai-alignment-course.github.io/tutorial/)] · ядро · источник: AIDAS Values & Pluralism
- **On the Rationale of Group Decision-making** — [[ссылка](https://jstor.org/stable/1825026)] · ядро · источник: AIDAS Values & Pluralism
- **Perils and opportunities in using large language models in psychological research** — [[ссылка](https://academic.oup.com/pnasnexus/article/3/7/pgae245/7712371)] · смежная тема · источник: LLM Social Science
- **Personality testing of large language models: limited temporal stability, but highlighted prosociality, 2024.01, Royal Society Open Science** — [[ссылка](https://royalsocietypublishing.org/doi/full/10.1098/rsos.240180)] · ядро · источник: LLM Psychometrics
- **Pew Researcj Center's Global Attitudes Surveys (GAS)** — [[ссылка](https://pewresearch.org/)] · ядро · источник: Alignment Goal Survey
- **Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449** — [[ссылка](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449)] · ядро · источник: STONIC bibliography
- **Refining the theory of basic individual values** — [[ссылка](https://pubmed.ncbi.nlm.nih.gov/22823292/)] · ядро · источник: AIDAS Values & Pluralism
- **Rokeach value survey. Rokeach et al. The nature of human values. 1967.** — [[ссылка](https://en.wikipedia.org/wiki/Rokeach_Value_Survey)] · ядро · источник: Alignment Goal Survey
- **Social bias frames: Reasoning about social and power implications of language. Sap et al. arXiv 2019.** — [[ссылка](https://maartensap.com/social-bias-frames/)] · ядро · источник: Alignment Goal Survey
- **Social chemistry 101: Learning to reason about social and moral norms. Forbes et al. arXiv 2020.** — [[ссылка](https://maxwellforbes.com/social-chemistry/)] · ядро · источник: Alignment Goal Survey, Awesome LLM Safety
- **Social Choice and Individual Values** — [[ссылка](https://jstor.org/stable/j.ctt1nqb90)] · ядро · источник: AIDAS Values & Pluralism
- **Social Choice Theory (in Stanford Encyclopedia of Philosophy)** — [[ссылка](https://plato.stanford.edu/entries/social-choice/)] · ядро · источник: AIDAS Values & Pluralism
- **Stanford 2025: Human-Centered LLMs (CS329X)** — [[ссылка](https://web.stanford.edu/class/cs329x/)] · ядро · источник: AIDAS Values & Pluralism
- **Stanford 2025: Machine Learning from Human Preferences (CS329H)** — [[ссылка](https://web.stanford.edu/class/cs329h/)] · ядро · источник: AIDAS Values & Pluralism
- **Steerable Alignment with Conditional Multiobjective Preference Optimization** — [[ссылка](https://dspace.mit.edu/handle/1721.1/156747)] · ядро · источник: Pluralistic Alignment
- **Survey of Cultural Awareness in Language Models: Text and Beyond Open Access** — [[ссылка](https://direct.mit.edu/coli/article/51/3/907/130804/Survey-of-Cultural-Awareness-in-Language-Models)] · ядро · источник: Pluralistic Alignment
- **The Impossibility of a Paretian Liberal** — [[ссылка](https://jstor.org/stable/1829633)] · ядро · источник: AIDAS Values & Pluralism
- **The Morality of Freedom** — [[ссылка](https://academic.oup.com/book/9926)] · ядро · источник: AIDAS Values & Pluralism
- **The Morality of Pluralism** — [[ссылка](https://jstor.org/stable/j.ctt7smh7)] · ядро · источник: AIDAS Values & Pluralism
- **The Morals of Modernity** — [[ссылка](https://cambridge.org/core/books/morals-of-modernity/2D52EFBB271F119438B8B4DA753079D3)] · ядро · источник: AIDAS Values & Pluralism
- **The nature of human values.** — [[ссылка](https://psycnet.apa.org/record/2011-15663-000)] · ядро · источник: AIDAS Values & Pluralism
- **The Right and the Good** — [[ссылка](https://academic.oup.com/book/27608)] · ядро · источник: AIDAS Values & Pluralism
- **The Righteous Mind** — [[ссылка](https://righteousmind.com/)] · ядро · источник: AIDAS Values & Pluralism
- **The Theory of Communicative Action** — [[ссылка](https://philpapers.org/rec/HABTTO)] · ядро · источник: AIDAS Values & Pluralism
- **The theory of dyadic morality: Reinventing moral judgment by redefining harm.** — [[ссылка](https://psycnet.apa.org/record/2018-02142-002)] · ядро · источник: AIDAS Values & Pluralism
- **Towards Answering Open-ended Ethical Quandary Questions. Bang et al. arXiv 2022.** — [[ссылка](https://amulyayadav.github.io/AI4SG2023/images/22.pdf)] · ядро · источник: Alignment Goal Survey
- **Towards Pluralistic Alignment of LLMs: A Comprehensive Survey** — [[ссылка](https://preprints.org/manuscript/202603.1876)] · ядро · источник: AIDAS Values & Pluralism
- **Towards Pluralistic Value Alignment: Aggregating Value Systems through ℓp-Regression, AAMAS 2022 workshop** — [[ссылка](https://openaccess.city.ac.uk/id/eprint/31381/)] · смежная тема · источник: LLM Social Science
- **Two Concepts of Liberty** — [[ссылка](https://academic.oup.com/book/7968/chapter-abstract/153281672)] · ядро · источник: AIDAS Values & Pluralism
- **Universals in the content and structure of values: Theoretical advances and empirical tests in 20 countries.** — [[ссылка](https://psycnet.apa.org/record/2003-00370-001)] · ядро · источник: AIDAS Values & Pluralism
- **Value Pluralism (in Stanford Encyclopedia of Philosophy)** — [[ссылка](https://plato.stanford.edu/entries/value-pluralism/)] · ядро · источник: AIDAS Values & Pluralism

<!-- complete-catalog:end -->

## Данные и участие

README служит входной точкой для человека, а структурированные файлы позволяют
воспроизводимо искать, дедуплицировать и курировать материалы.

```text
работа ──< исследование >── аксиология
                 ├──────── инструмент
                 ├──────── датасет
                 ├──────── модель + роль
                 └──────── свидетельства валидности
```

| Слой данных | Содержание |
|---|---|
| [`data/raw/catalog_links.jsonl`](data/raw/catalog_links.jsonl) | дедуплицированная очередь обнаруженных ресурсов с происхождением |
| [`data/curated/works.jsonl`](data/curated/works.jsonl) | публикации, проверенные по первичному источнику |
| [`data/curated/studies.jsonl`](data/curated/studies.jsonl) | интерфейсы, ценностные пространства, скореры и валидация экспериментов |
| [`data/curated/axiologies.json`](data/curated/axiologies.json) | именованные, индуцированные, латентные и открытые ценностные пространства |
| [`data/catalog_sources.json`](data/catalog_sources.json) | каталоги-источники и правила включения |

### Как участвовать

Можно добавить отсутствующую работу, исправить ссылку, дополнить запись или
описать измерительный контракт исследования. Методические утверждения должны
ссылаться на первичную статью; awesome-lists используются только как источники
обнаружения. См. [руководство для участников](CONTRIBUTING.md).

### Пересборка

```bash
python3 scripts/sync_sources.py
python3 scripts/harvest_catalogs.py
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_catalog.py
```

### Лицензия

Код распространяется по MIT. Оригинальные структурированные метаданные и
документация — по CC BY 4.0. Права и лицензии на связанные статьи, датасеты,
модели и сторонние репозитории сохраняются за их правообладателями.
