"""Deterministic, explicitly named completions of published selection rules.

Unspecified ties use row-before-column then increasing indices. LDVAM applies
the supplied paper's extra minimum-cost line tie. TDSM uses theta=2 by default.
"""
import numpy as np
from .common import balance, audit

def ranked_cells(C,s,d,method='VAM',tie='index',weight=0,theta=2):
    rows=np.flatnonzero(s>1e-9); cols=np.flatnonzero(d>1e-9)
    if not len(rows) or not len(cols): return []
    cells=[(int(i),int(j)) for i in rows for j in cols]
    if method=='NWCM': return cells
    def ck(ij):
        i,j=ij
        return (C[i,j],-min(s[i],d[j]) if tie=='allocation' else 0,i,j)
    if method=='LCM': return sorted(cells,key=ck)
    if method=='RAM':
        u={i:max(C[i,cols]) for i in rows}; v={j:max(C[rows,j]) for j in cols}
        return sorted(cells,key=lambda p:(C[p]-u[p[0]]-v[p[1]],-min(s[p[0]],d[p[1]]) if tie=='allocation' else 0,*p))
    lines=[]
    axes=(0,) if method in {'TDM1','TDSM'} else (0,1)
    for axis in axes:
        for idx in (rows if axis==0 else cols):
            pts=[(int(idx),int(j)) for j in cols] if axis==0 else [(int(i),int(idx)) for i in rows]
            a=np.sort([C[p] for p in pts]); least=[p for p in pts if C[p]==a[0]]
            least.sort(key=lambda p:(-min(s[p[0]],d[p[1]]) if tie=='allocation' else 0,*p))
            if method in {'VAM','LDVAM'}: penalty=a[1]-a[0] if len(a)>1 else 0.0
            elif method=='THP': penalty=a[-1]-a[0]
            elif method in {'TDM1','TDM2'}: penalty=float(sum(a-a[0]))
            elif method=='TDSM': penalty=float(sum((a-a[0])**theta))
            else: raise ValueError(f'Unknown constructive method {method}')
            if weight: penalty*=min(s[least[0][0]],d[least[0][1]])**weight
            line_key=(-penalty,a[0] if method=='LDVAM' or tie=='cost' else 0,
                      -min(s[least[0][0]],d[least[0][1]]) if tie=='allocation' else 0,axis,int(idx))
            lines.append((line_key,penalty,least))
    lines.sort(key=lambda v:v[0])
    if method=='THP':
        levels=sorted({p for _,p,_ in lines},reverse=True)[:2]
        eligible={p for _,v,ps in lines if v in levels for p in ps}
        return sorted(eligible,key=lambda p:(C[p]*min(s[p[0]],d[p[1]]),C[p],*p))
    seen=set(); ordered=[]
    for _,_,pts in lines:
        # A line contributes its selected cheapest cell; remaining equal minima
        # are alternatives only after the canonical cell, preserving baseline.
        for p in pts:
            if p not in seen: ordered.append(p); seen.add(p)
    return ordered

def construct(C,s,d,method='VAM',tie='index',weight=0,theta=2,trace=False):
    s=s.copy(); d=d.copy(); X=np.zeros_like(C); steps=[]
    while s.sum()>1e-8:
        candidates=ranked_cells(C,s,d,method,tie,weight,theta)
        if not candidates: raise RuntimeError('No candidate with remaining mass')
        i,j=candidates[0]; q=min(s[i],d[j]); X[i,j]+=q; s[i]-=q; d[j]-=q
        if trace: steps.append(dict(row=i,column=j,quantity=float(q),unit_cost=float(C[i,j])))
    return X,steps

def solve_constructive(C,s,d,method='VAM',**kwargs):
    C,s,d,dummy=balance(C,s,d)
    X,steps=construct(C,s,d,method,**kwargs)
    return dict(**audit(C,s,d,X),dummy=dummy,trace=steps)
