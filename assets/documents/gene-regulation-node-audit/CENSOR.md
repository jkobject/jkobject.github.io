# CENSOR audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The node is accurate but should avoid reducing NMD solely to the >50 nt EJC rule.

## What the current graph claims
- Node definition: Nonsense-mediated mRNA decay, especially UPF/SMG-dependent recognition of premature termination contexts and some normal regulatory transcripts.
- Incoming edges:
  - SPLICER -> CENSOR: PTC from / alternative exons
  - RECODER -> CENSOR: Alu exon→PTC / → NMD (or prevents)
- Outgoing edges:
  - CENSOR -> TIMER: triggers / degradation

## Literature-grounded assessment
- What is strongly supported: UPF1/2/3 and SMG factors drive surveillance of premature termination codons and regulate many endogenous transcripts; translation termination context is central.
- What is context-dependent: EJC-dependent >50-55 nt rule is useful in mammals but NMD can be EJC-independent and varies by gene, cell state, and stress.
- What is weak, controversial, or assay-biased: RNA-seq after NMD-factor depletion includes direct and indirect targets; NMD inhibition triggers stress and feedback effects.
- What may be duplicate biology under another name: Overlaps with TIMER and SPLICER.

## Missing or excessive graph structure
- Missing edges: Add CENSOR -> BRAKE/UPR stress caveat? NMD intersects ISR/UPR in some contexts but not needed at map scale.
- Excess edges: None major.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: NMD would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; broaden definition beyond the simple EJC distance rule.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 30190575 — NMD mechanisms and physiological regulation review.
- PMID 25218057 — NMD pathway and EJC-dependent/independent recognition review.
- PMID 35314867 — current review on NMD in quality control and gene regulation.
- PMID 27453686 — NMD factor perturbation and transcriptome interpretation context.
