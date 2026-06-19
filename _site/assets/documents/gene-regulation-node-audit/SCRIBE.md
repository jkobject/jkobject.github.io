# SCRIBE audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. This is a central coupling node; retain emphasis on pausing and CTD-mediated RNA-processing coordination.

## What the current graph claims
- Node definition: RNA polymerase II initiation, promoter-proximal pausing, pause release, elongation, and CTD phosphorylation code.
- Incoming edges:
  - WRITER-A -> SCRIBE: H3K4me3 / → Pol II recruit
  - HUBS -> SCRIBE: P-TEFb release / pause→elongation
  - KEYS -> SCRIBE: TF→Mediator/PIC / → Pol II recruitment
  - SWITCH -> SCRIBE: P-TEFb/CDK9 / Ser2-CTD
- Outgoing edges:
  - SCRIBE -> ZONES: active txn / → comp. A [context/dashed]
  - SCRIBE -> SHIELD: Ser5-P CTD / → capping co-tx
  - SCRIBE -> SPLICER: Pol II rate / → exon inclusion / (kinetic coupling C) [emphasized]
  - SCRIBE -> TRIMMER: CTD → CstF / cleavage/polyA
  - SCRIBE -> STAMP: CTD recruits METTL3/14 / (co-tx m6A, B)
  - SCRIBE -> WRITER-A: SETD2 coupled / Ser2-P → H3K36me3 (C) [emphasized]

## Literature-grounded assessment
- What is strongly supported: Promoter-proximal pausing by NELF/DSIF and release by P-TEFb/CDK9 are well established; CTD phosphorylation coordinates capping, elongation, splicing, 3 end processing, and chromatin marks.
- What is context-dependent: Pausing is gene- and stimulus-specific; CTD marks are combinatorial and not a simple linear code.
- What is weak, controversial, or assay-biased: “CTD code” can be too deterministic; reader recruitment is dynamic and redundant.
- What may be duplicate biology under another name: Overlaps with SHIELD/SPLICER/TRIMMER/STAMP/WRITER-A via co-transcriptional coupling.

## Missing or excessive graph structure
- Missing edges: Add SCRIBE -> RECODER only indirectly? ADAR editing is often nuclear/co-transcriptional but more substrate/dsRNA-driven.
- Excess edges: SCRIBE -> STAMP as CTD recruits METTL3/14 is supported but should be caveated as not all m6A is strictly co-transcriptionally determined by CTD.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: POL-II would be clearer but SCRIBE is fine.

## Recommendation
- Concrete graph change, if any: Keep; caveat CTD-code determinism and pausing generality.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 24704787 — Pol II pausing control review.
- PMID 31332364 — CTD phosphorylation and co-transcriptional processing review.
- PMID 28985512 — transcription elongation coupling to chromatin/RNA processing.
- PMID 35090588 — modern review of promoter-proximal pausing and release.
