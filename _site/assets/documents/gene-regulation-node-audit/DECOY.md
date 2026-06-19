# DECOY audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. uORF biology is strong and the ATF4/GCN4 examples are appropriate; phrase effects as often repressive but sometimes enabling conditional translation.

## What the current graph claims
- Node definition: Upstream open reading frames that intercept scanning ribosomes and tune main ORF translation, including stress-dependent reinitiation logic.
- Incoming edges:
  - BRAKE -> DECOY: eIF2α-P → TC↓ / uORF bypass → ATF4(C) [emphasized]
- Outgoing edges:
  - DECOY -> FORGE: regulate / initiation (inhibitory)

## Literature-grounded assessment
- What is strongly supported: uORFs are widespread and regulate translation initiation by ribosome diversion, reinitiation, leaky scanning, and start-codon context; ATF4/GCN4 mechanisms are canonical.
- What is context-dependent: Effect size depends on uORF length, start context, distance to main ORF, termination/reinitiation competence, and cell state.
- What is weak, controversial, or assay-biased: Ribosome profiling can overcall translated uORFs without careful harringtonine/lactimidomycin/ORF validation and conservation/proteomics support.
- What may be duplicate biology under another name: Overlaps with BRAKE and FORGE.

## Missing or excessive graph structure
- Missing edges: Add DECOY -> CENSOR/TIMER? uORFs and translation termination can affect NMD for some transcripts.
- Excess edges: DECOY -> FORGE inhibitory is mostly correct but should allow activating/conditional uORFs.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: uORF.

## Recommendation
- Concrete graph change, if any: Keep; wording should include activating/conditional uORFs, not only decoys.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 24440511 — uORFs as translational regulators review.
- PMID 11532949 — ATF4 uORF mechanism under eIF2alpha phosphorylation.
- PMID 33500560 — ribosome profiling and translated uORF annotation review/caveats.
- PMID 35858642 — uORFs in stress and disease review.
