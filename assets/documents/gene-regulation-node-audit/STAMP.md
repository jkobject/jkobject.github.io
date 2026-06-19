# STAMP audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep, but revise reader-specific arrows. The older one-reader-one-output model is too clean; cytoplasmic YTHDF proteins show substantial redundancy and context-specific effects.

## What the current graph claims
- Node definition: m6A RNA modification written by METTL3/14 complexes, removed by FTO/ALKBH5 in some contexts, and read by YTH/YTHDC and other proteins.
- Incoming edges:
  - SCRIBE -> STAMP: CTD recruits METTL3/14 / (co-tx m6A, B)
- Outgoing edges:
  - STAMP -> SPLICER: YTHDC1→SRSF / (co-tx, B) (drawn back/coupled) [context/dashed]
  - STAMP -> TIMER: YTHDF2→CCR4-NOT / (decay)
  - STAMP -> FORGE: YTHDF1→eIF3 / (initiation ↑)
  - STAMP -> BYPASS: 5'UTR m6A / → cap-independent translation
  - STAMP -> CLIPS: m6A destab. / rG4 structure [context/dashed]

## Literature-grounded assessment
- What is strongly supported: m6A is abundant on mRNA and controls stability, translation, splicing/export, and stress responses through reader proteins; writer perturbations have strong phenotypes.
- What is context-dependent: m6A effects depend on site position, stoichiometry, cell state, reader expression, and assay. Eraser biology can include catalytic and noncatalytic effects.
- What is weak, controversial, or assay-biased: m6A mapping methods can have antibody bias/resolution limits; METTL3 overexpression or knockdown can cause indirect transcriptional effects.
- What may be duplicate biology under another name: Overlaps with READERS and TIMER because reader proteins mediate outcomes.

## Missing or excessive graph structure
- Missing edges: Add STAMP -> READERS as the direct interpretation step; then READERS -> TIMER/FORGE/BYPASS.
- Excess edges: STAMP -> FORGE as “YTHDF1 -> eIF3” and STAMP -> TIMER as “YTHDF2 -> CCR4-NOT” should be caveated/rephrased with YTHDF redundancy.
- Candidate splits: No split, but notes should separate nuclear YTHDC1 from cytoplasmic YTHDF functions.
- Candidate merges: Do not merge with READERS; m6A mark is distinct from protein readers.
- Candidate renames: m6A would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; change simple YTHDF1/2/3 arrows to context/redundancy-aware reader outputs.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 32492408 — unified/redundant YTHDF model for m6A-modified mRNA decay.
- PMID 38531646 — 2024 review specifically on redundant YTHDF functions.
- PMID 38677920 — evidence for distinct cellular YTHDF functions, useful counterbalance.
- PMID 37069041 — updated structural/function review of YTHDF readers.
- DOI 10.1016/j.molcel.2024.12.007 — 2024/2025 coding-region m6A decay pathway, current mechanism update.
