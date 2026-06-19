# LICENSE audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The node is correctly narrow: neddylation licenses CRL activity rather than directly degrading substrates.

## What the current graph claims
- Node definition: NEDD8 conjugation, mainly to cullins, activating cullin-RING ligases and thereby enabling ubiquitin-mediated substrate routing.
- Incoming edges:
  - None shown in current DOT.
- Outgoing edges:
  - LICENSE -> ROUTER: NEDD8 licenses CRLs / → Ub routing [emphasized]

## Literature-grounded assessment
- What is strongly supported: Cullin neddylation changes CRL conformation and promotes ubiquitin transfer; deneddylation by COP9 signalosome resets CRLs; NAE inhibitors validate pathway importance.
- What is context-dependent: NEDD8 can modify non-cullin substrates in some contexts, but cullins dominate canonical biology.
- What is weak, controversial, or assay-biased: Treating neddylation as a general degradation route would be wrong; graph avoids this well.
- What may be duplicate biology under another name: Overlaps with ROUTER.

## Missing or excessive graph structure
- Missing edges: Add LICENSE <-> SWITCH? CRL activation can be phosphorylation-regulated, but not necessary.
- Excess edges: None major.
- Candidate splits: No split.
- Candidate merges: Could merge into ROUTER for a simpler map, but keeping it highlights CRL regulation.
- Candidate renames: NEDD8-CRL.

## Recommendation
- Concrete graph change, if any: Keep as narrow upstream switch for ROUTER.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 24466314 — neddylation and CRL regulation review.
- PMID 29686390 — structural/mechanistic review of CRL activation by NEDD8.
- PMID 33127844 — neddylation in cancer/therapeutic targeting review.
- PMID 32424077 — COP9 signalosome deneddylation and CRL cycling review.
