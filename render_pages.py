"""Render explicitly selected PDF pages for transcription checks (1-based)."""
import sys
from pathlib import Path
import fitz
path = Path(sys.argv[1])
out = Path(__file__).parent / 'papers' / 'page_checks'
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(path)
for page in map(int, sys.argv[2:]):
    target = out / f'{path.stem[:20]}_p{page}.png'
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(target)
    print(target)
