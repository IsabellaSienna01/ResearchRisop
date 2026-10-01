# Complete aggregate experimental results

Published summaries use 84 matrices after balancing-equivalent duplicates are removed. Raw runs include 86 matrices. Random uses 300 fixed problems. Gaps are percentages, sample standard deviation; optimal hit denominator includes failures. Successful-only means are not fair rankings for methods with failures.

## published_baseline

| method | n | failures | mean_gap_pct | median_gap_pct | max_gap_pct | std_gap_pct | optimal_hits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NWCM | 84 | 0 | 35.0831 | 21.8914 | 226.9307 | 45.3675 | 7 |
| LCM | 84 | 0 | 9.2633 | 5.1019 | 66.9856 | 12.0537 | 15 |
| VAM | 84 | 0 | 3.7178 | 0 | 21.1382 | 5.3724 | 44 |
| LDVAM | 84 | 0 | 3.6352 | 0 | 28.7081 | 5.8281 | 45 |
| RAM | 84 | 0 | 2.3736 | 0 | 49.3069 | 6.3908 | 46 |
| TDM1 | 84 | 0 | 2.8007 | 0 | 21.1382 | 4.7171 | 44 |
| TDM2 | 84 | 0 | 3.7466 | 0.8553 | 26.6667 | 5.9728 | 34 |
| TDSM | 84 | 0 | 2.2851 | 0 | 16.8975 | 4.007 | 46 |
| THP | 84 | 0 | 7.0225 | 3.1303 | 72.7273 | 11.1783 | 26 |
| SSM | 84 | 0 | 2.6031 | 0 | 28.2051 | 5.0726 | 51 |
| CSM | 84 | 0 | 2.2748 | 0 | 23.0769 | 4.2525 | 51 |
| RBSM | 84 | 0 | 2.5392 | 0 | 23.0769 | 4.4978 | 49 |
| BCE | 84 | 15 | 1.6345 | 0 | 28.2051 | 4.2917 | 48 |
| MRM | 84 | 0 | 2.7582 | 0 | 26.6667 | 5.1505 | 46 |

## published_modifications

| method | n | failures | mean_gap_pct | median_gap_pct | max_gap_pct | std_gap_pct | optimal_hits | improved | worsened | tied |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LCM_tie_allocation | 84 | 0 | 7.6816 | 5.1397 | 52.6531 | 8.8694 | 15 | 11 | 7 | 66 |
| VAM_tie_cost | 84 | 0 | 3.6352 | 0 | 28.7081 | 5.8281 | 45 | 6 | 2 | 76 |
| VAM_tie_allocation | 84 | 0 | 3.9025 | 0 | 26.5347 | 5.8224 | 44 | 3 | 7 | 74 |
| VAM_penalty_sqrtA | 84 | 0 | 4.0915 | 1.5527 | 26.5347 | 5.6881 | 34 | 5 | 22 | 57 |
| VAM_penalty_A | 84 | 0 | 4.7388 | 1.9515 | 26.5347 | 6.3939 | 32 | 9 | 31 | 44 |
| TDSM_theta1_5 | 84 | 0 | 2.2822 | 0 | 16.6667 | 3.9805 | 45 | 5 | 8 | 71 |
| LCM_top2_product | 84 | 0 | 9.9511 | 6.0945 | 66.9856 | 11.9002 | 18 | 12 | 21 | 51 |
| LCM_top2_LB | 84 | 0 | 5.5803 | 1.6605 | 63.1579 | 10.2711 | 30 | 42 | 9 | 33 |
| VAM_top2_LB | 84 | 0 | 3.5582 | 0 | 32.1429 | 7.0565 | 47 | 19 | 19 | 46 |
| THP_top2_LB | 84 | 0 | 2.4382 | 0 | 27.381 | 4.5311 | 46 | 43 | 2 | 39 |
| LCM_top2_rollout | 84 | 0 | 4.9477 | 1.0608 | 60.2871 | 9.9343 | 36 | 48 | 0 | 36 |
| LCM_top3_rollout | 84 | 0 | 2.3289 | 0 | 23.0769 | 4.35 | 46 | 62 | 0 | 22 |
| VAM_top2_rollout | 84 | 0 | 0.8763 | 0 | 14.4044 | 2.2791 | 63 | 29 | 0 | 55 |
| VAM_top3_rollout | 84 | 0 | 0.844 | 0 | 14.5631 | 2.6001 | 67 | 32 | 0 | 52 |
| THP_top2_rollout | 84 | 0 | 2.1315 | 0 | 17.8571 | 4.1786 | 52 | 48 | 0 | 36 |
| THP_top3_rollout | 84 | 0 | 1.9044 | 0 | 17.8571 | 4.1594 | 57 | 49 | 0 | 35 |
| THP_top2_LCMcompletion | 84 | 0 | 2.2285 | 0 | 17.8571 | 4.168 | 48 | 45 | 1 | 38 |
| VAM_top2_first_only | 84 | 0 | 1.9812 | 0 | 16.0396 | 3.9971 | 54 | 16 | 0 | 68 |
| THP_top2_first_only | 84 | 0 | 3.8414 | 1.7077 | 28.7129 | 5.4328 | 34 | 27 | 0 | 57 |
| VAM_tieA_top2_rollout | 84 | 0 | 1.1724 | 0 | 21.5311 | 3.2543 | 63 | 28 | 1 | 55 |
| MRM_orientation_ensemble | 84 | 0 | 1.1837 | 0 | 16.8975 | 3.2785 | 66 | 24 | 0 | 60 |
| LCM_score_alpha025 | 84 | 0 | 11.826 | 5.0602 | 120.0957 | 17.3634 | 14 | 25 | 31 | 28 |
| LCM_score_alpha050 | 84 | 0 | 9.727 | 5.3038 | 63.1579 | 12.4535 | 14 | 15 | 18 | 51 |
| LCM_score_alpha075 | 84 | 0 | 8.8636 | 5.1397 | 63.1579 | 11.6791 | 15 | 10 | 8 | 66 |

## random

| method | n | failures | mean_gap_pct | median_gap_pct | max_gap_pct | std_gap_pct | optimal_hits | improved | worsened | tied |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NWCM | 300 | 0 | 130.0788 | 73.5034 | 1288.8889 | 175.2443 | 7 | unavailable | unavailable | unavailable |
| LCM | 300 | 0 | 30.3971 | 10.5063 | 446.2147 | 58.7581 | 53 | unavailable | unavailable | unavailable |
| VAM | 300 | 0 | 12.9678 | 1.375 | 701.634 | 48.3879 | 128 | unavailable | unavailable | unavailable |
| LDVAM | 300 | 0 | 14.4054 | 1.1654 | 701.634 | 54.3888 | 129 | unavailable | unavailable | unavailable |
| RAM | 300 | 0 | 13.0211 | 3.6492 | 208.2418 | 23.5694 | 107 | unavailable | unavailable | unavailable |
| TDM1 | 300 | 0 | 9.2592 | 3.4861 | 146.6096 | 17.0378 | 92 | unavailable | unavailable | unavailable |
| TDM2 | 300 | 0 | 8.5334 | 3.1357 | 78.1841 | 13.2518 | 92 | unavailable | unavailable | unavailable |
| TDSM | 300 | 0 | 10.1453 | 4.1124 | 146.6096 | 17.4254 | 92 | unavailable | unavailable | unavailable |
| THP | 300 | 0 | 13.6475 | 6.3785 | 150.0898 | 20.0676 | 59 | unavailable | unavailable | unavailable |
| SSM | 300 | 0 | 14.6674 | 4.7766 | 245.9964 | 28.1299 | 80 | unavailable | unavailable | unavailable |
| CSM | 300 | 0 | 16.4253 | 7.6699 | 316.3054 | 30.6811 | 71 | unavailable | unavailable | unavailable |
| RBSM | 300 | 0 | 23.0636 | 8.605 | 701.634 | 55.3468 | 66 | unavailable | unavailable | unavailable |
| BCE | 300 | 96 | 9.0752 | 0.882 | 232.5309 | 22.4037 | 89 | unavailable | unavailable | unavailable |
| MRM | 300 | 0 | 10.904 | 4.6039 | 146.6096 | 16.4726 | 85 | unavailable | unavailable | unavailable |
| LCM_tie_allocation | 300 | 0 | 27.0494 | 10.0929 | 446.2147 | 50.6494 | 54 | 48 | 36 | 216 |
| VAM_tie_cost | 300 | 0 | 14.4054 | 1.1654 | 701.634 | 54.3888 | 129 | 27 | 28 | 245 |
| VAM_tie_allocation | 300 | 0 | 14.2936 | 1.4574 | 701.634 | 49.5879 | 126 | 34 | 38 | 228 |
| VAM_penalty_sqrtA | 300 | 0 | 15.3143 | 2.6218 | 701.634 | 49.2878 | 101 | 53 | 107 | 140 |
| VAM_penalty_A | 300 | 0 | 15.3294 | 3.7327 | 701.634 | 48.018 | 78 | 61 | 135 | 104 |
| TDSM_theta1_5 | 300 | 0 | 9.7667 | 3.5507 | 146.6096 | 17.3328 | 91 | 25 | 16 | 259 |
| LCM_top2_product | 300 | 0 | 31.4012 | 11.4299 | 390.0208 | 55.894 | 43 | 55 | 118 | 127 |
| LCM_top2_LB | 300 | 0 | 24.9873 | 6.3102 | 701.634 | 61.7537 | 79 | 135 | 48 | 117 |
| VAM_top2_LB | 300 | 0 | 14.5462 | 3.2062 | 227.1218 | 31.9877 | 96 | 43 | 113 | 144 |
| THP_top2_LB | 300 | 0 | 9.982 | 3.2518 | 122.9859 | 16.8774 | 94 | 149 | 43 | 108 |
| LCM_top2_rollout | 300 | 0 | 16.1721 | 4.4026 | 289.2857 | 31.5372 | 95 | 174 | 0 | 126 |
| LCM_top3_rollout | 300 | 0 | 11.9323 | 1.9505 | 186.6523 | 23.9653 | 121 | 208 | 0 | 92 |
| VAM_top2_rollout | 300 | 0 | 5.0325 | 0 | 152.0633 | 14.6169 | 154 | 117 | 0 | 183 |
| VAM_top3_rollout | 300 | 0 | 2.9521 | 0 | 69.9035 | 7.3897 | 170 | 140 | 0 | 160 |
| THP_top2_rollout | 300 | 0 | 6.2636 | 1.1118 | 101.167 | 11.5555 | 122 | 182 | 0 | 118 |
| THP_top3_rollout | 300 | 0 | 5.3713 | 0.7524 | 83.7662 | 9.697 | 130 | 189 | 0 | 111 |
| THP_top2_LCMcompletion | 300 | 0 | 7.2017 | 1.6755 | 83.7662 | 12.1325 | 112 | 175 | 16 | 109 |
| VAM_top2_first_only | 300 | 0 | 10.1028 | 0.7494 | 227.1218 | 27.2086 | 135 | 17 | 0 | 283 |
| THP_top2_first_only | 300 | 0 | 11.4954 | 5.0592 | 150.0898 | 17.5704 | 79 | 56 | 0 | 244 |
| VAM_tieA_top2_rollout | 300 | 0 | 5.9656 | 0 | 222.8167 | 18.6283 | 160 | 117 | 12 | 171 |
| MRM_orientation_ensemble | 300 | 0 | 6.1589 | 1.6892 | 67.8571 | 9.4707 | 116 | 111 | 0 | 189 |
| LCM_score_alpha025 | 300 | 0 | 31.9275 | 10.9516 | 869.0176 | 69.1617 | 41 | 109 | 116 | 75 |
| LCM_score_alpha050 | 300 | 0 | 26.6556 | 10.1958 | 319.3103 | 46.3178 | 45 | 78 | 68 | 154 |
| LCM_score_alpha075 | 300 | 0 | 27.4111 | 10.1209 | 446.2147 | 52.2199 | 53 | 56 | 42 | 202 |

