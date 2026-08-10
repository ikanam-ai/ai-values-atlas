const wikiRoot = document.body.dataset.wikiRoot || "";

function escapeHtml(value = "") {
  return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

const searchInput = document.querySelector("#wikiSearch");
const searchResults = document.querySelector("#searchResults");
let searchIndex = [];

fetch(`${wikiRoot}search.json`, { cache: "no-store" })
  .then((response) => response.ok ? response.json() : Promise.reject(new Error(`HTTP ${response.status}`)))
  .then((rows) => { searchIndex = rows; })
  .catch(() => { searchInput.placeholder = "Search unavailable"; });

function renderSearch() {
  const query = searchInput.value.trim().toLowerCase();
  if (!query) { searchResults.hidden = true; searchResults.innerHTML = ""; return; }
  const tokens = query.split(/\s+/).filter(Boolean);
  const matches = searchIndex.filter((item) => {
    const text = `${item.title} ${item.summary} ${item.group}`.toLowerCase();
    return tokens.every((token) => text.includes(token));
  }).slice(0, 10);
  searchResults.innerHTML = matches.length ? matches.map((item) =>
    `<a href="${wikiRoot}${escapeHtml(item.path)}/"><b>${escapeHtml(item.title)}</b><span>${escapeHtml(item.group)} · ${escapeHtml(item.summary)}</span></a>`
  ).join("") : '<p class="search-empty">No wiki page matches this search.</p>';
  searchResults.hidden = false;
}

searchInput.addEventListener("input", renderSearch);
searchInput.addEventListener("keydown", (event) => {
  if (event.key === "Escape") { searchInput.value = ""; renderSearch(); searchInput.blur(); }
});
document.addEventListener("click", (event) => {
  if (!event.target.closest(".wiki-search")) searchResults.hidden = true;
});

const menuButton = document.querySelector("#menuButton");
const searchButton = document.querySelector("#searchButton");
const sidebar = document.querySelector("#wikiSidebar");
menuButton.addEventListener("click", () => {
  const open = sidebar.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(open));
});
sidebar.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
  sidebar.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
}));
searchButton.addEventListener("click", () => {
  const open = document.querySelector(".wiki-search").classList.toggle("open");
  searchButton.setAttribute("aria-expanded", String(open));
  if (open) searchInput.focus();
});

window.addEventListener("scroll", () => {
  const maximum = document.documentElement.scrollHeight - window.innerHeight;
  document.querySelector("#readingProgress").style.width = `${maximum > 0 ? window.scrollY / maximum * 100 : 0}%`;
}, { passive: true });

const tocLinks = [...document.querySelectorAll(".article-toc a[href^='#']:not(.toc-top)")];
const tocTargets = tocLinks.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
if (tocTargets.length) {
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    tocLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${visible.target.id}`));
  }, { rootMargin: "-18% 0px -65%", threshold: [0, .2, .5] });
  tocTargets.forEach((target) => observer.observe(target));
}

function flow(items, caption = "") {
  return `<div class="static-flow">${items.map(([title, copy], index) => `<div class="flow-step"><i>${String(index + 1).padStart(2, "0")}</i><b>${escapeHtml(title)}</b><span>${escapeHtml(copy)}</span></div>`).join("")}</div>${caption ? `<p class="diagram-caption">${escapeHtml(caption)}</p>` : ""}`;
}

function grammarDiagram() {
  return flow([
    ["Axiology", "Which values and relations exist"],
    ["Instrument", "Reusable items or tasks"],
    ["Interface", "Rate, choose, generate, rank, act"],
    ["Scorer", "Map evidence into a space"],
    ["Claim", "The narrow conclusion licensed"],
  ], "Changing any stage changes the measurement contract.");
}

function scopeMap() {
  const systems = [
    ["Values", "good / desirable", "Schwartz · GPLA"],
    ["Norms & rights", "required / permitted", "constitutions · duties"],
    ["Virtues", "the good agent", "honesty · courage · care"],
    ["Preferences", "chosen under constraints", "SVO · revealed choice"],
    ["Beliefs", "taken to be true", "worldviews · causal models"],
  ];
  return `<div class="normative-system"><div class="system-orbit">${systems.map(([title, question, examples], index) => `<div class="system-node n${index + 1}"><b>${title}</b><span>${question}</span><small>${examples}</small></div>`).join("")}<div class="moral-crosscut"><b>Moral judgment</b><span>draws on values, duties, virtues, beliefs, and context</span></div></div><div class="action-output"><b>Observed speech · choice · action</b><span>evidence produced by the combined system under one interface</span></div></div><p class="diagram-caption">Moral values overlap axiology, while morality cross-cuts several normative and cognitive systems.</p>`;
}

function shapeGallery() {
  const rows = [
    ["○", "Circumplex", "adjacency + opposition", "Schwartz"],
    ["＋", "Bipolar axes", "position between poles", "Inglehart–Welzel"],
    ["⇅", "Hierarchy / rank", "order, not distance", "Rokeach"],
    ["⌘", "Ontology", "typed contextual relations", "Kaleidoscope"],
    ["▤", "Induced factors", "interpretable covariance", "GPLA"],
    ["∴", "Latent embedding", "distance without named axes", "UniVaR"],
    ["…", "Open set", "values supplied at runtime", "GPV"],
  ];
  return `<div class="shape-atlas">${rows.map(([icon, title, relation, example]) => `<div><i>${icon}</i><b>${title}</b><span>${relation}</span><small>${example}</small></div>`).join("")}</div>`;
}

function interfacesDiagram() {
  return `<div class="shared-situation"><small>ONE SHARED SITUATION</small><b>A team trades immediate usefulness against a longer safety review.</b></div>` + flow([
    ["L0 · Questionnaire", "Stated profile under a questionnaire protocol"],
    ["L1 · Endorse", "Independent item endorsement"],
    ["L2 · Choose", "Priority under explicit conflict"],
    ["L3 · Generate", "Free-text framing under a scorer"],
    ["Action", "Behavior in a specified environment"],
  ], "These outputs can converge, but they are not interchangeable observations.");
}

function scoringDiagram() {
  return flow([
    ["Raw response", "Preserve the primary evidence"],
    ["Input unit", "Whole text, sentence, proposition, or action window"],
    ["Mapper", "Key, classifier, generator, encoder, or judge"],
    ["Policy", "Threshold, coverage, missingness, contradiction"],
    ["Aggregate", "Item, value, model, and uncertainty"],
  ], "The input splitter and aggregation policy are part of the scorer, not invisible preprocessing.");
}

function validityDiagram() {
  const rows = [
    ["01", "Coverage", "usable evidence without selective loss"],
    ["02", "Reliability", "repeatability inside one protocol"],
    ["03", "Convergence", "agreement across independent operationalizations"],
    ["04", "Transfer", "agreement across interfaces or contexts"],
    ["05", "Specificity", "closer to self than to alternative subjects"],
    ["06", "Prediction", "evidence beyond the measurement sample"],
  ];
  return `<div class="validity-stack">${rows.map(([n, title, text]) => `<div><i>${n}</i><b>${title}</b><span>${text}</span></div>`).join("")}</div>`;
}

function frameworkMatrix() {
  const rows = [
    ["Broad profile", "Individual model", "Named motives", "Schwartz / Functional / Rokeach"],
    ["Moral lens", "Individual response", "Moral concerns", "MFT"],
    ["Culture", "Population", "Distribution / aggregate axes", "WVS / Hofstede / GLOBE"],
    ["LLM-native", "Model", "Named induced factors", "GPLA"],
    ["Identity", "Model × language", "Latent similarity", "UniVaR"],
    ["Context", "Situation", "Values, rights, duties", "Kaleidoscope / GPV"],
  ];
  return `<div class="comparison-matrix"><div class="matrix-header"><b>Question</b><b>Unit</b><b>Output</b><b>Candidate</b></div>${rows.map((row) => `<div>${row.map((cell) => `<span>${escapeHtml(cell)}</span>`).join("")}</div>`).join("")}</div>`;
}

function circumplex(dimensions) {
  const shown = dimensions.length ? dimensions : ["Open", "Variable", "Contextual"];
  return `<div class="static-compass"><div class="compass-ring">${shown.map((name, index) => { const angle = (-90 + index * 360 / shown.length) * Math.PI / 180; const left = 50 + 42 * Math.cos(angle); const top = 50 + 42 * Math.sin(angle); return `<span style="left:${left}%;top:${top}%">${escapeHtml(name)}</span>`; }).join("")}<b>compatibility<br/>↕<br/>conflict</b></div><div class="compass-key"><p><i class="adjacent"></i><b>Adjacent</b><span>motivationally compatible</span></p><p><i class="opposed"></i><b>Opposed</b><span>motivational tension</span></p></div></div>`;
}

function quadrants(dimensions) {
  const values = dimensions.length === 4 ? dimensions : ["Openness", "Self-Enhancement", "Conservation", "Self-Transcendence"];
  return `<div class="quadrant-map">${values.map((name, index) => `<div class="q${index + 1}"><b>${escapeHtml(name)}</b></div>`).join("")}<span class="axis-x">personal focus ← → social focus</span><span class="axis-y">change ← → stability</span></div>`;
}

function mftVersions() {
  const columns = [
    ["Classic MFQ-1", "5", ["Care", "Fairness", "Loyalty", "Authority", "Purity"]],
    ["Proposed extension", "5 + Liberty", ["Care", "Fairness", "Loyalty", "Authority", "Purity", "Liberty"]],
    ["MFQ-2", "6 · 36 items", ["Care", "Equality", "Proportionality", "Loyalty", "Authority", "Purity"]],
  ];
  return `<div class="version-columns">${columns.map(([title, count, values]) => `<div><p>${count}</p><h3>${title}</h3><ul>${values.map((value) => `<li>${value}</li>`).join("")}</ul></div>`).join("")}</div><p class="diagram-caption">“Six foundations” is ambiguous unless the instrument and version are named.</p>`;
}

function surveyDiagram() {
  const topics = ["family", "work", "religion", "politics", "trust", "environment", "gender", "security", "well-being", "migration", "democracy", "technology"];
  return `<div class="survey-bank"><div class="topic-cloud">${topics.map((topic) => `<span>${topic}</span>`).join("")}</div><div class="survey-derivations"><b>WVS item bank</b><i>→</i><span>question responses</span><i>→</i><span>population distributions</span><i>→</i><span>optional derived maps</span></div></div>`;
}

function axesDiagram(dimensions) {
  const split = (value, fallback) => (value || fallback).split(/\s+vs\.?\s+/i);
  const x = split(dimensions[0], "Traditional vs. Secular-Rational");
  const y = split(dimensions[1], "Survival vs. Self-Expression");
  return `<div class="static-axes"><i class="x-axis"></i><i class="y-axis"></i><span class="left">${escapeHtml(x[0])}</span><span class="right">${escapeHtml(x[1] || "Pole B")}</span><span class="bottom">${escapeHtml(y[0])}</span><span class="top">${escapeHtml(y[1] || "Pole B")}</span><div class="sample-cloud">societies,<br/>not people</div></div>`;
}

function profileBars(dimensions) {
  return `<div class="named-coordinate-list">${dimensions.map((name, index) => `<div><i>${String(index + 1).padStart(2, "0")}</i><b>${escapeHtml(name)}</b><span>country-level index</span></div>`).join("")}</div>`;
}

function practicesValues(dimensions) {
  return `<div class="two-view-grid"><div class="view-head"></div><div class="view-head">Practices · “as is”</div><div class="view-head">Values · “should be”</div>${dimensions.map((name) => `<b>${escapeHtml(name)}</b><span>observed cultural practice</span><span>desired cultural state</span>`).join("")}</div>`;
}

function terminalInstrumental(dimensions) {
  const terminal = dimensions.slice(0, 18);
  const instrumental = dimensions.slice(18, 36);
  return `<div class="split-lists"><div><p>18 terminal values</p><h3>Desired end states</h3><ol>${terminal.map((v) => `<li>${escapeHtml(v)}</li>`).join("")}</ol></div><div><p>18 instrumental values</p><h3>Preferred conduct</h3><ol>${instrumental.map((v) => `<li>${escapeHtml(v)}</li>`).join("")}</ol></div></div>`;
}

function svoAngle() {
  return `<div class="svo-figure"><div class="svo-plane"><i class="svo-ray"></i><span class="competitive">competitive</span><span class="individualistic">individualistic</span><span class="prosocial">prosocial</span><span class="altruistic">altruistic</span><b>other outcome ↑<br/><br/>self outcome →</b></div><p>Six primary allocation items estimate one continuous angle; labels summarize regions of that angle.</p></div>`;
}

function functionalMatrix() {
  const cells = [["Excitement", "Suprapersonal", "Interactive"], ["Promotion", "Existence", "Normative"]];
  return `<div class="functional-grid"><div></div><b>Personal</b><b>Central</b><b>Social</b><strong>Humanitarian</strong>${cells[0].map((item) => `<span>${item}</span>`).join("")}<strong>Materialistic</strong>${cells[1].map((item) => `<span>${item}</span>`).join("")}</div><p class="diagram-caption">Each subfunction contains three marker values: 6 subfunctions × 3 markers = 18 values.</p>`;
}

function factorStructure(dimensions) {
  return `<div class="factor-funnel"><div class="atom-field"><b>123</b><span>atomic values</span></div><i>factor analysis</i><div class="factor-output">${dimensions.map((name) => `<span>${escapeHtml(name)}</span>`).join("")}</div></div>`;
}

function latentMap() {
  const dots = [[12, 18, 0], [19, 26, 0], [27, 16, 0], [22, 39, 0], [62, 18, 1], [71, 29, 1], [79, 21, 1], [67, 43, 1], [40, 69, 2], [50, 78, 2], [58, 65, 2], [46, 52, 2], [82, 75, 3], [25, 72, 3]];
  return `<div class="latent-figure"><div class="latent-stage">${dots.map(([x, y, c]) => `<i class="c${c}" style="left:${x}%;top:${y}%"></i>`).join("")}<span class="axis-note x">unnamed projection axis</span><span class="axis-note y">unnamed projection axis</span></div><div class="latent-legend"><b>Distance and clusters may be meaningful</b><span>Individual coordinates are not named human values.</span></div></div>`;
}

function ontologyDiagram() {
  return `<div class="ontology-diagram"><div class="context-node">Situation</div><i class="line l1"></i><i class="line l2"></i><i class="line l3"></i><i class="line l4"></i><div class="ontology-node value">Value</div><div class="ontology-node right">Right</div><div class="ontology-node duty">Duty</div><div class="ontology-node stakeholder">Stakeholder</div><p>relevance · support · opposition · ambiguity</p></div>`;
}

function hhhTriangle() {
  return `<div class="hhh-figure"><svg viewBox="0 0 640 360" role="img" aria-label="Helpful, Honest, and Harmless objectives in tension"><path d="M320 42 88 310h464Z" fill="#edf3ef" stroke="#12634f" stroke-width="2"/><circle cx="320" cy="190" r="54" fill="#0d3f35"/><text x="320" y="186" text-anchor="middle" fill="white" font-size="18">response</text><text x="320" y="207" text-anchor="middle" fill="#b9d6ca" font-size="12">task-specific trade-off</text><text x="320" y="26" text-anchor="middle" font-size="20">Helpful</text><text x="54" y="334" font-size="20">Honest</text><text x="512" y="334" font-size="20">Harmless</text></svg></div>`;
}

function constitutionDiagram() {
  return flow([
    ["Constitution", "Natural-language principles"],
    ["Critique", "Identify conflicts with principles"],
    ["Revision", "Rewrite the response"],
    ["AI preferences", "Choose preferred outputs"],
    ["Training", "Update the assistant policy"],
  ], "This pipeline creates a normative target; it does not read out intrinsic values.");
}

function openPipeline() {
  return `<div class="gpv-diagram"><div class="text-block"><b>Long response</b><span>Several claims, speakers, and possible values</span></div><i>split without changing meaning</i><div class="perception-stack"><span>perception 01</span><span>perception 02</span><span>perception 03</span></div><i>score against supplied definitions</i><div class="value-stack"><span>Schwartz</span><span>GPLA</span><span>custom value</span></div></div>`;
}

function renderFigure(module) {
  const canvas = module.querySelector(".widget-canvas");
  let dimensions = [];
  try { dimensions = JSON.parse(module.dataset.dimensions || "[]"); } catch { dimensions = []; }
  const handlers = {
    grammar: grammarDiagram,
    "scope-map": scopeMap,
    "shape-gallery": shapeGallery,
    interfaces: interfacesDiagram,
    "scoring-pipeline": scoringDiagram,
    "validity-ladder": validityDiagram,
    "framework-matrix": frameworkMatrix,
    circumplex: () => circumplex(dimensions),
    quadrants: () => quadrants(dimensions),
    "mft-versions": mftVersions,
    survey: surveyDiagram,
    axes2d: () => axesDiagram(dimensions),
    "profile-bars": () => profileBars(dimensions),
    "practices-values": () => practicesValues(dimensions),
    "terminal-instrumental": () => terminalInstrumental(dimensions),
    "svo-angle": svoAngle,
    "functional-matrix": functionalMatrix,
    "factor-structure": () => factorStructure(dimensions),
    "latent-map": latentMap,
    ontology: ontologyDiagram,
    "hhh-triangle": hhhTriangle,
    constitution: constitutionDiagram,
    "open-pipeline": openPipeline,
  };
  canvas.innerHTML = (handlers[module.dataset.widget] || (() => '<p class="diagram-caption">Diagram unavailable.</p>'))();
}

document.querySelectorAll(".visual-module").forEach(renderFigure);
