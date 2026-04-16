---
title: "Finishing the PhD"
excerpt:
  "2.5 years, two labs, one foundation model, and a defense. Here is what I
  learned."
category: "PhD"
toc: true
date: 2026-05-01
tags:
  - PhD
  - Comp-Bio
  - Foundation Models
header:
  teaser: "assets/images/photo-pasteur.jpg"
  overlay_image: "assets/images/photo-pasteur.jpg"
---

It's done. March 25, 2026, 1:30pm, Duclaux amphitheater at Institut Pasteur. 🎓

I started in October 2023. Took 2.5 years instead of two. Here's what happened.

## What I set out to do

The project was building foundation models for single-cell transcriptomics —
taking the pretraining ideas from NLP and applying them to gene expression at
scale. The goal: a model that could infer gene regulatory networks, classify
cell types zero-shot, denoise expression, and actually be useful to biologists.
Not just publishable, usable.

%% WIP$$$ 


I was split between two labs:
[Laura Cantini](https://research.pasteur.fr/fr/team/machine-learning-for-integrative-genomics/)
at Institut Pasteur (computational biology, gene networks) and
[Gabriel Peyré](http://www.gpeyre.com/) at ENS (applied mathematics, optimal
transport). Two very different worlds, two sets of expectations, two weekly
meetings.

Outside the lab, I wanted to keep training — endurance sports had become
important to me during this period, and I wanted to see more of the world while
I could.

## What I did

### The papers

The thesis produced three papers:

**scPRINT**
([Nature Communications, 2025](https://www.nature.com/articles/s41467-025-58126-9))
— a large cell model trained on 50M+ cells for gene network inference. Novel
gene tokens from ESM2 protein embeddings, learned expression tokenization,
genomic positional encoding. State-of-the-art on GRN inference benchmarks,
zero-shot cell type classification, denoising. Code at
[github.com/cantinilab/scPRINT](https://github.com/cantinilab/scPRINT).

**Xpressor** — a cross-attention architecture for learning across biological
scales. The idea: compress gene-level representations into cell-state vectors,
and fine-tune protein language models using cellular tasks. Improved cell-type
prediction (+28%) and embedding quality (+8%) over standard architectures.

**scPRINT-2** (in revision, Nature Methods) — trained on 350M cells from 16
organisms, 25 TB of data. 42-model ablation study to figure out what actually
matters in scFM design. 75% zero-shot cell type classification on OpenProblems
(up from 47% with scPRINT-1). State-of-the-art denoising, batch correction,
cross-species generalization, counterfactual generation.

### The tools

Seven Python packages released:
[scPRINT](https://github.com/cantinilab/scPRINT),
[BenGRN](https://github.com/jkobject/BenGRN) (GRN benchmarking),
[GRnnData](https://github.com/cantinilab/GRnnData) (gene networks in AnnData),
and more for data processing, evaluation, and model serving. Everything
open-source under GPL-v3.

<!-- TODO: add the full list of packages with links -->

### The conferences

<!-- TODO: fill in the full list — Jérémie should add the specific conferences -->

Over a dozen conferences and workshops across Europe and beyond. Oral
presentations, poster sessions, invited talks. Each one forced me to sharpen the
story and meet people working on adjacent problems.

### The outreach

I mentored a student during the PhD. Wrote blog posts (you're reading one), made
videos, gave talks to non-specialist audiences. I think this kind of work
matters — it's how ideas spread beyond the 50 people who read your paper.

### The people

The labs at Pasteur and ENS. Jules Samaran, Remi Trimbour, Geert Huizing at ENS.
Alex Wolf, Sergei Ribakov, Brice Rafestin for software help. The Nucleate
community, Whitelab Genomics, Blossom, dot Omics, Biographica. A lot of people
made this work possible.

### Outside the lab

I trained for and ran a medium triathlon, a half-marathon, the Mont-Blanc trail,
and the Paris Marathon. Traveled to the UK, Portugal, Spain, Guadeloupe,
Vancouver, Thailand. I needed this. Long runs are good for thinking, and getting
away from the screen makes you come back sharper.

## The defense

March 25. Pasteur, Duclaux amphitheater.

I was stressed. I'd prepared well, but defending years of work in one afternoon
is a strange exercise. You try to make it look like everything was planned from
the start, when in reality half of the good ideas came from accidents.

The jury was rigorous but fair. Hard questions in the Q&A — the kind that make
you think, not the kind designed to trip you up. That's what makes a defense
feel worth it.

Having my mentoree there meant a lot. And the next week, I finished a marathon.
Different kind of endurance, same feeling at the end.

## What I learned

How to write papers. How to think about research impact beyond citations. How to
set goals when nobody is setting them for you.

The research community matters more than I expected. Not just for collaboration
— for sanity. The conferences, the DMs, the random conversations at poster
sessions.
[Open source](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/)
is how you actually have an impact: if scPRINT is useful, it's because people
can use it.

Technically: a lot about transformers, diffusion models, optimal transport, the
math of self-supervised learning. But also about the gaps — the missing data,
the incomplete benchmarks, the things we still don't know how to measure
properly.

Company research and a PhD are different. The PhD gave me time to go deep, be
wrong for months, follow a thread until it broke or became a paper. I wouldn't
trade that.

## What's next

I'm not going back into academia. Never planned to. 🚀

I'm thinking of building **Jouvence** — a company using AI and biology to extend
healthy human lifespan. The thesis work on foundation models, gene networks, and
cellular representation is directly relevant: if you can model how cells work
and how they break, you can start to intervene.
<!-- TODO: add 2-3 sentences about Jouvence's approach, from Notion pages -->

I'm also looking at companies working on similar goals: longevity, disease
modeling, AI-driven high-throughput data generation. Places like Lilas
Bioscience and Xaira Therapeutics are doing interesting work in this space.

Lots to do.

---

The full arc:
[the PhD decision](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/),
[a year in](https://www.jkobject.com/blog/a-year-in-the-phd/), and now this.

Thanks to Laura, Gabriel, Juliette, my family, and everyone who was part of the
last 2.5 years.
