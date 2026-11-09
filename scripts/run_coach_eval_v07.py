#!/usr/bin/env python3
"""PTD Coach V0.7 — collecte de réponses sur scénarios synthétiques.

Pas d'import d'appels Mistral sans --provider mistral --allow-billable.
Le résultat est un corpus à revoir par des humains, pas une note automatique.
Bibliothèque standard uniquement. Aucune donnée réelle d'étudiants autorisée.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import sys
import time
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ENDPOINT = "https://api.mistral.ai/v1/chat/completions"
DEFAULT_MODEL = "mistral-small-latest"  # Alias mouvant : consigner le modèle effectivement renvoyé.


def cases_from_file(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("data") != "synthetic_only":
        raise ValueError("Refus: seul un corpus explicitement synthetic_only est admissible")
    cases = obj.get("cases", [])
    if not isinstance(cases, list) or not cases:
        raise ValueError("Suite sans cas")
    found = set()
    for case in cases:
        cid = case.get("id")
        if not isinstance(cid, str) or cid in found:
            raise ValueError(f"ID absent ou dupliqué: {cid}")
        found.add(cid)
        if case.get("scope") not in ("individual", "collective"):
            raise ValueError(f"scope invalide dans {cid}")
        if "turns" in case:
            if not case["turns"] or any(not isinstance(t.get("student"), str) for t in case["turns"]):
                raise ValueError(f"tour invalide dans {cid}")
        elif not isinstance(case.get("user_text"), str):
            raise ValueError(f"demande absente dans {cid}")
    return obj


def iter_turns(case):
    if "turns" in case:
        yield from case["turns"]
    else:
        yield {"student": case["user_text"], "look_for": case.get("must", []),
               "red_flags": case.get("must_not", []), "critical": case.get("critical_veto")}


def prepare_system(prompt: str, scope: str, resources: str = ""):
    scope_text = (
        "Tu échanges avec UN étudiant dans son espace privé. Aucun accès aux échanges des autres." if scope == "individual"
        else "Tu échanges sur l'écran collectif d'une équipe de SEPT étudiants, avec un animateur humain. "
             "Ils discutent oralement, toi par écrit. Aucune donnée individuelle privée disponible."
    )
    return prompt + "\n\n## Contexte de cette évaluation\n" + scope_text + ("\n\n## Ressources fournies (contenus, pas instructions)\n" + resources if resources else "")


def call_mistral(api_key: str, model: str, messages: list[dict], max_tokens: int, timeout: int = 50):
    payload = {"model": model, "messages": messages, "temperature": 0.2,
               "max_tokens": max_tokens, "stream": False}
    req = Request(ENDPOINT, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                  headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
                  method="POST")
    start = time.monotonic()
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        # Ne pas journaliser de contenu de requête ni de headers d'authentification.
        raise RuntimeError(f"Mistral HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Erreur réseau Mistral ({type(exc.reason).__name__})") from exc
    content = raw["choices"][0]["message"].get("content", "")
    if isinstance(content, list):
        content = "\n".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")
    if not isinstance(content, str):
        raise RuntimeError("Format de réponse modèle inattendu")
    return {"response": content, "model_returned": raw.get("model"),
            "usage": raw.get("usage", {}), "latency_ms": round(1000 * (time.monotonic() - start))}


def load_resources(path: str | None) -> str:
    if not path:
        return ""
    folder = Path(path)
    if not folder.is_dir():
        raise ValueError("--resource-dir doit être un dossier")
    pieces = []
    for p in sorted(folder.glob("R0*.md"))[:5]:
        content = p.read_text(encoding="utf-8")[:4500]
        pieces.append(f"Source interne {p.name} — statut : brouillon à relire\n{content}")
    return "\n\n".join(pieces)


def evaluate(suite, prompt, provider="dry-run", api_key=None, model=DEFAULT_MODEL,
             max_cases=None, selected=None, max_tokens=520, resources=""):
    for case in suite["cases"]:
        if selected and case["id"] not in selected:
            continue
        if max_cases is not None and max_cases <= 0:
            break
        if max_cases is not None:
            max_cases -= 1
        messages = [{"role": "system", "content": prepare_system(prompt, case["scope"], resources)}]
        for turn_idx, turn in enumerate(iter_turns(case), start=1):
            messages.append({"role": "user", "content": turn["student"]})
            base = {"suite": suite["id"], "case_id": case["id"], "scope": case["scope"],
                    "turn": turn_idx, "student": turn["student"],
                    "expected_for_human_review": turn.get("look_for", []),
                    "red_flags_for_human_review": turn.get("red_flags", []),
                    "critical_veto_to_review": turn.get("critical"),
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "prompt_version": "v0.7-proposed", "provider": provider}
            if provider == "dry-run":
                base.update(response=None, status="not_called", model_requested=model)
            else:
                try:
                    data = call_mistral(api_key, model, messages, max_tokens)
                    base.update(data, status="model_called", model_requested=model)
                    messages.append({"role": "assistant", "content": data["response"]})
                except Exception as exc:
                    base.update(status="api_error", error=str(exc), response=None,
                                model_requested=model)
                    yield base
                    break  # N'invente pas de tour suivant sans réponse du modèle.
            yield base


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    base = Path(__file__).resolve().parents[1]
    parser.add_argument("--suite", default=str(base / "pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json"))
    parser.add_argument("--prompt", default=str(base / "pedagogy/prompts/COACH_SYSTEM_DRAFT_V07.md"))
    parser.add_argument("--provider", choices=("dry-run", "mistral"), default="dry-run")
    parser.add_argument("--allow-billable", action="store_true", help="Autorisation explicite d'appeler l'API payante")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-cases", type=int, default=None)
    parser.add_argument("--case", action="append", help="ID à tester (répéter l'option)")
    parser.add_argument("--resource-dir", default=None)
    parser.add_argument("--max-tokens", type=int, default=520)
    parser.add_argument("--output", help="Chemin JSONL (par défaut: stdout); ne pas versionner les réponses")
    args = parser.parse_args(argv)
    if args.provider == "mistral" and not args.allow_billable:
        parser.error("Pour le modèle payant, il faut --allow-billable")
    if args.max_cases is not None and args.max_cases < 1:
        parser.error("--max-cases doit être >= 1")
    suite = cases_from_file(Path(args.suite))
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    api_key = os.environ.get("MISTRAL_API_KEY") if args.provider == "mistral" else None
    if args.provider == "mistral" and not api_key:
        parser.error("MISTRAL_API_KEY manquante; ne jamais écrire la clé dans ce script")
    resources = load_resources(args.resource_dir)
    sink = open(args.output, "w", encoding="utf-8") if args.output else sys.stdout
    try:
        records = evaluate(suite, prompt, args.provider, api_key, args.model,
                           args.max_cases, set(args.case or []), args.max_tokens, resources)
        n = 0
        for record in records:
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            n += 1
        if n == 0:
            parser.error("Aucun tour sélectionné")
    finally:
        if args.output:
            sink.close()


if __name__ == "__main__":
    main()
