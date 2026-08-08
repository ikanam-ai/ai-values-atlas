const state = {
  data: null,
  view: "links",
  search: "",
  type: "",
  scope: "",
  source: "",
  visible: 60,
};

const content = document.querySelector("#content");
const resultCount = document.querySelector("#resultCount");
const loadMore = document.querySelector("#loadMore");
const filters = document.querySelector("#linkFilters");
const statusText = document.querySelector("#statusKey span");

function escapeHtml(value = "") {
  return value.replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
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

function renderLinks() {
  const query = state.search.toLowerCase();
  const rows = state.data.links.filter((link) => {
    const haystack = [titleFor(link), link.label, link.url, ...sourcesFor(link), ...link.occurrences.map((item) => item.section)].join(" ").toLowerCase();
    return (!query || haystack.includes(query)) &&
      (!state.type || link.link_type_guess === state.type) &&
      (!state.scope || link.scope_tier_guess === state.scope) &&
      (!state.source || sourcesFor(link).includes(state.source));
  });
  resultCount.textContent = `${rows.length.toLocaleString()} discovered resources`;
  const visible = rows.slice(0, state.visible);
  content.innerHTML = visible.length ? visible.map((link) => {
    const sources = sourcesFor(link);
    return `<article class="record">
      <div class="record-top"><span class="pill">${escapeHtml(link.link_type_guess)}</span><span class="scope">${escapeHtml(link.scope_tier_guess)}</span></div>
      <h3><a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(titleFor(link))}</a></h3>
      <div class="record-meta"><span>${sources.length} source${sources.length === 1 ? "" : "s"}</span><span title="${escapeHtml(sources.join(", "))}">${escapeHtml(sources[0] || "")}</span></div>
    </article>`;
  }).join("") : '<div class="empty">No resources match these filters.</div>';
  loadMore.hidden = state.visible >= rows.length;
}

function renderAxiologies() {
  const rows = state.data.axiologies;
  resultCount.textContent = `${rows.length} curated value representations`;
  content.innerHTML = rows.map((item) => `<article class="record">
    <div class="record-top"><span class="pill">${escapeHtml(item.representation_type.replaceAll("_", " "))}</span><span class="scope">${item.dimension_count ?? "open"} dimensions</span></div>
    <h3><a href="${escapeHtml(item.primary_sources[0])}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a></h3>
    <div class="record-meta"><span>${escapeHtml(item.family.replaceAll("_", " "))}</span><span>${escapeHtml(item.interpretability)}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderWorks() {
  const rows = state.data.works;
  resultCount.textContent = `${rows.length} method-aware publication records`;
  content.innerHTML = rows.map((item) => `<article class="record">
    <div class="record-top"><span class="pill">${escapeHtml(item.work_types[0].replaceAll("_", " "))}</span><span class="scope">${item.year} · ${escapeHtml(item.curation.status)}</span></div>
    <h3><a href="${escapeHtml(item.primary_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.title)}</a></h3>
    <p class="record-note">${escapeHtml(item.summary || "Method record in curation.")}</p>
    <div class="record-meta"><span>${escapeHtml(item.venue || item.publication_status)}</span><span>${escapeHtml(item.research_roles[0].replaceAll("_", " "))}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderInstruments() {
  const rows = state.data.instruments;
  resultCount.textContent = `${rows.length} curated instruments`;
  content.innerHTML = rows.map((item) => `<article class="record">
    <div class="record-top"><span class="pill">${escapeHtml(item.instrument_type.replaceAll("_", " "))}</span><span class="scope">${escapeHtml(item.status)}</span></div>
    <h3><a href="${escapeHtml(item.primary_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a></h3>
    <div class="record-meta"><span>${item.axiology_ids.length} axiology link${item.axiology_ids.length === 1 ? "" : "s"}</span><span>${escapeHtml(item.aliases.join(", "))}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderModels() {
  const rows = state.data.models;
  resultCount.textContent = `${rows.length} curated value-related models`;
  content.innerHTML = rows.map((item) => `<article class="record">
    <div class="record-top"><span class="pill">${escapeHtml(item.model_kind.replaceAll("_", " "))}</span><span class="scope">${escapeHtml(item.curation_status)}</span></div>
    <h3><a href="${escapeHtml(item.primary_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a></h3>
    <p class="record-note">${escapeHtml(item.notes)}</p>
    <div class="record-meta"><span>${escapeHtml(item.developer)}</span><span>${item.axiology_ids.length} axiology link${item.axiology_ids.length === 1 ? "" : "s"}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function renderDatasets() {
  const rows = state.data.datasets;
  resultCount.textContent = `${rows.length} curated datasets and item banks`;
  content.innerHTML = rows.map((item) => `<article class="record">
    <div class="record-top"><span class="pill">${escapeHtml(item.dataset_kinds[0].replaceAll("_", " "))}</span><span class="scope">${escapeHtml(item.curation_status)}</span></div>
    <h3><a href="${escapeHtml(item.primary_url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a></h3>
    <p class="record-note">${escapeHtml(item.notes)}</p>
    <div class="record-meta"><span>${escapeHtml(item.annotation)} annotation</span><span>${item.axiology_ids.length} axiology link${item.axiology_ids.length === 1 ? "" : "s"}</span></div>
  </article>`).join("");
  loadMore.hidden = true;
}

function render() {
  filters.hidden = state.view !== "links";
  content.className = "catalog-grid";
  statusText.textContent = state.view === "links"
    ? "Discovery records are not yet method-verified"
    : "Curated records disclose their review status";
  if (state.view === "links") renderLinks();
  else if (state.view === "works") renderWorks();
  else if (state.view === "axiologies") renderAxiologies();
  else if (state.view === "instruments") renderInstruments();
  else if (state.view === "models") renderModels();
  else renderDatasets();
}

function populateFilters() {
  const types = [...new Set(state.data.links.map((item) => item.link_type_guess))].sort();
  const sources = [...new Set(state.data.links.flatMap(sourcesFor))].sort();
  document.querySelector("#typeFilter").insertAdjacentHTML("beforeend", types.map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`).join(""));
  document.querySelector("#sourceFilter").insertAdjacentHTML("beforeend", sources.map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`).join(""));
  document.querySelector("#metricLinks").textContent = state.data.counts.links.toLocaleString();
  document.querySelector("#metricWorks").textContent = state.data.counts.works;
  document.querySelector("#metricStudies").textContent = state.data.counts.studies;
  document.querySelector("#metricAxiologies").textContent = state.data.counts.axiologies;
  document.querySelector("#metricModels").textContent = state.data.counts.models;
  document.querySelector("#metricDatasets").textContent = state.data.counts.datasets;
  document.querySelector("#generatedAt").textContent = `Built ${new Date(state.data.generated_at).toLocaleDateString()}`;
}

document.querySelectorAll(".tab").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll(".tab").forEach((item) => item.classList.toggle("active", item === button));
  state.view = button.dataset.view;
  render();
}));

document.querySelector("#search").addEventListener("input", (event) => { state.search = event.target.value; state.visible = 60; render(); });
document.querySelector("#typeFilter").addEventListener("change", (event) => { state.type = event.target.value; state.visible = 60; render(); });
document.querySelector("#scopeFilter").addEventListener("change", (event) => { state.scope = event.target.value; state.visible = 60; render(); });
document.querySelector("#sourceFilter").addEventListener("change", (event) => { state.source = event.target.value; state.visible = 60; render(); });
loadMore.addEventListener("click", () => { state.visible += 60; render(); });

fetch("data.json", { cache: "no-store" })
  .then((response) => {
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  })
  .then((data) => { state.data = data; populateFilters(); render(); })
  .catch((error) => {
    resultCount.textContent = "Catalog could not be loaded";
    content.innerHTML = `<div class="empty">${escapeHtml(error.message)}</div>`;
  });
