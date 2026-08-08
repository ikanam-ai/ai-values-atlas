const state = {
  data: null,
  domain: 'measurement-profiling',
  search: '',
  contribution: '',
  artifact: '',
  year: null,
  limit: 30,
};

const $ = (selector) => document.querySelector(selector);
const esc = (value = '') => String(value).replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const pretty = (value) => value.replaceAll('-', ' ').replaceAll('_', ' ').replace(/\b\w/g, c => c.toUpperCase());

fetch('data.json')
  .then(response => {
    if (!response.ok) throw new Error(`Could not load atlas data (${response.status})`);
    return response.json();
  })
  .then(data => {
    state.data = data;
    initialize();
    render();
  })
  .catch(error => {
    $('#work-list').innerHTML = `<li class="empty">${esc(error.message)}</li>`;
  });

function initialize() {
  const {stats, domains, works, standalone_resources: resources} = state.data;
  const statItems = [
    ['Works', stats.research_works],
    ['Domains', stats.domains],
    ['Source links', stats.source_links.toLocaleString()],
    ['Resource links', stats.work_resource_relations.toLocaleString()],
    ['Independent', stats.standalone_resources],
  ];
  $('#stats').innerHTML = statItems.map(([label, value]) => `<div class="stat"><dt>${label}</dt><dd>${value}</dd></div>`).join('');
  $('#all-count').textContent = stats.research_works;

  $('#domain-map').innerHTML = domains.map(domain => `
    <div class="domain-map-row" data-domain="${domain.id}" role="button" tabindex="0">
      <span class="icon">${domain.icon}</span><strong>${esc(domain.name)}</strong><p>${esc(domain.question)}</p><b>${domain.work_count}</b>
    </div>`).join('');
  $('#domain-nav').innerHTML = domains.map(domain => `
    <button class="domain-nav" data-domain="${domain.id}" type="button">
      <span class="nav-name"><i>${domain.icon}</i>${esc(domain.name)}</span><b>${domain.work_count}</b>
    </button>`).join('');

  const types = [...new Set(works.flatMap(work => work.contribution_types))].sort();
  $('#type-filter').insertAdjacentHTML('beforeend', types.map(type => `<option value="${type}">${pretty(type)}</option>`).join(''));
  const kinds = [...new Set(resources.map(resource => resource.kind))].sort();
  $('#resource-kind').insertAdjacentHTML('beforeend', kinds.map(kind => `<option value="${kind}">${pretty(kind)}</option>`).join(''));

  document.addEventListener('click', event => {
    const domainButton = event.target.closest('[data-domain]');
    if (domainButton) selectDomain(domainButton.dataset.domain);
  });
  document.addEventListener('keydown', event => {
    const row = event.target.closest('.domain-map-row');
    if (row && (event.key === 'Enter' || event.key === ' ')) selectDomain(row.dataset.domain);
  });
  $('#search').addEventListener('input', event => { state.search = event.target.value.trim().toLowerCase(); resetPage(); });
  $('#type-filter').addEventListener('change', event => { state.contribution = event.target.value; resetPage(); });
  $('#artifact-filter').addEventListener('change', event => { state.artifact = event.target.value; resetPage(); });
  $('#clear-filters').addEventListener('click', () => {
    state.search = ''; state.contribution = ''; state.artifact = ''; state.year = null;
    $('#search').value = ''; $('#type-filter').value = ''; $('#artifact-filter').value = '';
    resetPage();
  });
  $('#clear-year').addEventListener('click', () => { state.year = null; resetPage(); });
  $('#load-more').addEventListener('click', () => { state.limit += 30; renderWorks(); });
  $('#resource-search').addEventListener('input', renderResources);
  $('#resource-kind').addEventListener('change', renderResources);
  renderResources();
}

function selectDomain(domain) {
  state.domain = domain;
  state.year = null;
  state.limit = 30;
  render();
  $('#explorer').scrollIntoView({behavior: 'smooth', block: 'start'});
}

function resetPage() {
  state.limit = 30;
  render();
}

function domainInfo() {
  return state.data.domains.find(domain => domain.id === state.domain);
}

function ranking(work) {
  return work.rankings.find(row => row.domain_id === state.domain);
}

function domainWorks() {
  let works = state.data.works.filter(work => work.scope !== 'out_of_scope');
  if (state.domain !== 'all') works = works.filter(work => work.domains.includes(state.domain));
  if (state.search) works = works.filter(work => [work.title, work.venue, work.description, ...work.contribution_types].join(' ').toLowerCase().includes(state.search));
  if (state.contribution) works = works.filter(work => work.contribution_types.includes(state.contribution));
  if (state.artifact) works = works.filter(work => work.links.some(link => link.label === state.artifact));
  if (state.year) works = works.filter(work => work.year === state.year);
  if (state.domain === 'all') return works.sort((a,b) => (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title));
  return works.sort((a,b) => ranking(a).rank - ranking(b).rank || a.title.localeCompare(b.title));
}

function render() {
  const info = domainInfo();
  $('#domain-title').textContent = info ? `${info.icon} ${info.name}` : 'All research works';
  $('#domain-question').textContent = info ? info.question : 'Browse the complete corpus by year; select a domain for a scientifically meaningful ranking.';
  document.querySelectorAll('.domain-nav').forEach(button => button.classList.toggle('active', button.dataset.domain === state.domain));
  renderTimeline();
  renderWorks();
}

function renderTimeline() {
  const baseWorks = state.data.works.filter(work => work.scope !== 'out_of_scope' && (state.domain === 'all' || work.domains.includes(state.domain)));
  const counts = new Map();
  baseWorks.forEach(work => { if (work.year) counts.set(work.year, (counts.get(work.year) || 0) + 1); });
  const years = [...counts.keys()].sort((a,b) => a-b);
  const max = Math.max(...counts.values(), 1);
  $('#timeline').innerHTML = years.map(year => `<button class="year-bar ${state.year === year ? 'active' : ''}" data-year="${year} · ${counts.get(year)} works" title="${year}: ${counts.get(year)} works" style="--h:${Math.max(5, counts.get(year)/max*66)}px" aria-label="Filter to ${year}"></button>`).join('');
  $('#timeline').querySelectorAll('.year-bar').forEach((button, index) => button.addEventListener('click', () => { state.year = years[index]; resetPage(); }));
  $('#clear-year').hidden = !state.year;
}

function renderWorks() {
  const works = domainWorks();
  const visible = works.slice(0, state.limit);
  const filters = [state.year, state.contribution && pretty(state.contribution), state.artifact && `with ${state.artifact}`].filter(Boolean);
  $('#result-count').textContent = `${works.length} work${works.length === 1 ? '' : 's'}`;
  $('#active-filter').textContent = filters.join(' · ');
  $('#work-list').innerHTML = visible.length ? visible.map(renderWork).join('') : '<li class="empty">No works match these filters.</li>';
  $('#load-more').hidden = visible.length >= works.length;
}

function renderWork(work) {
  const row = state.domain === 'all' ? null : ranking(work);
  const primary = work.links.find(link => link.label === 'paper') || work.links[0];
  const links = work.links.map(link => `<a class="artifact-link" href="${esc(link.url)}" target="_blank" rel="noopener">${esc(link.label)}</a>`).join('');
  const tags = work.contribution_types.map(type => `<span class="tag">${esc(pretty(type))}</span>`).join('');
  const scorePanel = row ? `
    <div class="score-panel">
      <div class="domain-score">${row.domain_score.toFixed(1)} <small>/ 100</small></div>
      ${scoreBar('Contribution', row.scientific_contribution, 'contribution')}
      ${scoreBar('Relevance', row.field_relevance, 'relevance')}
      ${scoreBar('Influence', row.influence, 'influence')}
    </div>` : '';
  const release = work.release ? renderRelease(work.release) : '';
  return `<li class="work-row">
    <div class="rank">${row ? row.rank : (work.year || '—')}<small>${row ? 'rank' : ''}</small></div>
    <article>
      <h3 class="work-title">${work.publication_status === 'published' ? '⭐' : '📄'} <a href="${esc(primary?.url || '#')}" target="_blank" rel="noopener">${esc(work.title)}</a></h3>
      <p class="work-meta"><span>${esc(work.venue || 'Venue not listed')}</span><span>${work.year || 'n.d.'}</span></p>
      <p class="work-description">${esc(work.description)}</p>
      <div class="tags">${tags}</div>
      <div class="artifact-links">${links}</div>
      ${release}
    </article>
    ${scorePanel}
  </li>`;
}

function scoreBar(label, value, className) {
  const shown = value == null ? '—' : Math.round(value);
  const width = value == null ? 0 : value;
  return `<div class="score-row ${className}"><label><span>${label}</span><b>${shown}</b></label><div class="track"><i style="--w:${width}%"></i></div></div>`;
}

function renderRelease(release) {
  const available = release.available.map(pretty).join(', ') || 'No computational release expected';
  const licenses = Object.entries(release.licenses).filter(([, value]) => !['not_applicable','not_released'].includes(value)).map(([kind, value]) => `${kind}: ${value}`).join(' · ');
  const limitations = release.limitations.length ? `<p><strong>Practical limits:</strong> ${esc(release.limitations.join(' · '))}</p>` : '';
  return `<details class="release-note"><summary>Release contents</summary><p><strong>Available:</strong> ${esc(available)}</p>${licenses ? `<p><strong>Licenses:</strong> ${esc(licenses)}</p>` : ''}${limitations}</details>`;
}

function renderResources() {
  if (!state.data) return;
  const query = $('#resource-search').value.trim().toLowerCase();
  const kind = $('#resource-kind').value;
  const resources = state.data.standalone_resources.filter(row => (!kind || row.kind === kind) && (!query || row.title.toLowerCase().includes(query)));
  $('#resource-list').innerHTML = resources.map(row => `<div class="resource-item"><a href="${esc(row.url)}" target="_blank" rel="noopener">${esc(row.title)}</a><span>${esc(row.roles.join(' · '))}</span></div>`).join('') || '<p class="empty">No resources match these filters.</p>';
}
