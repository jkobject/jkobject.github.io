# SHIELD audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. It is accurately placed as co-transcriptional protection and a bridge to export/translation.

## What the current graph claims
- Node definition: 5 prime m7G capping coupled to early Pol II elongation and recognized by nuclear CBC and cytoplasmic eIF4E/eIF4F.
- Incoming edges:
  - SCRIBE -> SHIELD: Ser5-P CTD / → capping co-tx
- Outgoing edges:
  - SHIELD -> FORGE: cap→eIF4E / binding

## Literature-grounded assessment
- What is strongly supported: Capping occurs very early during Pol II transcription and is recruited by Ser5-phosphorylated CTD; cap-binding proteins protect RNA, promote processing/export, and enable translation initiation.
- What is context-dependent: Cap quality and cap-binding factors vary across RNA classes; some RNAs use noncanonical caps or cap-independent translation.
- What is weak, controversial, or assay-biased: SHIELD -> FORGE should specify that mature mRNA cap/eIF4E binding is downstream of nuclear CBC exchange and export.
- What may be duplicate biology under another name: Overlaps with FORGE and TIMER because cap state controls initiation and decapping decay.

## Missing or excessive graph structure
- Missing edges: Add SHIELD -> TIMER inhibitory/protective edge: capping protects from 5 to 3 decay; decapping removes protection.
- Excess edges: None major.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: CAPPING would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; add cap protection versus decapping in notes.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 24813608 — review of mRNA capping enzymes and CTD coupling.
- PMID 32968261 — cap-binding complex and RNA fate review.
- PMID 30093596 — mRNA cap in translation and decay control.
- PMID 31332364 — CTD coordination of capping with transcription.
