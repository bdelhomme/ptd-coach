const $ = selector => document.querySelector(selector);
const state = { session: null, config: null, conversation: null, busy: false, keys: new Map() };

function node(tag, text, className) {
  const item = document.createElement(tag);
  if (text != null) item.textContent = text;
  if (className) item.className = className;
  return item;
}
function showError(message = '') {
  $('#error').textContent = message;
  $('#error').hidden = !message;
}
function lock(locked) {
  state.busy = locked;
  document.querySelectorAll('button,select,input').forEach(item => { item.disabled = locked; });
  $('#waiting').hidden = !locked;
  $('#message').readOnly = locked;
}
async function action(task) {
  if (state.busy) return;
  lock(true); showError();
  try { await task(); }
  catch (error) { showError(error.message); }
  finally { lock(false); updateSend(); }
}
async function api(path, method = 'GET', payload) {
  const headers = {};
  const signature = method + path + JSON.stringify(payload);
  if (method !== 'GET') {
    headers['Content-Type'] = 'application/json';
    if (state.session) headers['X-CSRF-Token'] = state.session.csrf;
    if (!state.keys.has(signature)) state.keys.set(signature, crypto.randomUUID());
    headers['Idempotency-Key'] = state.keys.get(signature);
  }
  let response;
  try { response = await fetch(path, { method, headers, credentials: 'same-origin', body: payload === undefined ? undefined : JSON.stringify(payload) }); }
  catch { throw new Error('Connexion locale interrompue. Réessayez le même message : sa clé est conservée pour éviter un double appel.'); }
  const value = await response.json();
  if (!response.ok) {
    if (!['call_pending', 'internal_error'].includes(value.error?.code)) state.keys.delete(signature);
    throw new Error(value.error?.message || 'Cette action n’a pas abouti.');
  }
  state.keys.delete(signature);
  return value;
}
function updateSend() {
  $('#send').disabled = state.busy || !state.conversation || !state.config?.configured || state.conversation.pending;
  $('#export').disabled = state.busy || !state.conversation;
}
function scopeHelp() {
  $('#scope-help').textContent = $('#scope').value === 'individual'
    ? 'Visible seulement pour ce compte. Aucun transfert automatique vers l’équipe ou le tuteur.'
    : 'Visible aux membres de cette équipe fictive. Saisissez une synthèse discutée ensemble ; aucun dialogue privé n’est repris.';
}
async function refreshList() {
  const list = await api('/api/coach/conversations');
  $('#conversations').replaceChildren(...list.map((item, index) => {
    const name = item.coach_version.toUpperCase().replace('V0', 'V0.') + ' · ' + (item.scope === 'individual' ? 'Privée' : 'Équipe') + ' · ' + new Date(item.created_at).toLocaleString('fr-FR', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });
    const button = node('button', name + (item.pending ? ' · en attente' : ''));
    button.type = 'button';
    if (state.conversation?.id === item.id) { button.className = 'active'; button.setAttribute('aria-current', 'true'); }
    button.addEventListener('click', () => action(async () => {
      state.conversation = await api('/api/coach/conversations/' + item.id);
      $('#message').value = '';
      renderConversation(); await refreshList();
    }));
    return button;
  }));
}
function renderConversation() {
  const conversation = state.conversation;
  const collective = conversation?.scope === 'collective';
  $('#visibility').textContent = !conversation ? 'Choisissez votre espace' : collective ? 'Collectif · équipe uniquement' : 'Privé · ce compte uniquement';
  $('#visibility').className = 'badge' + (collective ? ' collective' : '');
  $('#conversation-title').textContent = collective ? 'Réfléchir ensemble.' : 'De quoi avez-vous besoin ?';
  $('#provider').textContent = (conversation ? conversation.coach_version.toUpperCase().replace('V0', 'V0.') + ' · ' : '') + (state.config.provider === 'mistral' ? 'API Mistral' : 'Simulation hors réseau') + ' · ' + state.config.model +
    (state.config.configured ? '' : ' · Clé absente : ajoutez MISTRAL_API_KEY dans .env, puis redémarrez le serveur.');
  $('#starters').hidden = !!conversation?.messages.length;
  const messages = conversation?.messages || [];
  $('#messages').replaceChildren(...messages.map((message, index) => {
    const bubble = node('article', null, 'bubble ' + message.role);
    bubble.append(node('span', message.role === 'assistant' ? 'PTD Coach' : collective ? 'Équipe · ' + message.author_id.replace('student_demo_', 'étudiant ') : 'Vous', 'speaker'));
    // Only bold emphasis is rendered, using text nodes. No HTML or URLs execute.
    const content = node('p');
    message.content.split(/(\*\*[^*]+\*\*)/g).forEach(part => {
      content.append(part.startsWith('**') && part.endsWith('**')
        ? node('strong', part.slice(2, -2)) : document.createTextNode(part));
    });
    bubble.append(content);
    if (message.role === 'assistant') {
      const invocation = conversation.invocations.filter(item => item.status === 'succeeded')[Math.floor(index / 2)];
      if (invocation) bubble.append(node('small', invocation.model_returned + ' · ' + (invocation.usage.total_tokens ?? 'non mesuré') + ' tokens · ' + (invocation.latency_ms ?? '?') + ' ms' + (invocation.finish_reason === 'length' ? ' · réponse limitée en longueur' : '')));
    }
    return bubble;
  }));
  if (conversation) {
    const usage = conversation.usage;
    $('#usage').textContent = 'Consommation cumulée : ' + usage.known_tokens.total_tokens.toLocaleString('fr-FR') + ' tokens mesurés' +
      ' (entrée ' + usage.known_tokens.prompt_tokens + ', sortie ' + usage.known_tokens.completion_tokens + ').' +
      (usage.unmeasured_calls ? ' ' + usage.unmeasured_calls + ' appel(s) non mesuré(s).' : '');
    if (conversation.pending) showError('Un appel est en cours ou son résultat est incertain. Actualisez pour vérifier. Aucun renvoi automatique.');
  } else $('#usage').textContent = 'Créez une conversation pour commencer. Aucun message n’est envoyé automatiquement.';
  $('#messages').scrollTop = $('#messages').scrollHeight;
  updateSend();
}
async function load() {
  state.config = await api('/api/coach/config');
  $('#coach-version').value = state.config.default_coach_version;
  const resources = await api('/api/coach/resources');
  $('#resources').replaceChildren(...resources.map(resource => {
    const details = node('details');
    details.append(node('summary', resource.title));
    details.append(node('pre', resource.content, 'resource-text'));
    return details;
  }));
  $('#identity').textContent = state.session.user.label + ' · équipe ' + state.session.user.team.slice(-1);
  $('#login').hidden = true; $('#workspace').hidden = false;
  await refreshList(); renderConversation(); scopeHelp();
}
$('#open').addEventListener('click', () => action(async () => {
  state.session = await api('/api/demo-session', 'POST', { user_id: $('#student').value });
  state.conversation = null; state.keys.clear(); await load();
}));
$('#logout').addEventListener('click', () => action(async () => {
  await api('/api/demo-session', 'DELETE');
  state.session = null; state.conversation = null; state.keys.clear();
  $('#messages').replaceChildren(); $('#conversations').replaceChildren(); $('#message').value = '';
  $('#synthetic').checked = false;
  $('#workspace').hidden = true; $('#login').hidden = false;
}));
$('#scope').addEventListener('change', scopeHelp);
$('#new').addEventListener('click', () => action(async () => {
  if (!$('#synthetic').checked) throw new Error('Confirmez l’utilisation de données fictives avant de créer une conversation.');
  state.conversation = await api('/api/coach/conversations', 'POST', { scope: $('#scope').value, synthetic_confirmed: true, coach_version: $('#coach-version').value });
  $('#message').value = ''; renderConversation(); await refreshList(); $('#message').focus();
}));
$('#compose').addEventListener('submit', event => {
  event.preventDefault();
  action(async () => {
    if (!state.conversation) throw new Error('Choisissez un espace puis commencez une conversation.');
    const text = $('#message').value.trim();
    if (!text) return;
    state.conversation = await api('/api/coach/conversations/' + state.conversation.id + '/messages', 'POST', { message: text, version: state.conversation.version });
    $('#message').value = ''; renderConversation(); await refreshList(); $('#message').focus();
  });
});
$('#refresh').addEventListener('click', () => action(async () => {
  if (state.conversation) state.conversation = await api('/api/coach/conversations/' + state.conversation.id);
  await refreshList(); renderConversation();
}));
$('#export').addEventListener('click', () => action(async () => {
  if (!state.conversation) return;
  const value = await api('/api/coach/conversations/' + state.conversation.id + '/export');
  const url = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'ptd-conversation-fictive.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}));
document.querySelectorAll('[data-example]').forEach(button => button.addEventListener('click', () => {
  $('#message').value = button.dataset.example; $('#message').focus();
}));
action(async () => {
  try { state.session = await api('/api/me'); } catch { return; }
  if (state.session.user.role === 'student') await load();
  else state.session = null;
});
