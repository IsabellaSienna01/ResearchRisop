# Reproduction audit

A matched scalar cost does not uniquely validate every decision rule. Unspecified ties are completed deterministically as documented. Claims with unavailable algorithms are retained. This is the historical core audit; the later restricted JHM reproduction is recorded separately in [jhm_results.md](jhm_results.md) and [jhm_supplement.md](jhm_supplement.md), without changing the core 207-comparison denominator.

| occurrence | source | locator | method | published_cost | reproduced_cost | match | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L01_Table2 | L01 | Table 2; Table 7 P09 | VAM | 475 | 475 | True | qualified deterministic implementation |
| L01_Table2 | L01 | Table 2; Table 7 P09 | TDM1 | 475 | 475 | True | qualified deterministic implementation |
| L01_Table2 | L01 | Table 2; Table 7 P09 | TOCM_MT | 435 | unavailable | unavailable | method not implemented / worked allocation claim |
| L01_Table2 | L01 | Table 2; Table 7 P09 | JHM | 460 | unavailable | unavailable | method not implemented / worked allocation claim |
| L01_Table2 | L01 | Table 2; Table 7 P09 | BCE | 435 | 435 | True | qualified deterministic implementation |
| L01_Table2 | L01 | Table 2; Table 7 P09 | optimal | 435 | 435 | True | LP verified |
| L02_Table3 | L02 | Tables 3-6; N09 | RBSM | 111 | 111 | True | qualified deterministic implementation |
| L02_Table3 | L02 | Tables 3-6; N09 | optimal | 111 | 111 | True | LP verified |
| L02_Table7 | L02 | Table 7; N06 | RBSM | 7750 | 7750 | True | qualified deterministic implementation |
| L02_Table7 | L02 | Table 7; N06 | BCE | 8350 | unavailable | unavailable | NotImplementedError: BCE unbalanced branch/model not sufficiently unambiguous; no dummy substitution |
| L02_Table7 | L02 | Table 7; N06 | optimal | 7750 | 7750 | True | LP verified |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | SSM | 465 | 465 | True | qualified deterministic implementation |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | LCM | 473 | 473 | True | qualified deterministic implementation |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | VAM | 473 | 473 | True | qualified deterministic implementation |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | JHM | 475 | unavailable | unavailable | method not implemented / worked allocation claim |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | TOCM_MT | 475 | unavailable | unavailable | method not implemented / worked allocation claim |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | BCE | 475 | 475 | True | qualified deterministic implementation |
| L03_Table2 | L03 | Tables 2-5; Table 7 P26 | optimal | 465 | 465 | True | LP verified |
| L04_Example1 | L04 | Example 1; Table 9 | NWCM | 57 | 61 | False | qualified deterministic implementation |
| L04_Example1 | L04 | Example 1; Table 9 | LCM | 55 | 61 | False | qualified deterministic implementation |
| L04_Example1 | L04 | Example 1; Table 9 | VAM | 61 | 61 | True | qualified deterministic implementation |
| L04_Example1 | L04 | Example 1; Table 9 | AIP_MT | 61 | unavailable | unavailable | method not implemented / worked allocation claim |
| L04_Example1 | L04 | Example 1; Table 9 | optimal | 61 | 55 | False | LP verified |
| L04_Example1 | L04 | Example 1; Table 9 | AIP_worked | 55 | 55 | True | Published allocation audited; not a general algorithm reproduction |
| L04_Example2 | L04 | Example 2; Table 9 | NWCM | 2215 | 2245 | False | qualified deterministic implementation |
| L04_Example2 | L04 | Example 2; Table 9 | LCM | 1995 | 2360 | False | qualified deterministic implementation |
| L04_Example2 | L04 | Example 2; Table 9 | VAM | 2245 | 2245 | True | qualified deterministic implementation |
| L04_Example2 | L04 | Example 2; Table 9 | AIP_MT | 2360 | unavailable | unavailable | method not implemented / worked allocation claim |
| L04_Example2 | L04 | Example 2; Table 9 | optimal | 1945 | 1945 | True | LP verified |
| L04_Example2 | L04 | Example 2; Table 9 | AIP_worked | 1995 | 1995 | True | Published allocation audited; not a general algorithm reproduction |
| L05_Example1 | L05 | Example 1 | VAM | 1095 | 1095 | True | qualified deterministic implementation |
| L05_Example1 | L05 | Example 1 | LDVAM | 1095 | 1095 | True | qualified deterministic implementation |
| L05_Example1 | L05 | Example 1 | THP | 1045 | 1045 | True | qualified deterministic implementation |
| L05_Example1 | L05 | Example 1 | optimal | 985 | 985 | True | LP verified |
| L05_Example2 | L05 | Example 2 | VAM | 5125 | 5125 | True | qualified deterministic implementation |
| L05_Example2 | L05 | Example 2 | LDVAM | 5125 | 5125 | True | qualified deterministic implementation |
| L05_Example2 | L05 | Example 2 | THP | 4525 | 4525 | True | qualified deterministic implementation |
| L05_Example2 | L05 | Example 2 | optimal | 4525 | 4525 | True | LP verified |
| L05_Example3 | L05 | Example 3 | VAM | 2388 | 2388 | True | qualified deterministic implementation |
| L05_Example3 | L05 | Example 3 | LDVAM | 2388 | 2388 | True | qualified deterministic implementation |
| L05_Example3 | L05 | Example 3 | THP | 2366 | 2366 | True | qualified deterministic implementation |
| L05_Example3 | L05 | Example 3 | optimal | 2366 | 2366 | True | LP verified |
| E01_Example1 | E01 | Example 1; Tables 3 or 7 | NWCM | 3680 | 3680 | True | qualified deterministic implementation |
| E01_Example1 | E01 | Example 1; Tables 3 or 7 | LCM | 3670 | 3670 | True | qualified deterministic implementation |
| E01_Example1 | E01 | Example 1; Tables 3 or 7 | VAM | 3520 | 3520 | True | qualified deterministic implementation |
| E01_Example1 | E01 | Example 1; Tables 3 or 7 | TDM1 | 3570 | 3570 | True | qualified deterministic implementation |
| E01_Example1 | E01 | Example 1; Tables 3 or 7 | TDSM | 3710 | 3710 | True | qualified deterministic implementation |
| E01_Example2 | E01 | Example 2; Tables 3 or 7 | NWCM | 670 | 670 | True | qualified deterministic implementation |
| E01_Example2 | E01 | Example 2; Tables 3 or 7 | LCM | 650 | 650 | True | qualified deterministic implementation |
| E01_Example2 | E01 | Example 2; Tables 3 or 7 | VAM | 650 | 650 | True | qualified deterministic implementation |
| E01_Example2 | E01 | Example 2; Tables 3 or 7 | TDM1 | 630 | 650 | False | qualified deterministic implementation |
| E01_Example2 | E01 | Example 2; Tables 3 or 7 | TDSM | 610 | 610 | True | qualified deterministic implementation |
| E01_Example3 | E01 | Example 3; Tables 3 or 7 | NWCM | 1015 | 1015 | True | qualified deterministic implementation |
| E01_Example3 | E01 | Example 3; Tables 3 or 7 | LCM | 814 | 814 | True | qualified deterministic implementation |
| E01_Example3 | E01 | Example 3; Tables 3 or 7 | VAM | 779 | 779 | True | qualified deterministic implementation |
| E01_Example3 | E01 | Example 3; Tables 3 or 7 | TDM1 | 779 | 779 | True | qualified deterministic implementation |
| E01_Example3 | E01 | Example 3; Tables 3 or 7 | TDSM | 781 | 781 | True | qualified deterministic implementation |
| E01_Example4 | E01 | Example 4; Tables 3 or 7 | NWCM | 1451 | 1451 | True | qualified deterministic implementation |
| E01_Example4 | E01 | Example 4; Tables 3 or 7 | VAM | 490 | 490 | True | qualified deterministic implementation |
| E01_Example4 | E01 | Example 4; Tables 3 or 7 | TDM1 | 490 | 490 | True | qualified deterministic implementation |
| E01_Example4 | E01 | Example 4; Tables 3 or 7 | TDSM | 490 | 490 | True | qualified deterministic implementation |
| E01_Example5 | E01 | Example 5; Tables 3 or 7 | NWCM | 1853 | 1853 | True | qualified deterministic implementation |
| E01_Example5 | E01 | Example 5; Tables 3 or 7 | VAM | 1401 | 1401 | True | qualified deterministic implementation |
| E01_Example5 | E01 | Example 5; Tables 3 or 7 | TDM1 | 1401 | 1401 | True | qualified deterministic implementation |
| E01_Example5 | E01 | Example 5; Tables 3 or 7 | TDSM | 1661 | 1465 | False | qualified deterministic implementation |
| E01_Example6 | E01 | Example 6; Tables 3 or 7 | NWCM | 1651 | 1651 | True | qualified deterministic implementation |
| E01_Example6 | E01 | Example 6; Tables 3 or 7 | VAM | 740 | 586 | False | qualified deterministic implementation |
| E01_Example6 | E01 | Example 6; Tables 3 or 7 | TDM1 | 712 | 558 | False | qualified deterministic implementation |
| E01_Example6 | E01 | Example 6; Tables 3 or 7 | TDSM | 712 | 558 | False | qualified deterministic implementation |
| E01_Example7 | E01 | Example 7; Tables 3 or 7 | NWCM | 2251 | 2251 | True | qualified deterministic implementation |
| E01_Example7 | E01 | Example 7; Tables 3 or 7 | VAM | 844 | 826 | False | qualified deterministic implementation |
| E01_Example7 | E01 | Example 7; Tables 3 or 7 | TDM1 | 935 | 830 | False | qualified deterministic implementation |
| E01_Example7 | E01 | Example 7; Tables 3 or 7 | TDSM | 979 | 844 | False | qualified deterministic implementation |
| CSM_N01 | E12 | Data document N01 | optimal | 5600 | 5600 | True | LP verified |
| CSM_N02 | E12 | Data document N02 | optimal | 28 | 28 | True | LP verified |
| CSM_N03 | E12 | Data document N03 | optimal | 1102 | 1079 | False | LP verified |
| CSM_N04 | E12 | Data document N04 | optimal | 1580 | 1580 | True | LP verified |
| CSM_N05 | E12 | Data document N05 | optimal | 410 | 410 | True | LP verified |
| CSM_N06 | E12 | Data document N06 | optimal | 2850 | 2850 | True | LP verified |
| CSM_N07 | E12 | Data document N07 | optimal | 1160 | 1160 | True | LP verified |
| CSM_N09 | E12 | Data document N09 | optimal | 111 | 111 | True | LP verified |
| CSM_N10 | E12 | Data document N10 | optimal | 910 | 910 | True | LP verified |
| CSM_N11 | E12 | Data document N11 | optimal | 2460 | 2460 | True | LP verified |
| CSM_N12 | E12 | Data document N12 | optimal | 425 | 425 | True | LP verified |
| CSM_N13 | E12 | Data document N13 | optimal | 4525 | 4525 | True | LP verified |
| CSM_N14 | E12 | Data document N14 | optimal | 920 | 920 | True | LP verified |
| CSM_N15 | E12 | Data document N15 | optimal | 156 | 156 | True | LP verified |
| CSM_N16 | E12 | Data document N16 | optimal | 1510 | 1510 | True | LP verified |
| CSM_N17 | E12 | Data document N17 | optimal | 743 | 743 | True | LP verified |
| CSM_N18 | E12 | Data document N18 | optimal | 29 | 29 | True | LP verified |
| CSM_N21 | E12 | Data document N21 | optimal | 4205 | 4205 | True | LP verified |
| CSM_N22 | E12 | Data document N22 | optimal | 12075 | 12075 | True | LP verified |
| CSM_N23 | E12 | Data document N23 | optimal | 23 | 23 | True | LP verified |
| CSM_N24 | E12 | Data document N24 | optimal | 3460 | 3460 | True | LP verified |
| CSM_N25 | E12 | Data document N25 | optimal | 809 | 809 | True | LP verified |
| CSM_N26 | E12 | Data document N26 | optimal | 490 | 490 | True | LP verified |
| CSM_N27 | E12 | Data document N27 | optimal | 59356 | 59356 | True | LP verified |
| CSM_N28 | E12 | Data document N28 | optimal | 40 | 40 | True | LP verified |
| CSM_N29 | E12 | Data document N29 | optimal | 3857 | 3857 | True | LP verified |
| CSM_N30 | E12 | Data document N30 | optimal | 465 | 465 | True | LP verified |
| CSM_N31 | E12 | Data document N31 | optimal | 1480 | 1480 | True | LP verified |
| CSM_N32 | E12 | Data document N32 | optimal | 348 | 1780 | False | LP verified |
| CSM_N33 | E12 | Data document N33 | optimal | 151750 | 151750 | True | LP verified |
| CSM_N34 | E12 | Data document N34 | optimal | 510 | 510 | True | LP verified |
| CSM_N35 | E12 | Data document N35 | optimal | 417 | 412 | False | LP verified |
| CSM_S1 | E12 | Data document S1 | optimal | 18855 | 18855 | True | LP verified |
| CSM_S2 | E12 | Data document S2 | optimal | 2790 | 153500 | False | LP verified |
| CSM_S3 | E12 | Data document S3 | optimal | 1044180 | 116020 | False | LP verified |
| CSM_S4 | E12 | Data document S4 | optimal | 92212 | 92212 | True | LP verified |
| CSM_S5 | E12 | Data document S5 | optimal | 116020 | 116020 | True | LP verified |
| EDM_C01 | E09 | C01 (Goyal, 1984) | optimal | 1650 | 1650 | True | LP verified |
| EDM_C03 | E09 | C03 (Ramadan & Ramadan, 2012) | optimal | 5600 | 5600 | True | LP verified |
| EDM_C04 | E09 | C04 (Uddin et al., 2016) | optimal | 149 | 149 | True | LP verified |
| EDM_C05 | E09 | C05 (Samuel, 2012) | optimal | 28 | 28 | True | LP verified |
| EDM_C06 | E09 | C06 (Hosseini, 2017) | optimal | 3460 | 3460 | True | LP verified |
| EDM_C07 | E09 | C07 (Uddin et al., 2016) | optimal | 799 | 799 | True | LP verified |
| EDM_C08 | E09 | C08 (Morade, 2017) | optimal | 820 | 820 | True | LP verified |
| EDM_C09 | E09 | C09 (Amaliah et al., 2019) | optimal | 291 | 291 | True | LP verified |
| EDM_C10 | E09 | C10 (Juman & Hoque, 2015) | optimal | 4525 | 4525 | True | LP verified |
| EDM_C11 | E09 | C11 (Juman & Hoque, 2015) | optimal | 109 | 109 | True | LP verified |
| EDM_C13 | E09 | C13 (Nath Mondal et al., 2015) | optimal | 605 | 605 | True | LP verified |
| EDM_C14 | E09 | C14 (Ahmed et al., 2015) | optimal | 425 | 425 | True | LP verified |
| EDM_C15 | E09 | C15 (Ahmed et al., 2015) | optimal | 465 | 465 | True | LP verified |
| EDM_C16 | E09 | C16 (Uddin et al., 2016) | optimal | 450 | 450 | True | LP verified |
| EDM_C17 | E09 | C17 (Das et al., 2014) | optimal | 1160 | 1160 | True | LP verified |
| EDM_C19 | E09 | C19 (Kulkarni & Datar, 2010) | optimal | 840 | 840 | True | LP verified |
| EDM_C20 | E09 | C20 (Schrenk et al., 2011) | optimal | 59 | 59 | True | LP verified |
| EDM_C21 | E09 | C21 (Imam et al., 2009) | optimal | 435 | 435 | True | LP verified |
| EDM_C22 | E09 | C22 (Adlakha, 2009) | optimal | 390 | 390 | True | LP verified |
| EDM_R1 | E09 | R1 Real 1 | optimal | 12928429 | 12928429 | True | LP verified |
| EDM_R2 | E09 | R2 Real 2 | optimal | 13657053 | 13657053 | True | LP verified |
| EDM_R3 | E09 | R3 Real 3 | optimal | 12296587 | 12296587 | True | LP verified |
| EDM_R4 | E09 | R4 Real 4 | optimal | 14117586 | 14117586 | True | LP verified |
| EDM_R5 | E09 | R5 Real 5 | optimal | 14017419 | 14017419 | True | LP verified |
| EDM_S1 | E09 | S1 Synthesis 1 | optimal | 1375 | 1375 | True | LP verified |
| EDM_S2 | E09 | S2 Synthesis 2 | optimal | 172 | 1375 | False | LP verified |
| EDM_S3 | E09 | S3 Synthesis 3 | optimal | 73 | 73 | True | LP verified |
| EDM_S4 | E09 | S4 Synthesis 4 | optimal | 127 | 127 | True | LP verified |
| EDM_S5 | E09 | S5 Synthesis 5 | optimal | 1380 | 1380 | True | LP verified |
| E11_Table3 | E11 | Tables III-VII, worked N32 | CSM | 1780 | 1780 | True | qualified deterministic implementation |
| E11_Table3 | E11 | Tables III-VII, worked N32 | SSM | 1820 | 1820 | True | qualified deterministic implementation |
| E11_Table3 | E11 | Tables III-VII, worked N32 | optimal | 1780 | 1780 | True | LP verified |
| MRM_BTP1 | E15 | Tables 42/45/46 BTP1 | NWCM | 770 | 770 | True | qualified deterministic implementation |
| MRM_BTP1 | E15 | Tables 42/45/46 BTP1 | LCM | 605 | 605 | True | qualified deterministic implementation |
| MRM_BTP1 | E15 | Tables 42/45/46 BTP1 | VAM | 490 | 490 | True | qualified deterministic implementation |
| MRM_BTP1 | E15 | Tables 42/45/46 BTP1 | MRM | 475 | 475 | True | qualified deterministic implementation |
| MRM_BTP1 | E15 | Tables 42/45/46 BTP1 | optimal | 475 | 475 | True | LP verified |
| MRM_BTP2 | E15 | Tables 42/45/46 BTP2 | NWCM | 730 | 730 | True | qualified deterministic implementation |
| MRM_BTP2 | E15 | Tables 42/45/46 BTP2 | LCM | 555 | 555 | True | qualified deterministic implementation |
| MRM_BTP2 | E15 | Tables 42/45/46 BTP2 | VAM | 555 | 555 | True | qualified deterministic implementation |
| MRM_BTP2 | E15 | Tables 42/45/46 BTP2 | MRM | 555 | 555 | True | qualified deterministic implementation |
| MRM_BTP2 | E15 | Tables 42/45/46 BTP2 | optimal | 555 | 555 | True | LP verified |
| MRM_BTP3 | E15 | Tables 42/45/46 BTP3 | NWCM | 320 | 320 | True | qualified deterministic implementation |
| MRM_BTP3 | E15 | Tables 42/45/46 BTP3 | LCM | 248 | 248 | True | qualified deterministic implementation |
| MRM_BTP3 | E15 | Tables 42/45/46 BTP3 | VAM | 240 | 248 | False | qualified deterministic implementation |
| MRM_BTP3 | E15 | Tables 42/45/46 BTP3 | MRM | 248 | 248 | True | qualified deterministic implementation |
| MRM_BTP3 | E15 | Tables 42/45/46 BTP3 | optimal | 240 | 240 | True | LP verified |
| MRM_BTP4 | E15 | Tables 42/45/46 BTP4 | NWCM | 4400 | 4400 | True | qualified deterministic implementation |
| MRM_BTP4 | E15 | Tables 42/45/46 BTP4 | LCM | 2900 | 2850 | False | qualified deterministic implementation |
| MRM_BTP4 | E15 | Tables 42/45/46 BTP4 | VAM | 2850 | 2850 | True | qualified deterministic implementation |
| MRM_BTP4 | E15 | Tables 42/45/46 BTP4 | MRM | 2850 | 2850 | True | qualified deterministic implementation |
| MRM_BTP4 | E15 | Tables 42/45/46 BTP4 | optimal | 2850 | 2850 | True | LP verified |
| MRM_BTP5 | E15 | Tables 42/45/46 BTP5 | NWCM | 540 | 540 | True | qualified deterministic implementation |
| MRM_BTP5 | E15 | Tables 42/45/46 BTP5 | LCM | 435 | 435 | True | qualified deterministic implementation |
| MRM_BTP5 | E15 | Tables 42/45/46 BTP5 | VAM | 470 | 470 | True | qualified deterministic implementation |
| MRM_BTP5 | E15 | Tables 42/45/46 BTP5 | MRM | 415 | 415 | True | qualified deterministic implementation |
| MRM_BTP5 | E15 | Tables 42/45/46 BTP5 | optimal | 410 | 410 | True | LP verified |
| MRM_BTP6 | E15 | Tables 42/45/46 BTP6 | NWCM | 4160 | 4160 | True | qualified deterministic implementation |
| MRM_BTP6 | E15 | Tables 42/45/46 BTP6 | LCM | 3500 | 3320 | False | qualified deterministic implementation |
| MRM_BTP6 | E15 | Tables 42/45/46 BTP6 | VAM | 3320 | 3320 | True | qualified deterministic implementation |
| MRM_BTP6 | E15 | Tables 42/45/46 BTP6 | MRM | 3320 | 3320 | True | qualified deterministic implementation |
| MRM_BTP6 | E15 | Tables 42/45/46 BTP6 | optimal | 3320 | 3320 | True | LP verified |
| MRM_BTP7 | E15 | Tables 42/45/46 BTP7 | NWCM | 1500 | 1500 | True | qualified deterministic implementation |
| MRM_BTP7 | E15 | Tables 42/45/46 BTP7 | LCM | 1450 | 1450 | True | qualified deterministic implementation |
| MRM_BTP7 | E15 | Tables 42/45/46 BTP7 | VAM | 1500 | 1500 | True | qualified deterministic implementation |
| MRM_BTP7 | E15 | Tables 42/45/46 BTP7 | MRM | 1390 | 1390 | True | qualified deterministic implementation |
| MRM_BTP7 | E15 | Tables 42/45/46 BTP7 | optimal | 1390 | 1390 | True | LP verified |
| MRM_BTP8 | E15 | Tables 42/45/46 BTP8 | NWCM | 830 | 830 | True | qualified deterministic implementation |
| MRM_BTP8 | E15 | Tables 42/45/46 BTP8 | LCM | 890 | 890 | True | qualified deterministic implementation |
| MRM_BTP8 | E15 | Tables 42/45/46 BTP8 | VAM | 830 | 830 | True | qualified deterministic implementation |
| MRM_BTP8 | E15 | Tables 42/45/46 BTP8 | MRM | 830 | 830 | True | qualified deterministic implementation |
| MRM_BTP8 | E15 | Tables 42/45/46 BTP8 | optimal | 830 | 830 | True | LP verified |
| MRM_BTP9 | E15 | Tables 42/45/46 BTP9 | NWCM | 740 | 740 | True | qualified deterministic implementation |
| MRM_BTP9 | E15 | Tables 42/45/46 BTP9 | LCM | 470 | 450 | False | qualified deterministic implementation |
| MRM_BTP9 | E15 | Tables 42/45/46 BTP9 | VAM | 450 | 450 | True | qualified deterministic implementation |
| MRM_BTP9 | E15 | Tables 42/45/46 BTP9 | MRM | 450 | 450 | True | qualified deterministic implementation |
| MRM_BTP9 | E15 | Tables 42/45/46 BTP9 | optimal | 430 | 430 | True | LP verified |
| MRM_BTP10 | E15 | Tables 42/45/46 BTP10 | NWCM | 93 | 93 | True | qualified deterministic implementation |
| MRM_BTP10 | E15 | Tables 42/45/46 BTP10 | LCM | 79 | 79 | True | qualified deterministic implementation |
| MRM_BTP10 | E15 | Tables 42/45/46 BTP10 | VAM | 68 | 68 | True | qualified deterministic implementation |
| MRM_BTP10 | E15 | Tables 42/45/46 BTP10 | MRM | 68 | 68 | True | qualified deterministic implementation |
| MRM_BTP10 | E15 | Tables 42/45/46 BTP10 | optimal | 68 | 68 | True | LP verified |
| MRM_UTP1 | E15 | Tables 42/45/46 UTP1 | NWCM | 18800 | 18800 | True | qualified deterministic implementation |
| MRM_UTP1 | E15 | Tables 42/45/46 UTP1 | LCM | 8800 | 8800 | True | qualified deterministic implementation |
| MRM_UTP1 | E15 | Tables 42/45/46 UTP1 | VAM | 8350 | 8350 | True | qualified deterministic implementation |
| MRM_UTP1 | E15 | Tables 42/45/46 UTP1 | MRM | 7750 | 7750 | True | qualified deterministic implementation |
| MRM_UTP1 | E15 | Tables 42/45/46 UTP1 | optimal | 7750 | 7750 | True | LP verified |
| MRM_UTP2 | E15 | Tables 42/45/46 UTP2 | NWCM | 14725 | 14725 | True | qualified deterministic implementation |
| MRM_UTP2 | E15 | Tables 42/45/46 UTP2 | LCM | 14625 | 14625 | True | qualified deterministic implementation |
| MRM_UTP2 | E15 | Tables 42/45/46 UTP2 | VAM | 13225 | 13225 | True | qualified deterministic implementation |
| MRM_UTP2 | E15 | Tables 42/45/46 UTP2 | MRM | 12475 | 12475 | True | qualified deterministic implementation |
| MRM_UTP2 | E15 | Tables 42/45/46 UTP2 | optimal | 12475 | 12475 | True | LP verified |
| MRM_UTP3 | E15 | Tables 42/45/46 UTP3 | NWCM | 13100 | 13100 | True | qualified deterministic implementation |
| MRM_UTP3 | E15 | Tables 42/45/46 UTP3 | LCM | 9800 | 9800 | True | qualified deterministic implementation |
| MRM_UTP3 | E15 | Tables 42/45/46 UTP3 | VAM | 9200 | 9200 | True | qualified deterministic implementation |
| MRM_UTP3 | E15 | Tables 42/45/46 UTP3 | MRM | 9200 | 9200 | True | qualified deterministic implementation |
| MRM_UTP3 | E15 | Tables 42/45/46 UTP3 | optimal | 9200 | 9200 | True | LP verified |
