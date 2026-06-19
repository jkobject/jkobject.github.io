# DESTROY audit

## Verdict
- Status: split
- Confidence: high
- Short verdict: Biology is strong, but the node fuses two major degradation systems with different substrates, machinery, kinetics, and regulation. Split if the map can tolerate another node.

## What the current graph claims
- Node definition: Protein clearance by the ubiquitin-proteasome system and selective autophagy/lysosomal routes.
- Incoming edges:
  - INSPECTOR -> DESTROY: RQC ubiquitinates / nascent chains
  - ROUTER -> DESTROY: K48→26S / K63→p62/LC3
  - PAR -> DESTROY: PARylation → / proteolytic condensates
  - MATURE -> DESTROY: misfolded cargo / triage [context/dashed]
- Outgoing edges:
  - DESTROY -> FORGE: lysosomal AA / → mTORC1 [context/dashed]
  - DESTROY -> KEYS: IκBα decay / → NF-κB activ. [context/dashed]

## Literature-grounded assessment
- What is strongly supported: The 26S proteasome degrades many short-lived or damaged ubiquitinated proteins; selective autophagy clears larger cargo, aggregates, organelles, and some ubiquitinated complexes via receptors such as p62/SQSTM1.
- What is context-dependent: Proteasome and autophagy compensate or cooperate under stress; K48/K63 shorthand is not absolute.
- What is weak, controversial, or assay-biased: Proteolytic condensate/LLPS claims are context-specific; not all degradation occurs in condensates.
- What may be duplicate biology under another name: Overlaps with ROUTER, LICENSE, MATURE, INSPECTOR.

## Missing or excessive graph structure
- Missing edges: Add DESTROY -> MATURE/proteostasis feedback or keep MATURE -> DESTROY; both are relevant.
- Excess edges: PAR -> DESTROY “PARylation -> proteolytic condensates” is too strong; better PAR -> ROUTER/repair turnover dashed.
- Candidate splits: Split PROTEASOME and SELECTIVE-AUTOPHAGY.
- Candidate merges: No merge.
- Candidate renames: CLEARANCE if kept fused.

## Recommendation
- Concrete graph change, if any: Prefer split; if kept, make label “protein clearance outputs: proteasome + selective autophagy.”
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 28104834 — ubiquitin-proteasome system review.
- PMID 28671639 — selective autophagy receptors and mechanisms review.
- PMID 31413922 — proteasome/autophagy crosstalk review.
- PMID 31948651 — condensate/LLPS caveats relevant to degradation assemblies.
