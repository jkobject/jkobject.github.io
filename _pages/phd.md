---
title: "Ph.D."
layout: single
excerpt: "Foundation models for cell biology — ENS / Institut Pasteur, 2022–2026"
sitemap: true
permalink: /phd/
header:
  overlay_image: ""
  caption: ""
skip_amp: false
toc: true
---

## Abstract

Single-cell RNA sequencing has opened a window into the cellular diversity of living organisms at unprecedented resolution — but making sense of millions of cells across thousands of studies remains a formidable challenge. My PhD, completed in March 2026 at ENS and Institut Pasteur under the supervision of [Laura Cantini](https://research.pasteur.fr/fr/team/machine-learning-for-integrative-genomics/) and [Gabriel Peyré](http://www.gpeyre.com/), tackled this challenge by building **foundation models for cell biology**: large-scale, pre-trained transformer models capable of learning universal representations of transcriptomic data.

The central contribution is **scPRINT**, a foundation model trained on tens of millions of single cells that can denoise expression profiles, embed cells in a meaningful latent space, and — most distinctively — infer **gene regulatory networks (GRNs)** directly from single-cell data. Unlike prior methods, scPRINT leverages the full complexity of large-scale single-cell atlases to produce cell-type-specific regulatory landscapes, without requiring bulk ATAC-seq or ChIP-seq. scPRINT was published in *Nature Communications* (2025). Its successor, **scPRINT-2**, extends the framework with improved scalability and generalization, and is currently under revision at *Nature Methods*.

To make this work possible, I developed a full software ecosystem: **scDataLoader** for efficient multi-dataset training, **GRnnData** for storing and manipulating GRN data alongside single-cell objects, **BenGRN** for benchmarking GRN inference methods, **Xpressor** for expression prediction, and the scPRINT-2 model itself. Taken together, this thesis establishes a new paradigm for analyzing single-cell data through the lens of foundation models, with concrete biological insights into transcriptional regulation.

<a href="/assets/documents/PhD_project.pdf" class="btn btn--primary btn--large">Ph.D. Proposal</a>

---

## The Thesis Manuscript

<iframe src="/assets/documents/thesis.pdf" width="100%" height="800" frameborder="0"></iframe>

---

## Packages

<div class="grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
  <a href="https://www.jkobject.com/projects/about-scprint/"><img src="/assets/images/scprint.png" alt="scPRINT"></a>
  <a href="https://www.jkobject.com/projects/about-scdataloader/"><img src="/assets/images/scdataloader.png" alt="scDataLoader"></a>
  <a href="https://www.jkobject.com/projects/about-grnndata/"><img src="/assets/images/grnndata.png" alt="GRNData"></a>
  <a href="https://www.jkobject.com/projects/about-bengrn/"><img src="/assets/images/bengrn.png" alt="BenGRN"></a>
  <a href="https://www.jkobject.com/projects/about-xpressor/"><img src="/assets/images/xpressor.png" alt="Xpressor"></a>
  <a href="https://www.jkobject.com/projects/about-scprint2/"><img src="/assets/images/scprint2.png" alt="scPRINT2"></a>
</div>

---

## Blog Posts

These posts trace the arc of the PhD — the decision to start, the work in progress, and the finish line.

- 🚀 [The PhD Decision: GRNs & Foundation Models](/blog/the-phd-decision-grn-foundation-model/) — Why I left industry to pursue this PhD, and what I hoped to build *(Oct 2023)*
- 🧬 [Ancestry Bias in CRISPR Screens](/blog/ancestry-bias-in-crispr/) — A paper on population bias in CRISPR libraries, published in *Nature Communications* *(Jun 2024)*
- 📅 [A Year in the PhD](/blog/a-year-in-the-phd/) — Reflections after the first year: what I learned, what surprised me *(Sep 2024)*
- 🤖 [About the AIVC Paper](/blog/about-the-aivc-paper/) — Commentary on the AI Virtual Cell initiative and where it sits in the landscape *(Dec 2024)*
- 🧫 [VCC Starter Pack](/blog/vcc-starter-pack/) — A practical guide to working with Virtual Cell Concepts *(Oct 2025)*
- 🏁 [Finishing the PhD](/blog/finishing-the-phd/) — The final stretch: writing up, defending, and what comes next *(Mar 2026)*

---

## Technical Guides

During the PhD I wrote a few deep-dive guides on methods I used daily. These stand on their own as references.

- 📊 [Enrichment Analysis: Enrichr, PreRank & GSEA](/blog/enrichr-prerank-gsea/) — A practical walkthrough of gene set enrichment methods *(Feb 2024)*
- 📐 [AUPRC vs Average Precision](/blog/auprc-vs-ap/) — Clarifying the difference between two commonly confused classification metrics *(Jun 2024)*
- 🕸️ [Gene Regulatory Networks: what they are and how to use them](/blog/manage-grn-and-what-they-mean/) — A conceptual and practical guide to GRNs in single-cell biology *(Jun 2024)*
- 🔬 [What are Large Cell Models?](/blog/what-are-large-cell-models/) — Defining the emerging class of foundation models for biology *(Sep 2024)*

---

## Presentations

### scPRINT @ISMB/ECCB

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/wZswWkJZqcI" frameborder="0" allowfullscreen></iframe>

### Outreach

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/bgtcDs5EXY8" frameborder="0" allowfullscreen></iframe>

### First Year PhD Committee Presentation

<iframe width="100%" height="70%" src="https://www.youtube.com/embed/ePRU9E7sWNY" frameborder="0" allowfullscreen></iframe>

### scPRINT @GenBioAI

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/D3ykmh-CH3w" frameborder="0" allowfullscreen></iframe>

### scPRINT @ValenceLabs

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/s9_DZz9E1To" frameborder="0" allowfullscreen></iframe>

### Hackathon using scPRINT @Owking @Servier

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/DFPTvAYMxjk" frameborder="0" allowfullscreen></iframe>

### Outreach @ Pint of Science

<iframe width="100%" height="70%"  src="https://www.youtube.com/embed/fc8L8Dn_7tw" frameborder="0" allowfullscreen></iframe>

I undertook many more presentations at a dozen conferences and companies, of not
only scPRINT but also Xpressor (@IBM) and scPRINT-2 (@RAMH).
