# WRITER-A audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep, but rename because methylation marks are not uniformly activating and “writer” mixes mark, enzyme, and readout.

## What the current graph claims
- Node definition: Activating-associated histone methylation including H3K4me3 at promoters, H3K4me1 at enhancers, and H3K36me3 over elongating gene bodies.
- Incoming edges:
  - KEYS -> WRITER-A: TF→MLL / → H3K4me3 [context/dashed]
  - SCRIBE -> WRITER-A: SETD2 coupled / Ser2-P → H3K36me3 (C) [emphasized]
- Outgoing edges:
  - WRITER-A -> SCRIBE: H3K4me3 / → Pol II recruit
  - WRITER-A -> SPLICER: H3K36me3→MRG15 / →PTB→exon incl.(B) [emphasized]

## Literature-grounded assessment
- What is strongly supported: H3K4me3/H3K4me1 and H3K36me3 are robust chromatin-state features; SETD2-coupled H3K36me3 links elongation to splicing and DNA repair.
- What is context-dependent: H3K4me3 can mark bivalent/poised promoters; H3K36 methylation can suppress cryptic initiation as well as support co-transcriptional processing.
- What is weak, controversial, or assay-biased: Calling methylation “activating” can imply causality where many marks are consequences or stabilizers of transcription.
- What may be duplicate biology under another name: Overlaps with SCRIBE and SPLICER through H3K36me3.

## Missing or excessive graph structure
- Missing edges: Add WRITER-A -> SHUFFLER/OPENER reader recruitment only where supported; keep H3K36me3 -> SPLICER.
- Excess edges: WRITER-A -> SCRIBE “Pol II recruit” should be caveated: H3K4me3 is associated with PIC recruitment but not universally sufficient.
- Candidate splits: Consider splitting H3K4 methylation from H3K36 elongation methylation.
- Candidate merges: No merge.
- Candidate renames: ACTIVE-HISTONE-MARKS or HISTONE-METHYL-A.

## Recommendation
- Concrete graph change, if any: Revise text to “active-associated histone methylation” and caveat causality.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26383031 — broad review of histone modifications in active chromatin.
- PMID 25693172 — SETD2/H3K36me3 roles in transcription and RNA processing.
- PMID 20832724 — H3K36me3 links chromatin and alternative splicing.
- PMID 31278053 — review on H3K4 methylation and transcriptional regulation.
