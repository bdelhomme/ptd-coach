#!/usr/bin/env python3
"""Three frozen contexts, development-only comparison; never opens reserved cases."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ptd_coach.chat_config import settings, provider_from_settings
from ptd_coach.chat_context import ChatContext
from ptd_coach.chat_context_v08 import ChatContextV08
from ptd_coach.chat_context_v08_c2 import ChatContextV08C2
from compare_conversation_v08 import verify_freeze
from run_coach_eval_v07 import cases_from_file
from run_conversation_eval import evaluate

VARIANTS = ('v07', 'c1', 'c2')
REVIEW_FIELDS = ('exactitude_conceptuelle', 'utilite', 'intervention_dominante',
                 'verification_utile', 'feedback', 'arret', 'autonomie', 'confidentialite',
                 'nombre_sollicitations_principales', 'citations_sollicitations', 'veto', 'commentaire', 'lecteur')
ALLOWED = ('COACH_DEV_CASES_V08.json', 'COACH_CONCEPT_CASES_C2.json', 'COACH_MULTI_TURN_CASES_V07.json')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_suite(path):
    path = Path(path).resolve()
    # Check canonical path BEFORE opening. No arbitrary copy of the held-out set.
    if path not in {(ROOT / 'pedagogy/qa' / n).resolve() for n in ALLOWED}:
        raise ValueError('Only canonical development/regression suites allowed; reserved set stays closed')
    return cases_from_file(path)


def verify_c2_freeze():
    verify_freeze()  # c1 commitment is unmodified, including its original engine.
    path = ROOT / 'pedagogy/qa/V08_C2_FREEZE.json'
    freeze = json.loads(path.read_text())
    for name, expected in freeze['files'].items():
        if digest((ROOT / name).read_bytes()) != expected:
            raise ValueError('c2 freeze mismatch: ' + name)
    return digest(path.read_bytes())


def contexts():
    return {'v07': ChatContext(), 'c1': ChatContextV08(), 'c2': ChatContextV08C2()}


class Capture:
    """Forward without copying credentials; retain only authorized model messages."""
    def __init__(self, provider):
        self.provider = provider
        for name in ('name', 'model', 'max_tokens', 'configured'):
            setattr(self, name, getattr(provider, name))
        self.messages = None

    def complete(self, messages):
        self.messages = messages
        return self.provider.complete(messages)


def collect(suite, provider=None, selected=None, variants=VARIANTS, repetition=0):
    bundles = contexts()
    wrapped = Capture(provider) if provider else None
    cases = [c for c in suite['cases'] if not selected or c['id'] in selected]
    if selected and set(selected) - {c['id'] for c in cases}:
        raise ValueError('Unknown case')
    if not variants or set(variants) - set(VARIANTS) or len(set(variants)) != len(variants):
        raise ValueError('Invalid variants')
    for index, case in enumerate(cases):
        shift = (index + repetition) % len(variants)
        order = variants[shift:] + variants[:shift]
        for variant in order:
            for row in evaluate(dict(suite, cases=[case]), bundles[variant], wrapped):
                row.update(variant=variant, repetition=repetition)
                if wrapped:
                    row['messages_exact'] = wrapped.messages
                yield row
                if row['status'] == 'api_error':
                    return


def summarize(rows):
    result = {}
    for variant in dict.fromkeys(r['variant'] for r in rows):
        group = [r for r in rows if r['variant'] == variant]
        latencies = [r['latency_ms'] for r in group if r.get('latency_ms') is not None]
        result[variant] = {'responses': sum(r['response'] is not None for r in group),
            'records': len(group), 'api_errors': sum(r['status'] == 'api_error' for r in group),
            'tokens': {k: sum(r.get('usage', {}).get(k) or 0 for r in group)
                       for k in ('prompt_tokens', 'completion_tokens', 'total_tokens')},
            'unmeasured_calls': sum(r.get('usage', {}).get('total_tokens') is None for r in group),
            'median_latency_ms': statistics.median(latencies) if latencies else None,
            'characters': sum(len(r['response'] or '') for r in group),
            'question_marks_not_solicitations': sum((r['response'] or '').count('?') for r in group),
            'truncated': sum(r.get('finish_reason') == 'length' for r in group),
            'models_returned': sorted({r['model_returned'] for r in group if r.get('model_returned')})}
    return result


def write_review(folder, rows):
    variants = list(dict.fromkeys(r['variant'] for r in rows))
    random.SystemRandom().shuffle(variants)
    labels = dict(zip(variants, 'ABC'))
    (folder / 'CLE_VARIANTES.json').write_text(json.dumps(labels, indent=2) + '\n')
    markdown = ['# Comparaison à lire avant la clé\n',
                'Messages fictifs, sorties réelles ou simulations explicitement marquées. '
                'Aucun verdict humain ; les labels peuvent être devinés par le style.\n']
    with (folder / 'GRILLE_VIERGE.csv').open('x', encoding='utf-8', newline='') as sink:
        fields = ('case_id', 'turn', 'label') + REVIEW_FIELDS
        writer = csv.DictWriter(sink, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for r in sorted(rows, key=lambda r: (r['case_id'], r['turn'], labels[r['variant']])):
            label = labels[r['variant']]
            markdown.extend([f"\n## {r['case_id']} · tour {r['turn']} · {label}\n",
                'Étudiant fictif :\n', '~~~~text\n' + r['student'] + '\n~~~~\n',
                'Réponse exacte :\n', '~~~~text\n' + (r['response'] if r['response'] is not None else '[' + r['status'] + ']') + '\n~~~~\n',
                'Attendus : ' + '; '.join(r['expected_for_human_review']) + '\n',
                'Signaux à examiner : ' + '; '.join(r['red_flags_for_human_review']) + '\n'])
            writer.writerow({'case_id': r['case_id'], 'turn': r['turn'], 'label': label})
    (folder / 'LECTURE_COMPARATIVE.md').write_text('\n'.join(markdown), encoding='utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suite', default=str(ROOT / 'pedagogy/qa/COACH_DEV_CASES_V08.json'))
    parser.add_argument('--provider', choices=('dry-run', 'mock', 'mistral'), default='dry-run')
    parser.add_argument('--allow-billable', action='store_true')
    parser.add_argument('--max-calls', type=int, default=18)
    parser.add_argument('--case', action='append')
    parser.add_argument('--variant', action='append', choices=VARIANTS)
    parser.add_argument('--repetition', type=int, default=0)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args(argv)
    if args.provider == 'mistral' and not args.allow_billable:
        parser.error('Paid API requires --allow-billable')
    suite = load_suite(args.suite)
    freeze = verify_c2_freeze()
    variants = tuple(args.variant or VARIANTS)
    selected = set(args.case or [])
    if selected - {c['id'] for c in suite['cases']} or len(set(variants)) != len(variants):
        parser.error('Unknown case or duplicate variant')
    planned = len(variants) * sum(len(c['turns']) for c in suite['cases'] if not selected or c['id'] in selected)
    if args.max_calls < 1 or args.repetition < 0 or (args.provider == 'mistral' and planned > args.max_calls):
        parser.error('Call ceiling exceeded or invalid repetition')
    config = settings(ROOT)
    if config['CHAT_MAX_TOKENS'] != 700:
        parser.error('Use CHAT_MAX_TOKENS=700 for this controlled comparison')
    provider = None
    if args.provider != 'dry-run':
        config['CHAT_PROVIDER'] = args.provider
        provider = provider_from_settings(config)
        if not provider.configured:
            parser.error('Missing local Mistral key')
    folder = Path(args.output_dir)
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    rows = []
    with (folder / 'responses.jsonl').open('x', encoding='utf-8') as sink:
        for row in collect(suite, provider, selected, variants, args.repetition):
            row.update(c2_freeze_sha256=freeze, suite_sha256=digest(Path(args.suite).read_bytes()))
            sink.write(json.dumps(row, ensure_ascii=False) + '\n')
            sink.flush()
            rows.append(row)
    report = {'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'provider': args.provider,
              'planned_calls': planned, 'mistral_attempt_ceiling': args.max_calls, 'variants': variants,
              'model_requested': provider.model if provider else None, 'c2_freeze_sha256': freeze,
              'parameters': {'max_tokens': 700, 'temperature': 0.2, 'stream': False, 'tool_choice': 'none',
                             'timeout_seconds': config['CHAT_TIMEOUT_SECONDS']},
              'summary': summarize(rows), 'human_pedagogical_verdict': None, 'currency_cost': None,
              'limitations': ['Development only; no held-out evaluation', 'Moving model alias',
                              'Fixed student continuations with different assistant histories',
                              'Question marks are not counts of pedagogical requests',
                              'Technical and descriptive measurements are not student scores']}
    (folder / 'MESURES.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    write_review(folder, rows)
    print(json.dumps(report, ensure_ascii=False))
    return int(any(r['status'] == 'api_error' for r in rows))


if __name__ == '__main__':
    sys.exit(main())
