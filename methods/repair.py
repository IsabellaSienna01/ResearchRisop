"""Demand-first repair interpretations; all nonprescribed ties are documented.

SSM/CSM/RBSM use a shortage receiver, treating satisfied rows as crossed out.
CSM follows numbered narrative, NOT the conflicting Figure 3 priority pseudocode.
RBSM follows numbered narrative, NOT the inconsistent downloadable C++ code.
BCE is a balanced-only interpretation: non-satisfied receiver including excess
rows; signed differences. These are qualified implementations, not proof that
every published result follows these tie completions.
"""
import numpy as np
from .common import balance,audit

def solve_repair(C,s,d,method,trace=False):
    if method=='BCE' and sum(s)!=sum(d):
        raise NotImplementedError('BCE unbalanced branch/model not sufficiently unambiguous; no dummy substitution')
    C,s,d,dummy=balance(C,s,d); m,n=C.shape; X=np.zeros_like(C)
    tc=C.sum(axis=1); cs=tc*s; steps=[]
    def rowkey(i,j): return (C[i,j],-tc[i] if method in {'CSM','RBSM'} else 0,i)
    for j in range(n): X[min(range(m),key=lambda i:rowkey(i,j)),j]=d[j]
    seen=set()
    for iteration in range(10000):
        state=X.tobytes()
        if state in seen: raise RuntimeError('Repair cycle; no fallback or forced feasibility applied')
        seen.add(state)
        total=X.sum(axis=1); excess=total-s; donors=np.flatnonzero(excess>1e-8)
        if not len(donors):
            return dict(**audit(C,s,d,X),dummy=dummy,trace=steps,iterations=iteration)
        candidates=[]
        for i in donors:
            for j in np.flatnonzero(X[i]>1e-8):
                receivers=[r for r in range(m) if r!=i and (abs(excess[r])>1e-8 if method=='BCE' else excess[r]<-1e-8)]
                if not receivers: continue
                r=min(receivers,key=lambda r:rowkey(r,j))
                diff=C[r,j]-C[i,j]
                if method!='BCE': diff=abs(diff)
                if method=='SSM':
                    if s[i]==s[r]:
                        target=i if X[i,j]>=excess[i] else r if X[i,j]>=-excess[r] else None
                    elif len(donors)==1: target=i if s[i]<s[r] else r
                    else: target=i if s[i]>s[r] else r
                elif method=='CSM': target=i if s[i]==s[r] or cs[i]>cs[r] else r
                elif method=='RBSM': target=i if s[i]==s[r] or C[i,j]*s[i]>C[r,j]*s[r] else r
                else:
                    if C[i,j]==C[r,j]: target=i if tc[i]>tc[r] else None
                    elif s[i]==s[r] or excess[r]>0: target=i
                    elif abs(s[i]-s[r]) % diff != 0 or tc[i]>tc[r]: target=i
                    else: target=r
                q=min(X[i,j],excess[i] if target==i else -excess[r]) if target is not None else X[i,j]
                if q<=0: continue
                if method=='SSM': key=(diff,-X[i,j],int(i),int(j),int(r))
                elif method in {'CSM','RBSM'}: key=(diff,q*C[r,j],C[i,j],int(i),int(j),int(r))
                else: key=(diff,int(i),int(j),int(r))
                candidates.append((key,int(i),int(j),int(r),float(q),target))
        if not candidates: raise RuntimeError('No admissible transfer under extracted rules')
        key,i,j,r,q,target=min(candidates,key=lambda t:t[0])
        X[i,j]-=q; X[r,j]+=q
        if trace: steps.append(dict(donor=i,receiver=r,column=j,quantity=q,priority_row=None if target is None else int(target),difference=float(key[0])))
    raise RuntimeError('Repair iteration limit; no fallback applied')
