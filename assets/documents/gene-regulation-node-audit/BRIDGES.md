# BRIDGES audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, with a note that physical proximity is neither always sufficient nor always strictly required for enhancer function at every time point.

## What the current graph claims
- Node definition: Enhancer-promoter contacts that increase the effective regulatory communication between distal enhancers and target promoters.
- Incoming edges:
  - FENCES -> BRIDGES: delimits
- Outgoing edges:
  - BRIDGES -> HUBS: anchors

## Literature-grounded assessment
- What is strongly supported: Enhancer-promoter contacts are repeatedly observed by 3C/Hi-C derivatives and perturbation studies; cohesin, Mediator, YY1, LDB1, and lineage TFs can contribute in specific systems.
- What is context-dependent: Contact frequency, enhancer transcription, promoter competence, and local chromatin environment determine output; some contacts pre-exist activation.
- What is weak, controversial, or assay-biased: Loop detection can be resolution- and normalization-dependent; population contacts hide cell-to-cell heterogeneity.
- What may be duplicate biology under another name: Overlaps with HUBS for clustered enhancers and with FENCES for structural loops.

## Missing or excessive graph structure
- Missing edges: Add explicit KEYS -> BRIDGES/BRIDGES -> SCRIBE connection: TF-bound enhancers contact promoters to recruit/stimulate Pol II.
- Excess edges: BRIDGES -> HUBS is too one-directional; super-enhancer clusters can contain many enhancer-promoter contacts but are not defined by a single bridge.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: E-P LOOPS would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; caveat contact-output relationships and avoid equating every loop with activation.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 30681780 — review on enhancer-promoter communication mechanisms and evidence.
- PMID 30242255 — enhancer-promoter specificity and 3D genome review context.
- DOI 10.1038/nature20158 — YY1 enhancer-promoter structural regulator example.
- PMID 26499245 — CTCF/cohesin loop architecture relevant to contact constraints.
