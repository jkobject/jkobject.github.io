---
title: "The Gene Regulation Landscape"
excerpt: "A compact map of how cells decide which genes become proteins"
date: 2026-06-10
category: "PhD"
tags:
  - Cell Bio
  - Comp-Bio
header:
  teaser: "/assets/images/gene-expr.png"
---

I have always wanted to understand how a cell works.

Most of the time, even when textbooks go into molecular detail, the story is
still organized around dogmas. One chapter adds chromatin. Another adds
transcription factors. Later, RNA processing appears. Then translation, protein
degradation, signaling, condensates, non-coding RNAs, and so on. Each new
mechanism is real, but they often arrive as separate layers of complexity, not
as one formal picture of what we collectively know.

That is what I tried to build here: a summary of our current formal knowledge of
gene regulation, placed into one landscape.

While doing it, I noticed something that surprised me. Biology has many
measurements and many local names, but sometimes no clean conceptual object for
things that are probably views of the same underlying cellular structure. For
example, super-enhancers in ChIP-seq and transcriptional condensates in
microscopy are not strictly identical, but they are clearly not unrelated
either. In other places, molecular biology has long descriptive sentences for
mechanisms, but no short handle that makes the mechanism easy to reason about.

So I gave each main mechanism a short code name. The names are not meant to
replace the biology; they are handles that point back to precise glossary
entries. I hope the map is useful, and maybe sparks discussions.

The map is very large, so the embedded version below is mostly a preview. You can
[open the full-resolution zoomable map here](/assets/images/gene-reg-v7.png).
The companion [technical notes](/assets/documents/gene-regulation-landscape-details.md)
contain the 1-to-1 glossary for every box name, the full mechanism catalogue,
link rationale, and legend details. The [Graphviz DOT source](/assets/documents/gene-reg-v7.dot)
is also available.

In the figure, each box title is a code name that maps 1-to-1 to the catalogue
entry in the technical notes. Solid arrows are the main mechanistic relations;
dashed arrows indicate contextual, feedback, or association-style links;
tee-headed arrows indicate repression; bold arrows mark especially important
coupling edges. Border styles mark meta-principles such as `LLPS` and `DECAY`:
these are recurring physical or regulatory motifs that appear across several
mechanisms, not separate boxes in the pathway.

[![Gene Regulation Landscape](/assets/images/gene-reg-v7.png)](/assets/images/gene-reg-v7.png)

## Box Glossary

Each box in the image has exactly one entry here. Box titles are the short code
names; italic text inside the image marks genes or proteins when the label needs
examples.

| Code | Layer | Meaning |
|------|-------|---------|
| `ZONES` | 3D genome | A/B chromatin compartments. |
| `FENCES` | 3D genome | TAD boundaries and insulation by CTCF/cohesin. |
| `BRIDGES` | 3D genome | Enhancer-promoter loops. |
| `HUBS` | 3D genome | Super-enhancers and Pol II condensates. |
| `SILENCER` | Epigenetics | DNA methylation and repressive chromatin memory. |
| `OPENER` | Epigenetics | Histone acetylation that opens chromatin. |
| `WRITER-A` | Epigenetics | Activating histone methylation marks. |
| `WRITER-R` | Epigenetics | Repressive histone methylation marks. |
| `SHUFFLER` | Epigenetics | ATP-dependent nucleosome remodeling. |
| `GUIDES` | Epigenetics | ncRNAs that recruit chromatin regulators. |
| `KEYS` | Transcription | Transcription factors, including pioneer factors. |
| `SCRIBE` | Transcription | Pol II pausing, release, and CTD phosphorylation. |
| `SHIELD` | Co-transcriptional | 5' capping and cap-dependent protection/export. |
| `SPLICER` | Co-transcriptional | Alternative splicing coupled to Pol II kinetics. |
| `TRIMMER` | Co-transcriptional | Alternative polyadenylation and 3'UTR choice. |
| `RECODER` | Co-transcriptional | A-to-I RNA editing by ADARs. |
| `STAMP` | Post-transcriptional | m6A RNA marking and reader-dependent fate choices. |
| `READERS` | Post-transcriptional | RNA-binding proteins that tune RNA processing, stability, localization, and translation. |
| `DARTS` | Post-transcriptional | miRNA-RISC targeting. |
| `SPONGE` | Post-transcriptional | Cytoplasmic lncRNAs and ceRNA-like buffering. |
| `CENSOR` | Post-transcriptional | Nonsense-mediated mRNA decay. |
| `TIMER` | Post-transcriptional | mRNA half-life, deadenylation, decapping, and decay. |
| `CLIPS` | Post-transcriptional | RNA G-quadruplex structures that affect scanning and translation. |
| `VAULT` | Post-transcriptional | Stress granules and P-bodies for RNA storage or decay. |
| `FORGE` | Translation | Starting cap-dependent translation through mTOR/eIF4F. |
| `BRAKE` | Translation | Slowing global translation during stress through ISR/eIF2α-P. |
| `DECOY` | Translation | uORFs that divert scanning ribosomes and gate main ORF translation. |
| `BYPASS` | Translation | IRES-driven translation without the normal cap/scanning route. |
| `TEMPO` | Translation | Ribosome speed, pausing, codon usage, and co-translational folding. |
| `INSPECTOR` | Translation | RQC/NGD/NSD surveillance of stalled or broken translation. |
| `SWITCH` | Post-translational | Phosphorylation/O-GlcNAc switches for protein activity and interactions. |
| `UBI` | Post-translational | Ubiquitin-chain logic that routes proteins to signaling, proteasome, or autophagy. |
| `SUMO` | Post-translational | SUMOylation that tunes nuclear localization, repression, complex assembly, and DNA repair. |
| `NEDD8` | Post-translational | Neddylation that activates cullin-RING E3 ubiquitin ligases. |
| `DESTROY` | Post-translational | Protein clearance through the proteasome and selective autophagy. |
| `MATURE` | Post-translational | Protein folding, refolding, triage, and ER-stress UPR. |
| `PAR` | Post-translational | PARP/PAR signaling at DNA damage and repair condensates. |

## The Seven Layers

The map follows the flow from DNA to RNA to protein:

1. **3D genome**: `ZONES`, `FENCES`, `BRIDGES`, and `HUBS` represent A/B
   compartments, TADs, enhancer-promoter loops, and super-enhancers or
   transcriptional condensates.
2. **Epigenetics**: `SILENCER`, `OPENER`, `WRITER-A`, `WRITER-R`, `SHUFFLER`,
   and `GUIDES` cover DNA methylation, histone marks, chromatin remodeling, and
   non-coding RNAs that guide chromatin complexes.
3. **Transcription**: `KEYS` are transcription factors; `SCRIBE` is Pol II,
   promoter-proximal pausing, and the phosphorylation code of its CTD.
4. **Co-transcriptional processing**: `SHIELD`, `SPLICER`, `TRIMMER`, and
   `RECODER` cover capping, alternative splicing, alternative polyadenylation,
   and A-to-I RNA editing.
5. **Post-transcriptional control**: `STAMP`, `READERS`, `DARTS`, `SPONGE`,
   `CENSOR`, `TIMER`, `CLIPS`, and `VAULT` cover m6A, RNA-binding proteins,
   miRNAs, lncRNAs, nonsense-mediated decay, mRNA stability, RNA structures, and
   cytoplasmic granules.
6. **Translation**: `FORGE`, `BRAKE`, `DECOY`, `BYPASS`, `TEMPO`, and
   `INSPECTOR` describe cap-dependent initiation, the integrated stress
   response, uORFs, IRES elements, decoding kinetics, and ribosome quality
   control.
7. **Post-translational regulation**: `SWITCH`, `UBI`, `SUMO`, `NEDD8`,
   `DESTROY`, `MATURE`, and `PAR` cover phosphorylation/O-GlcNAc, ubiquitin,
   SUMOylation, neddylation, proteasome/autophagy clearance, maturation/UPR,
   and PARP/PAR signaling.

Across the whole diagram, border styles flag recurring meta-principles. `LLPS`
marks liquid-liquid phase separation, and `DECAY` marks turnover or clearance.
They are not extra regulatory layers. They are reused in several places:
transcriptional condensates, stress granules and P-bodies, mRNA decay,
proteolytic condensates, autophagy, and DNA damage repair assemblies.

## The Useful Reduction

The full map contains 37 mechanism boxes, 2 meta-principles, and dozens of
interactions. But conceptually, most of gene regulation reduces to three
strategies.

**1. Control accessibility.**  
Make a substrate accessible or inaccessible to its molecular machinery.
Chromatin opening lets transcription factors bind. TADs constrain which
enhancers can contact which promoters. Stress granules temporarily remove mRNAs
from translation. miRNAs and lncRNAs tune whether an mRNA is available to the
ribosome.

**2. Write a reversible mark, then interpret it.**  
Histone methylation, DNA methylation, m6A, phosphorylation, ubiquitination,
SUMOylation: the mark alone is never the full story. The reader and the context
determine the output. m6A can promote translation or accelerate decay. A K48
ubiquitin chain points toward the proteasome; K63 often acts in signaling or
selective autophagy. Phosphorylation can activate a transcription factor or
create a degron.

**3. Couple two processes through kinetics.**  
Some regulation is not a static state but a timing problem. Pol II elongation
speed influences exon choice. SETD2 deposits H3K36me3 during elongation, linking
transcription to splicing. eIF2α phosphorylation globally slows translation but
selectively favors ATF4 through uORF logic. Codon usage changes ribosome speed
and can influence co-translational folding.

That is the central idea of the landscape: gene regulation is not just a list of
mechanisms. It is a multi-layer control architecture built from recurring design
patterns.

## Why This Matters For AI Biology

For AI biology, this kind of map is not only educational. It shows why
predicting “gene expression” cannot be reduced to reading a promoter sequence.

The output of a gene depends on chromatin state, 3D contacts, Pol II kinetics,
splicing, RNA modifications, RNA-binding proteins, translational control, and
protein lifetime. A model that wants to predict perturbation response, cell
state, or disease mechanism needs to represent at least part of this stack.

The lesson of the Gene Regulation Landscape is simple: gene expression is not a
scalar. It is the endpoint of a control system.

## Sources To Anchor The Map

- Core & Adelman, 2019, promoter-proximal Pol II pausing:
  https://pubmed.ncbi.nlm.nih.gov/31123063/
- Naftelberg et al., 2015, transcription/chromatin/splicing coupling:
  https://pubmed.ncbi.nlm.nih.gov/26034889/
- Wang & He, 2014, dynamic RNA modifications:
  https://pubmed.ncbi.nlm.nih.gov/25263552/
- Wang et al., 2015, m6A and translation efficiency:
  https://www.cell.com/cell/fulltext/S0092-8674(15)00562-0
- Shi et al., 2017, YTHDF3 translation/decay:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5339834/
- Sabari et al., 2018, coactivator condensation at super-enhancers:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6092193/
- Robson et al., 2019, chromatin topology:
  https://pubmed.ncbi.nlm.nih.gov/31324893/
