"""Download an explicitly selected public research source; preserve URL and hash."""
from pathlib import Path
import sys, json, hashlib, urllib.request, ssl
from datetime import datetime, timezone

url, name = sys.argv[1:3]
out = Path(__file__).resolve().parent / 'papers' / 'external'
out.mkdir(parents=True, exist_ok=True)
agent = 'Mozilla/5.0' if '--browser-agent' in sys.argv[3:] else 'TransportationResearch/1.0'
req = urllib.request.Request(url, headers={'User-Agent': agent})
context = None
expired_public_source = '--expired-ulm-certificate' in sys.argv[3:]
if expired_public_source:
    # One anonymous public PDF only. No persistent/network-wide TLS change.
    if url != 'https://ppjp.ulm.ac.id/journals/index.php/epsilon/article/download/2876/pdf':
        raise ValueError('Certificate exception is restricted to the selected public ULM paper')
    context = ssl._create_unverified_context()
with urllib.request.urlopen(req, timeout=35, context=context) as response:
    data = response.read()
    final_url = response.url
target = out / name
target.write_bytes(data)
target.with_suffix(target.suffix + '.source.json').write_text(json.dumps({
    'requested_url': url, 'final_url': final_url,
    'retrieved_utc': datetime.now(timezone.utc).isoformat(),
    'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
    'tls_certificate_verified': not expired_public_source, 'user_agent': agent
}, indent=2), encoding='utf-8')
print(str(target), len(data), data[:20])
