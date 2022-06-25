---
title: "genepy"
excerpt: "An open community tool for genomics."
category: "BroadInstitute"
date: 2022-03-15
tags:
 - Big Data
 - genomics
 - Python
header:
  teaser: "/assets/images/genepy.jpeg"
---

If you too, want to do computational biology but have a strong opinion about R. You have come to the right place.

When I arrived at the [BroadInstitute](https://www.broadinstitute.org/) in early 2019, I quickly realized that my goal of doing python at work was in jeopardy.

## what is going on

![](/assets/images/whatgoingon.jpeg)

Everyone was working in R. The justification was simple, everything is made in R, the plots, the differential expression tools, the "Granges", "limma"s and other "seurat"s were all in R.

My first instinct was.. -to run, obviously, quit my job and become a data scientist in neuro-marketing at Uber or-     to finally learn R.

However, after some time, I decided to see it as an opportunity.

After a quick lookout on github for nice genomic centric packages, I figured that whatever I use, a lot of "pretty basic" code was not available. This actually looked ok since, looking at the genomics community overall, people were fine writing these "pretty basic" functions over and over!

## Lazyness

![](/assets/images/lazyme.gif)

But I am lazy. If I am going to make all this work better to functionalize and save it for later. This is how I ended up creating a genomics python tool: [genepy](https://github.com/broadinstitute/genepy). Something filled with simple code for a lot of repetitive computational biologist tasks.
Is it complete? Is it easy to use?
Likely not. But I haven't seen that being the case for a lot of other bio informatics anyway. 

If this all seems like the most basic thing you have ever heard in CS.. Welcome to computational biology, you are certainly a lost react.js developer.

> But why Genepy?

It was initially named "[JKBIO](https://github.com/jkobject/JKBio)" (in my personnal github). It then became a BroadInsitute repository and got renamed into [genepy](https://github.com/broadinstitute/genepy). for .. Gene + python. and the famous [genepi](https://en.wikipedia.org/wiki/G%C3%A9n%C3%A9pi) drinks from the Alps.

Throughout my 3 years at the Broad I kept on using this tool again and again. I created many dozens of functions and kept most of the tool maintained. It is now used by at least 5 persons, but I would love to see it take its own wings and fly away to the community. So if you are a computational biologist in any way. Feel free to have a look, write your own set of tool, add your own functions and make tons of pull requests!

It already has pretty general functions such as nice interactive plots for CNVs, scatter plots... Functions to merge genomic regions, to do differential gene expression ([DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html), GSEA,..) in python, to work with ChIPseq data, to work with super resolution-microscopy data, etc.

Have a look and tell me what you think!

Cheers,

PS: you are looking for it? [GENEPY](https://github.com/broadinstitute/genepy)
