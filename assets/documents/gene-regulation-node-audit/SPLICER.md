# SPLICER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. This node is well supported and is correctly emphasized as kinetic/co-transcriptional coupling.

## What the current graph claims
- Node definition: Spliceosome-mediated intron removal and alternative exon choice, often coupled to Pol II kinetics and chromatin marks.
- Incoming edges:
  - SCRIBE -> SPLICER: Pol II rate / → exon inclusion / (kinetic coupling C) [emphasized]
  - WRITER-A -> SPLICER: H3K36me3→MRG15 / →PTB→exon incl.(B) [emphasized]
  - RECODER -> SPLICER: A→I at 5'SS / → splice change (bidirectional) [emphasized]
  - STAMP -> SPLICER: YTHDC1→SRSF / (co-tx, B) (drawn back/coupled) [context/dashed]
  - READERS -> SPLICER: SR/hnRNP / → splice (A) (drawn back/coupled) [context/dashed]
- Outgoing edges:
  - SPLICER -> CENSOR: PTC from / alternative exons

## Literature-grounded assessment
- What is strongly supported: Most human multi-exon genes undergo alternative splicing; SR/hnRNP regulators, spliceosome assembly, Pol II elongation rate, and chromatin marks influence exon choice.
- What is context-dependent: Splicing decisions are tissue-, developmental-, and signal-specific; many isoforms detected by RNA-seq have unclear protein-level consequence.
- What is weak, controversial, or assay-biased: Isoform catalogs overstate functional protein diversity if not supported by long-read, proteomic, or perturbation evidence.
- What may be duplicate biology under another name: Overlaps with READERS, WRITER-A, SCRIBE, CENSOR.

## Missing or excessive graph structure
- Missing edges: Add SPLICER -> TRIMMER coupling? Terminal exon choice often coordinates splicing and polyadenylation.
- Excess edges: None major.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: SPLICING would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; add isoform-function caution and optional splicing-APA edge.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 29134139 — alternative splicing regulation review.
- PMID 20832724 — chromatin H3K36me3 and splicing coupling evidence.
- PMID 26114644 — Pol II elongation kinetics and alternative splicing review.
- PMID 36640702 — modern review of co-transcriptional splicing.
