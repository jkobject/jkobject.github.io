---
title: "AUPRC vs AP: Evaluating Binary Classification"
excerpt: "A deep dive into classification metrics and their nuances"
category: "PhD"
toc: true
date: 2024-06-09
tags:
 - Data-Science
 - Research
header:
  teaser: "/assets/images/auprc2.png"
---


When analysing a classification task for my recent paper [scPRINT](https://www.biorxiv.org/content/10.1101/2024.07.29.605556v1), I fell into a fascinating "data-sciency" rabbit-hole about AUPRC, AUC and AP.

## Understanding Classification Metrics

When evaluating a binary classification model that outputs probabilities or has internal regularization, we need ways to assess its performance across different decision thresholds.

![Classification Example](/assets/images/auprc1.png)

### ROC Curves
One common approach is plotting the ROC curve, which shows the tradeoff between true positive and false positive rates. The area under this curve (AUC/ROC-AUC/ROC/AUROC) is a popular metric:

![ROC Curve](/assets/images/auprc2.png)

### The Need for Precision
However, in some cases like predicting graph edges in sparse gene networks, precision becomes crucial. AUROC can miss important information about optimal cutoff points. 🚫

![Precision Example](/assets/images/auprc3.png)

### AUPRC and Its Challenges
This is where AUPRC (PR-AUC) becomes valuable, focusing on precision and recall:

![AUPRC Curve](/assets/images/auprc4.png)

However, AUPRC comes with its own challenges: ⚠️

1. Random precision baselines differ between tasks, making direct comparisons difficult
2. Jagged results require careful sampling of PR curves 😟
3. In gene network inference, many links lack prediction values, requiring special handling 🔥

## Introducing rAUPRC

To address these limitations, I developed rAUPRC, which includes:
- Correction for random precision
- Proper handling of incomplete predictions
- A modified approach for drawing the curve from partial to complete recall

## Average Precision (AP)

AP is computed as:

![AP Formula](/assets/images/auprc5.png)

While AP is often recommended for skewed classification tasks, my rAUPRC implementation showed more consistent results across different parameters in practice.