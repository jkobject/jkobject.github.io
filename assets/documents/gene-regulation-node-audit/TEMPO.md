# TEMPO audit

## Verdict
- Status: revise connections
- Confidence: medium
- Short verdict: Keep but narrow. Codon/tRNA effects and ribosome pausing are strong; broad “specialized ribosome code” claims remain unsettled.

## What the current graph claims
- Node definition: Translation elongation/decoding kinetics shaped by codon usage, tRNA abundance/modifications, mRNA structure, and possible ribosome heterogeneity.
- Incoming edges:
  - None shown in current DOT.
- Outgoing edges:
  - TEMPO -> INSPECTOR: codon/tRNA tempo / → ribosome stalls
  - TEMPO -> MATURE: translation speed / → co-translational folding [context/dashed]

## Literature-grounded assessment
- What is strongly supported: Codon optimality and tRNA supply affect elongation speed, mRNA stability, folding windows, and stress responses; tRNA/rRNA modifications can alter decoding and frameshifting.
- What is context-dependent: Effects are organism-, tissue-, growth-, and transcript-specific; pauses can be functional or pathological depending on position and quality-control thresholds.
- What is weak, controversial, or assay-biased: Specialized ribosome claims are difficult: altered ribosome composition can reflect biogenesis, stress, or degradation intermediates rather than programmed selectivity.
- What may be duplicate biology under another name: Overlaps with INSPECTOR and MATURE; codon optimality also overlaps with TIMER.

## Missing or excessive graph structure
- Missing edges: Add TEMPO -> TIMER for codon-optimality-dependent mRNA stability.
- Excess edges: TEMPO -> MATURE is plausible but should be dashed/contextual; many folding effects are protein-specific.
- Candidate splits: Separate CODON/T RNA TEMPO from SPECIALIZED RIBOSOMES in notes or figure.
- Candidate merges: No merge.
- Candidate renames: DECODING-TEMPO.

## Recommendation
- Concrete graph change, if any: Keep; downgrade ribosome heterogeneity language and add codon optimality -> mRNA stability.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26620904 — codon optimality controls mRNA stability through translation.
- PMID 29784749 — tRNA modifications and translation regulation review.
- PMID 37047306 — specialized ribosomes in health/disease review.
- PMC6467006 — skeptical review asking whether specialized ribosomes really exist.
- PMC11883428 — 2025 review on ribosome heterogeneity/specialization with current framing.
