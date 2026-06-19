# ROUTER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The ubiquitin-code framing is valid if caveated: linkage type biases fate but readers, architecture, and substrate context decide output.

## What the current graph claims
- Node definition: Ubiquitin conjugation and chain topology directing proteins to proteasomal degradation, signaling, trafficking, or autophagy.
- Incoming edges:
  - SWITCH -> ROUTER: phospho-degron / → E3 ligase
  - TETHER -> ROUTER: STUbLs: / SUMO→Ub [context/dashed]
  - LICENSE -> ROUTER: NEDD8 licenses CRLs / → Ub routing [emphasized]
- Outgoing edges:
  - ROUTER -> DESTROY: K48→26S / K63→p62/LC3
  - ROUTER -> KEYS: K63/M1 Ub / → NF-κB signaling [context/dashed]
  - ROUTER -> MATURE: Ub-chaperone / proteostasis [context/dashed]

## Literature-grounded assessment
- What is strongly supported: E1/E2/E3 cascades attach ubiquitin; K48/K11 often support proteasomal degradation, K63/M1 often support signaling/scaffolding, and mixed/branched chains add complexity.
- What is context-dependent: Chain length, branching, substrate site, E3/DUB context, and reader proteins shape outcome.
- What is weak, controversial, or assay-biased: “K48 = proteasome, K63 = autophagy/signaling” is a useful shorthand but too deterministic.
- What may be duplicate biology under another name: Overlaps with LICENSE, TETHER/STUbL, DESTROY.

## Missing or excessive graph structure
- Missing edges: Add ROUTER -> INSPECTOR? RQC uses ubiquitination, but current INSPECTOR -> DESTROY covers output.
- Excess edges: ROUTER -> MATURE “Ub-chaperone proteostasis” is broad but acceptable as dashed.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: UBIQUITIN-CODE.

## Recommendation
- Concrete graph change, if any: Keep; add chain-complexity caveat.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 24142891 — ubiquitin code concept review.
- PMID 26304824 — ubiquitin chain linkage and cellular outcomes review.
- PMID 31624214 — branched/mixed ubiquitin chain complexity review.
- PMID 31273098 — DUBs/readers and ubiquitin signaling specificity.
