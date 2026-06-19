# MATURE audit

## Verdict
- Status: revise connections
- Confidence: high
- Short verdict: Keep, but separate cytosolic chaperone folding from ER UPR signaling in wording; both are proteostasis but different systems.

## What the current graph claims
- Node definition: Protein folding, refolding, triage, chaperone systems, and ER unfolded protein response.
- Incoming edges:
  - TEMPO -> MATURE: translation speed / → co-translational folding [context/dashed]
  - FORGE -> MATURE: co-translational / folding
  - ROUTER -> MATURE: Ub-chaperone / proteostasis [context/dashed]
- Outgoing edges:
  - MATURE -> BRAKE: UPR: PERK / = eIF2α kinase [context/dashed]
  - MATURE -> DESTROY: misfolded cargo / triage [context/dashed]

## Literature-grounded assessment
- What is strongly supported: Hsp70/Hsp90/CCT chaperones assist folding and triage; ER UPR sensors IRE1, PERK, and ATF6 tune translation, chaperones, ERAD, and apoptosis under ER stress.
- What is context-dependent: Chaperones can stabilize clients, promote degradation via CHIP, or aid assembly; UPR outcomes vary by duration and stress intensity.
- What is weak, controversial, or assay-biased: “Mature” can imply productive folding only; much of proteostasis is triage and degradation.
- What may be duplicate biology under another name: Overlaps with DESTROY, BRAKE/PERK, INSPECTOR.

## Missing or excessive graph structure
- Missing edges: Add MATURE -> ROUTER via CHIP/ERAD ubiquitination; current MATURE -> DESTROY is okay but less mechanistic.
- Excess edges: FORGE -> MATURE is correct but should say nascent-chain folding, not all mature protein folding.
- Candidate splits: Optional split CHAPERONES and UPR.
- Candidate merges: No merge.
- Candidate renames: PROTEOSTASIS.

## Recommendation
- Concrete graph change, if any: Keep but rename/reword toward proteostasis and add CHIP/ERAD routing.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 26961567 — proteostasis/chaperone network review.
- PMID 30089775 — Hsp70/Hsp90 folding and triage review.
- PMID 32555482 — unfolded protein response mechanisms review.
- PMID 22814339 — ERAD and ubiquitin-dependent protein quality control review.
