# FORGE audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. It is a central translation output node, but mTOR is only one upstream regulator of cap-dependent initiation.

## What the current graph claims
- Node definition: Cap-dependent translation initiation controlled by mTORC1/eIF4F/eIF4E/4E-BP and scanning to start codons.
- Incoming edges:
  - STAMP -> FORGE: YTHDF1→eIF3 / (initiation ↑)
  - READERS -> FORGE: FMRP represses / initiation (inhibitory)
  - CLIPS -> FORGE: 5'UTR rG4 / blocks scanning (inhibitory)
  - DARTS -> FORGE: blocks / initiation (inhibitory)
  - SHIELD -> FORGE: cap→eIF4E / binding
  - DECOY -> FORGE: regulate / initiation (inhibitory)
  - DESTROY -> FORGE: lysosomal AA / → mTORC1 [context/dashed]
- Outgoing edges:
  - FORGE -> INSPECTOR: elongation stalls / → RQC/NGD
  - FORGE -> MATURE: co-translational / folding
  - FORGE -> SWITCH: mTOR→AKT / → kinases [context/dashed]

## Literature-grounded assessment
- What is strongly supported: mTORC1 phosphorylation of 4E-BPs promotes eIF4E availability and eIF4F assembly; eIF4A/eIF4G/PABP and 43S scanning control initiation efficiency.
- What is context-dependent: mRNA-specific translation depends on 5UTR structure, uORFs, TOP motifs, RBPs, polyA, codon usage, and stress signaling.
- What is weak, controversial, or assay-biased: Equating mTOR activity with global translation can overgeneralize; rapamycin/ATP-site inhibitors have substrate- and timing-specific effects.
- What may be duplicate biology under another name: Overlaps with SHIELD, BRAKE, DECOY, BYPASS.

## Missing or excessive graph structure
- Missing edges: Add READERS -> FORGE bidirectional/activation and repression; add TIMER/codon optimality influence if detailed.
- Excess edges: FORGE -> INSPECTOR “elongation stalls” is not directly from initiation; better TEMPO/defective mRNA -> INSPECTOR.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: CAP-INITIATION.

## Recommendation
- Concrete graph change, if any: Keep; revise edge to INSPECTOR and broaden beyond mTOR only.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 25589112 — mTORC1 regulation of translation review.
- PMID 26383135 — eukaryotic translation initiation review.
- PMID 27810076 — 4E-BP/eIF4F and mTOR translational control.
- PMID 33230281 — mTOR and selective mRNA translation review.
