---
title: "Lessons learned from large scale genomics projects"
excerpt: "If you are working in data-sciences / genomics and on large-scale projects: This post might be of interest to you."
category: "BroadInstitute"
date: 2022-03-15
tags:
 - Big Data
 - genomics
 - Python
header:
  teaser: "assets/images/depmap-lessons.png"
---

If you are working in data sciences / genomics and on large-scale projects: This post might be of interest to you. Part of my work at the [Broad Institute](https://jkobject.com/blog/2021-06-11-two-years-at-the-broad) was to take charge of the burgeoning computational pipeline that was DepMap Omics 🏋️.

DepMap Omics represents first a big dataset that was made through a multi-year project by Mahmoud Ghandi, Bill Sellers, Aviad Tsherniak, Paquita Vazquez, and many other collaborators, initially called [CCLE](https://sites.broadinstitute.org/ccle/), or Cancer Cell Line Encyclopedia. 📚 It contained multi-omics sequencing from aa thousand cancer models such as WESeq, RRBSeq, RNAseq, HybridCaptureseq, RainDanceseq, etc. :sweat_drops: Some of it was done at the Broad, some elsewhere. This all took years to produce, analyze and publish. It uncovered many key results and new dependencies related to specific cancer genetic features. Unfortunately for me, the paper was already finalized when I arrived.

But something else was also happening in parallel, the new DepMap project was also recently launched and its objective was to create and add as many cell lines as possible and release the viability results of their [genome-wide knockouts/knockdowns](https://depmap.org/portal/) to the public. 🗣️

We had to finance all this. How did we do it? Well, first using Broad's money, but also using private partners, like many big pharma companies and also tech companies. 🤑 This is how the [DepMap consortium (DMC)](https://depmap.org/portal/home/#/depmap-consortium) was launched. I won't go into too many details regarding this as I don't know how much can be freely divulged. What was important is that we had new deadlines: release updated datasets every 3 months...

We thus had to transfer a multi-year research project composed of many R scripts into a computational pipeline that could load new data, make production-level data releases, and likely scale to 10x the amount of data. This is when I arrived.

In this lesson learned, I will talk about what we learned in building this large-scale multi-omics pipeline for target discovery.

1. Data Management
2. Code Management

People that have had to do that kind of thing will know the many challenges involved. For others just know that in such a context, you are fighting daily against Occam's razor: Any possible bug is going to happen at some point. But I will come back to it since our first issue was actually: "Where is our data?"

> "Where is our data?"

## Data management

the data had not necessarily been correctly registered after the CCLE2 project and even then most datasets that were easily available were the processed output matrices. Finding the raw reads (i.e. the sequencing fastq files) became very difficult for some sources and some samples had to be reanalyzed or altogether dropped from subsequent releases due to lack of raw data.

For us, the question is how do we move forward and what can we do so that this never happens again?

We did our research and better and better sample management tools have come to life in recent years. I will list some here that I highly advise you to look into:

- [xena](https://xenabrowser.net/)
- [gdc](https://portal.gdc.cancer.gov/)
- [sra](https://www.ncbi.nlm.nih.gov/sra)
- [dnanexus](https://www.dnanexus.com/)
- [synapse](https://www.synapse.org/)
- [terra](https://terra.bio/)
- [ega](https://ega-archive.org/)

> I am also very eager to learn of other similar tools (feel free to post in the comments).

The tools listed are the state of the art for genomics data management. But all have flaws. Some of them are for long-term storage or only for public access, some of them are made for specific datasets, etc.
Thus I will say it is almost impossible to just base the data architecture of your project around only one of them.

What we ended up finding easier is to use a mix of
- __synapse__ (for output data management, and sharing output data with the public and within our team).
- __terra__ for data processing and processing output storage management.
- __google cloud storage__ for longer-term storage, larger files, and sharing data within our team and collaborators
- __sra__ for sharing data with the public

> We had our copycat of Synapse internally but for all intents and purposes you can consider it to be like a paid version of Synapse. 🚀

However, as is often the case in large collaborations, things were more complex. In total, from the onboarding of samples to the data that become available to the public, we actually used many more software, all with many interconnections and handled by various teams scripts and cloud functions.

- dozens of google-spreadsheets 🤮
- [arxspan](https://arxspan.com/)
- [jirra](https://www.atlassian.com/fr/software/jira)
- [bsp](https://www.broadinstitute.org/files/shared/biosamples/ISBER_Mahan_2008.pdf) <- a broad internal tool like arxspan.

All of them were because different teams had different needs for sample metadata management.
What can we do against it?

### sample metadata management

When? The sooner the better. This is akin to the many efforts of Knowledge Graphs in companies. The goal is that all this knowledge generated about your project, samples, or whatever gets put into a relational database.

One way to have that is to ensure that there is a team whose goal and responsibility is to build the infrastructure that will interconnect everyone

Some of what we learned here is that there are a few pillars that the database has to have: 🗽

1. __modular__: it needs to be very modular and can be updated easily.
2. __reliable__: it should rarely break and not for longer than a few hours.
3. __queriable__: it needs to be queried very simply in Python / R and other languages
4. __accessible__: people should be able to get many important data about the database and to view it as a table. Important data like the number of edits, who makes the most edits, and what are the possible values for a specific field.
5. __interoperable__: people should be able to share subparts of the table to others or export it in other formats to others. (CSV, spreadsheet, ...)
6. __findable__: most people should see most of the database. people that generate the data should be able to write on their respective fields and be allowed to add new data. New data should be added through a form-like page that verifies the entries, explain potential errors, and display examples for entries.
7. __access controlled__: this is a management problem too but you do not want people writing new data to spreadsheets and notebooks because they haven't received the right access. You also don't want edits made by anyone. Edits should be allowed to have comments for the DB management team to let them know that something like a new field or an additional value needs to be added. Moreover, all or most entries should be well controlled with specific dictionaries (snake_case, no majuscules) and ranges. Last, but not least, define a minimum viable set of values for a specific entry, a sample has to have at least these N values or it is rejected. Be uncompromising on these rules. You will be thanked later.
8. __ACID__, etc: and of course you want all the basics of a database, unique ID (eg. auto increment), atomicity, ...
9. __Versionned__: if an error is made, one should be able to know who made it, and revert to previously.

> If you could see the [FAIR principles]() in here, good job. If you couldn't please look at the link it will be better explained than I could.

a final remark: if possible, connecting overlapping databases from internal or external (interoperable) sources to yours, will be extremely valuable. This allows you to spot issues in your database and more. We have been able to greatly improve ours this way. :medal:

### dataset management

While small datasets can be put on GitHub or Fileshare which both come with a great number of safeguards and policies on versioning etc.

As long as you do a good enough job of consistently naming and describing your datasets, you should be fine. Ah hem... __GOOD ENOUGH__ 🥉

For larger files, however, 🧬 we have mentioned Google storage and although many other tools exist I can vouch for the quality and reliability of google cloud.
_looking at you AWS, please stop becomming the 2000s era microsoft of cloud providers_ #unpopular-opinion

However, google storage is not helping you that much more and you will want to have internal rules about your dataset.

What you want to think about in advance is:

- __versioning__: how much, how long...
- __access control__: who has access (read, write)
- __storage class__: how often do you want to access the data, how fast do you want it to be, and how much are you willing to pay?

> However these decisions tend to become more automatized nowadays.

It is quite similar topics to the metadata, except you won't have the ability to be as stringent for large files.

Additional tools in google cloud (e.g. google big query) can become of use to you although I haven't made as much use of them and won't mention them here.

One remark is that many providers might let you store your data in their managed environment. We have noticed that, for large files, we have almost always returned to a bare-bone tool like Google storage due to missing functionality in other providers. _looking at you Terra.bio_. 🔍

__Final remark__: bam files, vcfs, ... and largely most indexable files can be index-queried directly from google cloud. This is a huge upside that you ought to look into. Especially if you don't know what I am referring to here.

## code management

- same repo for everyone. In science, big is the drive of many of your teammates to use your code, add / change something to make it better and then never tell anyone about it. Just pressure your peers into pushing their changes. You might have to be lenient on code quality and good practices but it will be worth it.
- once they have done it. And if they start contributing a bit more, you might start to push them to use versioning. "make a few commits along the way and let me know what you are changing". Say it calmly and repeat it as much as needed.

You can then go on and ask for additional work until you feel you are losing your colleague:

- documentation: add a small description of the functions in the readme, add function documentation in the code, and add some examples in the readme...
- test environment / branch: you will have to test it yourself but if there is a few quickly runnable functions with example data, already present in the code, this is a plus. Even better, can this be automated in a CI/CD environment?

Overall a quick and easy way to achieve a good quality pipeline / code / tool for the get-go is to use this template Github environment for any new Python project (I am sure that an R version exists somewhere): [https://github.com/rochacbruno/python-project-template](https://github.com/rochacbruno/python-project-template)

### tools

I have mentioned tools quickly and I won't go into the sterile python/R debate here. Everyone knows Python is best, deep down.

No, the question is what tool should you use to pipeline your code, this is a common need in computational biology and elsewhere. Many tools exist but for computational biology, I haven't seen much better than:

1. [Terra](https://terra.bio/) <- the easiest one
2. [Nextflow](https://nf-co.re/)
3. [Snakemake](https://bio.tools/snakemake)
4. [Airflow](https://airflow.apache.org/) <- the most generalist one

They are not in order of awesomeness but in order of ease of use for newbies and of how generalistic they are. Honestly, I would always advise starting with Terra and continuing with something like NetFlow or airflow once this is not suiting your need anymore.

Obviously, there are thousands: https://github.com/pditommaso/awesome-pipeline
... but these ones are key.

Similarly, whatever language/tool you use, you will have to know that they are actually mostly following the same logic and doing the same thing. And overall, one tool that will be inevitable to know how to use is __docker__. 🙏

During the introduction to this lesson's learned blog post, I mentioned Occam's razor Occam's razor 🪒. It is something that I kept thinking about during the time I handled the depmap-omics pipeline.

But behind this curse what you ought to think about are things like. How do we prevent the most bugs? 🐛 How do we onboard new people? How do we make it reproducible for external and internal users? etc.

To some, many of the rules / lessons I will mention here will be basic engineering and good practices. Then maybe what will interest you is what I didn't mention. I leave you to comment if you think these omissions were important or not. 📝