"""Small controlled timing sample; no concurrent experiment processes required."""
from pathlib import Path
import json,time,statistics
from ..methods import solve
from ..modifications import solve_variant
from .run_baselines import write_csv

def main():
    root=Path(__file__).resolve().parents[1]
    cases=json.loads((root/'datasets/generated/seed20261001.json').read_text())
    cases=[p for p in cases if p['id'].endswith(('_00','_01'))]
    methods=['VAM','THP','MRM','VAM_top2_rollout','THP_top2_rollout','MRM_orientation_ensemble','VAM_top2_first_only']
    rows=[]
    for p in cases:
        for name in methods:
            fun=solve_variant if '_' in name else solve
            args=(p['costs'],p['supply'],p['demand'],name)
            fun(*args) # untimed warmup
            measurements=[]
            for _ in range(3):
                start=time.perf_counter(); fun(*args); measurements.append(time.perf_counter()-start)
            rows.append(dict(problem=p['id'],size=len(p['supply']),method=name,median_seconds=statistics.median(measurements)))
    write_csv(root/'results/controlled_timing.csv',rows)
    print(f'Saved 3-repeat median timings for {len(cases)} cases x {len(methods)} methods.')

if __name__=='__main__':main()
