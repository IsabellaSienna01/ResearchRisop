"""Wireko et al. 2025 narrative MRM, with orientation frozen at first choice.

Equal supply/demand: remove selected orientation only (section 3.1); zero
residual lines remain until selected. Worked UTP3 uses a different tie removal.
"""
import numpy as np
from .common import balance,audit

def solve_mrm(C,s,d,trace=False,orientation=None):
    C,s0,d0,dummy=balance(C,s,d); s=s0.copy(); d=d0.copy(); X=np.zeros_like(C)
    rows=list(np.flatnonzero(s>0)); cols=list(np.flatnonzero(d>0)); steps=[]
    axis=orientation
    if axis is None and dummy: axis=0 if dummy[0]=='row' else 1
    while rows and cols and s.sum()>1e-8:
        lines=[]
        for a in ([axis] if axis is not None else [0,1]):
            for k in (rows if a==0 else cols):
                pts=[(int(k),int(j)) for j in cols] if a==0 else [(int(i),int(k)) for i in rows]
                p=min(pts,key=lambda ij:(C[ij],*ij)); vals=[C[ij] for ij in pts]
                lines.append((-(max(vals)-min(vals)),min(vals),a,int(k),p))
        _,_,a,k,(i,j)=min(lines); axis=a
        si,dj=s[i],d[j]; q=min(si,dj); X[i,j]+=q; s[i]-=q; d[j]-=q
        if si<dj: rows.remove(i)
        elif dj<si: cols.remove(j)
        elif axis==0: rows.remove(i)
        else: cols.remove(j)
        if trace: steps.append(dict(row=i,column=j,quantity=float(q),orientation=axis))
    return dict(**audit(C,s0,d0,X),dummy=dummy,trace=steps,orientation=axis)
