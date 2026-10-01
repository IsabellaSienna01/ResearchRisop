"""Audit saved research evidence and report links without rerunning experiments."""
from pathlib import Path
import json
import re
from urllib.parse import unquote

import numpy as np
import pandas as pd

from ..methods.common import balance, audit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def close(actual, expected, context):
    assert np.isclose(actual, expected, atol=1e-7, rtol=1e-10), (context, actual, expected)


def main():
    core = read_json(ROOT / 'datasets/published/benchmarks.json')
    canonical = set(read_json(ROOT / 'datasets/published/canonical_ids.json'))
    random = read_json(ROOT / 'datasets/generated/seed20261001.json')
    supplement = read_json(ROOT / 'datasets/published/jhm_supplement.json')
    assert (len(core), len(canonical), len(random), len(supplement)) == (86, 84, 300, 10)
    assert len(read_json(ROOT / 'datasets/published/occurrences.json')) == 140
    assert sum(bool(p['core_exact_duplicates']) for p in supplement) == 6

    frames = {name: pd.read_csv(OUT / f'{name}.csv') for name in
              ['baseline', 'modifications', 'random_benchmark', 'jhm_restricted', 'jhm_supplement']}
    assert [len(frames[x]) for x in frames] == [1204, 2064, 11400, 1930, 430]
    for name, df in frames.items():
        good = df[df.status.eq('ok')]
        assert good.cost.notna().all(), name
        assert (good.cost >= good.optimal - 1e-6).all(), name
        assert good.basic.all(), name
        assert not good.duplicated([c for c in ['suite', 'problem', 'method', 'variant'] if c in good]).any(), name
        if 'improvement' in good:
            paired = good.dropna(subset=['baseline_cost'])
            assert np.allclose(paired.improvement, paired.baseline_cost-paired.cost), name

    # Recalculate published/random aggregate headlines from the saved per-case rows.
    for _, row in pd.read_csv(OUT / 'summary.csv').iterrows():
        name = {'published_baseline': 'baseline', 'published_modifications': 'modifications',
                'random': 'random_benchmark'}[row.suite]
        df = frames[name]
        selected = df[df.method.eq(row.method)]
        if row.suite != 'random':
            selected = selected[selected.problem.isin(canonical)]
        good = selected[selected.status.eq('ok')]
        assert (len(selected), len(good)) == (row.n, row.successes)
        close(good.gap_pct.mean(), row.mean_gap_pct, (row.suite, row.method, 'mean'))
        assert good.optimal_hit.sum() == row.optimal_hits
        if pd.notna(row.improved):
            assert ((good.improvement > 1e-7).sum(), (good.improvement < -1e-7).sum(),
                    (good.improvement.abs() <= 1e-7).sum()) == (row.improved, row.worsened, row.tied)

    # JHM denominator is the paired successful subset, not all attempted inputs.
    for _, row in pd.read_csv(OUT / 'jhm_summary.csv').iterrows():
        df = frames['jhm_restricted']
        selected = df[df.suite.eq(row.suite) & df.variant.eq(row.variant)]
        if row.suite == 'published':
            selected = selected[selected.problem.isin(canonical)]
        good = selected[selected.status.eq('ok')]
        paired = good[good.baseline_status.eq('ok')]
        assert (len(selected), len(good), len(paired)) == (row.total, row.successful, row.paired_n)
        baseline_gaps = 100 * (paired.baseline_cost - paired.optimal) / paired.optimal
        close(baseline_gaps.mean(), row.paired_baseline_mean_gap_pct, (row.suite, row.variant))
        close(paired.gap_pct.mean(), row.paired_modified_mean_gap_pct, (row.suite, row.variant))
        assert ((paired.improvement > 1e-7).sum(), (paired.improvement.abs() <= 1e-7).sum(),
                (paired.improvement < -1e-7).sum()) == (row.improved, row.tied, row.worsened)

    # Independently recheck saved primal allocations and numerical dual bounds.
    certificate_count = 0
    for cases, filename in [(core, 'optimal_certificates.json'),
                            (random, 'random_optimal_certificates.json'),
                            (supplement, 'jhm_supplement_optimal.json')]:
        certificates = read_json(OUT / filename)
        for p in cases:
            cert = certificates[p['id']]
            C, s, d, _ = balance(p['costs'], p['supply'], p['demand'])
            check = audit(C, s, d, np.asarray(cert['allocation']))
            u, v = np.asarray(cert['row_duals']), np.asarray(cert['column_duals'])
            assert np.max(u[:, None] + v[None, :] - C) <= 1e-7, p['id']
            close(check['cost'], u @ s + v @ d, p['id'])
            close(check['cost'], cert['cost'], p['id'])
            certificate_count += 1

    case_map = {p['id']: p for p in core + random + supplement}
    allocation_count = 0
    for filename in ['baseline_allocations.json', 'modification_allocations.json',
                     'jhm_allocations.json', 'jhm_supplement_allocations.json']:
        for key, result in read_json(OUT / filename).items():
            parts = key.split('::')
            pid = parts[1] if filename == 'jhm_allocations.json' else parts[0]
            p = case_map[pid]
            C, s, d, _ = balance(p['costs'], p['supply'], p['demand'])
            check = audit(C, s, d, np.asarray(result['allocation']))
            close(check['cost'], result['cost'], key)
            assert check['feasible'] and check['basic'], key
            allocation_count += 1

    # Report navigation and Markdown tables: do not scan raw extracted source text.
    files = [p for folder in ['report', 'modifications', 'experiments']
             for p in (ROOT / folder).glob('*.md')] + [ROOT / x for x in
             ['README.md', 'progress.md', 'paper_inventory.md', 'STRUKTUR_FOLDER.md', 'FILE_INDEX.md']]
    problems = []
    for path in files:
        fenced = False
        columns = None
        for lineno, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if line.startswith('```'):
                fenced = not fenced
            if fenced:
                continue
            if line.startswith('|'):
                count = len(re.split(r'(?<!\\)\|', line)) - 2
                if columns is None:
                    columns = count
                elif count != columns:
                    problems.append(f'{path.name}:{lineno}: table columns {count} != {columns}')
            else:
                columns = None
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', line):
                if target.startswith(('http://', 'https://', '#', 'mailto:')):
                    continue
                local = unquote(target.split('#', 1)[0]).strip('<>')
                if not (path.parent / local).exists():
                    problems.append(f'{path.name}:{lineno}: missing link {local}')
    assert not problems, '\n'.join(problems)
    report = (ROOT / 'report/research_report.md').read_text(encoding='utf-8')
    assert [int(x) for x in re.findall(r'^## (\d+)\.', report, re.M)] == list(range(1, 36))

    # Exact manual certificate in the presentation example.
    p = next(p for p in core if p['id'] == 'L05_Example1')
    C = np.asarray(p['costs']); u = np.array([1, 0, 5, 2]); v = np.array([5, -1, 0, 1])
    assert np.all(u[:, None] + v[None, :] <= C)
    assert u @ p['supply'] + v @ p['demand'] == 985

    message = (f'PASS: dataset/run counts; all saved aggregate and JHM paired statistics; '
               f'{certificate_count} primal-dual certificates; {allocation_count} saved allocations; '
               f'{len(files)} report/navigation files; table columns and local links; '
               '35 report sections; exact THP dual certificate. No experiments retuned.\n')
    (OUT / 'artifact_audit.txt').write_text(message, encoding='utf-8')
    print(message)


if __name__ == '__main__':
    main()
