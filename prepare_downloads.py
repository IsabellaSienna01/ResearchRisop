"""Prepare public source URLs already discovered in publisher/author HTML."""
from pathlib import Path
from bs4 import BeautifulSoup
import re, json
base = Path(__file__).parent / 'papers' / 'external'
soup = BeautifulSoup((base/'E08_rbsm_drive.html').read_text(encoding='utf-8'), 'html.parser')
records = {}
for node in soup.select('[data-id]'):
    label = node.get_text(' ', strip=True)
    if re.fullmatch(r'(?:n\d+|S\d+)\.txt|metodeS2new\.cpp', label):
        records[label] = {'name': 'rbsm_' + label, 'url': 'https://drive.google.com/uc?export=download&id=' + node['data-id']}
extra = [
    ('E11_csm.pdf','https://etasr.com/index.php/ETASR/article/download/16468/6350/83362'),
    ('E12_csm_data.pdf','https://drive.google.com/uc?export=download&id=1QLlQK3MtIPtcjDVSAHeQ7pMc9Md4-UVs'),
    ('E13_csm_results.pdf','https://drive.google.com/uc?export=download&id=1yhujVAolPIx_Nmn6ohiq4WIGYM-KaWJp'),
    ('E14_csm_runtime.pdf','https://drive.google.com/uc?export=download&id=1TTbv5Xrohbcw3m0lUQKzwwNxbbo9tdNg'),
    ('E15_mrm_author.html','https://www.researchgate.net/publication/390608938_The_maximum_range_method_for_finding_initial_basic_feasible_solution_for_transportation_problems'),
    ('E16_ivam_author.html',"https://www.researchgate.net/publication/266911500_An_Improved_Vogel's_Approximation_Method_for_the_Transportation_Problem"),
    ('E17_capacity2024.pdf','https://thesai.org/Downloads/Volume15No9/Paper_28-A_Capacity_Influenced_Approach_to_Find_Bette_Initial_Solution.pdf'),
]
all_records = list(records.values()) + [dict(name=n, url=u) for n,u in extra]
(base/'download_queue.json').write_text(json.dumps(all_records, indent=2), encoding='utf-8')
print('Prepared',len(all_records),'public files')
