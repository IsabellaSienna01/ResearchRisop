# Literature search log

Search date: 2026-10-01, Asia/Jakarta. Scope: crisp, single-commodity, linear cost transportation problems; IBFS construction distinguished from improvement to optimality. Local inventory was completed first. Searches used a general web index followed by publisher pages, full papers and author datasets; this is a documented research search, not a systematic database review or proof of novelty.

## Search families and outcomes

| Search terms | Outcome / follow-up |
|---|---|
| Transportation problem + IHW; IHW method; IHW heuristic; IHW transportasi; exclusions waste/hypothesis | No relevant defined TP heuristic located. Unrelated Independent Hypothesis Weighting and infectious healthcare waste excluded. Asked user for title/author/DOI; no invented expansion. |
| Transportation problem + MRM / maximum range method | Wireko et al. 2025 cost-minimization paper found; older 2020 time-minimization MRM and 2021 theses also found. Distinguish objective and orientation rule. |
| Transportation problem + CSM / Cost Supply Method | Bunyamin, Amaliah, Saikhu 2026, publisher ETASR, DOI 10.48084/etasr.16468. Full text pursued. |
| Total Differences Square Method / Total Differences Method + Hosseini | Hosseini 2017 primary PDF retrieved. TDM1/TDM2 and exponent-parameter ambiguity documented. |
| Juman Hoque 2015 algorithm / FLC SLC / exact paper title + PDF | 2015 Applied Soft Computing publisher record; 2014 conference abstract is insufficient for full algorithm. Full-text access sought separately. |
| Russell 1969 Extension Dantzig | Original INFORMS record, DOI 10.1287/opre.17.1.187. Classical algorithm cross-checked against comparative primary paper. |
| Classical heuristic algorithms comprehensive transportation study | Szwarc et al. 2019 LogForum primary comparative study (NWC, LCM, VAM, RAM); 7,500 generated instances. |
| An experimental study of newly proposed initial basic feasible solution methods | Mathirajan, Reddy, Rani 2022 OPSEARCH, DOI 10.1007/s12597-021-00533-5; 23 proposed/variant rules and 640 instances. Important anti-novelty/comparison source; full text sought. |
| Improved Vogel approximation + Korukoglu Balli | 2011 IVAM: total opportunity costs, top-three penalties, alternative allocation costs. Top-k alone already exists. |
| transportation problem look-ahead / lookahead / rollout / minimum cost look ahead | Many routing/scheduling hits are a different problem and excluded from TP-specific equivalence claims. General rollout is established; candidate completion must not be claimed as a new general principle. |
| Vogel allocation penalty weighted / dynamically-updated weighted opportunity cost | 2021 modified dynamically-updated weighted opportunity cost paper found. Allocation-aware/dynamic scores have substantial prior art. |

## Access and provenance

- Supplied papers L01–L05 remain primary for their contents.
- Public files fetched under `papers/external/` have adjacent `.source.json` files with request URL, final URL, retrieval timestamp and SHA-256. Access timestamps use host UTC; the report date uses the user's Asia/Jakarta date.
- Initial direct downloads were blocked by the sandbox; retried with explicit network approval. Publisher redirect pages are not assumed to be full papers.
- SSM's linked `netiquetting.blogspot.com` returned a page with only the title “Paper”, without benchmark matrices.
- RBSM's author page links a public Google Drive folder, rather than embedding the data. CSM's author page contains embedded content requiring separate extraction.
- No emails or requests were sent to authors. No paywall was bypassed. Search snippets alone do not establish an implementable algorithm.

Novelty labels used later: A existing published rule; B similar prior literature; C combination of existing ideas; D no close match found in the searched literature. D is not a novelty proof.

## JHM follow-up and synthesis, 2026-10-01

The user's instruction to **skip IHW** supersedes the earlier source-identification request. No additional IHW search or answer is pending.

| Follow-up search/access | Observed outcome |
|---|---|
| Exact Juman–Hoque title, 2015 DOI, author copies and Indonesian JHM applications | Original publisher preview found; complete 2015 decision tree not obtained |
| Indrawan / Affandi / Soesanto + JHM + theorem / tie / excess; EPSILON record variants | Publisher `/article/view/2876/0` verifies DOI **10.20527/epsilon.v15i1.2876**. Selected indexed pages discuss theorem 4.2–4.4, algorithm and allocation. Full PDF: expired TLS, then HTTP 403 even with narrowly scoped certificate exception and browser user agent |
| ULM Indrawan thesis public download | E21 obtained, but only one cover page; no algorithm or benchmark evidence |
| Juman-Hoque Sumathi-Sathiya + UNHAS + Rahayu | E22 public 24-page chapters 1–2 downloaded; six-step summary read. Full endpoint gives HTTP 401 even though displayed embargo date is past. No authentication bypass attempted |
| Juman & Nawarathne 2019 / Appendix A | Full E19 already downloaded; nine matrices and Table 8 claims transcribed and page image checked. Appendix B is mentioned but absent from obtained PDF |
| Re-reading supplied BCE real-application section while checking JHM comparisons | Complete 2x94 input found on p2306, independently transcribed and visually checked; inventory correction and separate supplemental experiment recorded |
| Transportation candidate completion / rollout; maximum-allocation least-cost tie; capacity-influenced IBFS | Original rollout paper, iLCM 2016 and CI-DI 2024 establish related principles; sources and exact overlap recorded in modification catalog |
| Recent VAM weighted spread / opportunity / capacity | Rashid & Mondal 2026 DSO-VAM, DOI **10.4236/ojop.2026.152003**, publisher HTML algorithm accessed. Added as scoring prior art, not as a reproduced competitor |

Full-access status was not inferred from a download filename. E21 cover-only, E22 partial chapters, E18 indexed fragments, and original JHM preview are labelled separately. The new implementation is deliberately restricted and does not claim that snippets establish all branches. Supplemental examples are separate from the frozen core suite, with exact duplicate mapping.

DSO-VAM provides an additional caution for weighted scoring: its printed decision index is maximized after subtracting an opportunity term. Holding the penalty fixed, increasing the subtracted term lowers priority; that direction must be reconciled with its stated rationale before a reproduction. This is our formula-level observation, not an experimental refutation. We did not implement it or import its superiority claims.

## Documentation and source check, 2026-10-02

At the user's request, the three shortlisted rules now have separate Markdown documents in `research/modifications/`, with algorithm steps matched to actual code, source/concept attribution, novelty limits, and runnable commands. This is a documentation/source verification follow-up, not a new full novelty search or a new benchmark selection.

Reopened the original Bertsekas–Tsitsiklis–Wu rollout PDF, checked the MRM publisher record, and checked primary MRCM/UNDIP pages. The MRCM publisher confirms DOI **10.26782/jmcms.2021.01.00006**; the downloaded publisher PDF displays a placeholder, which is not used as a DOI. The exact project policies remain classified as combinations/adaptations; no originality proof is inferred from writing our own Python code. All saved experimental results are unchanged.
