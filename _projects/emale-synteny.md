---
title: "EMALE genome explorer"
excerpt: "An interactive genome synteny plot in JavaScript and Python."
date: 2026-10-01
tags:
  - genomics
  - JavaScript
  - Python
toc: false
---

[Open the genome explorer](/emale-synteny/){: .btn .btn--primary}

This interactive plot compares six endogenous mavirus-like elements (EMALEs): viral genomes integrated into the genome of the marine flagellate *Cafeteria burkhardae*.

Gene arrows show position and direction. Ribbons connect matching regions between genomes. Other tracks show GC content, terminal repeats, and Ngaro retrotransposon insertions.

You can zoom, inspect genes, filter alignments, reverse or reorder genomes, import your own JSON dataset, and export the plot as SVG or PNG. The app uses JavaScript and SVG, with Python preparing the data. It also works offline.

The example uses the real public data from [gggenomes](https://thackl.github.io/gggenomes/), associated with [Hackl et al., eLife (2021)](https://doi.org/10.7554/eLife.72674). Data and the reference composition are credited to Thomas Hackl and the gggenomes authors.

[Download the app, source, and example data](/emale-synteny/emale-synteny.zip)
