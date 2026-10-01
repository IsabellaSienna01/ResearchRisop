# Terminology and algorithm contracts

Source class **A** means a supplied PDF, **B** external literature, and **C** this project's analysis or explicit implementation convention. A paper's use of the word "optimal" is not an optimality certificate. All identified named heuristics below generate a starting solution; LP/MODI/transportation simplex belong to a different stage.

| Acronym | Full name / resolved meaning | Main defining source | Year | Method type | Verified? |
|---|---|---|---|---|---|
| VAM | Vogel's Approximation Method | Reinfeld & Vogel, *Mathematical Programming*; algorithm also in supplied L05 | 1958 historical book; L05 2021 | IBFS | Rule verified; original book not accessed |
| IHW | Unresolved; skipped at the user's request on 2026-10-01 | No defining TP paper identified; supplied folder empty | Unknown | Unknown | Not investigated further; no invented expansion |
| SSM | Supply Selection Method | Amaliah, Fatichah, Suryani, L03; [DOI](https://doi.org/10.1016/j.eswa.2022.117399) | 2022 | IBFS through infeasible demand-first initialization and repair | Yes; residual ties require a convention |
| IBFS | Initial Basic Feasible Solution, a solution category | User's DOI is L01, defining BCE | Online 2020 / issue 2022 | Category, not another algorithm | Yes; counted once with BCE |
| MRM | Maximum Range Method, Wireko et al. cost version | E15; [DOI](https://doi.org/10.1016/j.rico.2025.100551) | 2025 | IBFS | Yes; narrative and pseudocode differ |
| CSM | Cost Supply Method / Cost-Supply Method | Bunyamin, Amaliah, Saikhu, E11; [DOI](https://doi.org/10.48084/etasr.16468) | 2026 | IBFS repair | Yes for this version; empty user folder cannot confirm intended version |
| RBSM | Rihan-Bilqis-Saikhu Method | Bunyamin, Amaliah, Saikhu, L02; [DOI](https://doi.org/10.1016/j.mex.2026.103825) | 2026 | IBFS repair | Yes; paper/code discrepancies documented |
| JHM | Juman & Hoque Method | Juman & Hoque; [publisher](https://www.sciencedirect.com/science/article/pii/S1568494615003099); Indrawan et al. 2021 | 2015 | IBFS repair | Restricted single-excess branch implemented and tested; full multi-excess decision tree unavailable |
| TDSM | User's "Total Differences Square Method"; Hosseini labels it TDSM | E01; [DOI](https://doi.org/10.12988/ams.2017.75178) | 2017 | IBFS | Formula verified; paper permits powers 1 < theta <= 2, not just squares; long expansion not explicitly confirmed in its heading |
| TDM | Total Differences Method; distinguish TDM1 and TDM2 | Hosseini E01 | 2017 | IBFS | Yes; row-only TDM1 differs from row-and-column TDM2 |
| BCE | Bilqis Chastine Erma method | Amaliah, Fatichah, Suryani, L01; [DOI](https://doi.org/10.1016/j.jksuci.2020.07.007) | Online 2020 / issue 2022 | IBFS repair | Yes; complete reproduction remains qualified |
| RAM | Russell's Approximation Method | Edward J. Russell; [DOI](https://doi.org/10.1287/opre.17.1.187) | 1969 | IBFS | Name/source verified; rule checked in external classical comparison |
| LCM | Least Cost Method; also matrix-minimum method in many texts | Classical rule; Szwarc et al. 2019 and Uddin et al. 2016 | Historical original attribution not established | IBFS | Rule verified; tie conventions vary |
| NWCM | North-West Corner Method (NWC/NWCR variants of the label) | Classical rule; Szwarc et al. 2019 | Historical original attribution not established | IBFS | Rule verified |

SSM also means **Stepping Stone Method** in Juman & Nawarathne's 2019 paper. That is an improvement method, different from the supplied 2022 SSM. MRM occurs in a 2020 time-minimization paper whose objective is the maximum time of a used route, and in a 2021 thesis combining row/column ranges. Neither is silently substituted for Wireko's 2025 cost version. TDM1/TDM2 must be named in comparisons. The supplied AIP method is variously labelled MS/MT/M.T.; it is not identified as MRM. THP is Two Highest Penalties, a separate modified-VAM baseline in supplied L05.

## Shared constructive contract

Inputs are a complete nonnegative cost matrix C, nonnegative supply s and demand d. Missing entries are not zero and prohibited routes are outside this implementation's scope. Balance with a zero-cost dummy source for demand excess, or dummy destination for supply excess. This models free shortage/slack; a real shortage penalty must replace zero when the application requires it.

For VAM, LCM, RAM, TDM1/2, TDSM and THP: remove initially zero residual lines, recalculate the specified priorities on active lines, select a cell, allocate q=min(s_i,d_j), subtract q, remove exhausted rows/columns, and repeat until all mass is allocated. If both exhaust, remove both for subsequent scoring. Degeneracy is represented afterward by **zero basic cells joining support components without a cycle**; no positive epsilon changes the solution. A feasible cyclic support is reported as nonbasic, not silently called an IBFS.

Each algorithm below incorporates this contract unless explicitly stated otherwise. Thus preprocessing, balancing, allocation, elimination and termination are fully specified once rather than repeated with possible inconsistencies. All final costs use original costs, including after any reduction/scoring transformation. The code returns allocation matrices and, for supplied examples, traces.

## Constructive selection rules

| Method | Row / column priority or penalty | Cell and tie rule | Determinism / domain |
|---|---|---|---|
| NWCM | No cost priority; original ordering | First active row and first active column | Deterministic for fixed ordering; both balance types |
| LCM | Global smallest active cost | Minimum C; our index completion is row-major; maximum-allocation tie is a separately tested known variant | Arbitrary ties in some sources; both after balancing |
| VAM | Each line: second-smallest minus smallest (multiplicity retained) | Largest penalty, then cheapest cell in that line; supplied paper allows arbitrary ties, completed by row-before-column then indices | Conditional on tie rule; both after balancing |
| LDVAM | Same VAM penalties | Equal penalties: smaller minimum cost; remaining ties by indices | Specific L05 description; both |
| RAM | u_i=max_j C_ij; v_j=max_i C_ij | Minimize Delta_ij=C_ij-u_i-v_j, recomputing maxima after elimination; ties by indices | Unspecified ties completed; both |
| TDM1 | Row alpha_i=sum_j(C_ij-min_k C_ik) | Maximum alpha row, then minimum cost cell | Row/cheapest-cell ties completed by indices; both |
| TDM2 | Same sum of differences for rows AND columns | Maximum line sum, then minimum cost cell | Ties as above; both |
| TDSM | Row alpha_i=sum_j(C_ij-min_k C_ik)^theta | Maximum alpha row, then minimum cost cell; theta=2 in baseline | Theta is a parameter; ties completed; both |
| THP | Each line: max cost minus min cost | Keep TWO DISTINCT highest levels, including every tied line; each contributes its cheapest cells. Minimize C_ij*min(s_i,d_j), then C_ij, then indices | Final arbitrary choices acknowledged by L05; both |

For a one-cell line the experimental penalty is zero; if only one row or column remains, conservation uniquely determines its positive shipments regardless of ordering. VAM candidate ordering for modifications lists line candidates in penalty order, removes repeated cells, and preserves the exact baseline candidate first. For THP, "two levels" can mean more than two lines; the experimental **top-2 cells** is a separate restriction after THP's published filtering, not a reinterpretation of the paper.

## MRM contract (E15 narrative, sections 3.1-3.2)

Compute ranges max-min. With no dummy, choose the largest range across both orientations at the first step; dummy source forces row ranges, dummy destination column ranges. **Freeze that orientation** thereafter. Break equal ranges by the smaller line minimum, then northwest index; select the line's cheapest cell. Allocate min(s,d). Remove the exhausted line; when both exhaust, remove only the selected orientation, retaining the zero residual line until a later choice. Finish all shipments and complete a symbolic-zero basis. The original narrative is implemented; its MATLAB listing does not consistently enforce the frozen orientation. Worked UTP3 chooses a different simultaneous-exhaustion removal, but the final reported cost is reproduced. Both balance types are supported.

## Demand-first family: SSM, CSM and RBSM

These algorithms initially satisfy every column by placing its entire demand in a cheapest row, even if row capacity is exceeded. This intermediate allocation is infeasible. Let t_i=sum_j X_ij and e_i=t_i-s_i. Rows with e>0 are excess, e<0 shortage, e=0 satisfied. Satisfied rows are excluded from subsequent transfers. Recompute row statuses after each move.

For every positive allocation X_ij in an excess row i, choose the least eligible shortage-row cost C_rj in that column. Score the proposed transfer by |C_rj-C_ij| and choose the smallest difference. Let the donor priority quantity be q_D=min(X_ij,e_i), and receiver priority quantity q_R=min(X_ij,-e_r). Priority means choosing one of these quantities, not min(X_ij,e_i,-e_r). A transfer can therefore change the receiver to excess or the donor to shortage. Move q from X_ij to X_rj and repeat until no excess remains. Balanced totals then imply row feasibility. Cycles or absence of a valid transfer are reported, never repaired with a hidden fallback.

| Decision | SSM, L03 | CSM, E11 narrative | RBSM, L02 narrative |
|---|---|---|---|
| Initial minimum-cost tie / receiver tie | Not fully prescribed; lowest index here | Higher TC_i=sum_j C_ij, then smallest index | Higher TC_i, then index completion |
| Equal difference | Larger X_ij, then index completion | Smaller q*C_rj, then smaller donor unit cost, then indices | Same gross destination-cost tie score; final unit-cost interpretation explicitly completed |
| Unequal original supplies | One excess row: satisfy smaller original supply. Multiple excess rows: satisfy larger original supply | Satisfy larger CS_i=s_i*TC_i | Satisfy larger CSS=C_ij*s_i versus C_rj*s_r |
| Equal original supplies | Donor if its excess fits X; else receiver if its shortage fits X; else transfer all X | Donor | Donor |
| Equal CS/CSS after unequal supplies | Not applicable | Receiver convention; equality not fully specified | Receiver under numbered step 8 |

Original supplies, not remaining residual quantities, enter these priority comparisons. CSM/RBSM compute TC once. SSM's title restricts attention to balanced TP, but step 1 instructs balancing; the implementation uses the shared zero-dummy model. CSM likewise illustrates that extension. Generalization beyond the experiments is not a guarantee of optimality or termination.

**CSM inconsistency:** Figure 3's prose-like comments mention cost increase, but its equal-difference branch compares maximum CS priority instead. This implementation follows the numbered narrative and worked allocation, labelled accordingly. It reproduces the worked N32 cost 1780.

**RBSM inconsistency:** supplied worked prose says satisfy the donor when 1*12=2*6, while its next table satisfies the receiver. The numbered equal-product branch and table are used. The author C++ has different tie accounting (donor-cost product, priority values retained from an earlier candidate, index-based equality) and lacks the paper's explicit equal-supply branch. Downloaded code is preserved for inspection and was not executed. No claim is made that a paper-narrative implementation is byte-for-byte the author's implementation.

## BCE / the IBFS DOI (L01)

Allocate all column demands to their first minima; mark excess and satisfied rows. For positive excess allocations find the next eligible least cost, using **signed** SLC-FLC. Select the smallest difference. If supplies differ and costs differ, check receiver status: an excess receiver triggers donor satisfaction; otherwise compute DS=|s_r-s_i| and DS mod (C_rj-C_ij). A nonzero remainder triggers donor satisfaction. A zero remainder compares original row sums TC_i and TC_r: TC_i>TC_r triggers donor satisfaction, otherwise receiver satisfaction. Equal supplies with different costs trigger donor satisfaction. Equal cell costs compare row sums; if donor total is larger satisfy donor, otherwise move the whole cell and advance the least/next-least assignment. Cross out a row when it is satisfied. Repeat its status/difference logic to termination.

The supplied unbalanced branch uses a separate total-allocation difference test, without a fully resolved modelling/receiver-selection contract in this audit. It is deliberately **not replaced by adding a dummy and pretending the balanced rule is the original**. The code's balanced interpretation recalculates eligible unsatisfied rows, permits an excess receiver as the paper does, and completes missing ties by indices. Its current least/next-least bookkeeping can cycle. These failures identify an unresolved implementation contract, not a proved defect of the entire published BCE method. Successful costs may be compared casewise; its success-only mean must not be ranked against complete algorithms.

The modulo combines quantity units and unit-cost units. Our scale test on the fully reproduced L01 worked example changes costs C to 10C: baseline 435 becomes 460 when expressed back in original units. This is a concrete unit-sensitivity observation under the documented implementation, and the worked initial modulo branch explains why it can happen.

## JHM: restricted verified branch, explicit multi-excess limit

The JHM publisher confirms column-first infeasible allocation followed by repair, column penalties only, an incorporated tie mechanism, and no dummy destination needed during supply-surplus construction. Demand excess is balanced with a zero-cost source. The original full section 5 remains inaccessible. Indrawan et al. 2021 is now bibliographically verified, [DOI 10.20527/epsilon.v15i1.2876](https://doi.org/10.20527/epsilon.v15i1.2876); selected indexed pages expose theorem 4.2 and multi-excess dependencies, but direct full retrieval still fails. A 2024 UNHAS thesis's public chapters 1–2 provide a six-step summary; its results chapter is inaccessible. The 2019 Juman-Nawarathne row-first algorithm is not substituted or silently transposed.

The separately named **JHM_single** contract is implemented in [jhm.py](../methods/jhm.py): allocate every demand to its column minimum; freeze exactly satisfied rows; require at most one excess donor when selecting a donor; choose the smallest signed next-eligible-cost minus donor-cost difference among its allocated cells; on equal differences prefer higher donor unit cost, then indices; transfer min(cell allocation, donor excess); finish that donor before selecting another. Receivers may become excess. Unknown multi-excess dependencies raise `UnverifiedJHMBranch`; no fallback is invented. Equal initial/recipient minima use a declared lowest-index convention. Supply-surplus slack is attached to a zero dummy destination after repair. All successful results undergo feasibility and acyclic-basis audits.

This interpretation reproduces local JHM 460 but yields 473 versus L03's printed 475; a separate index-tie diagnostic yields 475. Both results remain recorded. It covers 55/84 canonical inputs and 73/300 random inputs; successful-only means must not be ranked against full-suite algorithms. Four small variants, including receiver-cap and two-transfer completion, are tested within this restriction. Full algorithm, sources, limitations, negative results and manual example: [jhm_analysis.md](jhm_analysis.md).

## IHW: skipped by user instruction

IHW was unresolved after exact acronym/transportation/heuristic/Indonesian searches. On 2026-10-01 the user explicitly asked to skip it and continue with JHM. No source request is pending; no pseudocode, domain or modification formula is invented.

## Supplied AIP modification: extractable but not an accepted baseline

The described procedure balances, subtracts column minima then row minima, maps reduced zeros back to original cells, and processes rows from top to bottom. It allocates using zero cells, then remaining cheapest nonzero cells. The meaning of the "maximum zero" selection and ties is unclear. Its reduction tables contain arithmetic inconsistencies. The two complete matrices and worked allocations are preserved and LP-checked; no invented deterministic rule is labelled the paper's exact method.
