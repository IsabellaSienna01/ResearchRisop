from pathlib import Path
import json,time,csv
import numpy as np
from ..methods.common import balance,audit
from ..methods import solve,BASELINES
from ..solver.optimal_lp import optimal

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)

def write_csv(path,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(rows)

def metrics(z,opt):
    if z<opt-1e-6: raise ValueError('Heuristic below certified optimum')
    return dict(gap=z-opt,gap_pct=100*(z-opt)/opt if opt else (0 if not z else None),
                accuracy=100*opt/z if z else 100,optimal_hit=abs(z-opt)<1e-6)

def main():
    cases=json.loads((ROOT/'datasets/published/benchmarks.json').read_text())
    occurrences=json.loads((ROOT/'datasets/published/occurrences.json').read_text())
    rows=[]; certificates={}; allocations={}; byhash={}
    for k,p in enumerate(cases):
        C,s,d=p['costs'],p['supply'],p['demand']; opt=optimal(C,s,d); certificates[p['id']]=opt; byhash[p['sha256']]={}
        for method in BASELINES:
            start=time.perf_counter(); row=dict(problem=p['id'],source=p['source'],kind=p['kind'],method=method,optimal=opt['cost'])
            try:
                out=solve(C,s,d,method,trace=p['source'].startswith('L'))
                row.update(cost=out['cost'],**metrics(out['cost'],opt['cost']),basic=out['basic'],degenerate=out['degenerate'],status='ok')
                allocations[p['id']+'::'+method]=out
            except Exception as e: row.update(status='failed',error=type(e).__name__+': '+str(e))
            row['seconds']=time.perf_counter()-start; rows.append(row); byhash[p['sha256']][method]=row
        if (k+1)%10==0: print(f'Completed {k+1}/{len(cases)} benchmarks',flush=True)
    reproduction=[]
    for p in occurrences:
        available=byhash[p['sha256']]; opt=next(iter(available.values()))['optimal']
        for method,published in p['claims'].items():
            row=dict(occurrence=p['id'],source=p['source'],locator=p['locator'],method=method,published_cost=published)
            r=available.get(method)
            if method=='optimal': row.update(reproduced_cost=opt,match=abs(published-opt)<1e-6,status='LP verified')
            elif method=='AIP_worked':
                C,s,d,_=balance(p['costs'],p['supply'],p['demand'])
                z=audit(C,s,d,np.array(p['worked_allocation']))['cost']
                row.update(reproduced_cost=z,match=abs(published-z)<1e-6,status='Published allocation audited; not a general algorithm reproduction')
            elif r and r['status']=='ok': row.update(reproduced_cost=r['cost'],match=abs(published-r['cost'])<1e-6,status='qualified deterministic implementation')
            else: row.update(status=r['error'] if r else 'method not implemented / worked allocation claim')
            reproduction.append(row)
    write_csv(OUT/'baseline.csv',rows); write_csv(OUT/'reproduction.csv',reproduction)
    (OUT/'optimal_certificates.json').write_text(json.dumps(certificates,indent=2))
    (OUT/'baseline_allocations.json').write_text(json.dumps(allocations,indent=2))
    print(f'Saved {len(rows)} baseline runs and {len(reproduction)} source claim comparisons')

if __name__=='__main__': main()
