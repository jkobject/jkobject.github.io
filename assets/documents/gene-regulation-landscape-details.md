# Gene Regulation Landscape — detailed construction notes
### From DNA to proteins — reductionist architecture (v7)

*Clawd · 2026-05-01 / updated 2026-06-18 · 37 mechanisms · 2 meta-principles · 7 layers*

These notes are the technical companion to the current Gene Regulation
Landscape v7 graph. They document the 37 mechanism boxes, 2 meta-principles, 73
mechanism relations, and 7 meta-style annotations used in the rendered figure.
The rendered figure was generated from the Graphviz source file
[`gene-reg-v7.dot`](/assets/documents/gene-reg-v7.dot).

---

## Executive Summary

Cells regulate gene expression across **7 nested levels**, from three-dimensional
genome organization to selective protein clearance. The graph contains 37
distinct mechanism boxes plus 2 cross-cutting meta-principles, **LLPS** and
**DECAY**, shown as border styles on the mechanisms they affect. Across the
map, most mechanisms reduce to three recurring strategies: (A) controlling
physical accessibility, (B) writing and reading reversible marks, and (C)
kinetic coupling between processes.

## How To Read These Notes

- The **37 mechanisms** are the boxes in the graph, grouped into 7 layers.
- **LLPS** and **DECAY** are not ordinary mechanism boxes; they are
  meta-principles indicated by border styles on relevant boxes.
- The **73 mechanism edges** describe causal, coupling, or feedback relations
  between mechanism boxes.
- The **7 meta annotations** connect LLPS and DECAY to the mechanisms that
  instantiate them.

## Graph Notation And Abbreviations

| Term | Meaning |
|------|---------|
| `tx` | Transcription. The graph avoids using it for translation to prevent ambiguity. |
| `co-tx` | Co-transcriptional: coupled to Pol II progression or nascent RNA. |
| `A` | Accessibility principle: making a substrate available or unavailable. |
| `B` | Mark/reader principle: a reversible mark has effects depending on its reader and context. |
| `C` | Kinetic-coupling principle: the speed of one process changes the outcome of another. |
| `⊣` | Repression, inhibition, or direct blocking. |
| `(back)` | Feedback or relation back to an upstream layer. |
| `(bidirectional)` | Reciprocal relation represented as two-way coupling. |
| `(**)` | Especially important kinetic coupling linked to principle C. |
| `initiation ↑` | Increased translation initiation. |
| `RQC` | Ribosome-associated quality control; surveillance of stalled ribosomes and nascent-peptide degradation. |
| `NGD` | No-go decay; decay triggered by a ribosome stalled on an mRNA. |
| `NSD` | Non-stop decay; decay triggered by an mRNA without a functional stop codon. |
| `SUMO` | Small ubiquitin-like modifier; a small protein conjugated to substrates as a post-translational mark. |
| `NEDDylation` | NEDD8 conjugation, especially on cullins to activate CRL E3 ligases. |
| bold | In the image, the top text in each box is the mechanism code name and maps 1-to-1 to the glossary. |
| italics | In the image and descriptions, italics are used for gene/protein names when helpful; graph boxes remain mechanism names. |

## Glossary Of Non-Gene Concepts

| Term | Meaning |
|------|---------|
| A/B compartments | Chromatin domains seen by Hi-C; A is usually active/euchromatic, B inactive/heterochromatic. |
| TAD | Topologically associating domain; a chromatin neighborhood insulated by boundaries such as CTCF/cohesin. |
| Enhancer-promoter loop | 3D contact bringing a distal enhancer close to a target promoter. |
| Super-enhancer | Dense enhancer cluster enriched in master TFs, Mediator, BRD4, and Pol II. |
| Condensate / LLPS | Liquid-liquid phase separation that concentrates molecules into a dense non-membrane phase. |
| DNA methylation | Addition of methyl groups to DNA, often linked to promoter repression. |
| Histone mark | Chemical histone modification, such as acetylation or methylation, read by chromatin proteins. |
| Chromatin remodeling | ATP-dependent repositioning, eviction, or exchange of nucleosomes. |
| ncRNA | Functional non-coding RNA not translated into protein. |
| Pol II pausing | Promoter-proximal RNA polymerase II pause before productive elongation. |
| CTD phosphorylation | Phosphorylation of the Pol II CTD tail, coordinating transcription and RNA processing. |
| 5' capping | Addition of an m7G cap to nascent RNA, required for protection, export, and translation. |
| Alternative splicing | Regulated exon choice producing multiple isoforms from one gene. |
| Alternative polyadenylation | Use of different cleavage/polyA sites, often changing 3'UTR length. |
| A-to-I editing | Adenosine-to-inosine RNA editing; inosine is often read as guanosine. |
| m6A | N6-methyladenosine, a reversible RNA modification interpreted by reader proteins. |
| RBP | RNA-binding protein. |
| miRNA-RISC | MicroRNA loaded into RISC to repress or destabilize target mRNAs. |
| ceRNA | Competing endogenous RNA; an RNA that can buffer miRNAs through shared target sites when abundance, affinity, and colocalization are sufficient. |
| NMD | Nonsense-mediated decay; surveillance and degradation of transcripts with premature stop codons. |
| Deadenylation / decapping | Removal of the polyA tail and 5' cap, usually committing an mRNA to decay. |
| RNA G-quadruplex | Guanine-rich RNA structure that can block scanning or alter RNA fate. |
| Stress granule / P-body | Cytoplasmic RNA-protein condensates involved in RNA storage, repression, or decay. |
| Cap-dependent translation | Canonical initiation through cap recognition followed by 5'UTR scanning. |
| ISR / eIF2α-P | Integrated stress response; eIF2α phosphorylation lowers global initiation but favors selected mRNAs. |
| uORF | Upstream open reading frame in a 5'UTR that can divert scanning ribosomes. |
| IRES / ITAF | Internal ribosome entry site and helper factors. Viral IRESs are strong examples; many cellular IRES claims need context-specific validation. |
| RQC / NGD / NSD | Ribosome quality control, no-go decay, and non-stop decay; surveillance of abnormal translation. |
| O-GlcNAc | Reversible sugar modification on Ser/Thr residues that can crosstalk with phosphorylation. |
| Ubiquitin chain | Ubiquitin polymer whose linkage type, such as K48 or K63, helps determine protein fate. |
| SUMOylation | SUMO conjugation, often involved in nuclear interactions and complex assembly. |
| Neddylation | NEDD8 conjugation, mostly on cullins, activating CRL E3 ligases. |
| Proteasome | Proteolytic complex that degrades many short-lived or damaged ubiquitinated proteins. |
| Selective autophagy | Lysosomal clearance of specific cargoes: aggregates, organelles, or ubiquitinated complexes. |
| UPR | Unfolded protein response; ER-stress response. |
| PAR / ADP-ribosylation | Poly-ADP-ribose signaling, often around DNA damage and condensate formation. |

## Reductionist Architecture — Three Core Strategies

```text
Strategy A — ACCESSIBILITY CONTROL
  "Make a substrate accessible or inaccessible to its machinery"
  Examples: OPENER/SHUFFLER -> TF access
            FENCES/BRIDGES -> enhancer-promoter proximity
            DARTS/SPONGE -> mRNA availability
            VAULT -> translational access

Strategy B — REVERSIBLE MARK + CONTEXTUAL READING
  "The same mark has different effects depending on its reader and context"
  Examples: SILENCER/WRITER-A/WRITER-R (histone code + DNA methylation)
            STAMP (m6A -> YTHDF1 or YTHDF2 depending on context)
            ROUTER (K48 -> proteasome; K63 -> signaling/autophagy)
            SWITCH (phosphorylation -> activation or degradation depending on substrate)

Strategy C — KINETIC COUPLING
  "The speed of process A determines the output of process B"
  Examples: Pol II rate -> SPLICER
            H3K36me3 deposited by SCRIBE -> SPLICER
            limiting ternary complex (BRAKE) -> DECOY bypass -> selective ATF4 FORGE
            codon pausing (TEMPO) -> co-translational MATURE
```

## Graph Box Map

| Layer | Mechanisms |
|-------|------------|
| 0 — 3D genome | ZONES, FENCES, BRIDGES, HUBS |
| 1 — Epigenetics | SILENCER, OPENER, WRITER-A, WRITER-R, SHUFFLER, GUIDES |
| 2 — Transcription | KEYS, SCRIBE |
| 3 — Co-transcriptional | SHIELD, SPLICER, TRIMMER, RECODER |
| 4 — Post-transcriptional | STAMP, READERS, DARTS, SPONGE, CENSOR, TIMER, CLIPS, VAULT |
| 5 — Translational | FORGE, BRAKE, DECOY, BYPASS, TEMPO, INSPECTOR |
| 6 — Post-translational | SWITCH, ROUTER, TETHER, LICENSE, DESTROY, MATURE, PAR |
| Meta | LLPS, DECAY |

## I. The 7 Layers — Explanations And Mechanisms

### Layer 0 — 3D Genome
*The genome is not linear but three-dimensional. Spatial organization determines which enhancers can communicate with which promoters.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **ZONES** | A/B compartments | Large chromatin regions (~5-20 Mb) detected by Hi-C. **A** compartments are transcriptionally active euchromatin (H3K27ac, H3K4me3). **B** compartments are inactive heterochromatin (H3K27me3, H3K9me3, DNA methylation, nuclear lamina). A↔B transitions accompany cell differentiation. |
| **FENCES** | TADs (Topologically Associating Domains) | Preferential interaction domains of ~0.1-2 Mb, often delimited by convergent CTCF boundaries. Dominant mechanism: cohesin extrudes loops until blocked by convergent CTCF pairs, producing partial inter-domain insulation. Boundaries strongly reduce aberrant enhancer-promoter contacts but do not always abolish them; expression effects depend on locus and cell type. |
| **BRIDGES** | Enhancer-promoter loops | Specific physical contacts between a distal enhancer and its target promoter, often but not exclusively within the same TAD. Mediated or stabilized, depending on context, by Mediator, cohesin, YY1, ZNF143, LDB1, and other factors. Can span over 1 Mb of linear distance. |
| **HUBS** | Super-enhancers / Pol II condensates | Clusters of ordinary enhancers spanning 5-50 kb and densely loaded with master TFs, BRD4, Mediator, and Pol II. They can form or feed coactivator-enriched transcriptional condensates, but "super-enhancer" as a ChIP-seq definition and "condensate" as a dynamic physical object are not strictly synonymous. Often drive cell-identity genes and some oncogenes. |

### Layer 1 — Epigenetics
*Heritable or semi-stable chromatin changes that alter accessibility without changing DNA sequence.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **SILENCER** | DNA methylation | Addition of a methyl group to cytosine (5mC) at CpG dinucleotides. **Writers**: DNMT1 for replication maintenance, DNMT3A/3B for *de novo* methylation. **Erasers**: TET1/2/3 oxidize 5mC to 5hmC/5fC/5caC followed by BER. **Readers**: MBD proteins recruit HDACs and repress transcription. General effect: repression at promoter CpG islands; gene-body methylation can stabilize Pol II elongation. |
| **OPENER** | Histone acetylation | Acetyl groups added to histone lysines (H3K27ac, H3K9ac, H4K16ac). **Writers**: p300/CBP, GCN5, PCAF, MOF. **Erasers**: HDACs. **Readers**: bromodomains such as BRD4 and BRG1. Acetylation neutralizes Lys positive charge, weakens histone-DNA attraction, opens nucleosomes, and permits TF/Pol II access. H3K27ac marks active enhancers. |
| **WRITER-A** | Activating histone methylation | H3K4me3 at active promoters, H3K4me1 at enhancers, H3K36me3 in elongating gene bodies, H3K79me2 at telomeres/elongation. **Writers**: MLL1-4/KMT2A-D and SET1A/B for H3K4; SETD2 for H3K36me3 coupled to Pol II Ser2-P. **Readers**: PHD fingers for H3K4me3 and PWWP domains for H3K36me3. H3K36me3 recruits splicing regulators, linking chromatin state to exon choice. |
| **WRITER-R** | Repressive histone methylation | H3K27me3 for facultative Polycomb repression, H3K9me3 for constitutive heterochromatin, and H4K20me3 in heterochromatin. **Writers**: EZH1/2 in PRC2 for H3K27me3; SUV39H1/2 and SETDB1 for H3K9me3. **Readers**: CBX/PRC1 and HP1/CBX1/3/5. H3K27me3 and H3K27ac compete on the same residue, forming an activation/repression switch. |
| **SHUFFLER** | ATP-dependent chromatin remodeling | Complexes that use ATP to reposition, evict, or replace nucleosomes. Families include **SWI/SNF** (BAF/PBAF), **ISWI**, **CHD**, and **INO80**. They are recruited by TFs and by histone marks through reader modules. |
| **GUIDES** | Epigenetic ncRNAs | Small and long non-coding RNAs that guide chromatin-modifying complexes to target loci. **piRNAs** guide transposon silencing by *de novo* DNA methylation in the germline. **lncRNA scaffolds** such as XIST, HOTAIR, and KCNQ1OT1 recruit PRC2 or related complexes to regional chromatin targets. |

### Layer 2 — Transcription
*Control of RNA polymerase II initiation and progression.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **KEYS** | Transcription factors (TFs) | Sequence-specific DNA-binding proteins with activation or repression domains. **Activators** recruit HATs, KMTs, CRCs, Mediator, and Pol II. **Repressors** recruit HDACs, PRC, or NuRD. **Pioneer factors** such as FOXA1, OCT4, and GATA3 can open compact chromatin. Master TFs such as OCT4, SOX2, and MYC define super-enhancers. Some stress-dependent or non-canonically translated proteins, such as ATF4 via uORF/reinitiation and proposed HIF-1α or c-MYC IRES-like routes, are themselves TFs. |
| **SCRIBE** | Pol II + pausing | RNA polymerase II is a ~550 kDa, 12-subunit enzyme. Its CTD tail (YSPTSPS repeats) is a signaling hub: **Ser5-P** marks initiation/capping, **Ser2-P** elongation, and **Ser7-P** non-coding RNA programs. Promoter-proximal pausing stalls Pol II 25-50 bp after the TSS through NELF and DSIF. P-TEFb release enables productive elongation. SETD2 and METTL3/14 are recruited through Pol II, coupling elongation to H3K36me3 and m6A deposition. |

### Layer 3 — Co-Transcriptional Processing
*Nascent RNA processing coupled to Pol II progression.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **SHIELD** | 5' capping | Addition of an m7G cap to the 5' end of nascent RNA at ~25-30 nt, coupled to Ser5-P CTD. The cap protects against 5'→3' exonucleases and is recognized by eIF4E for translation and CBC for nuclear export. |
| **SPLICER** | Alternative splicing | Intron excision and exon joining by the spliceosome (U1/U2/U4/U6/U5 snRNPs plus many proteins). Most multi-exon human genes produce multiple isoforms. Regulation occurs through exon skipping, intron retention, alternative splice sites, and mutually exclusive exons. Pol II elongation speed creates a kinetic window for weak exon recognition, and histone marks such as H3K36me3 recruit splicing regulators. |
| **TRIMMER** | Alternative polyadenylation (APA) | Many mammalian genes have multiple cleavage/polyadenylation sites, producing isoforms with different 3'UTR lengths. CPA factors recognize the AAUAAA signal upstream of the polyA site. Long 3'UTRs expose additional miRNA and RBP sites, increasing post-transcriptional regulation. |
| **RECODER** | A-to-I editing (ADAR) | ADAR enzymes deaminate adenosine to inosine in dsRNA. Inosine is read as guanosine, recoding RNA information. ADAR1 p150 is interferon-induced and marks endogenous Alu dsRNAs as self; ADAR2 specializes in nuclear neuronal recoding. A-to-I editing near splice sites can prevent Alu exonization and downstream NMD. |

### Layer 4 — Post-Transcriptional Control
*Regulation of mature mRNAs in the nucleus and cytoplasm.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **STAMP** | m6A epitranscriptome | **N6-methyladenosine (m6A)** is an abundant mRNA modification enriched near stop codons, long exons, and some 5'UTRs. **Writers**: METTL3/14/WTAP. **Erasers**: FTO, ALKBH5. **Readers**: YTHDF1/2/3 and YTHDC1. The classic model links YTHDF1 to translation, YTHDF2 to decay, YTHDF3 to output coordination, and YTHDC1 to splicing/export, but recent work also emphasizes partial redundancy among cytoplasmic YTHDF proteins. |
| **READERS** | Regulatory RBPs | Roughly 1500 human RNA-binding proteins use RRM, KH, CCCH zinc finger, PAZ, DEAD-box, and other modules. They regulate splicing, stability, translation, localization, and IRES activity. Examples include SRSF proteins, hnRNPs, HuR/ELAVL1, TTP/ZFP36, FMRP, Staufen1, PTB, DAP5/eIF4G2, and hnRNPQ. |
| **DARTS** | miRNA-RISC | ~22 nt microRNAs are processed by Drosha/DGCR8, Exportin-5, Dicer/TRBP, and AGO2 loading. Imperfect seed pairing to 3'UTRs recruits TNRC6/CCR4-NOT, causing deadenylation, decapping, and translational repression. |
| **SPONGE** | Cytoplasmic lncRNAs | Cytoplasmic lncRNAs can act as ceRNAs or miRNA sponges, but only when target-site abundance, affinity, and colocalization support meaningful competition. Examples include CDR1as/miR-7, HULC, and cytoplasmic HOTAIR contexts. Other lncRNAs modulate translation or act as decoys. |
| **CENSOR** | NMD (nonsense-mediated mRNA decay) | Surveillance of mRNAs carrying premature stop codons. If translation terminates >50-55 nt upstream of an exon junction complex, UPF factors and SMG1 trigger rapid degradation. NMD also regulates physiological alternative splicing products. |
| **TIMER** | mRNA stability / decay | mRNA half-lives range from minutes to over a day. The main route is deadenylation by CCR4-NOT/PAN2-PAN3, decapping by DCP1/2, and 5'→3' decay by XRN1; the exosome provides 3'→5' decay. ARE-binding proteins, miRNAs, and m6A tune stability. |
| **CLIPS** | RNA G-quadruplexes (rG4) | Guanine-rich RNA structures stabilized by K+ that occur in 5'UTRs, 3'UTRs, Pol II pause regions, and telomeric contexts. They can block 43S scanning, modulate IRES accessibility, and be unwound by helicases such as DHX36, eIF4A, and RHAU. |
| **VAULT** | Stress granules / P-bodies | Cytoplasmic RNA-protein condensates for mRNA storage, repression, or decay. **Stress granules** contain G3BP1, TIA-1, PABPC, and untranslated mRNAs. **P-bodies** contain DCP1/2, XRN1, CNOT, and decay machinery. Material exchanges dynamically between them. |

### Layer 5 — Translation
*Protein synthesis control at the ribosome.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **FORGE** | mTOR → cap-dependent initiation | mTORC1 phosphorylates 4E-BP1, releasing eIF4E and enabling eIF4F assembly. eIF4F recruits the 43S PIC, scans the 5'UTR, and recognizes AUG in a Kozak context. Insulin/nutrients activate PI3K/AKT/mTORC1, while AMPK inhibits mTORC1. |
| **BRAKE** | ISR / eIF2α-P | The integrated stress response uses GCN2, PERK, HRI, and PKR to phosphorylate eIF2α Ser51. eIF2α-P sequesters eIF2B, lowers ternary complex, and represses global cap-dependent translation while selectively favoring mRNAs such as ATF4 through uORF/reinitiation logic. |
| **DECOY** | uORFs (upstream ORFs) | Upstream ORFs in 5'UTRs divert scanning ribosomes and usually reduce main ORF translation. Short uORFs can permit reinitiation, and under stress ATF4 is selectively translated because low ternary complex causes bypass of inhibitory downstream uORFs. |
| **BYPASS** | IRES (Internal Ribosome Entry Sites) | RNA elements that recruit ribosomes through routes less dependent on the cap. Viral IRESs are well established; many cellular IRES claims remain context-dependent because bicistronic assays can confound cryptic promoters, splicing, or readthrough. Proposed cellular examples include HIF-1α, VEGF-A, FGF2, p53 isoforms, and c-MYC; ATF4 is mainly uORF/reinitiation-driven. |
| **TEMPO** | Codon usage + tRNA modifications + ribosome heterogeneity | Synonymous codons translate at different speeds depending on cognate tRNA abundance. tRNA modifications affect decoding fidelity, frameshifting, and stalling. Ribosomal protein variation or rRNA modifications may bias translation in some contexts, but "specialized ribosomes" remain experimentally difficult and should be treated as contextual rather than a settled general code. |
| **INSPECTOR** | Translation surveillance (RQC/NGD/NSD) | Quality-control mechanisms detect defective mRNAs and peptides. **NGD** responds to stalled ribosomes, **NSD** to mRNAs lacking stop codons, and **RQC** to stuck ribosomes whose nascent chains are ubiquitinated by LTN1. NEMF CAT-tailing can mark stalled peptides for degradation. |

### Layer 6 — Post-Translational Regulation
*Protein modification, maturation, routing, and destruction after synthesis.*

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **SWITCH** | Phosphorylation / O-GlcNAcylation | Phosphorylation on Ser/Thr/Tyr changes conformation, interaction sites, and enzyme or TF activity. It is reversible through phosphatases. O-GlcNAcylation adds GlcNAc on Ser/Thr and can crosstalk with phosphorylation. These switches activate kinases, Pol II CTD regulators, ISR kinases, and DDR pathways. |
| **ROUTER** | Ubiquitin code | The E1-E2-E3 cascade conjugates ubiquitin to substrate Lys residues. Chain topology determines fate: **K48** often routes to proteasome, **K63** supports signaling/scaffolding/autophagy routing, **K11** marks mitotic degradation, and **M1/linear** supports NF-κB signaling. |
| **TETHER** | SUMOylation | SUMO1/2/3 are conjugated by SAE1/SAE2, UBC9, and PIAS-family E3s. SUMOylation changes protein-protein interactions, stabilizes nuclear complexes, recruits co-repressors, modulates DNA repair, and can bridge to ROUTER through STUbL E3 ligases such as RNF4/RNF111. |
| **LICENSE** | Neddylation / CRL activation | NEDD8 is a ubiquitin-like protein conjugated mainly to cullins. Neddylation activates Cullin-RING ligases by improving substrate/E2 positioning. It is not an autonomous degradation route but an upstream switch that licenses ROUTER capacity for specific substrates. |
| **DESTROY** | Protein destruction: proteasome + selective autophagy | A fused box for the two major protein-clearance outputs. The **26S proteasome** reads mostly K48-polyUb, deubiquitinates, unfolds, and degrades short-lived or damaged proteins. **Selective autophagy** uses receptors such as p62/SQSTM1 to link ubiquitinated cargo to LC3/GABARAP and lysosomes, especially for aggregates, organelles, or bulky cargo. |
| **MATURE** | Chaperones / UPR | Chaperones such as Hsp70/Hsc70, Hsp90, and CCT/TRiC fold, refold, or triage proteins. CHIP links chaperones to ubiquitination of misfolded substrates. The ER **UPR** uses PERK, IRE1, and ATF6 to slow translation, expand folding capacity, and induce ER chaperone programs. |
| **PAR** | ADP-ribosylation / PARP / PAR | PARP1 detects DNA breaks and synthesizes poly-ADP-ribose on itself and other proteins. PAR chains nucleate DNA-damage condensates and recruit repair factors such as FUS, XRCC1, and RPA. PAR can also recruit ubiquitin/E3 factors and couple repair, remodeling, and local turnover, but broad proteasomal destruction is context-dependent. |

### Cross-Cutting Meta-Principles

| Code name | Full name | Exact definition |
|-----------|-----------|------------------|
| **LLPS** | Liquid-liquid phase separation | A thermodynamic process in which macromolecules concentrate into a dense phase or condensate-like assembly. Driven by multivalent interactions among IDRs, RGG repeats, tyrosines, RNA, and RNA-binding proteins. LLPS is not a single regulatory mechanism but a physical principle used by stress granules, P-bodies, PAR-damage foci, some transcriptional condensates, and some polyUb/proteolytic condensates. |
| **DECAY** | Turnover / clearance | A functional output that removes a molecule from the system: mRNA decay through TIMER/CENSOR, protein destruction through DESTROY, and broader switches between temporary storage and elimination. |

## II. Relation Catalogue (73 Mechanism Edges + 7 Meta Annotations)

### Color Code
| Color | Type | Meaning |
|-------|------|---------|
| Green `#27ae60` | Direct activation | A recruits, activates, or deposits B. |
| Red `#c0392b` | Direct repression | A blocks or prevents B (`arrowhead=tee`). |
| Yellow `#f4d03f` | Pol II coupling | Mechanism linked to Pol II progression. |
| Orange `#e67e22` | Co-transcriptional coupling | Regulation coupled to transcription. |
| Purple `#8e44ad` | Post-transcriptional / m6A / RBP | Post-transcriptional regulation. |
| Gray `#566573` | PTM / post-translational signaling | Post-translational regulation. |
| Blue `#2e86c1` | Structural / 3D | Three-dimensional organization. |
| Cyan `#22d3ee` dotted border | LLPS | Participation in LLPS/condensate logic. |
| Pink `#f472b6` dashed border | DECAY | Participation in turnover/clearance logic. |

### All Relations By Source Layer

#### 3D → 3D
| Source | Target | Relation name | Mechanism |
|--------|--------|---------------|-----------|
| ZONES | FENCES | **CONTAINS** | A/B compartments constrain TAD formation within them. |
| ZONES | WRITER-R | **ANCHORS-B** | B compartments anchor at the lamina and co-localize with H3K9/27me3. |
| FENCES | BRIDGES | **DELIMITS** | TAD boundaries insulate E-P loops within the same domain. |
| BRIDGES | HUBS | **ANCHORS-SE** | E-P loops anchor super-enhancers to target promoters. |

#### 3D → Epigenetics
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| OPENER | HUBS | **H3K27AC-BRD4** | BRD4 reads H3K27ac through bromodomains, supporting enhancer hubs. |
| HUBS | OPENER | **SE-ACETYLATION** | Super-enhancers maintain a highly acetylated local state. |

#### Epigenetics → Epigenetics
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SILENCER | WRITER-R | **CO-RECRUIT** (bidirectional) | MBD recruits SUV39H1 to H3K9me3, and HP1 can recruit DNMT3. |
| OPENER | SHUFFLER | **ACETYL-REMODEL** | Acetylated marks recruit bromodomain readers and remodelers such as SWI/SNF/BAF. |
| GUIDES | SILENCER | **PIRNAGUIDE** | piRNA-PIWI guides DNMT3L/3A toward transposons for *de novo* methylation. |

#### Epigenetics → Transcription
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| OPENER | KEYS | **OPENS-TF** | Histone acetylation loosens nucleosomes and gives TFs access. |
| WRITER-R | KEYS | **SILENCES-TF** ⊣ | H3K27me3/H3K9me3 compact chromatin and exclude TFs. |
| SHUFFLER | KEYS | **REMODELS** | CRCs reposition or evict nucleosomes to create TF binding windows. |
| WRITER-A | SCRIBE | **RECRUITS-POL2** | H3K4me3 recruits TAF3/TFIID and supports Pol II recruitment. |
| HUBS | SCRIBE | **RELEASES-PAUSE** | P-TEFb concentrated in SEs phosphorylates Ser2-CTD and releases paused Pol II. |
| OPENER | ZONES | **ACETYL-TO-A** | H3K27ac and active chromatin favor A-compartment identity. |
| WRITER-R | ZONES | **REPRESS-TO-B** | H3K27me3/H3K9me3 and heterochromatin favor B-compartment identity. |
| SILENCER | ZONES | **METH-TO-B** | CpG methylation recruits MBD, compacts chromatin, and favors B compartments. |

#### Transcription → Epigenetics (feedbacks)
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| KEYS | OPENER | **TF-HAT** | Activating TFs recruit p300/CBP to deposit H3K27ac. |
| KEYS | WRITER-A | **TF-KMT** | TFs recruit MLL/KMT2 enzymes to deposit H3K4me3. |
| KEYS | SHUFFLER | **TF-CRC** (back) | TFs recruit SWI/SNF to their target genes. |
| KEYS | GUIDES | **TF-NCRNA-EPI** | TFs can activate piRNA/lncRNA loci that later guide chromatin complexes. |
| KEYS | SPONGE | **TF-LNCRNA** | TFs activate cytoplasmic lncRNA loci, adding a post-transcriptional output. |

#### Transcription → Transcription
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| KEYS | SCRIBE | **INITIATES** | TFs recruit Mediator, assemble the PIC, and recruit Pol II. |
| KEYS | HUBS | **DEFINES-SE** | Master TFs such as OCT4, MYC, and SOX2 define and maintain SE identity. |
| KEYS | RECODER | **IFN-ADAR** | IFN-response TFs such as IRF3/7 transcribe ADAR1p150. |

#### Transcription → Co-Transcriptional
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SCRIBE | SHIELD | **CTD-CAP** | Ser5-P CTD recruits capping enzymes. |
| SCRIBE | SPLICER | **RATE-SPLICE** (**) | Pol II elongation speed sets the opportunity window for weak exon inclusion. |
| SCRIBE | TRIMMER | **CTD-CST** | Pol II Ser2-P recruits CstF for cleavage and polyadenylation. |
| SCRIBE | STAMP | **CTD-M6A** | METTL3/14 is recruited by the CTD for co-transcriptional m6A. |
| SCRIBE | ZONES | **TXN-TO-A** | Transcriptional activity helps maintain active regions in A compartments. |
| WRITER-A | SPLICER | **HISTONE-SPLICE** (**) | H3K36me3 deposited by SETD2-associated Pol II recruits MRG15/PTB to affect exon inclusion. |
| SCRIBE | WRITER-A | **SETD2-COUPLING** (**) | SETD2 physically couples to Pol II Ser2-P and deposits H3K36me3 during elongation. |

(**) = key kinetic couplings linked to principle C.

#### Post-Transcriptional → Co-Transcriptional (feedbacks)
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| STAMP | SPLICER | **M6A-SPLICE** (back) | Nuclear YTHDC1 binds m6A and recruits SRSF3/SRSF10 to affect splicing. |
| READERS | SPLICER | **RBP-SPLICE** (back) | SR proteins and hnRNPs regulate spliceosomal ESE/ESS recognition. |
| RECODER | SPLICER | **ADAR-SPLICE** (bidirectional) | ADAR1/2 edit 5' splice sites and alter U1 snRNA recognition. |

#### Co-Transcriptional → Post-Transcriptional
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SPLICER | CENSOR | **SPLICE-NMD** | Alternative exons introducing PTCs send the isoform to NMD. |
| TRIMMER | DARTS | **APA-MIRNA** | Long 3'UTRs expose additional miRNA sites. |
| TRIMMER | READERS | **APA-RBP** | Long 3'UTRs expose additional RBP sites. |
| RECODER | CENSOR | **ADAR-NMD** | Alu exonization can create PTCs; ADAR editing near 5'SS can prevent exonization. |

#### Post-Transcriptional Intra-Layer
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| STAMP | TIMER | **M6A-DECAY** | Cytoplasmic YTHDF proteins, classically YTHDF2, promote CCR4-NOT/P-body decay routes. |
| STAMP | CLIPS | **M6A-G4** | m6A can destabilize adjacent RNA G-quadruplex structures. |
| DARTS | TIMER | **MIRNA-DECAY** | AGO2-RISC recruits CCR4-NOT for deadenylation and decapping. |
| SPONGE | DARTS | **CERNA** ⊣ | lncRNA/circRNA ceRNAs can sponge miRNAs when stoichiometry and colocalization are sufficient. |
| CENSOR | TIMER | **NMD-DECAY** | UPF1-P recruits SMG6 and SMG5/7 for rapid degradation. |
| TIMER | VAULT | **MRNA-SG** (bidirectional) | Untranslated mRNAs enter granules; dissolved granules release mRNAs. |
| READERS | TIMER | **RBP-STABILITY** | HuR/ELAVL1 stabilizes AREs, while TTP/ZFP36 destabilizes through CCR4-NOT. |
| CLIPS | BYPASS | **G4-IRES** | rG4 structures in 5'UTRs can modulate IRES accessibility. |

#### Post-Transcriptional → Translational
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| STAMP | FORGE | **M6A-INIT** | m6A can stimulate initiation via YTHDF1/eIF3 or context-dependent 5'UTR mechanisms. |
| STAMP | BYPASS | **M6A-IRES** | 5'UTR m6A can promote cap-independent translation under stress. |
| READERS | FORGE | **FMRP-REPRESS** ⊣ | FMRP binds polysomes and represses translation. |
| DARTS | FORGE | **MIRNA-TRANSL** ⊣ | RISC blocks 80S joining or reinitiation, inhibiting translation. |
| CLIPS | FORGE | **G4-BLOCK** ⊣ | 5'UTR rG4 blocks 43S scanning. |

#### Capping → Translation
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SHIELD | FORGE | **CAP-EIF4E** | The m7G cap is recognized by eIF4E, enabling eIF4F assembly and initiation. |

#### Translational Intra-Layer
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| BRAKE | DECOY | **ISR-UORF** (**) | eIF2α-P limits ternary complex, causing ribosomes to bypass inhibitory uORFs and induce ATF4. |
| BRAKE | BYPASS | **ISR-IRES** | Cap-dependent translation is blocked, favoring alternative routes; ATF4 is mainly uORF/reinitiation-driven, while HIF-1α/c-MYC are proposed IRES-like cases. |
| DECOY | FORGE | **UORF-COMPETE** ⊣ | uORFs sequester ribosomes and reduce main ORF translation. |
| FORGE | INSPECTOR | **STALL-RQC** | Active translation can stall on rare codons or structures, triggering RQC/NGD. |
| TEMPO | INSPECTOR | **CODON-STALL** | Rare codons can prolong ribosome pauses and trigger NGD/NSD/RQC. |
| TEMPO | MATURE | **COTRANSL-FOLD** | Translation rhythm shapes co-translational folding kinetics. |
| INSPECTOR | DESTROY | **RQC-26S** | CAT-tailed stalled nascent peptides are recognized by LTN1 and degraded. |

#### Translation → Post-Translational
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| FORGE | MATURE | **COTRANSL-MATURATION** | Nascent translation exposes chains to co-translational chaperones and folding. |
| FORGE | SWITCH | **MTOR-KINASES** | mTORC1 and growth pathways couple initiation to AKT/S6K and other kinase cascades. |

#### Post-Translational Intra-Layer
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SWITCH | ROUTER | **SWITCH-DEGRON** | Phospho-degrons are recognized by SCF E3s such as β-TrCP/Fbxw7 or APC/C. |
| SWITCH | TETHER | **PDSM** | PDSM motifs use Ser phosphorylation to activate SUMOylation on nearby Lys. |
| ROUTER | DESTROY | **ROUTER-DESTROY** | K48-polyUb routes to 26S proteasome; K63-polyUb can recruit p62/SQSTM1 for selective autophagy. |
| TETHER | ROUTER | **STUBLS** | polySUMO is recognized by RNF4/RNF111 STUbL E3s and converted into ubiquitin routing. |
| LICENSE | ROUTER | **CRL-ACTIVATION** | Cullin neddylation activates CRL E3 ligases for substrate ubiquitination. |
| PAR | DESTROY | **PAR-CONDENSATE** | Long PAR chains support DDR condensates and contextual recruitment of ubiquitin/proteostasis factors. |
| MATURE | BRAKE | **UPR-ISR** | PERK in the UPR phosphorylates eIF2α and activates the ISR. |
| DESTROY | FORGE | **LYSOSOME-MTOR** | Amino acids released by lysosomes activate Ragulator/RRAG and reactivate mTORC1. |
| DESTROY | KEYS | **DESTROY-TF** | Degradation of TF inhibitors, such as IκBα, activates TF programs such as NF-κB. |

#### Post-Translational → Transcription / Pol II
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| SWITCH | SCRIBE | **CDK9-CTD** | Activated CDK9/P-TEFb phosphorylates Ser2-CTD and releases paused Pol II. |
| SWITCH | BRAKE | **KINASE-EIF2A** | GCN2, PERK, HRI, and PKR phosphorylate eIF2α Ser51 and activate BRAKE. |

#### Cross-Cutting Meta-Principles
| Source | Target | Name | Mechanism |
|--------|--------|------|-----------|
| LLPS | HUBS | **LLPS-SE** | LLPS/transcriptional condensates can contribute to super-enhancer activity without being identical to it. |
| LLPS | VAULT | **LLPS-SG-PB** | LLPS forms stress granules and P-bodies. |
| LLPS | DESTROY | **LLPS-DESTROY** | LLPS can form proteolytic or polyUb condensates in some contexts. |
| LLPS | PAR | **LLPS-PAR** | PAR chains nucleate DNA-repair condensates. |
| DECAY | TIMER | **DECAY-MRNA** | mRNA turnover through deadenylation, decapping, and exonucleases. |
| DECAY | CENSOR | **DECAY-NMD** | NMD as a surveillance and elimination branch for aberrant mRNAs. |
| DECAY | DESTROY | **DECAY-DESTROY** | Ubiquitin-dependent protein degradation or selective lysosomal clearance of proteins, aggregates, or organelles. |

## III. Overlaps And Mergers — What Was Consolidated

| Merged entities | Rationale |
|-----------------|-----------|
| Super-enhancers + transcriptional condensates | Closely related but not identical: super-enhancer is a genomic/ChIP-seq definition; condensate is a dynamic physical assembly enriched in coactivators. |
| A/B compartments + global epigenetic state | Strongly correlated; compartments emerge from marks but are not identical to them. |
| YTHDF1 + YTHDF2 + YTHDF3 → **STAMP** | One signal, m6A, with partly specialized but also redundant readers depending on context. |
| Codon usage + tRNA modifications + ribosome heterogeneity → **TEMPO** | Three facets of decoding-efficiency control. |
| SWI/SNF + ISWI + CHD + INO80 → **SHUFFLER** | Same ATP-dependent remodeling principle across four subfamilies. |
| eRNAs (enhancer RNAs) | Mostly enhancer-activity readouts, not a separate mechanism box here. |
| ISR branch PERK / UPR | PERK is both an ISR kinase and a UPR branch, integrated through MATURE → BRAKE. |
| siRNA / miRNA | Share RISC/AGO2; animal siRNA is mostly an experimental/tool-like variant here, folded into DARTS. |
| ceRNA hypothesis | Special case of SPONGE + DARTS, kept as a conditional mechanism requiring stoichiometric support. |

## Appendix A — Databases And Resources

| Resource | URL | Contents |
|----------|-----|----------|
| ENCODE | https://encodeproject.org | ChIP-seq, ATAC-seq, CTCF, histone marks, 150+ cell types |
| Roadmap Epigenomics | https://egg2.wustl.edu/roadmap | 127 cell types, methylation + histone maps |
| GTEx | https://gtexportal.org | Tissue-specific eQTLs |
| FANTOM5 | https://fantom.gsc.riken.jp/5 | TSS atlas, eRNAs, lncRNAs |
| miRBase | https://mirbase.org | miRNA catalogue |
| POSTAR3 | http://postar.ncrnalab.org | RBP binding sites from CLIP-seq |
| RMBase v3 | https://rmbase.sysu.edu.cn | RNA modification sites (m6A, m5C, Ψ...) |
| G4 motif resources | To verify | G-quadruplexes in transcriptomes |
| PhosphoSitePlus | https://phosphosite.org | PTM sites (phosphorylation, ubiquitination, acetylation, methylation) |
| STRING | https://string-db.org | Protein-protein interactions |
| UniProt | https://uniprot.org | Protein annotations + PTMs |

## Appendix B — Foundational References

- Kouzarides T. (2007). Chromatin modifications and their function. *Cell* 128(4):693-705.
- Wang X. & He C. (2014). Dynamic RNA modifications in posttranscriptional regulation. *Mol Cell* 56(1):5-12.
- Core L. & Adelman K. (2019). Promoter-proximal pausing of RNA polymerase II. *Nat Rev Genet* 20:700-714.
- Naftelberg S. et al. (2015). Regulation of alternative splicing through coupling with transcription and chromatin structure. *Annu Rev Biochem* 84:165-198.
- Dever TE et al. (2023). Translational control by uORFs. *Genes Dev* 37(11-12):474-489.
- Rhine K. et al. (2023). Regulation of biomolecular condensates by poly(ADP-ribose). *Chem Rev* 123:9065.
- Bhatt DL et al. (2020). Integrated Stress Response in gene regulation. *Nat Rev Mol Cell Biol*.
- Noda Y. et al. (2022). Regulation of A-to-I RNA editing and stop codon recoding. *Nat Commun* 13:2503.
- Robson et al. (2019). Regulatory functions of chromatin topology. *Nat Rev Genet* 20:489-499.
- Yau R. & Bhatt DL (2020). Ubiquitin-modulated phase separation of shuttle proteins. *J Mol Biol*.

---

*v7 — 37 mechanisms, 2 meta-principles, 73 mechanism relations + 7 meta annotations*
*File: `assets/documents/gene-regulation-landscape-details.md`*
*Diagram: `assets/documents/gene-reg-v7.dot` + `assets/images/gene-reg-v7.png`*
