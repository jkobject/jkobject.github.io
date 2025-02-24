---
title: "scDataloader"
excerpt: "An open community tool for AI and scRNAseq"
category: "PhD"
date: 2023-12-29
tags:
 - Big Data
 - AI
 - Python
 - genomics
header:
  teaser: "/assets/images/scdataloader.png"
redirect_to: https://www.jkobject.com/scDataLoader/
---

In my new manuscript scPRINT, I present a tool called scDataLoader 🧬. You can find more details in our [preprint](https://www.biorxiv.org/content/10.1101/2024.07.29.605556v1).

## Origins

Last year, while starting my Ph.D. and after asking many questions on the cellxgene's slack channel, I got contacted by Alex who wanted me to try their new tool: lamindb 👀

LaminDB had many compelling features:
- Management of notebooks, metadata, and runs
- Ontologies of cell types, markers, genes, tissues
- Support for various datasets like anndata, spatial omics, imaging data and more

We discussed my need for a dataloader, which aligned with their thinking and previous work with Ko on anndata dataloaders 🔥

## Why Dataloaders Matter

Recent papers ([paper 1](https://www.biorxiv.org/content/10.1101/2023.10.24.563625v1.full), [paper 2](https://www.nature.com/articles/s42256-023-00757-8)) have shown that scRNAseq training datasets containing many similar cell types can cause imbalance issues for foundation models training and low performance on rare cell types.

For example, if you train a model on 50% images of cars, it might overfit to cars. We wanted to prevent scPRINT from similar overfitting issues 😱

## Implementation

We implemented our dataloader with two key capabilities:
1. Ability to work with any number of datasets and cells
2. Support for weighted random sampling

This implementation builds on lamin's mapped dataset functionality. scDataLoader serves as a wrapper around the mapped dataset tool, providing integration with cell labels, PyTorch and Lightning.

For more information about each component, visit [lamin.ai](https://lamin.ai). I highly recommend checking out lamin's work if you work in computational biology! 💪

## Recent Developments

We recently published a review of dataloaders and mapped collections with interesting findings: [Arrayloader Benchmarks](https://lamin.ai/blog/arrayloader-benchmarks)

Looking ahead, we're excited about developing an interface to work with remote datasets 🚀
