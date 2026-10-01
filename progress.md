# Research progress

Updated: **2026-10-01, Asia/Jakarta**. Latest user instruction: skip IHW, continue JHM, and write all research results with actionable conclusions. No clarification or permission is pending. Main deliverable: [Indonesian synthesis](report/hasil_riset_dan_kesimpulan.md); detailed [35-section report](report/research_report.md).

## Completed work and scope limits by stage

| Requested stages | Status | Evidence / limit |
|---|---|---|
| Local inventory before external research | Completed; later correction recorded | Five supplied PDFs recursively inventoried; second pass recovered L01 real 2x94, so ten complete local source examples are now identified |
| 0: terminology | Completed for identified versions; IHW skipped | IBFS DOI=BCE; TDM1/TDM2 distinct; SSM and MRM ambiguity explained; TDSM formula verified but long-name wording qualified |
| 1–2: discovery and classification | Completed documented search, not exhaustive literature coverage | Publisher/original sources, modifications, comparisons, prior art, source classes and access levels recorded |
| 3–5: algorithms, purpose, weakness | Completed for documented contracts; explicit unresolved branches | Constructive baselines and repair interpretations described; full JHM multi-excess and BCE bookkeeping/unbalanced contract unresolved |
| 6: benchmarks | Core and JHM addendum extracted | 140 core source occurrences -> 86 raw -> 84 canonical; ten supplemental source occurrences, six exact core duplicates; all input conflicts retained |
| 7–10: reproduction, LP, metrics, comparison | Completed for implemented inputs | 1,204 core baseline runs; 207 historical claim comparisons; LP primal/dual checks; failure-aware comparisons |
| 11–18: modifications, ties, candidates, look-ahead, weights, novelty | Completed catalog and selected experiments | 2–4 directions per identified method where responsible; untested ideas labelled; general rollout/top-k/weighting not claimed novel |
| 19–22: implementations, modification experiments, ablation, published tests | Completed selected scope | 14 core configurations, 24 variations, 2,064 raw published modification runs; all failed/negative/tied cases retained |
| 23–25: random tests, robustness, complexity | Completed | 300 saved common inputs; 11,400 core random runs; strata, worst cases, source sensitivity, 30-case controlled timings |
| JHM follow-up | Implemented and tested only verified restricted branch | 1,930 attempts, baseline coverage 55/84 and 73/300; four variants; separate 430-run supplemental audit; full JHM not claimed reproduced |
| 26–30: feasibility, shortlist, designs, first experiments, roadmap | Completed evidence-based synthesis | THP/VAM main directions, MRM conditional; manual 4x4 with dual certificate; JHM cap not robust |

## JHM follow-up findings

- E18 DOI verified as 10.20527/epsilon.v15i1.2876. Publisher metadata and selected indexed pages accessed; full PDF still unavailable. E21 is a cover only. E22 contains public chapters 1–2 only; its complete-file endpoint returns HTTP 401.
- `JHM_single` implements the documented single-excess selection branch. Multi-excess dependency decisions are marked `unverified`, without an invented fallback. All successful outputs are feasible/basic.
- L01 JHM 460 reproduced; receiver cap reaches LP optimum 435. L03 higher-donor-cost tie gives 473 vs source 475; a separately recorded index tie gives 475. Matching cost does not uniquely verify an algorithm.
- Receiver cap: paired core 15 improved/28 tied/12 worsened; paired random 14/39/20. Top-2 completion helps the covered subset, but coverage is too limited for full-method ranking.
- E19 Appendix A's nine matrices extracted; its mentioned Appendix B is absent in the obtained PDF. Deshmukh's literal demand 40 preserved despite conflicting older sources.
- L01 real 2x94: BCE/VAM/restricted JHM reproduce 12,175,097, LP confirms it; TDM1 reproduces 12,208,071. Added separately rather than changing the frozen core suite.

## Remaining limitations, not hidden completed tasks

1. **IHW is intentionally excluded**, not awaiting further user input.
2. Full JHM 2015 multi-excess dependency and third-cost rules still require a complete accessible source. No claim that the restricted implementation covers the full method.
3. BCE's unresolved successor bookkeeping/unbalanced branch causes failures or unavailability; CSM/RBSM narrative, pseudocode and author code are not identical. Successful-only mean gaps do not establish superiority.
4. The full source suites with 35/45/42 labels were not all reconstructed. Unknown matrix identity stays unlinked; malformed/conflicting data remain explicit.
5. Hosseini's larger fixed matrices, three MRM high-dimensional tables needing visual validation, and missing E19 Appendix B remain outside accepted benchmarks.
6. SSM/CSM/RBSM/RAM/NWCM modifications in the catalog are design opportunities, not claimed tested improvements. DSO-VAM and other extra inspiration methods were not all implemented; they do not indefinitely expand the main project.
7. Novelty is not established. Some original/full comparative papers were inaccessible. No source was contacted and no restricted-access material was bypassed.
8. One random seed and selected distributions, small Python timing sample, no end-to-end simplex pivot study, and no industrial generalization proof.

The available evidence is sufficient for a qualified undergraduate project choice, not a claim that every paper and every suggested modification has been completely reproduced. Next optional research is source reconciliation or a focused new experiment, not repetition of the completed runs.

## Final artifact audit

`python -m research.experiments.audit_artifacts` passed: dataset/run counts and all saved aggregate statistics agree; 396 primal–dual certificates and 4,333 saved allocations independently rechecked; 18 report/navigation files have valid local links and table columns; the main report has all 35 requested sections; the manual THP certificate proves cost 985. This checks saved evidence without rerunning or retuning experiments. Output: [artifact_audit.txt](results/artifact_audit.txt). Earlier algorithm checks remain in [verification.txt](results/verification.txt) and [jhm_verification.txt](results/jhm_verification.txt).

## Documentation follow-up, 2026-10-02

User requested separate steps/references/originality explanations for the three shortlisted modifications, confirmation of executable code, and a complete guide to research files. Added [modification README](modifications/README.md) plus separate VAM/THP/MRM Markdown; each labels the exact policy as an adaptation/combination with novelty unestablished. The existing `variants.py` algorithms were not changed. Added a demo CLI for single examples and [folder guide](STRUKTUR_FOLDER.md) with a generated [file index](FILE_INDEX.md). MRCM DOI independently verified from its publisher. The expanded artifact audit includes these documents. Experimental costs and frozen dataset selection are unchanged.

The subsequent request for a shared paper-style numerical example is fulfilled in section 6 of each modification document and the folder README. All use **L05_Example1**, with full residual tableaux, penalty/candidate evaluation, every tested completion, MRM orientation paths (including zero-allocation eliminations), final allocation and optimality certificate. Results: VAM 1095 -> 985, THP 1045 -> 985, MRM 1045 -> 985. MRM's baseline on this input is our cross-paper computation, not a published THP-paper claim. The [example generator](modifications/worked_example.py) validates each step and stores [structured evidence](results/worked_example_L05_Example1.json); no heuristic or core result was changed.
