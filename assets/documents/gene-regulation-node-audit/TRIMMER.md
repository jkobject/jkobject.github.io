# TRIMMER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The 3UTR-length logic is valid but should also include coding-region and promoter-proximal APA/termination effects.

## What the current graph claims
- Node definition: Alternative cleavage and polyadenylation choosing different 3 prime ends and often changing 3UTR regulatory site content.
- Incoming edges:
  - SCRIBE -> TRIMMER: CTD → CstF / cleavage/polyA
- Outgoing edges:
  - TRIMMER -> READERS: 3'UTR length / → RBP sites
  - TRIMMER -> DARTS: 3'UTR length / → miRNA sites

## Literature-grounded assessment
- What is strongly supported: Widespread APA changes transcript isoform abundance, 3UTR length, miRNA/RBP site exposure, localization, and sometimes protein C-termini.
- What is context-dependent: APA shifts vary with proliferation, differentiation, immune activation, and cancer; distal versus proximal site use does not always map simply to higher protein output.
- What is weak, controversial, or assay-biased: Shorter 3UTR does not automatically escape regulation if alternative sites add other elements or change localization/translation.
- What may be duplicate biology under another name: Overlaps with TIMER, READERS, DARTS, SCRIBE.

## Missing or excessive graph structure
- Missing edges: Add TRIMMER -> TIMER edge for polyA tail/3UTR-dependent stability; add SPLICER <-> TRIMMER coupling.
- Excess edges: TRIMMER -> DARTS/READERS is correct but should be “changes potential sites,” not guaranteed targeting.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: APA would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; expand from 3UTR shortening to broader 3 end processing/APA.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 25695964 — APA review linking 3UTR length and regulation.
- PMID 30463964 — global APA mechanisms and biological roles review.
- PMID 34794882 — APA in cell fate and disease review.
- PMID 31332364 — Pol II/CTD coupling to 3 end processing.
