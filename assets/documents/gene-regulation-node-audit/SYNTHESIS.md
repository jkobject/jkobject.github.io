# Gene Regulation Landscape node-audit synthesis

Generated: 2026-06-18

## Coverage
All 37 node reports were written in this directory. Reports use the current DOT, technical notes, and blog post as graph claims and audit them against literature-level evidence and assay caveats.

## Nodes to keep as-is or with only wording caveats
BRIDGES, SILENCER, OPENER, WRITER-R, SHUFFLER, KEYS, SCRIBE, SHIELD, SPLICER, TRIMMER, RECODER, READERS, DARTS, CENSOR, TIMER, FORGE, BRAKE, DECOY, INSPECTOR, SWITCH, ROUTER, TETHER, LICENSE

## Nodes to rename or make more literal
Most code names can remain as mnemonic labels, but the technical notes should prefer literal names in definitions. Highest-value literal renames: FENCES -> INSULATORS/DOMAINS, WRITER-A -> ACTIVE-HISTONE-MARKS, WRITER-R -> REPRESSIVE-HISTONE-MARKS, SHUFFLER -> REMODELER, GUIDES -> CHROMATIN-ncRNA, SHIELD -> CAPPING, TRIMMER -> APA, STAMP -> m6A, READERS -> RBPs, FORGE -> CAP-INITIATION, BRAKE -> ISR, TEMPO -> DECODING-TEMPO, MATURE -> PROTEOSTASIS, PAR -> ADP-RIBOSE.

## Nodes to split
- HUBS: split super-enhancers from transcriptional condensates, or at minimum caveat that one is a ChIP-seq enhancer class and the other is a physical model.
- DESTROY: split proteasome and selective autophagy if graph space allows.
- Optional detailed-map splits: WRITER-A into H3K4-associated promoter/enhancer marks and H3K36 elongation marks; GUIDES into piRNA-guided DNA methylation and lncRNA chromatin scaffolds; BYPASS into viral IRES and cellular noncanonical initiation; MATURE into cytosolic chaperones and ER UPR.

## Nodes to merge
- Consider merging SPONGE into DARTS as a dashed/contextual “RNA competitors/ceRNA” submechanism unless the map intentionally wants a skeptical lncRNA node.
- LICENSE could be merged into ROUTER for a smaller map, but current separation is biologically defensible because neddylation specifically licenses CRL ubiquitin ligases.

## Major issue nodes
- SPONGE: ceRNA/sponging is heavily overclaimed without abundance, affinity, and localization evidence.
- BYPASS: viral IRESs are strong, but many cellular IRES claims are reporter-artifact-prone and need strict controls.

## Edges to add
- KEYS -> BRIDGES: enhancer-bound TFs help establish or stabilize enhancer-promoter communication.
- GUIDES -> WRITER-R: XIST and some nuclear lncRNA contexts recruit Polycomb/repressive histone systems.
- SHIELD -> TIMER: the cap protects from 5-prime decay; decapping commits many RNAs to turnover.
- SPLICER <-> TRIMMER: terminal exon choice and splicing are coupled to cleavage/polyadenylation.
- READERS -> TRIMMER and READERS -> VAULT: RBPs regulate APA and RNP-granule partitioning.
- BRAKE -> VAULT: eIF2alpha-P/ISR commonly promotes stress-granule assembly through translation repression.
- TEMPO -> TIMER: codon optimality and translation elongation affect mRNA stability.
- INSPECTOR -> TIMER: NGD/NSD produce mRNA decay outputs, not only nascent-chain destruction.
- MATURE -> ROUTER: CHIP/ERAD/chaperone triage connects proteostasis to ubiquitination.
- PAR -> SHUFFLER/repair-chromatin context: PARP/PAR recruits chromatin remodelers and repair assemblies.

## Edges to remove or caveat
- ZONES -> FENCES: change to coexistence/interplay; compartments do not simply create TADs.
- FENCES -> BRIDGES: change “delimits” to probabilistically constrains/biases.
- BRIDGES -> HUBS: caveat; super-enhancers are not simply anchored by individual loops.
- STAMP -> TIMER/FORGE/BYPASS: route through reader context and YTHDF redundancy rather than one-reader-one-output arrows.
- DARTS -> FORGE: caveat that mammalian miRNA repression often proceeds through deadenylation/decay, with translational repression context-dependent.
- TIMER <-> VAULT: granule localization is not proof of decay; storage and exchange are common.
- BRAKE -> BYPASS: mark as contextual; stress does not generally activate all IRES-like translation.
- FORGE -> INSPECTOR: initiation does not itself cause RQC; stalls/defective elongation do.
- FORGE -> SWITCH: fix mTOR/AKT directionality; AKT is often upstream of mTORC1, while mTORC1 signals through S6K/4E-BP.
- PAR -> DESTROY: narrow to PAR-dependent repair-factor recruitment, ubiquitin crosstalk, or local turnover; broad proteolytic-condensate output is too strong.


## Applied patch — 2026-06-21

The first post-audit patch was applied to the DOT, rendered image, public blog
post, and detailed technical notes.

Applied edge additions/caveats:
- Added `GUIDES -> WRITER-R` for XIST/nuclear-lncRNA Polycomb/repressive-mark contexts.
- Added `SHIELD -> TIMER` for cap protection and decapping-to-decay logic.
- Added `READERS -> TRIMMER` and `READERS -> VAULT` for RBP control of APA and RNP-granule partitioning.
- Added `TEMPO -> TIMER` for codon optimality / elongation effects on mRNA stability.
- Added `KEYS -> TEMPO` for MYC/growth-state regulation of tRNA/ribosome-biogenesis/translation-capacity programs.
- Added `FORGE -> TEMPO` and `BRAKE -> TEMPO` for initiation-load and stress-flux effects on ribosome density and elongation context.
- Added `INSPECTOR -> TIMER` for NGD/NSD mRNA decay outputs.
- Added `MATURE -> ROUTER` for CHIP/ERAD/chaperone-to-ubiquitin triage.
- Added `SWITCH -> LICENSE` for signaling control of CRL substrate receptors, assembly, and effective neddylation/deneddylation balance.
- Replaced broad `PAR -> DESTROY` with contextual `PAR -> ROUTER` repair/ubiquitin/local-turnover logic.
- Softened over-strong edges: `FENCES -> BRIDGES`, `BRIDGES -> HUBS`, `STAMP` outputs, `DARTS -> FORGE`, `TIMER <-> VAULT`, `BRAKE -> BYPASS`, `FORGE -> INSPECTOR`, and `FORGE -> SWITCH`.

Node-level decisions:
- `HUBS` was kept as one compact node but strongly caveated: super-enhancer is an enhancer-cluster/ChIP-seq annotation; transcriptional condensate is a physical model requiring direct evidence.
- `SPONGE` was kept as a skeptical/contextual node requiring abundance, affinity, localization, and loss-of-function stoichiometric support.
- `BYPASS` was kept as a skeptical/contextual noncanonical-initiation node: viral IRESs are robust, while many cellular IRES-like claims are reporter-artifact-prone.
- `DESTROY` was kept fused for layout compactness but explicitly described as two major outputs, proteasome and selective autophagy; split remains an option for a larger map.

## Literature-risk notes
- Condensates/LLPS: require direct material-property and functional evidence; puncta, overexpression, and 1,6-hexanediol sensitivity are weak alone.
- lncRNA mechanisms: distinguish localization and abundance; PRC2 binding or miRNA-site prediction alone is not mechanism.
- Reporter assays: cellular IRES, miRNA sponging, and enhancer claims are especially vulnerable to cryptic promoter/splicing/overexpression artifacts.
- Omics readouts: Hi-C, ChIP-seq, CLIP, Ribo-seq, m6A maps, and half-life assays are powerful but assay-biased; perturbation and endogenous validation should carry more weight.
- Context specificity: many mechanisms are strong in one lineage, stress, developmental stage, or locus but should not be generalized to a universal edge.

## Priority patch plan for DOT/details/blog
1. Patch the DOT relation labels first for caveated edges: ZONES->FENCES, FENCES->BRIDGES, BRIDGES->HUBS, STAMP outputs, BRAKE->BYPASS, FORGE->INSPECTOR, FORGE->SWITCH, PAR->DESTROY.
2. Add the highest-confidence missing edges: KEYS->BRIDGES, GUIDES->WRITER-R, SHIELD->TIMER, SPLICER<->TRIMMER, BRAKE->VAULT, TEMPO->TIMER, INSPECTOR->TIMER, MATURE->ROUTER.
3. Decide whether to split HUBS and DESTROY before editing layout, because those changes affect node count and rank width.
4. Revise the technical notes with skepticism boxes for LLPS, ceRNA, cellular IRES, specialized ribosomes, and m6A reader specificity.
5. Update the blog post after DOT/details are patched so the public narrative emphasizes that the map is a high-level control architecture with confidence/caveat annotations, not a claim that every arrow is universal.

## Completed node reports
ZONES, FENCES, BRIDGES, HUBS, SILENCER, OPENER, WRITER-A, WRITER-R, SHUFFLER, GUIDES, KEYS, SCRIBE, SHIELD, SPLICER, TRIMMER, RECODER, STAMP, READERS, DARTS, SPONGE, CENSOR, TIMER, CLIPS, VAULT, FORGE, BRAKE, DECOY, BYPASS, TEMPO, INSPECTOR, SWITCH, ROUTER, TETHER, LICENSE, DESTROY, MATURE, PAR
