"""Exhaust all allowed arbitrary choices on selected small mismatches."""
from functools import lru_cache
from pathlib import Path
import json
import numpy as np
from ..methods.common import balance
from .run_baselines import write_csv

def costs(C,s,d,method,limit=100000):
    C,s,d,_=balance(C,s,d); states=0
    @lru_cache(None)
    def visit(st,dt):
        nonlocal states
        states+=1
        if states>limit: raise RuntimeError('Enumeration limit; result would be incomplete')
        rs=[i for i,v in enumerate(st) if v]; cs=[j for j,v in enumerate(dt) if v]
        if not rs: return frozenset([0])
        if method=='LCM':
            low=min(C[i,j] for i in rs for j in cs)
            pts={(i,j) for i in rs for j in cs if C[i,j]==low}
        else:
            lines=[]
            for axis in ([0] if method in {'TDM1','TDSM'} else [0,1]):
                for k in (rs if axis==0 else cs):
                    pts=[(k,j) for j in cs] if axis==0 else [(i,k) for i in rs]
                    a=sorted(C[p] for p in pts)
                    score=(a[1]-a[0] if len(a)>1 else 0) if method=='VAM' else sum((x-a[0])**(2 if method=='TDSM' else 1) for x in a)
                    lines.append((score,[p for p in pts if C[p]==a[0]]))
            best=max(score for score,_ in lines); pts={p for score,pp in lines if score==best for p in pp}
        out=set()
        for i,j in pts:
            q=min(st[i],dt[j]); ss=list(st); dd=list(dt); ss[i]-=q; dd[j]-=q
            out.update(q*C[i,j]+z for z in visit(tuple(ss),tuple(dd)))
        return frozenset(out)
    result=visit(tuple(s),tuple(d))
    return sorted(result),states

def main():
    root=Path(__file__).resolve().parents[1]; ps={p['id']:p for p in json.loads((root/'datasets/published/occurrences.json').read_text())}
    checks=[('L04_Example1','LCM'),('L04_Example2','LCM'),('E01_Example2','TDM1'),('E01_Example5','TDSM'),('E01_Example6','TDM1'),('E01_Example7','TDM1')]
    rows=[]
    for key,method in checks:
        p=ps[key]; row=dict(problem=key,method=method,published=p['claims'][method])
        try:
            zs,n=costs(p['costs'],p['supply'],p['demand'],method)
            row.update(status='exhaustive',reachable=json.dumps(zs),states=n,published_reachable=p['claims'][method] in zs)
        except RuntimeError as e: row.update(status=str(e))
        rows.append(row)
    write_csv(root/'results/tie_enumeration.csv',rows)
    print(json.dumps(rows,indent=2))

if __name__=='__main__': main()
