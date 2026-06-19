# READERS audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but avoid implying all RBPs are only post-transcriptional cytoplasmic regulators; many are nuclear and co-transcriptional.

## What the current graph claims
- Node definition: RNA-binding proteins that bind RNA sequence/structure/modifications and regulate processing, stability, localization, and translation.
- Incoming edges:
  - TRIMMER -> READERS: 3'UTR length / → RBP sites
- Outgoing edges:
  - READERS -> SPLICER: SR/hnRNP / → splice (A) (drawn back/coupled) [context/dashed]
  - READERS -> TIMER: HuR (stabilize) / TTP (decay)
  - READERS -> FORGE: FMRP represses / initiation (inhibitory)

## Literature-grounded assessment
- What is strongly supported: Human cells encode hundreds to over a thousand RBPs with diverse RNA-binding domains; CLIP and perturbation studies show broad control of splicing, decay, localization, and translation.
- What is context-dependent: RBP binding is concentration-, compartment-, modification-, and RNA-structure-dependent; motifs are short and often not sufficient for regulation.
- What is weak, controversial, or assay-biased: CLIP peaks can be crosslinking/antibody-biased; binding does not guarantee functional effect.
- What may be duplicate biology under another name: Overlaps with SPLICER and STAMP readers; SR/hnRNPs appear in multiple nodes.

## Missing or excessive graph structure
- Missing edges: Add READERS -> TRIMMER and READERS -> VAULT; many RBPs control APA and granule partitioning.
- Excess edges: READERS -> FORGE as only FMRP repression is too narrow; RBPs can repress or activate translation.
- Candidate splits: No split, but notes could separate splicing RBPs, stability RBPs, translation RBPs.
- Candidate merges: No merge.
- Candidate renames: RBPs would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; broaden translation and APA effects and flag CLIP binding-function caveat.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 28951558 — census and functional diversity of human RBPs.
- PMID 31086105 — RBP regulation across RNA life cycle review.
- PMID 27899515 — CLIP methods and interpretation caveats.
- PMID 34953825 — RBP dysfunction and RNA regulation review.
