#!/usr/bin/env python3
"""High reasoning, no requested output token cap, on canonical development cases only."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ptd_coach.chat_config import settings
from ptd_coach.chat_context_v08_c2 import ChatContextV08C2
from ptd_coach.chat_context_library import LibraryContext
from ptd_coach.chat_provider_reasoning import MistralReasoningProvider
from ptd_coach.chat_provider import MockChatProvider
from compare_library import ForcedLibrary
from compare_conversation_c2 import verify_c2_freeze, summarize
from run_conversation_eval import evaluate
from run_coach_eval_v07 import cases_from_file
from run_transversal_eval import TimedProvider, write_review


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider',choices=('mock','mistral'),default='mock')
    parser.add_argument('--allow-billable',action='store_true')
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--effort',choices=('low','medium','high'),default='high')
    parser.add_argument('--timeout',type=int,default=60)
    parser.add_argument('--case',choices=('TX05','TX07'),action='append')
    parser.add_argument('--variant',choices=('c2','resource_forced','library_contextual'),action='append')
    args=parser.parse_args()
    if args.provider=='mistral' and not args.allow_billable:
        parser.error('Une autorisation explicite des appels facturables est nécessaire.')
    path=ROOT/'pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json'
    suite=cases_from_file(path)
    cases=[c for c in suite['cases'] if c['id'] in ('TX05','TX07')]
    if len(cases)!=2 or sum(len(c['turns']) for c in cases)!=4:
        raise ValueError('Scénarios de développement canoniques inattendus')
    cases=[c for c in cases if not args.case or c['id'] in args.case]
    wanted=set(args.variant or ('c2','resource_forced','library_contextual'))
    planned=len(wanted)*sum(len(c['turns']) for c in cases)
    freeze=verify_c2_freeze()
    config=settings(ROOT)
    backend=MockChatProvider() if args.provider=='mock' else MistralReasoningProvider(
        config['MISTRAL_API_KEY'],'mistral-large-4',None,args.timeout,args.effort)
    if not backend.configured: raise ValueError('Clé Mistral locale absente')
    provider=TimedProvider(backend)
    folder=Path(args.output_dir);folder.mkdir(parents=True,exist_ok=False)
    rows=[]
    with (folder/'responses.jsonl').open('x',encoding='utf-8') as out:
        for case in cases:
            variants=[('c2',ChatContextV08C2()),('resource_forced',ForcedLibrary('M06' if case['id']=='TX05' else 'M03')),('library_contextual',LibraryContext())]
            for variant,context in variants:
                if variant not in wanted: continue
                for row in evaluate(dict(suite,cases=[case]),context,provider):
                    row.update(variant=variant,messages_exact=provider.messages,c2_freeze_sha256=freeze,
                        suite_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),reasoning_effort=args.effort,
                        max_tokens_requested=None)
                    out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();rows.append(row)
                    if row['status']=='api_error':
                        print('Échec API : arrêt sans nouvel essai automatique.')
                        return 1
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'provider':args.provider,
        'model_requested':provider.model,'planned_calls':planned,
        'parameters':{'temperature':0.2,'max_tokens':'omitted','reasoning_effort':args.effort,'timeout_seconds':args.timeout},
        'summary':summarize(rows),'human_pedagogical_verdict':None,
        'limitations':['Deux scénarios fictifs de développement, 12 appels maximum.',
          'Les limites du fournisseur et le délai réseau subsistent ; aucune limite de tokens n’est fixée dans la requête.',
          'Les blocs thinking ne sont pas conservés dans l’historique ; Mistral avertit d’une possible perte de qualité multitour.',
          'Limite de taille technique du connecteur et taille maximale de réponse affichable : 30 000 caractères.',
          'Une seule répétition ; conditions et historiques diffèrent des comparaisons historiques.']}
    (folder/'MESURES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    write_review(folder,rows,cases)
    print(json.dumps(report,ensure_ascii=False));return 0
if __name__=='__main__':sys.exit(main())
