---
title: "A year at the Broad Institute"
category: "BroadInstitute"
layout: "single"
toc: true
tags:
 - Computational Biology
 - Data Science
 - Associate Computational Biologist
header:
 teaser: "/assets/images/yearbroaad.jpg"
 overlay_image: "/assets/images/yearbroaad.jpg"
---

I have to say that when I had planned this article, I was not expecting the craziness of the next 6 months.
I have now spent 1.5 years at the Broad. But 6 of them have actually been remote and back in France. I now expect to spend the entirety of this second year, remote.

I am thus going to talk about the first non-remote, pre-Covid year.

## Finishing onboarding.

I was warned that the onboarding might last a couple of months. Being a foreigner did not help and I can finally say that now, a year later, I feel fully onboarded to the Broad and the Cambridge way of life.

> _Cambridge way of life often implies, amongst other things: Grocery shopping at union square market, getting a couple of doughnuts at Union square doughnuts. drinking fancy beers at remnant, lamplighter or  . Asking people if they are doing a post-doc or a phd the first time you meet. Getting your baguette at Tate and enjoying the many ice creams cambridge has to offer_

What takes so long. Well except getting up to speed with the lab's specific softwares and technologies. Getting a sense of the myriads of projects ✨ and collaborations happening around you. its getting to know the history of projects that came before you, reason for things. **It's getting to know power dynamics!** 💖 It is soo important to know the power dynamics. I really feel that this is when you know you are on board.

This is when you know you have been onboarded. When you know what actions you can do andd what actions you can't. Then you know how to navigate.

And last but not least. Once you get your routine. Waiting for the CC&E meetings (cell circuitry and epigenomics), the [MIA talks](https://www.youtube.com/watch?v=MKD1ScU_XJs&list=PLlMMtlgw6qNjROoMNTBQjAcdx53kV50cS) (models, inference and algorithms) 👍.

Once you are onboarded this is also when you start getting ideas for projects you could launch and whom to collaborate with.

## What I have done

During this year I have been able to present papers and lead team meetings.
I have been able to present my research during the yearly Broad research conference.
A 3000 people event gathering all imaginable research in molecular biology 🤯.

I was also able to interact with many teams across the broad for small projects. helping them solve issues or helping me to solve issues.

As you may know from other posts: _see [AML project](https://jkobject.com/projects/predicting-dependencies-from-enhancers/), [depmap omics](https://jkobject.com/projects/depmap-omics-howto/)_  I am the principal bio-informaticist of two main projects. One at the Broad and one at the Dana-Farber Cancer Institute.

But I was also able to have a smaller participation in some side projects (side projects for me :wink:) regarding specific cancer dependencies.

### Diversity of Projects

One of them was focused on the WRN dependency in MSI cancers. see [wrn dependencies](https://jkobject.com/projects/wrn-dependencies/), and one was on the VPS4A dependency in VPS4B deficient cancers. see [vps4a dependency](). These projects were driven primarily by biologists and experimentalists. They came to us because they needed some additional computational analysis.

Once the goal fo the projects understood, this was "fairly trivial" analysis, wrapped up in less than 2 weeks. What takes 90% of my time are the two main projects.

For the first 8 months of my time I was also involved in revamping [CCLF](https://cellfactory.broadinstitute.org/)'s computational pipeline. I also layed down a first SOP and road-map for the data processing and release 💪.

### CCLE

For CCLE, a set of circumstances made it so that I ended up being the only computationalist on the project during a period of 10 months. Hopefully Neekesh Dharia, my mentor at the time was able to provide the biology intuition in all of that. I went on to maintain, QC and productionalize the pipeline. My main focus was on the reproducibility. It quickly appeared that none of what we were producing could be reproduced by anyone. Even ourselves. We had to work with many people from [GtEX](https://gtexportal.org/home/), [CGA](https://www.broadinstitute.org/cancer/cancer-genome-computational-analysis), [DSP](https://www.broadinstitute.org/data-sciences-platform), [GP](https://www.broadinstitute.org/reading-and-editing-biology/genomics-platform).. At the end, I layed down a plan taking from everything We have learnt along the way.

#### CCLE: Main Issues

The two major issues faced in our work now has been on the data sharing process. Even cell lines, released at this scale, need to have a regulatory framework built around them. issues are mostly around pseudo-somatic[1] and [germline](https://en.wikipedia.org/wiki/Germline_mutation) mutations and which ones can be released to whom, and how?

The second one is mainly regarding the size of the project. This is project is between a large science experiment and a fully fledged product. The amount of users that we have and the sensitivity of their projects make any of our changes have big consequences downstream for a lot of human cancer research\*. 😑

This entails that any changes we want to make need to be carefully reviewed and thought about. This makes for a lot of frustrations. Things can be slow. Mistakes & non optimal decisions can live on for much longer because the effort needed to change them become very high. ⬆️

\* _I think that we all take this pressure, at depmap, fairly well. This drives us to put the best of ourselves while still being ok with our mistakes. We know that everyone makes mistakes and that the state of genetic cancer research and computational biology as a whole, does not reach anyone's expectations, yet._

#### CCLE: What is to come

Most of the main objectives are still works in progress. We are in the work of hiring a new ACB to take on most of the workload around improving, productionalizing and running the pipeline itself. :construction:

More recently, we have recently switched to WGS -whole genome- data which required us to rethink the flow data architecture.

My main focus ↘️ for the coming month will be to have it in a good state of documentation and to have clearly layed down SOPs and directions of improvements for the new ACB -entry level computational biologist-.

I will also soon start to focus full time on a machine learning project (undisclosed for now), related to CCLE and Dependencies.

### AMLproject

Here we are working mainly with very deep sequencing of a handful of cell lines under many different conditions 🌪️. The dynamics are very different: 

- we are pursuing a very specific goal 🥅 in understanding a biological phenomena.
- we are all young scientist learning as we go and doing more cutting edge experiments (and thus, analysis)
- reliability and efficiency is really a side goal (until it can't be).
- many many different types of experiments of various quality exist.

We have now almost proved what we need to in order to publish this work in a high tier journal. Maxim Pimkin has really been the master mind 🔦 behind everything related to the biology in this project. His intuition 💭 has led most of our decisions, which also a big difference compared to CCLE. Other very talented people have worked hard on this project. But I like to think of myself as the lead computational biologist.

#### AML: Main Issues

Something that is notoriously hard in a project, is to work with low foresight. Here each new experiments would trigger new unforeseen ones. 
In code there is two ways to do things: 🧑‍🏭

- iteratively: 1version 2nd version etc.. --> going toward a metric of quality
- in one go: you have to build something and you build it block by block

Here we did the first one, however we never know what the next version would be and we would go as much toward an improved version as toward version with new functionalities.

This takes obviously, time. Each version is also very specific toward one specific thing. Transmitting this information and approach was particularly hard to biologist. They often expect the later. It is also hard to estimate the time things will take. A very similar experiment could run much faster than a slightly different one for example.
A marginal amount of work on a first experiment could save countless hours in the coming ones, etc..

> A very similar experiment could run much faster than a slightly different one for example.

Interacting across disciplines is hard but leads to some of the best projects and we could see some examples here. :sparkles:

#### AML: What is to come

During this project we have discovered many interesting properties of the leukemia regulatory circuitry. We have also discovered interesting features of [slam-seq](https://www.lexogen.com/slamseq-metabolic-rna-labeling/) ⏲️. We want it to become an additional side -letter format- paper. Moreover we have left open many biological questions.

One of our Main objectives is quite similar to CCLE's. We need an additional ACB which will learn from me and learn how to use my pipelines. This will also free me from wrapping up some analysis and thinking more about the paper and how to better release the code. 📈

But I want to also try and be able to finish our analysis of large scale [Transcription factor](https://en.wikipedia.org/wiki/Transcription_factor) co-binding. 🎇

Let's meet in a month to see how things turned out! :wave: 

---
[1] I call pseudo-somatic, [somatic](https://en.wikipedia.org/wiki/Somatic_mutation) mutations in cell lines as they are somewhat more losely defined than somatic in cancer tissues, they regroup immortalizing mutations -due to the process of [immortalizing a cell line](https://en.wikipedia.org/wiki/Immortalised_cell_line), [private](https://www.medicinenet.com/script/main/art.asp?articlekey=5048) snps and cancer mutations that also exist as germlines.
