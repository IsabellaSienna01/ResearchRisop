"""Preserve all reported result rows, including those without verified matrices."""
from pathlib import Path
import re,csv,json

ROOT=Path(__file__).resolve().parent
rows=[]
specs=[('L01','papers/local_text/L01.txt',r'^\s*\d+\s+(P\d+)\s+','Table 7',35,['VAM','TDM1','TOCM_MT','JHM','BCE','optimal']),
       ('L03','papers/local_text/L03.txt',r'^\s*\d+\s+([PSR]\d+)\s+','Table 7',45,['LCM','VAM','JHM','TOCM_MT','BCE','SSM','optimal']),
       ('E13','papers/external/E13_csm_results.txt',r'^\s*\d+\s+(N\d+|S\d+|Real\s+\d+)\s+','Table 1',42,['VAM','JHM','TOCM_MT','BCE','SSM','CSM','optimal'])]
for source,path,pat,table,count,methods in specs:
    text=(ROOT/path).read_text(encoding='utf-8'); lines=text.splitlines(); seen=set()
    # First matching numbered table block: runtime tables occur later.
    for line in lines:
        match=re.match(pat,line)
        if not match: continue
        label=match.group(1).replace(' ','')
        if label in seen: continue
        values=re.findall(r'\d[\d,]*(?:\.\d+)?\*?',line[match.end():])
        if len(values)<len(methods): continue
        # L01 preceding source table also starts number/P? sources are before label,
        # so pattern starts only in the costs table, checked count and first cost.
        for method,value in zip(methods,values):
            rows.append(dict(source=source,table=table,label=label,method=method,published_cost=float(value.replace(',','').replace('*','')),matrix_link_status='unlinked; require matrix identity and original provenance'))
        seen.add(label)
        if len(seen)==count: break
    assert len(seen)==count,(source,len(seen))
dest=ROOT/'datasets/published/reported_claims.csv'
with dest.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
assert next(r for r in rows if r['source']=='L01' and r['label']=='P09' and r['method']=='BCE')['published_cost']==435
assert next(r for r in rows if r['source']=='L03' and r['label']=='P26' and r['method']=='SSM')['published_cost']==465
print(f'Preserved {len(rows)} published costs; no automatic joins by cost/label.')
