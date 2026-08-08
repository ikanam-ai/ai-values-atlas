const state = { data: null, view: "publications", search: "", scope: "", source: "", year: "", importance: "", researchClass: "", visible: 80 };

const content = document.querySelector("#content");
const resultCount = document.querySelector("#resultCount");
const loadMore = document.querySelector("#loadMore");
const filters = document.querySelector("#filters");
const indexHead = document.querySelector("#indexHead");
const viewTitle = document.querySelector("#viewTitle");
const timelinePanel = document.querySelector("#timelinePanel");
const yearChart = document.querySelector("#yearChart");
const timelineSummary = document.querySelector("#timelineSummary");

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
  if (link.link_type_guess === "publication" && link.title) return link.title;
  const generic = new Set(["paper", "pdf", "code", "github", "dataset", "data", "model", "project", "website", "link"]);
  const clean = (value) => value.replace(/^\d+\.\s+/, "").replace(/,\s*20\d{2}(?:\.\d{1,2})?,?\s*$/, "").trim();
  if (link.context_title && !generic.has(link.context_title.toLowerCase())) return clean(link.context_title);
  if (link.label && !generic.has(link.label.toLowerCase())) return clean(link.label);
  try { return new URL(link.url).pathname.split("/").filter(Boolean).slice(-2).join(" / ") || link.url; }
  catch { return link.url; }
}

function sourcesFor(link) {
  return [...new Set(link.occurrences.map((item) => item.catalog_id))];
}

function matchesFilters(link, { ignoreYear = false } = {}) {
  const query = state.search.toLowerCase();
  const haystack = [titleFor(link), link.label, link.url, link.research_class, ...sourcesFor(link), ...link.occurrences.map((item) => item.section)].join(" ").toLowerCase();
  const publicationFilters = state.view === "publications" && link.link_type_guess === "publication";
  return (!query || haystack.includes(query)) &&
    (!state.scope || link.scope_tier_guess === state.scope) &&
    (!state.source || sourcesFor(link).includes(state.source)) &&
    (!publicationFilters || !state.importance || link.featured) &&
    (!publicationFilters || !state.researchClass || link.research_class_id === state.researchClass) &&
    (!publicationFilters || ignoreYear || !state.year || String(link.publication_year || "unknown") === state.year);
}

function discoveryRows() {
  const datasetTerms = /dataset|benchmark|item bank|corpus|survey|questionnaire/i;
  let rows = state.data.links.filter((link) => {
    if (state.view === "publications") return link.link_type_guess === "publication";
    if (state.view === "datasets") return link.link_type_guess === "dataset" || datasetTerms.test(titleFor(link));
    return ["model", "repository", "project"].includes(link.link_type_guess);
  });
  return rows.filter((link) => matchesFilters(link)).sort((left, right) => {
    const weak = (link) => /^(?:\d{4}\.\d{4,5}|\d{4}\.[\w.-]+|collection|leaderboard|hf datasets|hg & ci)$/i.test(titleFor(link)) || /^https?:/i.test(titleFor(link));
    if (state.view === "publications") {
      return Number(right.featured) - Number(left.featured) ||
        (right.publication_year || 0) - (left.publication_year || 0) ||
        Number(weak(left)) - Number(weak(right)) || titleFor(left).localeCompare(titleFor(right));
    }
    return Number(weak(left)) - Number(weak(right)) || titleFor(left).localeCompare(titleFor(right));
  });
}

function renderTimeline() {
  const publications = state.data.links.filter((link) => link.link_type_guess === "publication" && matchesFilters(link, { ignoreYear: true }));
  const counts = new Map();
  publications.forEach((link) => {
    const key = String(link.publication_year || "unknown");
    counts.set(key, (counts.get(key) || 0) + 1);
  });
  const keys = [...counts.keys()].sort((a, b) => {
    if (a === "unknown") return 1;
    if (b === "unknown") return -1;
    return Number(a) - Number(b);
  });
  const peak = Math.max(1, ...counts.values());
  yearChart.innerHTML = keys.map((key) => {
    const count = counts.get(key);
    const height = Math.max(8, Math.round((count / peak) * 118));
    const label = key === "unknown" ? "?" : key;
    const selected = state.year === key;
    return `<button class="year-column${selected ? " selected" : ""}" data-year="${escapeHtml(key)}" aria-pressed="${selected}">
      <span class="year-count">${count}</span><span class="year-bar" style="height:${height}px"></span><span class="year-label">${label}</span>
    </button>`;
  }).join("");
  const featured = publications.filter((link) => link.featured).length;
  timelineSummary.textContent = `${publications.length.toLocaleString()} works · ${featured.toLocaleString()} featured`;
  yearChart.querySelectorAll(".year-column").forEach((button) => button.addEventListener("click", () => {
    state.year = state.year === button.dataset.year ? "" : button.dataset.year;
    document.querySelector("#yearFilter").value = state.year;
    state.visible = 80;
    render();
  }));
}

function renderDiscovery() {
  const rows = discoveryRows();
  resultCount.textContent = `${rows.length.toLocaleString()} matching resources`;
  const visible = rows.slice(0, state.visible);
  content.innerHTML = visible.length ? visible.map((link) => {
    const sources = sourcesFor(link);
    const section = link.occurrences[0]?.section?.split(" / ").slice(-2).join(" / ") || "catalog entry";
    const year = link.publication_year || "—";
    const evidence = link.link_type_guess === "publication"
      ? `${link.featured ? '<span class="featured-tag">◆ featured</span>' : ""}<strong>${year}</strong><span title="${escapeHtml(link.research_class || "")}">${escapeHtml(link.research_class || "unclassified")}</span>`
      : `<span class="tag">${escapeHtml(link.link_type_guess)}</span><span>${escapeHtml(link.scope_tier_guess)}</span>`;
    const publicationEntry = link.link_type_guess === "publication";
    const artifactLabels = { repository: "code", dataset: "dataset", model: "model", project: "project", other: "link" };
    const artifactLinks = publicationEntry
      ? [{ type: "publication", url: link.url }, ...(link.related_artifacts || [])]
        .map((item) => `<a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer">${artifactLabels[item.type] || "paper"}</a>`).join("")
      : "";
    const resource = publicationEntry
      ? `<div class="resource-title publication-title">
          ${link.subdomain ? `<span class="subdomain">(${escapeHtml(link.subdomain)})</span>` : ""}
          <strong><span class="title-status" title="${escapeHtml(link.publication_status?.label || "")}">${escapeHtml(link.publication_status?.icon || "📄")}</span> ${escapeHtml(titleFor(link))}</strong>
          <small>${escapeHtml([link.venue, link.date].filter(Boolean).join(" · "))}</small>
          <span class="artifact-links">${artifactLinks}</span>
        </div>`
      : `<div class="resource-title"><a href="${escapeHtml(link.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(titleFor(link))}</a><small>${escapeHtml(link.url)}</small></div>`;
    return `<article class="index-row${link.featured ? " featured-row" : ""}">
      ${resource}
      <div class="evidence-cell">${evidence}</div>
      <div class="provenance-cell"><b>${escapeHtml(sources[0] || "")}</b><span>${escapeHtml(link.scope_tier_guess)}</span><span title="${escapeHtml(section)}">${escapeHtml(section)}</span></div>
    </article>`;
  }).join("") : '<div class="empty">No resources match the current filters.</div>';
  loadMore.hidden = state.visible >= rows.length;
}

function renderAxiologies() {
  const rows = state.data.axiologies;
  resultCount.textContent = `${rows.length} mapped value representations`;
  content.innerHTML = rows.map((item) => `<article class="index-row entity-row axiology-row">
    <div class="resource-title"><a href="${escapeHtml(item.primary_sources[0])}" target="_blank" rel="noopener noreferrer">${escapeHtml(item.name)}</a><small>${escapeHtml(item.origin_domain.replaceAll("_", " "))}</small>
      <details class="entity-details"><summary>Show dimensions and structure</summary><p>${escapeHtml(item.dimensions?.length ? item.dimensions.join(" · ") : "No fixed named dimensions")}</p><p>${escapeHtml(item.structure_notes || "")}</p></details>
    </div>
    <div class="evidence-cell"><span class="tag">${escapeHtml(item.representation_type.replaceAll("_", " "))}</span><span>${item.dimension_count ?? "open / variable"} dimensions</span></div>
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
  timelinePanel.hidden = state.view !== "publications";
  document.querySelectorAll(".publication-only").forEach((item) => { item.hidden = state.view !== "publications"; });
  indexHead.innerHTML = state.view === "publications" ? "<span>Subdomain · title · venue · date · links</span><span>Year & class</span><span>Provenance</span>" : "<span>Resource</span><span>Evidence</span><span>Provenance</span>";
  indexHead.hidden = false;
  if (discovery) {
    if (state.view === "publications") renderTimeline();
    renderDiscovery();
  }
  else if (state.view === "axiologies") renderAxiologies();
  else if (state.view === "instruments") renderInstruments();
  else renderSources();
}

function populate() {
  const sourceIds = [...new Set(state.data.links.flatMap(sourcesFor))].sort();
  document.querySelector("#sourceFilter").insertAdjacentHTML("beforeend", sourceIds.map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`).join(""));
  const classes = [...new Map(state.data.links.filter((item) => item.research_class_id).map((item) => [item.research_class_id, item.research_class])).entries()].sort((a, b) => a[1].localeCompare(b[1]));
  document.querySelector("#classFilter").insertAdjacentHTML("beforeend", classes.map(([id, label]) => `<option value="${escapeHtml(id)}">${escapeHtml(label)}</option>`).join(""));
  const yearCounts = new Map();
  state.data.links.filter((item) => item.link_type_guess === "publication").forEach((item) => {
    const key = String(item.publication_year || "unknown");
    yearCounts.set(key, (yearCounts.get(key) || 0) + 1);
  });
  const years = [...yearCounts.keys()].sort((a, b) => a === "unknown" ? 1 : b === "unknown" ? -1 : Number(b) - Number(a));
  document.querySelector("#yearFilter").insertAdjacentHTML("beforeend", years.map((year) => `<option value="${escapeHtml(year)}">${year === "unknown" ? "Unknown year" : year} (${yearCounts.get(year)})</option>`).join(""));
  document.querySelector("#metricPublications").textContent = state.data.links.filter((item) => item.link_type_guess === "publication").length.toLocaleString();
  document.querySelector("#metricFeatured").textContent = state.data.links.filter((item) => item.link_type_guess === "publication" && item.featured).length.toLocaleString();
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
document.querySelector("#importanceFilter").addEventListener("change", (event) => { state.importance = event.target.value; state.visible = 80; render(); });
document.querySelector("#classFilter").addEventListener("change", (event) => { state.researchClass = event.target.value; state.visible = 80; render(); });
document.querySelector("#yearFilter").addEventListener("change", (event) => { state.year = event.target.value; state.visible = 80; render(); });
loadMore.addEventListener("click", () => { state.visible += 80; render(); });

fetch("data.json", { cache: "no-store" })
  .then((response) => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then((data) => { state.data = data; populate(); render(); })
  .catch((error) => { resultCount.textContent = "Index unavailable"; content.innerHTML = `<div class="empty">${escapeHtml(error.message)}</div>`; });
