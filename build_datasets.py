"""Transcribe supplied examples; parse author supplements without repairing numbers."""
from pathlib import Path
import json, re, hashlib
import fitz
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'datasets' / 'published'
OUT.mkdir(parents=True, exist_ok=True)
cases, exclusions = [], []

def add(identifier, C, s, d, source, locator, claims=None, note='', kind='literature'):
    assert len(C) == len(s) and all(len(r) == len(d) for r in C), identifier
    assert min(s+d) >= 0 and min(sum(C, [])) >= 0
    key = json.dumps([C,s,d], separators=(',', ':'))
    cases.append(dict(id=identifier, costs=C, supply=s, demand=d, source=source,
                      locator=locator, claims=claims or {}, note=note, kind=kind,
                      balanced=sum(s)==sum(d), sha256=hashlib.sha256(key.encode()).hexdigest()))

add('L01_Table2',[[10,2,20,11],[12,7,9,20],[4,14,16,18]],[15,25,10],[5,15,15,15],
    'L01','Table 2; Table 7 P09',dict(VAM=475,TDM1=475,TOCM_MT=435,JHM=460,BCE=435,optimal=435))
add('L02_Table3',[[4,6,5,2],[6,4,1,4],[5,2,3,1],[4,6,7,8]],[6,10,12,14],[9,16,10,7],
    'L02','Tables 3-6; N09',dict(RBSM=111,optimal=111))
add('L02_Table7',[[10,8,4,3],[12,14,20,2],[6,9,23,25]],[500,400,300],[250,350,600,150],
    'L02','Table 7; N06',dict(RBSM=7750,BCE=8350,optimal=7750),'Zero-cost dummy source of 150 required.')
add('L03_Table2',[[13,21,14],[8,12,21],[15,17,19]],[13,20,5],[12,15,11],
    'L03','Tables 2-5; Table 7 P26',dict(SSM=465,LCM=473,VAM=473,JHM=475,TOCM_MT=475,BCE=475,optimal=465))
add('L04_Example1',[[1,3,2],[3,2,6],[3,5,4]],[5,8,7],[5,5,10],
    'L04','Example 1; Table 9',dict(NWCM=57,LCM=55,VAM=61,AIP_MT=61,optimal=61,AIP_worked=55),
    'Published worked feasible cost 55 contradicts Table 9 optimal 61; reduced table has errors.')
add('L04_Example2',[[2,3,7,11],[0,12,5,6],[14,1,3,9],[10,2,5,8]],[150,125,75,50],[100,20,80,200],
    'L04','Example 2; Table 9',dict(NWCM=2215,LCM=1995,VAM=2245,AIP_MT=2360,optimal=1945,AIP_worked=1995),
    'Worked proposed cost 1995 differs from summary proposed cost 2360; reduced table has errors.')
add('L05_Example1',[[6,3,1,4],[7,6,2,1],[10,4,5,9],[7,7,7,3]],[50,55,75,60],[90,65,30,55],
    'L05','Example 1',dict(VAM=1095,LDVAM=1095,THP=1045,optimal=985))
add('L05_Example2',[[6,8,10],[7,11,11],[4,5,12]],[150,175,275],[200,100,300],
    'L05','Example 2',dict(VAM=5125,LDVAM=5125,THP=4525,optimal=4525))
add('L05_Example3',[[70,37,6,76,17],[59,90,93,5,10],[93,62,77,47,62],[54,55,26,9,84],[53,20,84,15,9]],
    [18,17,19,13,15],[16,18,20,14,14],'L05','Example 3',dict(VAM=2388,LDVAM=2388,THP=2366,optimal=2366))

hc=[
([[20,22,17,4],[24,37,9,7],[32,37,20,15]],[120,70,50],[60,40,30,110]),
([[3,5,7,6],[2,5,8,2],[3,6,9,2]],[50,75,25],[20,20,50,60]),
([[19,30,50,10],[70,30,40,60],[40,8,70,20]],[7,9,18],[5,8,7,14]),
([[41,46,14,49],[46,32,28,8],[7,5,48,49]],[7,9,18],[5,8,7,14]),
([[82,10,16,15,66],[91,28,98,43,4],[13,55,96,92,85],[92,96,49,80,94],[64,97,81,96,68]], [2,3,5,7,9],[1,4,6,8,7]),
([[17,4,14,15,9,6,16],[19,20,1,1,8,14,6],[3,20,17,6,16,14,11],[19,10,19,1,16,4,14],[13,17,14,2,4,3,18],[2,3,16,17,10,10,20],[6,9,15,14,9,20,11],[11,19,8,7,13,7,3],[20,16,14,20,15,12,3],[20,20,4,1,16,5,6]],
 [6,8,11,13,23,5,20,13,14,16],[14,24,28,33,4,12,14]),
([[25,29,13,21,9,14,22,29,27],[28,29,28,23,2,12,23,11,29],[4,5,24,23,3,23,9,18,17],[28,30,29,12,25,24,21,7,5],[19,29,20,20,21,6,20,23,5],[3,15,2,6,10,15,5,8,8],[9,25,26,22,29,14,4,16,26],[17,5,29,1,2,20,15,21,8]],
 [16,18,10,13,11,15,22,23],[13,21,15,8,10,12,20,13,16])]
results=[(3680,3670,3520,3570,3710),(670,650,650,630,610),(1015,814,779,779,781),
         (1451,None,490,490,490),(1853,None,1401,1401,1661),(1651,None,740,712,712),(2251,None,844,935,979)]
for k,((C,s,d),v) in enumerate(zip(hc,results),1):
    add(f'E01_Example{k}',C,s,d,'E01',f'Example {k}; Tables 3 or 7',
        {a:b for a,b in zip(['NWCM','LCM','VAM','TDM1','TDSM'],v) if b is not None},
        'TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.')
exclusions.append(dict(source='E01',cases='Examples 8-15',reason='Complete fixed cost matrices/seeds unavailable.'))

for p in sorted((ROOT/'papers/external').glob('rbsm_*.txt')):
    raw=p.read_text(encoding='utf-8-sig'); a=list(map(int,raw.split())); m,n=a[:2]; v=a[2:]
    assert len(v)==m*n+m+n,p.name
    add('RBSM_'+p.stem[5:].upper(),[v[i*n:(i+1)*n] for i in range(m)],v[m*n:m*n+m],v[m*n+m:],
        'E02',p.name,note='Public author file. Some instances already contain dummy rows/columns.',
        kind='author_synthetic' if p.stem[5:].upper().startswith('S') else 'literature')

def parse_matrices(text):
    pat=r'Cij\]\s*(\d+)\s*x\s*(\d+)\s*=\s*\[([^\]]+)\]\s*\[Si\]\s*\d+\s*x\s*\d+\s*=\s*\[([^\]]+)\]\s*\[D[ji]\]\s*\d+\s*x\s*\d+\s*=\s*\[([^\]]+)\]'
    out=[]
    for match in re.finditer(pat,text,re.S):
        m,n=map(int,match.group(1,2)); fields=match.group(3,4,5)
        assert all(not re.search(r'[^\d\s,;.-]',f) for f in fields),fields
        c,s,d=[list(map(int,re.findall(r'-?\d+',f))) for f in fields]
        assert len(c)==m*n and len(s)==m and len(d)==n,(m,n,c,s,d)
        out.append(([c[i*n:(i+1)*n] for i in range(m)],s,d))
    return out

doc=fitz.open(ROOT/'papers/external/E12_csm_data.pdf')
clipped='\n'.join(p.get_text(clip=fitz.Rect(340 if i<3 else 280 if i==3 else 0,0,p.rect.width,p.rect.height),sort=True) for i,p in enumerate(doc))
(OUT/'csm_matrix_extraction.txt').write_text(clipped,encoding='utf-8')
matrices=parse_matrices(clipped)
labels=[f'N{i:02}' for i in list(range(1,8))+list(range(9,19))+list(range(21,36))]+[f'S{i}' for i in range(1,6)]+[f'Real{i}' for i in range(1,6)]
opts=[5600,28,1102,1580,410,2850,1160,111,910,2460,425,4525,920,156,1510,743,29,4205,12075,23,3460,809,490,59356,40,3857,465,1480,348,151750,510,417,18855,2790,1044180,92212,116020]+[None]*5
assert len(matrices)==42,len(matrices)
for label,(C,s,d),opt in zip(labels,matrices,opts):
    add('CSM_'+label,C,s,d,'E12',f'Data document {label}',dict(optimal=opt) if opt is not None else {},
        'Data and result documents have label/matrix inconsistencies; do not join by label alone.',
        kind='author_synthetic' if label.startswith('S') else 'author_real' if label.startswith('Real') else 'literature')

# Author HTML is a distinct source; malformed records are quarantined, not repaired.
soup=BeautifulSoup((ROOT/'papers/external/E09_edm_dataset.html').read_text(encoding='utf-8'),'html.parser')
for tr in soup.select('.post-body table tr')[1:]:
    fields=[c.get_text(' ',strip=True) for c in tr.find_all(['td','th'])]
    if len(fields)!=6: continue
    _,label,ref,size,opt,raw=fields
    try:
        vals=parse_matrices(raw)
        if len(vals)!=1: raise ValueError('Incomplete or malformed matrix/vector text')
        C,s,d=vals[0]
        # C02 explicitly conflicts with the original balanced example: quarantine, no silent balancing.
        if label=='C02': raise ValueError('Supply [7,9,10] conflicts with source example [7,9,18] and total demand 34')
        add('EDM_'+label,C,s,d,'E09',label+' '+ref,dict(optimal=int(opt.replace(',',''))),
            'Secondary author dataset; original reference not necessarily accessed.')
    except (ValueError,AssertionError) as e:
        exclusions.append(dict(source='E09',cases=label,reason=str(e),raw=raw))

add('E11_Table3',[[4,4,9,10,13],[7,9,8,10,4],[9,3,7,10,6],[11,4,10,6,9]],
    [100,90,80,70],[60,40,90,70,80],'E11','Tables III-VII, worked N32',
    dict(CSM=1780,SSM=1820,optimal=1780),'Worked paper matrix independently confirms the supplement N32 matrix, not its printed optimum 348.')
mrmb=[
([[4,2,1],[3,8,4],[6,5,2]],[50,70,45],[40,65,60]),
([[6,4,1],[3,8,7],[4,4,2]],[50,40,60],[20,95,35]),
([[9,8,5,7],[4,6,8,7],[5,8,9,5]],[12,14,16],[8,18,13,3]),
([[3,1,7,4],[2,6,5,9],[8,3,3,2]],[300,400,500],[250,350,400,200]),
([[7,5,9,11],[4,3,8,6],[3,8,10,5],[2,6,7,3]],[30,25,20,15],[30,30,20,10]),
([[50,60,100,50],[80,40,70,50],[90,70,30,50]],[20,38,16],[10,18,22,24]),
([[4,3,5],[6,5,4],[8,10,7]],[90,80,100],[70,120,80]),
([[5,7,8],[4,4,6],[6,7,7]],[70,30,50],[65,42,43]),
([[1,2,1,4,5,2],[3,3,2,1,4,3],[4,2,5,9,6,2],[3,1,7,3,4,6]],[30,50,75,20],[20,40,30,10,50,25]),
([[2,2,2,1],[10,8,5,4],[7,6,6,8]],[3,7,5],[4,3,4,4]),
([[10,8,4,3],[12,14,20,2],[6,9,23,25]],[500,400,300],[250,350,600,150]),
([[12,10,6,13],[19,8,16,25],[17,15,15,20],[23,22,26,12]],[150,200,600,225],[300,500,75,100]),
([[5,8,6,6,3],[4,7,7,6,5],[8,4,6,6,4]],[800,500,900],[400,400,500,400,800])]
mrmresults=[(770,605,490,475,475),(730,555,555,555,555),(320,248,240,248,240),
 (4400,2900,2850,2850,2850),(540,435,470,415,410),(4160,3500,3320,3320,3320),
 (1500,1450,1500,1390,1390),(830,890,830,830,830),(740,470,450,450,430),
 (93,79,68,68,68),(18800,8800,8350,7750,7750),(14725,14625,13225,12475,12475),
 (13100,9800,9200,9200,9200)]
for i,((C,s,d),vals) in enumerate(zip(mrmb,mrmresults)):
    label=f'BTP{i+1}' if i<10 else f'UTP{i-9}'
    add('MRM_'+label,C,s,d,'E15',f'Tables 42/45/46 {label}',dict(zip(['NWCM','LCM','VAM','MRM','optimal'],vals)),
        'Author-uploaded full text accessed through browser; local direct PDF unavailable.')
hd3=[[7,5,9,8,6,4,3,6,5,9,7],[6,8,7,5,9,11,10,3,6,7,4],[8,6,5,7,9,10,4,11,8,5,6],
 [4,7,8,6,5,9,11,10,4,7,6],[5,9,6,4,8,7,10,12,6,5,8],[7,5,9,6,8,4,11,10,12,7,5],
 [8,7,5,9,6,4,12,11,5,8,7],[6,8,7,9,5,11,4,6,9,5,8],[4,9,5,8,7,10,6,3,9,5,7],
 [5,8,7,6,4,10,12,9,7,8,6],[7,6,8,5,9,11,4,5,7,10,8],[6,7,9,4,5,8,10,11,6,7,5]]
add('MRM_HDTP3',hd3,[60,80,40,70,50,60,70,40,80,50,70,50],[60,70,50,60,80,40,50,70,40,50,60],
    'E15','Table 43 HDTP-3',kind='author_synthetic')
exclusions.append(dict(source='E15',cases='HDTP-1, HDTP-2, HDTP-4',reason='Browser text has merged entries/missing supply line or questionable separators. Require visual original-page verification before transcription.'))

# Two literal matrices in L04 already specify the worked feasible allocations.
for p in cases:
    if p['id']=='L04_Example1': p['worked_allocation']=[[0,0,5],[3,5,0],[2,0,5]]
    if p['id']=='L04_Example2': p['worked_allocation']=[[100,20,30,0],[0,0,0,125],[0,0,50,25],[0,0,0,50]]
    C,s,d=p['costs'],p['supply'],p['demand']
    if sum(s)<sum(d): C=C+[[0]*len(d)]; s=s+[sum(d)-sum(s)]
    elif sum(s)>sum(d): C=[r+[0] for r in C]; d=d+[sum(s)-sum(d)]
    p['balanced_sha256']=hashlib.sha256(json.dumps([C,s,d],separators=(',',':')).encode()).hexdigest()

(OUT/'occurrences.json').write_text(json.dumps(cases,indent=2),encoding='utf-8')
unique={}
for c in cases:
    if c['sha256'] not in unique:
        unique[c['sha256']]={**c,'occurrences':[]}
    unique[c['sha256']]['occurrences'].append(c['id'])
(OUT/'benchmarks.json').write_text(json.dumps(list(unique.values()),indent=2),encoding='utf-8')
canonical={}
for p in unique.values():
    h=p['balanced_sha256']
    if h not in canonical or (not p['balanced'] and canonical[h]['balanced']): canonical[h]=p
(OUT/'canonical_ids.json').write_text(json.dumps([p['id'] for p in canonical.values()],indent=2))
(OUT/'exclusions.json').write_text(json.dumps(exclusions,indent=2),encoding='utf-8')
print(f'{len(cases)} source occurrences; {len(unique)} raw unique matrices; {len(canonical)} balanced unique; {len(exclusions)} exclusion records')
