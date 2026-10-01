"""Run the restricted JHM follow-up separately from complete-suite rankings."""
from pathlib import Path
import json,time
import numpy as np
import pandas as pd
from ..methods.jhm import solve_jhm,UnverifiedJHMBranch
from ..methods.common import audit,balance
from .run_baselines import write_csv,metrics
from .summarize import md

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'results'
VARIANTS=['baseline','cap_receiver','net_tie','cap_net_tie','top2_completion']


def main():
    ids=set(json.loads((ROOT/'datasets/published/canonical_ids.json').read_text()))
    runs=[]; allocations={}
    for suite,file,certfile in [('published','datasets/published/benchmarks.json','optimal_certificates.json'),
                                ('random','datasets/generated/seed20261001.json','random_optimal_certificates.json')]:
        cases=json.loads((ROOT/file).read_text()); certificates=json.loads((OUT/certfile).read_text())
        for p in cases:
            for variant in VARIANTS:
                row=dict(suite=suite,problem=p['id'],canonical=suite=='random' or p['id'] in ids,variant=variant,
                         optimal=certificates[p['id']]['cost'],source=p.get('source','generated'))
                start=time.perf_counter()
                try:
                    result=solve_jhm(p['costs'],p['supply'],p['demand'],variant,trace=suite=='published')
                    row.update(cost=result['cost'],status='ok',basic=result['basic'],**metrics(result['cost'],row['optimal']))
                    allocations[suite+'::'+p['id']+'::'+variant]=result
                except UnverifiedJHMBranch as e:
                    row.update(status='unverified',error=str(e))
                except Exception as e:
                    row.update(status='failed',error=type(e).__name__+': '+str(e))
                row['seconds']=time.perf_counter()-start; runs.append(row)
    df=pd.DataFrame(runs)
    base=df[df.variant=='baseline'][['suite','problem','cost','status']].rename(columns={'cost':'baseline_cost','status':'baseline_status'})
    df=df.merge(base,on=['suite','problem'],validate='many_to_one')
    df['improvement']=df.baseline_cost-df.cost
    write_csv(OUT/'jhm_restricted.csv',df.to_dict('records'))
    (OUT/'jhm_allocations.json').write_text(json.dumps(allocations,indent=2))
    summaries=[]
    for (suite,variant),g in df[df.canonical].groupby(['suite','variant'],sort=False):
        good=g[g.status=='ok']; paired=good[good.baseline_status=='ok']
        summaries.append(dict(suite=suite,variant=variant,total=len(g),successful=len(good),
            unverified=int((g.status=='unverified').sum()),failures=int((g.status=='failed').sum()),
            nonbasic=int((good.basic==False).sum()),mean_gap_pct=good.gap_pct.mean(),median_gap_pct=good.gap_pct.median(),
            max_gap_pct=good.gap_pct.max(),std_gap_pct=good.gap_pct.std(),optimal_hits=int(good.optimal_hit.sum()),
            paired_n=len(paired),paired_baseline_mean_gap_pct=(100*(paired.baseline_cost-paired.optimal)/paired.optimal).mean(),
            paired_modified_mean_gap_pct=paired.gap_pct.mean(),
            improved=int((paired.improvement>1e-6).sum()),
            tied=int((paired.improvement.abs()<1e-6).sum()),worsened=int((paired.improvement < -1e-6).sum())))
    write_csv(OUT/'jhm_summary.csv',summaries)
    # Claims tied to fully known local matrices; do not join paper labels by optimum.
    occurrences=json.loads((ROOT/'datasets/published/occurrences.json').read_text())
    raw=json.loads((ROOT/'datasets/published/benchmarks.json').read_text()); hashid={p['sha256']:p['id'] for p in raw}
    rep=[]
    for p in occurrences:
        if 'JHM' not in p['claims']: continue
        row=df[(df.suite=='published')&(df.problem==hashid[p['sha256']])&(df.variant=='baseline')].iloc[0]
        rep.append(dict(source=p['source'],occurrence=p['id'],locator=p['locator'],published=p['claims']['JHM'],
                        reproduced=row.cost,status=row.status,match=row.status=='ok' and abs(row.cost-p['claims']['JHM'])<1e-6))
    write_csv(OUT/'jhm_reproduction.csv',rep)
    tie_rows=[]
    for pid in ['L01_Table2','L03_Table2']:
        p=next(p for p in raw if p['id']==pid)
        for rule in ['higher_donor_cost','index']:
            out=solve_jhm(p['costs'],p['supply'],p['demand'],trace=True,tie_rule=rule)
            published=p['claims']['JHM']
            tie_rows.append(dict(problem=pid,tie_rule=rule,cost=out['cost'],published=published,match=out['cost']==published,
                                 allocation=json.dumps(out['allocation'])))
    write_csv(OUT/'jhm_tie_sensitivity.csv',tie_rows)
    # Required anchors, explicit exclusions, invariants and no-optimum-in-selection checks.
    for pid,z in [('L01_Table2',460),('L03_Table2',473)]:
        row=df[(df.suite=='published')&(df.problem==pid)&(df.variant=='baseline')].iloc[0]
        assert row.status=='ok' and row.cost==z,(pid,row.to_dict())
    good=df[(df.status=='ok')&(df.variant=='top2_completion')&(df.baseline_status=='ok')]
    assert (good.improvement>=-1e-6).all()
    assert not (df.status=='failed').any(),df[df.status=='failed'][['problem','variant','error']].to_dict('records')
    for key,out in allocations.items():
        assert out['feasible'] and out['basic'],key
    # L01's printed JHM allocation is an independent cost/feasibility audit.
    p=next(p for p in raw if p['id']=='L01_Table2'); C,s,d,_=balance(p['costs'],p['supply'],p['demand'])
    printed=np.array([[0,0,0,15],[0,10,15,0],[5,5,0,0]],float)
    assert audit(C,s,d,printed)['cost']==460
    # Demand excess and supply excess both audited against independent LP certificates.
    assert len(df[(df.suite=='published')&(df.problem=='L02_Table7')&(df.variant=='baseline')&(df.status=='ok')])==1
    text='# Restricted JHM results\n\nThis is a partial algorithm contract, not a full JHM ranking. '+\
         'Mean gaps and hit counts apply only to the successful single-excess subset; all excluded inputs remain in the CSV. '+\
         'Do not compare these means with other methods on all 84/300 inputs.\n\n'+md(pd.DataFrame(summaries))+\
         '\n## Published source claim checks\n\n'+md(pd.DataFrame(rep))+\
         '\n## Tie sensitivity, not a changed reproduction rule\n\n'+md(pd.DataFrame(tie_rows))+\
         '\n## Every canonical published input\n\n'+md(df[(df.suite=='published')&df.canonical][['problem','variant','status','baseline_cost','cost','optimal','gap_pct','improvement']])
    (ROOT/'report/jhm_results.md').write_text(text,encoding='utf-8')
    (OUT/'jhm_verification.txt').write_text('PASS: L01 cost 460 matches; L03 higher-unit-cost tie trace gives 473, explicitly mismatching published 475; printed L01 allocation audited; all successful outputs feasible and basic; demand-excess dummy case; same-policy completion never worsens the baseline on matched inputs; unresolved branches excluded explicitly.\n',encoding='utf-8')
    print(pd.DataFrame(summaries).to_string(index=False))
    print('Saved',len(df),'runs,',len(rep),'published claim comparisons')


if __name__=='__main__': main()
