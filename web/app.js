const $ = (selector) => document.querySelector(selector);
const state = { session: null, users: [], cases: [], cycles: [], cycle: null, shares: [], view: 'parcours', busy: false };
const fieldLabels = { answer: 'Réponse à l’exercice', action: 'Action à expérimenter', when: 'Occasion prévue', observation: 'Observation recherchée', facts: 'Faits rapportés', interpretation: 'Interprétation', lesson: 'Leçon à retenir', private_summary: 'Bilan personnel' };
const stages = ['Objectif', 'Comprendre', 'S’entraîner', 'Expérimenter', 'Débriefer'];
const stageIndex = { OBJECTIVE_SELECTED: 0, LEARNING: 1, PRACTICING: 2, EXPERIMENT_PLANNED: 3, AWAITING_EXPERIENCE: 3, REFLECTING: 4, REVIEWED: 4, CLOSED: 4 };
const keys = new Map();

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key.startsWith('on')) node.addEventListener(key.slice(2).toLowerCase(), value);
    else if (key === 'class') node.className = value;
    else if (value !== false && value != null) node.setAttribute(key, value === true ? '' : value);
  }
  for (const child of children.flat(Infinity)) if (child != null) node.append(child instanceof Node ? child : document.createTextNode(String(child)));
  return node;
}
function button(label, handler, secondary = false, small = false) {
  return el('button', { type: 'button', class: `button${secondary ? ' secondary' : ''}${small ? ' small' : ''}`, onClick: () => run(handler) }, label);
}
function notice(message = '') { $('#notice').textContent = message; $('#notice').hidden = !message; }
async function run(task) {
  if (state.busy) return;
  state.busy = true; notice();
  document.querySelectorAll('button').forEach(b => { b.disabled = true; });
  try { await task(); }
  catch (error) { notice(error.message || 'La connexion locale a été interrompue. Réessayez avec le même contenu.'); }
  finally { state.busy = false; document.querySelectorAll('button').forEach(b => { b.disabled = false; }); }
}
async function api(path, method = 'GET', body, command = false) {
  const headers = {};
  if (body !== undefined) headers['Content-Type'] = 'application/json';
  if (state.session && method !== 'GET') headers['X-CSRF-Token'] = state.session.csrf;
  const signature = method + path + JSON.stringify(body);
  if (command) { if (!keys.has(signature)) keys.set(signature, crypto.randomUUID()); headers['Idempotency-Key'] = keys.get(signature); }
  const response = await fetch(path, { method, headers, credentials: 'same-origin', body: body === undefined ? undefined : JSON.stringify(body) });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error?.message || 'Cette action n’a pas abouti.');
  if (command) keys.delete(signature);
  return result;
}
function heading(eyebrow, title, intro) { return el('div', { class: 'page-heading' }, el('p', { class: 'eyebrow' }, eyebrow), el('h1', { class: 'page-title' }, title), el('p', { class: 'intro' }, intro)); }
function privacy() { return el('div', { class: 'privacy' }, el('span', { class: 'privacy-icon', 'aria-hidden': 'true' }, '◇'), el('span', {}, 'Votre dialogue et votre bilan restent privés. Vous choisissez séparément ce que vous partagez.')); }
function card(...children) { return el('section', { class: 'card' }, ...children); }
function field(name, label, placeholder, options = {}) {
  const control = el(options.single ? 'input' : 'textarea', { name, id: `field-${name}`, required: true, minlength: 10, maxlength: options.max || 4000, ...(options.single ? { type: 'text' } : { rows: options.rows || 4 }), placeholder });
  if (options.value) control.value = options.value;
  return el('label', { class: 'field' }, el('span', {}, label), control, options.help ? el('small', {}, options.help) : null);
}
function form(fields, label, submit, arrow = true) {
  const node = el('form', {}, fields, el('div', { class: 'actions' }, el('button', { class: 'button', type: 'submit' }, label, arrow ? el('span', { 'aria-hidden': 'true' }, '→') : null)));
  node.addEventListener('submit', (event) => { event.preventDefault(); if (node.reportValidity()) run(() => submit(Object.fromEntries(new FormData(node)))); });
  return node;
}
function context() {
  const selected = state.cases.find(c => c.id === state.cycle?.case_id);
  return el('aside', { class: 'stack context-stack', 'aria-label': 'Repères du parcours' },
    card(el('span', { class: 'a2-code' }, 'A2'), el('p', { class: 'mini-label' }, 'COMPÉTENCE TRAVAILLÉE'), el('p', { class: 'goal-title' }, 'Structurer et planifier un projet'), el('span', { class: 'badge neutral' }, 'Référentiel candidat'), el('hr', { class: 'divider' }), el('p', { class: 'fine-print' }, 'Ce parcours est un entraînement. Il n’attribue ni note ni niveau de compétence.')),
    card(el('p', { class: 'mini-label' }, 'VOTRE TERRAIN D’ESSAI'), el('h3', {}, selected?.title || 'Un projet fictif, un geste concret'), el('p', {}, selected?.focus || 'Entraînez-vous sur une situation de projet, puis choisissez une action à expérimenter.'), privacy())
  );
}
function navigation() {
  const student = state.session?.user.role === 'student';
  const entries = student || !state.session ? [['parcours', '↗', 'Mon parcours'], ['preuves', '▤', 'Mes preuves'], ['aide', '○', 'Les repères']] : [['preuves', '▤', 'Preuves reçues'], ['aide', '○', 'Les repères']];
  $('#navigation').replaceChildren(...entries.map(([view, icon, label]) => el('button', { type: 'button', class: `nav-button${state.view === view ? ' active' : ''}`, 'aria-current': state.view === view ? 'page' : null, onClick: () => run(async () => { state.view = view; if (view === 'preuves' && state.session && ['student', 'tutor'].includes(state.session.user.role)) state.shares = await api('/api/shares'); render(); }) }, el('span', { class: 'nav-icon', 'aria-hidden': 'true' }, icon), label)));
  $('#page-label').textContent = !state.session ? 'Bienvenue' : (entries.find(e => e[0] === state.view)?.[2] || 'Mon espace');
  const identity = $('#identity'); identity.replaceChildren();
  if (state.session) {
    const user = state.session.user;
    identity.append(el('span', { class: 'avatar', 'aria-hidden': 'true' }, user.role === 'student' ? user.label.slice(-1) : 'D'), el('span', { class: 'identity-label' }, user.label, el('small', {}, 'Compte fictif')), button('Changer de compte', logout, true, true));
  }
}
async function logout() {
  await api('/api/demo-session', 'DELETE');
  Object.assign(state, { session: null, cycle: null, cycles: [], shares: [], view: 'parcours' }); keys.clear(); render();
}
async function loadWorkspace() {
  state.cases = (await api('/api/cases')).cases;
  const role = state.session.user.role;
  state.cycles = role === 'student' ? await api('/api/cycles') : [];
  state.cycle = state.cycles[0] || null;
  state.shares = ['student', 'tutor'].includes(role) ? await api('/api/shares') : [];
  state.view = role === 'student' ? 'parcours' : 'preuves';
}
function welcome() {
  const select = el('select', { id: 'demo-user', name: 'user_id' }, state.users.map(u => el('option', { value: u.id }, u.label)));
  return [heading('PTD COACH · PREMIÈRE EXPLORATION', 'Un projet d’équipe. Un parcours à vous.', 'Développez vos pratiques de gestion de projet, une expérience à la fois.'),
    el('div', { class: 'workspace-grid' }, el('section', { class: 'card welcome-card' }, el('div', { class: 'hero-symbol', 'aria-hidden': 'true' }, '↗'), el('span', { class: 'badge' }, 'Premier parcours · A2'), el('h2', {}, 'Anticiper les dépendances, puis passer à l’action.'), el('p', {}, 'Comprenez ce qui relie les tâches d’un projet. Testez votre raisonnement, préparez une action et prenez du recul sur votre expérience.'),
      el('ol', { class: 'welcome-list' }, ['Une situation fictive pour vous entraîner', 'Une action précise à expérimenter', 'Un bilan personnel et une preuve choisie'].map((s, i) => el('li', {}, el('span', {}, i + 1), s))),
      form([el('label', { class: 'field', for: 'demo-user' }, el('span', {}, 'Choisir un compte de démonstration'), select), el('p', { class: 'fine-print' }, 'Tous les comptes sont fictifs et librement sélectionnables dans cette démo. Utilisez uniquement des contenus inventés.')], 'Explorer cet espace', async values => { state.session = await api('/api/demo-session', 'POST', values); await loadWorkspace(); render(); })), context())];
}
function objective() {
  return card(el('div', { class: 'card-top' }, el('span', { class: 'badge' }, 'Votre premier objectif'), el('span', { class: 'count' }, 'A2 · Parcours individuel')), el('h2', {}, 'Anticiper les dépendances dans un projet'), el('p', {}, 'Choisissez un cas pour commencer. Vous pourrez ensuite préparer votre propre action dans le cadre de la simulation.'),
    form([el('div', { class: 'case-options', role: 'radiogroup', 'aria-label': 'Cas d’entraînement' }, state.cases.map((c, i) => el('label', { class: 'case-option' }, el('input', { type: 'radio', name: 'case_id', value: c.id, checked: i === 0, required: true }), el('span', {}, c.title, el('small', {}, c.focus)))))], 'Choisir cet objectif', async values => { state.cycle = await api('/api/cycles', 'POST', values, true); state.cycles.unshift(state.cycle); render(); }), privacy());
}
async function act(action, fields = {}) {
  state.cycle = await api(`/api/cycles/${state.cycle.id}/actions`, 'POST', { action, version: state.cycle.version, fields }, true);
  render();
  $('#step-title')?.focus();
}
function coachBlock(message) { return el('div', { class: 'coach' }, el('div', { class: 'coach-label' }, el('span', { 'aria-hidden': 'true' }, '✦'), 'LE COACH · SIMULATION'), el('p', {}, message)); }
function history() {
  const messages = state.cycle.messages;
  if (!messages.length) return null;
  return el('details', { class: 'history' }, el('summary', {}, `Votre historique privé · ${messages.length} messages`), messages.map(m => {
    let content = m.content;
    if (m.role === 'student') {
      const fields = JSON.parse(content);
      content = Object.entries(fields).filter(([k]) => k !== 'experience_reported').map(([k, v]) => `${fieldLabels[k] || k} : ${v}`).join('\n\n');
    }
    return el('div', { class: 'message' }, el('strong', {}, m.role === 'coach' ? 'COACH SIMULÉ' : 'VOTRE RÉPONSE'), el('p', {}, content));
  }));
}
function cycleCard() {
  const cycle = state.cycle, data = cycle.data;
  const index = stageIndex[cycle.state];
  const names = {
    OBJECTIVE_SELECTED: ['Votre objectif est posé.', 'Commencez par quelques repères pour lire les dépendances.'],
    LEARNING: ['Comprendre avant de planifier.', 'Une validation peut changer l’ordre des tâches. Rendons-la visible.'],
    PRACTICING: ['À vous de proposer un enchaînement.', 'Appuyez votre réponse sur la situation, puis confrontez-la aux questions du coach.'],
    EXPERIMENT_PLANNED: ['Votre action est prête.', 'Prenez le temps de l’expérimenter dans la simulation avant de faire le bilan.'],
    AWAITING_EXPERIENCE: ['Un temps pour expérimenter.', 'Revenez ici lorsque vous aurez une expérience à raconter. Aucune réalisation n’est déduite de la date.'],
    REFLECTING: ['Gardez une trace qui vous aide.', 'À partir de votre récit et du retour du coach, rédigez le bilan que vous souhaitez conserver.'],
    REVIEWED: ['Un bilan pour votre prochaine action.', 'Votre bilan est sauvegardé. Vous pouvez garder ce parcours privé ou sélectionner une preuve à partager.'],
    CLOSED: ['Ce parcours est clôturé.', 'Votre travail reste consultable. La clôture ne valide pas un niveau de compétence.'],
  };
  const [title, intro] = names[cycle.state];
  const node = card(el('div', { class: 'card-top' }, el('span', { class: 'badge' }, cycle.state === 'CLOSED' ? 'Parcours clôturé' : `Étape ${index + 1} sur 5`), el('span', { class: 'mini-label' }, 'ESPACE INDIVIDUEL')), el('h2', { id: 'step-title', tabindex: '-1' }, title), el('p', {}, intro));
  const latestCoach = cycle.messages.filter(m => m.role === 'coach').at(-1);
  if (latestCoach && !['OBJECTIVE_SELECTED', 'CLOSED'].includes(cycle.state)) node.append(coachBlock(latestCoach.content));
  switch (cycle.state) {
    case 'OBJECTIVE_SELECTED': node.append(el('div', { class: 'actions' }, button('Comprendre les dépendances →', () => act('learn')))); break;
    case 'LEARNING': node.append(el('div', { class: 'actions' }, button('M’entraîner sur le cas →', () => act('practice')))); break;
    case 'PRACTICING':
      node.append(form([field('answer', 'Votre proposition', 'Distinguez les tâches qui peuvent avancer, celles qui attendent une validation et le prochain jalon.', { value: data.answer })], data.answer ? 'Réessayer avec une autre réponse' : 'Examiner ma proposition', fields => act('answer', fields), false));
      if (data.answer) node.append(el('hr', { class: 'divider' }), el('h3', {}, 'Préparer une action à expérimenter'), form([
        field('action', 'Quelle action concrète allez-vous tester ?', 'Par exemple : rendre explicites les validations attendues dans un planning fictif.'),
        field('when', 'À quelle occasion ?', 'Décrivez une occasion précise dans votre simulation.', { single: true }),
        field('observation', 'Qu’allez-vous observer ?', 'Quel fait vous aidera à comprendre l’effet de votre action ?')
      ], 'Enregistrer mon plan d’action', fields => act('plan', fields)));
      break;
    case 'EXPERIMENT_PLANNED':
      node.append(el('div', { class: 'summary-block' }, `Action : ${data.action}\n\nOccasion : ${data.when}\n\nObservation recherchée : ${data.observation}`), el('div', { class: 'actions' }, button('Passer au temps d’expérimentation →', () => act('start_experience')))); break;
    case 'AWAITING_EXPERIENCE':
      node.append(form([
        field('facts', 'Quels faits rapportez-vous ?', 'Décrivez seulement ce qui s’est passé dans votre expérience simulée.'),
        field('interpretation', 'Comment interprétez-vous ces faits ?', 'Distinguez ce que vous observez et ce que vous supposez.'),
        field('lesson', 'Quelle leçon en tirez-vous ?', 'Que pourriez-vous conserver ou ajuster la prochaine fois ?'),
        el('label', { class: 'check-label' }, el('input', { type: 'checkbox', name: 'experience_reported', required: true }), 'Je confirme rapporter une expérience simulée, sans prétendre qu’elle a été observée par le coach.')
      ], 'Débriefer cette expérience', fields => act('report', { ...fields, experience_reported: fields.experience_reported === 'on' })));
      break;
    case 'REFLECTING':
      node.append(form([field('private_summary', 'Votre bilan personnel', 'Ce que je retiens, ce qui reste incertain et ce que je testerai ensuite…', { rows: 6 })], 'Sauvegarder mon bilan privé', fields => act('review', fields)));
      break;
    case 'REVIEWED': case 'CLOSED':
      node.append(el('div', { class: 'summary-block' }, data.private_summary), el('div', { class: 'actions' }, button('Sélectionner une preuve à partager', async () => { state.shares = await api('/api/shares'); state.view = 'preuves'; render(); }, true)));
      if (cycle.state === 'REVIEWED') node.append(el('div', { class: 'actions' }, button('Clôturer ce parcours', () => act('close'), true, true)));
      if (cycle.state === 'CLOSED') node.append(el('div', { class: 'actions' }, button('M’entraîner sur un autre cas', async () => { state.cycle = null; render(); }, true)));
  }
  node.append(privacy());
  return node;
}
function parcours() {
  const progress = state.cycle ? el('ol', { class: 'stepper', 'aria-label': 'Étapes du parcours' }, stages.map((label, i) => el('li', { class: i === stageIndex[state.cycle.state] ? 'current' : (i < stageIndex[state.cycle.state] ? 'done' : ''), 'aria-current': i === stageIndex[state.cycle.state] ? 'step' : null }, el('div', { class: 'step-line' }), el('span', { class: 'step-number' }, String(i + 1).padStart(2, '0')), label))) : null;
  const selectCycle = state.cycles.length > 1 ? el('label', { class: 'field' }, el('span', {}, 'Reprendre un parcours'), el('select', { onChange: event => run(async () => { state.cycle = await api(`/api/cycles/${event.target.value}`); render(); }) }, state.cycles.map((c, i) => el('option', { value: c.id, selected: c.id === state.cycle?.id }, `${state.cases.find(x => x.id === c.case_id)?.title || 'A2'} · ${i + 1}`)))) : null;
  return [heading('MON PARCOURS · A2', 'Un prochain pas, à votre rythme.', 'Comprendre une méthode, la mettre à l’épreuve, puis apprendre de ce que vous avez fait.'), selectCycle, progress,
    el('div', { class: 'workspace-grid' }, el('div', {}, state.cycle ? cycleCard() : objective(), state.cycle ? history() : null,
      state.cycle ? el('div', { class: 'actions' }, el('a', { href: `/api/cycles/${state.cycle.id}/export`, class: 'button secondary small', download: 'ptd-a2-prive.json' }, 'Exporter mon parcours privé'), button('Recharger le parcours', async () => { state.cycle = await api(`/api/cycles/${state.cycle.id}`); render(); }, true, true)) : null), context())];
}
function proofList(owner) {
  if (!state.shares.length) return card(el('div', { class: 'empty-state' }, el('div', { class: 'empty-icon', 'aria-hidden': 'true' }, '▤'), el('h3', {}, owner ? 'Aucune preuve partagée.' : 'Aucune preuve reçue.'), el('p', {}, owner ? 'Vous gardez la main sur le texte et le destinataire.' : 'Seuls les textes volontairement sélectionnés par les étudiants fictifs apparaîtront ici. Aucun accès à leur dialogue ou à leur bilan privé.')));
  return card(el('h3', {}, owner ? 'Mes partages actifs' : 'Preuves explicitement reçues'), state.shares.map(s => el('article', { class: 'proof' }, el('span', { class: 'badge' }, owner ? 'Partagé avec le tuteur démo' : s.owner_label), el('p', { class: 'proof-text' }, s.text), el('p', { class: 'proof-meta' }, 'Texte sélectionné par l’étudiant · A2 · déclaration personnelle'), owner ? button('Révoquer l’accès', async () => { await api(`/api/shares/${s.id}`, 'DELETE', { version: s.version }, true); state.shares = await api('/api/shares'); render(); }, true, true) : null)));
}
function preuves() {
  const owner = state.session.user.role === 'student';
  if (!owner && state.session.user.role !== 'tutor') return [heading('COMPTE DE DÉMONSTRATION', 'Un accès limité à ce rôle.', 'Ce premier prototype porte sur le parcours individuel. La coordination et l’administration n’ont aucun accès aux dialogues privés.'), card(el('p', {}, 'Utilisez un compte étudiant fictif pour explorer le parcours, ou le compte tuteur pour vérifier un partage explicite.'))];
  const content = [proofList(owner)];
  if (owner && state.cycle && ['REVIEWED', 'CLOSED'].includes(state.cycle.state)) {
    const tutor = state.users.find(u => u.role === 'tutor' && u.team === state.session.user.team);
    if (tutor) content.unshift(card(el('span', { class: 'badge neutral' }, 'Un partage volontaire'), el('h2', {}, 'Choisir exactement ce qui devient visible.'), el('p', {}, 'Rédigez ou copiez seulement la preuve que vous souhaitez montrer. Le reste du dialogue et votre bilan restent privés.'), form([
      field('text', 'Texte sélectionné pour le partage', 'Une action, une observation ou une trace précise…', { max: 2000, help: 'Le texte de ce champ est le contenu exact qui sera visible par le tuteur démo.' }),
      el('p', { class: 'fine-print' }, `Destinataire : ${tutor.label} · votre équipe fictive.`),
      el('label', { class: 'check-label' }, el('input', { type: 'checkbox', name: 'confirmed', required: true }), 'Je confirme partager uniquement ce texte avec ce destinataire. Une révocation bloque les accès futurs, sans retirer une copie déjà consultée.')
    ], 'Confirmer le partage de cette preuve', async values => { await api(`/api/cycles/${state.cycle.id}/shares`, 'POST', { version: state.cycle.version, text: values.text, recipient_id: tutor.id, confirmed: values.confirmed === 'on' }, true); state.cycle = await api(`/api/cycles/${state.cycle.id}`); state.shares = await api('/api/shares'); render(); }, false)));
    else content.unshift(card(el('p', {}, 'Aucun tuteur fictif n’est affecté à cette équipe. Le partage est indisponible.')));
  } else if (owner) content.unshift(card(el('h3', {}, 'Le bilan précède la sélection de preuves.'), el('p', {}, 'Terminez d’abord le débrief et sauvegardez votre bilan personnel.'), button('Revenir à mon parcours', async () => { state.view = 'parcours'; render(); }, true)));
  return [heading(owner ? 'MES PREUVES' : 'ESPACE TUTEUR · DÉMONSTRATION', owner ? 'Partager une trace, en connaissance de cause.' : 'Des preuves choisies, un regard humain.', owner ? 'Votre parcours vous appartient. Le partage concerne uniquement le texte et le destinataire que vous confirmez.' : 'Les conversations individuelles restent privées. Vous consultez ici les seules preuves qui vous ont été explicitement adressées.'), el('div', { class: 'stack' }, content)];
}
function aide() { return [heading('LES REPÈRES', 'Apprendre au fil du projet.', 'Le coach accompagne votre réflexion ; l’encadrant humain garde son rôle pédagogique.'), card(el('h2', {}, 'Une boucle d’apprentissage individuelle'), el('ol', { class: 'helper-list' }, ['Choisir un objectif concret.', 'Comprendre puis essayer sur une situation fictive.', 'Préparer une action et son observation.', 'Expérimenter avant de rapporter ce qui s’est passé.', 'Séparer faits, interprétations et leçons.', 'Conserver un bilan privé et partager une preuve si vous le souhaitez.'].map(s => el('li', {}, s))), el('hr', { class: 'divider' }), el('h3', {}, 'Ce que permet cette démonstration'), el('p', {}, 'Les réponses du coach sont une simulation déterministe. Elles servent à éprouver le parcours et doivent être relues par un encadrant. Le référentiel est candidat, sans validation scientifique ou institutionnelle présumée.'), el('p', {}, 'Les comptes sont librement sélectionnables pour tester les différents rôles. N’utilisez aucune donnée réelle. Les textes soumis sont sauvegardés localement ; un champ non envoyé n’est pas sauvegardé.'))]; }
function render() {
  navigation();
  const content = !state.session ? welcome() : state.view === 'aide' ? aide() : state.view === 'preuves' ? preuves() : parcours();
  $('#workspace').replaceChildren(...content.filter(node => node != null));
}
async function boot() {
  try {
    state.users = await api('/api/demo-users');
    try { state.session = await api('/api/me'); } catch { state.session = null; }
    if (state.session) await loadWorkspace();
    render();
  } catch (error) { $('#workspace').replaceChildren(heading('DÉMONSTRATION LOCALE', 'La connexion n’est pas disponible.', 'Vérifiez que le serveur PTD Coach est démarré, puis rechargez cette page.')); notice(error.message); }
}
boot();
