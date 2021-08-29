---
title: "Reproducibility in Biology"
excerpt: "When do we decide an experiment has failed/succeded and when does it becomes cherrypicking?"
category: "Scientific Method"
date: 2021-07-31
tags:
 - Computational Biology
 - Data Science
 - Research
header:
 teaser: "/assets/images/pipetting_bio.jpg"
---

# Reproducibility in biology - bioinformatics research

Having now worked for more than 2 years in a research environment and having been very sensitive about good, reproducible and open science. I have seen from large group computational labs and small group bench labs the issues and reasoning that might lead to unreproducible science. 🧑‍🔬

First, this is not a denunciation of any malevolent act. Non-reproducibility in biology is the norm and up to 70% of researcher admit having published unreproducible results [1](https://www.nature.com/articles/533452a) as you will see, my standards are very high as I come from an engineering background. 🧑‍🏭

I have also come to grips with the inherent difficulty in day to day bench life, to not end up with very strong bias and cherry picking. 🧪

## Not controlling all parameters

A first basic and irresolvable issue in biology is not being able to control all/most parameters. This has a tremendous impact on the possible results of an experiment. Given the results & the available control parameters, the researcher's conclusions can often be way too optimistic and misleading. 🎇

However, new companies and research institute's organizations are emerging, making what I would call Experiment as a Service :office:, where some key and tortuous steps of experiments are taken care of by experts in this part, which make sure of removing all known biases and human errors 🤖.

Expanding these to many experiments in biology and chaining providers, might allow reproducibility to dramatically increase.

## Removing failed experiments vs data selection

> When do we decide an experiment has failed/succeeded and when does it become cherry picking?

I have seen this issue first hand in my colleagues' decisions over selecting or not some data. 🍒 It appeared to me that __2 simple rules__ can be defined. They are based around the idea that _discarding an experiment/datapoint should be hard_.

1. __error attribution__: A failed experiment is only so when a failure reason has been given and shown. A wavy hand explanation cannot be ground to removing an experiment.
2. __replicate atomicity__: Given that replicas are done with the exact same process. One cannot select a replicate or remove some replicates from its results. _3 good replicates_ is a minimum for an experiment.


> when should I choose quality or quantity?

I often hear this debate or this notion around me in non-scientific circles mostly. Because from my current experience it really feels as if they are both feeding each other.

1. Without quality, the results of the many experiments and many replicates won't make sense. It is useless to go big when the quality standard has not been met. :yin_yang:

2. Without the quantity of replicates, it is impossible to set criterion for quality and reproducibility standards. Only repeating processes over and over can let you find out if the process is right and holds up to repetition and changes in conditions that are not accounted for. ☯️

`quality -> quantity -> quality -> quantity`

## Editors & reviewers role

> when is it showcasing a nice image and just proving a point without actual statistical significance?

I love cool pictures, I think they really help alleviate the reading burden of a paper. However, they can't be used to prove a point. But they have.. And in the research field any cool plot (however dry-looking) can be that image (no significance but convincing at first sight). If one does not have the data and code to investigate and reproduce it, it does not weigh that much for your hypothesis, it is as best a good idea to try again entirely. 🎱

Some of the blame has to be on the reviewers to just allow researchers to not publish their code and their data. This is not only about asking the researchers whether they have done it or not. It is about it being part of the reviewing. A reviewer has to try to run the code :bar_chart: that made the plot using:
 A. the data and
 B. a piece of code that did it.
Why would anything be allowed if this one simple 10mn check fails? What does it say about the rest of the research? :3rd_place_medal:

### Better standards

Yes a big part is about better standards 🎯 for code and data. Some more ideas such as:
1. requiring data QC as part of data upload.
2. requiring environment and package information as part of the code (docker image, requirements.txt, ...)
3. requiring not only the basic input data (e.g. fastqs) but the processed parts and processing pipeline too (e.g. bam files, big wigs, matrices). 💾 

This is a week worth of a computationalist' time (provided he did his job right). _And it is worth it 100 times_.

### Paper/Project bashing

In biology, more than other fields it seems, there is a harshness in what makes it out.

First, it is apparently very hard to get a grant to do something that another researcher already did. So much for reproducibility... (although this one can be "easily" by-passed, as one kinda does whatever he wants with his grant money).

Second, it is very hard to publish a paper that does not contain a certain amount of novelty. And this amount gets higher for better journals. You need to do something more. One can confirm or refute a previous paper in part B of its own paper. but part A,C,D, abstract, title, conclusion need to be about this novelty, new proof, etc. 💯

This paper bashing appearing at multiple levels is mainly the fault of the science enablers, reviewers, granters, editors... They want to be part of a science that will lead to citations basically.

> We need incentives for reproducing.

One maybe simple change on the side of publishers would be to make room for a great "related paper" section. One that really shows the many articles on topic A based on the paper's contents.

A final one is a paper aggregation service. For a specific topic, say: "ZMYND8 is a target in AML" would compile all 70 papers on the subject: Same for any research topic one can think of.

### Accepting imperfection

Another issue I have seen also related to paper bashing is the stringency of reviewers. No research is perfect, there might be some failed QC data, there might be some poorly commented code. Some missanotation, even some lost files (as long as they were not needed to prove a point in the paper). Reviewers need to be more accepting of imperfection regarding this additional data 📁 that is shared by researchers. Everything is imperfect and being too harsh on imperfections leads researchers to decide to entirely not release that information so that everything appears perfect on the first pass but then, under the hood, nothing can be reproduced.. 🤦‍♂️

I hope I laid down some issues, reasons and solutions for them and that in the future we will strive toward more reproducibility and, let's say out out loud! More fully open access, open review, free review journals. :crossed_fingers:
