# GUIDES audit

## Verdict
- Status: revise connections
- Confidence: medium
- Short verdict: Keep but narrow. The piRNA->DNA methylation pathway is strong in germline/transposons; many lncRNA->PRC2 claims are context-specific and sometimes promiscuous binding artifacts.

## What the current graph claims
- Node definition: ncRNAs that recruit or scaffold chromatin modifiers, including piRNAs in germline transposon silencing and lncRNAs such as XIST/KCNQ1OT1/HOTAIR contexts.
- Incoming edges:
  - KEYS -> GUIDES: TF drives / piRNA/lncRNA loci [context/dashed]
- Outgoing edges:
  - GUIDES -> SILENCER: piRNA→DNMT3 / de novo 5mC

## Literature-grounded assessment
- What is strongly supported: piRNA/PIWI pathways guide transposon silencing and can direct DNA methylation in mammalian germline; XIST is a robust chromosome-scale lncRNA regulator.
- What is context-dependent: LncRNA localization, abundance, and allele/chromosome context determine whether recruitment is specific and functional.
- What is weak, controversial, or assay-biased: HOTAIR/PRC2-style recruitment has been overgeneralized; PRC2 binds many RNAs with broad affinity, so binding alone is weak evidence.
- What may be duplicate biology under another name: Overlaps with SPONGE as lncRNA biology but nuclear chromatin-targeting and cytoplasmic ceRNA functions differ.

## Missing or excessive graph structure
- Missing edges: Add GUIDES -> WRITER-R for XIST/Polycomb recruitment, not only GUIDES -> SILENCER.
- Excess edges: KEYS -> GUIDES is broad; only some ncRNA loci are TF-driven in relevant contexts.
- Candidate splits: Split piRNA-guided DNA methylation from lncRNA chromatin scaffolds if space permits.
- Candidate merges: Do not merge with SPONGE; instead distinguish nuclear vs cytoplasmic lncRNA functions.
- Candidate renames: CHROMATIN-ncRNA.

## Recommendation
- Concrete graph change, if any: Keep with stronger caveats on lncRNA specificity and add GUIDES -> WRITER-R.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMID 30224350 — piRNA pathway and transposon silencing review.
- PMID 33007240 — XIST mechanisms and chromosome-scale silencing review.
- PMID 24074881 — cautionary evidence that PRC2 broadly binds RNA.
- PMID 34214486 — lncRNA chromatin regulation review with specificity caveats.
