"""Reproducible recursive PDF inventory and layout-preserving text extraction."""
from pathlib import Path
import hashlib
import json
import subprocess
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research' / 'papers' / 'local_text'
OUT.mkdir(parents=True, exist_ok=True)
records = []
for k, path in enumerate(sorted(p for p in ROOT.rglob('*.pdf') if 'research' not in p.relative_to(ROOT).parts), 1):
    paper_id = f'L{k:02}'
    doc = fitz.open(path)
    target = OUT / f'{paper_id}.txt'
    subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', str(path), str(target)], check=True)
    records.append(dict(id=paper_id, path=path.relative_to(ROOT).as_posix(), bytes=path.stat().st_size,
                        sha256=hashlib.sha256(path.read_bytes()).hexdigest(), pages=len(doc),
                        metadata=doc.metadata, text=target.relative_to(ROOT).as_posix()))
(ROOT / 'research' / 'papers' / 'local_manifest.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
for rec in records:
    print(json.dumps(rec, ensure_ascii=True))

if __name__ == '__main__':
    pass
