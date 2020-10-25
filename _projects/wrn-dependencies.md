---
title: "WRN dependencies"
excerpt: "Repeat expansions confer WRN dependence in microsatellite-unstable cancers"
category: "BroadInstitute"
date: 2020-02-10
tags:
 - Research
 - Broad Institute
 - Cancer Dependencies
 - Genomics
header:
  teaser: "/assets/images/msi.jpeg"
---

A side project that I had the chance to participate in was the WRN dependencies study found in cancer cell lines by the DepMap project.

![](/assets/images/depmap-logo.png)

## Introduction

At the Cancer Program in the Broad Institute, we are working on [cancer cell lines](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cancer-cell-line), cancers from patients that have been grown in a lab for often many years. They now serve as models 👷 to represent a cancer type. 
From these, we use [crispr-cas9](https://www.yourgenome.org/facts/what-is-crispr-cas9), a tool that amongst other things, can serve to deactivate -with relatively good precision- a gene in a cell by cutting ✂️ it in two.
Doing so on hundreds of cance cell lines, the DepMap project has now found many interesting relationships between some cancer models, with particular genomic features and how they react to the deactivation of some of their genes.

_Know 💁 more about the Broad and DepMap, in this related blogpost: [one year at the broad](www.jkobject.com/2020-06-11-one-year-at-the-broad.html)._

Here, we are investigating one specific dependency on the [WRN gene](https://en.wikipedia.org/wiki/Werner_syndrome_helicase).

![](/assets/images/wrn.png)

_the WRN protein._

It is known that for MSI cells, the depletion of the WRN protein induce cell death (or apoptosis).

But first, for a cell to be in [microsatellite instability](https://en.wikipedia.org/wiki/Microsatellite_instability) (MSI) means it is likely to mutate in such a way that some pattern will be replicated many times over. For example, go from $$ATAT$$ say, to $$ATATATATATAT$$. This pattern is due to issues in the cell's mechanism to repair itself when it finds that one strand of DNA 🧬 does not match its counterpart. These problems are often due to mutations or chemicals in the cell's environment. It is known that some cancers are under MSI.

![](/assets/images/msi.jpeg)
_what a microsatellite instability looks like._

To prevent this, cells have an additional unknown mechanism using the gene/protein WRN. 
(genes and proteins are often defined interchangeably in biology as the later is the expression of the other).

We can see that these cells undergo widespread DNA double-strand breaks -meaning the DNA gets split into pieces-, leading to apoptosis. 💀

## Explanation

In this paper: "*Repeat expansions confer WRN dependence in microsatellite-unstable cancers*", we show that when an $$AT$$ repeat occurs in MSI cancer cells, the pattern is so unstable that the repeat will become much longer than what is usually expected from other types of repeat patterns. So doing, the DNA in these regions will fold onto itself and be unable to do its most basic functions, like being read and replicated.

![](/assets/images/msi_mechanism.png)
_how it works._

When this happens, replication proteins will get stalled/stopped 🛑 in these regions, needing help from other proteins to unstall them. Without timely replication, the cell will most often undergo apoptosis. We found that one of these "un-stalling" proteins is WRN. Its goal is to unwind the DNA fold and relaunch transcription. This is done as part of the ATR checkpoint kinase pathway ⤵️.

in biology, a pathway can often be thought of as one (or mutliple) function or program. Taking an input from some other process and doing something, like launching the expression of genes or activating yet other programs 💻.

When this is not done by WRN. Say, because WRN has been disabled by a drug or because it has been mutated in such a way that its function has been lost. Then, the AT-dinucleotide repeats are susceptible to cleavage (or binding) by the MUS81 nuclease.
The MUS81 nuclease is a protein that will bind the folded DNA and cut it. If that happens in many regions of the genome it will cause shattering of the DNA and thus.. cell death.

## Next steps

We were thus able to explain how and why MSI cells will die when WRN is deactivated whereas other "healthy" cells often survive 🤯.
This is another step toward the potential usage of this protein as a target for cancer therapy 🧑‍⚕️.

When we find that a cancer is made of MSI cells, we could be able to design a drug that will bind WRN and prevent it from doing its function, thus creating the chain reaction leading to apoptosis of MSI cells and leaving regular cells relatively untouched. Reducing the amount of cancer cells and potientially curring it.

Read more about this story in our Nature paper: [https://www.nature.com/articles/s41586-020-2769-8](https://www.nature.com/articles/s41586-020-2769-8).