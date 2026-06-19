# FENCES audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep, but phrase as insulation/contact-domain architecture rather than absolute fences. TAD boundaries can constrain enhancer action, yet expression effects after boundary loss are locus-specific.

## What the current graph claims
- Node definition: TAD boundaries and insulation, especially convergent CTCF/cohesin loop-extrusion barriers that reduce inappropriate enhancer-promoter communication.
- Incoming edges:
  - ZONES -> FENCES: constrains [context/dashed]
- Outgoing edges:
  - FENCES -> BRIDGES: delimits

## Literature-grounded assessment
- What is strongly supported: Cohesin extrusion stopped or slowed by oriented CTCF sites explains many loops and contact domains; boundary perturbations can cause enhancer adoption and disease phenotypes.
- What is context-dependent: TAD strength varies by cell type, cohesin residence, transcription, and chromatin state. Some genes tolerate boundary deletion with limited expression change.
- What is weak, controversial, or assay-biased: The node label risks overpromising hard insulation. Assays differ: population Hi-C domains, single-cell structures, and functional enhancer boundaries are related but not identical.
- What may be duplicate biology under another name: Partial overlap with BRIDGES because loops can be both structural and regulatory.

## Missing or excessive graph structure
- Missing edges: Add caveat from SHUFFLER/OPENER/KEYS or transcription to boundary permeability where chromatin state changes contact use.
- Excess edges: FENCES -> BRIDGES should be “biases/limits” rather than universally delimits.
- Candidate splits: No split, unless separating CTCF/cohesin loops from broader TAD/domain compartments.
- Candidate merges: No merge.
- Candidate renames: INSULATORS or DOMAINS would be more literal than FENCES.

## Recommendation
- Concrete graph change, if any: Keep with wording that boundaries are probabilistic insulators produced largely by cohesin/CTCF loop extrusion.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26499245 — CTCF/cohesin loop-domain map supporting convergent motif logic.
- PMID 27192037 — loop-extrusion model explaining TAD and loop formation.
- PMC10167645 — current work/review context on loop stacking and hierarchical folding.
- PMC11190842 — useful for caveating extrusion versus compartmental interactions.
