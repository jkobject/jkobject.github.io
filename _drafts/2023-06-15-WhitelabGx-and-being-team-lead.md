---
title: "My Work at Whitelab and Creating a Team"
excerpt: "I have jointed an AI Biotech startup for CGTs in Paris. See my experience here"
category: "Other Work Experience"
date: 2023-06-15
tags:
 - Big Data
 - genomics
 - Python
header:
  teaser: "assets/images/whitelabgx.jpeg"
---

After a very deceptive end of the year, I decided I wanted to take a month or so to get my thoughts in order. To relax and find some peace with what had happened. :peace:

However the day following my departure I was already looking at companies and contacting labs. 📱 I was in this state where the only thing that could make me feel better was to look at the future and the possibilities. 💭

But it was still tough mentally, I was thinking about the option of going back to the Broad Institute. "Would it be hard? Should I go now? Would it be the easy way out? What about my apartment, my girlfriend? etc." I felt like a way out, like cowardly going back "home" 🏠 after a failed attempt.

I had, fortunately, all the support I could need.

It actually only took a week or so before I got replies. One coming from Deep Life and one from WhitelabGx.

I ended up being offered positions, but the choice was easy. DeepLife's management seems to have a few red flags 🟥 in their behavior during my couple of meetings. After my previous experience, this is something I was now much more sensitive to. I was not really able to see these before.

Whitelab on the other hand was very welcoming. Excited about my profile and offered me a very rewarding position, especially compared to DeepLife. I would be a team lead in Computational Biology :muscle:. Here I saw how much my previous experience was valuable as I felt I was now much more able to see in between the lines during recruitment processes. Not what people say, but how they behave, what they offer, and the way they do it. Doing so I could also see the tremendous difference between how companies can see or not someone's value and potential:moneybag:.

In a way, it is like friendship. It is a matter of taste, need but most of all serendipity.

On the surface, the position looked a lot like what I had been told at Aqemia (although not really offered). But here, the team was already there waiting for me and the objectives were clear. 🥇

## the environment

Many things were green flags 🟩 for me. The company was actually thinking of itself as a Biotech, the CSO was a biologist with experience. They had an HR manager. They also had a team of biologists and both the CEO / CSO were very honest, aware of what they didn't know, and were very open to my suggestions and ideas.

The place itself was a brand new incubator 👀 called Future4Care. As nice as Broad and less than 10 minutes from my place.

Every member of the team was nice and welcoming. It was small, however: 20 people.

The goal of WhitelabGx is to build a platform to help develop, de-risk, and fasten the preclinical phase of novel cell and gene therapies. The idea is to use ML and data science to drive the discovery, experimental design, and so on 📈.

Especially after getting experience in small molecule preclinical development, I could see the huge potential of CGTs in their precision compared to regular small molecules. I also believe strongly that many diseases will only be cured through the use of CGTs. Finally, it is also a nice experience to add to my resume.

## Disclaimer:

Why am I doing that?

It is simple: I strongly believe in openness and honesty and I think the world is a better place every time someone speaks freely and openly about subject matters that have been kept behind closed doors.

I am talking here about my sole experience at WhitelabGx. With the management of 2023. This is just one point of view at one specific moment in time. I also have my own values and reference frame. Please do not use anyone's past experience to judge a current company on this account and do your own due diligence.

Because of the nature of the subject and with respect for anyone currently working at WhitelabGx, I will keep this post private for now. If you are interested in reading it, please send out an email and I will send it to you.

But I might at least let you know about what WhitelabGx was very open about as of the end of 2023:

- Whitelab has a culture of kindness and honesty.
- Almost everyone is staying in the company after their trial period.
- Whitelab is largely composed of people with past experience in research, biotech, and biology.
- Whitelab is very diverse, exactly half of the company is non-french. with people coming from all over the world. The culture is very American.

## the work

My goal was to build both a team, a pipeline, and a product. The team was composed of 2 computational biologists. But I quickly realized that I would have to do more than that.

Effectively, I was the sole person in Whitelab with extended knowledge of computational biology. 🧑‍⚕️

I would describe this knowledge as mainly knowing well the current sequencing tools, processing & analysis tools, and the datasets. Knowing their advantages and issues. Knowing where the field is going and sensing the bullshit from the true science.
I think this is what differentiates me 4 years ago from what I know and what differentiates a computational biologist with experience from one without.

So I had effectively created the entire roadmap given the vision that David & Julien had 🔍.

Sure! Here's the text with emojis added:

The vision itself is one in progress but I could sense the idea of using ML to drive as much of the experimental design of the preclinical cell therapy discovery as possible. ✨🔬

They had already a sense of what were the best tools nowadays for such an endeavor. 🛠️🌟

They had envisioned 2 products for the CB team.

1. The Atlas 🌐
2. The Knowledge Graph 📚🧠

For the Atlas, they were talking here of something that would contain a data modality for all tissues in the human body. The initial goal was to be able to do one thing: 📊🧬

1. Find proteins that would be on the surface of one tissue and not rest. 🧪🎯

For the Knowledge Graph, the idea was more murky but the idea was that much information was available already in papers, in databases, and in the heads of the scientists. I was actually initially told to disregard this part as it was not a priority anymore.

After lots of research, some iterations, meetings with clients, and internal debates. I ended up presenting my proposition to the leadership a month after I arrived: 💼🗣️📅

First, the knowledge graph and the atlas were to be merged into one product. To query omics data, one needs good metadata. Omics data output will also be likely considered metadata. 🔍📊📈

Then the product being very complex, it will be divided into 5 parts:

1. The scAtlas 🧫🌍
2. The bulkAtlas 📊🌍
3. The intelAtlas 🧠🌍
4. The metaAtlas (knowledge graph) 📚🌍
5. The AtlasApp 📱🌍

From this, we could do a couple of things: 💡🔍

1. Find novel targets (target discovery) by comparing diseased and healthy phenotypes and e.g. finding genes that are differentially expressed in the disease. 🎯🧬
2. Assess model quality: analyze and compare model transcriptome and response to the original tissue transcriptome. 📊🧪
3. Find transcripts associated with proteins that could be on the surface of one tissue and not the rest.
4. Design a better payload based on the target, its expression, and the predicted promoter that is mostly activated in the cell type of interest.

In order to do that I would help myself with a few famous Databases and tools: 🛠️📚

1. CellxGene -> This is the backbone of the Atlas, used in most parts of it. From its databases to its processing pipelines and the technologies used to build it. The AtlasApp would stem entirely from it. 📊🧬📱
2. TCSA -> This is a multi-database knowledge base with the addition of an ML predictor, to assess the probability for a protein to be a surface receptor and its druggability. 📚🔍💊
3. Gget -> Used to query our main databases from chembl to uniprot, pubmed, ensembl, pdb etc. 📊🔍🔬
4. Scanpy -> Used to process the data and to build the Atlas. 📊🔬
5. Nextflow + GCP -> Used to store all of our datasets and to run our premade pipelines to process our supported sequencing technologies. ☁️📊🔬
6. Foundational models -> Not included in the first part, they would be used to become the core ML model representing the Atlas, they would synthesize the knowledge contained in the Atlas and the Knowledge Graph. Predicting cell types, correcting batch effect, missing genes, allowing us to query unseen conditions, etc. 🤖🔍🧬

The knowledge graph in itself would be in name only as we have realized that there is not an urgent need to create a graph database for now. For an MVP, tables and query tools would be enough.

Moreover, we have seen that only when high-quality data comes from many dozens of well-curated sources, together with good db structure and models can one be able to use a graph representation to produce knowledge. Even then, only a few papers show interesting results coming from using a graph representation vs a table representation. 📊📚🤝📝

## leading a team

Certainly, here's your text with a moderate use of emojis:

At Whitelab, not only am I a project leader, but I am also a team leader. Two computational biologists, each with great strength, knowledge, and years of experience in various topics have been under my supervision.

This was humbling and something I took extremely at heart. I had led people before at Whitelab and mentored at the Broad. Yet this was more important. Both were women and older than me.

I received good feedback from the get-go and even with some mishaps, things only got better. I have been able to start two new recruiters to increase the team from 3 to 5.

However, this was not just all fun. Amongst the possible points I could list, a big one was the reverse culture shock. In the way people behaved with one another in the professional sphere and the way things were done in general.

A few examples:

- vacation time ✈️🏖️
- smoking cigarettes 🚬
- going out in bars much more often 🍻🎉
- being very/too friendly with one another 🤗🤝
- jokes / swears / etc. 😄🤬

But some of it could be specific to this startup and the team being quite young, I was able to spot a general lack of personal know-how in startups. This would prove problematic as misbehavior, even unintentional, can backfire in the most terrible after some time and when you add stress and the like. Some issues could be seen as immaturity from some of the team members:

- fighting with each other instead of collaborating 🤼‍♂️🤝
- putting too much emotion on silly topics and on projects 😡📈
- taking feedback personally 🔄🙅‍♂️
- disregarding rules, processes, and hierarchy 🚫📋🏢

But especially processes, or the lack thereof, were a big issue in itself. This is something that team leaders were tasked with implementing. But it required as much learning as unlearning problematic behavior, and people were averse to change.

Now, even after 8 months, this is still an important topic, and many of the issues we are facing within the company are stemming from this lack of processes.

## the issues

It only took a few weeks before I saw the most glaring issues at Whitelab. But as always it took many months before they emerged as a clear picture to me.

This is very interesting to see patterns of similarity and differences between the two startup experiences I just had. What I could notice is that:

1. The C-levels personalities reflect totally on the company culture. 🧑‍💼🏢
2. The C-levels' domain knowledge is key to success. 💼🧠🔑
3. The ability to create agile processes and to hire the right people at the right time is also key to success. 🔄👥⏰🔑
4. Fostering a culture of trust and respect is how you can keep the best people in your company. 🤝💼

Whitelab was certainly checking a lot more boxes than Aqemia but some key topics emerged still:

- The level of the team at the time was still too low to be able to deliver on the vision. People were lacking the know-how in many regards, and this is because the C-levels were missing a CTO with expensive Comp Bio experience.
- This missing CTO was also hindering the ability to create a pipeline and a clear technical translation of the vision. Projects were going in all directions and people were not aligned.
- The growth was slow compared to the vision, and Whitelab lacked the ability to hire. This was also explained by the funding: 10M€ is not that much in hindsight.
- The chill-out work environment, in all the good it brings, was too extreme and led to a sense of inefficiency and lack of focus. I know how much people work in Boston, and how much they work in other startups. And even if one should not confuse working a lot with working well. I could see that people were not working enough for the vision to be achieved.
- The structural biology team was lead by someone with a strong experience in drug discovery, chemistry and structural biology but with no experience in project / team management. With ML and AI and without a product vision (POC->MVP->V1...).

## Issue in European biotechs

I would like to add 3 points that I believe are less specific to Whitelab and might be a common aspect of European companies:

- The funding in Europe is often much smaller than in the US, especially for seed and series A. This is especially problematic for biotech companies that need high capex from the get-go for things like doing experimental validation, building experimental facilities, and creating a first pipeline.

- Another issue that most companies not from either Boston or San Francisco or their surroundings will face is the difficulty in recruiting talents and the lack of experience from most team members. In a research environment, this is okay and known as a Ph.D. student. When you try to build a product, however, you need people with experience, especially at the beginning when the team is small and you try to lay out the strategy for the years to come

- A final issue I have noticed in both companies I was at, is the open sourcing scare. Knowing biologists and Business Developers, I can guess this is an issue in most non-GAFAM companies. This is problematic since software is something that can get copied and pasted so easily, scarcity has to be artificial. In this context, computational biology relies heavily on open-source software. mostly developed by research organizations and academic labs. However hundreds of, sometimes extremely wealthy companies are building software that could benefit everyone but which they keep behind closed doors to stifle competition. However, it mostly stifles innovation as we all know. This is problematic for many other reasons, like reproducibility and open assessment of results, but it is also at an individual level. Developing software based on fully open source data and code in a closed way, knowing that this could be useful to so many others and that likely hundreds of people are building the exact same tool too can be depressing.

Computational biologists should prioritize companies and positions where they can have the greatest impact. that often means working on open-source projects. and lobbying hard for their companies when this isn't the case. This has been a big lesson learned for me too.

## The startup vibe

I had worked in a startup before: At my own, PiPle, and I could see many things I was not used to anymore. Doing everything yourself, from the recruiting to the client presentation. From the product design to the strategy.

In many ways this is exhilarating. However, it is also very time-consuming and can be very stressful. If you have a project in mind you might have to wait for it.

The startup vibe is also one where things tend to change very quickly if you are on board for a project. Maybe a young startup is not the right bet. Be on board for a mission, but especially a team of people you believe in.

This is also a place where things go fast, hiring, promotions, and pay raises. But also fast in the other direction. Your colleagues can be laid off as quickly as they are hired, a project canceled or even a vision changed.
