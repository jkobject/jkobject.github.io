# WRITER-R audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, with explicit separation of Polycomb facultative repression from HP1/H3K9 constitutive heterochromatin.

## What the current graph claims
- Node definition: Repressive-associated histone methylation including Polycomb H3K27me3 and heterochromatic H3K9me3/H4K20me3.
- Incoming edges:
  - SILENCER -> WRITER-R: co-recruit / co-occupy (bidirectional) [context/dashed]
  - ZONES -> WRITER-R: B comp. ↔ / H3K27/9me3 [context/dashed]
- Outgoing edges:
  - WRITER-R -> ZONES: H3K27me3/K9me3 / → comp. B [context/dashed]
  - WRITER-R -> KEYS: compact chromatin / → TF exclusion (inhibitory)

## Literature-grounded assessment
- What is strongly supported: PRC2/EZH1/2 writes H3K27me3 and Polycomb systems maintain developmental repression; SUV39H/SETDB1-dependent H3K9me3 recruits HP1 and supports heterochromatin.
- What is context-dependent: H3K27me3 bivalency can coexist with H3K4me3; H3K9me3 effects depend on repeats, lamina, and cell type.
- What is weak, controversial, or assay-biased: Combining H3K27me3 and H3K9me3 is useful for a map but hides distinct readers, genomic targets, and dynamics.
- What may be duplicate biology under another name: Overlaps with SILENCER and ZONES.

## Missing or excessive graph structure
- Missing edges: Add WRITER-R -> SILENCER reciprocal logic already present; could add WRITER-R -> FENCES/ZONES via heterochromatin compaction as context.
- Excess edges: WRITER-R -> KEYS as compact chromatin exclusion is broadly true but should mention pioneer factors can bind some closed chromatin.
- Candidate splits: Optional split Polycomb vs H3K9/HP1 heterochromatin in a detailed version.
- Candidate merges: No merge.
- Candidate renames: REPRESSIVE-HISTONE-MARKS.

## Recommendation
- Concrete graph change, if any: Keep; notes should distinguish Polycomb and H3K9 systems and pioneer-factor exceptions.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 31819266 — review of Polycomb repression mechanisms.
- PMID 25467973 — H3K9 methylation/heterochromatin review context.
- PMID 29358053 — bivalent chromatin and developmental gene regulation.
- PMID 31673078 — DNA methylation and repressive chromatin crosstalk.
