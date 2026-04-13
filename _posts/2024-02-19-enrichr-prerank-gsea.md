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

Bioinformatician's main tool for discovery has often been differential expression analysis. But between Enrichr, Prerank, GSEA, and ssGSEA, which tool should you use? Here is the quick reminder X-plainer. 🧬

## The Decision Tree

The key question is: **what shape is your data?**

---

### Enrichr — you have a gene list, nothing else

_Enrichr_ is when you just have a list of genes (can be small). No values, no conditions — just names. 📋

```
GENEA, GENEB, GENEC
```

Under the hood, Enrichr tests each gene set in its databases using a **Fisher's exact test** (hypergeometric). It asks: is my list enriched for genes in pathway X more than expected by chance?

Best for: DE gene lists, hit lists from CRISPR screens, manually curated sets.

👉 [Enrichr](https://maayanlab.cloud/Enrichr/) | Python: [gseapy.enrichr](https://gseapy.readthedocs.io/en/latest/)

---

### Prerank — you have a ranked gene list

_Prerank_ is when you have a continuous value per gene that you can rank — a fold change, a correlation, a t-statistic, anything. 📊

| Gene  | Value |
|-------|-------|
| GENEA | 12    |
| GENEB | 8     |
| GENEC | 4     |

Prerank runs GSEA logic (the enrichment score / walking statistic) on your pre-ranked list, without needing raw expression data or phenotype labels. Useful when you already have a score but not the underlying samples.

Best for: correlation with a phenotype, output from another model, single-sample pseudo-bulk scores.

👉 Python: [gseapy.prerank](https://gseapy.readthedocs.io/en/latest/)

---

### GSEA — you have expression data with two conditions

_GSEA_ works best when you have a matrix of gene expression values across multiple samples with a clear phenotype label (treated vs control, disease vs healthy, etc.). It computes its own gene ranking internally. 🔬

| Gene  | C1 | C2 | C3 | D1 | D2 | D3 |
|-------|----|----|----|----|----|----|
| GENEA | 12 | 7  | 3  | 1  | 1  | 0  |
| GENEB | 8  | 0  | 6  | 8  | 1  | 1  |
| GENEC | 4  | 4  | 3  | 2  | 3  | 4  |

The key advantage over Enrichr: GSEA doesn't require you to define a hard cutoff ("top 200 DE genes"). It uses the full ranked list and identifies pathways enriched at the top or bottom. This makes it more sensitive and less arbitrary. ✅

Best for: bulk RNA-seq, any two-condition comparison with replicates (n ≥ 3 per group recommended).

👉 [GSEA software](https://www.gsea-msigdb.org/gsea/index.jsp) | Python: [gseapy.gsea](https://gseapy.readthedocs.io/en/latest/)

---

### ssGSEA — you want a per-sample enrichment score

_ssGSEA_ is for when you have many samples with no clear two-group contrast — or when you want a continuous enrichment score *per sample* rather than a comparison between groups. 🗂️

| Gene  | A  | B | C | D | E | F |
|-------|----|----|---|---|---|---|
| GENEA | 12 | 7 | 3 | 1 | 1 | 0 |
| GENEB | 8  | 0 | 6 | 8 | 1 | 1 |
| GENEC | 4  | 4 | 3 | 2 | 3 | 4 |

Each sample gets its own enrichment score for each pathway, independently. The output is a sample × pathway matrix. Great for downstream analysis — clustering, survival analysis, correlating pathway activity with other variables.

Best for: large cohorts (TCGA, GTEx), single-cell pseudo-bulk, any analysis where you want pathway activity as a continuous feature.

👉 Python: [gseapy.ssgsea](https://gseapy.readthedocs.io/en/latest/)

---

## Quick summary table

| Tool | Input | Statistics | Best for |
|------|-------|------------|----------|
| **Enrichr** | Gene list only | Fisher / hypergeometric | Small lists, no values |
| **Prerank** | Genes + score | GSEA walking statistic | Pre-computed rankings |
| **GSEA** | Expression matrix + 2 conditions | GSEA walking statistic | Bulk RNA-seq DE |
| **ssGSEA** | Expression matrix, no labels | Per-sample enrichment | Large cohorts, per-sample scores |

For most single-cell work: compute pseudo-bulk, run GSEA or Prerank per cell type. For single-cell pathway scoring directly, [decoupleR](https://decoupler-py.readthedocs.io/) is worth a look. 🔍
