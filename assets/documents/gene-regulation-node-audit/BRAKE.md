# BRAKE audit

## Verdict
- Status: keep
- Confidence: high
- Short verdict: Keep. The graph correctly emphasizes global repression plus selective translation through uORF logic.

## What the current graph claims
- Node definition: Integrated stress response: eIF2alpha Ser51 phosphorylation by GCN2, PERK, PKR, or HRI reduces ternary complex and global initiation.
- Incoming edges:
  - MATURE -> BRAKE: UPR: PERK / = eIF2α kinase [context/dashed]
  - SWITCH -> BRAKE: eIF2α kinases / (PERK, GCN2)
- Outgoing edges:
  - BRAKE -> DECOY: eIF2α-P → TC↓ / uORF bypass → ATF4(C) [emphasized]
  - BRAKE -> BYPASS: cap-dep blocked / → IRES active

## Literature-grounded assessment
- What is strongly supported: ISR kinases phosphorylate eIF2alpha, limiting eIF2B-mediated ternary-complex recycling; ATF4/GCN4-like transcripts are selectively translated under low TC conditions.
- What is context-dependent: Different kinases sense distinct stresses; chronic ISR can be adaptive or pathological, and recovery via GADD34/PPP1R15A matters.
- What is weak, controversial, or assay-biased: Not all stress translation is ISR-dependent, and “cap-dependent blocked -> IRES active” can be too broad.
- What may be duplicate biology under another name: Overlaps with DECOY, BYPASS, MATURE/UPR, SWITCH phosphorylation.

## Missing or excessive graph structure
- Missing edges: Add BRAKE -> VAULT for stress granule formation in many eIF2alpha-P contexts.
- Excess edges: BRAKE -> BYPASS should be dashed/caveated; many proposed cellular IRES events are assay-sensitive.
- Candidate splits: No split.
- Candidate merges: No merge.
- Candidate renames: ISR would be clearer.

## Recommendation
- Concrete graph change, if any: Keep; add stress-granule connection and caveat IRES activation.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 28600166 — integrated stress response review.
- PMID 32132706 — eIF2B/eIF2alpha mechanistic ISR review.
- PMID 11532949 — ATF4 uORF stress-translation mechanism.
- PMID 33411209 — ISR in physiology and disease review.
