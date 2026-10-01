# Additional JHM source audit

These ten source occurrences were extracted during the JHM follow-up and are separate from the frozen 84-case comparison. Exact core duplicates are identified below; do not count them as independent extra validation. The literal Deshmukh transcription is retained for error analysis. No metaheuristic is introduced.
## Published claim reproduction

| problem | method | published_cost | reproduced_cost | status | match |
| --- | --- | --- | --- | --- | --- |
| E19_Srinivasan | JHM | 880 | unavailable | unverified | unavailable |
| E19_Srinivasan | VAM | 955 | 955 | ok | True |
| E19_Srinivasan | optimal | 880 | 880 | LP verified | True |
| E19_Sen | JHM | 2146750 | 2146750 | ok | True |
| E19_Sen | VAM | 2164000 | 2164000 | ok | True |
| E19_Sen | optimal | 2146750 | 2146750 | LP verified | True |
| E19_Deshmukh_literal | JHM | 743 | 883 | ok | False |
| E19_Deshmukh_literal | VAM | 779 | 883 | ok | False |
| E19_Deshmukh_literal | optimal | 743 | 743 | LP verified | True |
| E19_Ramadan | JHM | 5600 | 5600 | ok | True |
| E19_Ramadan | VAM | 5600 | 5600 | ok | True |
| E19_Ramadan | optimal | 5600 | 5600 | LP verified | True |
| E19_Kulkarni | JHM | 840 | unavailable | unverified | unavailable |
| E19_Kulkarni | VAM | 880 | 880 | ok | True |
| E19_Kulkarni | optimal | 840 | 840 | LP verified | True |
| E19_Schrenk | JHM | 59 | 59 | ok | True |
| E19_Schrenk | VAM | 59 | 59 | ok | True |
| E19_Schrenk | optimal | 59 | 59 | LP verified | True |
| E19_Samuel | JHM | 28 | 28 | ok | True |
| E19_Samuel | VAM | 28 | 28 | ok | True |
| E19_Samuel | optimal | 28 | 28 | LP verified | True |
| E19_Imam | JHM | 460 | 460 | ok | True |
| E19_Imam | VAM | 475 | 475 | ok | True |
| E19_Imam | optimal | 435 | 435 | LP verified | True |
| E19_Adlakha | JHM | 390 | unavailable | unverified | unavailable |
| E19_Adlakha | VAM | 390 | 390 | ok | True |
| E19_Adlakha | optimal | 390 | 390 | LP verified | True |
| L01_Real2x94 | BCE | 12175097 | 12175097 | ok | True |
| L01_Real2x94 | VAM | 12175097 | 12175097 | ok | True |
| L01_Real2x94 | TDM1 | 12208071 | 12208071 | ok | True |
| L01_Real2x94 | TOCM_MT | 12210362 | unavailable | not implemented | unavailable |
| L01_Real2x94 | JHM | 12175097 | 12175097 | ok | True |
| L01_Real2x94 | optimal | 12175097 | 12175097 | LP verified | True |

## E19_Srinivasan

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: []. 

```json
{
  "costs": [
    [
      3,
      6,
      3,
      4
    ],
    [
      6,
      5,
      11,
      15
    ],
    [
      1,
      3,
      10,
      5
    ]
  ],
  "supply": [
    80,
    90,
    55
  ],
  "demand": [
    70,
    60,
    35,
    60
  ]
}
```

LP optimum: 880.0


## E19_Sen

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: []. 

```json
{
  "costs": [
    [
      60,
      120,
      75,
      180
    ],
    [
      58,
      100,
      60,
      165
    ],
    [
      62,
      110,
      65,
      170
    ],
    [
      65,
      115,
      80,
      175
    ],
    [
      70,
      135,
      85,
      195
    ]
  ],
  "supply": [
    8000,
    9200,
    6250,
    4900,
    6100
  ],
  "demand": [
    5000,
    2000,
    10000,
    6000
  ]
}
```

LP optimum: 2146750.0


## E19_Deshmukh_literal

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: []. Exact printed demand 40; inconsistent with the balanced Deshmukh instance in other sources; sensitivity audit only.

```json
{
  "costs": [
    [
      19,
      30,
      50,
      10
    ],
    [
      70,
      30,
      40,
      60
    ],
    [
      40,
      8,
      70,
      20
    ]
  ],
  "supply": [
    7,
    9,
    18
  ],
  "demand": [
    40,
    8,
    7,
    14
  ]
}
```

LP optimum: 743.0


## E19_Ramadan

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['RBSM_N01']. 

```json
{
  "costs": [
    [
      32,
      40,
      120
    ],
    [
      60,
      68,
      104
    ],
    [
      200,
      80,
      60
    ]
  ],
  "supply": [
    20,
    30,
    45
  ],
  "demand": [
    30,
    35,
    30
  ]
}
```

LP optimum: 5600.0


## E19_Kulkarni

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['EDM_C19']. 

```json
{
  "costs": [
    [
      3,
      4,
      6
    ],
    [
      7,
      3,
      8
    ],
    [
      6,
      4,
      5
    ],
    [
      7,
      5,
      2
    ]
  ],
  "supply": [
    100,
    80,
    90,
    120
  ],
  "demand": [
    110,
    110,
    60
  ]
}
```

LP optimum: 840.0


## E19_Schrenk

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['EDM_C20']. 

```json
{
  "costs": [
    [
      3,
      6,
      1,
      5
    ],
    [
      7,
      9,
      2,
      7
    ],
    [
      2,
      4,
      2,
      1
    ]
  ],
  "supply": [
    6,
    6,
    6
  ],
  "demand": [
    4,
    5,
    4,
    5
  ]
}
```

LP optimum: 59.0


## E19_Samuel

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['RBSM_N02']. 

```json
{
  "costs": [
    [
      1,
      2,
      3,
      4
    ],
    [
      4,
      3,
      2,
      0
    ],
    [
      0,
      2,
      2,
      1
    ]
  ],
  "supply": [
    6,
    8,
    10
  ],
  "demand": [
    4,
    6,
    8,
    6
  ]
}
```

LP optimum: 28.0


## E19_Imam

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['L01_Table2']. 

```json
{
  "costs": [
    [
      10,
      2,
      20,
      11
    ],
    [
      12,
      7,
      9,
      20
    ],
    [
      4,
      14,
      16,
      18
    ]
  ],
  "supply": [
    15,
    25,
    10
  ],
  "demand": [
    5,
    15,
    15,
    15
  ]
}
```

LP optimum: 435.0


## E19_Adlakha

Source E19, Appendix A p29; Table 8 p23. Core exact duplicates: ['EDM_C22']. 

```json
{
  "costs": [
    [
      2,
      1,
      3,
      2,
      2
    ],
    [
      3,
      2,
      1,
      1,
      1
    ],
    [
      5,
      4,
      2,
      1,
      3
    ],
    [
      7,
      5,
      5,
      3,
      1
    ]
  ],
  "supply": [
    20,
    70,
    30,
    60
  ],
  "demand": [
    50,
    30,
    30,
    50,
    20
  ]
}
```

LP optimum: 390.0


## L01_Real2x94

Source L01, p2306, real application. Core exact duplicates: []. Directly extracted from supplied PDF; numerical page visually inspected.

```json
{
  "costs": [
    [
      22,
      38,
      32,
      17,
      31,
      15,
      23,
      25,
      25,
      20,
      33,
      30,
      18,
      12,
      23,
      18,
      26,
      20,
      15,
      18,
      15,
      25,
      28,
      23,
      16,
      18,
      21,
      28,
      20,
      20,
      25,
      18,
      18,
      18,
      25,
      27,
      21,
      25,
      23,
      26,
      33,
      38,
      29,
      17,
      38,
      17,
      39,
      39,
      22,
      22,
      35,
      25,
      28,
      31,
      33,
      20,
      36,
      31,
      23,
      27,
      25,
      35,
      30,
      31,
      28,
      27,
      28,
      30,
      27,
      54,
      43,
      52,
      56,
      46,
      59,
      53,
      40,
      58,
      44,
      51,
      40,
      43,
      45,
      49,
      48,
      57,
      46,
      46,
      60,
      61,
      66,
      59,
      55,
      56
    ],
    [
      26,
      41,
      36,
      21,
      35,
      20,
      27,
      30,
      28,
      25,
      38,
      34,
      23,
      15,
      20,
      15,
      23,
      18,
      14,
      17,
      13,
      23,
      25,
      25,
      17,
      23,
      23,
      33,
      18,
      19,
      28,
      23,
      20,
      18,
      25,
      31,
      20,
      25,
      25,
      23,
      39,
      36,
      28,
      12,
      33,
      14,
      38,
      38,
      20,
      28,
      33,
      28,
      26,
      28,
      31,
      17,
      38,
      30,
      30,
      25,
      22,
      33,
      26,
      29,
      31,
      34,
      28,
      33,
      31,
      49,
      38,
      49,
      52,
      43,
      56,
      49,
      36,
      54,
      40,
      46,
      36,
      39,
      41,
      46,
      44,
      54,
      41,
      43,
      57,
      57,
      62,
      55,
      52,
      51
    ]
  ],
  "supply": [
    281820,
    136731
  ],
  "demand": [
    3071,
    4187,
    1155,
    3438,
    6851,
    3441,
    5351,
    20838,
    2752,
    6363,
    2838,
    2695,
    37543,
    6595,
    2611,
    0,
    0,
    2859,
    622,
    2113,
    4599,
    6339,
    249,
    4727,
    17334,
    4391,
    25700,
    1519,
    3029,
    2207,
    46729,
    3084,
    3922,
    1381,
    961,
    3098,
    1078,
    2910,
    1700,
    4848,
    0,
    0,
    0,
    10441,
    0,
    4724,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    9820,
    0,
    0,
    0,
    0,
    6215,
    0,
    0,
    0,
    14221,
    1503,
    2137,
    501,
    562,
    6626,
    1494,
    5878,
    5338,
    611,
    1117,
    472,
    1814,
    1227,
    1229,
    1724,
    3743,
    7922,
    281,
    689,
    7822,
    1307,
    1012,
    2395,
    1150,
    456,
    4123,
    528,
    21067,
    33274
  ]
}
```

LP optimum: 12175097.0


## Every computed result

| problem | method | optimal | cost | status | basic | gap | gap_pct | accuracy | optimal_hit | seconds | error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E19_Srinivasan | NWCM | 880 | 1255 | ok | True | 375 | 42.6136 | 70.1195 | False | 0.0003 | unavailable |
| E19_Srinivasan | LCM | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0001 | unavailable |
| E19_Srinivasan | VAM | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0003 | unavailable |
| E19_Srinivasan | LDVAM | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0002 | unavailable |
| E19_Srinivasan | RAM | 880 | 1000 | ok | True | 120 | 13.6364 | 88 | False | 0.0002 | unavailable |
| E19_Srinivasan | TDM1 | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Srinivasan | TDM2 | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Srinivasan | TDSM | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Srinivasan | THP | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0004 | unavailable |
| E19_Srinivasan | SSM | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Srinivasan | CSM | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Srinivasan | RBSM | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Srinivasan | BCE | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Srinivasan | MRM | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0001 | unavailable |
| E19_Srinivasan | LCM_tie_allocation | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0001 | unavailable |
| E19_Srinivasan | VAM_tie_cost | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.003 | unavailable |
| E19_Srinivasan | VAM_tie_allocation | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0002 | unavailable |
| E19_Srinivasan | VAM_penalty_sqrtA | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0002 | unavailable |
| E19_Srinivasan | VAM_penalty_A | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0002 | unavailable |
| E19_Srinivasan | TDSM_theta1_5 | 880 | 880 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Srinivasan | LCM_top2_product | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0001 | unavailable |
| E19_Srinivasan | LCM_top2_LB | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0003 | unavailable |
| E19_Srinivasan | VAM_top2_LB | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0004 | unavailable |
| E19_Srinivasan | THP_top2_LB | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0005 | unavailable |
| E19_Srinivasan | LCM_top2_rollout | 880 | 985 | ok | True | 105 | 11.9318 | 89.3401 | False | 0.0007 | unavailable |
| E19_Srinivasan | LCM_top3_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0007 | unavailable |
| E19_Srinivasan | VAM_top2_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0012 | unavailable |
| E19_Srinivasan | VAM_top3_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0011 | unavailable |
| E19_Srinivasan | THP_top2_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0009 | unavailable |
| E19_Srinivasan | THP_top3_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0009 | unavailable |
| E19_Srinivasan | THP_top2_LCMcompletion | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0007 | unavailable |
| E19_Srinivasan | VAM_top2_first_only | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0007 | unavailable |
| E19_Srinivasan | THP_top2_first_only | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0005 | unavailable |
| E19_Srinivasan | VAM_tieA_top2_rollout | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0008 | unavailable |
| E19_Srinivasan | MRM_orientation_ensemble | 880 | 910 | ok | True | 30 | 3.4091 | 96.7033 | False | 0.0003 | unavailable |
| E19_Srinivasan | LCM_score_alpha025 | 880 | 1605 | ok | True | 725 | 82.3864 | 54.8287 | False | 0.0003 | unavailable |
| E19_Srinivasan | LCM_score_alpha050 | 880 | 955 | ok | True | 75 | 8.5227 | 92.1466 | False | 0.0002 | unavailable |
| E19_Srinivasan | LCM_score_alpha075 | 880 | 1075 | ok | True | 195 | 22.1591 | 81.8605 | False | 0.0002 | unavailable |
| E19_Srinivasan | JHM_single | 880 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0.0001 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Srinivasan | JHM_cap_receiver | 880 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Srinivasan | JHM_net_tie | 880 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Srinivasan | JHM_cap_net_tie | 880 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Srinivasan | JHM_top2_completion | 880 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Sen | NWCM | 2146750 | 2174000 | ok | True | 27250 | 1.2694 | 98.7466 | False | 0.0002 | unavailable |
| E19_Sen | LCM | 2146750 | 2383250 | ok | True | 236500 | 11.0167 | 90.0766 | False | 0.0002 | unavailable |
| E19_Sen | VAM | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0003 | unavailable |
| E19_Sen | LDVAM | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0003 | unavailable |
| E19_Sen | RAM | 2146750 | 2200000 | ok | True | 53250 | 2.4805 | 97.5795 | False | 0.0003 | unavailable |
| E19_Sen | TDM1 | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.0003 | unavailable |
| E19_Sen | TDM2 | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.0004 | unavailable |
| E19_Sen | TDSM | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.0003 | unavailable |
| E19_Sen | THP | 2146750 | 2301350 | ok | True | 154600 | 7.2016 | 93.2822 | False | 0.0004 | unavailable |
| E19_Sen | SSM | 2146750 | 2286100 | ok | True | 139350 | 6.4912 | 93.9045 | False | 0.0003 | unavailable |
| E19_Sen | CSM | 2146750 | 2210500 | ok | True | 63750 | 2.9696 | 97.116 | False | 0.0002 | unavailable |
| E19_Sen | RBSM | 2146750 | 2210500 | ok | True | 63750 | 2.9696 | 97.116 | False | 0.0002 | unavailable |
| E19_Sen | BCE | 2146750 | unavailable | failed | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | NotImplementedError: BCE unbalanced branch/model not sufficiently unambiguous; no dummy substitution |
| E19_Sen | MRM | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0004 | unavailable |
| E19_Sen | LCM_tie_allocation | 2146750 | 2404500 | ok | True | 257750 | 12.0065 | 89.2805 | False | 0.0002 | unavailable |
| E19_Sen | VAM_tie_cost | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0006 | unavailable |
| E19_Sen | VAM_tie_allocation | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0004 | unavailable |
| E19_Sen | VAM_penalty_sqrtA | 2146750 | 2322000 | ok | True | 175250 | 8.1635 | 92.4526 | False | 0.0004 | unavailable |
| E19_Sen | VAM_penalty_A | 2146750 | 2322000 | ok | True | 175250 | 8.1635 | 92.4526 | False | 0.0003 | unavailable |
| E19_Sen | TDSM_theta1_5 | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.0003 | unavailable |
| E19_Sen | LCM_top2_product | 2146750 | 2402250 | ok | True | 255500 | 11.9017 | 89.3641 | False | 0.0002 | unavailable |
| E19_Sen | LCM_top2_LB | 2146750 | 2387000 | ok | True | 240250 | 11.1913 | 89.9351 | False | 0.0004 | unavailable |
| E19_Sen | VAM_top2_LB | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0009 | unavailable |
| E19_Sen | THP_top2_LB | 2146750 | 2301350 | ok | True | 154600 | 7.2016 | 93.2822 | False | 0.0009 | unavailable |
| E19_Sen | LCM_top2_rollout | 2146750 | 2319500 | ok | True | 172750 | 8.047 | 92.5523 | False | 0.0013 | unavailable |
| E19_Sen | LCM_top3_rollout | 2146750 | 2246500 | ok | True | 99750 | 4.6466 | 95.5598 | False | 0.0012 | unavailable |
| E19_Sen | VAM_top2_rollout | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0024 | unavailable |
| E19_Sen | VAM_top3_rollout | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.003 | unavailable |
| E19_Sen | THP_top2_rollout | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0023 | unavailable |
| E19_Sen | THP_top3_rollout | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0027 | unavailable |
| E19_Sen | THP_top2_LCMcompletion | 2146750 | 2158500 | ok | True | 11750 | 0.5473 | 99.4556 | False | 0.0011 | unavailable |
| E19_Sen | VAM_top2_first_only | 2146750 | 2164000 | ok | True | 17250 | 0.8035 | 99.2029 | False | 0.0008 | unavailable |
| E19_Sen | THP_top2_first_only | 2146750 | 2163200 | ok | True | 16450 | 0.7663 | 99.2396 | False | 0.0007 | unavailable |
| E19_Sen | VAM_tieA_top2_rollout | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0026 | unavailable |
| E19_Sen | MRM_orientation_ensemble | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0005 | unavailable |
| E19_Sen | LCM_score_alpha025 | 2146750 | 2412000 | ok | True | 265250 | 12.3559 | 89.0029 | False | 0.0003 | unavailable |
| E19_Sen | LCM_score_alpha050 | 2146750 | 2412000 | ok | True | 265250 | 12.3559 | 89.0029 | False | 0.0006 | unavailable |
| E19_Sen | LCM_score_alpha075 | 2146750 | 2404500 | ok | True | 257750 | 12.0065 | 89.2805 | False | 0.0005 | unavailable |
| E19_Sen | JHM_single | 2146750 | 2146750 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Sen | JHM_cap_receiver | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0004 | unavailable |
| E19_Sen | JHM_net_tie | 2146750 | 2146750 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Sen | JHM_cap_net_tie | 2146750 | 2159500 | ok | True | 12750 | 0.5939 | 99.4096 | False | 0.0002 | unavailable |
| E19_Sen | JHM_top2_completion | 2146750 | 2146750 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Deshmukh_literal | NWCM | 743 | 1483 | ok | True | 740 | 99.5962 | 50.1011 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | LCM | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | VAM | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | LDVAM | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0005 | unavailable |
| E19_Deshmukh_literal | RAM | 743 | 993 | ok | True | 250 | 33.6474 | 74.8238 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | TDM1 | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | TDM2 | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | TDSM | 743 | 781 | ok | True | 38 | 5.1144 | 95.1344 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | THP | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0005 | unavailable |
| E19_Deshmukh_literal | SSM | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | CSM | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | RBSM | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | BCE | 743 | unavailable | failed | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | NotImplementedError: BCE unbalanced branch/model not sufficiently unambiguous; no dummy substitution |
| E19_Deshmukh_literal | MRM | 743 | 781 | ok | True | 38 | 5.1144 | 95.1344 | False | 0.0001 | unavailable |
| E19_Deshmukh_literal | LCM_tie_allocation | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0001 | unavailable |
| E19_Deshmukh_literal | VAM_tie_cost | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | VAM_tie_allocation | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | VAM_penalty_sqrtA | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | VAM_penalty_A | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0005 | unavailable |
| E19_Deshmukh_literal | TDSM_theta1_5 | 743 | 781 | ok | True | 38 | 5.1144 | 95.1344 | False | 0.0005 | unavailable |
| E19_Deshmukh_literal | LCM_top2_product | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | LCM_top2_LB | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0004 | unavailable |
| E19_Deshmukh_literal | VAM_top2_LB | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0005 | unavailable |
| E19_Deshmukh_literal | THP_top2_LB | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0006 | unavailable |
| E19_Deshmukh_literal | LCM_top2_rollout | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.001 | unavailable |
| E19_Deshmukh_literal | LCM_top3_rollout | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0009 | unavailable |
| E19_Deshmukh_literal | VAM_top2_rollout | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0012 | unavailable |
| E19_Deshmukh_literal | VAM_top3_rollout | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0016 | unavailable |
| E19_Deshmukh_literal | THP_top2_rollout | 743 | 743 | ok | True | 0 | 0 | 100 | True | 0.0013 | unavailable |
| E19_Deshmukh_literal | THP_top3_rollout | 743 | 743 | ok | True | 0 | 0 | 100 | True | 0.0043 | unavailable |
| E19_Deshmukh_literal | THP_top2_LCMcompletion | 743 | 743 | ok | True | 0 | 0 | 100 | True | 0.0009 | unavailable |
| E19_Deshmukh_literal | VAM_top2_first_only | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0004 | unavailable |
| E19_Deshmukh_literal | THP_top2_first_only | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0004 | unavailable |
| E19_Deshmukh_literal | VAM_tieA_top2_rollout | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0015 | unavailable |
| E19_Deshmukh_literal | MRM_orientation_ensemble | 743 | 743 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Deshmukh_literal | LCM_score_alpha025 | 743 | 779 | ok | True | 36 | 4.8452 | 95.3787 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | LCM_score_alpha050 | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | LCM_score_alpha075 | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0003 | unavailable |
| E19_Deshmukh_literal | JHM_single | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0004 | unavailable |
| E19_Deshmukh_literal | JHM_cap_receiver | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | JHM_net_tie | 743 | 883 | ok | True | 140 | 18.8425 | 84.145 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | JHM_cap_net_tie | 743 | 814 | ok | True | 71 | 9.5559 | 91.2776 | False | 0.0002 | unavailable |
| E19_Deshmukh_literal | JHM_top2_completion | 743 | 743 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| E19_Ramadan | NWCM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | LCM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | VAM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | LDVAM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | RAM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | TDM1 | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | TDM2 | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | TDSM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | THP | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | SSM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | CSM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | RBSM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | BCE | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | MRM | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | LCM_tie_allocation | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | VAM_tie_cost | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Ramadan | VAM_tie_allocation | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Ramadan | VAM_penalty_sqrtA | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Ramadan | VAM_penalty_A | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | TDSM_theta1_5 | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Ramadan | LCM_top2_product | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | LCM_top2_LB | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0009 | unavailable |
| E19_Ramadan | VAM_top2_LB | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0009 | unavailable |
| E19_Ramadan | THP_top2_LB | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Ramadan | LCM_top2_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Ramadan | LCM_top3_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Ramadan | VAM_top2_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| E19_Ramadan | VAM_top3_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0011 | unavailable |
| E19_Ramadan | THP_top2_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0007 | unavailable |
| E19_Ramadan | THP_top3_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0007 | unavailable |
| E19_Ramadan | THP_top2_LCMcompletion | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Ramadan | VAM_top2_first_only | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Ramadan | THP_top2_first_only | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Ramadan | VAM_tieA_top2_rollout | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Ramadan | MRM_orientation_ensemble | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Ramadan | LCM_score_alpha025 | 5600 | 7600 | ok | True | 2000 | 35.7143 | 73.6842 | False | 0.0005 | unavailable |
| E19_Ramadan | LCM_score_alpha050 | 5600 | 6880 | ok | True | 1280 | 22.8571 | 81.3953 | False | 0.0006 | unavailable |
| E19_Ramadan | LCM_score_alpha075 | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0007 | unavailable |
| E19_Ramadan | JHM_single | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Ramadan | JHM_cap_receiver | 5600 | 6880 | ok | True | 1280 | 22.8571 | 81.3953 | False | 0.0002 | unavailable |
| E19_Ramadan | JHM_net_tie | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Ramadan | JHM_cap_net_tie | 5600 | 6880 | ok | True | 1280 | 22.8571 | 81.3953 | False | 0.0001 | unavailable |
| E19_Ramadan | JHM_top2_completion | 5600 | 5600 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Kulkarni | NWCM | 840 | 1010 | ok | True | 170 | 20.2381 | 83.1683 | False | 0.0002 | unavailable |
| E19_Kulkarni | LCM | 840 | 1210 | ok | True | 370 | 44.0476 | 69.4215 | False | 0.0001 | unavailable |
| E19_Kulkarni | VAM | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0003 | unavailable |
| E19_Kulkarni | LDVAM | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0003 | unavailable |
| E19_Kulkarni | RAM | 840 | 840 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Kulkarni | TDM1 | 840 | 980 | ok | True | 140 | 16.6667 | 85.7143 | False | 0.0002 | unavailable |
| E19_Kulkarni | TDM2 | 840 | 980 | ok | True | 140 | 16.6667 | 85.7143 | False | 0.0004 | unavailable |
| E19_Kulkarni | TDSM | 840 | 950 | ok | True | 110 | 13.0952 | 88.4211 | False | 0.0002 | unavailable |
| E19_Kulkarni | THP | 840 | 1070 | ok | True | 230 | 27.381 | 78.5047 | False | 0.0005 | unavailable |
| E19_Kulkarni | SSM | 840 | 860 | ok | True | 20 | 2.381 | 97.6744 | False | 0.0002 | unavailable |
| E19_Kulkarni | CSM | 840 | 840 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Kulkarni | RBSM | 840 | 900 | ok | True | 60 | 7.1429 | 93.3333 | False | 0.0001 | unavailable |
| E19_Kulkarni | BCE | 840 | unavailable | failed | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | NotImplementedError: BCE unbalanced branch/model not sufficiently unambiguous; no dummy substitution |
| E19_Kulkarni | MRM | 840 | 840 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Kulkarni | LCM_tie_allocation | 840 | 990 | ok | True | 150 | 17.8571 | 84.8485 | False | 0.0001 | unavailable |
| E19_Kulkarni | VAM_tie_cost | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0003 | unavailable |
| E19_Kulkarni | VAM_tie_allocation | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0003 | unavailable |
| E19_Kulkarni | VAM_penalty_sqrtA | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0003 | unavailable |
| E19_Kulkarni | VAM_penalty_A | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0002 | unavailable |
| E19_Kulkarni | TDSM_theta1_5 | 840 | 980 | ok | True | 140 | 16.6667 | 85.7143 | False | 0.0002 | unavailable |
| E19_Kulkarni | LCM_top2_product | 840 | 1210 | ok | True | 370 | 44.0476 | 69.4215 | False | 0.0002 | unavailable |
| E19_Kulkarni | LCM_top2_LB | 840 | 1070 | ok | True | 230 | 27.381 | 78.5047 | False | 0.0003 | unavailable |
| E19_Kulkarni | VAM_top2_LB | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0004 | unavailable |
| E19_Kulkarni | THP_top2_LB | 840 | 1070 | ok | True | 230 | 27.381 | 78.5047 | False | 0.0005 | unavailable |
| E19_Kulkarni | LCM_top2_rollout | 840 | 980 | ok | True | 140 | 16.6667 | 85.7143 | False | 0.0006 | unavailable |
| E19_Kulkarni | LCM_top3_rollout | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0007 | unavailable |
| E19_Kulkarni | VAM_top2_rollout | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0012 | unavailable |
| E19_Kulkarni | VAM_top3_rollout | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0016 | unavailable |
| E19_Kulkarni | THP_top2_rollout | 840 | 990 | ok | True | 150 | 17.8571 | 84.8485 | False | 0.0017 | unavailable |
| E19_Kulkarni | THP_top3_rollout | 840 | 990 | ok | True | 150 | 17.8571 | 84.8485 | False | 0.0013 | unavailable |
| E19_Kulkarni | THP_top2_LCMcompletion | 840 | 990 | ok | True | 150 | 17.8571 | 84.8485 | False | 0.0007 | unavailable |
| E19_Kulkarni | VAM_top2_first_only | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0004 | unavailable |
| E19_Kulkarni | THP_top2_first_only | 840 | 990 | ok | True | 150 | 17.8571 | 84.8485 | False | 0.0006 | unavailable |
| E19_Kulkarni | VAM_tieA_top2_rollout | 840 | 880 | ok | True | 40 | 4.7619 | 95.4545 | False | 0.0012 | unavailable |
| E19_Kulkarni | MRM_orientation_ensemble | 840 | 840 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Kulkarni | LCM_score_alpha025 | 840 | 1350 | ok | True | 510 | 60.7143 | 62.2222 | False | 0.0003 | unavailable |
| E19_Kulkarni | LCM_score_alpha050 | 840 | 1310 | ok | True | 470 | 55.9524 | 64.1221 | False | 0.0002 | unavailable |
| E19_Kulkarni | LCM_score_alpha075 | 840 | 1210 | ok | True | 370 | 44.0476 | 69.4215 | False | 0.0003 | unavailable |
| E19_Kulkarni | JHM_single | 840 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0.0001 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Kulkarni | JHM_cap_receiver | 840 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Kulkarni | JHM_net_tie | 840 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Kulkarni | JHM_cap_net_tie | 840 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Kulkarni | JHM_top2_completion | 840 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Schrenk | NWCM | 59 | 64 | ok | True | 5 | 8.4746 | 92.1875 | False | 0.0004 | unavailable |
| E19_Schrenk | LCM | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | VAM | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | LDVAM | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | RAM | 59 | 64 | ok | True | 5 | 8.4746 | 92.1875 | False | 0.0002 | unavailable |
| E19_Schrenk | TDM1 | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | TDM2 | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | TDSM | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | THP | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | SSM | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0001 | unavailable |
| E19_Schrenk | CSM | 59 | 63 | ok | True | 4 | 6.7797 | 93.6508 | False | 0.0001 | unavailable |
| E19_Schrenk | RBSM | 59 | 63 | ok | True | 4 | 6.7797 | 93.6508 | False | 0.0001 | unavailable |
| E19_Schrenk | BCE | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0001 | unavailable |
| E19_Schrenk | MRM | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Schrenk | LCM_tie_allocation | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0001 | unavailable |
| E19_Schrenk | VAM_tie_cost | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | VAM_tie_allocation | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | VAM_penalty_sqrtA | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | VAM_penalty_A | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | TDSM_theta1_5 | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | LCM_top2_product | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0001 | unavailable |
| E19_Schrenk | LCM_top2_LB | 59 | 60 | ok | True | 1 | 1.6949 | 98.3333 | False | 0.0003 | unavailable |
| E19_Schrenk | VAM_top2_LB | 59 | 61 | ok | True | 2 | 3.3898 | 96.7213 | False | 0.0006 | unavailable |
| E19_Schrenk | THP_top2_LB | 59 | 60 | ok | True | 1 | 1.6949 | 98.3333 | False | 0.0004 | unavailable |
| E19_Schrenk | LCM_top2_rollout | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0006 | unavailable |
| E19_Schrenk | LCM_top3_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Schrenk | VAM_top2_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| E19_Schrenk | VAM_top3_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0014 | unavailable |
| E19_Schrenk | THP_top2_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0012 | unavailable |
| E19_Schrenk | THP_top3_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0011 | unavailable |
| E19_Schrenk | THP_top2_LCMcompletion | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Schrenk | VAM_top2_first_only | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Schrenk | THP_top2_first_only | 59 | 60 | ok | True | 1 | 1.6949 | 98.3333 | False | 0.0003 | unavailable |
| E19_Schrenk | VAM_tieA_top2_rollout | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0008 | unavailable |
| E19_Schrenk | MRM_orientation_ensemble | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Schrenk | LCM_score_alpha025 | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | LCM_score_alpha050 | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | LCM_score_alpha075 | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | JHM_single | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Schrenk | JHM_cap_receiver | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0001 | unavailable |
| E19_Schrenk | JHM_net_tie | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0006 | unavailable |
| E19_Schrenk | JHM_cap_net_tie | 59 | 69 | ok | True | 10 | 16.9492 | 85.5072 | False | 0.0002 | unavailable |
| E19_Schrenk | JHM_top2_completion | 59 | 59 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Samuel | NWCM | 28 | 42 | ok | True | 14 | 50 | 66.6667 | False | 0.0001 | unavailable |
| E19_Samuel | LCM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | VAM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | LDVAM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | RAM | 28 | 34 | ok | True | 6 | 21.4286 | 82.3529 | False | 0.0002 | unavailable |
| E19_Samuel | TDM1 | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | TDM2 | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | TDSM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Samuel | THP | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | SSM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | CSM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | RBSM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | BCE | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | MRM | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | LCM_tie_allocation | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | VAM_tie_cost | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Samuel | VAM_tie_allocation | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | VAM_penalty_sqrtA | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | VAM_penalty_A | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | TDSM_theta1_5 | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | LCM_top2_product | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | LCM_top2_LB | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Samuel | VAM_top2_LB | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | THP_top2_LB | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | LCM_top2_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | LCM_top3_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0008 | unavailable |
| E19_Samuel | VAM_top2_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0007 | unavailable |
| E19_Samuel | VAM_top3_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0009 | unavailable |
| E19_Samuel | THP_top2_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0008 | unavailable |
| E19_Samuel | THP_top3_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| E19_Samuel | THP_top2_LCMcompletion | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Samuel | VAM_top2_first_only | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | THP_top2_first_only | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Samuel | VAM_tieA_top2_rollout | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| E19_Samuel | MRM_orientation_ensemble | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Samuel | LCM_score_alpha025 | 28 | 36 | ok | True | 8 | 28.5714 | 77.7778 | False | 0.0002 | unavailable |
| E19_Samuel | LCM_score_alpha050 | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | LCM_score_alpha075 | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0002 | unavailable |
| E19_Samuel | JHM_single | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | JHM_cap_receiver | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | JHM_net_tie | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | JHM_cap_net_tie | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Samuel | JHM_top2_completion | 28 | 28 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | NWCM | 435 | 520 | ok | True | 85 | 19.5402 | 83.6538 | False | 0.0001 | unavailable |
| E19_Imam | LCM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0001 | unavailable |
| E19_Imam | VAM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0003 | unavailable |
| E19_Imam | LDVAM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0003 | unavailable |
| E19_Imam | RAM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | TDM1 | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | TDM2 | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | TDSM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0001 | unavailable |
| E19_Imam | THP | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | SSM | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0001 | unavailable |
| E19_Imam | CSM | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | RBSM | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | BCE | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | MRM | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0001 | unavailable |
| E19_Imam | LCM_tie_allocation | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0001 | unavailable |
| E19_Imam | VAM_tie_cost | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | VAM_tie_allocation | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | VAM_penalty_sqrtA | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | VAM_penalty_A | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | TDSM_theta1_5 | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0001 | unavailable |
| E19_Imam | LCM_top2_product | 435 | 520 | ok | True | 85 | 19.5402 | 83.6538 | False | 0.0001 | unavailable |
| E19_Imam | LCM_top2_LB | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | VAM_top2_LB | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0004 | unavailable |
| E19_Imam | THP_top2_LB | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0004 | unavailable |
| E19_Imam | LCM_top2_rollout | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0008 | unavailable |
| E19_Imam | LCM_top3_rollout | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0005 | unavailable |
| E19_Imam | VAM_top2_rollout | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0014 | unavailable |
| E19_Imam | VAM_top3_rollout | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0011 | unavailable |
| E19_Imam | THP_top2_rollout | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0006 | unavailable |
| E19_Imam | THP_top3_rollout | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0006 | unavailable |
| E19_Imam | THP_top2_LCMcompletion | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0004 | unavailable |
| E19_Imam | VAM_top2_first_only | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0005 | unavailable |
| E19_Imam | THP_top2_first_only | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0003 | unavailable |
| E19_Imam | VAM_tieA_top2_rollout | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0008 | unavailable |
| E19_Imam | MRM_orientation_ensemble | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0003 | unavailable |
| E19_Imam | LCM_score_alpha025 | 435 | 505 | ok | True | 70 | 16.092 | 86.1386 | False | 0.0002 | unavailable |
| E19_Imam | LCM_score_alpha050 | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | LCM_score_alpha075 | 435 | 475 | ok | True | 40 | 9.1954 | 91.5789 | False | 0.0002 | unavailable |
| E19_Imam | JHM_single | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0001 | unavailable |
| E19_Imam | JHM_cap_receiver | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | JHM_net_tie | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0001 | unavailable |
| E19_Imam | JHM_cap_net_tie | 435 | 435 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Imam | JHM_top2_completion | 435 | 460 | ok | True | 25 | 5.7471 | 94.5652 | False | 0.0003 | unavailable |
| E19_Adlakha | NWCM | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0001 | unavailable |
| E19_Adlakha | LCM | 390 | 490 | ok | True | 100 | 25.641 | 79.5918 | False | 0.0002 | unavailable |
| E19_Adlakha | VAM | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Adlakha | LDVAM | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Adlakha | RAM | 390 | 400 | ok | True | 10 | 2.5641 | 97.5 | False | 0.0002 | unavailable |
| E19_Adlakha | TDM1 | 390 | 400 | ok | True | 10 | 2.5641 | 97.5 | False | 0.0002 | unavailable |
| E19_Adlakha | TDM2 | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Adlakha | TDSM | 390 | 400 | ok | True | 10 | 2.5641 | 97.5 | False | 0.0002 | unavailable |
| E19_Adlakha | THP | 390 | 470 | ok | True | 80 | 20.5128 | 82.9787 | False | 0.0003 | unavailable |
| E19_Adlakha | SSM | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0001 | unavailable |
| E19_Adlakha | CSM | 390 | 480 | ok | True | 90 | 23.0769 | 81.25 | False | 0.0001 | unavailable |
| E19_Adlakha | RBSM | 390 | 480 | ok | True | 90 | 23.0769 | 81.25 | False | 0.0001 | unavailable |
| E19_Adlakha | BCE | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0001 | unavailable |
| E19_Adlakha | MRM | 390 | 400 | ok | True | 10 | 2.5641 | 97.5 | False | 0.0001 | unavailable |
| E19_Adlakha | LCM_tie_allocation | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0001 | unavailable |
| E19_Adlakha | VAM_tie_cost | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Adlakha | VAM_tie_allocation | 390 | 410 | ok | True | 20 | 5.1282 | 95.122 | False | 0.0003 | unavailable |
| E19_Adlakha | VAM_penalty_sqrtA | 390 | 410 | ok | True | 20 | 5.1282 | 95.122 | False | 0.0003 | unavailable |
| E19_Adlakha | VAM_penalty_A | 390 | 410 | ok | True | 20 | 5.1282 | 95.122 | False | 0.0003 | unavailable |
| E19_Adlakha | TDSM_theta1_5 | 390 | 400 | ok | True | 10 | 2.5641 | 97.5 | False | 0.0004 | unavailable |
| E19_Adlakha | LCM_top2_product | 390 | 520 | ok | True | 130 | 33.3333 | 75 | False | 0.0003 | unavailable |
| E19_Adlakha | LCM_top2_LB | 390 | 480 | ok | True | 90 | 23.0769 | 81.25 | False | 0.0004 | unavailable |
| E19_Adlakha | VAM_top2_LB | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0005 | unavailable |
| E19_Adlakha | THP_top2_LB | 390 | 410 | ok | True | 20 | 5.1282 | 95.122 | False | 0.0006 | unavailable |
| E19_Adlakha | LCM_top2_rollout | 390 | 480 | ok | True | 90 | 23.0769 | 81.25 | False | 0.0009 | unavailable |
| E19_Adlakha | LCM_top3_rollout | 390 | 480 | ok | True | 90 | 23.0769 | 81.25 | False | 0.001 | unavailable |
| E19_Adlakha | VAM_top2_rollout | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0025 | unavailable |
| E19_Adlakha | VAM_top3_rollout | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0022 | unavailable |
| E19_Adlakha | THP_top2_rollout | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0025 | unavailable |
| E19_Adlakha | THP_top3_rollout | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0022 | unavailable |
| E19_Adlakha | THP_top2_LCMcompletion | 390 | 410 | ok | True | 20 | 5.1282 | 95.122 | False | 0.001 | unavailable |
| E19_Adlakha | VAM_top2_first_only | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0007 | unavailable |
| E19_Adlakha | THP_top2_first_only | 390 | 430 | ok | True | 40 | 10.2564 | 90.6977 | False | 0.0009 | unavailable |
| E19_Adlakha | VAM_tieA_top2_rollout | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0017 | unavailable |
| E19_Adlakha | MRM_orientation_ensemble | 390 | 390 | ok | True | 0 | 0 | 100 | True | 0.0003 | unavailable |
| E19_Adlakha | LCM_score_alpha025 | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0003 | unavailable |
| E19_Adlakha | LCM_score_alpha050 | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0003 | unavailable |
| E19_Adlakha | LCM_score_alpha075 | 390 | 500 | ok | True | 110 | 28.2051 | 78 | False | 0.0003 | unavailable |
| E19_Adlakha | JHM_single | 390 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Adlakha | JHM_cap_receiver | 390 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Adlakha | JHM_net_tie | 390 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Adlakha | JHM_cap_net_tie | 390 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| E19_Adlakha | JHM_top2_completion | 390 | unavailable | unverified | unavailable | unavailable | unavailable | unavailable | unavailable | 0 | Multiple excess rows after initialization: original dependency branch not verified |
| L01_Real2x94 | NWCM | 12175097 | 12309686 | ok | True | 134589 | 1.1054 | 98.9066 | False | 0.0014 | unavailable |
| L01_Real2x94 | LCM | 12175097 | 12219653 | ok | True | 44556 | 0.366 | 99.6354 | False | 0.0028 | unavailable |
| L01_Real2x94 | VAM | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.014 | unavailable |
| L01_Real2x94 | LDVAM | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0123 | unavailable |
| L01_Real2x94 | RAM | 12175097 | 12181508 | ok | True | 6411 | 0.0527 | 99.9474 | False | 0.0078 | unavailable |
| L01_Real2x94 | TDM1 | 12175097 | 12208071 | ok | True | 32974 | 0.2708 | 99.7299 | False | 0.0033 | unavailable |
| L01_Real2x94 | TDM2 | 12175097 | 12208071 | ok | True | 32974 | 0.2708 | 99.7299 | False | 0.0152 | unavailable |
| L01_Real2x94 | TDSM | 12175097 | 12179696 | ok | True | 4599 | 0.0378 | 99.9622 | False | 0.004 | unavailable |
| L01_Real2x94 | THP | 12175097 | 12714389 | ok | True | 539292 | 4.4295 | 95.7584 | False | 0.0124 | unavailable |
| L01_Real2x94 | SSM | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.001 | unavailable |
| L01_Real2x94 | CSM | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0014 | unavailable |
| L01_Real2x94 | RBSM | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.002 | unavailable |
| L01_Real2x94 | BCE | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0015 | unavailable |
| L01_Real2x94 | MRM | 12175097 | 12264685 | ok | True | 89588 | 0.7358 | 99.2695 | False | 0.0026 | unavailable |
| L01_Real2x94 | LCM_tie_allocation | 12175097 | 12219653 | ok | True | 44556 | 0.366 | 99.6354 | False | 0.0032 | unavailable |
| L01_Real2x94 | VAM_tie_cost | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0114 | unavailable |
| L01_Real2x94 | VAM_tie_allocation | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0129 | unavailable |
| L01_Real2x94 | VAM_penalty_sqrtA | 12175097 | 12181456 | ok | True | 6359 | 0.0522 | 99.9478 | False | 0.0139 | unavailable |
| L01_Real2x94 | VAM_penalty_A | 12175097 | 12194454 | ok | True | 19357 | 0.159 | 99.8413 | False | 0.0122 | unavailable |
| L01_Real2x94 | TDSM_theta1_5 | 12175097 | 12185584 | ok | True | 10487 | 0.0861 | 99.9139 | False | 0.0043 | unavailable |
| L01_Real2x94 | LCM_top2_product | 12175097 | 12271494 | ok | True | 96397 | 0.7918 | 99.2145 | False | 0.0035 | unavailable |
| L01_Real2x94 | LCM_top2_LB | 12175097 | 12274409 | ok | True | 99312 | 0.8157 | 99.1909 | False | 0.0053 | unavailable |
| L01_Real2x94 | VAM_top2_LB | 12175097 | 12177956 | ok | True | 2859 | 0.0235 | 99.9765 | False | 0.015 | unavailable |
| L01_Real2x94 | THP_top2_LB | 12175097 | 12242354 | ok | True | 67257 | 0.5524 | 99.4506 | False | 0.0152 | unavailable |
| L01_Real2x94 | LCM_top2_rollout | 12175097 | 12217803 | ok | True | 42706 | 0.3508 | 99.6505 | False | 0.1344 | unavailable |
| L01_Real2x94 | LCM_top3_rollout | 12175097 | 12204705 | ok | True | 29608 | 0.2432 | 99.7574 | False | 0.1977 | unavailable |
| L01_Real2x94 | VAM_top2_rollout | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.6379 | unavailable |
| L01_Real2x94 | VAM_top3_rollout | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.8868 | unavailable |
| L01_Real2x94 | THP_top2_rollout | 12175097 | 12282430 | ok | True | 107333 | 0.8816 | 99.1261 | False | 0.6206 | unavailable |
| L01_Real2x94 | THP_top3_rollout | 12175097 | 12187811 | ok | True | 12714 | 0.1044 | 99.8957 | False | 0.8342 | unavailable |
| L01_Real2x94 | THP_top2_LCMcompletion | 12175097 | 12206729 | ok | True | 31632 | 0.2598 | 99.7409 | False | 0.1449 | unavailable |
| L01_Real2x94 | VAM_top2_first_only | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0224 | unavailable |
| L01_Real2x94 | THP_top2_first_only | 12175097 | 12714389 | ok | True | 539292 | 4.4295 | 95.7584 | False | 0.0244 | unavailable |
| L01_Real2x94 | VAM_tieA_top2_rollout | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.6175 | unavailable |
| L01_Real2x94 | MRM_orientation_ensemble | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0084 | unavailable |
| L01_Real2x94 | LCM_score_alpha025 | 12175097 | 12219155 | ok | True | 44058 | 0.3619 | 99.6394 | False | 0.0042 | unavailable |
| L01_Real2x94 | LCM_score_alpha050 | 12175097 | 12219181 | ok | True | 44084 | 0.3621 | 99.6392 | False | 0.0049 | unavailable |
| L01_Real2x94 | LCM_score_alpha075 | 12175097 | 12219653 | ok | True | 44556 | 0.366 | 99.6354 | False | 0.005 | unavailable |
| L01_Real2x94 | JHM_single | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0025 | unavailable |
| L01_Real2x94 | JHM_cap_receiver | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0013 | unavailable |
| L01_Real2x94 | JHM_net_tie | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0016 | unavailable |
| L01_Real2x94 | JHM_cap_net_tie | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.0014 | unavailable |
| L01_Real2x94 | JHM_top2_completion | 12175097 | 12175097 | ok | True | 0 | 0 | 100 | True | 0.01 | unavailable |
