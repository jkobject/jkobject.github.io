# KEYS audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The node is broad but biologically necessary; caveat that TF binding is not equivalent to regulation.

## What the current graph claims
- Node definition: Sequence-specific transcription factors, including pioneer, lineage, stress, activator, and repressor TFs.
- Incoming edges:
  - OPENER -> KEYS: open chromatin / → TF access
  - WRITER-R -> KEYS: compact chromatin / → TF exclusion (inhibitory)
  - SHUFFLER -> KEYS: nucleosome / remodeling
  - SWITCH -> KEYS: TF phospho / activity/localization [context/dashed]
  - ROUTER -> KEYS: K63/M1 Ub / → NF-κB signaling [context/dashed]
  - DESTROY -> KEYS: IκBα decay / → NF-κB activ. [context/dashed]
- Outgoing edges:
  - KEYS -> OPENER: TF→p300/CBP / → H3K27ac
  - KEYS -> SHUFFLER: TF→BAF/SWI-SNF / recruitment
  - KEYS -> WRITER-A: TF→MLL / → H3K4me3 [context/dashed]
  - KEYS -> GUIDES: TF drives / piRNA/lncRNA loci [context/dashed]
  - KEYS -> SPONGE: TF drives / lncRNA txn [context/dashed]
  - KEYS -> SCRIBE: TF→Mediator/PIC / → Pol II recruitment
  - KEYS -> HUBS: master TF clusters / → SE identity
  - KEYS -> RECODER: IFN TFs / → ADAR1p150 [context/dashed]

## Literature-grounded assessment
- What is strongly supported: TFs recruit coactivators, corepressors, remodelers, Mediator, and Pol II; pioneer factors can engage nucleosomal or compact chromatin and seed regulatory programs.
- What is context-dependent: Motif occupancy depends on chromatin, cofactors, concentration, post-translational state, and 3D enhancer-promoter context.
- What is weak, controversial, or assay-biased: ChIP-seq peaks and motifs overpredict function; many binding events are low-effect, opportunistic, or indirect.
- What may be duplicate biology under another name: Overlaps with OPENER/SHUFFLER/HUBS because TFs recruit those mechanisms.

## Missing or excessive graph structure
- Missing edges: Add KEYS -> BRIDGES to indicate enhancer-bound TFs help establish promoter communication.
- Excess edges: KEYS -> GUIDES/SPONGE should be phrased as transcriptional control of ncRNA genes, not mechanism-specific targeting.
- Candidate splits: No split in main map; optional activators/repressors/pioneer factors in notes.
- Candidate merges: No merge.
- Candidate renames: TFs would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; add binding-vs-function caveat and KEYS -> BRIDGES.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 31827280 — TF binding, regulatory grammar, and gene-control review.
- PMID 24270712 — pioneer factor concept and chromatin opening.
- PMID 29126285 — enhancer logic and TF/cofactor recruitment review.
- PMID 31285669 — functional interpretation caveats for TF ChIP and enhancer assays.
