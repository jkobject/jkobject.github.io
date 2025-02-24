---
title: "Ancestry Bias in CRISPR Screens"
excerpt: "How we discovered ancestry biases in CRISPR screens and published in Nature Communications"
category: "PhD"
toc: true
date: 2024-06-21
tags:
 - Comp-Bio
 - Research
 - CRISPR
header:
  teaser: "/assets/images/ancestry.jpeg"
---

# Ancestry Bias in CRISPR Screens

🎉 Thrilled to share our paper on ancestry biases in CRISPR screens published in Nature Communications! This work, led by Sean Misek, reveals an important discovery about potential biases in CRISPR screening technology. You can read the full paper here: [https://www.nature.com/articles/s41467-024-48957-z](https://www.nature.com/articles/s41467-024-48957-z)

## How It Started

🧐 While working in the Cancer Data Science group, I was exploring ways to extract interesting new features from our CCLE omics dataset that might reveal relationships between cancer vulnerabilities and genetics.

💡 One unexplored avenue was computing not just the cancer mutations in our cell lines, but also the germline mutations. The reasoning was twofold: some mutations might have been wrongly categorized as somatic, and we know there exist many germline mutations that can lead to cancer.

🔒 However, this idea faced some initial resistance as team members were concerned about releasing potentially identifiable patient-related data.

## The Discovery

🚀 Despite the pushback, I decided to implement the germline analysis pipeline and generate the data while awaiting the final decision on its release. Fortuitously, Sean Misek, a postdoc at the Broad, approached us with the same idea, wanting to use germline mutations for GWAS analysis.

🕵️‍♂️ Sean's analysis revealed surprisingly strong associations, but with genes completely unrelated to cancer. The breakthrough came when we examined how CRISPR guides were overlapping with these high association SNPs. We discovered that these SNPs were preventing the guides from binding to their target regions, creating false non-essentiality results. Even more significantly, when examining ancestry data we had recently computed, the affected cell lines were predominantly from patients of African descent.

## Impact

🤩 What started as a search for new cancer targets led to the discovery of a significant bias in our CRISPR guide library affecting 1-2% of the guides. This finding has now been incorporated into our CRISPR dataset and has important implications for ensuring more equitable and accurate research outcomes.

This project represents a true scientific journey - starting from an initially contested idea, leading to unexpected results, and culminating in an important discovery that helps address representation issues in cancer research. 🌍