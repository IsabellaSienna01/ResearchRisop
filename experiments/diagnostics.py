"""Exploratory audits after initial reproduction: tie and unit sensitivity."""
from pathlib import Path
import json
import numpy as np
from ..methods import solve
from .run_baselines import write_csv

ROOT=Path(__file__).resolve().parents[1]
def main():
    cases=json.loads((ROOT/'datasets/published/benchmarks.json').read_text()); rows=[]
    for p in cases:
        if max(len(p['supply']),len(p['demand']))>6: continue
        C=np.asarray(p['costs']); s=p['supply']; d=p['demand']
        for method in ['LCM','VAM','RAM','THP','TDM1','TDSM','SSM','BCE','CSM','RBSM']:
            for scale in [1,10]:
                try:
                    out=solve(C*scale,s,d,method)
                    rows.append(dict(problem=p['id'],method=method,scale=scale,status='ok',cost_original_units=out['cost']/scale))
                except Exception as e: rows.append(dict(problem=p['id'],method=method,scale=scale,status='failed',error=str(e)))
    write_csv(ROOT/'results/currency_sensitivity.csv',rows)
    ties=[]
    for p in cases:
        if not p['id'].startswith(('L04','E01')): continue
        for method in ['LCM','VAM','TDM1','TDSM']:
            for tie in ['index','cost','allocation']:
                out=solve(p['costs'],p['supply'],p['demand'],method,tie=tie)
                ties.append(dict(problem=p['id'],method=method,tie=tie,cost=out['cost']))
    write_csv(ROOT/'results/tie_diagnostics.csv',ties)
    print('Saved currency and tie diagnostics; these do not alter published baselines.')

if __name__=='__main__': main()
