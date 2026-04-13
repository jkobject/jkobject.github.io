---
title: "Finishing the PhD"
excerpt: "2.5 years, two labs, one foundation model, and a defense. Here is what I learned."
category: "PhD"
toc: true
date: 2026-03-01
tags:
 - PhD
 - Comp-Bio
 - Foundation Models
header:
  teaser: "assets/images/photo-pasteur.jpg"
  overlay_image: "assets/images/photo-pasteur.jpg"
---

It's done. On March 25, 2026, I defended my PhD at ENS. 🎓

I started this in October 2023 with [four goals](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/): do it in two years and be prepared, make as many connections as I can, maximize impact on the community, and enjoy it as much as possible. I ended up taking 2.5 years — not two — but looking back, I think I held the line on the other three pretty well.

This post is a retrospective. What happened, what I built, what I struggled with, and what I'm walking into next.

## What I built

The core of my thesis was [scPRINT](https://github.com/cantinilab/scPRINT): a large pre-trained transformer for single-cell transcriptomics. The idea was simple in principle and extremely hard in practice — take the ideas that had worked so well in NLP (pretraining on massive unlabeled data, then fine-tuning on downstream tasks) and apply them seriously to gene expression data at scale.

scPRINT was published in **Nature Communications** in 2025. That felt like a major milestone. Seeing it in print after years of wrangling datasets, debugging attention layers, and writing response letters was genuinely satisfying. 🙏

The second paper, **scPRINT-2**, is currently in revision at Nature Methods. It goes further — better architecture, broader benchmarks, more biological insights baked in. I'm proud of it. It will come out.

Beyond the two main papers, I built tooling, presented at over a dozen conferences and workshops, and tried to make every piece of the work usable by the community — not just publishable.

## Two labs, two PIs

My setup was unusual: I was split between [Laura Cantini's group](https://research.pasteur.fr/fr/team/machine-learning-for-integrative-genomics/) at Institut Pasteur and [Gabriel Peyré](http://www.gpeyre.com/)'s group at ENS. That's two labs, two cultures, two weekly meeting schedules, and two sets of expectations to manage.

Honestly? It was one of the richest parts of the experience. Laura brought deep biological grounding and a very direct, no-nonsense style of scientific feedback. Gabriel brought mathematical rigor and a kind of elegant skepticism that forced me to really understand what I was doing. The combination made me a better scientist than either lab alone would have.

But it was also genuinely hard. Being a full member of neither lab has a loneliness to it that's hard to explain. You are always a little bit a guest. You hold context that no one else fully shares. And when things are slow or unclear, there is no natural anchor.

## The hard parts

I won't pretend it was all great. A few things I found genuinely difficult:

**The administration.** PhD paperwork at French institutions is its own special adventure. Between Pasteur's admin, ENS's admin, and the doctoral school coordinating between both, I spent more hours than I care to count on forms, attestations, and bureaucratic loops that had nothing to do with science. 

**The solitude.** [I wrote about this after year one](https://www.jkobject.com/blog/a-year-in-the-phd/). It didn't get easier. Doing research means spending a lot of time alone — debugging, reading, thinking. When experiments don't work and papers are in revision and you can't tell if you're making progress, the isolation gets heavy. The communities I built around me — the people at Pasteur, at ENS, at conferences — were what kept me going.

**Knowing when to stop.** A foundation model is a bottomless pit of possible improvements. I could have kept iterating on scPRINT forever. Learning to say "this is good enough to ship" — and meaning it — was one of the hardest things I had to internalize.

**The pressure of two simultaneous timelines.** One paper in Nature Comms, one in revision at Nature Methods, while also preparing the actual manuscript and defense. The last few months were a juggling act I would not want to repeat. ⚡

## The defense itself

March 25. ENS, rue d'Ulm.

I won't over-dramatize it — I had prepared well, and the jury was rigorous but fair. There's a strange feeling to defending years of work in a single afternoon. You have to hold the whole arc of the project in your head — the original intuitions, the detours, the things that didn't work, and the ones that did — and present it as if it was all obvious from the start.

What I remember most is the Q&A. Real questions, hard ones. Questions that made me think. That's what makes a defense feel worthwhile. Not the ritual, but the sense that serious people took the work seriously.

> "The goal of a PhD is not to become a PhD. The goal is to learn how to do research."

Someone told me that early on. I think it's right.

## What I learned — beyond the science

A few things I'll carry forward:

**Autonomy is a skill you have to develop.** No one tells you what to do during a PhD, which sounds like freedom and feels like vertigo for the first six months. Getting comfortable with self-direction — setting my own objectives, deciding when something is done — was the most transferable thing I learned.

**Community is infrastructure.** The conferences, the collaborations, the DMs with people working on similar problems — these are not distractions from the work. They are part of the work. Ideas move through people.

**Open source is how you have an impact.** I [wrote about this before](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/), but doing it for 2.5 years only reinforced it. If scPRINT is useful, it's because people can actually use it. Every hour spent on documentation and APIs is an investment in impact.

**Being a researcher at a company and being a PhD student are different things.** Both are valuable. The PhD gave me something I couldn't have gotten any other way: the space to go deep, to be wrong for months, and to follow a thread until it either broke or became a paper.

## What's next

I'm not going back into academia. I never planned to. 🚀

The mission that's been forming for years is now crystallizing: I want to use AI and biology to extend healthy human lifespan. Not marginally. Significantly. I believe this is one of the most important problems of our time and that we're close enough to the necessary tools that it's time to go build something.

That means starting a company. That means going back to the US, probably. It means bringing together the foundation model work, the biological intuitions, and the product-first mindset I built at Whitelab and Broad — and pointing all of it at aging and disease.

There is so much to do. I'm impatient to start.

---

If you want to read the full arc: [the PhD decision](https://www.jkobject.com/blog/the-phd-decision-grn-foundation-model/), [a year in the PhD](https://www.jkobject.com/blog/a-year-in-the-phd/), and now this.

Thank you to Laura, Gabriel, and everyone who worked alongside me these last 2.5 years. It was worth it.
