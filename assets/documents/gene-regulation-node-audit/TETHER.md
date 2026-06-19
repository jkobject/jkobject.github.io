# TETHER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The interaction-tethering metaphor is useful, but SUMO also changes activity, localization, stability, and stress responses.

## What the current graph claims
- Node definition: SUMOylation by SAE/UBC9/PIAS systems altering protein interactions, nuclear bodies, repression, DNA repair, and STUbL-mediated ubiquitination.
- Incoming edges:
  - SWITCH -> TETHER: phospho-dep. / SUMO recruit [context/dashed]
- Outgoing edges:
  - TETHER -> ROUTER: STUbLs: / SUMO→Ub [context/dashed]

## Literature-grounded assessment
- What is strongly supported: SUMO modifies many nuclear proteins and recruits SIM-containing partners; SUMO-targeted ubiquitin ligases connect SUMO to ubiquitin turnover.
- What is context-dependent: SUMO1 versus SUMO2/3 chains, stress induction, and substrate-site context matter; many SUMO effects are transient and substoichiometric.
- What is weak, controversial, or assay-biased: Proteomics can identify many SUMO sites with uncertain function; assigning repression to SUMO broadly is overgeneralized.
- What may be duplicate biology under another name: Overlaps with ROUTER and PAR/DNA repair.

## Missing or excessive graph structure
- Missing edges: Add TETHER -> PAR/DNA repair or TETHER -> KEYS? SUMO strongly affects transcription factors and repair foci but map may stay simple.
- Excess edges: TETHER -> ROUTER via STUbL is accurate but should be context-specific/dashed.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: SUMO.

## Recommendation
- Concrete graph change, if any: Keep; broaden beyond repression/tethering and caveat functional proteomics.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26542802 — SUMOylation mechanisms and cellular regulation review.
- PMID 29540635 — SUMO in DNA repair and nuclear organization review.
- PMID 25527682 — SUMO-targeted ubiquitin ligases connecting SUMO to ubiquitin.
- PMID 33128053 — SUMO proteomics and functional interpretation review.
