from pathlib import Path
import json,platform,sys
import numpy as np
import pandas as pd
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .run_baselines import write_csv

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'results'; REPORT=ROOT/'report'

def md(df):
    def f(x):
        if pd.isna(x): return 'unavailable'
        if isinstance(x,(float,np.floating)): return f'{x:.4f}'.rstrip('0').rstrip('.')
        return ' '.join(str(x).replace('|','/').split())
    return '| '+' | '.join(map(str,df.columns))+' |\n| '+' | '.join('---' for _ in df.columns)+' |\n'+'\n'.join('| '+' | '.join(f(v) for v in row)+' |' for row in df.itertuples(index=False,name=None))+'\n'

def summarize(data,suite):
    rows=[]
    for method,g in data.groupby('method',sort=False):
        good=g[g.status=='ok']; gaps=good.gap_pct
        row=dict(suite=suite,method=method,n=len(g),successes=len(good),failures=len(g)-len(good),mean_gap_pct=gaps.mean(),median_gap_pct=gaps.median(),max_gap_pct=gaps.max(),std_gap_pct=gaps.std(),mean_absolute_gap=good.gap.mean(),mean_accuracy=good.accuracy.mean(),optimal_hits=int((good.gap.abs()<1e-6).sum()),optimal_hit_rate=100*(good.gap.abs()<1e-6).sum()/len(g),mean_seconds=good.seconds.mean(),median_seconds=good.seconds.median())
        if 'improvement' in good and good.improvement.notna().any():
            row.update(improved=int((good.improvement>1e-6).sum()),worsened=int((good.improvement < -1e-6).sum()),tied=int((good.improvement.abs()<1e-6).sum()),improvement_rate=100*(good.improvement>1e-6).sum()/len(g),worsening_rate=100*(good.improvement < -1e-6).sum()/len(g),baseline=good.baseline.iloc[0])
        rows.append(row)
    return rows

def main():
    ids=json.loads((ROOT/'datasets/published/canonical_ids.json').read_text())
    ps=json.loads((ROOT/'datasets/published/benchmarks.json').read_text()); occ=json.loads((ROOT/'datasets/published/occurrences.json').read_text())
    b=pd.read_csv(OUT/'baseline.csv'); v=pd.read_csv(OUT/'modifications.csv'); r=pd.read_csv(OUT/'random_benchmark.csv')
    b=b[b.problem.isin(ids)]; v=v[v.problem.isin(ids)]
    summary=summarize(b,'published_baseline')+summarize(v,'published_modifications')+summarize(r,'random')
    write_csv(OUT/'summary.csv',summary)
    subgroup=[]
    for (size,kind),g in r.groupby(['size','kind']):
        subgroup.extend(summarize(g,f'random_{size}_{kind}'))
    write_csv(OUT/'random_by_size_distribution.csv',subgroup)
    cautious=[i for i in ids if i not in ['CSM_N03','CSM_N35']]
    write_csv(OUT/'source_sensitivity.csv',summarize(v[v.problem.isin(cautious)],'exclude_two_conflicting_author_matrix_transcriptions'))
    frames=[]
    for suite in ['published_baseline','published_modifications','random']:
        g=pd.DataFrame([z for z in summary if z['suite']==suite])
        cols=['method','n','failures','mean_gap_pct','median_gap_pct','max_gap_pct','std_gap_pct','optimal_hits']
        if 'improved' in g: cols+=['improved','worsened','tied']
        frames.append('## '+suite+'\n\n'+md(g[cols])+'\n')
    (REPORT/'performance_tables.md').write_text('# Complete aggregate experimental results\n\nPublished summaries use 84 matrices after balancing-equivalent duplicates are removed. Raw runs include 86 matrices. Random uses 300 fixed problems. Gaps are percentages, sample standard deviation; optimal hit denominator includes failures. Successful-only means are not fair rankings for methods with failures.\n\n'+''.join(frames),encoding='utf-8')
    appendix=['# Published numerical benchmarks\n\nAll transcribed source occurrences and raw numbers are in `datasets/published/occurrences.json`. This appendix lists the 86 distinct raw problems, including provenance aliases. Repeated balanced forms count once in aggregate experiments. Published values are claims, not ground truth.\n']
    cert=json.loads((OUT/'optimal_certificates.json').read_text())
    for p in ps:
        appendix.append(f"\n## {p['id']}\n\nSource {p['source']}, {p['locator']}. Shape {len(p['supply'])} x {len(p['demand'])}; balanced: {p['balanced']}; kind: {p['kind']}.\n\n```json\n"+json.dumps({k:p[k] for k in ['costs','supply','demand']},indent=2)+'\n```\n')
        appendix.append(f"\nLP optimum: **{cert[p['id']]['cost']:g}**; dual gap {cert[p['id']]['dual_gap']:g}. Occurrences: {', '.join(p['occurrences'])}.\n\n{p['note']}\n")
        claims=[dict(occurrence=o['id'],method=m,published=z) for o in occ if o['id'] in p['occurrences'] for m,z in o['claims'].items()]
        if claims: appendix.append('\n'+md(pd.DataFrame(claims)))
    (REPORT/'benchmark_catalog.md').write_text(''.join(appendix),encoding='utf-8')
    reproduction=pd.read_csv(OUT/'reproduction.csv')
    (REPORT/'reproduction_tables.md').write_text('# Reproduction audit\n\nA matched scalar cost does not uniquely validate every decision rule. Unspecified ties are completed deterministically as documented. Claims with unavailable algorithms are retained. This is the historical core audit; the later restricted JHM reproduction is recorded separately in [jhm_results.md](jhm_results.md) and [jhm_supplement.md](jhm_supplement.md), without changing the core 207-comparison denominator.\n\n'+md(reproduction),encoding='utf-8')
    shortlist=['VAM_top2_rollout','THP_top2_rollout','MRM_orientation_ensemble']
    selections=[]
    for name in shortlist:
        g=v[v.method==name]; selections.append('## '+name+'\n\n'+md(g[['problem','baseline_cost','cost','optimal','baseline_gap_pct','gap_pct','improvement']]))
    (REPORT/'candidate_results.md').write_text('# All cases for the three candidate directions\n\n'+ '\n'.join(selections),encoding='utf-8')
    ablate=['VAM_tie_allocation','VAM_penalty_A','VAM_top2_LB','VAM_top2_first_only','VAM_top2_rollout','VAM_tieA_top2_rollout','VAM_top3_rollout','THP_top2_LB','THP_top2_first_only','THP_top2_rollout','THP_top3_rollout','THP_top2_LCMcompletion']
    tab=pd.DataFrame(summary); ab=tab[tab.method.isin(ablate)]
    (REPORT/'ablation_tables.md').write_text('# Ablation and component changes\n\nCompare against the corresponding baseline, plus first-only vs every-decision rollout. The combined VAM tie+rollout uses its changed tie policy during completion, so its guarantee is relative to that policy, not index-tie VAM.\n\n'+md(ab[['suite','method','mean_gap_pct','optimal_hits','improved','worsened']]),encoding='utf-8')
    fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
    pairs=[('VAM','VAM_top2_rollout'),('THP','THP_top2_rollout'),('MRM','MRM_orientation_ensemble')]
    for ax,suite,label in zip(axs,['published','random'],['84 published / author-supplied matrices','300 generated validation problems']):
        base=[next(z['mean_gap_pct'] for z in summary if z['method']==a and z['suite']==('published_baseline' if suite=='published' else 'random')) for a,_ in pairs]
        modified=[next(z['mean_gap_pct'] for z in summary if z['method']==a and z['suite']==('published_modifications' if suite=='published' else 'random')) for _,a in pairs]
        x=np.arange(3); ax.bar(x-.17,base,.34,label='Baseline',color='#54728c');ax.bar(x+.17,modified,.34,label='Modification',color='#25856c')
        ax.set_xticks(x,[a for a,_ in pairs]);ax.set_ylabel('Mean optimality gap (%)');ax.set_title(label);ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    axs[0].legend(); fig.savefig(OUT/'gap_comparison.svg');fig.savefig(OUT/'gap_comparison.png',dpi=170);plt.close(fig)
    (OUT/'environment.json').write_text(json.dumps(dict(python=sys.version,platform=platform.platform(),numpy=np.__version__,scipy=scipy.__version__,pandas=pd.__version__),indent=2))
    print('Summary tables, benchmark catalog, reproduction appendix, ablation tables, and chart saved.')

if __name__=='__main__': main()
