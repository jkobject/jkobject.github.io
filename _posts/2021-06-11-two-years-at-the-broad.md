---
title: "2 years at the Broad Institute"
category: "BroadInstitute"
layout: "single"
toc: true
tags:
 - Computational Biology
 - Data Science
 - Associate Computational Biologist
header:
 teaser: "/assets/images/broad_far.jpg"
 overlay_image: "/assets/images/broad_far.jpg"
---

# 2 years at the Broad Institute

The last year was tough. Much tougher for some than others. Here I want to speak about the 2nd year at the Broad and what life was like during this pandemic. 😷

## CCLE part

The Broad continued functioning as fast as ever despite this pandemic. My work was still divided into two groups and research focus. Let's look at the CCLE, also called depmap-omics.

### Making CCLE into a real pipeline

This past year, I managed to convince most of the team to put a lot of effort into making CCLE into a real pipeline. This is something that appeared to me like a very important issue since I was working on the pipeline (see previous CCLE articles: [one-year-at-the-broad](https://www.jkobject.com/blog/one-year-at-the-broad/),[depmap-omics-howto](https://www.jkobject.com/projects/depmap-omics-howto/))

This effort involved doing 4 separate tasks:

1. Finding all our data (bam files) across broad servers and Terra buckets. _This allowed us to realize we were missing a lot of input data for our output data._ :eyeglasses:
2. Creating an MVP database with all available metadata. _This allowed us to realize many missannotation._
3. Rewriting things into a coherent one command pipeline. _This allowed us to find errors in the code and to remove useless blocks._
4. Run the entire pipeline at every release (using call caching when possible).As, before the code was only run on new samples and the output appended to the full dataset (itself likely processed with different versions of the code). _This was truly key in uncovering big mistakes in the code that were not caught before._ ➿

2 more were also key in figuring out issues
5. making cross dataset QCs, spearheaded by James McFarland. ⛔
6. making SNP fingerprinting QCs on our input data, spearheaded by William 

### Issues in the pipeline

Some of the issues we discovered in our data and our code were found at the worst of time, during releases. With multiple ongoing projects, a very long pipeline, the only time I had to work on the pipeline was within releases. Because of that, it was very difficult to neatly separate my work into dev/prod branches. I basically only had the time to do 2 out of 3 key things: 1.improve the prod, 2.test it and 3.run it. ⏲️

In the end, after a year of asking for more involvement in this pipeline, it is finally thanks to a couple big "in release" issues that management woke up to this need. We then quickly got the manpower to work on some of the key improvements needed for this pipeline.

### What is next for productionalization of depmap omics

We now have a couple more things in our list of improvements:

1. making a true DB: a work spearheaded by Phil Montgommery to create an SQL database that would interface with multiple google sheets, python, google cloud and run a set of tests.
2. improving our data onboarding process: Getting data from the sequencing facility and matching it with what we have and the metadata from other groups is still a complex process that needs to be improved. This work is also spearheaded by Phil and could come as part of the DB. 🗳️
3. moving away from the CGA mutation calling pipeline
4. improving QCs: we generate many QC files as part of our analysis pipeline. Parsing and aggregating this into coherent metrics would be very useful.
5. increasing the documentation: for the folder structure, for the functions used and how to use the depmapomics github project.
6. simplifying code tests, using pytests and continuous development tools and good practices.

Knowing that a new goal: "sequencing 10x more data/ cell lines in the coming years" has been set, they will become necessary.

### Figuring out new features to extract

Working on depmap-omics was not only about making the things we already had better. But also creating new tools to extract more features from our sequencing.

We created with Javad an up-to-date [list of features to extract](https://docs.google.com/document/d/1d0dpGI1Ur0KXy9l-YbXzWV6d0CK7htrtNKp-lSSh-Is) that we will want to be extracted from our sequencing in the coming years.

I think that this can be used as an extensive list of what can be done with WG/WE/RNA -seq data. :blue_book:

I was able to start working on some of them in the last year:
- getting WGS CN
- getting Y chromosome WGS
- making SV calls on WES and WGS
- making "germline" mutation calling (SNP, indels) on our cell line for WGS and WES

Some of them were used and QCed by multiple groups at the Broad, often leading to new research. (e.g. [Misek et. al.](#))


### Changing manager

It feels like since I arrived, CCLE was always in a transition period. The manager had just left and his associate too. An interim from another manager was held while we looked for a more permanent manager.

We also changed ops team twice, which meant that twice in two years we reviewed, changed, and made errors because of team onboarding.

I think that this was a true issue as responsibilities were not held and there was no maintained vision for what would be the future of depmap and depmap-omics.

In the end, this vision was maintained by the people that were there since the beginning, even though they are not directly participating in the project. During this second year at the Broad I have spent more than a semester being the main responsible and objective tracking person for the depmap omics pipeline. The data, code, future objectives, management and responsibilities were on me while we waited for the new ops team, new associates and new manager to arrive and get onboarded. :adhesive_bandage:

In the end I think I liked this part. It allowed me to manage this project on my own and learn project management skills that I might not have otherwise.

Unfortunately my role was not meant for it. And I was not able (as described above) to express the needs of the project or be heard in potential issues. Every decision was done reactively once something went way too bad and not proactively following my recommandation. This was my main source of frustration during the last year on CCLE. 🤯

### Celligner

It has now been 2 months that my focus has changed from CCLE to a new project called [Celligner](https://www.nature.com/articles/s41467-020-20294-x). This project was initiated by Allie Warren. 💯

I decided to stay for a third year at the Broad to work on improving Celligner.

The axes of improvements are:

1. Usability (interactive platform, open sourcing, documentation...)
2. Aggregation of more data types (other sample type, other sequencing,...)
3. Algorithm improvement (using VAEs, decreasing memory load...)

A lot of work then, many papers to read and even more ideas. Let's see what we get out of this. 💭

## AMLproject part

As part of my second year in the AMLproject, I have done many more analyses but also had to wrap up what I had done.

### Slam-seq with spike-in

One of the endeavours I had to work on was analysing a data type that had not been produced before. A slam-seq experiment, which is RNA-sequencing where the nascent RNAs are labelled such that all their T nucleotides are transformed into C nucleotides. This forced mutation can be used to differentiate gene expression into transcript being produced currently and transcript produced before. ⏲️ This is to answer the question: are there more transcripts being produced now because of some condition we put the cell in (and differentiate it from secondary effects of co-regulation). 📶 🛑

This was already done before [Muhar et. al.](https://science.sciencemag.org/content/360/6390/800). However we had added spike-in to the mix. This allows us to differentiate absolute amounts of DNA in sample X vs sample Y.

Part of my work was figuring out how to analyse and use Slam-seq data with spike-ins.

### chipMerger

I won't go in the details of the cobinding matrix (which is already explained in the previous documents ([predicting-dependencies-from-enhancers](https://www.jkobject.com/projects/predicting-dependencies-from-enhancers/),[one-year-at-the-broad](https://www.jkobject.com//blog/one-year-at-the-broad/)). We quickly realized that we had to do better with our input ChIP-seq data in order to gain better results 💹. We devised an idea, with Max, to take ChIPseq bed and bigwig files and merge them together, then try to find new peaks under the replicate bigwigs where those peaks were not initially found, using a lower detection threshold than what MACS2 was using. This led to the [CREME algorithm](https://github.com/broadinstitute/genepy/blob/master/genepy/epigenetics/CREME.md).

### wrapping up AMLproject

In research, wrapping up a project means, 
1. setting up enough documentation for other people to take on your work and publishing your code.
2. writing a paper. :book:
3. selecting, improving and commenting figures for your paper. 📈
4. writing the method's section of the paper.
5. publishing and documenting your output data.
6. setting up server (SRA, google cloud, spreadsheets..) to publish your input data, QC and processing

This is what I also spent the last year doing. I also quickly set up a resource website for showing off some interactive plot and easy access to our data. In the meantime I also helped another Associate, Monika, to take on my pipelines and codes in order to continue the research endeavour :microscope: of Maxim Pimkin and Stew Orkin.

## the pandemic

Being away from my family, friends and girlfriend (all living in France), this pandemic was very stressful. After a month of being remote and witnessing border shut downs, 👮‍♂️ I decided to take one of the last planes between the US and europe in order to come to a lock downed Paris to stay with my girlfriend. At that time the Broad was already fully remote and every computational work was maintaining its speed. However, everything else was unknown. How long? How bad? What's next? This situation continued for 4 month. At that time, I had realized the US had shut its border to any non citizen, even valid visa holders, that had been in the EU less than 14 days prior. 🤦

I thought I would wait for this policy to end. But by July, with the first wave of the pandemic being over and almost no cases in the EU, direct entry was still banned for me and everyone I knew. Then started a tiring, stressful, expansive but awesome journey through Yucatan's and its wonders while still working remotely.

Being a European expat 🇪🇺 in the US during this pandemic was extremely tough. The Broad had a no tolerance policy that required me to either lie to everyone in my company whenever I went to see my family or take 2 weeks of unpaid leave for each trip to the EU. In a competitive environment like the Broad, where 4 weeks a year of vacation is a luxury, better say that there was no real choice. In the last year and a half of the pandemic I went back to France 3 times. Always waiting until it became unbearable, then staying long in France still working and then taking 2 weeks (still working) in Istanbul or Cancun before finally making it to the US. Working from France is also tough as my work day was from 1pm to midnight.

Many people around me told me to quit. Many insulted the US, my company, my boss, the pandemic, for what it put me through. What it put us through. I still feel I can't complain too much in the midst of what Covid did to so many others.

## Awards

I was happy to note that thanks to (and also despite) all of this, I received a Broad Spotlight award 🤴 and was promoted to ACB II ✨ (which is at least twice as good a position as ACB I 😂).
