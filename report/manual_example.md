# Manual demonstration: THP with two-candidate completion

Source **A**: supplied L05, Example 1, [IEEE DOI](https://doi.org/10.1109/ICTS52701.2021.9608005). The modification and all calculations here are **C**. Indices in this explanation start at 1; JSON traces start at 0.

| Supply node | D1 | D2 | D3 | D4 | Supply |
|---|---|---|---|---|---|
| S1 | 6 | 3 | 1 | 4 | 50 |
| S2 | 7 | 6 | 2 | 1 | 55 |
| S3 | 10 | 4 | 5 | 9 | 75 |
| S4 | 7 | 7 | 7 | 3 | 60 |
| Demand | 90 | 65 | 30 | 55 | 240 |

The published/reproduced THP cost is **1045**. The LP optimum is **985**. This is a useful baseline gap of **6.0914%**, not a fabricated illustrative result.

1. Calculate original THP max-minus-min penalties. Row ranges are 5,6,6,4; column ranges 4,4,6,8. Keep the two distinct largest values, 8 and 6, including all tied lines. Their cheapest candidate cells are (1,3), (2,4), (3,2). Their immediate CA values are 30,55,260.
2. The modification takes the first two THP-ranked distinct cells: (1,3) and (2,4). Temporarily allocating either and completing with original THP costs 1045. Preserve baseline order on a tie, so commit x13=30. This is the same first move as THP.
3. Recalculate after D3 is exhausted. The leading two cells are now (2,4) and (3,2). Original THP compares immediate costs 55 and 260 and selects (2,4).
4. **Modified step:** complete the residual separately after each candidate. For x24=55, the immediate-plus-remaining cost is 1015; for x32=65 it is 955. Add the already committed cost 30: competing full costs are **1045 versus 985**. Therefore commit x32=65.
5. Repeat the same procedure. Remaining committed shipments lead to the following allocation.

| Allocation | D1 | D2 | D3 | D4 | Row sum |
|---|---|---|---|---|---|
| S1 | 20 | 0 | 30 | 0 | 50 |
| S2 | 0 | 0 | 0 | 55 | 55 |
| S3 | 10 | 65 | 0 | 0 | 75 |
| S4 | 60 | 0 | 0 | 0 | 60 |
| Column sum | 90 | 65 | 30 | 55 | 240 |

Z = 20*6 + 30*1 + 55*1 + 10*10 + 65*4 + 60*7 = **985**.

The solution has six positive cells although m+n-1=7. It is a **degenerate BFS**, not infeasible. One cycle-free representation adds x14=0 as a basic cell. This zero is not an epsilon shipment and changes no cost.

Original THP sends 20 from S1 to D2, 45 from S3 to D2 and 30 from S3 to D1. The modified solution sends those 20 S1 units to D1 and lets S3 supply 20 more units to D2, saving 20*((3+10)-(6+4))=60. This explanation connects the early priority mistake to the final cost consequence.

Standard metrics: baseline gap=60, gap%=100*60/985=6.0914%; modified gap=0; baseline accuracy=100*985/1045=94.2584%; modified accuracy=100%. Baseline-minus-modified improvement=60.

This example also supplies an ablation: evaluating alternatives **only at the first allocation** leaves THP at 1045. Repeating the evaluation reaches 985 because the useful alternative appears on the second decision. On L05 Examples 2 and 3, the modified method ties the already optimal THP costs 4525 and 2366. Those two ties are reported alongside the improvement.

For VAM on this same example the original first candidate is (4,4), while its second line candidate is (1,3). VAM completions cost 1095 and 985, so VAM's useful change occurs at the first decision. Do not conflate that mechanism with THP's later change.

Full machine-readable allocation and candidate scores are in [modification_allocations.json](../results/modification_allocations.json). Independent LP primal/dual certificates are in [optimal_certificates.json](../results/optimal_certificates.json).

## A small exact optimality certificate

The optimum can also be checked manually, without trusting a solver status. Take row potentials `u=[1,0,5,2]` and column potentials `v=[5,-1,0,1]`. For every cell, `u_i+v_j <= C_ij`; equality holds on all six positive shipments above. The dual value is

`u*s + v*d = (50+0+375+120) + (450-65+0+55) = 545+440 = 985`.

Every feasible transportation allocation therefore costs at least 985. The displayed feasible allocation costs exactly 985, so primal and dual values agree and prove optimality for this instance. The potentials are a certificate checked after the experiment, not information used by the modified heuristic to select its cells.
