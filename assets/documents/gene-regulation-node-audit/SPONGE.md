# SPONGE audit

## Verdict
- Status: major issue
- Confidence: medium
- Short verdict: Keep only as a caveated, context-specific subcase of RNA competition. ceRNA/sponging is a frequent overclaim.

## What the current graph claims
- Node definition: Cytoplasmic lncRNAs/circRNAs or other RNAs acting as competing endogenous RNAs that titrate miRNAs under favorable stoichiometry/localization.
- Incoming edges:
  - KEYS -> SPONGE: TF drives / lncRNA txn [context/dashed]
- Outgoing edges:
  - SPONGE -> DARTS: ceRNA sponge / (A) (inhibitory)

## Literature-grounded assessment
- What is strongly supported: Specific high-abundance RNAs such as CDR1as can bind many miR-7 sites, and artificial sponges work experimentally.
- What is context-dependent: Endogenous competition requires high abundance, shared compartment, accessible high-affinity sites, and limiting miRNA/RISC; many lncRNAs are too low-abundance.
- What is weak, controversial, or assay-biased: ceRNA literature is inflated by correlation, target-prediction, and overexpression artifacts; loss-of-function stoichiometry is often missing.
- What may be duplicate biology under another name: Overlaps with GUIDES because both are lncRNA labels, but mechanisms differ; overlaps with DARTS/TIMER as miRNA pathway modulation.

## Missing or excessive graph structure
- Missing edges: Add SPONGE -> TIMER downstream relief only through DARTS; keep as inhibitory to DARTS but dashed/contextual.
- Excess edges: KEYS -> SPONGE is too broad unless simply “TF drives lncRNA transcription.”
- Candidate splits: Split cytoplasmic lncRNA translation/decoy/scaffold functions from ceRNA if keeping broad lncRNA node.
- Candidate merges: Merge SPONGE into DARTS as “RNA competitors” unless the graph wants a skeptical lncRNA-warning node.
- Candidate renames: ceRNA-SPONGE or RNA-COMPETITORS.

## Recommendation
- Concrete graph change, if any: Mark as highly context-dependent; require stoichiometry evidence in notes.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 22000013 — original ceRNA hypothesis framing.
- PMID 25488563 — quantitative/stoichiometric limits on ceRNA regulation.
- PMID 26072116 — ceRNA crosstalk review with caveats.
- PMID 35361991 — lncRNA mechanisms and abundance/localization constraints.
