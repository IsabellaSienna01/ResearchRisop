"""Additional source audit: JNM appendix A and BCE's printed 2x94 real case.

Separate from the frozen 84-case comparison. Preserve exact printed vectors,
including the conspicuous Deshmukh demand=40 (not silently changed to 5).
"""
import json,re,hashlib,time
import fitz
import pandas as pd
from ..methods import solve,BASELINES
from ..methods.jhm import solve_jhm,UnverifiedJHMBranch
from ..modifications.variants import VARIANTS,solve_variant
from ..solver.optimal_lp import optimal
from .run_baselines import ROOT,OUT,write_csv,metrics
from .summarize import md


def main():
    raw=[
      ('Srinivasan',[[3,6,3,4],[6,5,11,15],[1,3,10,5]],[80,90,55],[70,60,35,60],880,955),
      ('Sen',[[60,120,75,180],[58,100,60,165],[62,110,65,170],[65,115,80,175],[70,135,85,195]],
       [8000,9200,6250,4900,6100],[5000,2000,10000,6000],2146750,2164000),
      ('Deshmukh_literal',[[19,30,50,10],[70,30,40,60],[40,8,70,20]],[7,9,18],[40,8,7,14],743,779),
      ('Ramadan',[[32,40,120],[60,68,104],[200,80,60]],[20,30,45],[30,35,30],5600,5600),
      ('Kulkarni',[[3,4,6],[7,3,8],[6,4,5],[7,5,2]],[100,80,90,120],[110,110,60],840,880),
      ('Schrenk',[[3,6,1,5],[7,9,2,7],[2,4,2,1]],[6,6,6],[4,5,4,5],59,59),
      ('Samuel',[[1,2,3,4],[4,3,2,0],[0,2,2,1]],[6,8,10],[4,6,8,6],28,28),
      ('Imam',[[10,2,20,11],[12,7,9,20],[4,14,16,18]],[15,25,10],[5,15,15,15],460,475),
      ('Adlakha',[[2,1,3,2,2],[3,2,1,1,1],[5,4,2,1,3],[7,5,5,3,1]],[20,70,30,60],[50,30,30,50,20],390,390),
    ]
    cases=[dict(id='E19_'+name,costs=C,supply=s,demand=d,source='E19',locator='Appendix A p29; Table 8 p23',
                claims=dict(JHM=z,VAM=v,optimal=435 if name=='Imam' else z),
                note='Exact printed demand 40; inconsistent with the balanced Deshmukh instance in other sources; sensitivity audit only.' if name=='Deshmukh_literal' else '')
           for name,C,s,d,z,v in raw]
    doc=fitz.open(ROOT.parent/'IBFS/ibfs.pdf'); page=doc[8]
    text=page.get_text(clip=fitz.Rect(0,0,310,page.rect.height))
    strings=re.search(r'\[Cij\]2x94\s*=\s*\[(.*?)\]\s*\[Si\]2x1\s*=\s*\[(.*?)\]\s*\[Dj\]1x94\s*=\s*\[(.*?)\]',text,re.S).groups()
    c,s,d=[list(map(int,re.findall(r'\d+',t))) for t in strings]
    assert (len(c),len(s),len(d))==(188,2,94)
    cases.append(dict(id='L01_Real2x94',costs=[c[:94],c[94:]],supply=s,demand=d,source='L01',locator='p2306, real application',
          claims=dict(BCE=12175097,VAM=12175097,TDM1=12208071,TOCM_MT=12210362,JHM=12175097,optimal=12175097),note='Directly extracted from supplied PDF; numerical page visually inspected.'))
    core=json.loads((ROOT/'datasets/published/benchmarks.json').read_text())
    for p in cases:
        h=hashlib.sha256(json.dumps([p['costs'],p['supply'],p['demand']],separators=(',',':')).encode()).hexdigest()
        p.update(sha256=h,core_exact_duplicates=[x['id'] for x in core if x['sha256']==h])
    (ROOT/'datasets/published/jhm_supplement.json').write_text(json.dumps(cases,indent=2),encoding='utf-8')
    runs=[]; reproduction=[]; certificates={}; allocations={}
    for p in cases:
        C,s,d=p['costs'],p['supply'],p['demand']; opt=optimal(C,s,d); certificates[p['id']]=opt
        methods=list(BASELINES)+list(VARIANTS)+['JHM_single','JHM_cap_receiver','JHM_net_tie','JHM_cap_net_tie','JHM_top2_completion']
        bymethod={}
        for method in methods:
            row=dict(problem=p['id'],method=method,optimal=opt['cost']); start=time.perf_counter()
            try:
                if method.startswith('JHM_'):
                    variant='baseline' if method=='JHM_single' else method[4:]
                    out=solve_jhm(C,s,d,variant,trace=True)
                elif method in BASELINES: out=solve(C,s,d,method)
                else: out=solve_variant(C,s,d,method)
                row.update(cost=out['cost'],status='ok',basic=out['basic'],**metrics(out['cost'],opt['cost']))
                allocations[p['id']+'::'+method]=out
            except UnverifiedJHMBranch as e: row.update(status='unverified',error=str(e))
            except Exception as e: row.update(status='failed',error=type(e).__name__+': '+str(e))
            row['seconds']=time.perf_counter()-start; runs.append(row); bymethod[method]=row
        for method,published in p['claims'].items():
            row=dict(problem=p['id'],method=method,published_cost=published)
            if method=='optimal': row.update(reproduced_cost=opt['cost'],status='LP verified',match=published==opt['cost'])
            else:
                r=bymethod.get('JHM_single' if method=='JHM' else method,{})
                z=r.get('cost'); row.update(reproduced_cost=z,status=r.get('status','not implemented'),match=None if z is None else abs(published-z)<1e-6)
            reproduction.append(row)
    write_csv(OUT/'jhm_supplement.csv',runs);write_csv(OUT/'jhm_supplement_reproduction.csv',reproduction)
    (OUT/'jhm_supplement_optimal.json').write_text(json.dumps(certificates,indent=2))
    (OUT/'jhm_supplement_allocations.json').write_text(json.dumps(allocations,indent=2))
    sections=['# Additional JHM source audit\n\nThese ten source occurrences were extracted during the JHM follow-up and are separate from the frozen 84-case comparison. Exact core duplicates are identified below; do not count them as independent extra validation. The literal Deshmukh transcription is retained for error analysis. No metaheuristic is introduced.\n',
              '## Published claim reproduction\n\n'+md(pd.DataFrame(reproduction))]
    for p in cases:
        sections.append('\n## '+p['id']+'\n\nSource '+p['source']+', '+p['locator']+'. Core exact duplicates: '+str(p['core_exact_duplicates'])+'. '+p['note']+'\n\n```json\n'+json.dumps({k:p[k] for k in ['costs','supply','demand']},indent=2)+'\n```\n\nLP optimum: '+str(certificates[p['id']]['cost'])+'\n\n')
    sections.append('\n## Every computed result\n\n'+md(pd.DataFrame(runs)))
    (ROOT/'report/jhm_supplement.md').write_text(''.join(sections),encoding='utf-8')
    print(pd.DataFrame(reproduction).to_string(index=False))
    print('Saved',len(cases),'source occurrences and',len(runs),'runs')


if __name__=='__main__': main()
