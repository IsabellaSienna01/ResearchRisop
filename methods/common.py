import numpy as np

def balance(C,s,d):
    C=np.asarray(C,dtype=float).copy(); s=np.asarray(s,dtype=float).copy(); d=np.asarray(d,dtype=float).copy()
    if C.shape!=(len(s),len(d)) or not np.isfinite(C).all() or not np.isfinite(s).all() or not np.isfinite(d).all():
        raise ValueError('Invalid dimensions/nonfinite input')
    if min(C.min(),s.min(),d.min())<0: raise ValueError('This experimental suite assumes nonnegative data')
    dummy=None
    if s.sum()<d.sum():
        dummy=('row',len(s)); C=np.vstack([C,np.zeros(len(d))]); s=np.r_[s,d.sum()-s.sum()]
    elif s.sum()>d.sum():
        dummy=('column',len(d)); C=np.column_stack([C,np.zeros(len(s))]); d=np.r_[d,s.sum()-d.sum()]
    return C,s,d,dummy

def audit(C,s,d,X):
    """Check feasibility and whether positive support can form a transportation basis.

    A spanning tree is completed with symbolic zero basic cells. No epsilon
    shipments, improvement pivots, or cost-changing postprocessing are used.
    """
    if X.shape!=C.shape or not np.isfinite(X).all(): raise ValueError('Invalid allocation')
    residual=max(float(np.abs(X.sum(axis=1)-s).max()),float(np.abs(X.sum(axis=0)-d).max()))
    if X.min() < -1e-8 or residual>1e-7: raise ValueError(f'Infeasible allocation; residual {residual}')
    m,n=C.shape; parent=list(range(m+n))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    basis=[]; cycle=False
    for i,j in np.argwhere(X>1e-8):
        i,j=int(i),int(j); a,b=find(i),find(m+j)
        if a==b: cycle=True
        else: parent[a]=b
        basis.append([i,j])
    positive=len(basis)
    if not cycle:
        for i in range(m):
            for j in range(n):
                a,b=find(i),find(m+j)
                if a!=b: parent[a]=b; basis.append([i,j])
        assert len(basis)==m+n-1
    return dict(cost=float(np.sum(C*X)),feasible=True,basic=not cycle,positive_cells=positive,
                degenerate=not cycle and positive<m+n-1,basis=basis if not cycle else None,
                primal_residual=residual,allocation=X.tolist())
