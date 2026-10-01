"""Print selected lines without excessive layout padding; UTF-8 safe."""
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = Path(sys.argv[1])
lines = p.read_text(encoding='utf-8').splitlines()
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
for i in range(a-1, min(b, len(lines))):
    print(f'{i+1}: {lines[i].lstrip()}')
