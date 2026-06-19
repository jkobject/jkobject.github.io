# OPENER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but describe acetylation as a mark and reader-mediated accessibility/coactivation signal, not merely charge neutralization.

## What the current graph claims
- Node definition: Histone acetylation by HATs such as p300/CBP and removal by HDACs, with bromodomain readers linking acetyl marks to active chromatin.
- Incoming edges:
  - HUBS -> OPENER: SEs maintain / enhancer acetylation [context/dashed]
  - KEYS -> OPENER: TF→p300/CBP / → H3K27ac
- Outgoing edges:
  - OPENER -> SHUFFLER: acetyl marks / recruit readers/remodelers [context/dashed]
  - OPENER -> ZONES: H3K27ac / → comp. A [context/dashed]
  - OPENER -> HUBS: H3K27ac / → BRD4 hubs [context/dashed]
  - OPENER -> KEYS: open chromatin / → TF access

## Literature-grounded assessment
- What is strongly supported: H3K27ac and H3K9ac correlate with active promoters/enhancers; p300/CBP and bromodomain proteins recruit coactivation and remodeling machinery.
- What is context-dependent: Specific acetyl marks can have different readers and effects; HDAC inhibition produces broad indirect effects.
- What is weak, controversial, or assay-biased: Assuming H3K27ac alone defines an active enhancer can overcall poised or nonfunctional regions; ChIP signal is correlative without perturbation.
- What may be duplicate biology under another name: Overlaps with HUBS, SHUFFLER, KEYS.

## Missing or excessive graph structure
- Missing edges: Add HDAC/repressor connection to WRITER-R/SILENCER context if desired.
- Excess edges: OPENER -> ZONES is accurate as association but not a sufficient driver of compartment A.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: ACETYLATION would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; add reader-mediated and correlative caveats for H3K27ac.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26383031 — chromatin modifications and enhancer/promoter activity review.
- PMID 22955617 — p300/CBP and enhancer acetylation functional context.
- PMID 24461490 — BRD4/bromodomain link between acetylated chromatin and transcription.
- PMID 32632239 — enhancer mark interpretation and functional validation caveats.
