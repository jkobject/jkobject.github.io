# SHUFFLER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but note remodeler families have opposing effects depending on complex composition and recruitment.

## What the current graph claims
- Node definition: ATP-dependent chromatin remodeling complexes that reposition, evict, slide, or exchange nucleosomes.
- Incoming edges:
  - OPENER -> SHUFFLER: acetyl marks / recruit readers/remodelers [context/dashed]
  - KEYS -> SHUFFLER: TF→BAF/SWI-SNF / recruitment
- Outgoing edges:
  - SHUFFLER -> KEYS: nucleosome / remodeling

## Literature-grounded assessment
- What is strongly supported: SWI/SNF/BAF, ISWI, CHD, and INO80 families are central regulators of nucleosome positioning and access; mutations in BAF complexes strongly affect development and cancer.
- What is context-dependent: The same family can open, close, phase, or exchange nucleosomes depending on subunit composition and genomic context.
- What is weak, controversial, or assay-biased: “Open chromatin” framing can overgeneralize: remodelers also maintain nucleosome organization and repression.
- What may be duplicate biology under another name: Overlaps with OPENER and KEYS recruitment.

## Missing or excessive graph structure
- Missing edges: Add SHUFFLER -> SCRIBE or BRIDGES context? Remodelers affect promoter/enhancer accessibility and sometimes 3D contacts.
- Excess edges: None major.
- Candidate splits: No split at this map scale.
- Candidate merges: No merge.
- Candidate renames: REMODELER would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; wording should emphasize family-specific and bidirectional chromatin effects.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 30069008 — review of ATP-dependent chromatin remodelers.
- PMID 31597971 — BAF/SWI-SNF complexes in development and disease.
- PMID 34385722 — chromatin remodeler mechanisms and nucleosome organization review.
- PMID 26383031 — histone marks recruiting remodeler readers context.
