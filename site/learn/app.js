const wikiRoot = document.body.dataset.wikiRoot || "";

function escapeHtml(value = "") {
  return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

function buttonGroup(items, activeIndex = 0, className = "widget-button") {
  return items.map((item, index) => `<button type="button" class="${className}${index === activeIndex ? " active" : ""}" data-index="${index}" aria-pressed="${index === activeIndex}">${escapeHtml(item)}</button>`).join("");
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

const pipelineContent = {
  grammar: [
    ["Axiology", "Defines which values exist and how relations among them are represented."],
    ["Instrument", "Operationalizes a construct through reusable items, tasks, or environments."],
    ["Interface", "Specifies whether the subject rates, chooses, generates, ranks, or acts."],
    ["Scorer", "Maps raw evidence into labels, dimensions, probabilities, or embeddings."],
    ["Claim", "States the narrow conclusion licensed by the complete measurement chain."],
  ],
  scoring: [
    ["Response", "Raw ratings, choices, text, or trajectories remain the primary evidence object."],
    ["Input unit", "Whole response, sentence, proposition, or action window changes scorer context."],
    ["Mapper", "A key, classifier, generative scorer, encoder, or judge produces a representation."],
    ["Policy", "Thresholds, coverage, missingness, and zero-evidence rules shape the result."],
    ["Aggregate", "Item and value aggregation determines the reported profile or similarity."],
  ],
};

function pipelineWidget(canvas, type) {
  const items = pipelineContent[type];
  canvas.innerHTML = `<div class="pipeline">${items.map(([name], index) => `<button type="button" class="${index === 0 ? "active" : ""}" data-index="${index}" aria-pressed="${index === 0}">${index + 1}. ${name}</button>`).join("")}</div><div class="pipeline-detail"></div>`;
  const detail = canvas.querySelector(".pipeline-detail");
  const select = (index) => {
    const [name, description] = items[index];
    canvas.querySelectorAll(".pipeline button").forEach((button, buttonIndex) => {
      button.classList.toggle("active", buttonIndex === index);
      button.setAttribute("aria-pressed", String(buttonIndex === index));
    });
    detail.innerHTML = `<h3>${escapeHtml(name)}</h3><p>${escapeHtml(description)}</p>`;
  };
  canvas.querySelectorAll(".pipeline button").forEach((button) => button.addEventListener("click", () => select(Number(button.dataset.index))));
  select(0);
}

const shapeInfo = [
  ["Circumplex", "Neighborhood and opposition", "Schwartz"],
  ["Bipolar axes", "Position between named poles", "Inglehart–Welzel"],
  ["Hierarchy", "Level or priority order", "Rokeach / Functional Theory"],
  ["Ontology", "Typed concepts and relations", "Value Kaleidoscope"],
  ["Induced factors", "Recurring structure learned from data", "GPLA"],
  ["Latent space", "Similarity without named coordinates", "UniVaR"],
  ["Open set", "Values supplied at measurement time", "GPV"],
];

function shapeSvg(index) {
  const color = ["#12634f", "#d77863", "#806ca8", "#6f91b8", "#e9b44c", "#12634f", "#d77863"][index];
  if (index === 0) return `<svg class="widget-svg" viewBox="0 0 420 300"><circle cx="210" cy="150" r="110" fill="#eef3ef" stroke="#aebdb5"/><g fill="${color}">${[0,60,120,180,240,300].map((angle) => { const r=angle*Math.PI/180; return `<circle cx="${210+110*Math.cos(r)}" cy="${150+110*Math.sin(r)}" r="19"/>`; }).join("")}</g><text x="210" y="154" text-anchor="middle" font-family="Georgia" font-size="18">relations</text></svg>`;
  if (index === 1) return `<svg class="widget-svg" viewBox="0 0 420 300"><rect x="55" y="30" width="310" height="240" fill="#eef3ef" stroke="#aebdb5"/><path d="M210 30V270M55 150H365" stroke="#17201d"/><circle cx="282" cy="92" r="14" fill="${color}" stroke="white" stroke-width="5"/></svg>`;
  if (index === 2) return `<svg class="widget-svg" viewBox="0 0 420 300"><path d="M210 68V112M90 160V220M210 160V220M330 160V220M90 112H330M90 112V160M210 112V160M330 112V160" fill="none" stroke="#9caaa2"/><rect x="150" y="25" width="120" height="44" rx="22" fill="${color}"/><g fill="#dce8e1"><rect x="45" y="135" width="90" height="44" rx="22"/><rect x="165" y="135" width="90" height="44" rx="22"/><rect x="285" y="135" width="90" height="44" rx="22"/></g></svg>`;
  if (index === 3) return `<svg class="widget-svg" viewBox="0 0 420 300"><g stroke="#aebdb5"><path d="M210 150L90 70M210 150L330 70M210 150L95 235M210 150L325 235"/></g><circle cx="210" cy="150" r="45" fill="${color}"/><g fill="#c8e7da"><circle cx="90" cy="70" r="30"/><circle cx="330" cy="70" r="30"/><circle cx="95" cy="235" r="30"/><circle cx="325" cy="235" r="30"/></g></svg>`;
  if (index === 4) return `<svg class="widget-svg" viewBox="0 0 420 300"><g fill="#d8e6df"><rect x="55" y="45" width="170" height="17"/><rect x="55" y="80" width="270" height="17"/><rect x="55" y="115" width="210" height="17"/><rect x="55" y="150" width="300" height="17"/><rect x="55" y="185" width="135" height="17"/></g><path d="M338 55C385 100 385 180 338 220" fill="none" stroke="${color}" stroke-width="4"/></svg>`;
  if (index === 5) return `<svg class="widget-svg" viewBox="0 0 420 300"><rect x="45" y="25" width="330" height="250" fill="#eef3ef" stroke="#aebdb5"/>${[[90,80],[120,105],[105,140],[280,75],[310,115],[275,140],[190,220],[225,235],[245,205]].map(([x,y],i)=>`<circle cx="${x}" cy="${y}" r="9" fill="${i<3?'#12634f':i<6?'#d77863':'#806ca8'}"/>`).join("")}</svg>`;
  return `<svg class="widget-svg" viewBox="0 0 420 300"><rect x="62" y="55" width="296" height="55" rx="4" fill="white" stroke="#aebdb5"/><rect x="76" y="145" width="90" height="32" rx="16" fill="#c8e7da"/><rect x="176" y="145" width="90" height="32" rx="16" fill="#e9b44c"/><rect x="276" y="145" width="74" height="32" rx="16" fill="#d77863"/><rect x="135" y="195" width="80" height="32" rx="16" fill="#806ca8"/><rect x="225" y="195" width="110" height="32" rx="16" fill="#6f91b8"/></svg>`;
}

function shapeGallery(canvas) {
  canvas.innerHTML = `<div class="widget-toolbar">${buttonGroup(shapeInfo.map((item) => item[0]))}</div><div class="widget-grid"><div class="shape-drawing"></div><div class="widget-copy"></div></div>`;
  const render = (index) => {
    canvas.querySelectorAll(".widget-button").forEach((button, buttonIndex) => { button.classList.toggle("active", buttonIndex === index); button.setAttribute("aria-pressed", String(buttonIndex === index)); });
    canvas.querySelector(".shape-drawing").innerHTML = shapeSvg(index);
    const [title, relation, example] = shapeInfo[index];
    canvas.querySelector(".widget-copy").innerHTML = `<h3>${title}</h3><p>The representation makes <b>${relation.toLowerCase()}</b> natural to inspect.</p><dl><dt>Example</dt><dd>${example}</dd><dt>Preserves</dt><dd>${relation}</dd></dl>`;
  };
  canvas.querySelectorAll(".widget-button").forEach((button) => button.addEventListener("click", () => render(Number(button.dataset.index))));
  render(0);
}

const interfaceItems = [
  ["Questionnaire", "Standardized item responses", "Protocol-conditioned stated profile"],
  ["Endorsement", "Independent rating of each alternative", "Item-level endorsement"],
  ["Conflict choice", "One alternative selected over another", "Task-bounded priority"],
  ["Free text", "Generated rationale or recommendation", "Textual framing under a scorer"],
  ["Observed action", "Action in an environment", "Task-bounded behavioral evidence"],
];

function interfacesWidget(canvas) {
  canvas.innerHTML = `<div class="widget-toolbar">${buttonGroup(interfaceItems.map((item) => item[0]))}</div><div class="scenario-box"><small>SHARED SITUATION</small><p>A team chooses between immediate usefulness and a longer safety review.</p></div><div class="pipeline-detail"></div>`;
  const render = (index) => {
    canvas.querySelectorAll(".widget-button").forEach((button, i) => { button.classList.toggle("active", i === index); button.setAttribute("aria-pressed", String(i === index)); });
    const [name, evidence, claim] = interfaceItems[index];
    canvas.querySelector(".pipeline-detail").innerHTML = `<h3>${name}</h3><p><b>Observed:</b> ${evidence}. <b>Reportable:</b> ${claim}.</p>`;
  };
  canvas.querySelectorAll(".widget-button").forEach((button) => button.addEventListener("click", () => render(Number(button.dataset.index))));
  render(0);
}

function validityWidget(canvas) {
  const steps = [
    ["01", "Parse and coverage", "Can the protocol produce usable evidence without selective loss?"],
    ["02", "Within-interface reliability", "Does the result survive repetition and plausible prompt variants?"],
    ["03", "Convergent evidence", "Do independent operationalizations of the intended construct agree?"],
    ["04", "Cross-interface transfer", "Does evidence carry across endorsement, choice, text, or action?"],
    ["05", "Specificity and prediction", "Is the profile distinctive and useful beyond the measurement sample?"],
  ];
  canvas.innerHTML = `<div class="validity-ladder">${steps.map(([number,name,text],index)=>`<div class="validity-step${index===0?' active':''}" tabindex="0"><strong>${number}</strong><b>${name}</b><span>${text}</span></div>`).join("")}</div>`;
  canvas.querySelectorAll(".validity-step").forEach((step) => {
    const activate = () => { canvas.querySelectorAll(".validity-step").forEach((item) => item.classList.remove("active")); step.classList.add("active"); };
    step.addEventListener("click", activate);
    step.addEventListener("keydown", (event) => { if (["Enter", " "].includes(event.key)) { event.preventDefault(); activate(); } });
  });
}

function frameworkWidget(canvas) {
  const choices = [
    ["Named motives", "Schwartz, Rokeach, or Functional Theory"],
    ["Moral concerns", "Moral Foundations"],
    ["Aggregate culture", "WVS-derived maps, Hofstede, or GLOBE"],
    ["AI-native factors", "GPLA"],
    ["Model/language similarity", "UniVaR"],
    ["Contextual principles", "Value Kaleidoscope or an explicit constitution"],
    ["Open-vocabulary scoring", "GPV with a named scorer contract"],
  ];
  canvas.innerHTML = `<div class="widget-toolbar">${buttonGroup(choices.map((item) => item[0]))}</div><div class="widget-panel"></div>`;
  const render = (index) => {
    canvas.querySelectorAll(".widget-button").forEach((button,i)=>{button.classList.toggle("active",i===index);button.setAttribute("aria-pressed",String(i===index));});
    canvas.querySelector(".widget-panel").innerHTML = `<small>Candidate family</small><h3>${choices[index][1]}</h3><p>This is a starting point. Unit of analysis, interface, and validation requirements still determine the final design.</p>`;
  };
  canvas.querySelectorAll(".widget-button").forEach((button)=>button.addEventListener("click",()=>render(Number(button.dataset.index))));
  render(0);
}

function compassWidget(canvas, dimensions, pageId) {
  const shown = dimensions.length ? dimensions : ["Open", "Variable", "Contextual"];
  const dense = shown.length > 12 ? " dense" : "";
  canvas.innerHTML = `<div class="compass-widget"><div class="compass-stage${dense}">${shown.map((name,index)=>{const angle=(-90+index*360/shown.length)*Math.PI/180;const left=50+41*Math.cos(angle);const top=50+41*Math.sin(angle);return `<button type="button" class="compass-node${index===0?' active':''}" style="left:${left}%;top:${top}%" data-index="${index}" aria-pressed="${index===0}">${escapeHtml(name)}</button>`;}).join("")}</div><div class="widget-panel"></div></div>`;
  const render = (index) => {
    canvas.querySelectorAll(".compass-node").forEach((button,i)=>{button.classList.toggle("active",i===index);button.setAttribute("aria-pressed",String(i===index));});
    const name = shown[index];
    const previous = shown[(index - 1 + shown.length) % shown.length];
    const next = shown[(index + 1) % shown.length];
    const opposite = shown[(index + Math.floor(shown.length / 2)) % shown.length];
    const schwartzTenOppositions = {
      "Self-Direction": "Conformity / Tradition", "Stimulation": "Security / Conformity",
      "Hedonism": "Tradition", "Achievement": "Benevolence", "Power": "Universalism",
      "Security": "Stimulation", "Conformity": "Self-Direction", "Tradition": "Hedonism / Stimulation",
      "Benevolence": "Achievement", "Universalism": "Power",
    };
    const opposition = pageId === "schwartz-tbv-10" ? schwartzTenOppositions[name] : `${opposite} (approximate equal-sector position)`;
    canvas.querySelector(".widget-panel").innerHTML = `<small>Selected coordinate</small><h3>${escapeHtml(name)}</h3><p><b>Adjacent:</b> ${escapeHtml(previous)} and ${escapeHtml(next)}.<br/><b>Motivational tension:</b> ${escapeHtml(opposition)}.</p>`;
  };
  canvas.querySelectorAll(".compass-node").forEach((button)=>button.addEventListener("click",()=>render(Number(button.dataset.index))));
  render(0);
}

function quadrantWidget(canvas, dimensions) {
  const values = dimensions.length === 4 ? dimensions : ["A","B","C","D"];
  canvas.innerHTML = `<div class="principle-grid">${values.map((value,index)=>`<button type="button" class="principle-card${index===0?' active':''}" data-index="${index}" aria-pressed="${index===0}"><h3>${escapeHtml(value)}</h3><p>${index<2?'Change and personal focus':'Stability and concern beyond self'}</p></button>`).join("")}</div>`;
  canvas.querySelectorAll(".principle-card").forEach((button)=>button.addEventListener("click",()=>{canvas.querySelectorAll(".principle-card").forEach((item)=>{item.classList.toggle("active",item===button);item.setAttribute("aria-pressed",String(item===button));});}));
}

function radarWidget(canvas, dimensions) {
  const labels = dimensions.slice(0, 9);
  const values = labels.map((_, index) => 38 + (index * 17) % 53);
  canvas.innerHTML = `<div class="radar-layout"><div class="range-list">${labels.map((label,index)=>`<label><span>${escapeHtml(label)}</span><input type="range" min="0" max="100" value="${values[index]}" data-index="${index}"/><output>${values[index]}</output></label>`).join("")}</div><svg class="radar-svg" viewBox="0 0 420 360" role="img" aria-label="Illustrative profile"></svg></div>`;
  const svg = canvas.querySelector("svg");
  const point = (index, value, radius=125) => { const angle=(-90+index*360/labels.length)*Math.PI/180; return [210+Math.cos(angle)*radius*value/100,180+Math.sin(angle)*radius*value/100]; };
  const draw = () => {
    const rings = [25,50,75,100].map(level=>`<polygon fill="none" stroke="#d8dfda" points="${labels.map((_,i)=>point(i,level).join(',')).join(' ')}"/>`).join('');
    const axes = labels.map((_,i)=>{const [x,y]=point(i,100);return `<line x1="210" y1="180" x2="${x}" y2="${y}" stroke="#d8dfda"/>`;}).join('');
    const profile = labels.map((_,i)=>point(i,values[i]).join(',')).join(' ');
    const text = labels.map((label,i)=>{const [x,y]=point(i,118);return `<text x="${x}" y="${y}" text-anchor="middle" font-size="10" fill="#65716d">${escapeHtml(label.length>18?label.slice(0,16)+'…':label)}</text>`;}).join('');
    svg.innerHTML = `${rings}${axes}<polygon points="${profile}" fill="rgba(18,99,79,.22)" stroke="#12634f" stroke-width="3"/>${text}`;
  };
  canvas.querySelectorAll("input").forEach(input=>input.addEventListener("input",()=>{values[Number(input.dataset.index)]=Number(input.value);input.nextElementSibling.value=input.value;draw();}));
  draw();
}

function axesWidget(canvas, dimensions) {
  const split = (value, fallback) => (value || fallback).split(/\s+vs\.?\s+/i);
  const x = split(dimensions[0], "Traditional vs. Secular-Rational");
  const y = split(dimensions[1], "Survival vs. Self-Expression");
  canvas.innerHTML = `<div class="axis-map"><span class="axis-label left">${escapeHtml(x[0])}</span><span class="axis-label right">${escapeHtml(x[1]||'Pole B')}</span><span class="axis-label bottom">${escapeHtml(y[0])}</span><span class="axis-label top">${escapeHtml(y[1]||'Pole B')}</span><i class="axis-point"></i></div><div class="axis-controls"><label>${escapeHtml(dimensions[0]||'Horizontal axis')}<input data-axis="x" type="range" min="0" max="100" value="62"/></label><label>${escapeHtml(dimensions[1]||'Vertical axis')}<input data-axis="y" type="range" min="0" max="100" value="68"/></label></div>`;
  const update = () => { const xValue=canvas.querySelector('[data-axis="x"]').value;const yValue=canvas.querySelector('[data-axis="y"]').value;const point=canvas.querySelector('.axis-point');point.style.left=`${xValue}%`;point.style.bottom=`${yValue}%`; };
  canvas.querySelectorAll("input").forEach(input=>input.addEventListener("input",update));
  update();
}

function surveyWidget(canvas) {
  const topics = ["Family", "Work", "Religion", "Politics", "Trust", "Environment", "Gender", "Technology", "Security", "Well-being", "Migration", "Democracy"];
  canvas.innerHTML = `<div class="widget-toolbar">${buttonGroup(["Selected items","Thematic batteries","Response distributions","Derived dimensions"])}</div><div class="dimension-list">${topics.map((topic,index)=>`<span><b>${String(index+1).padStart(2,'0')}</b>${topic}</span>`).join('')}</div>`;
  canvas.querySelectorAll(".widget-button").forEach(button=>button.addEventListener("click",()=>{canvas.querySelectorAll('.widget-button').forEach(item=>{item.classList.toggle('active',item===button);item.setAttribute('aria-pressed',String(item===button));});}));
}

function rankWidget(canvas, dimensions) {
  const items = dimensions.slice(0, 10);
  const render = () => {
    canvas.innerHTML = `<p class="widget-intro">Move an item upward to see how a ranking preserves order but not distance.</p><div class="rank-list">${items.map((item,index)=>`<div class="rank-item"><span>${escapeHtml(item)}</span><button type="button" data-index="${index}" ${index===0?'disabled':''}>Move up</button></div>`).join('')}</div>`;
    canvas.querySelectorAll(".rank-item button").forEach(button=>button.addEventListener("click",()=>{const index=Number(button.dataset.index);[items[index-1],items[index]]=[items[index],items[index-1]];render();}));
  };
  render();
}

function continuumWidget(canvas) {
  const presets = [
    ["Competitive", 70, 30, "Maximize advantage over the other allocation."],
    ["Individualistic", 70, 55, "Prioritize own outcome without maximizing equality."],
    ["Prosocial", 60, 60, "Balance joint outcome and equality."],
    ["Altruistic", 45, 70, "Give relatively more weight to the other's outcome."],
  ];
  canvas.innerHTML = `<div class="widget-toolbar">${buttonGroup(presets.map(item=>item[0]))}</div><div class="widget-grid"><div class="allocation-view"></div><div class="widget-copy"></div></div>`;
  const render=(index)=>{canvas.querySelectorAll('.widget-button').forEach((button,i)=>{button.classList.toggle('active',i===index);button.setAttribute('aria-pressed',String(i===index));});const [name,self,other,text]=presets[index];canvas.querySelector('.allocation-view').innerHTML=`<div class="factor-list"><div class="factor-row"><i style="width:${self}%"></i><span>Self · ${self}</span></div><div class="factor-row"><i style="width:${other}%"></i><span>Other · ${other}</span></div></div>`;canvas.querySelector('.widget-copy').innerHTML=`<h3>${name}</h3><p>${text}</p><p>This is a geometry demonstration, not the official multi-item SVO Slider score.</p>`;};
  canvas.querySelectorAll('.widget-button').forEach(button=>button.addEventListener('click',()=>render(Number(button.dataset.index))));render(0);
}

function functionalMatrix(canvas) {
  const cells = [["Excitement","Suprapersonal","Interactive"],["Promotion","Existence","Normative"]];
  canvas.innerHTML = `<div class="matrix-widget"><div></div><div class="matrix-head">Personal</div><div class="matrix-head">Central</div><div class="matrix-head">Social</div><div class="matrix-head">Humanitarian</div>${cells[0].map(item=>`<div>${item}</div>`).join('')}<div class="matrix-head">Materialistic</div>${cells[1].map(item=>`<div>${item}</div>`).join('')}</div>`;
}

function factorsWidget(canvas, dimensions) {
  const widths=[86,58,74,67,81,62,77,55,71];
  canvas.innerHTML=`<div class="factor-list">${dimensions.map((name,index)=>`<div class="factor-row"><i style="width:${widths[index%widths.length]}%"></i><span>${escapeHtml(name)}</span></div>`).join('')}</div><p class="widget-intro">Bar lengths are illustrative. In the method, factors are induced from loading patterns across atomic values.</p>`;
}

function latentWidget(canvas) {
  const dots=[[12,18],[19,26],[27,16],[22,39],[62,18],[71,29],[79,21],[67,43],[40,69],[50,78],[58,65],[46,52],[82,75],[25,72]];
  canvas.innerHTML=`<div class="latent-stage">${dots.map(([x,y],index)=>`<i class="latent-dot ${index%3===1?'coral':index%3===2?'violet':''}" style="left:${x}%;top:${y}%"></i>`).join('')}</div><div class="widget-toolbar"><button type="button" class="widget-button active" aria-pressed="true">Model clusters</button><button type="button" class="widget-button" aria-pressed="false">Language clusters</button></div>`;
  canvas.querySelectorAll('.widget-button').forEach((button,index)=>button.addEventListener('click',()=>{canvas.querySelectorAll('.widget-button').forEach(item=>{item.classList.toggle('active',item===button);item.setAttribute('aria-pressed',String(item===button));});canvas.querySelectorAll('.latent-dot').forEach((dot,dotIndex)=>{dot.style.transform=index?`translate(${(dotIndex%4)*7}px, ${(dotIndex%3)*-6}px)`:'none';});}));
}

function ontologyWidget(canvas) {
  const nodes=[["Situation",50,50],["Value",18,18],["Right",82,18],["Duty",18,82],["Stakeholder",82,82]];
  canvas.innerHTML=`<div class="latent-stage ontology-stage">${nodes.map(([name,x,y],index)=>`<button type="button" class="compass-node${index===0?' active':''}" style="left:${x}%;top:${y}%" data-name="${name}" aria-pressed="${index===0}">${name}</button>`).join('')}</div><div class="pipeline-detail"><h3>Situation</h3><p>The context connects relevant values, rights, duties, and affected stakeholders.</p></div>`;
  canvas.querySelectorAll('.compass-node').forEach(button=>button.addEventListener('click',()=>{canvas.querySelectorAll('.compass-node').forEach(item=>{item.classList.toggle('active',item===button);item.setAttribute('aria-pressed',String(item===button));});canvas.querySelector('.pipeline-detail').innerHTML=`<h3>${button.dataset.name}</h3><p>This node participates in typed contextual relations; it is not one coordinate of a global profile.</p>`;}));
}

function principlesWidget(canvas, dimensions) {
  const values=dimensions.length?dimensions:["Principle A","Principle B","Principle C"];
  canvas.innerHTML=`<div class="principle-grid">${values.map((value,index)=>`<button type="button" class="principle-card${index===0?' active':''}" aria-pressed="${index===0}"><h3>${escapeHtml(value)}</h3><p>Select to foreground this objective. Concrete cases can expose conflicts with the others.</p></button>`).join('')}</div>`;
  canvas.querySelectorAll('.principle-card').forEach(button=>button.addEventListener('click',()=>{button.classList.toggle('active');button.setAttribute('aria-pressed',String(button.classList.contains('active')));}));
}

function constitutionWidget(canvas) {
  const principles=["Avoid harmful assistance","Respect user autonomy","Acknowledge uncertainty"];
  const render=()=>{canvas.innerHTML=`<div class="rank-list">${principles.map((item,index)=>`<div class="rank-item"><span>${escapeHtml(item)}</span><button type="button" data-index="${index}" ${index===0?'disabled':''}>Move up</button></div>`).join('')}</div><p class="widget-intro">Changing content or priority changes the normative target.</p>`;canvas.querySelectorAll('button').forEach(button=>button.addEventListener('click',()=>{const i=Number(button.dataset.index);[principles[i-1],principles[i]]=[principles[i],principles[i-1]];render();}));};render();
}

function openWidget(canvas) {
  canvas.innerHTML=`<div class="open-builder"><form><input aria-label="Value concept" maxlength="45" placeholder="e.g. epistemic humility"/><button type="submit">Add value</button></form><div class="value-chips"><span>care</span><span>prudence</span><span>transparency</span></div></div>`;
  canvas.querySelector('form').addEventListener('submit',(event)=>{event.preventDefault();const input=canvas.querySelector('input');const value=input.value.trim();if(!value)return;canvas.querySelector('.value-chips').insertAdjacentHTML('beforeend',`<span>${escapeHtml(value)}</span>`);input.value='';});
}

function renderWidget(module) {
  const canvas=module.querySelector('.widget-canvas');
  const type=module.dataset.widget;
  let dimensions=[];
  try { dimensions=JSON.parse(module.dataset.dimensions||'[]'); } catch { dimensions=[]; }
  const handlers={
    grammar:()=>pipelineWidget(canvas,'grammar'),
    'shape-gallery':()=>shapeGallery(canvas),
    interfaces:()=>interfacesWidget(canvas),
    'scoring-pipeline':()=>pipelineWidget(canvas,'scoring'),
    'validity-ladder':()=>validityWidget(canvas),
    'framework-matrix':()=>frameworkWidget(canvas),
    circumplex:()=>compassWidget(canvas,dimensions,module.dataset.page),
    quadrants:()=>quadrantWidget(canvas,dimensions),
    radar:()=>radarWidget(canvas,dimensions),
    survey:()=>surveyWidget(canvas),
    axes2d:()=>axesWidget(canvas,dimensions),
    rank:()=>rankWidget(canvas,dimensions),
    continuum:()=>continuumWidget(canvas),
    'functional-matrix':()=>functionalMatrix(canvas),
    factors:()=>factorsWidget(canvas,dimensions),
    latent:()=>latentWidget(canvas),
    ontology:()=>ontologyWidget(canvas),
    principles:()=>principlesWidget(canvas,dimensions),
    constitution:()=>constitutionWidget(canvas),
    open:()=>openWidget(canvas),
  };
  (handlers[type]||(()=>{canvas.innerHTML='<p>Interactive example unavailable.</p>';}))();
}

document.querySelectorAll('.interactive-module').forEach(renderWidget);
