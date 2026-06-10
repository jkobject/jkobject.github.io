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

So I gave the main mechanisms nicknames. Not because the nicknames are perfect,
but because naming is a way to think. I hope the map is useful, and maybe sparks
discussions.

The map is very large, so the embedded version below is mostly a preview. You
can [open the full-resolution zoomable map here](/assets/images/gene-reg-v7.png).
For the full mechanism catalogue and the detailed edge list used to build the
figure, see the [Gene Regulation Landscape technical notes](/assets/documents/gene-regulation-landscape-details.md)
and the [Graphviz DOT source](/assets/documents/gene-reg-v7.dot).

[![Gene Regulation Landscape](/assets/images/gene-reg-v7.png)](/assets/images/gene-reg-v7.png)

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
7. **Post-translational regulation**: `SWITCH`, `TAG`, `STAMP2`, `SHREDDER`,
   `RECYCLER`, `FOLDER`, and `ALARM` cover phosphorylation, ubiquitin,
   SUMO/NEDD8, the proteasome, autophagy, chaperones/UPR, and PARP/PAR
   signaling.

Across the whole diagram, `DROPLETS` represents liquid-liquid phase separation.
It is not an extra regulatory layer. It is a physical principle reused in
several places: transcriptional condensates, stress granules, P-bodies,
proteolytic condensates, and DNA damage repair assemblies.

## The Useful Reduction

The full map contains 38 mechanisms and dozens of interactions. But
conceptually, most of gene regulation reduces to three strategies.

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
