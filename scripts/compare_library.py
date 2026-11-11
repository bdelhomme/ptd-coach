#!/usr/bin/env python3
"""Bounded synthetic comparison on TX05/TX07; never opens held-out cases."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ptd_coach.chat_context_v08_c2 import ChatContextV08C2
from ptd_coach.chat_context_library import LibraryContext
from ptd_coach.chat_config import settings, provider_from_settings
from run_conversation_eval import evaluate
from run_coach_eval_v07 import cases_from_file
from run_transversal_eval import TimedProvider, write_review
from compare_conversation_c2 import verify_c2_freeze, summarize

class ForcedLibrary(LibraryContext):
    version = 'conversation-v08-c2-library-forced-eval-only'
    def __init__(self, resource_id):
        super().__init__()
        self.resource_id = resource_id
    def select_resources(self, message, history):
        return [resource for resource in self.resources if resource['id'] == self.resource_id]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider', choices=('mock','mistral'), default='mock')
    parser.add_argument('--allow-billable', action='store_true')
    parser.add_argument('--output-dir', required=True)
    args=parser.parse_args()
    if args.provider == 'mistral' and not args.allow_billable:
        parser.error('Mistral requires --allow-billable')
    path=ROOT/'pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json'
    suite=cases_from_file(path)
    cases=[case for case in suite['cases'] if case['id'] in ('TX05','TX07')]
    assert len(cases)==2 and sum(len(c['turns']) for c in cases)==4
    freeze=verify_c2_freeze()
    config=settings(ROOT); config['CHAT_PROVIDER']=args.provider
    if config['CHAT_MAX_TOKENS'] != 700: raise ValueError('max_tokens=700 required')
    provider=TimedProvider(provider_from_settings(config))
    if not provider.configured: raise ValueError('Provider not configured')
    folder=Path(args.output_dir); folder.mkdir(parents=True, exist_ok=False)
    rows=[]
    with (folder/'responses.jsonl').open('x',encoding='utf-8') as out:
        for case in cases:
            variants=[('c2', ChatContextV08C2()), ('resource_forced',ForcedLibrary('M06' if case['id']=='TX05' else 'M03')),('library_contextual',LibraryContext())]
            for variant, context in variants:
                for row in evaluate(dict(suite,cases=[case]),context,provider):
                    row.update(variant=variant,messages_exact=provider.messages,c2_freeze_sha256=freeze,
                               suite_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
                    out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();rows.append(row)
                    if row['status']=='api_error':
                        print('API error; stopped without retry');return 1
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'provider':args.provider,'model_requested':provider.model,
            'planned_calls':12,'parameters':{'temperature':0.2,'max_tokens':700},'summary':summarize(rows),
            'human_pedagogical_verdict':None,'limitations':['Développement uniquement ; deux scénarios, continuations fixées.',
            'Alias de modèle évolutif ; la version forcée diffère aussi du contexte c2 de base.',
            'La qualité et la substitution exigent une revue humaine ; longueur et fluidité ne démontrent pas un progrès.']}
    (folder/'MESURES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    write_review(folder,rows,cases)
    print(json.dumps(report,ensure_ascii=False))
    return 0
if __name__=='__main__': sys.exit(main())
