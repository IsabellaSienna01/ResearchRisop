# Ablation and component changes

Compare against the corresponding baseline, plus first-only vs every-decision rollout. The combined VAM tie+rollout uses its changed tie policy during completion, so its guarantee is relative to that policy, not index-tie VAM.

| suite | method | mean_gap_pct | optimal_hits | improved | worsened |
| --- | --- | --- | --- | --- | --- |
| published_modifications | VAM_tie_allocation | 3.9025 | 44 | 3 | 7 |
| published_modifications | VAM_penalty_A | 4.7388 | 32 | 9 | 31 |
| published_modifications | VAM_top2_LB | 3.5582 | 47 | 19 | 19 |
| published_modifications | THP_top2_LB | 2.4382 | 46 | 43 | 2 |
| published_modifications | VAM_top2_rollout | 0.8763 | 63 | 29 | 0 |
| published_modifications | VAM_top3_rollout | 0.844 | 67 | 32 | 0 |
| published_modifications | THP_top2_rollout | 2.1315 | 52 | 48 | 0 |
| published_modifications | THP_top3_rollout | 1.9044 | 57 | 49 | 0 |
| published_modifications | THP_top2_LCMcompletion | 2.2285 | 48 | 45 | 1 |
| published_modifications | VAM_top2_first_only | 1.9812 | 54 | 16 | 0 |
| published_modifications | THP_top2_first_only | 3.8414 | 34 | 27 | 0 |
| published_modifications | VAM_tieA_top2_rollout | 1.1724 | 63 | 28 | 1 |
| random | VAM_tie_allocation | 14.2936 | 126 | 34 | 38 |
| random | VAM_penalty_A | 15.3294 | 78 | 61 | 135 |
| random | VAM_top2_LB | 14.5462 | 96 | 43 | 113 |
| random | THP_top2_LB | 9.982 | 94 | 149 | 43 |
| random | VAM_top2_rollout | 5.0325 | 154 | 117 | 0 |
| random | VAM_top3_rollout | 2.9521 | 170 | 140 | 0 |
| random | THP_top2_rollout | 6.2636 | 122 | 182 | 0 |
| random | THP_top3_rollout | 5.3713 | 130 | 189 | 0 |
| random | THP_top2_LCMcompletion | 7.2017 | 112 | 175 | 16 |
| random | VAM_top2_first_only | 10.1028 | 135 | 17 | 0 |
| random | THP_top2_first_only | 11.4954 | 79 | 56 | 0 |
| random | VAM_tieA_top2_rollout | 5.9656 | 160 | 117 | 12 |
