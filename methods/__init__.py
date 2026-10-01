from .constructive import solve_constructive
from .repair import solve_repair
from .mrm import solve_mrm

BASELINES = ['NWCM','LCM','VAM','LDVAM','RAM','TDM1','TDM2','TDSM','THP','SSM','CSM','RBSM','BCE','MRM']

def solve(C, s, d, method, **kwargs):
    if method=='MRM': return solve_mrm(C,s,d,**kwargs)
    if method in {'SSM','CSM','RBSM','BCE'}:
        return solve_repair(C,s,d,method,**kwargs)
    return solve_constructive(C,s,d,method,**kwargs)
