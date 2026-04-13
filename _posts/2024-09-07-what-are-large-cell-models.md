---
title: "What are large cell models?"
excerpt: "A few thoughts on the term large cell models that I am using in my recent paper and my posts"
category: "PhD"
toc: true
date: 2024-09-07
tags:
 - Comp-Bio
header:
  teaser: "/assets/images/aivc.jpg"
---

In my recent paper [scPRINT](https://www.biorxiv.org/content/10.1101/2024.07.29.605556v1) I define the term Large Cell Model but what are they?

AI is everywhere nowadays, and in biology it is helping us enter a new era of what [jacob kimmel](https://x.com/jacobkimmel/status/1829550511768674401) describes as predictive biology.

In this new field, we use complex computational approaches together with high throughput data gathering to generate predictive models of physical phenoma like protein folding, binding, regulation, response, etc. 🧬

scPRINT, like scGPT, geneformer, scFoundation, scLM and more is part of a bread of AI tools 🤖 that try to better model the cell regulation and response using a large amount of parameters and data. In this context they are -large- -cell models-. 🦠

## Why This Name?

The analogy to Large Language Models (LLMs) is intentional and I think it's a good one. LLMs are trained on massive corpora of text and learn to model the "language" of human expression — grammar, semantics, context, all of it emergently, without being hand-coded. The hope with LCMs is exactly the same: train on massive datasets of single-cell transcriptomics and let the model learn the "language" of the cell. 🔤

A cell expresses thousands of genes at once. Which genes are active, how much, in what combination — this is the cell's way of encoding its state, its identity, its response to the environment. If we squint, gene expression profiles look a lot like sentences in a high-dimensional language. So it makes sense to apply similar techniques. Transformers, masked token prediction, large-scale pretraining — the same toolkit that gave us GPT-4 and BERT, now applied to biology.

The "Large" part matters too. These models are trained on tens of millions of single-cell profiles. Geneformer (~40M parameters) used 30M cells for pretraining. scGPT (~50M parameters) used 33M. scFoundation pushed further with ~100M parameters and 50M cells. And the field keeps scaling. 📈

## What Can They Actually Do?

This is where things get interesting — and also where a lot of hype meets hard reality.

In principle, LCMs can do several useful things:

- **Cell embeddings**: Compress a high-dimensional gene expression profile into a compact vector that captures biological meaning. Useful for cell type annotation, clustering, comparison across datasets.
- **Perturbation prediction**: Given a cell state, predict how gene expression would change if you knock out a gene, add a drug, or apply a cytokine. This is the holy grail for drug discovery. 💊
- **GRN inference**: Extract which genes regulate which other genes — reconstructing the regulatory logic of a cell from the patterns the model learned.
- **Batch integration**: Harmonize data from different labs, technologies, or conditions into a shared embedding space.

In practice? It's more nuanced. Recent benchmarking shows that in zero-shot settings (using these models without fine-tuning), both scGPT and Geneformer can be outperformed by simpler methods like selecting highly variable genes and running scVI or Harmony. That's a bit sobering. 😅

But the fine-tuned performance is real. And unlike classic approaches, LCMs don't need you to specify the regulatory logic upfront — they learn it from data. That's the paradigm shift.

## How Are They Different from Classical Approaches?

Before LCMs, the computational biology toolkit included things like pseudotime analysis, diffusion maps, factor analysis, and simple regression models for GRN inference. These are great tools! But they require a lot of prior knowledge and don't generalize well. You'd fit a model per dataset, per question.

LCMs change the frame: you pretrain once on the universe of available data, then adapt to specific questions. It's the transfer learning paradigm that revolutionized NLP and computer vision — finally landing in single-cell biology. The bet is that the representations learned at scale will capture something more fundamental about how cells work.

## The Hard Challenges

I won't sugarcoat it. LCMs face serious obstacles:

**Data quality and scale.** Tens of millions of cells sounds like a lot, but the human body has ~37 trillion cells across hundreds of types and states. Most training data is heavily biased toward easy-to-measure cell types (blood, PBMCs, cell lines). Rare cell types, spatial context, and dynamic states are vastly underrepresented. 🔍

**Evaluation is hard.** What does it mean for a cell model to be "good"? We don't have ground-truth labels for most biological processes. Perturbation benchmarks help, but they're limited in scale and often use the same few datasets everyone trains on. The field badly needs better, truly held-out evaluation.

**The measurement bottleneck.** As I've [written before](/PhD/about-the-aivc-paper/), the fundamental constraint isn't really the algorithm or even the compute — it's our ability to measure cellular state accurately. Current scRNA-seq gives us a snapshot of messenger RNA, but misses proteins, non-coding RNAs, spatial organization, dynamic timescales... A model can only be as good as the data it learns from.

**What's actually learned?** Recent interpretability work using sparse autoencoders on Geneformer and scGPT suggests these models have internalized rich biological structure — pathway membership, protein interactions, cell type identity. But they capture mostly *co-expression* patterns, not genuine *causal regulatory logic*. Whether scaling will fix this or whether we need different architectures is an open question. 🤔

## Where Is This Going?

I'm genuinely excited about the trajectory of this field, even with all the caveats above.

The next few years will likely bring bigger models trained on more diverse, multimodal data — combining transcriptomics with proteomics, epigenomics, spatial information. Better measurement technologies (total RNA-seq, multiplexed protein imaging, long-read sequencing) will give us richer training signal. And the benchmarking community is getting sharper about what "good" actually means.

The analogy to LLMs is instructive here too: early language models also seemed to fail on out-of-distribution tasks, often beaten by simpler methods. What changed? More data, better training objectives, and scale. I think we're at an early BERT moment for cell biology.

LCMs won't model a whole cell anytime soon — the biology is just too complex and our measurements too incomplete. But as tools for learning transferable, generalizable representations of cell state? They're already changing how we do science, and the best is yet to come. 🚀

---

*If you want to dig deeper into how scPRINT specifically fits into this landscape, check out [the paper](https://www.biorxiv.org/content/10.1101/2024.07.29.605556v1) or my other posts on [GRN inference](/PhD/manage-grn-and-what-they-mean/) and [the vision for AI virtual cells](/PhD/about-the-aivc-paper/).*
