from pathlib import Path
import json,time
import numpy as np
from ..methods import solve,BASELINES
from ..modifications import VARIANTS,solve_variant
from ..solver.optimal_lp import optimal
from .run_baselines import write_csv,metrics

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'results'

def generate():
    rng=np.random.default_rng(20261001); cases=[]
    for n in (3,4,5,6,10):
        for family in ('uniform','ties','skewed'):
            for k in range(20):
                C=rng.integers(1,100,(n,n)) if family=='uniform' else rng.integers(1,10,(n,n)) if family=='ties' else np.clip(np.rint(rng.lognormal(2,1.2,(n,n))),1,300).astype(int)
                s=rng.integers(5,101,n); d=1+rng.multinomial(int(s.sum())-n,rng.dirichlet(np.ones(n)))
                cases.append(dict(id=f'R{n}_{family}_{k:02}',costs=C.tolist(),supply=s.tolist(),demand=d.tolist(),kind=family))
    folder=ROOT/'datasets/generated'; folder.mkdir(exist_ok=True)
    (folder/'seed20261001.json').write_text(json.dumps(cases,indent=2)); return cases

def run(cases,random=False):
    rows=[]; traces={}; certs={}
    for k,p in enumerate(cases):
        C,s,d=p['costs'],p['supply'],p['demand']; cert=optimal(C,s,d); opt=cert['cost']; certs[p['id']]=cert
        baseline={}
        for method in BASELINES:
            start=time.perf_counter()
            try: baseline[method]=solve(C,s,d,method)
            except Exception as e: baseline[method]=dict(error=type(e).__name__+': '+str(e))
            if random:
                out=baseline[method]; row=dict(problem=p['id'],kind=p['kind'],size=len(s),method=method,role='baseline',optimal=opt,seconds=time.perf_counter()-start)
                if 'error' in out: row.update(status='failed',error=out['error'])
                else: row.update(status='ok',cost=out['cost'],**metrics(out['cost'],opt),basic=out['basic'])
                rows.append(row)
        for name,v in VARIANTS.items():
            start=time.perf_counter(); b=baseline[v['base']]; row=dict(problem=p['id'],kind=p['kind'],size=len(s),method=name,role='modified',baseline=v['base'],optimal=opt)
            try:
                out=solve_variant(C,s,d,name,trace=not random and p.get('source','').startswith('L'))
                row.update(status='ok',cost=out['cost'],baseline_cost=b['cost'],baseline_gap_pct=metrics(b['cost'],opt)['gap_pct'],improvement=b['cost']-out['cost'],**metrics(out['cost'],opt),basic=out['basic'])
                if not random: traces[p['id']+'::'+name]=out
                if (v['mode']=='rollout' and not v.get('completion') and not v.get('tie')) or v['mode']=='orientation':
                    assert row['improvement']>=-1e-7,'Same-policy rollout/portfolio guarantee violated'
            except Exception as e: row.update(status='failed',error=type(e).__name__+': '+str(e))
            row['seconds']=time.perf_counter()-start; rows.append(row)
        if (k+1)%10==0: print(f'{"Random" if random else "Published"}: {k+1}/{len(cases)}',flush=True)
    write_csv(OUT/('random_benchmark.csv' if random else 'modifications.csv'),rows)
    if not random: (OUT/'modification_allocations.json').write_text(json.dumps(traces,indent=2))
    else: (OUT/'random_optimal_certificates.json').write_text(json.dumps(certs,indent=2))

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(); parser.add_argument('--random',action='store_true'); args=parser.parse_args()
    if args.random: run(generate(),random=True)
    else: run(json.loads((ROOT/'datasets/published/benchmarks.json').read_text()))
