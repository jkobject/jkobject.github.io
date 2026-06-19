# RECODER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but note “recoding” is only a minority of ADAR biology; Alu/dsRNA editing and innate immune self-recognition are major functions.

## What the current graph claims
- Node definition: A-to-I RNA editing by ADAR enzymes, converting adenosine to inosine in dsRNA and affecting coding, splice, innate-immune, and RNA-fate outcomes.
- Incoming edges:
  - KEYS -> RECODER: IFN TFs / → ADAR1p150 [context/dashed]
- Outgoing edges:
  - RECODER -> SPLICER: A→I at 5'SS / → splice change (bidirectional) [emphasized]
  - RECODER -> CENSOR: Alu exon→PTC / → NMD (or prevents)

## Literature-grounded assessment
- What is strongly supported: ADAR1/2 edit dsRNA; neuronal coding recoding and widespread Alu editing are established. ADAR1 prevents inappropriate MDA5 sensing of endogenous dsRNA.
- What is context-dependent: Editing levels vary by tissue, interferon state, RNA structure, development, and disease; ADAR1 p150 and ADAR2 have distinct biology.
- What is weak, controversial, or assay-biased: The node name overemphasizes protein recoding and underemphasizes immune tolerance and RNA structure/splicing effects.
- What may be duplicate biology under another name: Overlaps with SPLICER, CENSOR, READERS.

## Missing or excessive graph structure
- Missing edges: Add RECODER -> innate immune/stress signaling if graph scope allows; within current graph, RECODER -> BRAKE/SWITCH via IFN/PKR would be plausible but broad.
- Excess edges: RECODER -> CENSOR should say editing can create or prevent NMD substrates; current label already partially does.
- Candidate splits: No split in map; optional ADAR recoding vs dsRNA-self marking.
- Candidate merges: No merge.
- Candidate renames: ADAR-EDIT would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; rename or revise definition to “ADAR A-to-I editing” rather than recoding alone.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 32810468 — ADAR editing biology and disease review.
- PMID 27653656 — ADAR1 prevents innate immune activation by endogenous dsRNA.
- PMID 32471237 — A-to-I editing in innate immunity and disease review.
- PMID 34216532 — ADAR-mediated editing and splicing/Alu transcriptome effects review.
