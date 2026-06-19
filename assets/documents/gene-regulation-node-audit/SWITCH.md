# SWITCH audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep, but consider separating phosphorylation from O-GlcNAc if precision matters; phosphorylation is vastly broader and mechanistically distinct.

## What the current graph claims
- Node definition: Post-translational switching by phosphorylation and O-GlcNAcylation affecting protein conformation, interactions, localization, degradation, and signaling.
- Incoming edges:
  - FORGE -> SWITCH: mTOR→AKT / → kinases [context/dashed]
- Outgoing edges:
  - SWITCH -> ROUTER: phospho-degron / → E3 ligase
  - SWITCH -> TETHER: phospho-dep. / SUMO recruit [context/dashed]
  - SWITCH -> SCRIBE: P-TEFb/CDK9 / Ser2-CTD
  - SWITCH -> BRAKE: eIF2α kinases / (PERK, GCN2)
  - SWITCH -> KEYS: TF phospho / activity/localization [context/dashed]
  - SWITCH -> PAR: DDR kinases / → PARP context [context/dashed]

## Literature-grounded assessment
- What is strongly supported: Kinase/phosphatase systems regulate TFs, Pol II, ISR kinases, mTOR, DNA damage, and degrons; O-GlcNAc is a nutrient-sensitive reversible Ser/Thr mark with crosstalk.
- What is context-dependent: Phosphorylation can activate, inhibit, localize, or create degrons depending on substrate and site; O-GlcNAc crosstalk is site- and pathway-specific.
- What is weak, controversial, or assay-biased: Combining two very broad PTMs can hide specificity; “switch” is a metaphor, not all phosphorylation is binary.
- What may be duplicate biology under another name: Overlaps with ROUTER, KEYS, SCRIBE, BRAKE.

## Missing or excessive graph structure
- Missing edges: Add SWITCH -> FORGE/mTOR more directly? Already FORGE -> SWITCH but feedback is complex.
- Excess edges: FORGE -> SWITCH “mTOR->AKT” direction is biologically awkward: AKT is upstream of mTORC1 in many pathways, while mTORC1 signals downstream to S6K/4E-BP.
- Candidate splits: Optional split PHOSPHO and O-GLCNAC.
- Candidate merges: No merge.
- Candidate renames: PTM-SWITCH.

## Recommendation
- Concrete graph change, if any: Keep; fix mTOR/AKT directionality and avoid binary switch wording.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 22078472 — phosphorylation signaling principles review.
- PMID 30213659 — phosphodegrons and ubiquitin crosstalk review.
- PMID 29522667 — O-GlcNAc signaling and phosphorylation crosstalk review.
- PMID 33230281 — mTOR signaling to translational control.
