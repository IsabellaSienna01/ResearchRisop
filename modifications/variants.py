"""Small preregistered experimental rules, not claims of new algorithms."""
import numpy as np
from ..methods import solve
from ..methods.common import balance,audit
from ..methods.constructive import ranked_cells,construct
from ..methods.mrm import solve_mrm

VARIANTS={
 'LCM_tie_allocation':dict(base='LCM',mode='tie',tie='allocation'),
 'VAM_tie_cost':dict(base='VAM',mode='tie',tie='cost'),
 'VAM_tie_allocation':dict(base='VAM',mode='tie',tie='allocation'),
 'VAM_penalty_sqrtA':dict(base='VAM',mode='weight',weight=.5),
 'VAM_penalty_A':dict(base='VAM',mode='weight',weight=1),
 'TDSM_theta1_5':dict(base='TDSM',mode='theta',theta=1.5),
 'LCM_top2_product':dict(base='LCM',mode='product',k=2),
 'LCM_top2_LB':dict(base='LCM',mode='lb',k=2),
 'VAM_top2_LB':dict(base='VAM',mode='lb',k=2),
 'THP_top2_LB':dict(base='THP',mode='lb',k=2),
 'LCM_top2_rollout':dict(base='LCM',mode='rollout',k=2),
 'LCM_top3_rollout':dict(base='LCM',mode='rollout',k=3),
 'VAM_top2_rollout':dict(base='VAM',mode='rollout',k=2),
 'VAM_top3_rollout':dict(base='VAM',mode='rollout',k=3),
 'THP_top2_rollout':dict(base='THP',mode='rollout',k=2),
 'THP_top3_rollout':dict(base='THP',mode='rollout',k=3),
 'THP_top2_LCMcompletion':dict(base='THP',mode='rollout',k=2,completion='LCM'),
 'VAM_top2_first_only':dict(base='VAM',mode='rollout',k=2,first_only=True),
 'THP_top2_first_only':dict(base='THP',mode='rollout',k=2,first_only=True),
 'VAM_tieA_top2_rollout':dict(base='VAM',mode='rollout',k=2,tie='allocation'),
 'MRM_orientation_ensemble':dict(base='MRM',mode='orientation'),
 'LCM_score_alpha025':dict(base='LCM',mode='score',alpha=.25,k=3),
 'LCM_score_alpha050':dict(base='LCM',mode='score',alpha=.5,k=3),
 'LCM_score_alpha075':dict(base='LCM',mode='score',alpha=.75,k=3),
}

def lower_bound(C,s,d):
    """Maximum of two admissible relaxations; summing would double-count."""
    rows=np.flatnonzero(s>1e-8); cols=np.flatnonzero(d>1e-8)
    if not len(rows): return 0.0
    sub=C[np.ix_(rows,cols)]
    return float(max(s[rows]@sub.min(axis=1),d[cols]@sub.min(axis=0)))

def solve_variant(C,s,d,name,trace=False):
    v=VARIANTS[name]; base=v['base']; mode=v['mode']; tie=v.get('tie','index')
    if mode=='tie': return solve(C,s,d,base,tie=tie,trace=trace)
    if mode=='weight': return solve(C,s,d,base,weight=v['weight'],trace=trace)
    if mode=='theta': return solve(C,s,d,base,theta=v['theta'],trace=trace)
    if mode=='orientation':
        choices=[solve_mrm(C,s,d,trace=trace,orientation=a) for a in (None,0,1)]
        return min(choices,key=lambda x:x['cost'])
    C,s0,d0,dummy=balance(C,s,d); s=s0.copy(); d=d0.copy(); X=np.zeros_like(C); steps=[]
    while s.sum()>1e-8:
        pts=ranked_cells(C,s,d,base,tie)[:v.get('k',2)]; values=[]; completions=[]
        for i,j in pts:
            q=min(s[i],d[j]); ss=s.copy(); dd=d.copy(); ss[i]-=q; dd[j]-=q; immediate=C[i,j]*q
            completion=None
            if mode=='rollout':
                completion,_=construct(C,ss,dd,v.get('completion',base),tie=tie)
                value=immediate+np.sum(C*completion)
            elif mode=='lb': value=immediate+lower_bound(C,ss,dd)
            elif mode=='product': value=immediate
            elif mode=='score': value=0.0
            else: raise ValueError(mode)
            values.append(float(value)); completions.append(completion)
        if mode=='score':
            costs=np.array([C[p] for p in pts]); alloc=np.array([min(s[i],d[j]) for i,j in pts])
            cn=(costs-costs.min())/(np.ptp(costs) or 1); an=(alloc-alloc.min())/(np.ptp(alloc) or 1)
            # Minimize costs, maximize allocations: opposite sign is intentional.
            values=(v['alpha']*cn-(1-v['alpha'])*an).tolist()
        pos=min(range(len(pts)),key=lambda k:values[k]); i,j=pts[pos]; q=min(s[i],d[j])
        X[i,j]+=q; s[i]-=q; d[j]-=q
        if trace: steps.append(dict(row=i,column=j,quantity=float(q),candidates=[list(p) for p in pts],scores=values,chosen=pos))
        if v.get('first_only'):
            X+=completions[pos]; break
    return dict(**audit(C,s0,d0,X),dummy=dummy,trace=steps)
