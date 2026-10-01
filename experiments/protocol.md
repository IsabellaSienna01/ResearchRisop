# Experiment protocol

Fixed before examining modification results. Selection uses no LP optimum. Data
from papers and author supplements are exploratory, not a representative random
sample; repeated matrices after adding a zero dummy count once in summaries.

24 small variations are specified in modifications/variants.py: tie-only changes;
VAM penalty times A and sqrt(A); TDSM theta=1.5 (already published parameter
family); top-2 cost-product; top-2 lower-bound look-ahead; top-2/top-3 completion
rollout; one first-decision rollout; tie+rollout ablation; MRM orientation ensemble;
three fixed normalized cost/allocation weights. All results, including failures and
worsening, are retained. No post-hoc weight is substituted into the baseline.

For rollout, select the first k distinct cells in the baseline's ordered candidate
list, including its original choice. THP uses cheapest cells from the two highest
distinct range levels; VAM uses line penalty order. Force one maximal allocation,
complete the residual with the stated heuristic, and compare immediate+completion
cost. A residual LP is never used for selection. First-only returns the selected
completion; repeated rollout reevaluates after every committed allocation.

Random validation: NumPy Generator seed 20261001; sizes 3,4,5,6,10 square;
20 instances per size per distribution (uniform integer costs 1..99; many ties
1..9; skewed costs via clipped lognormal), 300 instances total. Supplies uniform
integers 5..100, positive demands from 1+multinomial(total-n, Dirichlet(ones(n))).
Same saved inputs for all methods. No training/tuning on these instances.

Feasibility, support acyclicity, symbolic-zero basis completion, LP primal/dual
residuals, and nonnegative optimality gaps are checked. Record single-run elapsed
wall time as descriptive Python implementation cost, not an asymptotic proof or
precision microbenchmark. Aggregate only successful cases while reporting failures;
paired improvement denominators include all evaluated instances. Any additional
experiment prompted by findings will be marked exploratory separately.
