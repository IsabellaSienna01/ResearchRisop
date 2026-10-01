"""Restricted JHM audit, NOT a reconstruction of the inaccessible full 2015 method.

Verified domain: demand-first initialization has at most one excess row.
Multiple-excess dependency/third-cost selection is deliberately unsupported.
Sources: original publisher description; Indrawan et al. 2021 theorem 4.2 and
worked discussion; supplied BCE paper's JHM allocations and discussion.
Remaining equal-cost choices use lowest indices, an explicit convention.
"""
import numpy as np
from .common import balance, audit


class UnverifiedJHMBranch(NotImplementedError):
    pass


def solve_jhm(C, s, d, variant='baseline', trace=False, tie_rule='higher_donor_cost'):
    allowed={'baseline','cap_receiver','net_tie','cap_net_tie','top2_completion'}
    if variant not in allowed:
        raise ValueError(variant)
    if tie_rule not in {'higher_donor_cost','index'}:
        raise ValueError(tie_rule)
    # Use the common validator, but defer a dummy destination until the end:
    # original JHM does not use this column during supply-surplus construction.
    C,s,d,dummy=balance(C,s,d)
    if dummy and dummy[0]=='column':
        C=C[:,:-1]; d=d[:-1]
    m,n=C.shape
    X=np.zeros_like(C)
    for j in range(n):
        X[int(np.argmin(C[:,j])),j]=d[j]
    if np.count_nonzero(X.sum(axis=1)-s>1e-8)>1:
        raise UnverifiedJHMBranch('Multiple excess rows after initialization: original dependency branch not verified')
    active={i for i in range(m) if abs(X[i].sum()-s[i])>1e-8}
    initial=X.copy()

    def choices(Y, rows, policy, locked_donor=None):
        e=Y.sum(axis=1)-s
        donors=np.flatnonzero(e>1e-8)
        if locked_donor is not None and e[locked_donor]>1e-8:
            # Finish the identified row before invoking row selection again.
            # A recipient may become excess during this inner loop.
            donors=np.array([locked_donor])
        if len(donors)>1:
            raise UnverifiedJHMBranch('Multiple excess rows reached; no invented selection rule')
        if not len(donors):
            return []
        i=int(donors[0]); receivers=[r for r in rows if r!=i]
        if not receivers:
            raise RuntimeError('No unfrozen receiver')
        out=[]
        for j in np.flatnonzero(Y[i]>1e-8):
            j=int(j); r=min(receivers,key=lambda r:(C[r,j],r))
            delta=float(C[r,j]-C[i,j])
            if delta < -1e-8:
                raise UnverifiedJHMBranch('Donor is no longer an active column minimum')
            q=float(min(Y[i,j],e[i]))
            if policy in {'cap_receiver','cap_net_tie'}:
                q=min(q,float(-e[r]))
            if q<=1e-8:
                raise RuntimeError('Nonpositive transfer; no hidden fallback')
            key=(delta, q*delta if policy in {'net_tie','cap_net_tie'} else 0.,
                 -C[i,j] if tie_rule=='higher_donor_cost' else 0.,j,r)
            out.append(dict(donor=i,column=j,receiver=r,quantity=q,difference=delta,key=key))
        return sorted(out,key=lambda a:a['key'])

    def advance(Y,rows,a):
        Y=Y.copy(); rows=set(rows)
        i,j,r,q=a['donor'],a['column'],a['receiver'],a['quantity']
        Y[i,j]-=q; Y[r,j]+=q
        for t in (i,r):
            if abs(Y[t].sum()-s[t])<=1e-8:
                rows.discard(t)
        return Y,rows

    def finish(Y,rows,policy,record=False,locked_donor=None):
        steps=[]; seen=set()
        for _ in range(10000):
            state=(Y.tobytes(),tuple(sorted(rows)),locked_donor)
            if state in seen:
                raise RuntimeError('Restricted JHM cycle; no fallback')
            seen.add(state)
            candidates=choices(Y,rows,'baseline' if policy=='top2_completion' else policy,locked_donor)
            if not candidates:
                return Y,steps
            a=candidates[0]; scored=[]
            if policy=='top2_completion':
                for candidate in candidates[:2]:
                    trial,trialrows=advance(Y,rows,candidate)
                    completed,_=finish(trial,trialrows,'baseline',locked_donor=candidate['donor'])
                    scored.append((float(np.sum(C*completed)),candidate))
                # Stable min preserves the published baseline order on equal cost.
                a=min(scored,key=lambda v:v[0])[1]
            before=float(np.sum(C*Y)); Y,rows=advance(Y,rows,a)
            locked_donor=a['donor'] if Y[a['donor']].sum()>s[a['donor']]+1e-8 else None
            if record:
                step={k:v for k,v in a.items() if k!='key'}
                step.update(cost_before=before,cost_after=float(np.sum(C*Y)))
                if scored:
                    step['candidate_completion_costs']=[dict(column=b['column'],receiver=b['receiver'],cost=z) for z,b in scored]
                steps.append(step)
        raise RuntimeError('Restricted JHM transfer limit')

    X,steps=finish(X,active,variant,trace)
    if dummy and dummy[0]=='column':
        slack=s-X.sum(axis=1)
        C=np.column_stack([C,np.zeros(m)]); X=np.column_stack([X,slack]); d=np.r_[d,slack.sum()]
    return dict(**audit(C,s,d,X),dummy=dummy,trace=steps,initial_allocation=initial.tolist(),
                contract='restricted single-excess JHM interpretation',variant=variant,tie_rule=tie_rule)
