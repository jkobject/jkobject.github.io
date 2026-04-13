---
title: "scPRINT-2"
excerpt: "scPRINT-2"
category: "PhD"
toc: true
date: 2025-12-20
tags:
  - PhD
  - Comp-Bio
header:
  teaser: "/assets/images/scprint2.png"
---

After having built [scPRINT]() there was many things that we wanted to do both on scPRINT and on foundation models in general. One of the more "applied math" direction ended up being merged with stuff we wanted to do with scPRINT, mostly for the sake of fit with the initial Ph.D. topic, see [Xpressor]().

Regarding scPRINT, I still had a list of 10+ elements that I wanted to improve and at least as many things I wanted to test, whether on the benchmarking, architecture, training, encoding, etc..

And while it started being just this list of things, it ended up looking like a benchmark of componnents. I then decided to also test many of the classical features of scFMs to create out additive benchmark presented in scPRINT-2.

From the benchmark and results on some other tests, I built scPRINT-2. It was much harder than planned, because many features ended up interacting poorly with one another or when scaling the model learning would cause issues. One particular difficult one ended up being the use of ESM3 embeddings without gene locations. This caused the model to diverge somehow.

Other issues regarded scale:

1. when going from 50 to 350 millions cells, even storing the index became an issue, doing it across GPUs too.
2. when going from 40,000 genes to 300,000, the same thing happened, that meant a large matrix to store in the model.

Basically I broke it all multiple times.
