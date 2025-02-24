---
title: "Enrichr, Prerank, GSEA or ssGSEA?"
excerpt: "A quick reminder of when to use which enrichment analysis tool"
category: "PhD"
toc: true
date: 2024-02-19
tags:
 - Comp-Bio
 - Research
header:
  teaser: "/assets/images/enrichment.png"
---

Bioinformatician's main tool for discovery has often been differential expression analysis. But between Enrich, Prerank, GSEA, ssGSEA, which tool should you use? here is the quick reminder X-plainer:

_Enrichr_ is when you just have a list of genes (can be small):

GENEA, GENEB, GENEC

_Prerank_ is when you have values that you can rank your list of genes from:

| Gene  | Value |
|-------|-------|
| GENEA | 12    |
| GENEB | 8     |
| GENEC | 4     |

_GSEA_ works best when you have a list of genes, with values associated with them across multiple conditions (and replicates):

| Gene  | C1 | C2 | C3 | D1 | D2 | D3 |
|-------|----|----|----|----|----|----|
| GENEA | 12 | 7  | 3  | 1  | 1  | 0  |
| GENEB | 8  | 0  | 6  | 8  | 1  | 1  |
| GENEC | 4  | 4  | 3  | 2  | 3  | 4  |

_ssGSEA_ is when you have many values associated with them but not 2 specific condition and want to compare 1 vs the rest

| Gene  | A  | B | C | D | E | F |
|-------|----|----|---|---|---|---|
| GENEA | 12 | 7 | 3 | 1 | 1 | 0 |
| GENEB | 8  | 0 | 6 | 8 | 1 | 1 |
| GENEC | 4  | 4 | 3 | 2 | 3 | 4 |