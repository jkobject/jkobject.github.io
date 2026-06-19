# CLIPS audit

## Verdict
- Status: revise connections
- Confidence: medium
- Short verdict: Keep with caution. rG4 biology is real, but in-cell formation and functional prevalence are assay-sensitive and helicase-dependent.

## What the current graph claims
- Node definition: RNA G-quadruplex structures and related stable RNA structures that affect scanning, translation, stability, splicing, or localization.
- Incoming edges:
  - STAMP -> CLIPS: m6A destab. / rG4 structure [context/dashed]
- Outgoing edges:
  - CLIPS -> FORGE: 5'UTR rG4 / blocks scanning (inhibitory)
  - CLIPS -> BYPASS: modulates / IRES activity

## Literature-grounded assessment
- What is strongly supported: G-rich RNAs can form G-quadruplexes in vitro and in cells; DHX36/RHAU and other helicases bind/unwind rG4 and influence translation/localization.
- What is context-dependent: rG4 folding depends on ions, protein binding, transcript context, methylation, and competition with alternative structures.
- What is weak, controversial, or assay-biased: Chemical probing and antibody-based rG4 maps can disagree; stable in vitro structures may be unfolded in vivo.
- What may be duplicate biology under another name: Overlaps with BYPASS/FORGE and READERS because effects are mediated by helicases/RBPs.

## Missing or excessive graph structure
- Missing edges: Add READERS -> CLIPS for helicase/RBP remodeling of structures.
- Excess edges: STAMP -> CLIPS “m6A destabilizes rG4” is plausible for specific motifs but should be dashed and caveated.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: RNA-STRUCTURES or rG4.

## Recommendation
- Concrete graph change, if any: Keep but phrase as RNA structure module, with rG4 as prominent example.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 27417961 — transcriptome-wide rG4 mapping and regulatory potential.
- PMID 31896794 — rG4 biology and methods review.
- PMID 31296595 — DHX36/RHAU and RNA G-quadruplex regulation.
- PMID 35858636 — in-cell rG4 detection and assay caveats review.
