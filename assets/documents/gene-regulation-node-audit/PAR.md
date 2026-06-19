# PAR audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep. PAR at DNA damage is well supported; broad connection to proteolytic condensates/destruction should be narrowed.

## What the current graph claims
- Node definition: PARP-mediated ADP-ribosylation/PAR chains, especially at DNA damage, recruiting repair factors and organizing local assemblies.
- Incoming edges:
  - SWITCH -> PAR: DDR kinases / → PARP context [context/dashed]
- Outgoing edges:
  - PAR -> DESTROY: PARylation → / proteolytic condensates

## Literature-grounded assessment
- What is strongly supported: PARP1 rapidly detects DNA breaks and synthesizes PAR; PAR recruits repair, chromatin remodeling, and RNA-binding proteins and can nucleate transient repair assemblies.
- What is context-dependent: Mono-ADP-ribosylation and poly-ADP-ribosylation have distinct writers/readers/erasers; PARP trapping/inhibitor effects complicate interpretation.
- What is weak, controversial, or assay-biased: LLPS framing for PAR repair condensates is useful but can be overclaimed; direct material-property evidence matters.
- What may be duplicate biology under another name: Overlaps with TETHER and ROUTER in DNA damage turnover/signaling.

## Missing or excessive graph structure
- Missing edges: Add PAR -> SHUFFLER/OPENER/WRITER chromatin repair context if scope allows; PARP recruits chromatin remodelers.
- Excess edges: PAR -> DESTROY should be changed to PAR -> ROUTER/TETHER/repair-factor recruitment with a dashed degradation caveat.
- Candidate splits: No split at current scale.
- Candidate merges: No merge.
- Candidate renames: ADP-RIBOSE.

## Recommendation
- Concrete graph change, if any: Keep; narrow degradation edge and mention chromatin remodeling/DNA repair recruitment.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 29453264 — ADP-ribosylation/PARP DNA damage signaling review.
- PMID 33147445 — PARP biology and repair-factor recruitment review.
- PMID 31133750 — PAR-dependent phase separation in DNA damage response context.
- PMID 34349274 — PARP inhibitor/trapping biology and interpretation caveats.
