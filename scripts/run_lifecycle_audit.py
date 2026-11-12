#!/usr/bin/env python3
"""Fictional PTD lifecycle development audit; never opens held-out cases."""
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

IDS=tuple('PV%02d'%i for i in range(1,15))

def load_suite():
    path=ROOT/'pedagogy/qa/PTD_LIFECYCLE_AUDIT_DEV.json'
    fpath=ROOT/'pedagogy/qa/PTD_LIFECYCLE_AUDIT_FREEZE.json'
    freeze=json.loads(fpath.read_text())
    expected=freeze['files']['pedagogy/qa/PTD_LIFECYCLE_AUDIT_DEV.json']
    if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:raise ValueError('Gel des scénarios modifié')
    suite=cases_from_file(path)
    if suite.get('split')!='development' or tuple(c['id'] for c in suite['cases'])!=IDS:raise ValueError('Jeu de développement inattendu')
    return path,suite,hashlib.sha256(fpath.read_bytes()).hexdigest()

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider',choices=('mock','mistral'),default='mock')
    parser.add_argument('--allow-billable',action='store_true')
    parser.add_argument('--case',choices=IDS,action='append')
    parser.add_argument('--output-dir',required=True)
    args=parser.parse_args(argv)
    if args.provider=='mistral' and not args.allow_billable:parser.error('Appels facturables non autorisés')
    if args.case and len(args.case)!=len(set(args.case)):parser.error('Cas répété')
    candidate_freeze=verify_candidate_freeze();path,suite,scenario_freeze=load_suite()
    cases=[c for c in suite['cases'] if not args.case or c['id'] in args.case]
    planned=sum(len(c['turns']) for c in cases)
    if planned>28:raise ValueError('Plan d’appels dépassé')
    cfg=settings(ROOT)
    backend=MockChatProvider() if args.provider=='mock' else MistralReasoningProvider(cfg['MISTRAL_API_KEY'],'mistral-large-4',None,90,'medium')
    if not backend.configured:raise ValueError('Clé locale absente')
    provider=TimedProvider(backend);context=ReliableContext()
    folder=Path(args.output_dir);folder.mkdir(parents=True,exist_ok=False)
    rows=[];failed=False
    with (folder/'responses.jsonl').open('x',encoding='utf-8') as sink:
        for case in cases:
            for row in evaluate(dict(suite,cases=[case]),context,provider):
                row.update(variant='fiabilite',messages_exact=provider.messages,candidate_freeze_sha256=candidate_freeze,
                           scenario_freeze_sha256=scenario_freeze,suite_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                           reasoning_effort='medium',max_tokens_requested=None)
                if row['status']=='api_error':row['elapsed_ms_including_failure']=provider.elapsed_ms
                sink.write(json.dumps(row,ensure_ascii=False)+'\n');sink.flush();rows.append(row)
                if row['status']=='api_error':failed=True;break
            if failed:break
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'provider':args.provider,'model_requested':provider.model,
       'candidate_freeze_sha256':candidate_freeze,'scenario_freeze_sha256':scenario_freeze,
       'selected_cases':[c['id'] for c in cases],'planned_calls':planned,'attempted_calls':len(rows),
       'completed_calls':sum(r['response'] is not None for r in rows),'stopped_on_error':failed,
       'parameters':{'temperature':0.2,'max_tokens':'omitted','reasoning_effort':'medium','timeout_seconds':90},
       'summary':summarize(rows),'human_pedagogical_verdict':None,
       'limitations':['Scénarios fictifs de développement écrits après le cadrage ; pas de validation indépendante.',
       'Une réponse ne prouve ni une compétence ni un transfert ; pas de notation étudiante.',
       'Raisonnement non conservé ; limites du fournisseur, de taille de réponse et du délai réseau.',
       'Arrêt au premier échec sans retry automatique ; facturation de l’appel en échec inconnue.']}
    (folder/'MESURES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    write_review(folder,rows,cases)
    print(json.dumps(report,ensure_ascii=False));return int(failed)
if __name__=='__main__':sys.exit(main())
