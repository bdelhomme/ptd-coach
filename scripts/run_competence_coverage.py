#!/usr/bin/env python3
"""D-037: frozen coach on 12 preselected fictional development situations."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from ptd_coach.chat_config import settings
from ptd_coach.chat_context_reliable import ReliableContext
from ptd_coach.chat_provider import MockChatProvider
from ptd_coach.chat_provider_reasoning import MistralReasoningProvider
from compare_reliable_context import verify_candidate_freeze
from compare_conversation_c2 import summarize
from run_coach_eval_v07 import cases_from_file
from run_conversation_eval import evaluate
from run_transversal_eval import TimedProvider,write_review

SELECTED=('TX02','TX03','TX04','TX08','TX10','TX13','TX15','TX16','TX17','TX18','TX21','TX23')
COMPETENCIES={'A1','A2','A3','B1','B2','B3','C1','C2','D1','D2','D3'}

def load_cases():
    # This exact development path is the only suite opened by this runner.
    path=ROOT/'pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json'
    suite=cases_from_file(path)
    if suite.get('split')!='development':raise ValueError('Jeu de développement attendu')
    cases=[c for c in suite['cases'] if c['id'] in SELECTED]
    if (tuple(c['id'] for c in cases)!=SELECTED or sum(len(c['turns']) for c in cases)!=24 or
        {code for c in cases for code in c['competencies']}!=COMPETENCIES):
        raise ValueError('Plan de couverture inattendu')
    return path,suite,cases

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider',choices=('mock','mistral'),default='mock')
    parser.add_argument('--allow-billable',action='store_true')
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--case',choices=SELECTED,action='append',help='Sélection explicite de cas de développement')
    args=parser.parse_args(argv)
    if args.provider=='mistral' and not args.allow_billable: parser.error('Appels facturables non autorisés')
    freeze=verify_candidate_freeze()
    path,suite,cases=load_cases()
    if args.case:
        if len(set(args.case)) != len(args.case): raise ValueError('Cas répété')
        cases=[c for c in cases if c['id'] in args.case]
    planned=sum(len(c['turns']) for c in cases)
    config=settings(ROOT)
    backend=MockChatProvider() if args.provider=='mock' else MistralReasoningProvider(config['MISTRAL_API_KEY'],'mistral-large-4',None,90,'medium')
    if not backend.configured:raise ValueError('Clé locale absente')
    provider=TimedProvider(backend)
    context=ReliableContext()
    folder=Path(args.output_dir);folder.mkdir(parents=True,exist_ok=False)
    rows=[];failed=False
    with (folder/'responses.jsonl').open('x',encoding='utf-8') as sink:
        for case in cases:
            for row in evaluate(dict(suite,cases=[case]),context,provider):
                row.update(variant='fiabilite',messages_exact=provider.messages,freeze_sha256=freeze,
                           suite_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                           reasoning_effort='medium',max_tokens_requested=None)
                if row['status']=='api_error':row['elapsed_ms_including_failure']=provider.elapsed_ms
                sink.write(json.dumps(row,ensure_ascii=False)+'\n');sink.flush();rows.append(row)
                if row['status']=='api_error':failed=True;break
            if failed:break
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'provider':args.provider,
      'model_requested':provider.model,'freeze_sha256':freeze,'selected_cases':[c['id'] for c in cases],
      'planned_calls':planned,'attempted_calls':len(rows),'completed_calls':sum(r['response'] is not None for r in rows),
      'stopped_on_error':failed,'parameters':{'temperature':0.2,'max_tokens':'omitted','reasoning_effort':'medium','timeout_seconds':90},
      'summary':summarize(rows),'human_pedagogical_verdict':None,
      'limitations':['Cas fictifs de développement, ni examen indépendant ni test de transfert.',
       'Correspondances compétences proposées ; une réponse ne démontre pas un apprentissage.',
       'Plafonds du fournisseur et du connecteur, délai réseau et absence des blocs de raisonnement dans l’historique.',
       'Arrêt à la première erreur, sans reprise automatique ; facturation de l’appel en erreur inconnue.']}
    (folder/'MESURES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    write_review(folder,rows,cases)
    print(json.dumps(report,ensure_ascii=False));return int(failed)
if __name__=='__main__':sys.exit(main())
