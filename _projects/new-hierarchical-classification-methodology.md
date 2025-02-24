---
title: "A new hierarchical classification methodology"
excerpt: "How to perform classification of structured data like ontologies?"
category: "PhD"
toc: true
date: 2024-12-02
tags:
 - AI
 - Comp-Bio
 - Research
header:
  teaser: "/assets/images/hierarchical-classification.png"
---

As part of my recent paper [scPRINT]( https://www.biorxiv.org/content/10.1101/2024.07.29.605556v1) I stumbled upon an issue leading me to build a new kind of classifier for hierarchical-tree-based labels often defined in ontologies. What am I talking about?

A big issue plaguing the field of cell biology and some others is the lack of common terms to talk about things, like diseases, cells and tissues. Fortunately we now have really good ontologies that define and relate these terms in hierarchical trees: e.g. [CL](https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_1000223)

But how do we make the best use of these for a classifier? In the [cellxgene](https://cellxgene.cziscience.com/) datasets, labels of a [class](https://x.com/jkobject/status/1823263733545611316) come in different precisions, e.g. you might get “neurons” in one dataset, and other datasets you will get “dopaminergic neuron”; “GABA neurons”,…

With my hierarchical classifier, I define a training procedure on a classifier which only predicts the leaf nodes of the ontological tree (the most precise values possible). If the annotated label is something imprecise like “neurons”, the model will still compute a loss on its precise prediction by considering each children labels of neurons as a positive label.

![hierarchical-classification](/assets/images/hierarchical-classification.png)

Lastly note that the training procedure doesn’t just put each children labels to “True” but has to compute the max() over the children labels so as to enforce that the model only selects one label for which it has the most certainty or attribute high certainty to all labels if it doesn’t know which one to choose.

People can use tools like [lamindb](https://docs.lamin.ai/bio-registries) to convert from raw annotations to ontological annotations based on fuzzy matching. They can also use scPRINT to relabel the cells in datasets. For now labels such as cell type, disease, ethnicity, sequencer, sex are available. I will soon add Age and Tissues prediction to this mix.

Some work remain to be done on scPRINT to use its prediction uncertainty to better help labelling of cells and aggregate cell level labels to generate more consistent annotations. Help and PRs are very welcomed: [scPRINT](https://github.com/jkobject/scPRINT)
