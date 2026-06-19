# SILENCER audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but avoid implying DNA methylation is uniformly repressive. Promoter CpG island methylation is strongly associated with silencing; gene-body and enhancer methylation have context-specific meanings.

## What the current graph claims
- Node definition: DNA methylation, especially CpG 5mC written by DNMTs, maintained across replication, and oxidized by TET enzymes.
- Incoming edges:
  - GUIDES -> SILENCER: piRNA→DNMT3 / de novo 5mC
- Outgoing edges:
  - SILENCER -> WRITER-R: co-recruit / co-occupy (bidirectional) [context/dashed]
  - SILENCER -> ZONES: 5mC / → comp. B [context/dashed]

## Literature-grounded assessment
- What is strongly supported: DNMT1/3A/3B and TET enzymes form a well-established methylation/demethylation system; promoter CpG methylation recruits methyl-CpG readers and repressive complexes.
- What is context-dependent: Gene-body methylation can correlate with active transcription and splicing; enhancer methylation can be dynamic; non-CpG methylation is important in neurons and pluripotent cells.
- What is weak, controversial, or assay-biased: Causality is locus-dependent: methylation can be consequence, maintenance mark, or driver depending on promoter class and chromatin state.
- What may be duplicate biology under another name: Overlaps with WRITER-R and ZONES for heterochromatin.

## Missing or excessive graph structure
- Missing edges: Add SILENCER -> KEYS inhibitory edge for methylated motif/promoter exclusion; add TET/active demethylation in notes.
- Excess edges: SILENCER -> ZONES should be reciprocal and context-dependent rather than simply 5mC -> B compartment.
- Candidate splits: No split for map scale, though 5mC maintenance vs de novo vs TET oxidation are distinct.
- Candidate merges: No merge.
- Candidate renames: DNA-METHYLATION would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; wording should distinguish promoter repression from gene-body/enhancer context.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 22353506 — classic review on DNA methylation and regulation.
- PMID 31673078 — modern review on mammalian DNA methylation dynamics.
- PMID 24705243 — TET-mediated oxidation and active demethylation review.
- PMID 27716473 — DNA methylation in gene bodies/regulatory regions cautions against simple silencing model.
