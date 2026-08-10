const grammar = {
  axiology: {
    type: "Representation",
    title: "Axiology",
    body: "Defines which values exist and how they relate: named dimensions, a hierarchy, a circumplex, an ontology, or a learned space.",
    example: "Example: Schwartz defines motivational value types and their compatibility/opposition. It does not prescribe one prompt or one scorer.",
  },
  instrument: {
    type: "Operationalization",
    title: "Instrument",
    body: "Turns a construct into reusable items or tasks, such as PVQ portraits, a scenario bank, a ranking task, or a behavioral game.",
    example: "Example: PVQ-40 operationalizes ten Schwartz values with 40 short portraits. The theory is broader than those 40 items.",
  },
  interface: {
    type: "Elicitation",
    title: "Interface",
    body: "Specifies what the subject actually does: rates, chooses, ranks, generates text, or acts in an environment. Interface changes can change the evidence object.",
    example: "Example: endorsing two options independently is not the same observation as choosing between them in direct conflict.",
  },
  scorer: {
    type: "Mapping",
    title: "Scorer",
    body: "Maps raw responses into labels, dimensions, probabilities, or embeddings. It may be a key, a classifier, an LLM judge, or a representation model.",
    example: "Example: ValueLlama can estimate whether supplied values are present in text; it does not make the underlying generation a questionnaire response.",
  },
  claim: {
    type: "Interpretation",
    title: "Reportable claim",
    body: "States the narrow conclusion licensed by the full chain. Reliability, cross-interface transfer, and external validity are additional empirical questions.",
    example: "Example: a free-text scorer supports a textual-framing claim under that scorer—not automatically a stable, general value identity.",
  },
};

const shapes = {
  circumplex: {
    kind: "Relational geometry",
    title: "Circumplex",
    body: "Values form a circle. Neighbors share motivational content; opposing locations indicate tension. A profile should be interpreted with that relational structure intact.",
    example: "Schwartz-10 / Schwartz-19",
    useful: "Compatibility and conflict",
    risk: "Treating dimensions as unrelated scores",
  },
  axes: {
    kind: "Coordinate system",
    title: "Bipolar axes",
    body: "Cases occupy positions between named poles. One coordinate can summarize several correlated attitudes, often at an aggregate cultural level.",
    example: "Inglehart–Welzel; Hofstede dimensions",
    useful: "Position and directional contrast",
    risk: "Moving population-level axes to individuals",
  },
  hierarchy: {
    kind: "Ordered structure",
    title: "Hierarchy",
    body: "Values may be grouped into levels or placed in a priority order. Rank tells us what comes before what, but not how far apart the priorities are.",
    example: "Rokeach; Functional Theory",
    useful: "Priority and nested organization",
    risk: "Reading rank differences as metric distances",
  },
  ontology: {
    kind: "Relational vocabulary",
    title: "Ontology",
    body: "Nodes and typed relations describe contextual values, rights, duties, or principles. The result is a graph of relevant concepts rather than one profile vector.",
    example: "Value Kaleidoscope",
    useful: "Context and plural relations",
    risk: "Flattening a graph into an arbitrary score",
  },
  factors: {
    kind: "Data-induced structure",
    title: "Induced factors",
    body: "Many observed value terms are reduced to a smaller set of interpretable factors. The structure is learned from a particular corpus and subject panel.",
    example: "GPLA: 123 atomic values → 5 factors",
    useful: "Discovering recurring AI-native structure",
    risk: "Assuming factors are universal across corpora",
  },
  latent: {
    kind: "Learned representation",
    title: "Latent space",
    body: "A model encodes value-relevant responses as dense vectors. Distance and direction can be useful even when individual coordinates have no stable names.",
    example: "UniVaR",
    useful: "Similarity across models and languages",
    risk: "Inventing meanings for unnamed dimensions",
  },
  open: {
    kind: "Dynamic vocabulary",
    title: "Open value set",
    body: "Values are supplied or generated at measurement time rather than fixed in advance. Coverage is flexible, but comparability depends on the definitions and scorer.",
    example: "GPV / generative psychometrics",
    useful: "Context-specific value questions",
    risk: "Comparing scores built from different definitions",
  },
};

const shapeSvgs = {
  circumplex: `<svg viewBox="0 0 440 340"><circle cx="220" cy="170" r="120" fill="#eef4ef" stroke="#b8c8bf"/><circle cx="220" cy="50" r="27" fill="#c7eadc"/><circle cx="334" cy="133" r="27" fill="#e9b44c"/><circle cx="290" cy="267" r="27" fill="#d88a75"/><circle cx="150" cy="267" r="27" fill="#806ca8"/><circle cx="106" cy="133" r="27" fill="#6f91b8"/><path d="M220 80L318 142M303 247L220 80M137 247L303 247M122 142L137 247M220 80L122 142" fill="none" stroke="#17201d" stroke-opacity=".25"/><text x="220" y="174" text-anchor="middle" font-family="Georgia" font-size="19">compatibility</text><text x="220" y="198" text-anchor="middle" fill="#64716c" font-size="11">opposition across the circle</text></svg>`,
  axes: `<svg viewBox="0 0 440 340"><rect x="66" y="36" width="308" height="268" fill="#f5f8f4" stroke="#ccd7d0"/><path d="M220 36V304M66 170H374" stroke="#17201d"/><circle cx="286" cy="104" r="14" fill="#d66d58" stroke="white" stroke-width="5"/><text x="220" y="25" text-anchor="middle" fill="#64716c" font-size="11">pole B</text><text x="220" y="325" text-anchor="middle" fill="#64716c" font-size="11">pole A</text><text x="38" y="174" text-anchor="middle" fill="#64716c" font-size="11">pole C</text><text x="402" y="174" text-anchor="middle" fill="#64716c" font-size="11">pole D</text></svg>`,
  hierarchy: `<svg viewBox="0 0 440 340"><path d="M220 65V120M118 165V210M220 165V210M322 165V210M118 165H322M118 120H322M118 120V165M220 120V165M322 120V165" fill="none" stroke="#9caaa2" stroke-width="2"/><rect x="155" y="28" width="130" height="45" rx="22" fill="#12634f"/><rect x="65" y="120" width="106" height="45" rx="22" fill="#c7eadc"/><rect x="167" y="120" width="106" height="45" rx="22" fill="#e9b44c"/><rect x="269" y="120" width="106" height="45" rx="22" fill="#d88a75"/><rect x="70" y="210" width="96" height="38" rx="19" fill="#eef2ef" stroke="#ccd7d0"/><rect x="172" y="210" width="96" height="38" rx="19" fill="#eef2ef" stroke="#ccd7d0"/><rect x="274" y="210" width="96" height="38" rx="19" fill="#eef2ef" stroke="#ccd7d0"/><text x="220" y="56" text-anchor="middle" fill="white" font-size="12">higher order</text><text x="118" y="148" text-anchor="middle" font-size="11">group A</text><text x="220" y="148" text-anchor="middle" font-size="11">group B</text><text x="322" y="148" text-anchor="middle" font-size="11">group C</text></svg>`,
  ontology: `<svg viewBox="0 0 440 340"><g stroke="#acbbb3" stroke-width="2"><path d="M220 170L105 85M220 170L335 85M220 170L110 263M220 170L335 258M105 85L335 85M110 263L335 258"/></g><circle cx="220" cy="170" r="54" fill="#12634f"/><circle cx="105" cy="85" r="38" fill="#c7eadc"/><circle cx="335" cy="85" r="38" fill="#e9b44c"/><circle cx="110" cy="263" r="38" fill="#d88a75"/><circle cx="335" cy="258" r="38" fill="#806ca8"/><g text-anchor="middle" font-size="11"><text x="220" y="174" fill="white">situation</text><text x="105" y="89">value</text><text x="335" y="89">right</text><text x="110" y="267">duty</text><text x="335" y="262" fill="white">stakeholder</text></g></svg>`,
  factors: `<svg viewBox="0 0 440 340"><g fill="#d9e8e0"><rect x="65" y="48" width="116" height="18"/><rect x="65" y="83" width="238" height="18"/><rect x="65" y="118" width="178" height="18"/><rect x="65" y="153" width="295" height="18"/><rect x="65" y="188" width="146" height="18"/><rect x="65" y="223" width="267" height="18"/></g><path d="M330 50C390 98 390 198 330 240" fill="none" stroke="#12634f" stroke-width="3"/><circle cx="338" cy="64" r="18" fill="#c7eadc"/><circle cx="370" cy="118" r="18" fill="#e9b44c"/><circle cx="370" cy="183" r="18" fill="#d88a75"/><circle cx="338" cy="235" r="18" fill="#806ca8"/><text x="65" y="278" fill="#64716c" font-size="12">many observed terms → fewer factors</text></svg>`,
  latent: `<svg viewBox="0 0 440 340"><rect x="52" y="36" width="336" height="268" fill="#f2f6f2" stroke="#ccd7d0"/><g fill="#12634f"><circle cx="118" cy="100" r="9"/><circle cx="146" cy="119" r="9"/><circle cx="131" cy="143" r="9"/><circle cx="171" cy="92" r="9"/></g><g fill="#d66d58"><circle cx="284" cy="96" r="9"/><circle cx="314" cy="123" r="9"/><circle cx="276" cy="135" r="9"/><circle cx="337" cy="91" r="9"/></g><g fill="#806ca8"><circle cx="209" cy="234" r="9"/><circle cx="238" cy="259" r="9"/><circle cx="184" cy="265" r="9"/><circle cx="250" cy="220" r="9"/></g><text x="220" y="325" text-anchor="middle" fill="#64716c" font-size="11">unnamed projection for illustration</text></svg>`,
  open: `<svg viewBox="0 0 440 340"><rect x="68" y="72" width="304" height="68" rx="5" fill="white" stroke="#ccd7d0"/><text x="90" y="101" fill="#64716c" font-size="11">Value to test in this context…</text><rect x="284" y="86" width="68" height="38" rx="19" fill="#12634f"/><text x="318" y="109" text-anchor="middle" fill="white" font-size="11">Add</text><g font-size="11"><rect x="82" y="175" width="84" height="34" rx="17" fill="#c7eadc"/><text x="124" y="196" text-anchor="middle">prudence</text><rect x="176" y="175" width="98" height="34" rx="17" fill="#e9b44c"/><text x="225" y="196" text-anchor="middle">reciprocity</text><rect x="284" y="175" width="78" height="34" rx="17" fill="#d88a75"/><text x="323" y="196" text-anchor="middle">dignity</text><rect x="130" y="223" width="86" height="34" rx="17" fill="#806ca8"/><text x="173" y="244" text-anchor="middle" fill="white">care</text><rect x="226" y="223" width="108" height="34" rx="17" fill="#6f91b8"/><text x="280" y="244" text-anchor="middle" fill="white">transparency</text></g></svg>`,
};

const schwartzValues = [
  { name: "Self-Direction", angle: -90, color: "#79baa0", group: "Openness to Change", motive: "Independent thought and action; creating and exploring.", neighbor: "Stimulation", opposite: "Conformity / Tradition" },
  { name: "Stimulation", angle: -54, color: "#9ac67b", group: "Openness to Change", motive: "Excitement, novelty, and challenge.", neighbor: "Self-Direction / Hedonism", opposite: "Security" },
  { name: "Hedonism", angle: -18, color: "#e7c95f", group: "Openness + Self-Enhancement", motive: "Pleasure and sensuous gratification.", neighbor: "Stimulation / Achievement", opposite: "Tradition" },
  { name: "Achievement", angle: 18, color: "#e9a95c", group: "Self-Enhancement", motive: "Personal success through demonstrated competence.", neighbor: "Hedonism / Power", opposite: "Benevolence" },
  { name: "Power", angle: 54, color: "#db7565", group: "Self-Enhancement", motive: "Status, control over resources, and dominance.", neighbor: "Achievement / Security", opposite: "Universalism" },
  { name: "Security", angle: 90, color: "#bd7694", group: "Conservation", motive: "Safety, harmony, and stability of self and society.", neighbor: "Power / Conformity", opposite: "Stimulation" },
  { name: "Conformity", angle: 126, color: "#9277ae", group: "Conservation", motive: "Restraint of actions likely to upset others or violate norms.", neighbor: "Security / Tradition", opposite: "Self-Direction" },
  { name: "Tradition", angle: 162, color: "#707db2", group: "Conservation", motive: "Respect and commitment to cultural or religious customs.", neighbor: "Conformity / Benevolence", opposite: "Hedonism" },
  { name: "Benevolence", angle: 198, color: "#5d91b0", group: "Self-Transcendence", motive: "Welfare of people with whom one is in frequent contact.", neighbor: "Tradition / Universalism", opposite: "Achievement" },
  { name: "Universalism", angle: 234, color: "#5aa4a0", group: "Self-Transcendence", motive: "Understanding, tolerance, and protection of people and nature.", neighbor: "Benevolence / Self-Direction", opposite: "Power" },
];

const higherOrder = [
  { name: "Openness to Change", color: "#8fc38e", values: "Self-Direction, Stimulation, and part of Hedonism", motive: "Readiness for new experience and independent action.", opposite: "Conservation" },
  { name: "Self-Enhancement", color: "#e3a45d", values: "Achievement, Power, and part of Hedonism", motive: "Pursuit of personal success and dominance.", opposite: "Self-Transcendence" },
  { name: "Conservation", color: "#9a78a7", values: "Security, Conformity, Tradition", motive: "Order, self-restriction, stability, and resistance to change.", opposite: "Openness to Change" },
  { name: "Self-Transcendence", color: "#629da8", values: "Benevolence and Universalism", motive: "Concern for the welfare and interests of others.", opposite: "Self-Enhancement" },
];

const interfaces = {
  questionnaire: { evidence: "Responses to a separate standardized item bank", example: "The anchor estimates endorsement under a questionnaire protocol, often with its own wording and response scale.", claim: "Questionnaire-conditioned stated profile", caution: "It is an external anchor here; it does not prove how the same subject chooses or writes in the shared situation." },
  endorsement: { evidence: "Independent ratings of each response option", example: "“Ship now” and “delay for review” are each rated without forcing one to defeat the other.", claim: "Independent endorsement under the prompt", caution: "Two options can both be endorsed. Near-ties and scale-use behavior matter." },
  choice: { evidence: "A forced choice between conflicting alternatives", example: "The subject must select one option; counterbalancing reveals order and position sensitivity.", claim: "Choice priority under this conflict task", caution: "A selected option is not automatically a stable preference outside this choice set." },
  generation: { evidence: "Open-ended explanation or recommendation", example: "A scorer maps the generated framing to supplied values, named dimensions, or an embedding.", claim: "Textual framing under the scorer", caution: "Coverage, sentence splitting, scorer identity, and zero-evidence policy can change the profile." },
  action: { evidence: "A consequential action in an environment", example: "The system schedules a launch, allocates a budget, or invokes a tool under explicit constraints.", claim: "Task-bounded behavioral evidence", caution: "Ecological validity improves only to the extent that the environment represents the deployment context." },
};

function escapeHtml(value = "") {
  return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

function renderGrammar(key) {
  const item = grammar[key];
  document.querySelector("#grammarDetail").innerHTML = `<p class="detail-type">${item.type}</p><h3>${item.title}</h3><p>${item.body}</p><div class="example">${item.example}</div>`;
}

function renderShape(key) {
  const item = shapes[key];
  document.querySelector("#shapeVisual").innerHTML = shapeSvgs[key];
  document.querySelector("#shapeCopy").innerHTML = `<p class="shape-kind">${item.kind}</p><h3>${item.title}</h3><p>${item.body}</p><dl><dt>Example</dt><dd>${item.example}</dd><dt>Best for</dt><dd>${item.useful}</dd><dt>Watch for</dt><dd>${item.risk}</dd></dl>`;
}

function polar(angle, radius) {
  const radians = angle * Math.PI / 180;
  return { x: 260 + Math.cos(radians) * radius, y: 260 + Math.sin(radians) * radius };
}

function renderSchwartz(mode = "10", selected = 0) {
  const svg = document.querySelector("#schwartzCompass");
  const axis = `<circle class="ring" cx="260" cy="260" r="195"/><circle cx="260" cy="260" r="112" fill="white" stroke="#d6dfd8"/><path class="axis" d="M260 54V466M54 260H466"/><text class="center-label" x="260" y="255">motivational</text><text class="center-label" x="260" y="276">continuum</text>`;
  if (mode === "10") {
    svg.innerHTML = axis + schwartzValues.map((item, index) => {
      const point = polar(item.angle, 180);
      const words = item.name.split(" ");
      const labels = words.map((word, wordIndex) => `<text x="${point.x}" y="${point.y + 4 + (wordIndex - (words.length - 1) / 2) * 13}">${word}</text>`).join("");
      return `<g class="value-node${index === selected ? " active" : ""}" data-index="${index}"><circle cx="${point.x}" cy="${point.y}" r="34" fill="${item.color}"/>${labels}</g>`;
    }).join("");
    const item = schwartzValues[selected];
    document.querySelector("#schwartzDetail").innerHTML = `<p class="value-group">${item.group}</p><h3>${item.name}</h3><p>${item.motive}</p><dl><dt>Adjacent</dt><dd>${item.neighbor}</dd><dt>Opposes</dt><dd>${item.opposite}</dd></dl>`;
    svg.querySelectorAll(".value-node").forEach((node) => node.addEventListener("click", () => renderSchwartz("10", Number(node.dataset.index))));
  } else {
    const quadrants = [
      { path: "M260 260L260 65A195 195 0 0 1 455 260Z", x: 355, y: 165 },
      { path: "M260 260L455 260A195 195 0 0 1 260 455Z", x: 355, y: 355 },
      { path: "M260 260L260 455A195 195 0 0 1 65 260Z", x: 165, y: 355 },
      { path: "M260 260L65 260A195 195 0 0 1 260 65Z", x: 165, y: 165 },
    ];
    svg.innerHTML = `<circle cx="260" cy="260" r="195" fill="#f7f9f5" stroke="#d6dfd8"/>` + higherOrder.map((item, index) => `<g class="value-node${index === selected ? " active" : ""}" data-index="${index}"><path d="${quadrants[index].path}" fill="${item.color}" stroke="white" stroke-width="4"/><text x="${quadrants[index].x}" y="${quadrants[index].y}" text-anchor="middle">${item.name.split(" ").map((word, i) => `<tspan x="${quadrants[index].x}" dy="${i ? 14 : 0}">${word}</tspan>`).join("")}</text></g>`).join("") + `<circle cx="260" cy="260" r="74" fill="white"/><text class="center-label" x="260" y="255">higher-order</text><text class="center-label" x="260" y="276">organization</text>`;
    const item = higherOrder[selected];
    document.querySelector("#schwartzDetail").innerHTML = `<p class="value-group">Higher-order region</p><h3>${item.name}</h3><p>${item.motive}</p><dl><dt>Contains</dt><dd>${item.values}</dd><dt>Opposes</dt><dd>${item.opposite}</dd></dl>`;
    svg.querySelectorAll(".value-node").forEach((node) => node.addEventListener("click", () => renderSchwartz("4", Number(node.dataset.index))));
  }
}

function updateSvo() {
  const value = Number(document.querySelector("#svoSlider").value);
  const other = Math.round(value * .66);
  const self = 100 - other;
  document.querySelector("#selfAllocation").textContent = self;
  document.querySelector("#otherAllocation").textContent = other;
  document.querySelector("#svoLabel").textContent = value < 25 ? "Competitive region" : value < 50 ? "Individualistic region" : value < 80 ? "Prosocial region" : "Altruistic region";
}

function updateCultureMap() {
  const x = document.querySelector("#cultureX").value;
  const y = document.querySelector("#cultureY").value;
  const point = document.querySelector("#culturePoint");
  point.style.left = `${x}%`;
  point.style.bottom = `${y}%`;
}

const moral = [
  { name: "Care", value: 78 }, { name: "Fairness", value: 69 }, { name: "Loyalty", value: 42 },
  { name: "Authority", value: 35 }, { name: "Sanctity", value: 28 }, { name: "Liberty", value: 74 },
];

function renderMoral() {
  const controls = document.querySelector("#moralControls");
  if (!controls.children.length) {
    controls.innerHTML = moral.map((item, index) => `<label class="moral-control"><span>${item.name}</span><input type="range" min="0" max="100" value="${item.value}" data-moral="${index}"/><output>${item.value}</output></label>`).join("");
    controls.querySelectorAll("input").forEach((input) => input.addEventListener("input", () => {
      moral[Number(input.dataset.moral)].value = Number(input.value);
      input.nextElementSibling.value = input.value;
      drawRadar();
    }));
  }
  drawRadar();
}

function radarPoint(index, value, radius = 155) {
  const angle = -90 + index * 60;
  return polarFrom(260, 220, angle, radius * value / 100);
}

function polarFrom(cx, cy, angle, radius) {
  const radians = angle * Math.PI / 180;
  return { x: cx + Math.cos(radians) * radius, y: cy + Math.sin(radians) * radius };
}

function drawRadar() {
  const svg = document.querySelector("#moralRadar");
  const rings = [25, 50, 75, 100].map((level) => `<polygon class="radar-grid" points="${moral.map((_, i) => { const p = radarPoint(i, level); return `${p.x},${p.y}`; }).join(" ")}"/>`).join("");
  const axes = moral.map((_, i) => { const p = radarPoint(i, 100); return `<line class="radar-axis" x1="260" y1="220" x2="${p.x}" y2="${p.y}"/>`; }).join("");
  const shape = moral.map((item, i) => { const p = radarPoint(i, item.value); return `${p.x},${p.y}`; }).join(" ");
  const labels = moral.map((item, i) => { const p = radarPoint(i, 118); return `<text class="radar-label" x="${p.x}" y="${p.y + 4}">${item.name}</text>`; }).join("");
  svg.innerHTML = `${rings}${axes}<polygon class="radar-shape" points="${shape}"/>${labels}`;
}

function nativeContent(key) {
  if (key === "gpla") return `<div class="native-layout"><div class="native-copy"><p class="lab-kicker">INDUCED, INTERPRETABLE</p><h3>GPLA</h3><p>A generative psycho-lexical pipeline begins with 123 atomic value terms and induces five factors from patterns observed across LLMs.</p><div class="native-stat"><div><b>123</b><span>atomic values</span></div><div><b>5</b><span>induced factors</span></div></div><a class="inline-source" href="https://aclanthology.org/2025.acl-long.585/">Read the paper ↗</a></div><div class="factor-stack">${["Social Responsibility", "Risk-Taking", "Rule-Following", "Self-Competence", "Rationality"].map((name, i) => `<div class="factor-bar"><i style="width:${[88,58,76,68,82][i]}%"></i><span>${name}</span></div>`).join("")}</div></div>`;
  if (key === "univar") {
    const dots = [[18,22],[27,31],[33,19],[62,25],[74,31],[68,43],[45,68],[56,76],[38,81],[82,71],[20,65],[52,45]];
    return `<div class="native-layout"><div class="native-copy"><p class="lab-kicker">LATENT, CONTINUOUS</p><h3>UniVaR</h3><p>Question–answer sets are encoded into a dense model–language representation. Nearby points indicate similarity under the learned objective; the plotted axes themselves have no fixed value names.</p><div class="native-stat"><div><b>25</b><span>languages / cultures evaluated</span></div><div><b>15</b><span>models evaluated</span></div></div><a class="inline-source" href="https://aclanthology.org/2025.naacl-long.274/">Read the paper ↗</a></div><div class="latent-map">${dots.map(([x,y]) => `<i class="latent-dot" style="left:${x}%;top:${y}%"></i>`).join("")}<small>illustrative 2D projection · not paper data</small></div></div>`;
  }
  if (key === "kaleidoscope") return `<div class="native-layout"><div class="native-copy"><p class="lab-kicker">CONTEXTUAL ONTOLOGY</p><h3>Value Kaleidoscope</h3><p>A situation can activate multiple values, rights, and duties with different relations and valence. The structure preserves plurality instead of forcing every concept onto one axis.</p><div class="native-stat"><div><b>218k</b><span>values, rights, and duties</span></div><div><b>31k</b><span>situations</span></div></div><a class="inline-source" href="https://doi.org/10.1609/aaai.v38i18.29970">Read the paper ↗</a></div><div class="ontology"><svg viewBox="0 0 460 330"><g stroke="#adbbb4" stroke-width="2"><path d="M230 165L98 70M230 165L362 70M230 165L102 260M230 165L358 260"/></g><circle cx="230" cy="165" r="58" fill="#12634f"/><circle cx="98" cy="70" r="42" fill="#c7eadc"/><circle cx="362" cy="70" r="42" fill="#e9b44c"/><circle cx="102" cy="260" r="42" fill="#d88a75"/><circle cx="358" cy="260" r="42" fill="#806ca8"/><g text-anchor="middle" font-size="12"><text x="230" y="169" fill="white">situation</text><text x="98" y="74">value</text><text x="362" y="74">right</text><text x="102" y="264">duty</text><text x="358" y="264" fill="white">valence</text></g></svg></div></div>`;
  return `<div class="native-layout"><div class="native-copy"><p class="lab-kicker">OPEN, SUPPLIED AT RUNTIME</p><h3>Generative psychometrics</h3><p>GPV can test values supplied at measurement time. This expands coverage beyond a fixed inventory, while making the wording of each value and the scorer part of the contract.</p><div class="native-stat"><div><b>dynamic</b><span>value vocabulary</span></div><div><b>explicit</b><span>scorer dependence</span></div></div><a class="inline-source" href="https://doi.org/10.1609/aaai.v39i25.34839">Read the paper ↗</a></div><div class="open-builder"><label for="openValue">Add a value concept</label><div class="open-row"><input id="openValue" placeholder="e.g. epistemic humility" maxlength="40"/><button id="addValue">Add</button></div><div class="value-chips" id="valueChips"><button>care</button><button>prudence</button><button>transparency</button></div></div></div>`;
}

function renderNative(key) {
  document.querySelector("#nativeStage").innerHTML = nativeContent(key);
  if (key === "gpv") {
    const add = () => {
      const input = document.querySelector("#openValue");
      const value = input.value.trim();
      if (!value) return;
      document.querySelector("#valueChips").insertAdjacentHTML("beforeend", `<button>${escapeHtml(value)}</button>`);
      input.value = "";
    };
    document.querySelector("#addValue").addEventListener("click", add);
    document.querySelector("#openValue").addEventListener("keydown", (event) => { if (event.key === "Enter") add(); });
  }
}

function renderInterface(key) {
  const item = interfaces[key];
  document.querySelector("#interfaceEvidence").textContent = item.evidence;
  document.querySelector("#interfaceExample").textContent = item.example;
  document.querySelector("#interfaceClaim").textContent = item.claim;
  document.querySelector("#interfaceCaution").textContent = item.caution;
}

document.querySelectorAll(".grammar-step").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".grammar-step").forEach((item) => item.classList.toggle("active", item === button));
  renderGrammar(button.dataset.grammar);
}));

document.querySelectorAll(".shape-chip").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".shape-chip").forEach((item) => item.classList.toggle("active", item === button));
  renderShape(button.dataset.shape);
}));

document.querySelectorAll("[data-schwartz-view]").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll("[data-schwartz-view]").forEach((item) => item.classList.toggle("active", item === button));
  renderSchwartz(button.dataset.schwartzView, 0);
}));

document.querySelectorAll(".native-tab").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".native-tab").forEach((item) => item.classList.toggle("active", item === button));
  renderNative(button.dataset.native);
}));

document.querySelectorAll(".interface-tab").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".interface-tab").forEach((item) => item.classList.toggle("active", item === button));
  renderInterface(button.dataset.interface);
}));

document.querySelector("#svoSlider").addEventListener("input", updateSvo);
document.querySelector("#cultureX").addEventListener("input", updateCultureMap);
document.querySelector("#cultureY").addEventListener("input", updateCultureMap);

const chapters = [...document.querySelectorAll(".chapter")];
const chapterLinks = [...document.querySelectorAll(".chapter-link")];
const observer = new IntersectionObserver((entries) => {
  const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
  if (!visible) return;
  chapterLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${visible.target.id}`));
}, { rootMargin: "-20% 0px -65%", threshold: [0, .2, .5] });
chapters.forEach((chapter) => observer.observe(chapter));

window.addEventListener("scroll", () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  document.querySelector("#readingProgress").style.width = `${max > 0 ? window.scrollY / max * 100 : 0}%`;
}, { passive: true });

renderGrammar("axiology");
renderShape("circumplex");
renderSchwartz("10", 0);
updateSvo();
updateCultureMap();
renderMoral();
renderNative("gpla");
renderInterface("questionnaire");
