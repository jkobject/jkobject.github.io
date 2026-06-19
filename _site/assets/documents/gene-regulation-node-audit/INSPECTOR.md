# INSPECTOR audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The node is well placed, but distinguish mRNA surveillance from nascent-chain degradation.

## What the current graph claims
- Node definition: Translation surveillance including ribosome rescue, no-go decay, nonstop decay, and ribosome-associated quality control of stalled nascent chains.
- Incoming edges:
  - FORGE -> INSPECTOR: elongation stalls / → RQC/NGD
  - TEMPO -> INSPECTOR: codon/tRNA tempo / → ribosome stalls
- Outgoing edges:
  - INSPECTOR -> DESTROY: RQC ubiquitinates / nascent chains

## Literature-grounded assessment
- What is strongly supported: Stalled ribosomes are recognized and split; RQC factors such as LTN1, NEMF, VCP/p97 and ribosome rescue factors promote nascent-chain ubiquitination and clearance; NGD/NSD target defective mRNAs.
- What is context-dependent: Different stalls arise from damaged mRNA, polybasic tracts, rare codons, no stop codon, strong structures, or collided ribosomes.
- What is weak, controversial, or assay-biased: Ribo-seq stall signatures can be confounded by inhibitors, library biases, and RNA structure; causal RQC needs perturbation evidence.
- What may be duplicate biology under another name: Overlaps with TEMPO, TIMER, DESTROY, ROUTER.

## Missing or excessive graph structure
- Missing edges: Add INSPECTOR -> TIMER for NGD/NSD mRNA decay, not only INSPECTOR -> DESTROY.
- Excess edges: FORGE -> INSPECTOR should be replaced by defective elongation/stalling inputs.
- Candidate splits: No split for map scale, though RQC vs NGD/NSD are distinct.
- Candidate merges: No merge.
- Candidate renames: RQC-SURVEILLANCE.

## Recommendation
- Concrete graph change, if any: Keep; add mRNA decay output and revise initiation-stall edge.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 28132843 — ribosome-associated quality control review.
- PMID 31827284 — ribosome collisions as signal for quality control.
- PMID 34953884 — NGD/NSD/RQC surveillance review.
- PMID 33432186 — molecular mechanisms of RQC and nascent-chain ubiquitination.
