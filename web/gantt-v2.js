(() => {
  'use strict';

  const dayMs = 86_400_000;
  const lastDay = Date.parse('2100-12-31') / dayMs;
  const dayNumber = value => Date.parse(value) / dayMs;
  const isoDay = value => new Date(value * dayMs).toISOString().slice(0, 10);
  const dateFormat = new Intl.DateTimeFormat('fr-FR', { dateStyle: 'medium', timeZone: 'UTC' });
  const tickFormat = new Intl.DateTimeFormat('fr-FR', { day: 'numeric', month: 'short', timeZone: 'UTC' });
  const dateLabel = value => dateFormat.format(new Date(value * dayMs));
  const finalDay = task => dayNumber(task.start) + Math.max(0, task.duration - 1);
  const dateRange = task => {
    const start = dayNumber(task.start);
    return finalDay(task) === start ? dateLabel(start) : `${dateLabel(start)} – ${dateLabel(finalDay(task))}`;
  };

  function node(tag, content, className) {
    const element = document.createElement(tag);
    if (content != null) element.textContent = content;
    if (className) element.className = className;
    return element;
  }

  function button(label, action, className = 'secondary') {
    const control = node('button', label, className);
    control.type = 'button';
    control.addEventListener('click', action);
    return control;
  }

  function label(text, control) {
    const field = node('label', text);
    field.append(control);
    return field;
  }

  function warningsFor(tasks) {
    const byId = new Map(tasks.map(task => [task.id, task]));
    return tasks.flatMap(task => task.predecessors.flatMap(id => {
      const predecessor = byId.get(id);
      const earliest = dayNumber(predecessor.start) + predecessor.duration;
      return dayNumber(task.start) < earliest
        ? [{ task_id: task.id, predecessor_id: id, earliest_start: isoDay(earliest) }]
        : [];
    }));
  }

  function ticksFor(first, span) {
    const step = [1, 2, 7, 14, 28, 56, 91, 182, 365].find(value => span / value <= 7)
      ?? Math.ceil(span / 7 / 365) * 365;
    const ticks = [];
    for (let offset = 0; offset < span; offset += step) {
      const day = first + offset;
      ticks.push({ offset, label: span <= 120 ? tickFormat.format(new Date(day * dayMs)) : dateLabel(day) });
    }
    return ticks;
  }

  function chartFor(tasks, baseline, edit, conflicted) {
    const baselineById = new Map((baseline?.tasks ?? []).map(task => [task.id, task]));
    const currentById = new Map(tasks.map(task => [task.id, task]));
    const historical = [...baselineById.values()].filter(task => !currentById.has(task.id));
    const rows = [...tasks, ...historical];
    if (!rows.length) return node('p', 'Ajoutez une tâche ou chargez l’exemple fictif pour afficher le planning.', 'muted');

    const datedTasks = [...tasks, ...baselineById.values()];
    const first = Math.min(...datedTasks.map(task => dayNumber(task.start)));
    const last = Math.max(...datedTasks.map(finalDay));
    const span = last - first + 1;
    const ticks = ticksFor(first, span);
    const percent = days => `${100 * days / span}%`;
    const frame = node('div', null, 'ptd-gantt-scroll');
    frame.tabIndex = 0;
    frame.setAttribute('role', 'region');
    frame.setAttribute('aria-label', 'Frise du planning, défilement horizontal');
    const chart = node('div', null, 'ptd-gantt-chart');
    const period = node('div', null, 'ptd-gantt-chart-row ptd-gantt-period');
    const axis = node('div', null, 'ptd-gantt-axis');
    axis.setAttribute('aria-hidden', 'true');
    for (const tick of ticks) {
      const marker = node('span', tick.label, 'ptd-gantt-tick');
      marker.style.left = percent(tick.offset);
      axis.append(marker);
    }
    period.append(node('p', `${dateLabel(first)} – ${dateLabel(last)}`, 'ptd-gantt-task-label'), axis);
    chart.append(period);

    function addBar(track, task, variant) {
      const bar = node('span', null, `ptd-gantt-bar ${variant}`);
      bar.style.left = percent(dayNumber(task.start) - first + (task.duration ? 0 : 0.5));
      if (task.duration) {
        bar.style.width = percent(task.duration);
      } else {
        bar.classList.add('ptd-gantt-milestone');
      }
      bar.setAttribute('aria-hidden', 'true');
      track.append(bar);
    }

    for (const task of rows) {
      const current = currentById.get(task.id);
      const reference = baselineById.get(task.id);
      const row = node('div', null, 'ptd-gantt-chart-row');
      const description = node('div', null, 'ptd-gantt-task-label');
      if (current && edit) {
        const control = button(task.name, () => edit(task), 'ptd-gantt-edit');
        control.setAttribute('aria-label', `Modifier ${task.name}`);
        description.append(control);
      } else {
        description.append(node('strong', task.name));
      }
      if (current) {
        const kind = task.duration ? `${task.duration} j` : 'Jalon';
        description.append(node('p', `${dateRange(task)} · ${kind}`, 'ptd-gantt-detail'));
        if (current.predecessors.length) {
          const names = current.predecessors.map(id => currentById.get(id).name);
          description.append(node('p', `Après ${names.join(', ')}`, 'ptd-gantt-detail'));
        }
        if (conflicted.has(task.id)) description.append(node('p', 'Dépendance à vérifier', 'ptd-gantt-conflict'));
      }
      if (reference) {
        const historicalName = current && current.name !== reference.name ? `${reference.name} · ` : '';
        const kind = reference.duration ? `${reference.duration} j` : 'Jalon';
        description.append(node('p', `Référence · ${historicalName}${dateRange(reference)} · ${kind}`, 'ptd-gantt-detail'));
      }
      const track = node('div', null, 'ptd-gantt-track');
      for (const tick of ticks.slice(1)) {
        const line = node('span', null, 'ptd-gantt-gridline');
        line.style.left = percent(tick.offset);
        track.append(line);
      }
      if (current) addBar(track, current, conflicted.has(current.id) ? 'ptd-gantt-bar-conflict' : 'ptd-gantt-bar-current');
      if (reference) addBar(track, reference, 'ptd-gantt-bar-reference');
      row.append(description, track);
      chart.append(row);
    }
    frame.append(chart);
    return frame;
  }

  function legend(reference) {
    const description = node('div', null, 'ptd-gantt-legend');
    description.append(node('span', 'Planning actuel', 'ptd-gantt-key-current'), node('span', 'Jalon', 'ptd-gantt-key-milestone'));
    if (reference) description.append(node('span', 'Planning de référence', 'ptd-gantt-key-reference'));
    return description;
  }

  function mount(container, { data, version, save, openMethod, example }) {
    let draft = structuredClone(data);
    let currentVersion = version;
    let dirty = false;
    let saving = false;
    let showBaseline = Boolean(draft.baseline);
    let editing = null;
    let editorOpen = false;

    const section = node('section', null, 'ptd-gantt');
    const toolbar = node('div', null, 'ptd-gantt-toolbar');
    const editor = node('form', null, 'ptd-gantt-form');
    editor.hidden = true;
    const feedback = node('p', '', 'ptd-gantt-status');
    feedback.setAttribute('role', 'status');
    const error = node('p', '', 'ptd-gantt-error');
    error.setAttribute('role', 'alert');
    error.hidden = true;
    const warningPanel = node('div', null, 'ptd-gantt-warning');
    const chart = node('div', null, 'ptd-gantt-chart-area');
    const name = node('input');
    name.required = true;
    name.maxLength = 120;
    const start = node('input');
    start.type = 'date';
    start.required = true;
    start.min = '2000-01-01';
    start.max = '2100-12-31';
    const duration = node('input');
    duration.type = 'number';
    duration.required = true;
    duration.min = '0';
    duration.max = '3660';
    duration.step = '1';
    const dependencies = node('fieldset', null, 'ptd-gantt-dependencies');
    const editorTitle = node('h3', 'Ajouter une tâche');
    const editorButtons = node('div', null, 'ptd-gantt-toolbar');
    const apply = node('button', 'Ajouter au planning');
    apply.type = 'submit';
    const remove = button('Supprimer cette tâche', removeTask, 'secondary danger');
    editorButtons.append(apply, button('Annuler', () => closeEditor(true)), remove);
    const fields = node('div', null, 'ptd-gantt-fields');
    fields.append(label('Nom de la tâche ou du jalon', name), label('Début', start), label('Durée (jours, 0 pour un jalon)', duration));
    editor.append(editorTitle, fields, dependencies, editorButtons);

    const add = button('Ajouter une tâche', () => openEditor(null));
    const capture = button('Capturer la référence', captureBaseline);
    const compare = button('Comparer à la référence', () => {
      showBaseline = !showBaseline;
      render();
    });
    const print = button('Imprimer / PDF', printPlan);
    const persist = button('Enregistrer le Gantt', persistPlan, '');
    toolbar.append(add, capture, compare, print);
    const load = example && button('Charger un exemple fictif', loadExample);
    if (load) toolbar.append(load);
    if (openMethod) toolbar.append(button('Consulter la méthode', openMethod));
    toolbar.append(persist);
    section.append(toolbar, feedback, error, editor, warningPanel, chart);
    container.replaceChildren(section);

    function setError(message = '') {
      error.textContent = message;
      error.hidden = !message;
    }

    function updateControls() {
      add.disabled = saving || editorOpen || draft.tasks.length >= 100;
      capture.disabled = saving || editorOpen || !draft.tasks.length;
      compare.disabled = saving || !draft.baseline;
      compare.setAttribute('aria-pressed', String(Boolean(draft.baseline) && showBaseline));
      const hasVisibleTasks = draft.tasks.length || (showBaseline && draft.baseline?.tasks.length);
      print.disabled = saving || editorOpen || !hasVisibleTasks;
      persist.disabled = saving || editorOpen || !dirty;
      if (load) load.disabled = saving || editorOpen;
    }

    function warningList(warnings) {
      const byId = new Map(draft.tasks.map(task => [task.id, task]));
      const list = node('ul');
      for (const warning of warnings) {
        const task = byId.get(warning.task_id);
        const predecessor = byId.get(warning.predecessor_id);
        list.append(node('li', `« ${task.name} » commence trop tôt après « ${predecessor.name} ». Début possible à partir du ${dateLabel(dayNumber(warning.earliest_start))}.`));
      }
      return list;
    }

    function render(warnings = warningsFor(draft.tasks)) {
      const reference = showBaseline ? draft.baseline : null;
      const conflicted = new Set(warnings.map(warning => warning.task_id));
      const previousScroll = chart.querySelector('.ptd-gantt-scroll')?.scrollLeft ?? 0;
      const diagram = chartFor(draft.tasks, reference, editorOpen || saving ? null : openEditor, conflicted);
      chart.replaceChildren(diagram);
      diagram.scrollLeft = previousScroll;
      if (draft.tasks.length || reference?.tasks.length) chart.prepend(legend(reference));
      warningPanel.hidden = !warnings.length;
      warningPanel.replaceChildren();
      if (warnings.length) warningPanel.append(node('h3', 'Dépendances à vérifier'), warningList(warnings));
      updateControls();
    }

    function markChanged(message = 'Modifications à enregistrer.') {
      dirty = true;
      feedback.textContent = message;
      setError();
      render();
    }

    function openEditor(task) {
      if (saving || editorOpen) return;
      editorOpen = true;
      editing = task?.id ?? null;
      editorTitle.textContent = task ? 'Modifier la tâche ou le jalon' : 'Ajouter une tâche ou un jalon';
      apply.textContent = task ? 'Appliquer au planning' : 'Ajouter au planning';
      remove.hidden = !task;
      name.value = task?.name ?? '';
      start.value = task?.start ?? draft.tasks.at(-1)?.start ?? '';
      duration.value = task?.duration ?? 1;
      name.setCustomValidity('');
      duration.setCustomValidity('');

      const forbidden = new Set(editing ? [editing] : []);
      const successors = new Map(draft.tasks.map(candidate => [candidate.id, []]));
      for (const candidate of draft.tasks) {
        for (const predecessor of candidate.predecessors) successors.get(predecessor).push(candidate.id);
      }
      for (const id of forbidden) {
        for (const successor of successors.get(id)) forbidden.add(successor);
      }
      dependencies.replaceChildren(node('legend', 'Prédécesseurs (fin → début)'));
      for (const candidate of draft.tasks) {
        if (forbidden.has(candidate.id)) continue;
        const field = node('label', null, 'ptd-gantt-dependency');
        const checkbox = node('input');
        checkbox.type = 'checkbox';
        checkbox.value = candidate.id;
        checkbox.checked = task?.predecessors.includes(candidate.id) ?? false;
        field.append(checkbox, node('span', candidate.name));
        dependencies.append(field);
      }
      if (dependencies.children.length === 1) dependencies.append(node('p', 'Aucun prédécesseur disponible.', 'muted'));
      editor.hidden = false;
      setError();
      render();
      name.focus();
    }

    function closeEditor(restoreFocus = false) {
      const formerTaskIndex = draft.tasks.findIndex(task => task.id === editing);
      editing = null;
      editorOpen = false;
      editor.hidden = true;
      render();
      if (restoreFocus) {
        const editButtons = chart.querySelectorAll('.ptd-gantt-edit');
        (editButtons[formerTaskIndex] ?? add).focus();
      }
    }

    name.addEventListener('input', () => name.setCustomValidity(''));
    for (const field of [start, duration]) field.addEventListener('input', () => duration.setCustomValidity(''));
    editor.addEventListener('submit', event => {
      event.preventDefault();
      if (!name.value.trim()) {
        name.setCustomValidity('Renseignez le nom de la tâche.');
        name.reportValidity();
        return;
      }
      const candidate = {
        id: editing ?? crypto.randomUUID(),
        name: name.value.trim(),
        start: start.value,
        duration: duration.valueAsNumber,
        predecessors: [...dependencies.querySelectorAll('input:checked')].map(input => input.value)
      };
      if (finalDay(candidate) > lastDay) {
        duration.setCustomValidity('La tâche se termine au-delà du 31 décembre 2100.');
        duration.reportValidity();
        return;
      }
      if (editing) {
        draft.tasks = draft.tasks.map(task => task.id === editing ? candidate : task);
      } else {
        draft.tasks.push(candidate);
        editing = candidate.id;
      }
      markChanged();
      closeEditor(true);
    });

    function removeTask() {
      const task = draft.tasks.find(item => item.id === editing);
      const dependents = draft.tasks.filter(item => item.predecessors.includes(editing)).length;
      const note = dependents ? '\nLes liens de dépendance vers cette tâche seront supprimés.' : '';
      if (!window.confirm(`Supprimer « ${task.name} » du planning ?${note}`)) return;
      draft.tasks = draft.tasks.filter(item => item.id !== editing);
      for (const item of draft.tasks) item.predecessors = item.predecessors.filter(id => id !== editing);
      markChanged('Tâche supprimée. Enregistrez pour conserver la modification.');
      closeEditor(true);
    }

    function captureBaseline() {
      if (draft.baseline && !window.confirm('Remplacer le planning de référence par le planning actuel ?')) return;
      draft.baseline = { tasks: structuredClone(draft.tasks) };
      showBaseline = true;
      markChanged('Référence capturée. Enregistrez pour la conserver.');
    }

    function loadExample() {
      if ((draft.tasks.length || draft.baseline || dirty) && !window.confirm('Remplacer le planning en cours par l’exemple fictif ?')) return;
      draft = structuredClone(example);
      showBaseline = Boolean(draft.baseline);
      markChanged('Exemple fictif chargé. Enregistrez pour le conserver.');
    }

    async function persistPlan() {
      if (saving || !dirty || editorOpen) return;
      saving = true;
      setError();
      feedback.textContent = 'Enregistrement en cours…';
      render();
      let warnings;
      try {
        const saved = await save(structuredClone(draft), currentVersion);
        draft = structuredClone(saved.data);
        currentVersion = saved.version;
        warnings = saved.warnings;
        dirty = false;
        feedback.textContent = 'Gantt enregistré.';
      } catch (failure) {
        feedback.textContent = 'Modifications à enregistrer.';
        setError(failure.message || 'Le Gantt n’a pas pu être enregistré.');
      } finally {
        saving = false;
        render(warnings);
      }
    }

    function printPlan() {
      const reference = showBaseline ? draft.baseline : null;
      const warnings = warningsFor(draft.tasks);
      const conflicted = new Set(warnings.map(warning => warning.task_id));
      const page = node('main', null, 'ptd-gantt-print-page');
      page.append(node('h1', 'Planning Gantt'));
      if (dirty) page.append(node('p', 'Modifications non enregistrées.', 'muted'));
      page.append(legend(reference), chartFor(draft.tasks, reference, null, conflicted));
      if (warnings.length) page.append(node('h2', 'Dépendances à vérifier'), warningList(warnings));
      document.body.append(page);
      document.body.classList.add('ptd-gantt-print');
      const cleanup = () => {
        page.remove();
        document.body.classList.remove('ptd-gantt-print');
      };
      window.addEventListener('afterprint', cleanup, { once: true });
      window.print();
    }

    render();
    return { dirty: () => dirty || editorOpen };
  }

  window.PTDGantt = { mount };
})();
