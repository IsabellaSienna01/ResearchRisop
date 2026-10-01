# JHM follow-up protocol, 1 October 2026

Fixed before inspecting the new JHM variant results. IHW is excluded at the user's request.

The full 2015 decision tree remains inaccessible. Implement only the verified single-excess branch, explicitly named `JHM_single`, and do not mix its successful-subset mean with the complete 84/300-case rankings. Inputs with multiple excess rows after the same demand-first initialization are marked `unverified`, without fallback. A fixed lowest-index convention resolves equal initial/recipient minima; equal column penalties prefer the higher donor unit cost (Indrawan theorem 4.2), followed by index. Both balance directions follow the original publisher's description: demand excess gets a zero-cost dummy row initially; unused supply is sent to a zero-cost dummy column only after repair.

Baseline transfers min(cell allocation, donor excess), which can overload its recipient. Freeze exactly filled rows. Recompute choices after transfers. Audit feasibility and acyclic positive support. Match supplied L01 JHM=460 and L03 JHM=475; a matching cost is not proof of matching allocations or the complete algorithm.

Implementation audit: the identified donor remains selected until its excess is removed (the inner transfer loop in the source); multiple excess recipients trigger the unresolved row-selection gate only after that donor is finished. This is part of the source contract, not a new scoring variant. The first reproduction run revealed that the higher-donor-cost tie interpretation gives 473 on L03 rather than the published 475; retain this discrepancy. Do not alter the tie rule to force a match. A separate index-tie sensitivity audit will show whether ties can explain it.

Variants, fixed before measurement:

1. `cap_receiver`: also cap transfer by recipient deficit.
2. `net_tie`: only on equal penalties prefer the smaller actual incremental transfer cost q*delta.
3. `cap_net_tie`: combine 1 and 2 for ablation.
4. `top2_completion`: test two ranked transfers with complete baseline repair, choose the cheaper completed total, commit only the transfer and repeat. Include the baseline choice. No LP enters selection.

Use all saved 86 raw published/author inputs, aggregate on the existing 84 canonical IDs, and all 300 fixed random inputs. Record excluded inputs as well as successes, ties, negative results, allocations and traces for local worked cases. Reuse verified LP certificates and calculate standard gaps. Do not tune rules from outcomes or present this as a complete JHM reproduction. Capping is a known elementary feasibility rule and BCE/SSM already modify JHM transfers; rollout is established. Novelty is not claimed.
