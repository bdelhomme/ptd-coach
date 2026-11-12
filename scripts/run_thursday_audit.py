#!/usr/bin/env python3
"""Run only the separate Thursday development suite through the frozen coach."""
import hashlib
import json
from pathlib import Path
import run_lifecycle_audit as runner
from run_coach_eval_v07 import cases_from_file

IDS=('PJ01','PJ02','PJ03')

def load_suite():
    path=runner.ROOT/'pedagogy/qa/PTD_JEUDI_AUDIT_DEV.json'
    fpath=runner.ROOT/'pedagogy/qa/PTD_JEUDI_AUDIT_FREEZE.json'
    freeze=json.loads(fpath.read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest()!=freeze['files']['pedagogy/qa/PTD_JEUDI_AUDIT_DEV.json']:
        raise ValueError('Gel des scénarios jeudi modifié')
    suite=cases_from_file(path)
    if suite.get('split')!='development' or tuple(c['id'] for c in suite['cases'])!=IDS:
        raise ValueError('Jeu de développement inattendu')
    return path,suite,hashlib.sha256(fpath.read_bytes()).hexdigest()

if __name__=='__main__':
    runner.IDS=IDS
    runner.load_suite=load_suite
    raise SystemExit(runner.main())
