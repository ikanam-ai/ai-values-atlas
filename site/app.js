const state = { data: null, view: "publications", search: "", scope: "", source: "", visible: 80 };

const content = document.querySelector("#content");
const resultCount = document.querySelector("#resultCount");
const loadMore = document.querySelector("#loadMore");
const filters = document.querySelector("#filters");
const indexHead = document.querySelector("#indexHead");
const viewTitle = document.querySelector("#viewTitle");

const viewNames = {
  publications: "Publications",
  datasets: "Datasets & benchmarks",
  tools: "Models, code & tools",
  axiologies: "Axiological spaces",
  instruments: "Measurement instruments",
  sources: "Source catalogs",
};

function escapeHtml(value = "") {
  return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

function titleFor(link) {
  const generic = new Set(["paper", "pdf", "code", "github", "dataset", "data", "model", "project", "website", "link"]);
  if (link.context_title && !generic.has(link.context_title.toLowerCase())) return link.context_title;
  if (link.label && !generic.has(link.label.toLowerCase())) return link.label;
  try { return new URL(link.url).pathname.split("/").filter(Boolean).slice(-2).join(" / ") || link.url; }
  catch { return link.url; }
}

function sourcesFor(link) {
  return [...new Set(link.occurrences.map((item) => item.catalog_id))];
}

function discoveryRows() {
  const datasetTerms = /dataset|benchmark|item bank|corpus|survey|questionnaire/i;
  let rows = state.data.links.filter((link) => {
    if (state.view === "publications") return link.link_type_guess === "publication";
    if (state.view === "datasets") return link.link_type_guess === "dataset" || datasetTerms.test(titleFor(link));
    return ["model", "repository", "project"].includes(link.link_type_guess);
  });
  const query = state.search.toLowerCase();
  return rows.filter((link) => {
    const haystack = [titleFor(link), link.label, link.url, ...sourcesFor(link), ...link.occurrences.map((item) => item.section)].join(" ").toLowerCase();
    return (!query || haystack.includes(query)) &&
      (!state.scope || link.scope_tier_guess === state.scope) &&
      (!state.source || sourcesFor(link).includes(state.source));
  }).sort((left, right) => {
    const weak = (link) => /^(?:\d{4}\.\d{4,5}|\d{4}\.[\w.-]+|collection|leaderboard|hf datasets|hg & ci)$/i.test(titleFor(link)) || /^https?:/i.test(titleFor(link));
    return Number(weak(left)) - Number(weak(right)) || titleFor(left).localeCompare(titleFor(right));
  });
}

function renderDiscovery() {
  const rows = discoveryRows();
  resultCount.textContent = `${rows.length.toLocaleString()} matching resources`;
  const visible = rows.slice(0, state.visible);
  content.innerHTML = visible.length ? visible.map((link) => {
    const sources = sourcesFor(link);
    const section = link.occurrences[0]?.section?.split(" / ").slice(-2).join(" / ") || "catalog entry";
    return `<article class="index-row">
      <div class="resource-title"><a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(titleFor(link))}</a><small>${escapeHtml(link.url)}</small></div>
      <div class="evidence-cell"><span class="tag">${escapeHtml(link.link_type_guess)}</span><span>${escapeHtml(link.scope_tier_guess)}</span></div>
      <div class="provenance-cell"><b>${escapeHtml(sources[0] || "")}</b><span title="${escapeHtml(section)}">${escapeHtml(section)}</span></div>
    </article>`;
  }).join("") : '<div class="empty">No resources match the current filters.</div>';
  loadMore.hidden = state.visible >= rows.length;
}

function renderAxiologies() {
  const rows = state.data.axiologies;
  resultCount.textContent = `${rows.length} mapped value representations`;
  content.innerHTML = rows.map((item) => `<article class="index-row entity-row">
    <div class="resource-title"><a href="${escapeHtml(item.primary_sources[0])}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a><small>${escapeHtml(item.origin_domain.replaceAll("_", " "))}</small></div>
    <div class="evidence-cell"><span class="tag">${escapeHtml(item.representation_type.replaceAll("_", " "))}</span><span>${item.dimension_count ?? "open"} dimensions</span></div>
    <div class="provenance-cell"><b>${escapeHtml(item.family.replaceAll("_", " "))}</b><span>${escapeHtml(item.interpretability)}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderInstruments() {
  const rows = state.data.instruments;
  resultCount.textContent = `${rows.length} reusable elicitation instruments`;
  content.innerHTML = rows.map((item) => `<article class="index-row entity-row">
    <div class="resource-title"><a href="${escapeHtml(item.primary_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a><small>${escapeHtml(item.aliases.join(" · "))}</small></div>
    <div class="evidence-cell"><span class="tag">${escapeHtml(item.instrument_type.replaceAll("_", " "))}</span><span>${escapeHtml(item.status)}</span></div>
    <div class="provenance-cell"><b>${item.axiology_ids.length} linked spaces</b><span>${escapeHtml(item.axiology_ids.join(" · "))}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderSources() {
  const occurrenceCounts = new Map();
  state.data.links.forEach((link) => sourcesFor(link).forEach((id) => occurrenceCounts.set(id, (occurrenceCounts.get(id) || 0) + 1)));
  const rows = [...state.data.sources].sort((a, b) => (occurrenceCounts.get(b.id) || 0) - (occurrenceCounts.get(a.id) || 0));
  resultCount.textContent = `${rows.length} provenance sources`;
  content.innerHTML = rows.map((item) => `<article class="index-row entity-row source-row">
    <div class="resource-title"><a href="${escapeHtml(item.repo || "https://github.com/ikanam-ai/ai-values-atlas")}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a><small>${escapeHtml(item.id)}</small></div>
    <div class="evidence-cell"><strong>${(occurrenceCounts.get(item.id) || 0).toLocaleString()}</strong><span>unique links</span></div>
    <div class="provenance-cell"><b>${escapeHtml(item.scope_tier_guess)}</b><span>${escapeHtml(item.license_status)}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function render() {
  viewTitle.textContent = viewNames[state.view];
  const discovery = ["publications", "datasets", "tools"].includes(state.view);
  filters.hidden = !discovery;
  indexHead.hidden = false;
  if (discovery) renderDiscovery();
  else if (state.view === "axiologies") renderAxiologies();
  else if (state.view === "instruments") renderInstruments();
  else renderSources();
}

function populate() {
  const sourceIds = [...new Set(state.data.links.flatMap(sourcesFor))].sort();
  document.querySelector("#sourceFilter").insertAdjacentHTML("beforeend", sourceIds.map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`).join(""));
  document.querySelector("#metricPublications").textContent = state.data.links.filter((item) => item.link_type_guess === "publication").length.toLocaleString();
  document.querySelector("#metricResources").textContent = state.data.links.length.toLocaleString();
  document.querySelector("#metricSources").textContent = sourceIds.length;
  document.querySelector("#generatedAt").textContent = `Source snapshot ${new Date(state.data.generated_at).toLocaleDateString()}`;
}

document.querySelectorAll(".browse-tab").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".browse-tab").forEach((item) => item.classList.toggle("active", item === button));
  state.view = button.dataset.view;
  state.visible = 80;
  render();
}));
document.querySelector("#search").addEventListener("input", (event) => { state.search = event.target.value; state.visible = 80; render(); });
document.querySelector("#scopeFilter").addEventListener("change", (event) => { state.scope = event.target.value; state.visible = 80; render(); });
document.querySelector("#sourceFilter").addEventListener("change", (event) => { state.source = event.target.value; state.visible = 80; render(); });
loadMore.addEventListener("click", () => { state.visible += 80; render(); });

fetch("data.json", { cache: "no-store" })
  .then((response) => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then((data) => { state.data = data; populate(); render(); })
  .catch((error) => { resultCount.textContent = "Index unavailable"; content.innerHTML = `<div class="empty">${escapeHtml(error.message)}</div>`; });
