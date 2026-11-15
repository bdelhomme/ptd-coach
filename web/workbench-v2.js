const specificationGroups = [
  ["Contexte et périmètre", [
    ["context", "Contexte"], ["need", "Besoin et décision à éclairer"], ["scope", "Périmètre"],
    ["exclusions", "Hors périmètre"], ["stakeholders", "Parties prenantes"],
  ]],
  ["Livrables et vérification", [
    ["deliverables", "Livrables"], ["requirements", "Exigences"], ["constraints", "Contraintes"],
    ["verification", "Modalités de vérification"], ["acceptance", "Critères d’acceptation"],
  ]],
  ["Points à éclaircir", [
    ["assumptions", "Hypothèses à vérifier"], ["questions", "Questions ouvertes"],
    ["sponsor_evidence", "Éléments confirmés par le commanditaire et leurs sources"],
  ]],
];

const registerFields = {
  risks: [
    ["statement", "Risque ou problème"], ["impact", "Impact"], ["signal", "Signal ou déclencheur"],
    ["response", "Réponse envisagée"], ["owner", "Responsable du suivi"],
  ],
  decisions: [
    ["statement", "Décision ou option envisagée"], ["rationale", "Motif"], ["authority", "Personne ou instance qui décide"],
    ["source", "Source de l’accord"], ["next", "Suite à donner"],
  ],
};

function node(tag, content, className) {
  const element = document.createElement(tag);
  if (content) element.textContent = content;
  if (className) element.className = className;
  return element;
}

function button(label, action, className) {
  const element = node("button", label, className);
  element.type = "button";
  element.addEventListener("click", action);
  return element;
}

function field(label, control) {
  const wrapper = node("label", null, "wb2-field");
  wrapper.append(node("span", label), control);
  return wrapper;
}

function textInput(value, update, {limit, label, multiline, required, type} = {}) {
  const input = node(multiline ? "textarea" : "input");
  if (!multiline) input.type = type || "text";
  if (multiline) input.rows = 2;
  if (limit) input.maxLength = limit;
  if (label) input.setAttribute("aria-label", label);
  input.required = Boolean(required);
  input.value = value;
  input.addEventListener("input", () => update(input.value));
  return input;
}

function picker(value, choices, update, label) {
  const select = node("select");
  for (const [key, name] of choices) {
    const option = node("option", name);
    option.value = key;
    select.append(option);
  }
  select.value = value;
  if (label) select.setAttribute("aria-label", label);
  select.addEventListener("change", () => update(select.value));
  return select;
}

function editValue(record, key, change) {
  return value => {
    record[key] = value;
    change();
  };
}

function grid(caption) {
  const wrapper = node("div", null, "wb2-scroll");
  const table = node("table", null, "wb2-table");
  const head = table.createTHead().insertRow();
  const body = table.createTBody();
  table.createCaption().textContent = caption;
  wrapper.append(table);
  return {wrapper, head, body};
}

function header(row, title) {
  const cell = node("th", title);
  cell.scope = "col";
  row.append(cell);
  return cell;
}

function specification(container, state) {
  const {draft, change, render} = state;
  const reference = draft.reference;
  const controls = node("section", null, "wb2-card");
  controls.append(node("h3", "Référence du cahier des charges"));
  if (reference) {
    controls.append(node("p", `Source de la référence · ${reference.source}`));
    controls.append(node("p", "Les champs modifiés affichent leur valeur de référence."));
  } else {
    controls.append(node("p", "Figez le texte actuel avec sa source pour suivre les évolutions du cahier des charges."));
    const source = textInput(state.referenceSource, value => {
      state.referenceSource = value;
    }, {limit: 300});
    const error = node("p", "", "wb2-feedback");
    error.setAttribute("role", "alert");
    const capture = button("Figer le texte comme référence", () => {
      if (!source.value.trim()) {
        error.textContent = "Indiquez la source de la référence.";
        source.focus();
        return;
      }
      if (!Object.values(draft.sections).some(value => value.trim())) {
        error.textContent = "Renseignez au moins un champ du cahier des charges.";
        container.querySelector("textarea")?.focus();
        return;
      }
      draft.reference = {sections: structuredClone(draft.sections), source: source.value.trim()};
      render();
      container.querySelector("textarea")?.focus();
    });
    controls.append(field("Source de la référence", source), capture, error);
  }
  container.append(controls);

  for (const [title, entries] of specificationGroups) {
    const group = node("section", null, "wb2-card");
    group.append(node("h3", title));
    for (const [key, label] of entries) {
      const value = draft.sections[key];
      const marker = node("p", "", "wb2-reference");
      const updateMarker = text => {
        marker.hidden = !reference || text.trim() === reference.sections[key].trim();
        if (reference && !marker.hidden) {
          marker.textContent = `Champ modifié. Référence · ${reference.sections[key] || "champ vide"}`;
        }
      };
      const input = textInput(value, text => {
        draft.sections[key] = text;
        updateMarker(text);
        change();
      }, {limit: 900, multiline: true});
      if (reference) {
        marker.id = `wb2-spec-${key}`;
        input.setAttribute("aria-describedby", marker.id);
      }
      updateMarker(value);
      group.append(field(label, input), marker);
    }
    container.append(group);
  }
}

function raci(container, {draft, change, render}) {
  container.append(node("p", "R réalise, A assume la responsabilité finale, C est consulté et I est informé. R/A cumule R et A."));
  const {wrapper, head, body} = grid("Attributions par activité et par rôle");
  const choices = [["", "Vide"], ["R", "R"], ["A", "A"], ["RA", "R/A"], ["C", "C"], ["I", "I"]];
  header(head, "Activité");
  const updateLabels = () => {
    const rows = Array.from(body.rows);
    rows.forEach((row, index) => {
      const name = draft.rows[index].activity || `Activité ${index + 1}`;
      Array.from(row.querySelectorAll("select")).forEach((select, roleIndex) => {
        select.setAttribute("aria-label", `${name}, ${draft.roles[roleIndex] || `rôle ${roleIndex + 1}`}`);
      });
    });
  };

  draft.roles.forEach((role, index) => {
    const cell = header(head, "");
    const input = textInput(role, value => {
      draft.roles[index] = value;
      updateLabels();
      change();
    }, {limit: 70, required: true, label: `Nom du rôle ${index + 1}`});
    input.dataset.role = index;
    const remove = button("Retirer", () => {
      draft.roles.splice(index, 1);
      for (const row of draft.rows) row.assignments.splice(index, 1);
      render("#wb2-add-role");
    }, "wb2-subtle");
    remove.setAttribute("aria-label", `Retirer le rôle ${index + 1}`);
    cell.append(input, remove);
  });

  header(head, "Points à vérifier");
  header(head, "Actions");
  draft.rows.forEach((row, index) => {
    const line = body.insertRow();
    const feedback = node("span");
    feedback.setAttribute("aria-live", "polite");
    const updateWarnings = () => {
      const messages = [];
      const accountable = row.assignments.filter(value => value.includes("A")).length;
      if (!row.assignments.some(value => value.includes("R"))) messages.push("Aucun R");
      if (accountable === 0) messages.push("Aucun A");
      if (accountable > 1) messages.push("Plusieurs A");
      feedback.textContent = messages.join(" · ") || "—";
      feedback.classList.toggle("wb2-warning", messages.length > 0);
    };
    const activity = textInput(row.activity, value => {
      row.activity = value;
      updateLabels();
      change();
    }, {limit: 120, required: true, label: `Activité ${index + 1}`});
    activity.dataset.activity = index;
    line.insertCell().append(activity);
    row.assignments.forEach((assignment, roleIndex) => {
      line.insertCell().append(picker(assignment, choices, value => {
        row.assignments[roleIndex] = value;
        updateWarnings();
        change();
      }));
    });
    line.insertCell().append(feedback);
    const remove = button("Retirer", () => {
      draft.rows.splice(index, 1);
      render("#wb2-add-activity");
    }, "wb2-subtle");
    remove.setAttribute("aria-label", `Retirer l’activité ${index + 1}`);
    line.insertCell().append(remove);
    updateWarnings();
  });
  updateLabels();
  const addRole = button("Ajouter un rôle", () => {
    draft.roles.push("");
    for (const row of draft.rows) row.assignments.push("");
    render(`[data-role="${draft.roles.length - 1}"]`);
  });
  addRole.id = "wb2-add-role";
  addRole.disabled = draft.roles.length >= 10;
  const addActivity = button("Ajouter une activité", () => {
    draft.rows.push({activity: "", assignments: draft.roles.map(() => "")});
    render(`[data-activity="${draft.rows.length - 1}"]`);
  });
  addActivity.id = "wb2-add-activity";
  addActivity.disabled = draft.rows.length >= 30;
  const actions = node("div", null, "wb2-actions");
  actions.append(addRole, addActivity);
  container.append(wrapper, actions);
}

function register(container, {draft, change, render}, kind) {
  const isRisk = kind === "risks";
  const types = isRisk ? ["Risque", "Problème"] : ["Envisagée", "Prise"];
  const fields = registerFields[kind];
  if (isRisk) {
    container.append(node("p", "Un risque peut se produire. Un problème est déjà observé."));
  } else {
    container.append(node("p", "Pour une décision prise, renseignez l’autorité qui a décidé et la source de son accord."));
  }
  if (!draft.rows.length) container.append(node("p", "Le registre est vide."));
  draft.rows.forEach((row, index) => {
    const card = node("fieldset", null, "wb2-card wb2-register");
    card.append(node("legend", `Entrée ${index + 1}`));
    const controls = new Map();
    const updateRequired = () => {
      for (const key of ["authority", "source"]) {
        const control = controls.get(key);
        if (control) control.required = row.type === "Prise";
      }
    };
    const type = picker(row.type, types.map(value => [value, value]), value => {
      row.type = value;
      updateRequired();
      change();
    });
    type.dataset.entry = index;
    card.append(field(isRisk ? "Type" : "Statut", type));
    for (const [key, label] of fields) {
      const input = textInput(row[key], editValue(row, key, change), {
        limit: 180, multiline: key === "statement" || key === "rationale", required: key === "statement",
      });
      controls.set(key, input);
      card.append(field(label, input));
    }
    updateRequired();
    card.append(button("Retirer cette entrée", () => {
      draft.rows.splice(index, 1);
      render("#wb2-add-entry");
    }, "wb2-subtle"));
    container.append(card);
  });
  const add = button(isRisk ? "Ajouter un risque ou problème" : "Ajouter une décision", () => {
    draft.rows.push({type: types[0], ...Object.fromEntries(fields.map(([key]) => [key, ""]))});
    render(`[data-entry="${draft.rows.length - 1}"]`);
  });
  add.id = "wb2-add-entry";
  add.disabled = draft.rows.length >= 20;
  container.append(add);
}

function weightInput(value, update, label) {
  const input = textInput(value ?? "", value => update(value === "" ? null : Number(value)), {
    type: "number", required: true, label,
  });
  input.min = "0";
  input.max = "100";
  input.step = "1";
  return input;
}

function matrixResults({criteria, options}, weights, list) {
  const total = weights.reduce((sum, weight) => sum + weight, 0);
  const validWeight = weight => Number.isInteger(weight) && weight >= 0 && weight <= 100;
  const validCriteria = criteria.every(criterion => criterion.name.trim()) && weights.every(validWeight);
  list.replaceChildren();
  for (const option of options) {
    const name = option.name.trim() || "Option sans nom";
    const complete = option.scores.every(cell => cell.score !== null && cell.reason.trim());
    let result = "renseigner les notes et leur justification";
    if (!validCriteria || !total) result = "renseigner les critères et un total de poids positif";
    else if (complete && option.name.trim()) {
      const score = option.scores.reduce((sum, cell, index) => sum + cell.score * weights[index], 0) / total;
      result = `${score.toLocaleString("fr-FR", {maximumFractionDigits: 2})} / 5`;
    } else if (complete) result = "nommer l’option";
    list.append(node("li", `${name} · ${result}`));
  }
}

function matrix(container, state) {
  const {draft, change, render} = state;
  container.append(node("p",
    "Notez chaque option sur les mêmes critères, de 0 à 5, et justifiez la note. Laissez « Inconnue » quand les éléments manquent."));
  const {wrapper, head, body} = grid("Options, critères, poids et notes");
  const summary = node("ul", null, "wb2-results");
  const alternative = node("ul", null, "wb2-results");
  let sensitivityPicker;
  summary.setAttribute("aria-live", "polite");
  alternative.setAttribute("aria-live", "polite");
  const refreshScores = () => {
    const weights = draft.criteria.map(criterion => criterion.weight);
    matrixResults(draft, weights, summary);
    if (state.sensitivityIndex !== null && state.sensitivityWeight !== null) {
      weights[state.sensitivityIndex] = state.sensitivityWeight;
      matrixResults(draft, weights, alternative);
    } else {
      alternative.replaceChildren();
    }
  };
  const changed = () => {
    refreshScores();
    change();
  };

  header(head, "Option");
  draft.criteria.forEach((criterion, index) => {
    const cell = header(head, "");
    const name = textInput(criterion.name, value => {
      criterion.name = value;
      if (sensitivityPicker) sensitivityPicker.options[index + 1].textContent = value || `Critère ${index + 1}`;
      changed();
    }, {
      limit: 70, required: true, label: `Nom du critère ${index + 1}`,
    });
    name.dataset.criterion = index;
    cell.append(name, field("Poids", weightInput(criterion.weight, editValue(criterion, "weight", changed),
      `Poids du critère ${index + 1}`)));
    const remove = button("Retirer", () => {
      draft.criteria.splice(index, 1);
      for (const option of draft.options) option.scores.splice(index, 1);
      if (state.sensitivityIndex === index) state.sensitivityIndex = null;
      else if (state.sensitivityIndex > index) state.sensitivityIndex -= 1;
      render("#wb2-add-criterion");
    }, "wb2-subtle");
    remove.setAttribute("aria-label", `Retirer le critère ${index + 1}`);
    cell.append(remove);
  });
  header(head, "Actions");
  const scores = [["", "Inconnue"], ...Array.from({length: 6}, (_, i) => [String(i), String(i)])];
  draft.options.forEach((option, index) => {
    const row = body.insertRow();
    const name = textInput(option.name, editValue(option, "name", changed), {
      limit: 70, required: true, label: `Nom de l’option ${index + 1}`,
    });
    name.dataset.option = index;
    row.insertCell().append(name);
    option.scores.forEach((cell, criterionIndex) => {
      const label = `option ${index + 1}, critère ${criterionIndex + 1}`;
      const reason = textInput(cell.reason, editValue(cell, "reason", changed), {
        limit: 120, multiline: true, label: `Justification, ${label}`, required: cell.score !== null,
      });
      const score = picker(cell.score === null ? "" : String(cell.score), scores, value => {
        cell.score = value === "" ? null : Number(value);
        reason.required = cell.score !== null;
        changed();
      }, `Note, ${label}`);
      row.insertCell().append(field("Note", score), field("Justification", reason));
    });
    const remove = button("Retirer", () => {
      draft.options.splice(index, 1);
      render("#wb2-add-option");
    }, "wb2-subtle");
    remove.setAttribute("aria-label", `Retirer l’option ${index + 1}`);
    row.insertCell().append(remove);
  });

  const actions = node("div", null, "wb2-actions");
  const addCriterion = button("Ajouter un critère", () => {
    draft.criteria.push({name: "", weight: 1});
    for (const option of draft.options) option.scores.push({score: null, reason: ""});
    render(`[data-criterion="${draft.criteria.length - 1}"]`);
  });
  addCriterion.id = "wb2-add-criterion";
  addCriterion.disabled = draft.criteria.length >= 8;
  const addOption = button("Ajouter une option", () => {
    draft.options.push({name: "", scores: draft.criteria.map(() => ({score: null, reason: ""}))});
    render(`[data-option="${draft.options.length - 1}"]`);
  });
  addOption.id = "wb2-add-option";
  addOption.disabled = draft.options.length >= 10;
  actions.append(addCriterion, addOption);
  const results = node("section", null, "wb2-card");
  results.append(node("h3", "Scores pondérés"),
    node("p", "Le score est la somme des notes multipliées par leurs poids, divisée par le total des poids. Il dépend des critères, des poids et des éléments disponibles au moment de la comparaison."),
    summary);
  container.append(wrapper, actions, results);
  if (draft.criteria.length) {
    const sensitivity = node("section", null, "wb2-card");
    const choices = [["", "Choisir un critère"], ...draft.criteria.map(({name}, index) => [String(index), name || `Critère ${index + 1}`])];
    sensitivityPicker = picker(String(state.sensitivityIndex ?? ""), choices, value => {
      state.sensitivityIndex = value === "" ? null : Number(value);
      state.sensitivityWeight = state.sensitivityIndex === null ? null : draft.criteria[state.sensitivityIndex].weight;
      weight.value = state.sensitivityWeight ?? "";
      weight.disabled = state.sensitivityIndex === null;
      refreshScores();
    });
    const weight = weightInput(state.sensitivityWeight, value => {
      state.sensitivityWeight = value;
      refreshScores();
    });
    weight.disabled = state.sensitivityIndex === null;
    weight.required = false;
    weight.dataset.preview = "";
    sensitivity.append(node("h3", "Sensibilité à un poids"),
      node("p", "Changez un seul poids et comparez les scores. Cette simulation est temporaire."),
      field("Critère à faire varier", sensitivityPicker), field("Poids simulé (0 à 100)", weight), alternative);
    container.append(sensitivity);
  }
  refreshScores();
}

function calendar(container, {draft, change}) {
  const dates = node("div", null, "wb2-dates");
  for (const [key, label] of [["start", "Début de la mission"], ["end", "Fin de la mission"]]) {
    dates.append(field(label, textInput(draft[key], editValue(draft, key, change), {type: "date"})));
  }
  container.append(dates, field("Créneaux, séances et jalons convenus", textInput(
    draft.sessions, editValue(draft, "sessions", change), {limit: 500, multiline: true},
  )));
}

const tools = {
  specification,
  raci,
  risks: (container, state) => register(container, state, "risks"),
  decisions: (container, state) => register(container, state, "decisions"),
  "decision-matrix": matrix,
  calendar,
};

export function mountTool(container, kind, {data, version, save, openMethod, example}) {
  const state = {
    draft: structuredClone(data), referenceSource: "", sensitivityIndex: null, sensitivityWeight: null,
  };
  let saved = JSON.stringify(state.draft);
  let busy = false;
  const dirty = () => JSON.stringify(state.draft) !== saved;
  const form = node("form", null, "wb2-form");
  form.noValidate = true;
  const toolbar = node("div", null, "wb2-actions");
  if (typeof openMethod === "function") toolbar.append(button("Consulter la méthode", () => openMethod()));
  const feedback = node("p", "", "wb2-feedback");
  feedback.setAttribute("role", "status");
  const error = node("p", "", "wb2-feedback wb2-error");
  error.setAttribute("role", "alert");
  const fields = node("fieldset", null, "wb2-fields");
  const editor = node("div", null, "wb2-editor");
  fields.append(editor);
  const saveButton = node("button", "Enregistrer le brouillon");
  saveButton.type = "submit";
  const footer = node("div", null, "wb2-actions");
  footer.append(saveButton, feedback);
  const change = () => {
    saveButton.disabled = busy || !dirty();
    error.textContent = "";
    feedback.textContent = dirty() ? "Modifications à enregistrer." : "";
  };

  const render = focus => {
    editor.replaceChildren();
    tools[kind](editor, state);
    change();
    if (focus) editor.querySelector(focus)?.focus();
  };
  Object.assign(state, {change, render});

  let loadExample;
  if (example) {
    loadExample = button("Charger l’exemple fictif", () => {
      const reference = kind === "specification" ? state.draft.reference : null;
      const next = structuredClone(example);
      if (reference) next.reference = reference;
      if (JSON.stringify(state.draft) === JSON.stringify(next)) return;
      if ((version > 0 || dirty()) && !window.confirm("Remplacer le brouillon affiché par l’exemple fictif ?")) return;
      state.draft = next;
      state.sensitivityIndex = null;
      state.sensitivityWeight = null;
      render();
    });
    toolbar.append(loadExample);
  }
  form.append(toolbar, fields, footer, error);
  form.addEventListener("submit", async event => {
    event.preventDefault();
    if (busy || !dirty()) return;
    for (const control of editor.querySelectorAll("input:not([data-preview]), select, textarea")) {
      if (!control.reportValidity()) return;
    }
    busy = true;
    saveButton.disabled = true;
    fields.disabled = true;
    if (loadExample) loadExample.disabled = true;
    error.textContent = "";
    feedback.textContent = "Enregistrement…";
    try {
      const result = await save(structuredClone(state.draft), version);
      state.draft = structuredClone(result.data);
      version = result.version;
      saved = JSON.stringify(state.draft);
      render();
      feedback.textContent = "Brouillon enregistré.";
    } catch (failure) {
      feedback.textContent = "Modifications à enregistrer.";
      error.textContent = failure?.message || "Le brouillon n’a pas pu être enregistré.";
    } finally {
      busy = false;
      saveButton.disabled = !dirty();
      fields.disabled = false;
      if (loadExample) loadExample.disabled = false;
    }
  });
  container.replaceChildren(form);
  render();
  return {dirty};
}
