"""Download the fixed research download queue; no downloaded code is executed."""
from pathlib import Path
import json, urllib.request, hashlib
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
base = Path(__file__).parent / 'papers' / 'external'

def fetch(rec):
    target = (base / rec['name']).resolve()
    assert target.parent == base.resolve(), 'Target must be in research/papers/external'
    if target.exists():
        return {'name':rec['name'], 'status':'already downloaded'}
    try:
        request = urllib.request.Request(rec['url'], headers={'User-Agent':'TransportationResearch/1.0'})
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read()
            final_url = response.url
        target.write_bytes(data)
        meta = {**rec, 'final_url':final_url, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
                'retrieved_utc':datetime.now(timezone.utc).isoformat()}
        target.with_suffix(target.suffix+'.source.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
        return {'name':rec['name'], 'status':'downloaded', 'bytes':len(data), 'prefix':repr(data[:8])}
    except Exception as e:
        return {'name':rec['name'], 'status':'failed', 'error':str(e)}

queue = json.loads((base/'download_queue.json').read_text(encoding='utf-8'))
with ThreadPoolExecutor(max_workers=4) as pool:
    outcomes=list(pool.map(fetch, queue))
(base/'download_outcomes.json').write_text(json.dumps(outcomes,indent=2),encoding='utf-8')
for row in outcomes:
    print(json.dumps(row))
