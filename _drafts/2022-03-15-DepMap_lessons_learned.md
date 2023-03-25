---
title: "Lessons learned from large scale genomics projects"
excerpt: "If you are working in data-sciences / genomics and on large-scale projects: This post might be of interest to you."
category: "BroadInstitute"
date: 2021-12-15
tags:
 - Big Data
 - genomics
 - Python
header:
  teaser: "assets/images/caimann.png"
---

If you are working in data-sciences / genomics and on large-scale projects: This post might be of interest to you. Part of my work at the [Broad Institute]() was to take charge of the burgeoning computational pipeline that was DepMap Omics. 

DepMap Omics represents first a big dataset that was made through a multi year project by Mahmoud Ghandi, Bill Sellers, Aviad Tsherniak, Paquita Vazquez and many other collaborators, initially called [CCLE](), or Cancer Cell Line Encyclopedia. It contained multi omics sequencing from aa thousand cancer models such as WESeq, RRBSeq, RNAseq, HybridCaptureseq, RainDanceseq, etc. Some of it was done at the Broad, some elsewhere. This all took years to produce, analyse and publish. It uncovered many key results and new dependencies related to specific cancer genetic features. Unfortunately for me, the paper was already finalized when I arrived.

But something else was also happening in parallel, the new DepMap project was also recently launched and its objective was to create and add as many cell lines as possible and release the viability results of their [genome-wide knockouts/knockdowns]() to the public. 

Obviously, we had to finance all this. How we did it? Well, first using Broad's money, but also using private partners, like many big pharma companies and also tech companies. This is how the DepMap consortium  [(DMC)]() was launched. I won't go into too much details regarding this as I don't know how much can be freely divulged. What was important is that we had now deadlines: release updated datasets every 3 months..

We thus had to transfer a multi year research project composed of many R scripts into a computational pipeline that could load new data, make production level data releases and likely scale to 10x the amount of data. This is when I arrived.

In this lessons learned, I will talk about what we learned in building this large scale multi omics pipeline for target discovery.

1. Data Management
2. Code Management
3. Generating new genomic features

People that have had to do that kind of thing will know the many challenges involved. For others just know that in such a context, you are fighting daily against occam's razor: Any possible bug is going to happen at some point. But I will come back to it, since our first issues was actually: "where is our data"?


## data management

the data had not necessarily been correctly registered after the CCLE2 project and even then most datasets that were easily available were the  processed output matrices. Finding the raw [reads]() became very difficult for some sources and some samples had to be reanalyzed or altogether dropped from subsequent releases due to lack of raw data.

For us the question is how do we move forward and what can we do so that this never happens again?

We did our research and better and better sample management tools have come to life in the recent years. I will list some here that I highly advise to you to look into:
- [xena]
- [gdc]
- [sra]
- [dnanexus]()
- [synapse]()
- [terra]()
- [ega]()

> I am also very eager to learn of other similar tools (feel free to post in the comments).

The tools listed  are the state of the art for genomics data management. But all have flaws. Some of them are for long term storage or only for public access, some of them are made for specific datasets etc..
Thus I will say it is almost impossible to just base the data architecture of your project around only one of them.

What we ended up finding easier is to use a mix of 
- synapse* (for output data management, and sharing output data with the public and within our team). 
- terra for data processing and processing output storage management.
- google cloud storage for longer term storage, larger files and sharing data within our team and collaborators
- sra for sharing data with the public

> * we actually had our own copy cat of synapse internally but for all intents and purposes you can consider it to be like a paid version of synapse.

However, as is often the case in large collaborations, things were more complex. In total, from the onboarding of samples to the data that become available to the public, we actually used many more softwares, all with many interconnections and handled by various teams scripts and cloud functions.

- dozens of google-sheets
- [arxspan]()
- [jirra]()
- [bsp]()

All of them because different teams had different needs for sample metadata management.
What can we do against it?

### sample metadata management

The sooner the better. This is akin to the many efforts of Knowledge Graphs in companies. The goal is that all this knowledge generated about your project, samples or whatever gets put into a relational database.

One way to have that is to ensure that there is a team which goal and responsibility is to build the infrastructure that will interconnect everyone

Some of what we learn here is that there is a few pillars that the database has to have:

1. modular: it needs to be very modular and can be updated easily.
2. reliable: it should almost never break and not for longer than a few hours.
3. queriable: it needs to be queried very simply in python / R and other languages
4. accessible: people should be able to get many important data about the database and to view it as a table. Important data like number of edits, who makes the most edits, what are the possible values for a specific field. 
5. exportable: people should be able to share subpart of the table to others or export it in other formats to others. (csv, spreadsheet, ...)
6. access control: most people should see most of the database. people that generate the data should be able to write on their respective field and be allowed to add new data. New data should be added through a form-like page that verify the entries, explain potential errors and display examples for entries.
7. great access control: this is a management problem too but you do not want people writing new data to spreadsheet and notebooks because they haven't received the right access. You also don't want edits made by anyone. Edits should be allowed to have comments for the db management team to let them know that something like a new field or an additional value needs to be added. Moreover, all or most entries should be well controlled with specific dictionnary (snake_case, no majuscules) and ranges. Last but not least, define a minimum viable set of values for a specific entry, a sample has to have at least these N values or it is rejected. Be uncompromising on these rules. You will be thanked later.
8. ACID, etc: and of course you want all the basics of a database, unique ID (eg. auto increment), atomicity, ...
9. Versionned: if an error is made, one should be able to know who made it, and revert back to previously.


> QUARVA-GAME ? Nah. that sucks.

> it could be a highly engineered google spreadsheet? Nah. Airtable FTW.

a final remark: if possible, connecting overlapping databases from internal or external sources to yours, will be extremely valuable. This allows you to spot issues in your database and more.


### dataset management
  
While small datasets can be put on github or fileshare which both come with a great amount of safeguards and policies on versioning etc.

As long as you do a good enough job of consistently naming and describing your datasets, you should be fine. Ah hem.. __GOOD ENOUGH__

For larger files however, we have mentioned google storage and although many other tools exist I can vouch on the quality and reliability of google cloud. 
_looking at you AWS, please stop becomming the 2000s era microsoft of cloud providers_

However google storage is not helping you that much more and you will want to have internal rules about your dataset.

What you want to think about in advance is:

- versioning: how much, how long...
- access control: who has access (read, write)
- storage class: 

It is quite similar topics to the metadata, except you won't have the ability to be as stringent for large files.

Additional tools in google cloud (e.g. google bigquery) can become of use to you although I haven't made that much of a use from them and won't mention them here.

One remark is that many providers might let you store your data in their handled environment. We have noticed that, for large files, we have almost always returned to a bare bone tool like google storage due to missing functionality in other providers. _looking at you terra.bio_.

Final remark: bam files, vcfs, ... and largely most indexable files can be index-queried directly from google cloud. This is a huge upside that you ought to look into. Especially if you don't know what I am referring to here.

## code management

During the introduction to this lesson's learned blog post I mentionned occam's razor Occam's razor. It is something that I kept thinking about during the time I handled the depmap omics pipeline.

But behind this curse what you ought to think about are things like. How do we prevent the most bugs? how do we onboard new people? how do we make it reproducible for external and internal users? etc.

To some, many of the rules / lessons I will mention here will be basic algorithm engineering and good practices 101. Then maybe what will interest you is what I don't mention. I let you to comment if you think these omissions were important or not. But I believe they are not as important.

- same repo for everyone. In science, big is the drive of many of your teammate to use your code, add / change something to make it better and then never tell anyone about it. Just pressure your peers into pushing their changes. You might have to be lenient on code quality and good practices but it will be worth it.
- once they have done it. And if they start contributing a bit more, you might start to push them to use versioning. "make a few commits along the way and let me know what you are changing". Say it calmly and repeat it as much as needed.

You can then go on and ask for additional work until you feel you are loosing your colleague:

- documentation: add a small description of the functions in the readme, add function documentation in the code, add some examples in the readme....
- test environment / branch: you will have to test it yourself but if there is a few quickly runnable functions with example data, already present in the code, this is a plus. Even better, can this be automated in a CI/CD environment?

Overall a quick and easy way to achieve a good quality pipeline / code / tool for the get-go is to use this template github environment for any new python project (I am sure that an R version exists somewhere): 

https://github.com/rochacbruno/python-project-template

### tools

I have mentioned tools quickly and I won't go into the sterile python/R debate here. Everyone knows python is best, deep down.

No, the question is what tool should you use to pipeline your code, this is a common need in computational biology and elsewhere. Many tools exist but for computational biology I haven't seen much better than:

1. [Terra]()
2. [Snakemake]()
3. [Nextflow]()
4. [Airflow]()

They are not in order of awesomeness but in order of ease of use for newbies. Honestly I would always advice starting with Terra and continuing with something like nextflow or airflow once this is not suiting your need anymore.

Obviously there is thousands: https://github.com/pditommaso/awesome-pipeline 
... but these ones are key.

Similarly whatever language/tool you use, you will have to know that they are actually mostly following the same logic and doing the same thing. And overall, one tool that will be inevitable to know how to use is __docker__. 🙏

## new features

I cannot end this without talking about some more specific lesson's learned we had for depmap-omics, depmap and I believe the field of genomics for (target) discovery.

I believe we have made some strong impact for the community by open sourcing our toolkit and making our data reproducible. However from all the fancy Machine Learning and prediction tools we have tried and designed to make better prediction of gene dependency & cancer targets. Almost everytime, without a doubt, nothing had greater impact than to generate a new genomic feature from our dataset. I think this is a big ML for science lesson's learned for me at least.

I won't go into the details of the specific targets but to give examples of what I am talking about here. Some "new" features and some very new features were:

- getting info about microsattelite instabilities from DNAseq --> lead to the WRN / MSI paper
- associating features based on gene sets, gene proximity, etc.. --> lead to the 2022 VPS4A/VPS4B paper
- getting info about viral infection of the tumor sample.
- getting info structural variants.
- getting info about splicing QTLs.
- getting info about the global functional status of genes (based on CNV/SV/SNPs/ INDELS/ etc).
- ...

