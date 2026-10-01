"""Run one documented example per shortlisted modification; no result files changed."""
import argparse
import json
from pathlib import Path

from ..methods import solve
from ..solver.optimal_lp import optimal
from ..experiments.run_baselines import metrics
from .variants import solve_variant

ROOT = Path(__file__).resolve().parents[1]
DEMOS = {
    'vam': ('VAM', 'VAM_top2_rollout', 'L05_Example1'),
    'thp': ('THP', 'THP_top2_rollout', 'L05_Example1'),
    'mrm': ('MRM', 'MRM_orientation_ensemble', 'E01_Example1'),
}


def evaluate(problem, method, trace=False):
    baseline_name, variant_name, _ = DEMOS[method]
    C, s, d = problem['costs'], problem['supply'], problem['demand']
    baseline = solve(C, s, d, baseline_name, trace=trace)
    modified = solve_variant(C, s, d, variant_name, trace=trace)
    # Solve independently AFTER both heuristic runs; never pass LP information to them.
    optimum = optimal(C, s, d)
    return dict(problem=problem['id'], source=problem['source'], locator=problem['locator'],
                baseline_method=baseline_name, modified_method=variant_name,
                published_claims=problem.get('claims', {}),
                baseline=baseline, modified=modified, optimal_cost=optimum['cost'],
                baseline_metrics=metrics(baseline['cost'], optimum['cost']),
                modified_metrics=metrics(modified['cost'], optimum['cost']),
                improvement=baseline['cost'] - modified['cost'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--method', choices=['all', *DEMOS], default='all')
    parser.add_argument('--problem', help='Core benchmark ID; overrides the default for every selected method')
    parser.add_argument('--trace', action='store_true', help='Include zero-indexed allocation decisions')
    parser.add_argument('--json', action='store_true', help='Print full machine-readable results to stdout')
    parser.add_argument('--list-problems', action='store_true', help='List saved core IDs and exit')
    args = parser.parse_args()
    cases = json.loads((ROOT / 'datasets/published/benchmarks.json').read_text(encoding='utf-8'))
    by_id = {p['id']: p for p in cases}
    if args.list_problems:
        for p in cases:
            print(f"{p['id']}: {len(p['supply'])}x{len(p['demand'])}, source={p['source']}")
        return
    if args.problem and args.problem not in by_id:
        parser.error(f'Unknown problem {args.problem!r}; use --list-problems')
    selected = list(DEMOS) if args.method == 'all' else [args.method]
    results = [evaluate(by_id[args.problem or DEMOS[name][2]], name, args.trace) for name in selected]
    if args.json:
        print(json.dumps(results, indent=2, allow_nan=False))
        return
    for r in results:
        print(f"{r['modified_method']} | {r['problem']} ({r['source']}, {r['locator']})")
        print(f"  baseline={r['baseline']['cost']:g}, modified={r['modified']['cost']:g}, "
              f"optimal={r['optimal_cost']:g}, improvement={r['improvement']:g}")
        print(f"  gap: {r['baseline_metrics']['gap_pct']:.4f}% -> {r['modified_metrics']['gap_pct']:.4f}%")
        print(f"  feasible={r['modified']['feasible']}, basic={r['modified']['basic']}")
        if args.trace:
            print('  Modified allocation and decisions (indices start at 0):')
            print(json.dumps(dict(allocation=r['modified']['allocation'], trace=r['modified']['trace']), indent=2))


if __name__ == '__main__':
    main()
