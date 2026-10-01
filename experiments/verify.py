"""Independent small-network checks, published anchors, and rollout invariants."""
import itertools,json
from pathlib import Path
import numpy as np
from ..methods import solve
from ..methods.common import balance,audit
from ..modifications import solve_variant
from ..modifications.variants import lower_bound
from ..solver.optimal_lp import optimal

def brute(C,s,d):
    m,n=C.shape; best=float('inf')
    def search(k,ss,dd,z):
        nonlocal best
        if k==m*n:
            if not any(ss) and not any(dd): best=min(best,z)
            return
        i,j=divmod(k,n)
        for q in range(min(ss[i],dd[j])+1):
            ss[i]-=q; dd[j]-=q; search(k+1,ss,dd,z+q*C[i,j]); ss[i]+=q; dd[j]+=q
    search(0,list(s),list(d),0); return best

def main():
    rng=np.random.default_rng(1818); checked=0
    for k in range(24):
        C=rng.integers(0,10,(3,3)); s=rng.integers(1,4,3); d=rng.multinomial(int(s.sum()),[1/3]*3)
        opt=optimal(C,s,d)['cost']; assert abs(brute(C,s,d)-opt)<1e-7
        assert lower_bound(C,s,d)<=opt+1e-7
        for base in ['LCM','VAM','THP']:
            b=solve(C,s,d,base)
            for top in [2,3]:
                r=solve_variant(C,s,d,f'{base}_top{top}_rollout')
                assert r['basic'] and opt-1e-7<=r['cost']<=b['cost']+1e-7
        checked+=1
    root=Path(__file__).resolve().parents[1]
    cases={p['id']:p for p in json.loads((root/'datasets/published/occurrences.json').read_text())}
    anchors=[('L01_Table2','BCE',435),('L03_Table2','SSM',465),('L02_Table3','RBSM',111),('L02_Table7','RBSM',7750),('E11_Table3','CSM',1780),
             ('L05_Example1','THP',1045),('L05_Example2','THP',4525),('L05_Example3','THP',2366)]
    for i in range(1,11): anchors.append((f'MRM_BTP{i}','MRM',cases[f'MRM_BTP{i}']['claims']['MRM']))
    for i in range(1,4): anchors.append((f'MRM_UTP{i}','MRM',cases[f'MRM_UTP{i}']['claims']['MRM']))
    for key,method,z in anchors:
        p=cases[key]; assert solve(p['costs'],p['supply'],p['demand'],method)['cost']==z,(key,method)
    degenerate=solve([[1,5],[5,1]],[3,3],[3,3],'LCM')
    assert degenerate['degenerate'] and len(degenerate['basis'])==3
    # Positive-support cycle is feasible but not basic; do not silently call it IBFS.
    assert not audit(np.ones((2,2)),np.array([2,2]),np.array([2,2]),np.ones((2,2)))['basic']
    for s,d in [([2,3],[1,1]),([1,1],[2,3])]:
        for base in ['LCM','VAM','THP','MRM']:
            assert solve([[1,3],[4,2]],s,d,base)['feasible']
    msg=f'PASS: {checked} exhaustive 3x3 LP comparisons; {len(anchors)} published anchors; rollout dominance, lower bounds, degeneracy, cycles, both dummy directions.'
    (root/'results/verification.txt').write_text(msg+'\n',encoding='utf-8'); print(msg)

if __name__=='__main__': main()
