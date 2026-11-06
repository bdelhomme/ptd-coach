const $ = (selector) => document.querySelector(selector);
const state = { session: null, users: [], cases: [], cycles: [], cycle: null, shares: [], view: 'parcours', busy: false, planning: false, reflectionReady: false };
const fieldLabels = { answer: 'Réponse à l’exercice', action: 'Action à expérimenter', when: 'Occasion prévue', observation: 'Observation recherchée', facts: 'Faits rapportés', interpretation: 'Interprétation', lesson: 'Leçon à retenir', private_summary: 'Bilan personnel' };
const phases = [
  { title: 'Je m’entraîne', place: 'Ici, avec le coach' },
  { title: 'Je teste une action', place: 'Avec mon équipe' },
  { title: 'Je fais le point', place: 'De retour ici' }
];
const phaseIndex = { OBJECTIVE_SELECTED: 0, LEARNING: 0, PRACTICING: 0, EXPERIMENT_PLANNED: 1, AWAITING_EXPERIENCE: 1, REFLECTING: 2, REVIEWED: 2, CLOSED: 2 };
function currentPhase() {
  return state.cycle?.state === 'AWAITING_EXPERIENCE' && state.reflectionReady ? 2 : (phaseIndex[state.cycle?.state] ?? 0);
}
function reveal(flag, value = true) {
  state[flag] = value;
  render();
  $('#step-title')?.focus();
}
function journeyMap() {
  return el('ol', { class: 'journey-map', 'aria-label': 'Les trois moments de votre séance' }, phases.map((phase, i) =>
    el('li', {}, el('span', { class: 'journey-number' }, i + 1), el('div', {}, el('strong', {}, phase.title), el('span', {}, phase.place)))));
}

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
  return el('aside', { class: 'stack context-stack', 'aria-label': 'Vos repères' },
    card(el('h3', {}, 'À quoi cela va vous servir ?'), el('p', {}, 'Repérer ce qui bloque une tâche pour proposer un planning plus clair à votre équipe.'),
      el('details', { class: 'quiet-details' }, el('summary', {}, 'Ce que je travaille'), el('p', {}, 'A2 · Structurer et planifier un projet.'), el('span', { class: 'badge neutral' }, 'Référentiel candidat'), el('p', { class: 'fine-print' }, 'Cet entraînement n’attribue ni note ni niveau de compétence.'))),
    card(el('h3', {}, 'Qui voit mes réponses ?'), el('p', {}, 'Votre dialogue et votre bilan restent dans votre espace individuel. Le tuteur voit uniquement le texte que vous choisissez de lui partager.'))
  );
}

function navigation() {
  const student = state.session?.user.role === 'student';
  const canShare = state.shares.length > 0 || state.cycle?.data.private_summary;
  const entries = !state.session ? [] : student
    ? [['parcours', '↗', 'Ma séance'], ...(canShare ? [['preuves', '▤', 'Mes partages']] : []), ['aide', '○', 'Comment ça marche']]
    : [['preuves', '▤', 'Preuves reçues'], ['aide', '○', 'Comment ça marche']];
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
  Object.assign(state, { session: null, cycle: null, cycles: [], shares: [], view: 'parcours', planning: false, reflectionReady: false }); keys.clear(); render();
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
  return [heading('BIENVENUE DANS PTD COACH', 'Mieux préparer le travail avec votre équipe.', 'Entraînez-vous sur un exemple, choisissez une action à tester en équipe, puis revenez faire le point.'),
    card(el('span', { class: 'badge' }, 'Un exemple pour commencer'), el('h2', {}, 'Le client tarde à répondre. Que faire en attendant ?'),
      el('p', {}, 'Certaines tâches sont bloquées, mais votre équipe doit préparer sa prochaine revue. Vous allez apprendre à distinguer ce qui peut avancer de ce qui doit attendre.'),
      el('div', { class: 'actions' }, button('Commencer cet exemple guidé →', async () => {
        state.session = await api('/api/demo-session', 'POST', { user_id: 'student_demo_01' });
        await loadWorkspace();
        await beginCase('client-delay');
      })),
      el('p', { class: 'fine-print' }, 'Vous entrez dans un compte étudiant fictif. Les réponses du coach sont simulées ; utilisez seulement des contenus inventés.')),
    journeyMap(),
    el('details', { class: 'history role-picker' }, el('summary', {}, 'Tester un autre compte ou le rôle du tuteur'),
      form([el('label', { class: 'field', for: 'demo-user' }, el('span', {}, 'Compte fictif à ouvrir'), select)], 'Ouvrir ce compte', async values => {
        state.session = await api('/api/demo-session', 'POST', values);
        await loadWorkspace(); render();
      }, false))];
}
async function beginCase(caseId) {
  state.cycle = await api('/api/cycles', 'POST', { case_id: caseId }, true);
  state.cycles.unshift(state.cycle);
  await act('learn');
}

function objective() {
  return card(el('span', { class: 'badge' }, 'Commencer une séance'), el('h2', {}, 'Sur quelle situation voulez-vous vous entraîner ?'),
    el('p', {}, 'Choisissez un exemple. Vous préparerez ensuite une petite action à tester avec votre équipe.'),
    form([el('div', { class: 'case-options', role: 'radiogroup', 'aria-label': 'Situation à travailler' }, state.cases.map((c, i) =>
      el('label', { class: 'case-option' }, el('input', { type: 'radio', name: 'case_id', value: c.id, checked: i === 0, required: true }),
        el('span', {}, c.title, el('small', {}, c.focus)))))], 'Commencer avec cette situation', values => beginCase(values.case_id)));
}
async function act(action, fields = {}) {
  state.cycle = await api(`/api/cycles/${state.cycle.id}/actions`, 'POST', { action, version: state.cycle.version, fields }, true);
  state.planning = false; state.reflectionReady = false;
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
function planRecap(data) {
  return el('div', { class: 'action-recap' },
    el('p', { class: 'mini-label' }, 'MON ACTION À TESTER'), el('p', { class: 'recap-action' }, data.action),
    el('dl', {}, el('dt', {}, 'Quand ?'), el('dd', {}, data.when), el('dt', {}, 'Ce que je vais observer'), el('dd', {}, data.observation)));
}
function cycleCard() {
  const cycle = state.cycle, data = cycle.data;
  const selected = state.cases.find(c => c.id === cycle.case_id);
  const names = {
    OBJECTIVE_SELECTED: ['Commençons par un exemple.', 'Vous allez apprendre à repérer ce qui peut avancer et ce qui attend une validation.'],
    LEARNING: ['D’abord, comment repérer ce qui bloque ?', 'Lisez ce repère. Vous allez ensuite l’utiliser pour proposer une solution à votre équipe fictive.'],
    PRACTICING: state.planning
      ? ['Quelle petite action allez-vous tester ?', 'Choisissez un geste concret à essayer avec votre équipe. Décrivez aussi ce que vous observerez.']
      : data.answer
        ? ['Votre proposition : un point à approfondir.', 'Lisez le retour du coach, puis préparez une action que vous pourrez essayer avec votre équipe.']
        : ['Que proposeriez-vous à votre équipe ?', 'Lisez la situation, puis écrivez quelques phrases. Il s’agit de vous entraîner : votre réponse peut être imparfaite.'],
    EXPERIMENT_PLANNED: ['La suite se passe avec votre équipe.', 'Votre action est enregistrée. Vous pouvez maintenant la tester, puis revenir ici raconter ce qui s’est passé.'],
    AWAITING_EXPERIENCE: state.reflectionReady
      ? ['Vous avez essayé : que s’est-il passé ?', 'Racontez votre essai. Distinguez ce qui s’est passé de ce que vous en pensez.']
      : ['Votre prochaine étape : tester votre action.', 'Vous pouvez fermer cette page. Revenez après avoir essayé votre action avec votre équipe.'],
    REFLECTING: ['Gardez votre leçon pour la suite.', 'Voici la leçon que vous venez d’écrire. Relisez-la et ajustez-la si besoin avant de la conserver dans votre bilan privé.'],
    REVIEWED: ['Votre bilan est enregistré et reste privé.', 'Vous avez terminé cette séance. Vous pourrez retrouver vos réponses et votre bilan en revenant ici.'],
    CLOSED: ['Votre séance est terminée.', 'Votre bilan reste disponible. Vous pouvez vous entraîner sur une autre situation lorsque vous en aurez besoin.'],
  };
  const [title, intro] = names[cycle.state];
  const phase = phases[currentPhase()];
  const node = card(el('span', { class: 'badge' }, phase.place), el('h2', { id: 'step-title', tabindex: '-1' }, title), el('p', {}, intro));
  const latestCoach = cycle.messages.filter(m => m.role === 'coach').at(-1);
  if (latestCoach && cycle.state === 'LEARNING') node.append(coachBlock(latestCoach.content));
  switch (cycle.state) {
    case 'OBJECTIVE_SELECTED':
      node.append(el('div', { class: 'actions' }, button('Voir le premier repère →', () => act('learn')))); break;
    case 'LEARNING':
      node.append(el('div', { class: 'actions' }, button('Essayer sur la situation →', () => act('practice')))); break;
    case 'PRACTICING':
      if (state.planning) {
        node.append(form([
          field('action', 'Ce que je vais faire avec mon équipe', 'Exemple fictif : ajouter les validations attendues dans notre planning.'),
          field('when', 'Quand vais-je l’essayer ?', 'Exemple : lors de notre prochaine réunion simulée.', { single: true }),
          field('observation', 'Comment verrai-je ce que cela change ?', 'Exemple : regarder si chacun sait quelles tâches peuvent commencer.')
        ], 'Enregistrer mon action pour l’équipe', fields => act('plan', fields)),
        el('div', { class: 'actions' }, button('Revenir au retour sur l’exercice', async () => reveal('planning', false), true, true)));
      } else if (!data.answer) {
        node.append(el('div', { class: 'situation' }, el('p', { class: 'mini-label' }, 'LA SITUATION FICTIVE'), el('p', {}, selected.context), el('p', { class: 'situation-question' }, selected.question)),
          form([field('answer', 'Quelles tâches feriez-vous avancer, et lesquelles attendraient ?', 'Expliquez votre idée en quelques phrases.', { help: 'Vous pouvez commencer par : « En attendant la validation, notre équipe pourrait… »' })], 'Recevoir le retour du coach', fields => act('answer', fields)));
      } else {
        node.append(coachBlock(latestCoach.content), el('div', { class: 'actions' }, button('Préparer une action pour mon équipe →', async () => reveal('planning'))),
          el('details', { class: 'quiet-details' }, el('summary', {}, 'Relire la situation et retravailler ma réponse'), el('p', {}, selected.context), el('p', {}, selected.question),
            form([field('answer', 'Ma réponse', 'Votre nouvelle proposition…', { value: data.answer })], 'Envoyer cette nouvelle proposition', fields => act('answer', fields), false)));
      }
      break;
    case 'EXPERIMENT_PLANNED':
      node.append(planRecap(data), el('p', { class: 'demo-hint' }, 'Dans cette démo, imaginez une réunion fictive pour tester votre action. Dans un PTD réel, cette étape aurait lieu avec votre équipe.'),
        el('div', { class: 'actions' }, button('Mettre ma séance en pause →', () => act('start_experience')))); break;
    case 'AWAITING_EXPERIENCE':
      if (!state.reflectionReady) {
        node.append(planRecap(data), el('p', { class: 'demo-hint' }, 'Aucun bilan n’est à remplir avant l’essai. Dans cette démo, utilisez une expérience entièrement fictive.'),
          el('div', { class: 'actions' }, button('J’ai testé mon action : faire le point →', async () => reveal('reflectionReady'))),
          el('p', { class: 'fine-print' }, 'Si vous ne l’avez pas encore testée, vous pouvez simplement fermer cette page : votre plan est sauvegardé.'));
      } else {
        node.append(form([
          field('facts', 'Qu’est-ce qui s’est passé pendant l’essai ?', 'Décrivez les faits de votre simulation : ce que vous avez fait et ce que le groupe fictif a fait.'),
          field('interpretation', 'Comment comprenez-vous ce qui s’est passé ?', 'Dites ce que vous en pensez, en signalant ce qui reste incertain.'),
          field('lesson', 'Qu’allez-vous garder ou changer ?', 'Ce que vous referiez, ou ce que vous essaieriez autrement…'),
          el('label', { class: 'check-label' }, el('input', { type: 'checkbox', name: 'experience_reported', required: true }), 'Je rapporte un essai simulé que j’ai effectué. Le coach ne l’a pas observé.')
        ], 'Enregistrer mon retour d’expérience', fields => act('report', { ...fields, experience_reported: fields.experience_reported === 'on' })),
          el('div', { class: 'actions' }, button('Je n’ai pas encore essayé : revoir mon action', async () => reveal('reflectionReady', false), true, true)));
      }
      break;
    case 'REFLECTING':
      node.append(form([field('private_summary', 'La leçon que je veux garder pour la suite', 'Ce que je veux conserver pour la prochaine fois…', { rows: 5, value: data.lesson, help: 'Ce texte reprend votre réponse précédente. Il restera dans votre espace individuel.' })], 'Garder cette leçon dans mon bilan privé', fields => act('review', fields)));
      break;
    case 'REVIEWED': case 'CLOSED':
      node.append(el('div', { class: 'summary-block' }, data.private_summary),
        el('div', { class: 'actions' }, cycle.state === 'REVIEWED'
          ? button('Terminer ma séance', () => act('close'))
          : button('Essayer une autre situation', async () => { state.cycle = null; state.planning = false; state.reflectionReady = false; render(); })),
        el('details', { class: 'quiet-details' }, el('summary', {}, 'Partager un texte avec mon tuteur (facultatif)'),
          el('p', {}, 'Vous pouvez garder tout votre bilan privé. Si vous partagez une trace, vous choisirez le texte exact et confirmerez son destinataire.'),
          button('Choisir le texte que je veux partager', async () => { state.shares = await api('/api/shares'); state.view = 'preuves'; render(); }, true, true)));
      break;
  }
  return node;
}

function parcours() {
  const progress = state.cycle ? el('ol', { class: 'phase-strip', 'aria-label': 'Où en suis-je ?' }, phases.map((phase, i) =>
    el('li', { class: i === currentPhase() ? 'current' : (i < currentPhase() ? 'done' : ''), 'aria-current': i === currentPhase() ? 'step' : null },
      el('span', { class: 'phase-place' }, phase.place), el('span', {}, `${i + 1}. ${phase.title}`)))) : null;
  const selectCycle = state.cycles.length ? el('details', { class: 'quiet-details previous-sessions' }, el('summary', {}, 'Retrouver une autre séance enregistrée'),
    el('label', { class: 'field' }, el('span', {}, 'Séance à ouvrir'), el('select', { onChange: event => run(async () => {
      if (!event.target.value) return;
      state.cycle = await api(`/api/cycles/${event.target.value}`); state.planning = false; state.reflectionReady = false; render();
    }) }, el('option', { value: '' }, 'Choisir une séance…'), state.cycles.map((c, i) =>
      el('option', { value: c.id }, `${state.cases.find(x => x.id === c.case_id)?.title || 'Séance'} · ${i + 1}`))))) : null;
  return [heading('MA SÉANCE INDIVIDUELLE', 'Un essai pour mieux travailler en équipe.', 'Ici, préparez votre action. Avec votre équipe, testez-la. Puis revenez raconter ce qui s’est passé.'), progress,
    el('div', { class: 'workspace-grid' }, el('div', {}, state.cycle ? cycleCard() : objective(),
      state.cycle ? el('details', { class: 'quiet-details saved-work' }, el('summary', {}, 'Retrouver mes réponses ou exporter ma séance'), history(),
        el('div', { class: 'actions' }, el('a', { href: `/api/cycles/${state.cycle.id}/export`, class: 'button secondary small', download: 'ptd-a2-prive.json' }, 'Exporter ma séance privée'),
          button('Recharger mes réponses enregistrées', async () => { state.cycle = await api(`/api/cycles/${state.cycle.id}`); render(); }, true, true))) : null, selectCycle), context())];
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
  return [heading(owner ? 'MES PARTAGES' : 'ESPACE TUTEUR · DÉMONSTRATION', owner ? 'Choisir un texte pour mon tuteur.' : 'Des preuves choisies, un regard humain.', owner ? 'Votre parcours vous appartient. Le partage concerne uniquement le texte et le destinataire que vous confirmez.' : 'Les conversations individuelles restent privées. Vous consultez ici les seules preuves qui vous ont été explicitement adressées.'), el('div', { class: 'stack' }, content)];
}
function aide() {
  return [heading('COMMENT ÇA MARCHE', 'Vous n’avez pas tout à faire en une fois.', 'Le coach vous aide à préparer un essai dans votre équipe, puis à apprendre de ce qui s’est passé.'),
    journeyMap(), card(el('h2', {}, 'Un exemple concret'),
      el('p', {}, 'Ici : vous réfléchissez à ce que votre équipe pourrait faire pendant qu’elle attend une validation du client.'),
      el('p', {}, 'Avec votre équipe : vous essayez une petite action, par exemple ajouter les validations attendues dans votre planning.'),
      el('p', {}, 'De retour ici : vous racontez ce qui s’est passé et gardez une leçon pour la prochaine fois.'),
      el('hr', { class: 'divider' }), el('h3', {}, 'Vos réponses restent dans votre espace individuel'),
      el('p', {}, 'Vous n’êtes pas obligé de partager votre bilan. Si vous partagez un texte avec votre tuteur, vous en choisissez vous-même le contenu et confirmez le destinataire.'),
      el('p', { class: 'fine-print' }, 'Dans cette démo, les comptes sont fictifs et librement sélectionnables. Le coach suit des réponses simulées. N’utilisez que des contenus inventés.'))];
}
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
