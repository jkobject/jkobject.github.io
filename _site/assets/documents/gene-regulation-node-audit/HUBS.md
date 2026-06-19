# HUBS audit

## Verdict
- Status: split
- Confidence: medium
- Short verdict: Biology is real but the node conflates an operational ChIP-seq class (“super-enhancer”) with a microscopy/biophysics claim (“condensate”). Keep the concept but split or strongly caveat.

## What the current graph claims
- Node definition: Super-enhancer clusters and/or coactivator/Pol II-enriched transcriptional condensate-like assemblies.
- Incoming edges:
  - BRIDGES -> HUBS: anchors
  - OPENER -> HUBS: H3K27ac / → BRD4 hubs [context/dashed]
  - KEYS -> HUBS: master TF clusters / → SE identity
- Outgoing edges:
  - HUBS -> OPENER: SEs maintain / enhancer acetylation [context/dashed]
  - HUBS -> SCRIBE: P-TEFb release / pause→elongation

## Literature-grounded assessment
- What is strongly supported: Dense enhancer clusters enriched for master TFs, Mediator, BRD4, H3K27ac, and Pol II often regulate cell-identity genes; transcriptional coactivators can form condensate-like assemblies in cells and in vitro.
- What is context-dependent: Super-enhancers are thresholded from ChIP-seq ranking and depend on stitching parameters; condensate material properties vary by assay and perturbation.
- What is weak, controversial, or assay-biased: LLPS language is prone to hype: 1,6-hexanediol, overexpression, and puncta colocalization are not sufficient proof of functional phase separation.
- What may be duplicate biology under another name: Overlaps with BRIDGES, OPENER, KEYS, SCRIBE and LLPS meta-principle.

## Missing or excessive graph structure
- Missing edges: Add KEYS -> HUBS and HUBS -> SCRIBE/OPENER caveats as already present, but note evidence is enhancer- and cell-type-specific.
- Excess edges: BRIDGES -> HUBS “anchors” is too general; not all enhancer loops make super-enhancers.
- Candidate splits: Split into SUPER-ENHANCERS and TRANSCRIPTIONAL CONDENSATES, or rename to ENHANCER HUBS with a condensate caveat.
- Candidate merges: No merge.
- Candidate renames: ENHANCER-HUBS would avoid equating SEs with LLPS.

## Recommendation
- Concrete graph change, if any: Split or revise text: super-enhancer is an annotation; condensate is a physical model requiring direct evidence.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 23582322 — original super-enhancer concept in control of cell identity.
- PMID 23582323 — enhancer cluster/super-enhancer discovery in ESCs.
- PMID 29930091 — transcriptional coactivator condensates, important but often overgeneralized.
- PMID 30449622 — TF/coactivator phase separation evidence; useful with assay caveats.
- PMID 36593347 — review/cautionary discussion of biomolecular condensates in transcription.
