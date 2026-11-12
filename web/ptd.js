const $ = selector => document.querySelector(selector);
const panes = [...document.querySelectorAll('.pane')];
const kindLabels = {
  fact: 'Fait ou demande rapportée',
  hypothesis: 'Hypothèse',
  proposal: 'Proposition',
  requirement: 'Exigence',
  criterion: 'Critère de vérification',
  question: 'Question à confirmer',
  decision: 'Décision',
  obstacle: 'Obstacle',
  action: 'Action ou engagement',
  review: 'Bilan de séance',
  note: 'Note'
};
const scopeLabels = { individual: 'Privé', collective: 'Équipe' };
const state = {
  pane: 'home',
  requestedPane: window.location.pathname === '/coach' ? 'coach' : 'home',
  session: null,
  profiles: [],
  config: null,
  threads: [],
  thread: null,
  project: null,
  editing: null,
  editorPane: 'project',
  methods: [],
  methodReturn: null,
  busy: false,
  answering: false,
  keys: new Map(),
  createKeySignature: null,
  identityVersion: 0
};

function element(tag, content, className) {
  const node = document.createElement(tag);
  if (content != null) node.textContent = content;
  if (className) node.className = className;
  return node;
}

function button(label, action, className = 'secondary') {
  const node = element('button', label, className);
  node.type = 'button';
  node.addEventListener('click', action);
  return node;
}

function addOptions(select, options) {
  for (const [value, label] of options) {
    const option = element('option', label);
    option.value = value;
    select.append(option);
  }
}

function error(message = '') {
  $('#app-error').textContent = message;
  $('#app-error').hidden = !message;
}

function announce(message) {
  $('#app-status').textContent = message;
}

function isStudent() {
  return state.session?.user.role === 'student';
}

function syncControls() {
  $('#sign-in').disabled = state.busy || !state.profiles.length;
  $('#sign-out').disabled = state.busy;
  $('#new-thread').disabled = state.busy || !state.config;
  $('#refresh-thread').disabled = state.busy || !state.config;
  $('#send-message').disabled = state.busy || !state.config?.configured || !state.thread || state.thread.pending;
  $('#chat-message').readOnly = state.answering;
  $('#chat-waiting').hidden = !state.answering;
  $('#save-item').disabled = state.busy;
  $('#add-item').disabled = state.busy || !state.project;
  $('#refresh-project').disabled = state.busy;
  $('#refresh-checkpoint').disabled = state.busy;
  $('#next-week').disabled = state.busy || !state.project || state.project.project.current_week >= state.project.project.max_week;
}

async function perform(task, { answering = false } = {}) {
  if (state.busy) return;
  state.busy = true;
  state.answering = answering;
  error();
  syncControls();
  try {
    await task();
  } catch (failure) {
    error(failure.message || 'Une erreur est survenue.');
  } finally {
    state.busy = false;
    state.answering = false;
    syncControls();
  }
}

async function api(path, method = 'GET', payload) {
  const headers = {};
  const session = state.session;
  const identityVersion = state.identityVersion;
  if (session?.csrf) headers['X-CSRF-Token'] = session.csrf;
  let signature;
  if (method !== 'GET') {
    if (payload !== undefined) headers['Content-Type'] = 'application/json';
    if (path.startsWith('/api/coach/') || (path === '/api/project' && method === 'POST')) {
      signature = path + JSON.stringify(payload);
      if (!state.keys.has(signature)) state.keys.set(signature, crypto.randomUUID());
      headers['Idempotency-Key'] = state.keys.get(signature);
      if (path === '/api/project' && method === 'POST') state.createKeySignature = signature;
    }
  }
  let response;
  let data;
  try {
    response = await fetch(path, { method, headers, credentials: 'same-origin', body: payload === undefined ? undefined : JSON.stringify(payload) });
    data = await response.json().catch(() => null);
  } catch {
    throw new Error(signature ? 'Connexion locale interrompue. Réessayez sans modifier la demande pour éviter un doublon.' : 'Connexion locale interrompue. Actualisez pour vérifier l’état.');
  }
  const ended = 'La session fictive a pris fin. Choisissez un profil pour reprendre.';
  if (identityVersion !== state.identityVersion || (session && state.session !== session)) throw new Error(ended);
  if (session && (response.status === 401 || data?.error?.code === 'csrf_forbidden')) {
    clearSession();
    showPane('home', { focus: false });
    $('#profile').focus();
    if (path === '/api/demo-session' && method === 'DELETE' && response.status === 401) return null;
    throw new Error(ended);
  }
  if (!data) {
    throw new Error(signature ? 'Le résultat est incertain. Réessayez sans modifier la demande pour éviter un doublon.' : 'Le serveur local n’a pas renvoyé de résultat exploitable.');
  }
  if (!response.ok) {
    if (signature && response.status < 500 && data.error?.code !== 'call_pending') state.keys.delete(signature);
    const failure = new Error(data.error?.message || 'Cette action n’a pas abouti.');
    failure.status = response.status;
    failure.code = data.error?.code;
    throw failure;
  }
  if (signature) state.keys.delete(signature);
  if (signature && state.createKeySignature === signature) state.createKeySignature = null;
  return data;
}

function showPane(name, { focus = true } = {}) {
  if (['coach', 'project', 'checkpoint'].includes(name) && !state.session) {
    state.requestedPane = name;
    showPane('home', { focus: false });
    announce('Choisissez un profil fictif pour ouvrir cet espace.');
    $('#profile').focus();
    return;
  }
  if (['coach', 'checkpoint'].includes(name) && !isStudent()) name = 'project';
  state.pane = name;
  for (const pane of panes) pane.hidden = pane.id !== 'pane-' + name;
  for (const item of document.querySelectorAll('.navigation [data-pane]')) {
    if (item.dataset.pane === name) item.setAttribute('aria-current', 'page');
    else item.removeAttribute('aria-current');
  }
  if (focus) $('#' + name + '-title').focus();
}

function dateLabel(value, time = false) {
  if (!value) return '';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  const options = time ? { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' } : { day: 'numeric', month: 'short', year: 'numeric' };
  return date.toLocaleString('fr-FR', options);
}

function scopeDescription() {
  $('#scope-description').textContent = $('#thread-scope').value === 'collective'
    ? 'Les étudiants de votre équipe fictive peuvent lire ce fil.'
    : 'Votre profil fictif est le seul étudiant autorisé à lire ce fil.';
}

function renderThreadList() {
  const list = $('#thread-list');
  if (!state.threads.length) {
    list.replaceChildren(element('p', 'Aucun fil pour ce profil.', 'small muted'));
    return;
  }
  list.replaceChildren(...state.threads.map(thread => {
    const entry = button(scopeLabels[thread.scope] + ' · ' + dateLabel(thread.created_at, true), () => perform(async () => {
      state.thread = await api('/api/coach/conversations/' + encodeURIComponent(thread.id));
      $('#chat-message').value = '';
      renderCoach();
    }));
    if (thread.id === state.thread?.id) entry.setAttribute('aria-current', 'true');
    return entry;
  }));
}

async function refreshThreads() {
  state.threads = await api('/api/coach/conversations');
  renderThreadList();
}

function appendSafeEmphasis(target, value) {
  for (const part of value.split(/(\*\*[^*]+\*\*)/g)) {
    target.append(part.startsWith('**') && part.endsWith('**')
      ? element('strong', part.slice(2, -2)) : document.createTextNode(part));
  }
}

function renderCoach() {
  const thread = state.thread;
  const collective = thread?.scope === 'collective';
  $('#thread-visibility').textContent = thread ? (collective ? 'Fil de l’équipe' : 'Fil privé') : 'Aucun fil ouvert';
  const config = state.config;
  $('#provider').textContent = config ? (config.provider === 'mistral' ? 'Mistral' : 'Simulation hors réseau')
    + ' · ' + config.model + ' · ' + config.prompt_version
    + (config.configured ? '' : ' · Clé locale absente') : '';
  $('#chat-examples').hidden = Boolean(thread?.messages.length);
  const invocations = thread?.invocations.filter(invocation => invocation.status === 'succeeded') || [];
  let replyIndex = 0;
  const articles = (thread?.messages || []).map(message => {
    const assistant = message.role === 'assistant';
    const article = element('article', null, 'message ' + message.role);
    const author = state.profiles.find(profile => profile.id === message.author_id);
    const authorLabel = assistant ? 'PTD Coach' : (collective && author ? author.label : 'Vous');
    const paragraph = element('p');
    appendSafeEmphasis(paragraph, message.content);
    article.append(element('p', authorLabel, 'speaker'), paragraph);
    if (!assistant) return article;

    const invocation = invocations[replyIndex++];
    const details = element('div', null, 'details flow');
    if (invocation) {
      const tokens = invocation.usage?.total_tokens;
      const usage = tokens == null ? 'Consommation non mesurée' : tokens.toLocaleString('fr-FR') + ' tokens';
      details.append(element('p', usage + (invocation.latency_ms == null ? '' : ' · ' + invocation.latency_ms + ' ms')
        + (invocation.finish_reason === 'length' ? ' · Réponse incomplète' : ''), 'small muted'));
      for (const id of invocation.resource_ids || []) {
        const method = state.methods.find(item => item.id === id);
        if (!method) continue;
        const resource = button('Ouvrir la fiche « ' + method.nom + ' »', () => {
          openMethod(method, { pane: 'coach', trigger: resource });
        });
        details.append(element('p', 'Fiche fournie au coach pour cette réponse. ' + method.pertinence, 'small muted'), resource);
      }
    }
    if (state.project) {
      details.append(button(collective ? 'Reprendre comme brouillon d’équipe' : 'Reprendre comme brouillon privé', () => {
        if (state.busy) return;
        if (message.content.length > $('#item-text').maxLength) {
          error('Sélectionnez un extrait de la réponse et ajoutez-le à un brouillon du projet.');
          return;
        }
        openEditor({
          scope: thread.scope,
          kind: 'proposal',
          origin: 'ai',
          text: message.content,
          source: 'Réponse du coach du ' + dateLabel(message.created_at),
          fixedScope: true
        });
      }));
    }
    article.append(details);
    return article;
  });
  $('#chat-log').replaceChildren(...articles);
  $('#chat-log').scrollTop = $('#chat-log').scrollHeight;
  const total = thread?.usage?.known_tokens?.total_tokens;
  $('#chat-usage').textContent = thread
    ? (thread.pending ? 'Appel en cours ou résultat incertain. Actualisez avant un nouvel envoi.'
      : 'Consommation connue du fil ' + (total ?? 0).toLocaleString('fr-FR') + ' tokens.')
    : 'Créez un fil privé ou d’équipe pour envoyer un message.';
  renderThreadList();
  syncControls();
}

const normalize = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
const synonyms = [
  ['change', 'changement', 'modifier', 'avis'],
  ['client', 'commanditaire'],
  ['retard', 'delai', 'planning'],
  ['equipe', 'participation', 'coordination'],
  ['cahier', 'charges', 'specification', 'exigence'],
  ['cause', 'pourquoi', 'hypothese'],
  ['besoin', 'demande', 'usage']
];

function renderMethods() {
  const search = normalize($('#method-search').value.trim());
  const category = $('#method-category').value;
  const competence = $('#method-competence').value;
  const terms = search.split(/[^a-z0-9]+/).filter(term => term.length > 2);
  const matching = state.methods.filter(method => {
    const content = normalize([method.nom, method.resume, method.situations, ...method.mots_cles].join(' '));
    return (!category || category === method.categorie)
      && (!competence || method.competences.includes(competence))
      && (!terms.length || terms.some(term => content.includes(term) ||
        synonyms.some(group => group.some(word => term.includes(word)) && group.some(word => content.includes(word)))));
  });
  $('#method-count').textContent = matching.length + (matching.length === 1 ? ' méthode' : ' méthodes');
  $('#method-list').replaceChildren(...matching.map(method => {
    const article = element('article', null, 'card method-card');
    const open = button('Consulter la fiche', () => openMethod(method, { pane: 'library', trigger: open }));
    open.setAttribute('aria-label', 'Consulter la fiche ' + method.nom);
    article.append(element('p', method.categorie + ' · ' + method.competences.join(', '), 'small muted'),
      element('h2', method.nom), element('p', method.statut, 'tag draft'), element('p', method.resume), open);
    return article;
  }));
}

function closeMethod() {
  const origin = state.methodReturn;
  $('#method-detail').hidden = true;
  $('#method-detail').replaceChildren();
  $('#method-search').hidden = false;
  $('#library-search').hidden = false;
  $('#method-list').hidden = false;
  state.methodReturn = null;
  if (origin?.pane === 'coach') showPane('coach', { focus: !origin.trigger?.isConnected });
  if (origin?.trigger?.isConnected) origin.trigger.focus();
  else if (origin?.pane !== 'coach') $('#library-title').focus();
}

function openMethod(method, origin) {
  state.methodReturn = origin || state.methodReturn;
  showPane('library', { focus: false });
  $('#library-search').hidden = true;
  $('#method-list').hidden = true;
  const detail = $('#method-detail');
  const back = button(state.methodReturn?.pane === 'coach' ? 'Retour à la conversation' : 'Retour aux méthodes', closeMethod);
  detail.replaceChildren(back, element('h2', method.nom), element('p', method.statut, 'tag draft'));
  const fields = [
    ['En 30 secondes', 'resume'], ['Quand l’utiliser', 'situations'], ['Pourquoi', 'pertinence'],
    ['Étapes', 'etapes'], ['Exemple fictif', 'exemple'], ['Modèle vierge', 'modele'],
    ['Erreurs fréquentes', 'erreurs'], ['Limites', 'limites'], ['À savoir refaire', 'apprentissage'],
    ['Repères pour les tuteurs', 'tuteur']
  ];
  for (const [title, key] of fields) {
    const section = element('section');
    section.append(element('h3', title), element('p', method[key]));
    detail.append(section);
  }
  const source = element('section');
  source.append(element('h3', 'Source consultée'),
    element('p', [method.source.organisation, method.source.titre, method.source.consultation].join(' · ')),
    element('p', method.source.portee));
  try {
    const url = new URL(method.source.url);
    if (url.protocol === 'https:') {
      const link = element('a', 'Consulter la source');
      link.href = url.href;
      link.rel = 'noopener noreferrer';
      source.append(link);
    }
  } catch { /* Une source indisponible reste affichée sous forme de référence textuelle. */ }
  detail.append(source);
  const related = method.liens.map(id => state.methods.find(item => item.id === id)).filter(Boolean);
  if (related.length) {
    const section = element('section');
    const links = element('div', null, 'actions');
    for (const item of related) links.append(button(item.nom, () => openMethod(item)));
    section.append(element('h3', 'Méthodes complémentaires'), links);
    detail.append(section);
  }
  detail.hidden = false;
  detail.focus();
}

async function loadLibrary() {
  state.methods = await api('/api/library');
  const categories = [...new Set(state.methods.map(method => method.categorie))];
  const competences = [...new Set(state.methods.flatMap(method => method.competences))].sort();
  addOptions($('#method-category'), categories.map(value => [value, value]));
  addOptions($('#method-competence'), competences.map(value => [value, value]));
  renderMethods();
}

function closeEditor() {
  if (state.createKeySignature) state.keys.delete(state.createKeySignature);
  state.createKeySignature = null;
  state.editing = null;
  state.editorPane = 'project';
  $('#project-form').reset();
  $('#project-form').hidden = true;
  $('#item-scope').disabled = false;
  $('#item-origin').disabled = false;
}

function openEditor(draft = {}, pane = 'project') {
  if (!state.project || !isStudent()) return;
  const editing = Boolean(draft.id);
  const scope = draft.scope || $('#project-filter').value;
  state.editing = editing ? { id: draft.id, version: draft.version } : null;
  state.editorPane = pane;
  $('#editor-title').textContent = editing ? 'Modifier l’élément' : 'Ajouter un élément';
  $('#item-scope').value = scope;
  $('#item-scope').disabled = editing || Boolean(draft.fixedScope);
  $('#item-kind').value = draft.kind || (scope === 'individual' ? 'note' : 'fact');
  $('#item-origin').value = draft.origin || 'human';
  $('#item-origin').disabled = editing;
  $('#item-text').value = draft.text || '';
  $('#item-source').value = draft.source || '';
  $('#editor-help').textContent = editing
    ? 'La modification repasse l’élément en brouillon et retire son partage éventuel.'
    : 'L’élément sera enregistré en brouillon. La confirmation et le partage sont des actions distinctes.';
  const form = $('#project-form');
  $('#' + pane + '-editor-slot').append(form);
  form.hidden = false;
  showPane(pane, { focus: false });
  $('#editor-title').focus();
}

function renderItem(item, editPane) {
  const card = element('article', null, 'card');
  card.dataset.itemId = item.id;
  const metadata = element('div', null, 'item-meta');
  metadata.append(element('span', kindLabels[item.kind] || item.kind, 'tag neutral'),
    element('span', item.confirmed ? 'Confirmé par un humain' : 'Brouillon', 'tag' + (item.confirmed ? '' : ' draft')),
    element('span', item.origin === 'ai' ? 'Proposition du coach' : 'Formulation humaine', 'tag neutral'));
  if (item.shared) metadata.append(element('span', 'Partagé au tuteur', 'tag'));
  card.append(metadata, element('p', item.text, 'item-content'));
  const updated = dateLabel(item.updated_at || item.created_at);
  const confirmer = state.profiles.find(profile => profile.id === item.confirmed_by);
  const confirmation = item.confirmed_at
    ? ' · Confirmé le ' + dateLabel(item.confirmed_at) + (confirmer ? ' par ' + confirmer.label : '') : '';
  card.append(element('p', 'Semaine ' + item.week + ' · Source ' + item.source
    + (updated ? ' · Mis à jour le ' + updated : '') + confirmation, 'small muted'));
  if (!editPane) return card;

  const actions = element('div', null, 'actions');
  function addAction(action, label, handler, className) {
    const control = button(label, handler, className);
    control.dataset.itemAction = action;
    control.dataset.itemId = item.id;
    actions.append(control);
    return control;
  }
  addAction('update', 'Modifier', () => {
    if (!state.busy) openEditor(item, editPane);
  });
  if (!item.confirmed) addAction('confirm', 'Confirmer', () => mutateItem(item, 'confirm'));
  if (item.scope === 'collective' && item.confirmed) {
    if (item.shared) addAction('revoke', 'Retirer le partage', () => mutateItem(item, 'revoke'));
    else addAction('share', 'Partager au tuteur', () => mutateItem(item, 'share'));
  }
  const remove = addAction('delete', 'Supprimer', () => {
    if (state.busy) return;
    if (remove.dataset.confirming === 'true') {
      mutateItem(item, 'delete');
      return;
    }
    remove.dataset.confirming = 'true';
    remove.textContent = 'Confirmer la suppression';
    const cancel = button('Annuler la suppression', () => {
      remove.dataset.confirming = 'false';
      remove.textContent = 'Supprimer';
      cancel.remove();
      remove.focus();
    });
    actions.append(cancel);
    remove.focus();
  }, 'secondary danger');
  card.append(actions);
  return card;
}

function renderProject() {
  const data = state.project;
  const summary = $('#project-summary');
  const items = $('#project-items');
  const checkpoint = $('#checkpoint-items');
  if (!data) {
    summary.replaceChildren(element('p', 'Aucun projet fictif disponible pour ce profil.'));
    items.replaceChildren();
    checkpoint.replaceChildren();
    $('#checkpoint-week').textContent = '';
    $('#checkpoint-description').textContent = '';
    return;
  }
  const project = data.project;
  summary.replaceChildren(element('p', 'Semaine ' + project.current_week + ' · ' + project.slot, 'small muted'),
    element('h2', project.title), element('p', 'Commanditaire fictif · ' + project.sponsor),
    element('p', project.brief));
  $('#home-week').textContent = 'Semaine ' + project.current_week + ' sur ' + project.max_week;
  $('#home-project-title').textContent = project.title;
  $('#home-project-slot').textContent = project.slot;
  $('#home-project').hidden = false;

  const visible = isStudent()
    ? data.items.filter(item => item.scope === $('#project-filter').value)
    : data.items.filter(item => item.scope === 'collective' && item.confirmed && item.shared);
  items.replaceChildren(...visible.map(item => renderItem(item, isStudent() ? 'project' : null)));
  if (!visible.length) items.append(element('p', isStudent()
    ? 'Aucun élément dans cet espace.' : 'L’équipe n’a partagé aucun élément confirmé.', 'card muted'));
  if (!isStudent()) {
    checkpoint.replaceChildren();
    return;
  }
  $('#checkpoint-week').textContent = 'Semaine ' + project.current_week + (project.week_title ? ' · ' + project.week_title : '');
  $('#checkpoint-description').textContent = project.week_description || project.slot;

  const previous = element('section', null, 'card');
  previous.append(element('h3', 'Éléments confirmés la semaine précédente'));
  const previousItems = data.items.filter(item =>
    item.scope === 'collective' && item.confirmed && item.week === project.current_week - 1);
  const current = element('section', null, 'card');
  current.append(element('h3', 'Bilan, obstacles et actions de cette semaine'));
  const currentItems = data.items.filter(item =>
    item.scope === 'collective' && item.week === project.current_week && ['review', 'obstacle', 'action'].includes(item.kind));
  for (const [container, list, empty, editPane] of [
    [previous, previousItems, 'Aucun élément confirmé pour la séance précédente.'],
    [current, currentItems, 'Vous pouvez préparer un bilan ou proposer une action.', 'checkpoint']
  ]) {
    const group = element('div', null, 'item-list');
    if (list.length) group.append(...list.map(item => renderItem(item, editPane)));
    else group.append(element('p', empty, 'muted'));
    container.append(group);
  }
  checkpoint.replaceChildren(previous, current);
  syncControls();
}

async function refreshProject() {
  state.project = await api('/api/project');
  renderProject();
}

function mutateItem(item, action) {
  perform(async () => {
    state.project = await api('/api/project/items/' + encodeURIComponent(item.id) + '/' + action, 'POST', { version: item.version });
    if (state.editing?.id === item.id) closeEditor();
    renderProject();
    if (['project', 'checkpoint'].includes(state.pane)) $('#' + state.pane + '-title').focus();
    announce({
      confirm: 'Élément confirmé.',
      share: 'Élément partagé au tuteur.',
      revoke: 'Partage retiré.',
      delete: 'Élément supprimé.'
    }[action]);
  });
}

function renderSession() {
  const profile = state.session?.user;
  const tutor = profile?.role === 'tutor';
  $('#identity').hidden = !profile;
  $('#identity').textContent = profile?.label || '';
  $('#sign-out').hidden = !profile;
  $('#sign-in-form').hidden = Boolean(profile);
  $('#home-project').hidden = !profile || !state.project;
  for (const node of document.querySelectorAll('[data-student]')) node.hidden = tutor;
  $('#project-title').textContent = tutor ? 'Éléments partagés avec le tuteur' : 'Notre projet';
  $('#project-nav').textContent = tutor ? 'Éléments partagés' : 'Notre projet';
  $('#project-card-title').textContent = tutor ? 'Préparer le prochain échange' : 'Notre projet';
  $('#project-card-description').textContent = tutor
    ? 'Consultez les informations collectives que l’équipe vous a partagées.'
    : 'Formuler le besoin, préciser le cahier des charges et confirmer les décisions.';
  $('#project-intro').textContent = tutor
    ? 'Les éléments ci-dessous ont été confirmés et partagés par l’équipe.'
    : 'Consignez le besoin, les exigences, les questions et les décisions. Choisissez ce qui reste privé.';
  $('#project-controls').hidden = !isStudent();
}

function clearSession() {
  state.identityVersion++;
  state.session = null;
  state.config = null;
  state.threads = [];
  state.thread = null;
  state.project = null;
  state.keys.clear();
  state.createKeySignature = null;
  $('#chat-message').value = '';
  $('#demo-consent').checked = false;
  $('#thread-scope').value = 'individual';
  $('#project-filter').value = 'collective';
  $('#home-week').textContent = '';
  $('#home-project-title').textContent = '';
  $('#home-project-slot').textContent = '';
  $('#method-detail').replaceChildren();
  $('#method-detail').hidden = true;
  $('#library-search').hidden = false;
  $('#method-list').hidden = false;
  $('#method-search').value = '';
  state.methodReturn = null;
  closeEditor();
  renderSession();
  renderCoach();
  renderProject();
}

async function loadSession() {
  renderSession();
  const operations = [refreshProject()];
  if (isStudent()) {
    operations.push((async () => {
      state.config = await api('/api/coach/config');
      await refreshThreads();
      renderCoach();
    })());
  }
  const results = await Promise.allSettled(operations);
  const failure = results.find(result => result.status === 'rejected');
  if (failure) error(failure.reason.message);
}

document.querySelectorAll('[data-pane]').forEach(control => control.addEventListener('click', () => showPane(control.dataset.pane)));
document.querySelectorAll('[data-new-kind]').forEach(control => control.addEventListener('click', () => {
  if (!state.busy) openEditor({ scope: 'collective', kind: control.dataset.newKind, fixedScope: true }, 'checkpoint');
}));
document.querySelectorAll('[data-example]').forEach(control => control.addEventListener('click', () => {
  if (state.answering) return;
  $('#chat-message').value = control.dataset.example;
  $('#chat-message').focus();
}));

$('#sign-in-form').addEventListener('submit', event => {
  event.preventDefault();
  perform(async () => {
    if (!$('#demo-consent').checked) throw new Error('Confirmez l’utilisation de données fictives.');
    state.session = await api('/api/demo-session', 'POST', { user_id: $('#profile').value });
    state.identityVersion++;
    await loadSession();
    showPane(state.requestedPane);
    state.requestedPane = 'home';
  });
});
$('#sign-out').addEventListener('click', () => perform(async () => {
  try { await api('/api/demo-session', 'DELETE'); }
  finally {
    clearSession();
    showPane('home', { focus: false });
    $('#profile').focus();
  }
}));
$('#thread-scope').addEventListener('change', scopeDescription);
$('#new-thread').addEventListener('click', () => perform(async () => {
  state.thread = await api('/api/coach/conversations', 'POST', {
    scope: $('#thread-scope').value, synthetic_confirmed: true, coach_version: state.config.default_coach_version
  });
  renderCoach();
  await refreshThreads();
  $('#chat-message').focus();
}));
$('#refresh-thread').addEventListener('click', () => perform(async () => {
  if (state.thread) state.thread = await api('/api/coach/conversations/' + encodeURIComponent(state.thread.id));
  await refreshThreads();
  renderCoach();
  announce('Conversation actualisée.');
}));
$('#chat-form').addEventListener('submit', event => {
  event.preventDefault();
  if (!state.thread || !state.config?.configured || state.thread.pending) return;
  const message = $('#chat-message').value.trim();
  if (!message) return;
  perform(async () => {
    state.thread = await api('/api/coach/conversations/' + encodeURIComponent(state.thread.id) + '/messages', 'POST', { message, version: state.thread.version });
    $('#chat-message').value = '';
    renderCoach();
    if (state.pane === 'coach') $('#chat-message').focus();
  }, { answering: true });
});

for (const id of ['method-search', 'method-category', 'method-competence']) $('#' + id).addEventListener('input', renderMethods);
$('#project-filter').addEventListener('change', renderProject);
for (const id of ['refresh-project', 'refresh-checkpoint']) $('#' + id).addEventListener('click', () => perform(async () => {
  await refreshProject();
  announce('Projet actualisé.');
}));
$('#add-item').addEventListener('click', () => {
  if (!state.busy) openEditor();
});
$('#cancel-item').addEventListener('click', () => {
  if (state.busy) return;
  const origin = state.editorPane;
  closeEditor();
  (origin === 'project' ? $('#add-item') : $('#checkpoint-title')).focus();
});
$('#project-form').addEventListener('submit', event => {
  event.preventDefault();
  perform(async () => {
    const payload = { kind: $('#item-kind').value, text: $('#item-text').value.trim(), source: $('#item-source').value.trim() };
    if (!payload.text || !payload.source) throw new Error('Renseignez le texte et sa source.');
    const scope = $('#item-scope').value;
    const origin = state.editorPane;
    if (state.editing) {
      payload.version = state.editing.version;
      state.project = await api('/api/project/items/' + encodeURIComponent(state.editing.id) + '/update', 'POST', payload);
    } else {
      payload.scope = scope;
      payload.origin = $('#item-origin').value;
      state.project = await api('/api/project', 'POST', payload);
    }
    if (origin === 'project') $('#project-filter').value = scope;
    closeEditor();
    renderProject();
    if (state.pane === origin) (origin === 'project' ? $('#add-item') : $('#checkpoint-title')).focus();
    announce('Brouillon enregistré.');
  });
});
$('#next-week').addEventListener('click', () => perform(async () => {
  if (!state.project) return;
  state.project = await api('/api/project/next-week', 'POST', { version: state.project.project.version });
  renderProject();
  announce('Séance de démonstration avancée.');
}));

addOptions($('#item-kind'), Object.entries(kindLabels));
scopeDescription();
renderSession();
syncControls();
perform(async () => {
  const results = await Promise.allSettled([loadLibrary(), (async () => {
    const profiles = await api('/api/demo-users');
    state.profiles = profiles.filter(profile => ['student', 'tutor'].includes(profile.role));
    $('#profile').replaceChildren(element('option', 'Choisir un profil'));
    $('#profile').firstElementChild.value = '';
    addOptions($('#profile'), state.profiles.map(profile => [profile.id, profile.label]));
    try {
      const session = await api('/api/me');
      if (state.profiles.some(profile => profile.id === session.user.id)) {
        state.session = session;
        await loadSession();
        showPane(state.requestedPane, { focus: false });
        state.requestedPane = 'home';
      }
    } catch (failure) {
      if (failure.status !== 401) throw failure;
    }
  })()]);
  const failure = results.find(result => result.status === 'rejected');
  if (failure) error(failure.reason.message);
  renderCoach();
});
