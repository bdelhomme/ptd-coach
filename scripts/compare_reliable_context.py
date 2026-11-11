#!/usr/bin/env python3
"""Paired synthetic development-only comparison; never opens held-out cases."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from ptd_coach.chat_config import settings
from ptd_coach.chat_context_library import LibraryContext
from ptd_coach.chat_context_reliable import ReliableContext
from ptd_coach.chat_provider import MockChatProvider
from ptd_coach.chat_provider_reasoning import MistralReasoningProvider
from compare_conversation_c2 import summarize,verify_c2_freeze
from run_coach_eval_v07 import cases_from_file
from run_conversation_eval import evaluate
from run_transversal_eval import TimedProvider,write_review


def verify_candidate_freeze():
    path=ROOT/'pedagogy/qa/RELIABILITY_CONTEXT_FREEZE.json'
    data=json.loads(path.read_text())
    for filename,expected in data['files'].items():
        if hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()!=expected:
            raise ValueError('Gel de contexte modifié : '+filename)
    verify_c2_freeze()
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider',choices=('mock','mistral'),default='mock')
    parser.add_argument('--allow-billable',action='store_true')
    parser.add_argument('--output-dir',required=True)
    args=parser.parse_args()
    if args.provider=='mistral' and not args.allow_billable: parser.error('Appels facturables non autorisés')
    freeze=verify_candidate_freeze()
    path=ROOT/'pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json'
    suite=cases_from_file(path)
    cases=[c for c in suite['cases'] if c['id'] in ('TX05','TX07','TX22')]
    if len(cases)!=3 or sum(len(c['turns']) for c in cases)!=6: raise ValueError('Jeu de développement inattendu')
    cfg=settings(ROOT)
    backend=MockChatProvider() if args.provider=='mock' else MistralReasoningProvider(cfg['MISTRAL_API_KEY'],'mistral-large-4',None,90,'medium')
    if not backend.configured: raise ValueError('Clé locale absente')
    provider=TimedProvider(backend)
    folder=Path(args.output_dir);folder.mkdir(parents=True,exist_ok=False)
    rows=[]
    with (folder/'responses.jsonl').open('x',encoding='utf-8') as out:
        for i,case in enumerate(cases):
            variants=[('bibliotheque',LibraryContext()),('fiabilite',ReliableContext())]
            if i%2: variants.reverse()
            for variant,context in variants:
                for row in evaluate(dict(suite,cases=[case]),context,provider):
                    row.update(variant=variant,messages_exact=provider.messages,freeze_sha256=freeze,
                               reasoning_effort='medium',max_tokens_requested=None)
                    out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();rows.append(row)
                    if row['status']=='api_error':
                        print('Échec API : arrêt sans nouvel essai automatique.')
                        return 1
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'provider':args.provider,'model_requested':provider.model,
            'planned_calls':12,'freeze_sha256':freeze,'parameters':{'temperature':0.2,'max_tokens':'omitted',
            'reasoning_effort':'medium','timeout_seconds':90},'summary':summarize(rows),'human_pedagogical_verdict':None,
            'limitations':['Trois cas de développement ; aucune validation indépendante.',
            'Les réponses différentes modifient les historiques au second tour.',
            'L’omission de max_tokens ne supprime pas les limites du fournisseur et du connecteur.',
            'Les blocs de raisonnement ne sont pas conservés dans l’historique.',
            'L’identité des variantes peut être reconnaissable malgré les labels.']}
    (folder/'MESURES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    write_review(folder,rows,cases)
    print(json.dumps(report,ensure_ascii=False));return 0
if __name__=='__main__':sys.exit(main())
