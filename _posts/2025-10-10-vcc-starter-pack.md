---
title: "VCC starter pack"
excerpt:
  "If you do data science and machine learning, here is everything you need to
  know to get started on the Arc virtual cell challenge."
category: "PhD"
toc: true
date: 2025-10-10
tags:
  - AI
  - Comp-Bio
  - Research
header:
  teaser: "/assets/images/starterpack.png"
---

To start the VCC, you need to know a few things. This is your starter pack:

![image of a starter pack](/assets/images/starterpack.png)

The main packages for single cell data analysis are **scanpy** - **anndata** -
**pertpy:** with many other easy to use packages being part of the
**[scverse](https://scverse.org/)** ecosystem. In addition, both RNA-seq, csv,
and image datasets management across thousands of datasets is enabled with
**lamindb**.

To get started there is a couple nice tutorials in the packages referenced above
as well as some tutos
[here](https://open.substack.com/pub/surajparmar/p/from-molecules-to-matrices-part-1),
and [here](https://huggingface.co/blog/virtual-cell-challenge) that are must
reads!

**For further readings:**

I will shamelessly plug my paper and package
[scPRINT](https://www.nature.com/articles/s41467-025-58699-1) to understand
where we are at with single cell foundation model. I will also mention the
[state](https://arcinstitute.org/news/virtual-cell-model-state) model that is
the first to delve a lot into perturbations and how to do multiple cells at a
time contrary to most other methods.

A key perturbation method that is not foundation model based is
[GPO-VAE](https://academic.oup.com/bioinformatics/article/41/Supplement_1/i599/8199372),
which encompasses very similar idea to **scVI, cradle-VAE**, **GEARS**,
**chemCPA**, **Biolord**, **[txpert](https://arxiv.org/pdf/2505.14919)**, **[LPM](https://www.nature.com/articles/s43588-025-00870-1)**

Many of these tools and others have been benchmarked in a few papers:

1. [A Systematic Comparison of Single-Cell Perturbation Response Prediction Models](https://www.biorxiv.org/content/10.1101/2024.12.23.630036v2.full)
2. [Benchmarking AI Models for In Silico Gene Perturbation of Cells](https://www.biorxiv.org/content/10.1101/2024.12.20.629581v2.full)
3. [Benchmarking algorithms for generalizable single-cell perturbation response prediction](https://www.nature.com/articles/s41592-025-02980-0)

But we know already that many of the previous losses used to train models and
assess them on perturbation data suffered from issues as presented in this
paper: [mode collapse in current models](https://arxiv.org/abs/2506.22641) and
this [paper](https://www.nature.com/articles/s41587-025-02777-8). This is also
because current perturbation dataset are very noisy.

**Things that many people don’t say and that should be our theory when designing
the models:**

1. Many perturbations do nothing.
2. Many other perturbations kill the cell (but we don’t know it) and the readout
   is just really poor quality stuff because of it, or cells that survived
   somehow..
3. Many perturbations have very similar phenotypic effect. Triggering something
   like what happens when the cell has an issue in its genome.
4. Moreover the RNA-guides used to decide which region of the genome is
   perturbed have very different effect due to something called off-tagerting
   which was extensively studied and corrected for in the DepMap project.
5. Most datasets are super sparse (only some genes perturbed), or only a couple
   cell lines, and often low depth.

Fortunately, we have depmap and LINCs/L1000. which are genome-wide perturbations
in thousands of different cell models with guide-effect analysed However, while
some of them have 1000 genes assessed post perturbation most of the data is only
wether the cells died or not post perturbations. but we NEED to use this dataset
somehow. This in addition to what we learned above will be differentiating
factors. Another very similar
[dataset](https://www.nature.com/articles/s41467-019-13805-y) done by Sanger on
the same set of cell lines and using very similar guides also exist and has many
similarities and some differences with depmap.

Additionally, an image-based dataset also exist, made by Recursion called
[RxRx](https://www.rxrx.ai/). But it is using similar guides / molecules and
cell lines that depmap and Sanger are using!

Arc hasn’t released the guide sequences yet but we might infer it. we know also
the genetic sequence of the cell line. We also know about the novel ideas for
creating better losses. Now how would we do it well?

Finally to know more about ideas for the future of this field, please read the
2024 markov bio
[blog post](https://www.markov.bio/research/mech-interp-path-to-e2e-biology),
which I agree a lot with.

Many perturbation datasets are easily available on lamindb's own database
[here](https://lamin.ai/laminlabs/pertdata), plus
[depmap](https://www.depmap.org/) (where you will need both the genedependency,
expression, guide efficacy, and model files) and [LINCS](https://clue.io/) (see
the download instructions below).

## Outline of a project

1. get the lamindb and add all other datasets we need (depmap, lincs, xaira,
   ...) (3 weeks)
2. generate a good set of train/val/test datasets to test some hypothesis (more
   data, variability, adding chemical perturbation, multiple species, guide
   information, phenotypic only …) (3 weeks - 2 months)
3. reimplement all the scoring metrics used in previous papers
4. Define a MIN and MAX (MAX = subset of perturbed cells, same results from
   another dataset) (MIN=unperturbed cells, a linear model, a simple random
   forest, a gene embedding KNN model, ChatGPT, ...)
5. answer some questions on identifiability, quality, and information content:
   1. can we find perturbations that have no impact on cell state (might need to
      compare to average of perturbations) (1 week)
   2. can we find perturbations that have the same effect? (cell death, growth
      arrest, …) (1 week)
   3. what does correcting for off-targeting do in perturb-seq?
   4. how much more predictive accuracy do we get from using a depmap / rxrx /
      10 genes / 1000 / ... for different modalities, what information is only
      available in one of them? (3 months)
6. looking at the benchmarking, get the best performing and/or simplest
   VAE-based architecture (1 week)
7. retrain it and test if adding more data, changing the losses, or other
   parameters improve the model, check how much using LINCS & Depmap help (3
   months)
8. simple fine-tune of scPRINT with this data (1 month)
9. use a simple random forest model on crafted features to predict the
   perturbation and see how it does (1 month)
10. use a groundtruth dataset (literature and correlation (GENIE3)) to predict
    the perturbation and see how it does (1 month)
11. going further by mixing ideas of GPO-VAE to scPRINT in pseudo-bulk mode (3
    months)
12. going further by mixing ideas from STATE to scPRINT (3 months)

## other useful dataset ressources

- [VCC's datasets](https://virtualcellchallenge.org/datasets)
- [https://github.com/Peekxel/PRISM](https://github.com/Peekxel/PRISM)
- [CZI's genome scale perturb seq](https://virtualcellmodels.cziscience.com/dataset/genome-scale-tcell-perturb-seq)
- [Ginkgo's dataset](https://thevirtualcell.com/)
- [Millya's current challenge](https://www.kaggle.com/competitions/echoes-of-silenced-genes/leaderboard)

Another large dataset of perturbation, including some "unintended" double KO are
available in iPSCs thanks to XAIRA, called
[orion](https://plus.figshare.com/articles/dataset/Processed_data_for_X-Atlas_Orion_Genome-wide_Perturb-seq_Datasets_via_a_Scalable_Fix-Cryopreserve_Platform_for_Training_Dose-Dependent_Biological_Foundation_Models/29190726),
with a
[similar dataset](https://www.biorxiv.org/content/10.1101/2024.11.28.625833v1)
published by the sanger institute.

Some dual guide KO was also done in colorectal cancer (CRC)
[here](https://www.nature.com/articles/s41467-025-67256-9#Abs1).

### LINCS download:

`wget https://s3.amazonaws.com/macchiato.clue.io/builds/LINCS2020/level5/level5_beta_all_n1201944x12328.gctx`

`wget https://s3.amazonaws.com/macchiato.clue.io/builds/LINCS2020/siginfo_beta.txt`

`wget -r ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742_Broad_LINCS_gene_info.txt.gz`

`wget -r ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742_Broad_LINCS_sig_info.txt.gz`

`wget -r ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/GSE92742_Broad_LINCS_sig_metrics.txt.gz`

### Companies to whatchout for their perturbation datasets

- recursion
- xaira
- tahoe
- arc
- illumina
  ([yes indeed](https://www.illumina.com/company/news-center/press-releases/2026/fda84c92-b4b3-4691-a402-35555abe8605.html))
- cellular intelligence
- czi
- retro bio
- ginkgo

## EDIT: post VCC's feedbacks

interestingly, post VCC, it seems that many people that did not knew much about the data (icluding the organizers?) learnt a lot about things that had been published months, even years ago... This is great, because it still means that many people know learned collectively, we are at a better place now than before. We could have gotten there more efficiently of course.. I adviced to read some of the blog posts published by contenders on the topic:

- [regression model ftw](https://blog.turbine.ai/p/how-did-we-get-a-regression-model?hide_intro_popup=true)
- [the VCC diary](https://gmdbioinformatics.substack.com/p/arc-virtual-cell-challenge-my-diary)
- [the VCC metrics issues](https://giovannipalla.substack.com/p/virtual-cell-perturbation-metrics)
- [are we just modelling cell's fingerprints](https://newsletter.kiin.bio/p/arc-institutes-virtual-cell-challenge)

One thing that I find regretful is that no famous published models have been implemented openly to check for their abilities on this benchmark.