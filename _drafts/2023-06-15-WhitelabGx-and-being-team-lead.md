---
title: "My Work at Whitelab and Creating a Team"
excerpt: "If you are working in data-sciences / genomics and on large-scale projects: This post might be of interest to you."
category: "Other Work Experience"
date: 2023-06-15
tags:
 - Big Data
 - genomics
 - Python
header:
  teaser: "assets/images/.png"
---

After a very deceptive end of the year, I decided I wanted to take a month or so to get my thoughts in order. To relax and find some peace with what happened at Aqemia.  

However the day following my departure I was already looking at companies and contacting labs.

I was thinking about the option of going back to the Broad Institute. "Would it be hard? Should I go now? Would it be the easy way out? What about my apartment, my girlfriend? etc."

It was tough and I had, fortunately, all the support I could need. But still nothing was making it more bearable than looking out to the future and the new possibilities. Keeping my mind busy and staying positive.

It actually only took a week or so before I got replies. One coming from Deep Life and one from WhitelabGx.

I ended up being offered positions, but the choice was quite easy. DeepLife had quite a few red flags and its proposition seemed more complex and less regarding.

Whitelab on the other was very welcoming. Excited about my profile and offered me a Lead Computational Biologist postion. On the surface it looked a lot like Aqemia.

A young promising French Startup with a great vision. But there was many differences that I was only able to see after having had this previous experience.

But mostly the team was already there waiting for me and the objectives were clear.

## Disclaimer:

Why am I doing that?

It is simple: I strongly believe in openness and honesty and I think the world is a better place everytime someone speaks freely and openly about subject matters that have been kept behind closed doors.

I am talking here about my sole experience at WhitelabGx. With the management of 2023. This is just one point of view at one specific moment in time. I also have my own values and reference frame. Please do not use any one's past experience to judge a current company on this account and do your own due diligence.

Because of the nature of the subject and by respect for any one currently working at WhitelabGx, I will keep this post private for now. If you are interested in reading it, please shout out an email and I will send it to you.

But I might at least let you know about what WhitelabGx was very open about as of end of 2023:

- Whitelab has a culture of kindness and honnesty.
- Almost everyone is staying in the company after their trial period.
- Whitelab is largely composed of people with past experience in research, biotech and biology.
- Whitelab is very diverse, exactly half of the company is non french. with people coming from all over the world. The culture is very american.

[button: send me an email to get the full story here]

## the environment

Many things were green flags for me. The company was actually thinking of itself as a Biotech, the CSO was a biologist with experience. They had and HR manager. They also had a team of biologists and both the CEO / CSO were very honnest, aware of what they didn't know and were very open to my suggestions and ideas.

The place itself was a brand new incubator called Future4Care. As nice as Broad and less than 10mns from my place.

Every member of the team was nice and welcoming. It was small however: 20 people.

## the work

the goal was to build both a team, a pipeline and a product. The team was composed of 2 computational biologists. But I quickly realized that I would have to do more than that.

Effectively, I was the sole person in whitelab with extended knowledge of computational biology.

I would describe this knowledge as mainly knowing well the current sequencing tools, processing & analysis tools and the datasets. Knowing their advantages and issues. Knowing where the field is going and sensing the bullshit from the true science.
I think this is what differentiates me 4 years ago from me know and what differentiates a computational biologist with experience from one without.

So I had effectively to create the entire roadmap given the vision that David & Julien had.

The vision itself is one in progress but I could sense the idea of using ML to drive as much of the experimental design of the preclinical cell therapy discovery as possible.

They had already the sense of what were the best tools nowadays for such an endeavour.

They had envisionned 2 products for the CB team. 

1. The Atlas
2. The Knowledge Graph

For the Atlas they were talking here of something that would contain a data modality for all tissues in the human body. The intial goal was to be able to do one thing:

1. find proteins that would be on the surface of one tissue and not rest.

For the Knowledge Graph the idea was more murky but the idea was that much information was available already in papers, in databases and in the heads of the scientists. I was actually initially told to disregard this part as it was not a priority anymore.

After lots of search, some iterations, meetings with clients and internal debates. I ended up presenting my proposition to the leadership a month after I arrived:

First, the knowledge graph and the atlas were to be merged into one product. to query omics data, one need good metadata. omics data output will also be likely considered metadata.

Then the product being very complex, it will be devided into 5 parts:

1. the scAtlas
2. the bulkAtlas
3. the intelAtlas
4. the metaAtlas (knowledge graph)
5. the AtlasApp

from this we could do a couple of things:

1. find novel targets (target discovery) by comparing diseased and healthy phenotypes and e.g. finding genes that are differentially expressed in the disease.
2. assess model quality: analyse and compare models transcriptome and response to the original's tissue transcriptome.
3. find transcript associated with proteins that could be on the surface of one tissue and not rest.
4. Design better payload based on the target, its expression and predicted promoter that are mostly activated in the cell type of interest.

In order to do that I would help myself of a few famous Databases and tools:

1. cell x gene -> this is the backbone of the Atlas, used in most parts of it. From its databases, to its processing pipelines and the technologies used to build it. The AtlasApp would stem entirely from it.
2. TCSA -> this is a multi database knowledge base with addition of ML predictor, to assess the probability for a protein to be a surface receptor and its druggability.
3. gget -> used to query our main databases from chembl to uniprot, pubmed, ensembl, pdb etc.
4. scanpy -> used to process the data and to build the Atlas
5. Nextflow + GCP -> used to store all of our datasets and to run our premade pipelines to process our supported sequencing technologies.
6. foundational models -> not included in the first part, they would be used to become the core ML model representing the Atlas, they would synthetise the knowledge contained in the Atlas and the Knowledge Graph. predicting cell types, correcting batch effect, missing genes, allowing us to query unseen conditions, etc.

The knowledge graph in itself would be in name only as we have realized that there is not an urgent need to create a graph database for now. For an MVP, tables and query tools would be enough.

Moreover we have seen that only when high quality data coming from many dozens of well currated sources, together with good db structure and models can one be able to use a graph representation to produce knowledge. Even then, only a few papers show interesting results coming from using a graph representation vs a table representation.

## leading a team

At Whitelab, not only am I a project leader, I am also a team leader. Two computational biologist, each with great strength, knowledge and years of experience in various topics have been under my supervision.

This was humbling and something I took extremly at heart. I had lead people before at whitelab and mentored at the Broad. yet this was more important. Both were women and older than me.

I received good feedback from the get go and even with some misshaps things only got better. I have been able to start two new recruitment to increase the team from 3 to 5.

However this was not just all fun. Amongst the possible points I could list. A big one was the reverse culture shock. In the way people behaved with one another in the proffessional sphere and the way things were done in general.

A few examples:

- vacation time
- smoking cigarettes
- going out in bars much more often
- being very/too friendly with one another
- jokes / swears / etc.

But some of it could be specific to this startup and the team being quite young, I was able to spot a general lack of personal know how in startups. This would prove problematic as missbehaviours even unintentional can backfire in the most terrible after some time and when you add stress and the like. Some issues could be listed in the "behaving sometime like children" category:

- fighting with each other instead of collaborating
- putting too much emotion on silly topics and on projects
- taking feedbacks personnaly.
- disregarding rules, processes and hierarchy

But especially processes, or the lack thereof were a big issue in itself. This is something that team leader were tasked in implemeting. But it was requiring as much learning as unlearning problematic behavior and people were averse to change.

Now, even after 8 months this is still an important topic and many of the issues we are facing within the company are steming from this lack of processes.

## the issues

It only took a few weeks before I saw the most glaring issues at Whitelab. But as always it took many months before they emerged as a clear picture to me.

This is very interesting to see patterns of similarity and differences between the two startup experiences I just had. What I could notice is that:

1. The C-levels' personalities reflect totally on the company culture.
2. The C-levels' domain knowledge is key to success.
3. Ability to create agile processes and to hire the right people at the right time is also key to success.
4. Fostering a culture of trust and respect is how you can keep the best people in your company.

Whitelab was certainly checking a lot more boxes than Aqemia but some key topics emerged still:

- The level of the team at the time was still too low to be able to deliver on the vision. People were lacking the know how in many regards and this is because the C-levels were missing a CTO with an expensive Comp Bio experience.
- This missing CTO was also hindering the ability to create pipeline and a clear technical translation of the vision.
- The growth was slow compared to the vision and Whitelab was lacking an ability to hire. This was also explained by the funding: 10M€ is not that much in hindsight.
- the chill out work environment, in all the good it brings, was too extreme and leading to a sense for me of inefficiency and lack of focus. I know how much people work in Boston, how much they work in other startups. And even if one should not confuse working a lot with working well. I could see that people were not working enough for the vision to be achieved.

## issue in european biotechs

I would like to add 3 points that I believe are less specific to Whitelab and might be a common aspect of european companies:

- short on money for the experimental facility
- difficulty to recruit talents & lack of experience

### An issue in most biotechs

Final issue I noticed
- the open sourcing and privacy scare


## the startup vibe

- doing everything yourself
- recruitement
- client presentation



