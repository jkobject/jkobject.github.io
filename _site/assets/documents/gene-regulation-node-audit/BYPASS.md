# BYPASS audit

## Verdict
- Status: major issue
- Confidence: medium
- Short verdict: Keep only with strong skepticism. Viral IRESs are robust; many cellular IRES claims require stricter validation because classic bicistronic assays are artifact-prone.

## What the current graph claims
- Node definition: Noncanonical initiation routes less dependent on 5 cap/scanning, especially viral IRESs and selected cellular IRES-like or m6A-dependent mechanisms.
- Incoming edges:
  - STAMP -> BYPASS: 5'UTR m6A / → cap-independent translation
  - CLIPS -> BYPASS: modulates / IRES activity
  - BRAKE -> BYPASS: cap-dep blocked / → IRES active
- Outgoing edges:
  - None shown in current DOT.

## Literature-grounded assessment
- What is strongly supported: Viral IRES mechanisms are structurally and biochemically well supported; some cellular RNAs and circRNAs can initiate via noncanonical elements under specific contexts.
- What is context-dependent: ITAF expression, RNA structure, stress condition, reporter design, and transcript processing determine apparent activity.
- What is weak, controversial, or assay-biased: DNA bicistronic reporters can be confounded by cryptic promoters, splicing, readthrough, RNA stability, or unequal RNA abundance. Cellular IRES claims need RNA transfection/circular reporter/monocistronic controls and endogenous evidence.
- What may be duplicate biology under another name: Overlaps with CLIPS, READERS, STAMP, BRAKE.

## Missing or excessive graph structure
- Missing edges: Add READERS -> BYPASS because ITAFs/RBPs are central.
- Excess edges: BRAKE -> BYPASS “cap-dep blocked -> IRES active” should be dashed and caveated; ATF4 belongs mainly to DECOY/uORF logic, not IRES.
- Candidate splits: Split VIRAL-IRES from CELLULAR-NONCANONICAL if space permits.
- Candidate merges: No merge.
- Candidate renames: NONCANONICAL-INIT.

## Recommendation
- Concrete graph change, if any: Revise as a skeptical, context-dependent node; remove implied general activation under stress.
- Concrete technical-notes/blog wording change, if any: Mirror the graph recommendation in the glossary and relation catalogue, and explicitly mark the confidence/caveat where the claim is context-dependent or assay-sensitive.

## Key sources
- PMC1370562 — classic methods paper explaining bicistronic assay artifacts and RNA transfection controls.
- PMC6884710 — review noting debate around cellular IRESs.
- PMC12048685 — 2025 toolbox for determining IRES activity with stronger controls.
- PMC12687423 — 2025 review of IRES elements and current significance.
