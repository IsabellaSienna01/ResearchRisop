# Published numerical benchmarks

All transcribed source occurrences and raw numbers are in `datasets/published/occurrences.json`. This appendix lists the 86 distinct raw problems, including provenance aliases. Repeated balanced forms count once in aggregate experiments. Published values are claims, not ground truth.

## L01_Table2

Source L01, Table 2; Table 7 P09. Shape 3 x 4; balanced: True; kind: literature.

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

LP optimum: **435**; dual gap 0. Occurrences: L01_Table2, EDM_C21.



| occurrence | method | published |
| --- | --- | --- |
| L01_Table2 | VAM | 475 |
| L01_Table2 | TDM1 | 475 |
| L01_Table2 | TOCM_MT | 435 |
| L01_Table2 | JHM | 460 |
| L01_Table2 | BCE | 435 |
| L01_Table2 | optimal | 435 |
| EDM_C21 | optimal | 435 |

## L02_Table3

Source L02, Tables 3-6; N09. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      6,
      5,
      2
    ],
    [
      6,
      4,
      1,
      4
    ],
    [
      5,
      2,
      3,
      1
    ],
    [
      4,
      6,
      7,
      8
    ]
  ],
  "supply": [
    6,
    10,
    12,
    14
  ],
  "demand": [
    9,
    16,
    10,
    7
  ]
}
```

LP optimum: **111**; dual gap 0. Occurrences: L02_Table3, RBSM_N09, CSM_N09.



| occurrence | method | published |
| --- | --- | --- |
| L02_Table3 | RBSM | 111 |
| L02_Table3 | optimal | 111 |
| CSM_N09 | optimal | 111 |

## L02_Table7

Source L02, Table 7; N06. Shape 3 x 4; balanced: False; kind: literature.

```json
{
  "costs": [
    [
      10,
      8,
      4,
      3
    ],
    [
      12,
      14,
      20,
      2
    ],
    [
      6,
      9,
      23,
      25
    ]
  ],
  "supply": [
    500,
    400,
    300
  ],
  "demand": [
    250,
    350,
    600,
    150
  ]
}
```

LP optimum: **7750**; dual gap 0. Occurrences: L02_Table7, MRM_UTP1.

Zero-cost dummy source of 150 required.

| occurrence | method | published |
| --- | --- | --- |
| L02_Table7 | RBSM | 7750 |
| L02_Table7 | BCE | 8350 |
| L02_Table7 | optimal | 7750 |
| MRM_UTP1 | NWCM | 18800 |
| MRM_UTP1 | LCM | 8800 |
| MRM_UTP1 | VAM | 8350 |
| MRM_UTP1 | MRM | 7750 |
| MRM_UTP1 | optimal | 7750 |

## L03_Table2

Source L03, Tables 2-5; Table 7 P26. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      13,
      21,
      14
    ],
    [
      8,
      12,
      21
    ],
    [
      15,
      17,
      19
    ]
  ],
  "supply": [
    13,
    20,
    5
  ],
  "demand": [
    12,
    15,
    11
  ]
}
```

LP optimum: **465**; dual gap 0. Occurrences: L03_Table2, RBSM_N30, CSM_N30, EDM_C15.



| occurrence | method | published |
| --- | --- | --- |
| L03_Table2 | SSM | 465 |
| L03_Table2 | LCM | 473 |
| L03_Table2 | VAM | 473 |
| L03_Table2 | JHM | 475 |
| L03_Table2 | TOCM_MT | 475 |
| L03_Table2 | BCE | 475 |
| L03_Table2 | optimal | 465 |
| CSM_N30 | optimal | 465 |
| EDM_C15 | optimal | 465 |

## L04_Example1

Source L04, Example 1; Table 9. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      1,
      3,
      2
    ],
    [
      3,
      2,
      6
    ],
    [
      3,
      5,
      4
    ]
  ],
  "supply": [
    5,
    8,
    7
  ],
  "demand": [
    5,
    5,
    10
  ]
}
```

LP optimum: **55**; dual gap 0. Occurrences: L04_Example1.

Published worked feasible cost 55 contradicts Table 9 optimal 61; reduced table has errors.

| occurrence | method | published |
| --- | --- | --- |
| L04_Example1 | NWCM | 57 |
| L04_Example1 | LCM | 55 |
| L04_Example1 | VAM | 61 |
| L04_Example1 | AIP_MT | 61 |
| L04_Example1 | optimal | 61 |
| L04_Example1 | AIP_worked | 55 |

## L04_Example2

Source L04, Example 2; Table 9. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      2,
      3,
      7,
      11
    ],
    [
      0,
      12,
      5,
      6
    ],
    [
      14,
      1,
      3,
      9
    ],
    [
      10,
      2,
      5,
      8
    ]
  ],
  "supply": [
    150,
    125,
    75,
    50
  ],
  "demand": [
    100,
    20,
    80,
    200
  ]
}
```

LP optimum: **1945**; dual gap 0. Occurrences: L04_Example2.

Worked proposed cost 1995 differs from summary proposed cost 2360; reduced table has errors.

| occurrence | method | published |
| --- | --- | --- |
| L04_Example2 | NWCM | 2215 |
| L04_Example2 | LCM | 1995 |
| L04_Example2 | VAM | 2245 |
| L04_Example2 | AIP_MT | 2360 |
| L04_Example2 | optimal | 1945 |
| L04_Example2 | AIP_worked | 1995 |

## L05_Example1

Source L05, Example 1. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      3,
      1,
      4
    ],
    [
      7,
      6,
      2,
      1
    ],
    [
      10,
      4,
      5,
      9
    ],
    [
      7,
      7,
      7,
      3
    ]
  ],
  "supply": [
    50,
    55,
    75,
    60
  ],
  "demand": [
    90,
    65,
    30,
    55
  ]
}
```

LP optimum: **985**; dual gap 0. Occurrences: L05_Example1.



| occurrence | method | published |
| --- | --- | --- |
| L05_Example1 | VAM | 1095 |
| L05_Example1 | LDVAM | 1095 |
| L05_Example1 | THP | 1045 |
| L05_Example1 | optimal | 985 |

## L05_Example2

Source L05, Example 2. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      8,
      10
    ],
    [
      7,
      11,
      11
    ],
    [
      4,
      5,
      12
    ]
  ],
  "supply": [
    150,
    175,
    275
  ],
  "demand": [
    200,
    100,
    300
  ]
}
```

LP optimum: **4525**; dual gap 0. Occurrences: L05_Example2, RBSM_N13, CSM_N13, EDM_C10.



| occurrence | method | published |
| --- | --- | --- |
| L05_Example2 | VAM | 5125 |
| L05_Example2 | LDVAM | 5125 |
| L05_Example2 | THP | 4525 |
| L05_Example2 | optimal | 4525 |
| CSM_N13 | optimal | 4525 |
| EDM_C10 | optimal | 4525 |

## L05_Example3

Source L05, Example 3. Shape 5 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      70,
      37,
      6,
      76,
      17
    ],
    [
      59,
      90,
      93,
      5,
      10
    ],
    [
      93,
      62,
      77,
      47,
      62
    ],
    [
      54,
      55,
      26,
      9,
      84
    ],
    [
      53,
      20,
      84,
      15,
      9
    ]
  ],
  "supply": [
    18,
    17,
    19,
    13,
    15
  ],
  "demand": [
    16,
    18,
    20,
    14,
    14
  ]
}
```

LP optimum: **2366**; dual gap 0. Occurrences: L05_Example3.



| occurrence | method | published |
| --- | --- | --- |
| L05_Example3 | VAM | 2388 |
| L05_Example3 | LDVAM | 2388 |
| L05_Example3 | THP | 2366 |
| L05_Example3 | optimal | 2366 |

## E01_Example1

Source E01, Example 1; Tables 3 or 7. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      20,
      22,
      17,
      4
    ],
    [
      24,
      37,
      9,
      7
    ],
    [
      32,
      37,
      20,
      15
    ]
  ],
  "supply": [
    120,
    70,
    50
  ],
  "demand": [
    60,
    40,
    30,
    110
  ]
}
```

LP optimum: **3460**; dual gap 0. Occurrences: E01_Example1, RBSM_N24, CSM_N24, EDM_C06.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example1 | NWCM | 3680 |
| E01_Example1 | LCM | 3670 |
| E01_Example1 | VAM | 3520 |
| E01_Example1 | TDM1 | 3570 |
| E01_Example1 | TDSM | 3710 |
| CSM_N24 | optimal | 3460 |
| EDM_C06 | optimal | 3460 |

## E01_Example2

Source E01, Example 2; Tables 3 or 7. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      3,
      5,
      7,
      6
    ],
    [
      2,
      5,
      8,
      2
    ],
    [
      3,
      6,
      9,
      2
    ]
  ],
  "supply": [
    50,
    75,
    25
  ],
  "demand": [
    20,
    20,
    50,
    60
  ]
}
```

LP optimum: **610**; dual gap 0. Occurrences: E01_Example2.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example2 | NWCM | 670 |
| E01_Example2 | LCM | 650 |
| E01_Example2 | VAM | 650 |
| E01_Example2 | TDM1 | 630 |
| E01_Example2 | TDSM | 610 |

## E01_Example3

Source E01, Example 3; Tables 3 or 7. Shape 3 x 4; balanced: True; kind: literature.

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
    5,
    8,
    7,
    14
  ]
}
```

LP optimum: **743**; dual gap 0. Occurrences: E01_Example3, RBSM_N17, CSM_N17.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example3 | NWCM | 1015 |
| E01_Example3 | LCM | 814 |
| E01_Example3 | VAM | 779 |
| E01_Example3 | TDM1 | 779 |
| E01_Example3 | TDSM | 781 |
| CSM_N17 | optimal | 743 |

## E01_Example4

Source E01, Example 4; Tables 3 or 7. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      41,
      46,
      14,
      49
    ],
    [
      46,
      32,
      28,
      8
    ],
    [
      7,
      5,
      48,
      49
    ]
  ],
  "supply": [
    7,
    9,
    18
  ],
  "demand": [
    5,
    8,
    7,
    14
  ]
}
```

LP optimum: **490**; dual gap 0. Occurrences: E01_Example4.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example4 | NWCM | 1451 |
| E01_Example4 | VAM | 490 |
| E01_Example4 | TDM1 | 490 |
| E01_Example4 | TDSM | 490 |

## E01_Example5

Source E01, Example 5; Tables 3 or 7. Shape 5 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      82,
      10,
      16,
      15,
      66
    ],
    [
      91,
      28,
      98,
      43,
      4
    ],
    [
      13,
      55,
      96,
      92,
      85
    ],
    [
      92,
      96,
      49,
      80,
      94
    ],
    [
      64,
      97,
      81,
      96,
      68
    ]
  ],
  "supply": [
    2,
    3,
    5,
    7,
    9
  ],
  "demand": [
    1,
    4,
    6,
    8,
    7
  ]
}
```

LP optimum: **1401**; dual gap 0. Occurrences: E01_Example5.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example5 | NWCM | 1853 |
| E01_Example5 | VAM | 1401 |
| E01_Example5 | TDM1 | 1401 |
| E01_Example5 | TDSM | 1661 |

## E01_Example6

Source E01, Example 6; Tables 3 or 7. Shape 10 x 7; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      17,
      4,
      14,
      15,
      9,
      6,
      16
    ],
    [
      19,
      20,
      1,
      1,
      8,
      14,
      6
    ],
    [
      3,
      20,
      17,
      6,
      16,
      14,
      11
    ],
    [
      19,
      10,
      19,
      1,
      16,
      4,
      14
    ],
    [
      13,
      17,
      14,
      2,
      4,
      3,
      18
    ],
    [
      2,
      3,
      16,
      17,
      10,
      10,
      20
    ],
    [
      6,
      9,
      15,
      14,
      9,
      20,
      11
    ],
    [
      11,
      19,
      8,
      7,
      13,
      7,
      3
    ],
    [
      20,
      16,
      14,
      20,
      15,
      12,
      3
    ],
    [
      20,
      20,
      4,
      1,
      16,
      5,
      6
    ]
  ],
  "supply": [
    6,
    8,
    11,
    13,
    23,
    5,
    20,
    13,
    14,
    16
  ],
  "demand": [
    14,
    24,
    28,
    33,
    4,
    12,
    14
  ]
}
```

LP optimum: **505**; dual gap 0. Occurrences: E01_Example6.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example6 | NWCM | 1651 |
| E01_Example6 | VAM | 740 |
| E01_Example6 | TDM1 | 712 |
| E01_Example6 | TDSM | 712 |

## E01_Example7

Source E01, Example 7; Tables 3 or 7. Shape 8 x 9; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      25,
      29,
      13,
      21,
      9,
      14,
      22,
      29,
      27
    ],
    [
      28,
      29,
      28,
      23,
      2,
      12,
      23,
      11,
      29
    ],
    [
      4,
      5,
      24,
      23,
      3,
      23,
      9,
      18,
      17
    ],
    [
      28,
      30,
      29,
      12,
      25,
      24,
      21,
      7,
      5
    ],
    [
      19,
      29,
      20,
      20,
      21,
      6,
      20,
      23,
      5
    ],
    [
      3,
      15,
      2,
      6,
      10,
      15,
      5,
      8,
      8
    ],
    [
      9,
      25,
      26,
      22,
      29,
      14,
      4,
      16,
      26
    ],
    [
      17,
      5,
      29,
      1,
      2,
      20,
      15,
      21,
      8
    ]
  ],
  "supply": [
    16,
    18,
    10,
    13,
    11,
    15,
    22,
    23
  ],
  "demand": [
    13,
    21,
    15,
    8,
    10,
    12,
    20,
    13,
    16
  ]
}
```

LP optimum: **722**; dual gap 0. Occurrences: E01_Example7.

TDSM exponent theta=2 is the tested square specialization; paper also allows 1<theta<=2.

| occurrence | method | published |
| --- | --- | --- |
| E01_Example7 | NWCM | 2251 |
| E01_Example7 | VAM | 844 |
| E01_Example7 | TDM1 | 935 |
| E01_Example7 | TDSM | 979 |

## RBSM_N01

Source E02, rbsm_n01.txt. Shape 3 x 3; balanced: True; kind: literature.

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

LP optimum: **5600**; dual gap 0. Occurrences: RBSM_N01, CSM_N01, EDM_C03.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N01 | optimal | 5600 |
| EDM_C03 | optimal | 5600 |

## RBSM_N02

Source E02, rbsm_n02.txt. Shape 3 x 4; balanced: True; kind: literature.

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

LP optimum: **28**; dual gap 0. Occurrences: RBSM_N02, CSM_N02, EDM_C05.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N02 | optimal | 28 |
| EDM_C05 | optimal | 28 |

## RBSM_N03

Source E02, rbsm_n03.txt. Shape 5 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      73,
      40,
      9,
      79,
      20
    ],
    [
      62,
      93,
      96,
      8,
      13
    ],
    [
      96,
      65,
      80,
      50,
      65
    ],
    [
      57,
      58,
      29,
      12,
      87
    ],
    [
      56,
      23,
      87,
      18,
      12
    ]
  ],
  "supply": [
    8,
    7,
    9,
    3,
    5
  ],
  "demand": [
    6,
    8,
    10,
    4,
    4
  ]
}
```

LP optimum: **1102**; dual gap 0. Occurrences: RBSM_N03.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N04

Source E02, rbsm_n04.txt. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      4,
      1
    ],
    [
      3,
      8,
      7
    ],
    [
      4,
      4,
      2
    ]
  ],
  "supply": [
    50,
    40,
    60
  ],
  "demand": [
    20,
    95,
    35
  ]
}
```

LP optimum: **555**; dual gap 0. Occurrences: RBSM_N04, MRM_BTP2.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP2 | NWCM | 730 |
| MRM_BTP2 | LCM | 555 |
| MRM_BTP2 | VAM | 555 |
| MRM_BTP2 | MRM | 555 |
| MRM_BTP2 | optimal | 555 |

## RBSM_N05

Source E02, rbsm_n05.txt. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      5,
      9,
      11
    ],
    [
      4,
      3,
      8,
      6
    ],
    [
      3,
      8,
      10,
      5
    ],
    [
      2,
      6,
      7,
      3
    ]
  ],
  "supply": [
    30,
    25,
    20,
    15
  ],
  "demand": [
    30,
    30,
    20,
    10
  ]
}
```

LP optimum: **410**; dual gap 0. Occurrences: RBSM_N05, CSM_N05, MRM_BTP5.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N05 | optimal | 410 |
| MRM_BTP5 | NWCM | 540 |
| MRM_BTP5 | LCM | 435 |
| MRM_BTP5 | VAM | 470 |
| MRM_BTP5 | MRM | 415 |
| MRM_BTP5 | optimal | 410 |

## RBSM_N06

Source E02, rbsm_n06.txt. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      10,
      8,
      4,
      3
    ],
    [
      12,
      14,
      20,
      2
    ],
    [
      6,
      9,
      23,
      25
    ],
    [
      0,
      0,
      0,
      0
    ]
  ],
  "supply": [
    500,
    400,
    300,
    150
  ],
  "demand": [
    250,
    350,
    600,
    150
  ]
}
```

LP optimum: **7750**; dual gap 0. Occurrences: RBSM_N06.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N07

Source E02, rbsm_n07.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      1,
      9,
      3
    ],
    [
      11,
      5,
      2,
      8
    ],
    [
      10,
      12,
      4,
      7
    ]
  ],
  "supply": [
    70,
    55,
    90
  ],
  "demand": [
    85,
    35,
    50,
    45
  ]
}
```

LP optimum: **1160**; dual gap 0. Occurrences: RBSM_N07, CSM_N07, EDM_C17.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N07 | optimal | 1160 |
| EDM_C17 | optimal | 1160 |

## RBSM_N08

Source E02, rbsm_n08.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      5,
      7,
      9,
      6
    ],
    [
      6,
      7,
      10,
      5
    ],
    [
      7,
      6,
      8,
      1
    ]
  ],
  "supply": [
    12,
    14,
    10
  ],
  "demand": [
    10,
    6,
    8,
    12
  ]
}
```

LP optimum: **190**; dual gap 0. Occurrences: RBSM_N08.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N10

Source E02, rbsm_n10.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      20,
      2,
      20,
      11
    ],
    [
      24,
      7,
      9,
      20
    ],
    [
      8,
      14,
      16,
      18
    ]
  ],
  "supply": [
    30,
    50,
    20
  ],
  "demand": [
    10,
    30,
    30,
    30
  ]
}
```

LP optimum: **910**; dual gap 0. Occurrences: RBSM_N10, CSM_N10.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N10 | optimal | 910 |

## RBSM_N11

Source E02, rbsm_n11.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      10,
      2,
      20,
      22
    ],
    [
      12,
      7,
      9,
      40
    ],
    [
      4,
      14,
      16,
      32
    ]
  ],
  "supply": [
    60,
    100,
    40
  ],
  "demand": [
    20,
    60,
    60,
    60
  ]
}
```

LP optimum: **2460**; dual gap 0. Occurrences: RBSM_N11, CSM_N11.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N11 | optimal | 2460 |

## RBSM_N12

Source E02, rbsm_n12.txt. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      15,
      7,
      25
    ],
    [
      8,
      12,
      14
    ],
    [
      17,
      19,
      21
    ]
  ],
  "supply": [
    12,
    17,
    7
  ],
  "demand": [
    12,
    10,
    14
  ]
}
```

LP optimum: **425**; dual gap 0. Occurrences: RBSM_N12, CSM_N12, EDM_C14.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N12 | optimal | 425 |
| EDM_C14 | optimal | 425 |

## RBSM_N14

Source E02, rbsm_n14.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      6,
      8,
      8
    ],
    [
      6,
      8,
      6,
      7
    ],
    [
      5,
      7,
      6,
      8
    ]
  ],
  "supply": [
    40,
    60,
    50
  ],
  "demand": [
    20,
    30,
    50,
    50
  ]
}
```

LP optimum: **920**; dual gap 0. Occurrences: RBSM_N14, CSM_N14.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N14 | optimal | 920 |

## RBSM_N15

Source E02, rbsm_n15.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      6,
      9,
      5
    ],
    [
      2,
      6,
      4,
      1
    ],
    [
      5,
      7,
      2,
      9
    ]
  ],
  "supply": [
    16,
    12,
    15
  ],
  "demand": [
    12,
    14,
    9,
    8
  ]
}
```

LP optimum: **156**; dual gap 0. Occurrences: RBSM_N15, CSM_N15.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N15 | optimal | 156 |

## RBSM_N16

Source E02, rbsm_n16.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      22,
      17,
      25,
      15
    ],
    [
      13,
      10,
      16,
      20
    ],
    [
      16,
      19,
      9,
      5
    ]
  ],
  "supply": [
    30,
    50,
    50
  ],
  "demand": [
    30,
    30,
    50,
    20
  ]
}
```

LP optimum: **1510**; dual gap 0. Occurrences: RBSM_N16, CSM_N16.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N16 | optimal | 1510 |

## RBSM_N18

Source E02, rbsm_n18.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      10,
      14,
      0
    ],
    [
      12,
      19,
      21,
      0
    ],
    [
      15,
      14,
      17,
      0
    ]
  ],
  "supply": [
    50,
    50,
    50
  ],
  "demand": [
    30,
    40,
    55,
    25
  ]
}
```

LP optimum: **1650**; dual gap 0. Occurrences: RBSM_N18.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N21

Source E02, rbsm_n21.txt. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      135,
      71,
      260
    ],
    [
      81,
      126,
      144
    ],
    [
      170,
      189,
      201
    ]
  ],
  "supply": [
    12,
    17,
    7
  ],
  "demand": [
    12,
    10,
    14
  ]
}
```

LP optimum: **4205**; dual gap 0. Occurrences: RBSM_N21, CSM_N21.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N21 | optimal | 4205 |

## RBSM_N22

Source E02, rbsm_n22.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      11,
      13,
      17,
      14
    ],
    [
      16,
      18,
      14,
      10
    ],
    [
      21,
      24,
      13,
      10
    ]
  ],
  "supply": [
    250,
    300,
    400
  ],
  "demand": [
    200,
    225,
    275,
    250
  ]
}
```

LP optimum: **12075**; dual gap 0. Occurrences: RBSM_N22, CSM_N22.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N22 | optimal | 12075 |

## RBSM_N23

Source E02, rbsm_n23.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      2,
      3,
      7
    ],
    [
      1,
      5,
      4,
      5
    ],
    [
      7,
      2,
      4,
      5
    ]
  ],
  "supply": [
    2,
    1,
    3
  ],
  "demand": [
    2,
    1,
    1,
    2
  ]
}
```

LP optimum: **23**; dual gap 0. Occurrences: RBSM_N23, CSM_N23.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N23 | optimal | 23 |

## RBSM_N25

Source E02, rbsm_n25.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      19,
      30,
      50,
      12
    ],
    [
      70,
      30,
      40,
      60
    ],
    [
      40,
      10,
      60,
      20
    ]
  ],
  "supply": [
    7,
    10,
    18
  ],
  "demand": [
    5,
    7,
    8,
    15
  ]
}
```

LP optimum: **809**; dual gap 0. Occurrences: RBSM_N25, CSM_N25.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N25 | optimal | 809 |

## RBSM_N26

Source E02, rbsm_n26.txt. Shape 4 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      20,
      4,
      6,
      8,
      9
    ],
    [
      4,
      10,
      8,
      18,
      8
    ],
    [
      9,
      11,
      20,
      40,
      6
    ],
    [
      7,
      6,
      9,
      14,
      16
    ]
  ],
  "supply": [
    20,
    30,
    15,
    13
  ],
  "demand": [
    40,
    6,
    8,
    18,
    6
  ]
}
```

LP optimum: **490**; dual gap 0. Occurrences: RBSM_N26, CSM_N26.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N26 | optimal | 490 |

## RBSM_N27

Source E02, rbsm_n27.txt. Shape 5 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      46,
      74,
      9,
      28,
      99
    ],
    [
      12,
      75,
      6,
      36,
      48
    ],
    [
      35,
      199,
      4,
      5,
      71
    ],
    [
      61,
      81,
      44,
      88,
      9
    ],
    [
      85,
      60,
      14,
      25,
      79
    ]
  ],
  "supply": [
    461,
    277,
    356,
    488,
    393
  ],
  "demand": [
    278,
    60,
    461,
    116,
    1060
  ]
}
```

LP optimum: **59356**; dual gap 0. Occurrences: RBSM_N27, CSM_N27.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N27 | optimal | 59356 |

## RBSM_N28

Source E02, rbsm_n28.txt. Shape 4 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      3,
      1,
      7,
      4
    ],
    [
      2,
      6,
      5,
      9
    ],
    [
      8,
      3,
      3,
      2
    ],
    [
      0,
      0,
      0,
      0
    ]
  ],
  "supply": [
    300,
    400,
    270,
    370
  ],
  "demand": [
    250,
    350,
    290,
    450
  ]
}
```

LP optimum: **2090**; dual gap 0. Occurrences: RBSM_N28.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N29

Source E02, rbsm_n29.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      15,
      1,
      42,
      33
    ],
    [
      80,
      42,
      26,
      81
    ],
    [
      90,
      40,
      66,
      60
    ]
  ],
  "supply": [
    23,
    44,
    33
  ],
  "demand": [
    23,
    31,
    16,
    30
  ]
}
```

LP optimum: **3857**; dual gap 0. Occurrences: RBSM_N29, CSM_N29.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N29 | optimal | 3857 |

## RBSM_N31

Source E02, rbsm_n31.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      15,
      27,
      13,
      19
    ],
    [
      18,
      21,
      24,
      14
    ],
    [
      21,
      15,
      16,
      17
    ]
  ],
  "supply": [
    40,
    40,
    20
  ],
  "demand": [
    30,
    20,
    30,
    20
  ]
}
```

LP optimum: **1480**; dual gap 0. Occurrences: RBSM_N31, CSM_N31.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N31 | optimal | 1480 |

## RBSM_N32

Source E02, rbsm_n32.txt. Shape 4 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      4,
      9,
      10,
      13
    ],
    [
      7,
      9,
      8,
      10,
      4
    ],
    [
      9,
      3,
      7,
      10,
      6
    ],
    [
      11,
      4,
      10,
      6,
      9
    ]
  ],
  "supply": [
    100,
    90,
    80,
    70
  ],
  "demand": [
    60,
    40,
    90,
    70,
    80
  ]
}
```

LP optimum: **1780**; dual gap 0. Occurrences: RBSM_N32, CSM_N32, E11_Table3.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N32 | optimal | 348 |
| E11_Table3 | CSM | 1780 |
| E11_Table3 | SSM | 1820 |
| E11_Table3 | optimal | 1780 |

## RBSM_N33

Source E02, rbsm_n33.txt. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      3,
      3,
      5
    ],
    [
      6,
      5,
      4
    ],
    [
      6,
      10,
      7
    ]
  ],
  "supply": [
    90,
    80,
    100
  ],
  "demand": [
    70,
    120,
    80
  ]
}
```

LP optimum: **1250**; dual gap 0. Occurrences: RBSM_N33.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_N34

Source E02, rbsm_n34.txt. Shape 4 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      6,
      4,
      5,
      9
    ],
    [
      8,
      5,
      6,
      7,
      8
    ],
    [
      6,
      8,
      9,
      6,
      5
    ],
    [
      5,
      7,
      7,
      8,
      6
    ]
  ],
  "supply": [
    40,
    30,
    20,
    10
  ],
  "demand": [
    30,
    30,
    15,
    20,
    5
  ]
}
```

LP optimum: **510**; dual gap 0. Occurrences: RBSM_N34, CSM_N34.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N34 | optimal | 510 |

## RBSM_N35

Source E02, rbsm_n35.txt. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      1,
      6,
      5,
      9
    ],
    [
      3,
      2,
      4,
      15
    ],
    [
      8,
      9,
      3,
      10
    ]
  ],
  "supply": [
    20,
    25,
    15
  ],
  "demand": [
    15,
    15,
    10,
    20
  ]
}
```

LP optimum: **280**; dual gap 0. Occurrences: RBSM_N35.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_S1

Source E02, rbsm_S1.txt. Shape 5 x 5; balanced: True; kind: author_synthetic.

```json
{
  "costs": [
    [
      27,
      27,
      9,
      33,
      9
    ],
    [
      36,
      15,
      33,
      30,
      15
    ],
    [
      18,
      21,
      27,
      36,
      33
    ],
    [
      33,
      36,
      21,
      24,
      9
    ],
    [
      27,
      9,
      9,
      21,
      15
    ]
  ],
  "supply": [
    150,
    240,
    135,
    300,
    285
  ],
  "demand": [
    270,
    195,
    210,
    270,
    165
  ]
}
```

LP optimum: **18855**; dual gap 0. Occurrences: RBSM_S1, CSM_S1.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_S1 | optimal | 18855 |

## RBSM_S2

Source E02, rbsm_S2.txt. Shape 5 x 5; balanced: True; kind: author_synthetic.

```json
{
  "costs": [
    [
      80,
      80,
      20,
      100,
      20
    ],
    [
      110,
      40,
      100,
      90,
      40
    ],
    [
      50,
      60,
      80,
      110,
      100
    ],
    [
      100,
      110,
      60,
      70,
      20
    ],
    [
      80,
      20,
      20,
      60,
      40
    ]
  ],
  "supply": [
    400,
    700,
    350,
    900,
    850
  ],
  "demand": [
    800,
    550,
    600,
    800,
    450
  ]
}
```

LP optimum: **153500**; dual gap 0. Occurrences: RBSM_S2, CSM_S2.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_S2 | optimal | 2790 |

## RBSM_S3

Source E02, rbsm_S3.txt. Shape 11 x 12; balanced: True; kind: author_synthetic.

```json
{
  "costs": [
    [
      3,
      156,
      159,
      162,
      165,
      168,
      171,
      174,
      177,
      180,
      183,
      36
    ],
    [
      189,
      42,
      195,
      198,
      201,
      204,
      207,
      210,
      213,
      216,
      219,
      222
    ],
    [
      225,
      228,
      81,
      234,
      237,
      240,
      243,
      246,
      249,
      252,
      255,
      258
    ],
    [
      261,
      264,
      267,
      120,
      273,
      276,
      279,
      282,
      285,
      288,
      291,
      294
    ],
    [
      297,
      300,
      303,
      306,
      159,
      312,
      315,
      318,
      321,
      324,
      327,
      330
    ],
    [
      333,
      336,
      339,
      342,
      345,
      198,
      351,
      354,
      357,
      360,
      363,
      366
    ],
    [
      369,
      372,
      375,
      378,
      381,
      384,
      237,
      390,
      393,
      396,
      399,
      402
    ],
    [
      405,
      408,
      411,
      414,
      417,
      420,
      423,
      276,
      429,
      432,
      435,
      438
    ],
    [
      441,
      444,
      447,
      450,
      453,
      456,
      459,
      462,
      315,
      468,
      471,
      474
    ],
    [
      477,
      480,
      483,
      486,
      489,
      492,
      495,
      498,
      501,
      354,
      507,
      510
    ],
    [
      513,
      516,
      519,
      522,
      525,
      528,
      531,
      534,
      537,
      540,
      393,
      546
    ]
  ],
  "supply": [
    150,
    180,
    210,
    240,
    270,
    300,
    330,
    360,
    390,
    420,
    930
  ],
  "demand": [
    150,
    180,
    210,
    240,
    270,
    300,
    330,
    360,
    390,
    420,
    450,
    480
  ]
}
```

LP optimum: **1.04418e+06**; dual gap 0. Occurrences: RBSM_S3.

Public author file. Some instances already contain dummy rows/columns.

## RBSM_S4

Source E02, rbsm_S4.txt. Shape 11 x 12; balanced: True; kind: author_synthetic.

```json
{
  "costs": [
    [
      13,
      35,
      30,
      36,
      35,
      30,
      30,
      33,
      31,
      36,
      15,
      39
    ],
    [
      39,
      30,
      25,
      32,
      28,
      13,
      11,
      32,
      34,
      27,
      14,
      25
    ],
    [
      12,
      39,
      15,
      11,
      13,
      30,
      30,
      31,
      12,
      25,
      32,
      13
    ],
    [
      33,
      10,
      14,
      38,
      38,
      12,
      12,
      15,
      13,
      15,
      37,
      14
    ],
    [
      37,
      11,
      25,
      10,
      14,
      35,
      29,
      14,
      33,
      14,
      37,
      37
    ],
    [
      79,
      88,
      70,
      70,
      83,
      71,
      92,
      93,
      77,
      95,
      82,
      77
    ],
    [
      80,
      98,
      98,
      84,
      73,
      91,
      88,
      86,
      81,
      78,
      73,
      73
    ],
    [
      83,
      94,
      77,
      94,
      76,
      91,
      81,
      70,
      85,
      91,
      99,
      84
    ],
    [
      78,
      75,
      78,
      81,
      79,
      81,
      81,
      98,
      83,
      95,
      88,
      77
    ],
    [
      99,
      81,
      79,
      87,
      89,
      81,
      76,
      74,
      76,
      78,
      89,
      94
    ],
    [
      91,
      83,
      80,
      92,
      97,
      97,
      80,
      89,
      92,
      71,
      83,
      99
    ]
  ],
  "supply": [
    200,
    106,
    139,
    137,
    249,
    171,
    172,
    113,
    230,
    241,
    199
  ],
  "demand": [
    315,
    309,
    41,
    43,
    110,
    162,
    274,
    184,
    70,
    201,
    125,
    123
  ]
}
```

LP optimum: **92212**; dual gap 0. Occurrences: RBSM_S4, CSM_S4.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_S4 | optimal | 92212 |

## RBSM_S5

Source E02, rbsm_S5.txt. Shape 11 x 12; balanced: True; kind: author_synthetic.

```json
{
  "costs": [
    [
      1,
      52,
      53,
      54,
      55,
      56,
      57,
      58,
      59,
      60,
      61,
      12
    ],
    [
      63,
      14,
      65,
      66,
      67,
      68,
      69,
      70,
      71,
      72,
      73,
      74
    ],
    [
      75,
      76,
      27,
      78,
      79,
      80,
      81,
      82,
      83,
      84,
      85,
      86
    ],
    [
      87,
      88,
      89,
      40,
      91,
      92,
      93,
      94,
      95,
      96,
      97,
      98
    ],
    [
      99,
      100,
      101,
      102,
      53,
      104,
      105,
      106,
      107,
      108,
      109,
      110
    ],
    [
      111,
      112,
      113,
      114,
      115,
      66,
      117,
      118,
      119,
      120,
      121,
      122
    ],
    [
      123,
      124,
      125,
      126,
      127,
      128,
      79,
      130,
      131,
      132,
      133,
      134
    ],
    [
      135,
      136,
      137,
      138,
      139,
      140,
      141,
      92,
      143,
      144,
      145,
      146
    ],
    [
      147,
      148,
      149,
      150,
      151,
      152,
      153,
      154,
      105,
      156,
      157,
      158
    ],
    [
      159,
      160,
      161,
      162,
      163,
      164,
      165,
      166,
      167,
      118,
      169,
      170
    ],
    [
      171,
      172,
      173,
      174,
      175,
      176,
      177,
      178,
      179,
      180,
      131,
      182
    ]
  ],
  "supply": [
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    310
  ],
  "demand": [
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160
  ]
}
```

LP optimum: **116020**; dual gap 0. Occurrences: RBSM_S5, CSM_S3, CSM_S5.

Public author file. Some instances already contain dummy rows/columns.

| occurrence | method | published |
| --- | --- | --- |
| CSM_S3 | optimal | 1044180 |
| CSM_S5 | optimal | 116020 |

## CSM_N03

Source E12, Data document N03. Shape 5 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      73,
      40,
      9,
      79,
      20
    ],
    [
      62,
      93,
      96,
      8,
      13
    ],
    [
      96,
      65,
      80,
      50,
      65
    ],
    [
      57,
      58,
      29,
      12,
      87
    ],
    [
      56,
      23,
      87,
      18,
      1
    ]
  ],
  "supply": [
    8,
    7,
    9,
    3,
    5
  ],
  "demand": [
    6,
    8,
    10,
    4,
    4
  ]
}
```

LP optimum: **1079**; dual gap 0. Occurrences: CSM_N03.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N03 | optimal | 1102 |

## CSM_N04

Source E12, Data document N04. Shape 3 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      4,
      4,
      7,
      5
    ],
    [
      5,
      6,
      7,
      4,
      8
    ],
    [
      3,
      4,
      6,
      3,
      4
    ]
  ],
  "supply": [
    100,
    125,
    175
  ],
  "demand": [
    60,
    80,
    85,
    105,
    70
  ]
}
```

LP optimum: **1580**; dual gap 0. Occurrences: CSM_N04.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N04 | optimal | 1580 |

## CSM_N06

Source E12, Data document N06. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      3,
      1,
      7,
      4
    ],
    [
      2,
      6,
      5,
      9
    ],
    [
      8,
      3,
      3,
      2
    ]
  ],
  "supply": [
    300,
    400,
    500
  ],
  "demand": [
    250,
    350,
    400,
    200
  ]
}
```

LP optimum: **2850**; dual gap 0. Occurrences: CSM_N06, MRM_BTP4.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N06 | optimal | 2850 |
| MRM_BTP4 | NWCM | 4400 |
| MRM_BTP4 | LCM | 2900 |
| MRM_BTP4 | VAM | 2850 |
| MRM_BTP4 | MRM | 2850 |
| MRM_BTP4 | optimal | 2850 |

## CSM_N18

Source E12, Data document N18. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      2,
      5,
      4
    ],
    [
      6,
      1,
      2
    ],
    [
      4,
      5,
      2
    ]
  ],
  "supply": [
    4,
    6,
    6
  ],
  "demand": [
    3,
    7,
    6
  ]
}
```

LP optimum: **29**; dual gap 0. Occurrences: CSM_N18.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N18 | optimal | 29 |

## CSM_N28

Source E12, Data document N28. Shape 3 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      2,
      7,
      8,
      8,
      3
    ],
    [
      5,
      6,
      5,
      5,
      6
    ],
    [
      5,
      7,
      8,
      8,
      3
    ]
  ],
  "supply": [
    2,
    3,
    5
  ],
  "demand": [
    3,
    1,
    1,
    2,
    3
  ]
}
```

LP optimum: **40**; dual gap 0. Occurrences: CSM_N28.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N28 | optimal | 40 |

## CSM_N33

Source E12, Data document N33. Shape 2 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      400,
      510,
      800,
      270
    ],
    [
      600,
      450,
      750,
      500
    ]
  ],
  "supply": [
    200,
    100
  ],
  "demand": [
    100,
    100,
    75,
    25
  ]
}
```

LP optimum: **151750**; dual gap 0. Occurrences: CSM_N33.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N33 | optimal | 151750 |

## CSM_N35

Source E12, Data document N35. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      13,
      18,
      30,
      8
    ],
    [
      55,
      20,
      25,
      40
    ],
    [
      30,
      6,
      50,
      10
    ]
  ],
  "supply": [
    8,
    10,
    11
  ],
  "demand": [
    4,
    7,
    6,
    12
  ]
}
```

LP optimum: **412**; dual gap 0. Occurrences: CSM_N35.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| CSM_N35 | optimal | 417 |

## CSM_Real1

Source E12, Data document Real1. Shape 2 x 94; balanced: True; kind: author_real.

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
    308252,
    138801
  ],
  "demand": [
    3852,
    4759,
    1312,
    3451,
    7537,
    2827,
    3878,
    15224,
    2530,
    5690,
    2494,
    2383,
    32901,
    7314,
    2486,
    0,
    249,
    2735,
    498,
    1989,
    4475,
    6091,
    373,
    5492,
    17978,
    4305,
    23799,
    1597,
    2773,
    2556,
    48509,
    3279,
    4183,
    1303,
    795,
    4024,
    1381,
    2597,
    1666,
    4848,
    125,
    0,
    0,
    10192,
    0,
    4475,
    3356,
    0,
    2611,
    2984,
    1368,
    0,
    1119,
    249,
    0,
    9447,
    2984,
    2362,
    125,
    2984,
    26599,
    746,
    249,
    0,
    14055,
    1437,
    2283,
    556,
    812,
    5786,
    2034,
    5911,
    5026,
    524,
    1133,
    464,
    1792,
    1330,
    1457,
    1668,
    3827,
    7947,
    297,
    759,
    9074,
    1436,
    864,
    2217,
    1160,
    519,
    4166,
    614,
    19405,
    30392
  ]
}
```

LP optimum: **1.29284e+07**; dual gap 0. Occurrences: CSM_Real1, EDM_R1.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| EDM_R1 | optimal | 12928429 |

## CSM_Real2

Source E12, Data document Real2. Shape 2 x 94; balanced: True; kind: author_real.

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
    341015,
    138738
  ],
  "demand": [
    3332,
    3976,
    1252,
    3494,
    9871,
    3027,
    5214,
    20029,
    2437,
    5584,
    2615,
    2184,
    39154,
    6641,
    2735,
    0,
    249,
    2984,
    746,
    2238,
    4848,
    6837,
    373,
    4677,
    17447,
    4487,
    24968,
    1804,
    3137,
    2538,
    50087,
    3445,
    4375,
    1444,
    919,
    4024,
    1389,
    2960,
    1660,
    5221,
    125,
    0,
    0,
    11063,
    0,
    4972,
    3729,
    125,
    2859,
    5096,
    1492,
    0,
    871,
    249,
    125,
    10129,
    3232,
    2735,
    249,
    12554,
    28961,
    746,
    125,
    0,
    12664,
    1382,
    2405,
    479,
    724,
    6258,
    1924,
    5195,
    5217,
    536,
    924,
    385,
    2053,
    1111,
    1340,
    1712,
    3630,
    8300,
    321,
    679,
    8954,
    1385,
    862,
    2372,
    1225,
    480,
    4369,
    556,
    20814,
    27658
  ]
}
```

LP optimum: **1.36571e+07**; dual gap 0. Occurrences: CSM_Real2, EDM_R2.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| EDM_R2 | optimal | 13657053 |

## CSM_Real3

Source E12, Data document Real3. Shape 2 x 94; balanced: True; kind: author_real.

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
    280110,
    138801
  ],
  "demand": [
    3300,
    4628,
    1250,
    2852,
    8202,
    2916,
    3912,
    16157,
    2695,
    5526,
    2699,
    2271,
    41855,
    7074,
    1616,
    0,
    125,
    1741,
    373,
    1243,
    2859,
    3854,
    249,
    5151,
    17117,
    4368,
    24291,
    1560,
    2679,
    2952,
    42223,
    3585,
    4182,
    1423,
    838,
    3282,
    1491,
    2324,
    1553,
    3108,
    125,
    0,
    125,
    6464,
    0,
    2859,
    2238,
    0,
    1616,
    2921,
    871,
    0,
    498,
    125,
    0,
    6091,
    1865,
    1616,
    125,
    2921,
    17029,
    498,
    249,
    0,
    13885,
    1516,
    2480,
    410,
    799,
    6616,
    1980,
    5900,
    4721,
    584,
    1032,
    419,
    1702,
    1290,
    1536,
    1725,
    3455,
    7792,
    341,
    632,
    9100,
    1269,
    897,
    2333,
    1296,
    452,
    3957,
    487,
    20317,
    32228
  ]
}
```

LP optimum: **1.22966e+07**; dual gap 0. Occurrences: CSM_Real3, EDM_R3.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| EDM_R3 | optimal | 12296587 |

## CSM_Real4

Source E12, Data document Real4. Shape 2 x 94; balanced: True; kind: author_real.

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
    350910,
    142165
  ],
  "demand": [
    3512,
    4300,
    1291,
    3477,
    9394,
    3031,
    4597,
    22500,
    1776,
    5384,
    2824,
    2530,
    42638,
    7341,
    2735,
    0,
    249,
    2984,
    746,
    2238,
    4848,
    6837,
    3737,
    5858,
    16806,
    4210,
    24717,
    1715,
    2549,
    2520,
    50440,
    3185,
    4359,
    1437,
    914,
    3120,
    1551,
    2109,
    1578,
    5345,
    125,
    0,
    0,
    11187,
    0,
    4972,
    3729,
    125,
    2859,
    8452,
    1492,
    0,
    871,
    249,
    125,
    10317,
    3232,
    2735,
    249,
    8452,
    29085,
    746,
    373,
    0,
    13607,
    1421,
    2068,
    554,
    877,
    6207,
    1844,
    6259,
    4824,
    610,
    1175,
    403,
    1840,
    1110,
    1389,
    1739,
    3546,
    8113,
    348,
    753,
    8366,
    1329,
    970,
    2121,
    1181,
    530,
    3778,
    497,
    19912,
    34947
  ]
}
```

LP optimum: **1.41176e+07**; dual gap 0. Occurrences: CSM_Real4, EDM_R4.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| EDM_R4 | optimal | 14117586 |

## CSM_Real5

Source E12, Data document Real5. Shape 2 x 94; balanced: True; kind: author_real.

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
    359746,
    138801
  ],
  "demand": [
    3269,
    4456,
    1277,
    2783,
    8888,
    3679,
    4621,
    18426,
    2745,
    5940,
    2408,
    2437,
    48268,
    5585,
    3108,
    0,
    249,
    3356,
    746,
    2486,
    5594,
    7707,
    373,
    4944,
    19086,
    3758,
    27005,
    1884,
    3139,
    2275,
    48013,
    3411,
    4479,
    1386,
    911,
    3405,
    1402,
    3198,
    1657,
    5967,
    249,
    0,
    0,
    12678,
    0,
    5594,
    4226,
    125,
    3232,
    7955,
    1616,
    0,
    995,
    373,
    125,
    11560,
    3605,
    3108,
    249,
    7955,
    32938,
    871,
    249,
    0,
    13500,
    1377,
    2189,
    589,
    752,
    5974,
    1588,
    6085,
    4578,
    512,
    1056,
    452,
    2240,
    1138,
    1268,
    1818,
    3634,
    8274,
    300,
    703,
    8162,
    1308,
    901,
    2438,
    1088,
    454,
    4199,
    613,
    19521,
    29812
  ]
}
```

LP optimum: **1.40174e+07**; dual gap 0. Occurrences: CSM_Real5, EDM_R5.

Data and result documents have label/matrix inconsistencies; do not join by label alone.

| occurrence | method | published |
| --- | --- | --- |
| EDM_R5 | optimal | 14017419 |

## EDM_C01

Source E09, C01 (Goyal,
  1984). Shape 3 x 3; balanced: False; kind: literature.

```json
{
  "costs": [
    [
      6,
      10,
      14
    ],
    [
      12,
      19,
      21
    ],
    [
      15,
      14,
      17
    ]
  ],
  "supply": [
    50,
    50,
    50
  ],
  "demand": [
    30,
    40,
    55
  ]
}
```

LP optimum: **1650**; dual gap 0. Occurrences: EDM_C01.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C01 | optimal | 1650 |

## EDM_C04

Source E09, C04 (Uddin
  et al., 2016). Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      6,
      3,
      5,
      4
    ],
    [
      5,
      9,
      2,
      7
    ],
    [
      5,
      7,
      8,
      6
    ]
  ],
  "supply": [
    22,
    15,
    8
  ],
  "demand": [
    7,
    12,
    17,
    9
  ]
}
```

LP optimum: **149**; dual gap 0. Occurrences: EDM_C04.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C04 | optimal | 149 |

## EDM_C07

Source E09, C07 (Uddin
  et al., 2016). Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      19,
      30,
      50,
      12
    ],
    [
      70,
      30,
      40,
      60
    ],
    [
      40,
      10,
      60,
      20
    ]
  ],
  "supply": [
    7,
    10,
    18
  ],
  "demand": [
    5,
    8,
    7,
    15
  ]
}
```

LP optimum: **799**; dual gap 0. Occurrences: EDM_C07.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C07 | optimal | 799 |

## EDM_C08

Source E09, C08 (Morade,
  2017). Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      50,
      30,
      220
    ],
    [
      90,
      45,
      170
    ],
    [
      250,
      200,
      50
    ]
  ],
  "supply": [
    1,
    3,
    4
  ],
  "demand": [
    4,
    2,
    2
  ]
}
```

LP optimum: **820**; dual gap 0. Occurrences: EDM_C08.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C08 | optimal | 820 |

## EDM_C09

Source E09, C09 (Amaliah
  et al., 2019). Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      8,
      7
    ],
    [
      18,
      8,
      12
    ],
    [
      8,
      12,
      12
    ]
  ],
  "supply": [
    13,
    14,
    8
  ],
  "demand": [
    14,
    8,
    13
  ]
}
```

LP optimum: **291**; dual gap 0. Occurrences: EDM_C09.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C09 | optimal | 291 |

## EDM_C11

Source E09, C11 (Juman
  & Hoque, 2015). Shape 4 x 6; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      9,
      12,
      9,
      6,
      9,
      10
    ],
    [
      7,
      3,
      7,
      7,
      5,
      5
    ],
    [
      6,
      5,
      9,
      11,
      3,
      11
    ],
    [
      6,
      8,
      11,
      2,
      2,
      10
    ]
  ],
  "supply": [
    2,
    5,
    6,
    9
  ],
  "demand": [
    2,
    2,
    4,
    4,
    4,
    6
  ]
}
```

LP optimum: **109**; dual gap 0. Occurrences: EDM_C11.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C11 | optimal | 109 |

## EDM_C13

Source E09, C13 (Nath
  Mondal et al., 2015). Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      12,
      4,
      9,
      5
    ],
    [
      8,
      1,
      6,
      6
    ],
    [
      1,
      2,
      4,
      7
    ]
  ],
  "supply": [
    55,
    40,
    30
  ],
  "demand": [
    40,
    20,
    45,
    20
  ]
}
```

LP optimum: **605**; dual gap 0. Occurrences: EDM_C13.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C13 | optimal | 605 |

## EDM_C16

Source E09, C16 (Uddin
  et al., 2016). Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      1,
      2,
      1,
      4
    ],
    [
      4,
      2,
      5,
      9
    ],
    [
      20,
      40,
      30,
      10
    ]
  ],
  "supply": [
    30,
    50,
    20
  ],
  "demand": [
    20,
    40,
    30,
    10
  ]
}
```

LP optimum: **450**; dual gap 0. Occurrences: EDM_C16.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C16 | optimal | 450 |

## EDM_C19

Source E09, C19 (Kulkarni
  & Datar, 2010). Shape 4 x 3; balanced: False; kind: literature.

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

LP optimum: **840**; dual gap 0. Occurrences: EDM_C19.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C19 | optimal | 840 |

## EDM_C20

Source E09, C20 (Schrenk
  et al., 2011). Shape 3 x 4; balanced: True; kind: literature.

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

LP optimum: **59**; dual gap 0. Occurrences: EDM_C20.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C20 | optimal | 59 |

## EDM_C22

Source E09, C22 (Adlakha,
  2009). Shape 4 x 5; balanced: True; kind: literature.

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

LP optimum: **390**; dual gap 0. Occurrences: EDM_C22.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_C22 | optimal | 390 |

## EDM_S1

Source E09, S1 Synthesis
  1. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      2,
      10,
      4
    ],
    [
      12,
      6,
      3,
      9
    ],
    [
      11,
      13,
      5,
      8
    ]
  ],
  "supply": [
    70,
    55,
    90
  ],
  "demand": [
    85,
    35,
    50,
    45
  ]
}
```

LP optimum: **1375**; dual gap 0. Occurrences: EDM_S1, EDM_S2.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_S1 | optimal | 1375 |
| EDM_S2 | optimal | 172 |

## EDM_S3

Source E09, S3 Synthesis
  3. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      3,
      8,
      6
    ],
    [
      4,
      2,
      5,
      10
    ],
    [
      2,
      6,
      5,
      1
    ]
  ],
  "supply": [
    6,
    10,
    4
  ],
  "demand": [
    2,
    5,
    5,
    8
  ]
}
```

LP optimum: **73**; dual gap 0. Occurrences: EDM_S3.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_S3 | optimal | 73 |

## EDM_S4

Source E09, S4 Synthesis
  4. Shape 4 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      5,
      5,
      10
    ],
    [
      6,
      6,
      15
    ],
    [
      10,
      12,
      17
    ],
    [
      8,
      8,
      10
    ]
  ],
  "supply": [
    4,
    3,
    5,
    1
  ],
  "demand": [
    3,
    4,
    6
  ]
}
```

LP optimum: **127**; dual gap 0. Occurrences: EDM_S4.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_S4 | optimal | 127 |

## EDM_S5

Source E09, S5 Synthesis
  5. Shape 4 x 5; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      7,
      8,
      7,
      10,
      22
    ],
    [
      11,
      8,
      12,
      14,
      31
    ],
    [
      10,
      12,
      12,
      8,
      32
    ],
    [
      14,
      10,
      13,
      5,
      35
    ]
  ],
  "supply": [
    25,
    25,
    50,
    20
  ],
  "demand": [
    30,
    30,
    30,
    10,
    20
  ]
}
```

LP optimum: **1380**; dual gap 0. Occurrences: EDM_S5.

Secondary author dataset; original reference not necessarily accessed.

| occurrence | method | published |
| --- | --- | --- |
| EDM_S5 | optimal | 1380 |

## MRM_BTP1

Source E15, Tables 42/45/46 BTP1. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      2,
      1
    ],
    [
      3,
      8,
      4
    ],
    [
      6,
      5,
      2
    ]
  ],
  "supply": [
    50,
    70,
    45
  ],
  "demand": [
    40,
    65,
    60
  ]
}
```

LP optimum: **475**; dual gap 0. Occurrences: MRM_BTP1.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP1 | NWCM | 770 |
| MRM_BTP1 | LCM | 605 |
| MRM_BTP1 | VAM | 490 |
| MRM_BTP1 | MRM | 475 |
| MRM_BTP1 | optimal | 475 |

## MRM_BTP3

Source E15, Tables 42/45/46 BTP3. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      9,
      8,
      5,
      7
    ],
    [
      4,
      6,
      8,
      7
    ],
    [
      5,
      8,
      9,
      5
    ]
  ],
  "supply": [
    12,
    14,
    16
  ],
  "demand": [
    8,
    18,
    13,
    3
  ]
}
```

LP optimum: **240**; dual gap 0. Occurrences: MRM_BTP3.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP3 | NWCM | 320 |
| MRM_BTP3 | LCM | 248 |
| MRM_BTP3 | VAM | 240 |
| MRM_BTP3 | MRM | 248 |
| MRM_BTP3 | optimal | 240 |

## MRM_BTP6

Source E15, Tables 42/45/46 BTP6. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      50,
      60,
      100,
      50
    ],
    [
      80,
      40,
      70,
      50
    ],
    [
      90,
      70,
      30,
      50
    ]
  ],
  "supply": [
    20,
    38,
    16
  ],
  "demand": [
    10,
    18,
    22,
    24
  ]
}
```

LP optimum: **3320**; dual gap 0. Occurrences: MRM_BTP6.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP6 | NWCM | 4160 |
| MRM_BTP6 | LCM | 3500 |
| MRM_BTP6 | VAM | 3320 |
| MRM_BTP6 | MRM | 3320 |
| MRM_BTP6 | optimal | 3320 |

## MRM_BTP7

Source E15, Tables 42/45/46 BTP7. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      4,
      3,
      5
    ],
    [
      6,
      5,
      4
    ],
    [
      8,
      10,
      7
    ]
  ],
  "supply": [
    90,
    80,
    100
  ],
  "demand": [
    70,
    120,
    80
  ]
}
```

LP optimum: **1390**; dual gap 0. Occurrences: MRM_BTP7.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP7 | NWCM | 1500 |
| MRM_BTP7 | LCM | 1450 |
| MRM_BTP7 | VAM | 1500 |
| MRM_BTP7 | MRM | 1390 |
| MRM_BTP7 | optimal | 1390 |

## MRM_BTP8

Source E15, Tables 42/45/46 BTP8. Shape 3 x 3; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      5,
      7,
      8
    ],
    [
      4,
      4,
      6
    ],
    [
      6,
      7,
      7
    ]
  ],
  "supply": [
    70,
    30,
    50
  ],
  "demand": [
    65,
    42,
    43
  ]
}
```

LP optimum: **830**; dual gap 0. Occurrences: MRM_BTP8.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP8 | NWCM | 830 |
| MRM_BTP8 | LCM | 890 |
| MRM_BTP8 | VAM | 830 |
| MRM_BTP8 | MRM | 830 |
| MRM_BTP8 | optimal | 830 |

## MRM_BTP9

Source E15, Tables 42/45/46 BTP9. Shape 4 x 6; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      1,
      2,
      1,
      4,
      5,
      2
    ],
    [
      3,
      3,
      2,
      1,
      4,
      3
    ],
    [
      4,
      2,
      5,
      9,
      6,
      2
    ],
    [
      3,
      1,
      7,
      3,
      4,
      6
    ]
  ],
  "supply": [
    30,
    50,
    75,
    20
  ],
  "demand": [
    20,
    40,
    30,
    10,
    50,
    25
  ]
}
```

LP optimum: **430**; dual gap 0. Occurrences: MRM_BTP9.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP9 | NWCM | 740 |
| MRM_BTP9 | LCM | 470 |
| MRM_BTP9 | VAM | 450 |
| MRM_BTP9 | MRM | 450 |
| MRM_BTP9 | optimal | 430 |

## MRM_BTP10

Source E15, Tables 42/45/46 BTP10. Shape 3 x 4; balanced: True; kind: literature.

```json
{
  "costs": [
    [
      2,
      2,
      2,
      1
    ],
    [
      10,
      8,
      5,
      4
    ],
    [
      7,
      6,
      6,
      8
    ]
  ],
  "supply": [
    3,
    7,
    5
  ],
  "demand": [
    4,
    3,
    4,
    4
  ]
}
```

LP optimum: **68**; dual gap 0. Occurrences: MRM_BTP10.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_BTP10 | NWCM | 93 |
| MRM_BTP10 | LCM | 79 |
| MRM_BTP10 | VAM | 68 |
| MRM_BTP10 | MRM | 68 |
| MRM_BTP10 | optimal | 68 |

## MRM_UTP2

Source E15, Tables 42/45/46 UTP2. Shape 4 x 4; balanced: False; kind: literature.

```json
{
  "costs": [
    [
      12,
      10,
      6,
      13
    ],
    [
      19,
      8,
      16,
      25
    ],
    [
      17,
      15,
      15,
      20
    ],
    [
      23,
      22,
      26,
      12
    ]
  ],
  "supply": [
    150,
    200,
    600,
    225
  ],
  "demand": [
    300,
    500,
    75,
    100
  ]
}
```

LP optimum: **12475**; dual gap 0. Occurrences: MRM_UTP2.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_UTP2 | NWCM | 14725 |
| MRM_UTP2 | LCM | 14625 |
| MRM_UTP2 | VAM | 13225 |
| MRM_UTP2 | MRM | 12475 |
| MRM_UTP2 | optimal | 12475 |

## MRM_UTP3

Source E15, Tables 42/45/46 UTP3. Shape 3 x 5; balanced: False; kind: literature.

```json
{
  "costs": [
    [
      5,
      8,
      6,
      6,
      3
    ],
    [
      4,
      7,
      7,
      6,
      5
    ],
    [
      8,
      4,
      6,
      6,
      4
    ]
  ],
  "supply": [
    800,
    500,
    900
  ],
  "demand": [
    400,
    400,
    500,
    400,
    800
  ]
}
```

LP optimum: **9200**; dual gap 0. Occurrences: MRM_UTP3.

Author-uploaded full text accessed through browser; local direct PDF unavailable.

| occurrence | method | published |
| --- | --- | --- |
| MRM_UTP3 | NWCM | 13100 |
| MRM_UTP3 | LCM | 9800 |
| MRM_UTP3 | VAM | 9200 |
| MRM_UTP3 | MRM | 9200 |
| MRM_UTP3 | optimal | 9200 |

## MRM_HDTP3

Source E15, Table 43 HDTP-3. Shape 12 x 11; balanced: False; kind: author_synthetic.

```json
{
  "costs": [
    [
      7,
      5,
      9,
      8,
      6,
      4,
      3,
      6,
      5,
      9,
      7
    ],
    [
      6,
      8,
      7,
      5,
      9,
      11,
      10,
      3,
      6,
      7,
      4
    ],
    [
      8,
      6,
      5,
      7,
      9,
      10,
      4,
      11,
      8,
      5,
      6
    ],
    [
      4,
      7,
      8,
      6,
      5,
      9,
      11,
      10,
      4,
      7,
      6
    ],
    [
      5,
      9,
      6,
      4,
      8,
      7,
      10,
      12,
      6,
      5,
      8
    ],
    [
      7,
      5,
      9,
      6,
      8,
      4,
      11,
      10,
      12,
      7,
      5
    ],
    [
      8,
      7,
      5,
      9,
      6,
      4,
      12,
      11,
      5,
      8,
      7
    ],
    [
      6,
      8,
      7,
      9,
      5,
      11,
      4,
      6,
      9,
      5,
      8
    ],
    [
      4,
      9,
      5,
      8,
      7,
      10,
      6,
      3,
      9,
      5,
      7
    ],
    [
      5,
      8,
      7,
      6,
      4,
      10,
      12,
      9,
      7,
      8,
      6
    ],
    [
      7,
      6,
      8,
      5,
      9,
      11,
      4,
      5,
      7,
      10,
      8
    ],
    [
      6,
      7,
      9,
      4,
      5,
      8,
      10,
      11,
      6,
      7,
      5
    ]
  ],
  "supply": [
    60,
    80,
    40,
    70,
    50,
    60,
    70,
    40,
    80,
    50,
    70,
    50
  ],
  "demand": [
    60,
    70,
    50,
    60,
    80,
    40,
    50,
    70,
    40,
    50,
    60
  ]
}
```

LP optimum: **2600**; dual gap 0. Occurrences: MRM_HDTP3.


