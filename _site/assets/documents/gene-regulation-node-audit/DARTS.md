# DARTS audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The core pathway is strong; note that mammalian miRNA effects are usually modest per site and depend on target-site context.

## What the current graph claims
- Node definition: microRNA-loaded Argonaute/RISC complexes repressing target RNAs mostly through seed-paired 3UTR sites and TNRC6/CCR4-NOT-mediated deadenylation/decay.
- Incoming edges:
  - TRIMMER -> DARTS: 3'UTR length / → miRNA sites
  - SPONGE -> DARTS: ceRNA sponge / (A) (inhibitory)
- Outgoing edges:
  - DARTS -> TIMER: deadenylation / + decay
  - DARTS -> FORGE: blocks / initiation (inhibitory)

## Literature-grounded assessment
- What is strongly supported: Canonical miRNA biogenesis through Drosha/Dicer/AGO and seed-based targeting is well established; repression often proceeds through deadenylation and mRNA destabilization.
- What is context-dependent: Individual sites usually have small effects; cooperative site number, site accessibility, RBP competition, and cell-type expression control impact.
- What is weak, controversial, or assay-biased: Target prediction is noisy; many reported miRNA-target claims fail without AGO/perturbation and endogenous stoichiometry validation.
- What may be duplicate biology under another name: Overlaps with TIMER and SPONGE.

## Missing or excessive graph structure
- Missing edges: Add DARTS -> READERS or READERS -> DARTS competition/cooperation if detailed graph permits.
- Excess edges: DARTS -> FORGE “blocks initiation” should be secondary to deadenylation/decay for many mammalian targets; translational repression can precede decay.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: miRNA-RISC would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; wording should stress modest, context-dependent endogenous effects.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 22303290 — canonical miRNA pathway and targeting review.
- PMID 27824428 — miRNA repression via deadenylation/decay mechanisms.
- PMID 27720622 — target-site context and quantitative miRNA targeting.
- PMID 26685129 — AGO/miRNA target validation and functional caveats.
