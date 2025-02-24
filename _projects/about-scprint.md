---
title: "scPRINT"
excerpt: "Going more in depth about lessons learned in building large cell models"
category: "PhD"
toc: true
date: 2025-03-05
tags:
 - PhD
 - Comp-Bio
header:
  teaser: "/assets/images/scprint.png"
---

The goal of this project presentation is not to go through the details of the projects. Everything can be found in the paper: [scPRINT: a large cell model to predict and explain single-cell gene expression](https://www.biorxiv.org/content/10.1101/2024.09.10.556945v1), the [preprint](https://www.biorxiv.org/content/10.1101/2024.09.10.556945v1) and the [code](https://github.com/jkobject/scPRINT).

No instead, I want to talk about scPRINT in a way we don't do in papers, present it as a story and talk about the lessons learned that I might not have put as much emphasis on in the paper.

If you want to know more about scPRINT feel free also to check out my presentations at the [LoGG](https://www.youtube.com/watch?v=s9_DZz9E1To&t=1645s) or at the [scVerse](https://www.youtube.com/@scverse) community meetings.

## Why scPRINT

- some explaination in my previous post [The PhD Decision](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/)
- we need to use all the data we have at our disposal to learn about the cell for example the diverse set of cell types and their gene networks
- we need to understand and validate the claim that initial models have made
- there are so many improvements one can think of
- we need to make them more easily accessible to the community
- models couldn't do anything zero shot
- models were not really benchmarked and compared to SOTA
- 

## How it was built

- initially wanted to directly use scGPT and maybe make a few updates
- then realized that it was very hard to update, the code was not great and the reproducibility was not there
- so we decided to do it from scratch
- implement many ideas and try things out:
  - create / add a dataloader
  - training modalities as denoising, cell type prediction
  - 

## What it can do

- predict cell types, diseases, tissues, age, sex, sequencer, ethnicity for any given cell type in a zero shot manner (without fine-tuning)
- predict a genome-wide gene network for a cell or a set of cells in a zero shot manner (without fine-tuning)
- denoise the expression of any given cell zero shot (meaning, it can in silico increase the library size of the data)
- create embeddings of cells in a low dimensional space that is concept-specific (e.g. cell type embedding, tissue embedding, disease embedding, etc.)
- recreate a counterfactual expression profile given an embedding

## what about gene networks

- issues in the way we think about gene networks:
  - the cell is not a network but a complex system
  - being able to predict networks of size 10-50 nodes defined with simple ODEs is nothing related to what happens in the cell
- issues in the way we work with gene networks and represent them.
- created GRnnData, which builds on top of AnnData and allows for the efficient storage and manipulation of gene networks
- created BenGRN, which is a set of 4 different tasks, 5 metrics and many datasets to benchmark the performance of GRN models from single cell RNA-seq data

## Interesting things I learned

### for foundation models

- the data quality and amount is the bottleneck
- models seem to finish training before havin seen the whole dataset. Meaning there is not much more to learn after a certain point?
- 

### for gene networks

- We notice that applying the z-scoring makes DeepSEM considerably better at predicting networks on omnipath but worse for the McCalla et al. and genome-wide perturb-seq networks. This impact of z-scoring on predicting network is a trend that we have also seen with other models, like GENIE3. One possible reason why z-scoring could align predicted networks to the Omnipath ground truth is that Omnipath contains a quantity of lower quality connections extracted from early cancer cell line array expression datasets. There, many housekeeping genes are connected together and while often not predicted well based on MSE.
- GENIE3 with many more trees and cells This slightly degrades the model performance by around 20% but allows us to run all our benchmark on our cluster in a few hours rather than multiple days (see Table S4).
- What about even more cells and more trees? we tried, the run never finished
- Interestingly we have noticed that in some cases, taking the sum of the attention matrices over cells makes the Geneformer network much more in line with the ground truth. We expect this result as Geneformer only connects genes that are expressed in the same cell. Doing this thus artificially increases the score of edges when the genes were expressed in the same cell, adding a correlation bias to the networks.
- see my rant about GRN [on X](https://x.com/jkobject/status/1831989215485169762)

### others:

- different gene embeddings models and their impact on the performance of scPRINT and their patterns 
- AUPRC vs AP [on X](https://x.com/jkobject/status/1830966823229313109)

## What is next?

- working with Open Problems to push what I have learned and improve / add some benchmarks
- digging deeper into some ideas and issues in scPRINT ()
- working on some updates and fine-tuning strategies to imrpove scPRINT
- designing more flexible Transformer architectures