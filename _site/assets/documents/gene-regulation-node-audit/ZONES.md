# ZONES audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep the node, but present compartments as emergent 3D/chromatin states rather than a one-way upstream layer. The graph is good on A/B logic but should caveat that compartments, marks, transcription, and lamina contacts are mutually reinforcing and cell-state dependent.

## What the current graph claims
- Node definition: A/B chromatin compartments: large Hi-C domains where A generally tracks active, gene-rich euchromatin and B tracks inactive/lamina-associated heterochromatin.
- Incoming edges:
  - WRITER-R -> ZONES: H3K27me3/K9me3 / → comp. B [context/dashed]
  - SILENCER -> ZONES: 5mC / → comp. B [context/dashed]
  - OPENER -> ZONES: H3K27ac / → comp. A [context/dashed]
  - SCRIBE -> ZONES: active txn / → comp. A [context/dashed]
- Outgoing edges:
  - ZONES -> FENCES: constrains [context/dashed]
  - ZONES -> WRITER-R: B comp. ↔ / H3K27/9me3 [context/dashed]

## Literature-grounded assessment
- What is strongly supported: A/B compartments are robust Hi-C eigenvector features correlated with chromatin marks, lamina association, replication timing, and transcriptional state. Polymer and perturbation studies support an interplay between compartmental segregation and loop extrusion.
- What is context-dependent: Compartment identity can change during differentiation, senescence, cancer, and acute perturbation, but changes in compartment score do not always imply proportional expression changes.
- What is weak, controversial, or assay-biased: The edge ZONES -> FENCES is directionally too simple: cohesin-loop extrusion and compartment segregation can antagonize or coexist, and TADs are not simply formed inside compartments.
- What may be duplicate biology under another name: Overlaps conceptually with WRITER-R, OPENER, SILENCER, SCRIBE because those marks/activities define compartment identity.

## Missing or excessive graph structure
- Missing edges: Add reciprocal caveat edges between ZONES and OPENER/SILENCER/WRITER-R/SCRIBE as maintenance relationships, not strict causal arrows.
- Excess edges: ZONES -> FENCES should be caveated as spatial coexistence/constraint rather than direct formation.
- Candidate splits: No split.
- Candidate merges: No merge; do not merge with heterochromatin marks because Hi-C compartment is a 3D readout.
- Candidate renames: Consider COMPARTMENTS if code names are made more literal.

## Recommendation
- Concrete graph change, if any: Keep ZONES but rewrite as chromatin-compartment state shaped by transcription, epigenetic marks, lamina, and extrusion.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 19815776 — foundational Hi-C paper defining A/B compartments and linking them to open/closed chromatin.
- PMID 29348366 — review framing genome organization as integrated compartments, TADs, and loops.
- PMC11898215 — 2025 review of mechanistic drivers of compartments; useful current caution on phase separation, epigenetic state, and extrusion interplay.
- PMC11190842 — current review on attraction and disruption between loop extrusion and compartmentalization.
