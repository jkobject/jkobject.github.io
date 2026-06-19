# VAULT audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep, but avoid treating granule localization as fate. Stress granules and P-bodies are related but distinct and not always liquid-like.

## What the current graph claims
- Node definition: Stress granules and P-bodies: dynamic cytoplasmic RNP assemblies linked to storage, repression, decay, and stress adaptation.
- Incoming edges:
  - TIMER -> VAULT: stored or / degraded (bidirectional)
- Outgoing edges:
  - None shown in current DOT.

## Literature-grounded assessment
- What is strongly supported: G3BP-dependent stress granules and decapping-enriched P-bodies dynamically exchange mRNPs; they reflect translational repression and RNA triage under stress.
- What is context-dependent: Granule composition and material state vary by stress, cell type, and time; many RNAs/proteins pass through without being degraded.
- What is weak, controversial, or assay-biased: LLPS claims can be overextended; puncta formation, 1,6-hexanediol sensitivity, or FRAP alone do not prove functional phase separation.
- What may be duplicate biology under another name: Overlaps with TIMER and READERS.

## Missing or excessive graph structure
- Missing edges: Add BRAKE -> VAULT because ISR/eIF2alpha phosphorylation triggers many stress-granule contexts.
- Excess edges: TIMER <-> VAULT should be caveated because P-bodies can store as well as decay and stress granules are not decay sites per se.
- Candidate splits: Optionally split stress granules and P-bodies if the figure has room.
- Candidate merges: No merge.
- Candidate renames: RNP-GRANULES.

## Recommendation
- Concrete graph change, if any: Keep; add ISR connection and LLPS assay caveat.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 30682370 — stress granule assembly/function review.
- PMID 28062596 — P-body and mRNA decay/storage review.
- PMID 31948651 — biomolecular condensate principles and caveats.
- PMID 33692599 — stress granule material properties and disease context.
