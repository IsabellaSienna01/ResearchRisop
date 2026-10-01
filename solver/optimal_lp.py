"""HiGHS transportation LP, with primal and dual certificate checks."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import kron,eye,csr_matrix,vstack
from ..methods.common import balance,audit

def optimal(C,s,d):
    C,s,d,dummy=balance(C,s,d); m,n=C.shape
    A=vstack([kron(eye(m),csr_matrix(np.ones((1,n)))),kron(csr_matrix(np.ones((1,m))),eye(n))],format='csr')
    b=np.r_[s,d]
    result=linprog(C.ravel(),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
    if not result.success: raise RuntimeError(result.message)
    out=audit(C,s,d,result.x.reshape(m,n)); dual=result.eqlin.marginals
    reduced=C.ravel()-A.T@dual; dualcost=float(b@dual)
    gap=abs(out['cost']-dualcost); dual_violation=max(0.0,-float(min(reduced)))
    if gap>1e-6 or dual_violation>1e-7: raise RuntimeError('LP primal/dual certificate failed')
    return dict(**out,dual_cost=dualcost,dual_gap=gap,dual_violation=dual_violation,
                row_duals=dual[:m].tolist(),column_duals=dual[m:].tolist(),dummy=dummy)
