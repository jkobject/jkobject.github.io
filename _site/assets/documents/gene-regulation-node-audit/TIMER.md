# TIMER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. This is a core decay node; include that decay is coupled to translation, localization, and RNA modifications.

## What the current graph claims
- Node definition: mRNA stability and decay through deadenylation, decapping, XRN1/exosome degradation, and regulated half-life control.
- Incoming edges:
  - STAMP -> TIMER: YTHDF2→CCR4-NOT / (decay)
  - READERS -> TIMER: HuR (stabilize) / TTP (decay)
  - DARTS -> TIMER: deadenylation / + decay
  - CENSOR -> TIMER: triggers / degradation
- Outgoing edges:
  - TIMER -> VAULT: stored or / degraded (bidirectional)

## Literature-grounded assessment
- What is strongly supported: CCR4-NOT/PAN2-PAN3 deadenylation, DCP1/2 decapping, XRN1, and exosome pathways are central to mRNA turnover; decay strongly shapes expression output.
- What is context-dependent: Decay routes differ by transcript class, codon optimality, miRNA/RBP/m6A regulation, stress state, and subcellular location.
- What is weak, controversial, or assay-biased: Half-life measurements vary by metabolic labeling/drug shutoff method; transcription inhibition can perturb decay.
- What may be duplicate biology under another name: Overlaps with CENSOR, DARTS, STAMP, VAULT.

## Missing or excessive graph structure
- Missing edges: Add SHIELD -> TIMER protective relation and TEMPO/codon optimality -> TIMER in detailed map.
- Excess edges: TIMER -> VAULT “stored or degraded” is okay but P-body localization is not proof of decay.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: mRNA-DECAY would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; caveat measurement artifacts and P-body interpretation.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26183377 — eukaryotic mRNA decay pathways review.
- PMID 30659196 — CCR4-NOT/deadenylation and gene regulation review.
- PMID 26620904 — codon optimality links translation and mRNA stability.
- PMID 32968261 — cap-binding/decapping and RNA fate context.
