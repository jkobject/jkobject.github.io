---
title: "Review of Papers"
excerpt: "Here is the draft of a list of the papers I have read with a short personal summary of them"
sitemap: true
author_profile: true
layout: single
classes: wide
permalink: /review-of-papers/
skip_amp: false
toc: true
header:
  overlay_image: "/assets/images/research.jpg"
  caption: "thanks to dribble for this amazing design"
---


# Overview

## SUMMARY

What is the research problem the paper attempts to address? Consider
	What is the motivation of the research work?
	What problem does it attempt to resolve?
	Is it addressing weaknesses in existing approaches?
	Does it challenge an existing research paradigm?

What are the claimed contributions of the paper? What is new/original in this paper?
	A new question or research area?
	A new understanding of a research problem?
	A new algorithm/experimental method/proof technique/methodology for solving problems?
	A new breed of software tools or systems?
	A new formalism or notation?
	New evidence to substantiate or disprove a previously published claim?

How do the authors substantiate their claims? What makes the claims scientific?
	What is the methodology adopted to substantiate the claims?
	What is the argument of the paper?
	What are the major theorems?
	What experiments are conducted?  Look at:
	data analyses/simulations/benchmarks/user studies/cases studies/examples

What are the conclusions? 
	What is to be learnt from the paper?
	Will standard practice in the field be changed as result of the findings?
	Are the results generizable?
	Can the results be applied to other areas of the field?
	What are the open problems?

## EVALUATION

Is the research problem significant?
	Does the work only address a minor problem?§
	Does it deepen understanding?
	Does it explore new design ideas?

Are the contributions significant?
	Is the paper worth reading?
	Are the authors simply repeating the state of the art?
	Are there real surprises?
	Are the authors aware of the relation of their work to the existing literature?
	Is the paper addressing a well-known open problem?

Are the claims valid (and modest enough)?
	have the authors (intentionally or unintentionally) cut corners?
	Has the right theorem been proven?

## SYNTHESIS

What is the crux of the research problem?
What are some alternative approaches to address the problem?
What is a better way to substantiate the claim of the authors?
What is a good argument against the case made by the authors?
How can the research results be improved?
Can the research results be applied to another context?
What are the open problems raised by this work?
Can we do better than the authors?


## 7 things that would make papers better (after 156 papers)

1. papers are using the same expressions for things that could be said in simpler manner
2. papers are displaying citation + p values + data. within text: should be a hoverable link. 
summary should exist as in CELL with a table of content and nice image at the first Page. 
3. tables should be interactive and secondary material should be within the paper. or readily available from it. 
4. the paper, its data, its code, its bio methods and everything it cites should be accessible. 
5. there should be a table for complicated words/acronyms with explanations.
6. for other types of info (places/genes/labs/companies there should be links)
7. there should always be a corresponding press release/medium article corresponding to it. with simpler explanations.



------

# Papers

## Attention in a bayesian framework - sahani

-> atention as a byesian inference. to improve impoverish stimulus
appearance of a limitation == bottleneck in such framework


shouldn't you know about P to compute this minimization ? page 7

pb : 



## neural coding  Peter latham

neurons send and receive outputs which noise can be correlated meaning that there is in fact information in it. This can have a huge effect when looking at big number of neurons. We have to knwo the correlation to understand the coding as the neurons do 

the effect of correlation can be expressed as the variation of I_shuffled ( for encoding) & of I_diag for decoding information adn saying if correlation are important in this process. those values can be from 0 to 40% of the total information of the neurons

ICA ?
independent component analysis. if we admit that a signal is composed of multiple independent sources, each of them emitting an information (thus the corresponding random variable expresses Dependant outcomes) It is possible to each sources ( or each independent components) from the signal according to $y = Wx + o$ with W a matrix (like a Neural net) x the input and o the noise. it is part of unsupervised learning of features

pb : the noise is not gaussian as estimated here. 



## cracking the neural code --peter latham



The Equivalence of Information-Theoretic and Likelihood-Based Methods for Neural Dimensionality Reduction Manesh sahani

This paper is reviewing many modern information theoretic and stochastic methods to decipher the information encoded in spikes according to stimulus. It expresses concerns and solutions for the MID methods and present some new architectures as well. 


pb :



self calibrating NN for dimensionality reduction Chklovskii

A NN that is calibrating itself to its input and reduce the dimensionality the best way possible according to minimization rules. present online and offline with rules and reguralizers which creates update rules that can be attributed to hebbian & anti hebbian behavior in neurons.

pb : not really biologically plausible





## Alex graves talk at IJCNN


can use ActiveComputationTimeNN to know where are the important part of the data 
DifferentiableNeuralComputer? NTM

DecoupledNeuralInterface to stop using backprop ( as efficient)



## neural turing machine Graves

where does the vector emission of the heads comes from ? 
the NN
for examples the shifts are produced by a softmax layer applied to the output of the controller 
softmax : mise a l'expo de chaques val du vect avec normalization sur le vector ( sum =1)

cross entropy : objective function that uses entropy function of two stat distribution and the log loss function

objective function :  fonction d'apprentissage that needs to be minimized ( it gets the output and the hoped output)



Evolving Neural Networks through Augmenting Topologies - Kenneth O stanley

really nice paper, explained well, but few complexity though.

What if this evolving architecture leads you to train your growing NN over simplification of your data and it gets more and more complex (for images for example) and you could have different types of neurons with different acti function ...



## Predicting the sequence specificities of DnA- and RnA-binding proteins by deep learning Brendan Frey

k-mer ?
all the possible substrings of length k that are contained in a string

mini-batch  ?   stochastic gradient descent ?
In gradient descent algorithms, you can calculate the sum of gradients with respect to several examples and then update the parameters using this cumulative gradient. 
If you ‘see’ all training examples before one ‘update’, then it’s called full batch learning. 
If you use only one example, it’s called stochastic gradient descent (online learning). 
If you use a small batch of examples, it’s called mini-batch learning.

nesterov momentum ?
a way o compute how we move in our gradient descent, that is, using a momentum and in addition we give this an acceleration in the way we computer it which is called accelerated momentum (it seems to converge quicker)


hyperparameter search ?
a way to find the best set of parameters for a ML algo either by doing them all or by inferring a function from them if such exist. 


alternative splicing ?
when a gene encodes many proteins trough specific selection during the RNA "epissage" == "splicing"

metazoa ?
eucaryotes with different tissue types

sequence specificity protein ?
proteins that binds inside the holes in coiled DNA or RNA in specific places regulating their transcription in many ways


## Deep-learning-free Text and Sentence Embedding  --Sanjeev Arora
[link](http://www.offconvex.org/2018/06/17/textembeddings/)

like word2vec but for phrases

- you weight each word by its inverse smoothed frequency
- you sum the weighted vectors 
- you remove the component that is present in any possible phrases (corresponds to points etc..)

to produce phrases you have a discourse vector representing the subject
and you have a proba function of a vector appearing at pos t given discourse vector. ct moves as a random walk

## How do we capture structure in relational data --Sanjeev

we want to have a representation of the vertices (points) that is similar
when vertices pertain to a similar neighborhood do this by learning a representation that allows us to guess what will be the next given the preceding in a random walk

with node2vec there is 2 ways to look at neighborhoods (homophily or structural) and you can interpolate between the two with 2 hyper params

## Cancer Metastasis Detection With Neural Conditional Random Field --Yi Li

we want to use an information of the neighborhood of images the we find by computing an additional term on the inference of each elements according to their similarity/ distance to others and their labels. this creates a differentiable loss function (Conditional Random Field) that allows for fast computations etc. 80% success 

## Systematic identification of phosphorylation- mediated protein interaction switches

phosphorilation plays a regulatory role in prot-prot interaction by modifying the efficiency of functional domains.

from binding, enzymatic functions ...

(only using simple probabilistic methods given the presence of such amino acids and other chemical parameters..) -not well explained thought

there is much to do here but needs even more data and need clear characterization of the multiple effects of the folding in the chemical processes of phospho switches


## A polymorphism in the tumor suppressor p53 affects aging and longevity in mouse models

p53 if polymorph increase cancer probability but also increases life expectancy by preventing the knowing off of genes useful in cell replication and decreases stem cell exhaustion.

## gene2vector

really just applying the word2vect algorithm on protein sequences and inferring some interesting results like the destructuring or presence of proteins  

## Multi-Omics factor analysis - a framework for unsupervised integration of multi-omic data sets -- Ricard Argelaguet et al.

you integrate each data by doing a PCA on them basically.
but it uses a Latent factor model which is formulated in a bayesian way by Bayesian way. it i able to recover sparse features which explain well the underlying variations in the data and are able to thus predict outcomes in clinical data and importance features in pluripotent cell differentiation
NICE.

It is super efficient computationally (compared to similar methods)

## Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks -- David Kelley

you can learn the functional activity of ncDNA with a CNN and DNA seq (==FAIRE seq) data (ground truth here)

>understanding the DNA–protein interactions as a function of the un- derlying sequence.

Given training data, models parameterized by machine learning can effectively predict protein binding, DNA accessibility, histone modifications, and DNA methylation from the sequence


provide much information on relationship to diseases and allow fast training by reusing the weights to train on other datasets the first CNN weights are predictive of known binding configurations as well as unknown ones. (should be investigated)

## Machine theory of Mind

How to interpret and predict another agent's thinking according to its behavior.
>This “learning to learn” about new agents is what we mean by meta-learning

principal characteristics is that the network can learn that the agent hold false belief about their environment

## Analysis of Genomic Sequence Motifs for Deciphering Transcription Factor Binding and Transcriptional Regulation in Eukaryotic Cells --Valentina Boeva

>A eukaryotic genome contains a variety of structured patterns. A far from exhaustive list of genomic patterns includes (i) tandem repeats and transposable elements, (ii) stretches of GC- or AT-rich sequences (e.g., CpG islands in mammalian genomes), (iii) binding sites of DNA associated proteins (e.g., transcription factor binding sites), (iv) splice sites, and (v) DNA and RNA binding sites of non- coding RNA molecules. Different patterns may overlap each other. Therefore, although this review is focused on motifs for transcription factor binding sites (TFBSs), we provide a short overview of other types of genomic patterns.

This is an overview of the different Trans Fact Bind Sites TFBS and the Motifs Repeats, AT-GC rich sequences, splice sites, miRNA binding sites, techniques and DB to use, find, retrieve known or unknownTFBS.

_contains DB links to unknown DB of PWM motifs for TFBS_

discovery of Shadow binding sites that are low affinity binding sites that alone are not capable of retaining the TF long enough to ensure activation/repression, but instead are used to maintain a high concentration of TF in the vicinity of the primary binding sites


## GPU Kernels for Block-Sparse Weights --Scott Gray, openAI

increasing drastically computation speed on NN with blocks of zero valued weights, allowing to deepen or widen dense NN for same computational efficiency and better accuracy.

They use LSTMs with internal networks and connects them according to the small world paradigm (very good results)

--> would be nice to learn the sparsity structure
according to a predefined sparsity structure, a small world and block sparse  property

Available on tensorflow ops.
(best use multiples of 32x32 and small float values 16 bits etc..
best minibatch is 64 (for cache dilution)

## node2vec: Scalable Feature Learning for Networks -- Aditya Grover, stanford

How to embed a node from a network using a flexible notion of neighborhood (from random walks)

able to classify predict ... from this representation, which involves just creating an encoding matrix that is learnt by asyncSGD by trying to predict the neighborhood given the representation 


*questions*

What if we set out to encode not solely the local neighborhood but also some information of the distant neighborhood considering the prior that the network has the small world property?


## MicroRNA signature analysis in colorectal cancer: identification of expression profiles in stage II tumors associated with aggressive disease --Kah Hoong Chang

_touse_

Very High quality paper with a demonstration that 3 circulating miRNA
Can provide information on the colorectal cancer and its reaction to different treatment strategies, for personalized curration of the cancer, this association amongst more than 400 different miRNA (using micro array + microfluidics PCR)  was performed using an ANN to learn how to classify patients

## Efficient and Robust Automated Machine Learning --Matthias Feurer, Freiburg University

they build on the work of auto weka to solve the CASH optimization (hyperparams and model) problem, to create state of the art algo with sota performance using a tree based Bayesian method (random forest based) called SMAC. They improve this model by having a first instantiation step using meta learning: they have a model that have learnt what are the best instantiation for a given dataset using meta feature of the dataset such as entropy, number of points, classes etc... .
and secondly they use an ensembl of their best algo and not just one

## Vicus: Exploiting local structures to improve network-based analysis of biological data -- Bo Wang, Serafim Batzoglou

_touse_


They propose a new method to the manifold learning problem (dim reduction, clustering, classification etc..) Which uses local dimension learning to do its magic instead of the usual laplacian eigenvectors which learn comparing global euclidean distances.

It is basically the same thing as the laplacian but only it is constrained to do its computation on a local subgraph of close by datapoints

_contains DB links to unknown DB of single cell RNA (12-15, 24)_

## Active learning of cortical connectivity from two-photon imaging data --Mart ́ın A. Bertra ́n, Duke Uni

using bi photon imaging to look at a set of neuron activities and inferring some networks of connections given some stimulus using active learning. 
Basically, what edge should be added to the network that would maximize the likelihood of the model. (edges are weighted)
They model it with a GLM trying to optimize the BIC value of the model. to find whether promising edges to be added can be, it tries to drive the spiking rate of the model up.


## Finding Syntax in Human Encephalography with Beam Search --John Hale, Oxf, DeepMind

>a pattern of results recommends the RNNG+beam search combination as a mechanistic model of the syntactic processing that occurs during normal human language comprehension

RNNG are generative models (here for text) that rely on RNN. they can create a sentence or form a grammar tree of words given a sentence, a tree that you can parse within using beam search this parsing gives you information such as word surprisal and you can use these different statistics given the tree to generate different phrases that will create a predictable effect on the human brain meaning the way their syntax is generated is predictable of the human language comprehension. 

The guys basically made a point in cognitive neuroscience using ANN and advanced computer science. __MADNESS__

## GLOW: FLow based generative network --OpenAI

It is a particular kind of generative NN that is fully reversible thus encode^-1 == decode it is like an auto-encoder but without the re parametrization trick and with a latent space that is the same size as the input space. in the latent space you just have a multi dim Gaussian you can then interpolate to generate new inputs. 
(costly to train though)

## Prediction of acute myeloid leukemia risk in healthy individuals --Eran Segal, Moritz Gerstung

age-related clonal haematopoiesis is a phenomenon is a phenomenon that exists during aging but also is an indicator of AML 7yr before getting it (leukemia form). Here they try to differentiate between the two using deep sequencing methods they find a group of SNPs and markers in parts of the sequences that explains together much of the data but not enough separately. they then did the same on regular blood samples of patients and have seen that information on the size of hematopoetic cells (blood) have a correlation with age related diseases but also pre AML conditions. thus enabling a first easy screening of risky patients.

## A synthetic-diploid benchmark for accurate variant-calling evaluation -- Mc Arthur

trying to create a new benchmark for variant calling tools (matching reads to a reference genome and inferring the SNPs) this is faster than de novo WGS which is super costly and long. (this is part of NGS) they use a particular type of cell lines (human) called CHM which are diploids but fully homozygous and allows to use PACbio sequences without mixing the two genomes

## Meta-analysis of the diagnostic and clinical utility of genome and exome sequencing and chromosomal microarray in children with suspected genetic diseases -- Michelle Clark

A literature and statistical review of 10 years of genomics medicine for infant genetic diseases diagnostics. better use WES/WGS than previous method called CMA (molecular analysis) better sequence infant and 2 parents as well than jsut infant. a lot of heterogeneity and thus. take stats in this study with a grain of salt.

## Multi-scale deep tensor factorization learns a latent representation of the human epigenome -- Jacob Schreiber UW

_touse_

let's create an embedding of all epigenomics data. "Avocado" 
_quality article_
>o high-throughput assay is perfectly reproducible, and run-to-run differences in the same experiment may reflect either biological variation in the cells being assayed or experimental variance arising from sample preparation or downstream steps in the protocol. Finally, many epigenomic assays are highly redundant with one another, and many cell types are closely related to each other, leading to highly redundant measurements

--> so Embeddings
factorize an incomplete 3D matrix of epigenetic features into 3 2D matx of different feature types (pos, assays, cells), concatenating features for each pos on the matrix and passing through 2 * 2048 dense layers NN.

maybe try to train on predicting different features to have more generalization
train on ENCODE instead of RoadMap.. etc.
is it fully differentiable ?
How is the vector factorization working?
how is it constrained?
...
## Machine learning applications in genetics and genomics -- William Noble, UW

a review of every possible machine learning applications in genomics 

## BioAmbients: An abstraction for biological compartments

Ambient Calculus, a further abstraction of PI calculus, can be the mathematical base to design a framework for abstracting biological compartments

Basically how to design a framework for a code allowing us to simulate cells and their inner/outer processes. Bio ambient seems to be the most general mathematical framework. Available in BioSpi

further improvement such as duplicate, divide, erase, destroy, 3D... needs to be achieved

## Personal clinical history predicts antibiotic resistance in urinary tract infections -Yelin,Snitser,Novich

Using Israel's DB and stat explore they have shown that there is relation to many parameter from urinary tracks infection and other factors and related them to biological known factors. using those predictive factors, one would be able to predict the risk of such infection and to prevent it. Among the interesting factors, relation with location (old age institute etc) pharmaceutical history, cross relations eg between age/sex. 

## Deciphering regulatory DNA sequences and noncoding genetic variants using neural network models of massively parallel reporter assays - Rajiv Movva, Kundaje

_touse_

We can see how using a NN model trained to predict regulatory effects of SNP on non coding sequences from Multi array analysis datasets works well. It was used together with SNPs found in GWAS for some genetically correlated cardiac diseases. some interesting results but MPRA dataset is of poor quality in general (low correlation)
Big step forward thought.

## Clinical Concept Embeddings Learned from Massive Sources of Medical Data -- Andrew L Beam1, Benjamin Kompa UNC, Harvard

They manage to show 100,000 clinical concepts embeddings from 3 different data-sources, they compare them to other state of the art methods on different sets of benchmark they created using clinical data sources. They achieve the biggest dataset of embedding with sota results on most of the softs·

## pooled screens in human cells, David Feldman el al

there is the introduction of doing targeted fluorescent in situ sequencing ( sequencing of specific genes from within the cell by using the fluorescence sequencing method of sequencing by synthesis.) in addition, inferring the specificities of the cell (morphology, dynamics and interaction) and to link genetic variations to 

## Manifold-tiling Localized Receptive Fields are Optimal in Similarity-preserving Neural Networks, Pehlevan, Tepper FI CCB

we can see a bio plausible NN optimization function relying on Hebb. anti Hebb. neurons which can uncover the manifold in a set of data (Here done with symmetric datasets) even for highly dim. datasets. Also showing a link to kernel learning (Here it is obviously an unsupervised learning technique,)

## Can deep learning improve genomic prediction of complex human traits? - Pau Bellot et al

tried to regress human traits values (waist, hips, height, bone
106 heel mineral density (BHMD), body mass index (BMI), systolic blood pressure (SBP)) using MLP, CNN & LR over SNPs from WGAS. 
*very stupid idea if you ask me. it is not how CNN are supposed to work. It is really treating DL as magic here*

## Learning Graph-Level Representation for Drug Discovery -- Junying Li et. al.

They use GCN to extract embeddings from a network representing atoms linked together (i.e. a molecule). They use a dummy super node to represent the entire molecule in one feature and they are able to classify the molecule between ones that works and ones that don't

##  MultiPLIER: a transfer learning framework reveals systemic features of rare autoimmune disease -- Jaclyn N. Taroni et. al.

_touse_

multiplier is a method of using Plier (an NMF method to extract features related to gene interactions) on a large compendium of data from many gene interaction modification in multiple diseased over multiple tissues from MicroArray data. learning on a huge multivariate dataset allows the unsupervised embeddings to be richer and more precise in what they convey. They demonstrated that they were able to find feature (and thus genetic interactions for many different complex diseases. the model tries also to make similar vectors from similar tissues and diseases, aligned.
*quality paper*

## On entropy and information in gene interaction networks -- Z. S. Wallace1, S. B. Rosenthal

An information concept to extract from interaction networks, some subsets that are correlated or related together. It is complementary to other enrichment methods and can find relationships amongst diseases, metabolic pathways and genes with relation to phenotypic characteristics.
and recover many interesting relationships that have been found by researchers along the way.

_DisGeNet_
_InBioMap_
_UNIPROT_
_MSigDB_
_GeneOntology_

*plus présenter les derniers problèmes et questionement durant les résultats (ou on en est maintenant)*

*raconter aussi les résultat légèrement en mode histoire de ce qu'on a fait.*

## Allele-specific binding of RNA-binding proteins reveals functional genetic variants in the RNA -- Ei-Wen Yang, Jae Hoon Bahn

_eCLIP-Seq_

GV of diseases DB:
_GWAS, COSMIC, ClinVar, CIVIC and iGAP_

_touse_


A method to find Allele specific binding events using eCLIP-seq data (trancriptome-wide protein RNA interaction data) which gives enough data to do it in an allele specific manner, the method filters out biases in the data and appears to give SOTA results. It predicted functional SNV and how they act as regulators from direct observation instead of correlation inference
"we expect that allele-specific analyses of eCLIP will be an essential approach to deciphering the function of non-coding variants in the RNA."

## In silico prediction of high-resolution Hi-C interaction matrices --Shilu Zhang1, Deborah Chasman.

_touse_

to predict the contact count of two genomic regions from their one-dimensional regulatory signals which output from HiC-Reg can be used to identify significant interactions using peak-calling algorithms that have as good experimental support as those from true counts.
a regression-based framework to predict interactions between pairs
of regions across multiple cell lines by integrating published Hi-C datasets with one-dimensional regulatory genomic datasets.

## Winner-Take-All Autoencoders -- Brendan Frey

winner-take-all spatial and lifetime sparsity methods to train auto-encoders that learn to do fully-connected and convolutional sparse coding which jointly trains the encoder and decoder paths by direct back-propagation, and does not require an iterative EM-like optimization technique during training. sota results especially when doing semi supervised training

## Dissecting splicing decisions and cell-to-cell variability with designed sequence libraries -- Eran Segal, Martin Mikl

rationally designed libraries, consisting of altogether 32,789 variants, to address fundamental questions in splicing regulation considering the process in its entirety, from the processing of the RNA to the level of the final functional gene product. They could reproducibly detect even small changes in splicing ratios and quantitatively predict splicing of novel variants with high accuracy (R2 between 0.76 and 0.85)
cells evolved to have seemingly “suboptimal” splice sites, which maximizes the potential for dynamic regulation, but can also serve to ensure optimality at the level of protein isoforms. They have established an assay that is able to assess the cell-to-cell variability of splicing decisions in large scale by measuring the protein output of alternative isoforms and shown that the level of stochasticity can be encoded in the DNA.

__Highly rich paper__

## Quantum Entanglement in Neural Network States -- Dong-Ling Deng, Xiaopeng Li

the entanglement proper- ties of neural-network quantum states in the RBM architecture. and proof that all short-range RBM states satisfy an area law of entanglement for arbitrary dimensions and bipartition geometry
For some maximal volume- law entanglement RBM representation is remarkably efficient, requiring only a small number of parameters scaling linearly with the system size which show the power of NN to describe massive entanglement
Further explore the link between ANN and entangled quantum states...

## Cancer archetypes co-opt and adapt the transcriptional programs of existing cellular states -- Maayan Baron1, Isabella S. Kim

__quality paper__

study of the gene expression of individual cancer cells in zebrafish and human melanomas. three recurring gene expression patterns across melanoma cancer cells which we refer to as ‘archetypes’ because they appear to be co-opted cellular states with distinct spatial location
cancer cells between human and zebrafish melanomas exhibit the same transcriptional program.
not yet purview into the origin of archetypes. found cooperation across cancer cell lines as they form a tumor in vivo

## Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk -- Troyanskaya, FI
__addition of the second paper "Predicting effects of noncoding variants with deep learning–based sequence model",__ especially the method part of it.

_touse_

they have used a deep CNN with a lot of different Weighted patterns to predict regulatory profile (chromatin, methylation etc...) from a raw DNA sequence. using ENCODE datasets given specific cell types. this gave them the ability to predict a cell specific profile as well as to predict variation in regulatory profiles caused by variants, using a linear model (made from non linear basis function of the different profiles data, they are able to regress how much each the regulatory features of the non coding sequence before the Transcription Start Site (and a bit of the sequence after) influence the expression profile of different gene.) they were able to retrieve expression for famous protein and how they change with different cells and to retrieve SNPs causing variation in expression that were also shown from GWAS information (even better than in GWAS) and to find interesting disease correlations as well.

## One-Shot Imitation Learning -- Ilya Sutskever, Pieter Abbeel

a paper displaying the use of DQN with two distinct networks, one with an attentional mechanism (LSTLM) that sets a set of subtasks to achieve the objective, one to control the robot given the subtasks(MLP) (or even just reconstruct the sets of tasks given the final state it needs to achieve) Here the attentional system helps to subdivide the sets of tasks given to the MLP, results are SOTA for the type of tasks (first to achieve that) 

## MCM2 promotes symmetric inheritance of modified histones during DNA replication -- Nataliya Petryk, Maria Dalby

_not very interesting_

special sequencing technique revealed that parental histone segregation is almost symmetrical with a weak inherent preference for the leading strand. making it possible for MCM2 to recycle parental histones to the lagging strand (Fig. 3F, right), while a separate pathway deposits pa- rental histones on the leading strand. In this vein, it is conceivable that histone segregation can be regulated during development to drive asymmetric cell fates.

## Deep surveying of alternative splicing complexity in the human transcriptome by high-throughput sequencing -- Qun Pan, Ofer Shai, Frey

_old article_ 2008

explaining how the splicing complexity can be understood using RNA seq and how there may be a lot of possible transcripts from one sequence with different alternative splicing according to some regulatory sequences. one interesting aspect is that it shows how much there is and the amount we did not really knew about previously.

## Sequential regulatory activity prediction across chromosomes with convolutional neural networks. --David R. Kelley, Yakir A. Reshef

_touse_

bassenji is another DL algorithm to quantify regulatory features (certain - DNase seq, histone, Chip-seq) from CAGE experiments. it is using a CNN with expending layers (which multiply the ROI by a factor of 2 at each layers). it is from 16 month ago and appears to be less good than more recent work but provide trainings for coverage, GC%, EM for multi-reading alignment etc..
It shows link to eQTL found similarities and GWAS data, perform prediction of why some diseases happens etc, while preventing bias from LD. finally it is giving new research ideas (more data, finding more distant reg activities, better cell specific data, more precise data) and post transcriptional regulation activities etc...

## Deciphering the splicing code --- Yoseph Barash, Frey

_touse_

Kinda the previous version to deepBind. Here they describe an information theoretic method based on regression for prediction of variation of splicing probabilities compared to the baseline activity. this is used by taking in account typical base patterns that would create specific sec shape or bindings for the splicing to happen in a specific manner. This allowed the discovery of new features that make alternative splicing possible and of variation in different tissue with phenotypic logics behind.

## IMPALA -- DeepMind

A new DeepQN framework for the in parallel training of multiple actors and diminishing the delay/dissimilarity between the actors and the learners (and the learners to themselves) this framework/architecture is made possible by a new learning method that tries to combat the off policy (dissimilarity in policy) between the different agents. it uses previous work on batch A2C, Importance sampling, and other mathematically/experimentally driven techniques to compute the best possible gradient for episodes (a,s,r). 

## Unsupervised embedding of single-cell Hi-C data - Jie Liu, Galip Gurkan Yardımcı, UW

a paper displaying how one can use a previous technique called HiCRep which smooths the Hi-C contact matrix and then computes a weighted similarity measure separately at each genomic distance. Then averages the results for the cell itself. Finally followed by a Multidimensional Scaling (MDS) of the resulting matrix to reduce the dimensionality while preserving distance relations, allows to recover angle distance between datapoints (representing cells) which allows the classification of different cell phases. It can be done with high throughput scHiC data since using a subset of contacts still allows to recover the ground truth, especially if used in combination with a bag  of more deeply sequenced cells.

## An integrated encyclopedia of DNA elements in the human genome -- ENCODE

__start of the Engineer's map__

a detailed explanation of the types of data and means to get them from the encode collaboration. And an overview of this data. Interesting feedbacks from it. It displays the different things that might be achieved using it. 
Moreover it provides access and a biologically oriented summary of numerous research that have been undertaken by the consortium's researchers. Especially their results and how they fit in a more general summary of this kind of functional genomics data.


## Engineering Stem Cell Organoids -- Xiaolei Yin Benjamin E. Mead


an overview of the different use, techniques, and methods for the construction of organoids or organoids like objects from human stem cells. recapitulating OoC HoC etc. And talking about how a mix of these methods is required for the future of organoids engineering. 

## Advantages and limitations of current network inference methods -- Riet De Smet and Kathleen Marchal

a survey of the different network inference methods in genomics, to predict the regulatory network (in bacterial genomes) with the different algorithms that are available and their mathematical framework. The different DB that are available and the problematics and usages that everyone can have from these according to one's needs.

## Optimization Techniques on Riemannian Manifolds -- Steven Smith

two algorithms: Newton’s method and the conjugate gradient method on Riemannian manifolds, are presented and shown to possess resp. quadratic and super-linear convergence

## The Tsetlin Machine - A Game Theoretic Bandit Driven Approach to Optimal Pattern Recognition with Propositional Logic -- Granmo

the tsetlin machine is a form of machine learning techniques which uses tsetlin automaton the same way a neural network uses a neuron. However it is more computationally grounded by being in the framework of propositional logic. The paper shows how to reach an equilibrium in learning even from very noisy data by finding the right hyperparameter handling error assignment. it proves that it will be able to learn anything and then shows some sota results on some datasets. Moreover the paper derives CNN and RNN like structures from tsetlin machines.


## The Genetics of Transcription Factor DNA Binding Variation -- Deplancke 

	Since most of variant associated with phenotypic changes in mammals are from non coding region, the paper establishes the different mode of genetic variation mediated changes to TF binding. sets up the ways in which they have previously been uncovered, some examples and the difficulties behind this problem. It then goes on to highlight the possible technological (sequencing & computational(ML))-based techniques that might help in solving it.


## SegAnnDB interactive Web-based genomic segmentation --Hocking

a less interesting paper that reuses a mathematical framework to help on analysis (segmentation) of cancer genomes into different categories (CN variation, breakpoints(DNA deleted, inverted, or swapped)) by using a mathematical+vision framework to understand the user input segmentation and further them to the entirety of the cell genome in a supervised fashion.  

## Defining a Cancer Dependency Map -- Aviad Tsherniak, Francisca Vazquez, Phil G. Montgomery BroadInstitute

Researchers from CDS team at the broad present their ongoing effort to analyze a wide range of cancer cell lines to infer their dependencies (survival, reproduction) on different genes. To do so they are using genome scale loss of function RNAi screens (knocking down specific genes using silencing RNA which will get infiltrated by lentiviral infection in vitro on microArray live cell chips which is highly multiplexed (looking at the expression of the co-infected GFP RNA in each cases)). Each input RNA (shRNA ~100,000) will infect some cells and silence some genes. They contain a seed which will help in the binding to the desired mRNA.  
However, Because of this seed, this will also create off target effects (down-regulating other genes than the desired one by partial binding of the miRNA seed) it is using a linear regression model to understand the true effect of each shRNA in silencing a particular gene. (The model was in fact very similar in intuition to a NMF but was just a linear regression: to divide the dataset (cell line perturbation per shRNA) into two distinct part: cell line perturbation per gene knock down and cell line perturbation (instead of gene knock down) per shRNA with seed k) <-- could be done in a more efficient fashion by using an NMF which divide it and add a third matrix term which would contain the off target effect relation across shRNAs. 
The two matrix found allow one to understand specific cases where specific cell lines require a particular gene more than another and more than the regular cell. it is called: a differential dependency and might represent important therapeutic target. 
By taking the strongest ones (6std from the mean) they found 769 such genes for the 500 cell lines. they then used another non linear regression model with gene mutations, gene copy number, gene expression from the Cancer Cell Line Encyclopedia (CCLE).
They then carefully analyzed the different types of predictive MDPs (Marker dependency pairs) and specific MDPs for 86% of the dependencies.
However, to find a full range of MDP and predictive models for each, they estimate they would need to increase the amount of cell lines to >5000, to account for other types of dependencies such as ones that are not single cell specific (but are important in group behavior).
--> moreover, what happen for gene combination effects and in this case, time dependent gene known down effect? is there a non linear relationship between gene knockdown and gene knockoff? what about the many different type of cancer cells and their inter relationship present in a tumor?
how many other features can be added? (long range TF?) can one reuse some pretrained DL for genomic and find what molecular features in the sequence explain each types? 


## Improved estimation of cancer dependencies from large-scale RNAi screens using model-based normalization and data integration -- james McFarland BroadInstitute

*basically about explanaing demeter2*

explaining similar things as previously with a bit more emphasis in the comparative aspect and computational aspect of Demeter2 to other types of data. a larger dataset (790dtp). in the better explanation of the model and its results. interesting and deeper explanation of the computation in the methods:
the demeter2 model uses a Bayesian model with variational inference of some params and MAP estimates of others. it explains the full procedure to infer each params using scipy and Edward. in this model a lot has been used to find the best set of parameters / hyperparameters. comparing with ground truth or prior knowledge and values to set to test the strength of each.


## Genetic and transcriptional evolution alters cancer cell line drug response -- Uri Ben-David1, Benjamin Siranosian, Gavin Ha, Helen tang, Yaara Oren, Kunihiko Hinohara, craig Strathdee, Joshua Dempster, Nicholas lyons, robert Burns, Anwesha Nag, Guillaume Kugener, Beth cimini, Peter tsvetkov, Yosef Maruvka1, ryan O’rourke, Anthony Garrity, Andrew tubelli, Pratiti Bandopadhay, Aviad tsherniak

Here we look at the problems arising from the culture of cancer cell lines in research application. because of random mutations, changes in their environment, cancer cell lines undergo evolution. this creates strong differences to the in vivo scenario. The paper tries to infer the possible differences and how they might arise (medium, population bottleneck). They have dev a tool to compute the distance to a reference. They also show how to use this such as to understand cancer cooperation (with single cell seq) and correlation genotype-phenotype. 



## Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer and Beyond -- Mikel Artetxe, Holger Schwenk.

the papers show the power of many different languages used to create a same embeddings for all. it displays encoding techniques and train / test strategies and a new test set. It proves to be sota on most test set used. I uses a bi-LSTM encoder of 5 layers, 83 languages and an LSTM decoder  with skip connections 


## CytoGAN: Generative Modeling of Cell Images -- Imaging Platform Broad Institute of MIT and Harvard

this work uses a regular LSGAN to learn the important feature from a dataset of cell images. they show that it is not sota but can infer better latent factors which encode phenotypic information about the cell. both in the generator and discriminator. They show how to preprocess the image to get the best results. the work would need additional information to be reproducible.


## Pathway perturbations in signaling networks: Linking genotype to phenotype --Babu for Barth EPFL

_what about gene knockdown datasets... might be very interesting. 
drug interference data sets as well.
I heard of central regulators which are specific and specifically expressed in specific cancer cell lines and that knowing that information allows one to understand the specificities of the cell line (like its reaction to drugs etc..)_

In here we look at several different signaling pathways which have highly oncogenic potentials. looking at them via a What mutation, how it should work, what happens when mutations. How can it be fixed.
We are really looking at the causal explanation of a phenotype by a mutation/alt. splicing/ translocation/... .

## Pharmacogenomics of GPCR Drug Targets --  Masuho, Leonie J. Jahn, Kirill A. Martemyanov, David E. Gloriam, M. Madan Babu

Here we analyze how different drugs affecting primarily or secondarily the GPCR membrane receptors of cells can have different effects considering the naturally occurring mis-sense variation in the human population on these corresponding protein coding genes.

_how comme they never thought of doing the same in pharmacollogy??_
_what about the non coding variants in the population it will reflect also some differential effects in the signaling pathway and even variation in the proportion of membrane receptors_

## 

_I really want to see how the pipeline to integrate the entire G cycle looks like._


## Papers Gilchrist
### Combining Models of Protein Translation and Population Genetics to Predict Protein Production Rates from Codon Usage Patterns

### Explaining complex codon usage patterns with selection for translational efficiency, mutation bias, and genetic drift

### Estimating Gene Expression and Codon-Specific Translational Efficiencies, Mutation Biases, and Selection Coefficients from Genomic Data Alone

###  Quantifying codon usage in signal peptides: Gene expression and amino acid T usage explain apparent selection for inefficient codons

I had the time to read the papers you sent me and they were very good. The third one presented a great introduction to CUB and a good model which attains a very high score. I would guess that this model could not get the same score for other species. I still think that a model of CUB would always be reductionist as the CUB is a proxy for so many different processes and adaptations of the cell. The many fine grained Bayesian model that you present however seems to make sense and creating a model is to me the only way to test a theory. The ability to regress values such as the protein synthesis rate is impressive and it does not seem trivial to me that this should be the case. The model that you have developed seems very suited for answering questions about the CUB as shown for example in "quantifying codon usage in signal peptides". 

## Where genome biology is going next
multiple researchers giving their view of where genomics is heading

## A topological and conformational stability alphabet for multipass membrane proteins -- Patrick Barth

Here is the study of multipass transmembrane proteins which are composed of many transmembrane helices. they have a specific confirmation which is dictated by their sequence. interaction between helices yields the specific shape of thee multipass prot.
specific residues which help connect the helices and give them their shape seems to be coevolving, stabilizing the shape and are determinant of the topology. For the first time this study analyzed trimers of helices insetead of dimers.  


## Primer on Deep Learning in Genomics

## A guide to DL in healthcare -- Andre Esteva, Alexandre robicquet

Some simple yet necessary ideas about how one would best use DL in healthcare and what are the future and promises of it.

## Mammalian Genes Are Transcribed with Widely Different Bursting Kinetics

in this paper it is explained briefly (with more precision about the models in the supplementary materials) the rational behind bursting kinetics in mamlian genes. We look at a model going from in/activation; trancription rates; translation rates and degradations. using markovian prob. models. per coding genes. then correlates it with exeperimental fluo activity thanks to a poissonian noise model. the entirety of the model is then parametrized by EM algo thx to baum welsh algorithm. the computation of the states (bc it is a markov. model.) is done with the viterbi algorithm. The signal in the images were deconvolved using wavelet temporal analysis. the results described how different profiles of protein activity were highly periodic with different types of kinetics. also shown in the analysis of the states/params of the model for different mRNA. this difference could be seen also for similar genes accross cell lines.

## what are super enhancers? -- Sebastian Pott & Jason D Lieb
_very important_

Explainingwhat are enhancers. open questions about them at the functional level.
then turns out how to compute super enhancers. their possible differences with regular ones and possible similarity which would make them just reegular enhancers specific of the particular expression of the cell line.
it turns out to display 5 questions about super enhancer and if they truly are mechanistically different.
And a framework to find it out.

_how do gene dependancy relate to SEn? using the same Crispr screening technique
One Should Compute SEn without using merging of regular one according to the paper. Might help answering the question as well_

## Super-Enhancers in the Control of Cell Identity and Disease -- Denes Hnisz, Brian J. Abraham, Tong Ihn Lee
_very important_


_might be interesting to reuse softs such as DeepPeakCaller and DeepBind_

_Maybe one might find the equivalent of superENhancer for lesser TF type when looking only at these._

_Sen are concepts associated with TF master TF, enhancer, cell fate, cell differenciation/pluripotency (see for of Pr. Gioele La manno EPFL, transcription regulation (cis & trans) (also via enhancerRNAs), _

_it would be valuable to identify the master transcription factors that control all cell states._

_if alteration in superenhancer drive cell specificity. what if some cancer were some form of local valley in cell specificity out of which the cell can't escape. this could be seen by looking at differences in superenhancer region through stages of cancer or types of cancer from a same cell line through the eyeyes of what La Manno has done._

_when you look at Senh accross cell lines and cancers and you see ~ a thiord which are cell line specific. do the other 2/3 are shared accross cell? cell types? cell groups? random noise, i.e. not acual Senh?_

First the discovery that super enhancer are linked with cancer hallmark, disease SNPs, specific per cell types, linked with specific core transcription factors, miRNA ncRNA. might explain cell diff, fate, etc.. they create feedback loop. can be transcribed into eRNA (which may contribute to gene activation) and are not only enriched in TF but also in RNA Polymerase II, Cofactors, and Chromatin Regulators. It is also a dataset of 86 cell type (human) 

## Network In Network -- Min Lin, Qiang Chen, Shuicheng Yan

putting MLP instead of regular convolution for each layer of a CNN. ReLu then finishing by a global average pooling layer feeding to a logistic regression classifier.


## Selective Inhibition of Tumor Oncogenes by Disruption of Super-Enhancers -- Jakob Love, Heather A. Hoke, Charles Y. Lin

You have some enhancer of MYC, MCL1, IRF4, PRDM1 ... which are strongly bound by BRD4 and MED1. we know that reducing the level of BRD4 by using a JQ1 tratment which will lead to a bromodomain inhibition of BRD4 and thus restrict binding of itself and its coFactors. In many types of cancer cells. this leads to a selective desctruction of them and not of regular cells. This is explained in this paper by stating that these cells are known to have very strong super enhancers to these genes and thus it is places which relies more heavily on BRD4 and which are more essential to these cell lines. Giving ideas to explain and discover more oncogenic targets.

## ATARiS: Computational quantification of gene suppression phenotypes from multisample RNAi screens-- Diane D. Shao, Aviad Tsherniak, Shuba Gopal, Barbara A. Weir

The beginning of the DepMap, before large scale and demeter. Discovering how a lot of data can help uncovering gene dependency in cancer from rnaI. Using  a Matrix Factorization. Moreover as many RNAi can affect a gene. After it, a refinment step is performed to find a subset of best performing ones according to the profiles found by the matrix factorization problem.
showing ability to:
- identify fuctional relationship between genes
- identify nocel cancer associated genes.
- identify genomic predictor of gene dependency

_did not  get fig 4C ..._


## Pan-cancer genome and transcriptome analyses of 1,699 paediatric leukaemias and solid tumours-- Xiaotu Ma1, Yu Liu, Yanling Liu, Ludmil B. Alexandrov, Michael n. Edmonson

A paper recapitulating the creation a first analysis of 1699 pediatric leukimia tumors at the transcription and genomic level. understanding similarities and differencies btween them/ them and adult leukimia. and some interesting new genes and genetic features. Additionaly a more thoruough analysis of WT1 D447N. _for which I was not 100% confident on my comprehension_


## The landscape of genomic alterations across childhood cancers--Susanne N. Gröbner, Barbara C. Worst, Joachim Weischenfeldt Ivo Buchhalter, Kortine Kleinheinz, Vasilisa A. Rudneva Pascal D. Johann

Another presentation of a dataset containing a thousand tumours (most of them ALL and central nervous system related) with identification of regular driver genes, structural and CN variants and germline/somatic variants. with a study of the particular processes in childhood cancers as well as potential drug targets related to the discoveries listed here.

## A Landscape of Pharmacogenomic Interactions in Cancer-- Francesco Iorio, Theo A. Knijnenburg, Daniel J. Vis

A look at the pharmacogenomic landscape (response to 265 drugs) of 1,001 human cancer cell lines from 11,289 tumors points to new treatment applications for hundreds of known anti-cancer drugs. to determine:
- the extent to which cancer cell lines recapitulate oncogenic alterations in primary tumors.
- which oncogenic alterations associate with drug sensitivity, 
- whether logic combinations of multiple alterations better explain drug sensitivity.
- the relative contribution of different molecular data types, either individually or in combination, in predicting drug response

_here it seems that the gene expression data only helps to infer the cell type > thus the dependancy according to that. thus a two step model (cell type > specific sensitivity) might be more appropriate_
_Here I think you need to model some of the specific proteins to understand better what explains the sensitivity and what events (SNP, CNV, ...) might help you understand that. (see work from Patrick Barth)_
 
---
CFE  cancer functional events
RACS recurrently aberrant copy number segments

----

## Curiosity-driven Exploration by Self-supervised Prediction-- Deepak Pathak Pulkit Agrawal

_what about training on the ability to predict the distribution dynamics instead of just prediction error on the next state (else might be triggered by simple noise or stochastic distributions)_

agent is trained on minimizing the prediction error of state t+1 from state t and action t (_may be better with reusing all previous states in some form_)

_"the agent will be completly unperturbed by external factors" yet it seems very delicate for the agent to understand what will have future effect on him down the road. I guess the human brain does not do it this way._

_They should have tried to do parameters sharing._

## Master Transcription Factors and Mediator Establish Super-Enhancers at Key Cell Identity Genes-- Warren A. Whyte,1,4 David A. Orlando,1,4 Denes Hnisz

Very similar to the previous papers about super enhancers. Most of the new finding is in the title. 

>Super-enhancer formation appears to occur as a conse- quence of binding of large amounts of master transcription factors to clusters of DNA sequences that are relatively abundant across these large domains. Theses domains featiure CDS which are the core constituent of Cell Identity.


_it seems that super enhancers activate cell identity by the type of genes they bind to. However it seems that it is always the same master. What plays on the differences? (initial parameters/ TF concentration?/other non master TF) can we reprogram cells using these TF value?_

_given that cancer seems to be something that evolves really quickly over time from a regular cell (which in case of children might have a propension to go so). what about using a flow model on the cell's transcriptomics/genomic to understand the flow of cancerisation as a differenciation. You could see it going to a probabilistic valley with canyons and taking a path which will increase the likelyhood of turning into a cancer. Then, why not look at the cell before it become a full on cancer and see the possible differences in pathway and create things that attack cells in this particular state._

----
EPUs enhancer-promoter unit

----
MACS CHIp analysis
BOWTIE alignment
CAMs cell–cell adhesion molecules
----


## The Hallmarks of Cancer-- Douglas Hanahan* and Robert A. Weinberg

the foundationnal paper presenting the 6 hallmarks of cancer:
- limitless replication
- evading apoptosis
- insensitivity to antigrowth signals
- self sufficiency in growth signals
- tissue invasion (metastasis)
- sustained angiogenesis
 via a suite of possible mechanism.

showing that cancer should not happen with this likely hood but that instead cells when loosing specific sets of reparing/stability genes or phagocytosising cells (which may incorporate some instable DNA)) may undergo, with much more likelyhood: cancer.

> we look ahead 10 or 20 years to the time when the diagnosis of all the somatically acquired lesions present in a tumor cell genome will become a routine procedure. By then, genome-wide gene expression profiles of tumor cells will also be routine. With all this information in hand, it will become possible to test definitively our proposition that the development of all types of human tumor cells is governed by a common set of rules such as those implied by the six acquired capabilities enumerated here.

*really a paper about understanding cancer 101*

----
GS growth signal

----

## Coming of age: ten years of next- generation sequencing technologie--Sara Goodwin, John D. McPherson and W. Richard McCombie

a presentation of the sequencing technologies with their pros and cons and an explanation of how they work. Then a similar deeper presentation for all NGS technologies. a repartition according to differences and similarities.  the new long read sequencers from PACbio and Oxford nanopore seems extremelly powerfull and impressive. 	

*a lot of definitions and explanations in this paper (must read)*

-----
SBL sequencing by ligation
SBS sequencing by synthesis 
ssDNA single strand != dsDNA
dNTPs deoxynucleotide primer
CRT cyclic reversible termination
SNA single-nucleotide addition
ZMW zero-mode waveguides 

----

## High-performance medicine: the convergence of human and artificial intelligence-- Eric J. Topol   

presenting the use of DL for radiology, pathology, dermatology, ophthalmology, cardiology, gastroenterology, cardiology

a very good categorization of current companies and techniques and a lot of actual comparative data against clinicains and with clinicians

>A deep-learning algorithm for lung cancer digital pathol- ogy slides not only was able to accurately classify tumors, but also was trained to detect the pattern of several specific genomic driver mutations that would not otherwise be discernible by pathologist


## Generating Focussed Molecule Libraries for Drug Discovery with Recurrent Neural Networks-- Marwin HS Segler1, Thierry Kogej, Christian Tyrchan and Mark P Waller

using an RNN generator very similar to the ones used modelling language, to model molecules (no conformation, only placement). althought this work is nice and highlights what can be done with substantial results to show. it may lack information on conformation and it does not seem to use every information available to biochemists. It uses transfer learning and a measure of fitness which allows it to be efficient. it gives some informations of the goals in this field. 

It may be problematic however that it does not provide radically new molecules but quite similar ones. ways to present and tests such data does not seem to be present yet. The author do present good future work ideas and skepticism.

----
ECFP extended connecticvity fingerprint
TPM target prediction model
ESC embryonic stem cells

----


## Core Transcriptional Regulatory Circuitry in Human Embryonic Stem Cells

specific papers pre-Superenahncher discovery where it displays how core TF create a feedforward circuitry in ESCs and how it is the core circuitry defining their identity.

## Selective gene dependencies in MYCN-amplified neuroblastoma include the core transcriptional regulatory circuitry-- Adam D. Durbin  Mark W. Zimmerman Neekesh V. Dharia

this paper represent a deeper work on using CRC as tools to guess gene dependencies in a specific cancer type. It proved very efficient and puts itself in the framework of discoveries linked with super enhancers. 


---
CRC core regulatory circuitry
ATAC assay of transposase accessible chromatin


---

## Neuroblastoma is composed of two super-enhancer- associated differentiation states-- Tim van Groningen, Jan Koster, Linda J Valentijn, Danny A Zwijnenburg, Nurdan Akogul, Nancy E Hasselt, Marloes Broekmans

In this paper, people from the broad show that analysing tumors. two types of archetypes coexist from distinct original cell lines. They can be differentiated with Super enh profiling and by understanding their circuitry, changed from one state to another. The cells have been shown to present similar effect in vivo with one archetype being more chemoresistant. Leading path to new screenings and therapies.


*here it seems they identified only two archetype instead of 3...*

*it seems to make some sense and to be quite crazy that influencing just some TF would allow reprogramming of many cell types.*

----
IHC  Immunohistochemistry

----

## Interaction Networks for Learning about Objects, Relations and Physics-- DeepMind

Nice paper about predicting the future of physical interaction by combining relational reasoning, simulation and NN. (no deep learning here!) It provides inexact but extremelly believable results in many different simulation tasks and could learn non newtonian dynamics. 
*It is a first step/idea to many other interesting directions*

## Precision Targeting of BFL-1/A1 and an ATM Co- dependency in Human Cancer-- Rachel M. Guerra, Gregory H. Bird, Edward P. Harvey

> Guerra et al. constructed an exquisitely selective BFL-1 inhibitor capable of covalent BFL-1 targeting and cellular penetrance without membrane disruption. Mining a genetic dependency database revealed a spectrum of BFL-1 dependency in cancer and an ATM co- dependency in AML, prompting the combination of BFL-1 and ATM inhibitors to achieve synergistic cytotoxicity.

*I don't understood all the nuances of the paper, especially the design and thought process displayed in the results.*

*The papeer could have needed a bit more explanation on the underlying process it is trying to solve (schematics to avoid repeating long enumeration of action of protein)*


Here the author reuse and modify a NOXA protein to create one that will very specifically bind and inhibate BFL1 (with D-NA (at N term)) and thus reactivate the apoptotic route of the cell. They use staple peptide to consolidate the protein SAHB15 and subsequently modified aa for less hydrophobic ones to create a protein that could enter the cells without destroying them. they then undertakent to test variation, precision etc.. of this protein to confirm its pharmacological relevance in BFL1 and ATM co dependant ccl

---------
ATM ataxia-telangiectasia-mutated

CCL cancer cell line

---------

## Pioneer factors govern super-enhancer dynamics in stem cell plasticity and lineage choice-- Rene C. Adam, Hanseul Yang, Shira Rockowitz, Samantha B. Larsen, Maria Nikolova, Daniel S. Oristian


*what about computing superenhancers from raw sequence data by using a DL tool.
CNN on 250k bp (should reuse b&w like parameters) or maybe multiply values into one. 2^10 by combining 5 values)*

Here by using Hair Folicule stem cell as a proxy. researchers showed the impact of the pionner factor SOX9 on stem cell plasticity by activating other super enhancer link to the HFSC plasticity by initiating H3K27ac. Going with more precision in the superenhancer study for a particular/different problem.

----
pioneer factors: dominant in their ability to engage silent, unmarked chromatin and initiate the recruitment of other factors, thereby imparting new function to regulatory DNA sequences. 

[acetylation](https://en.wikipedia.org/wiki/Histone_acetylation_and_deacetylation)

TACs Transit-amplifying cells

GREAT soft(go function enrichment)

HOMER soft(motif enrichment)

---


## The Evolving War on Cancer-- Daniel A. Haber, Nathanael S. Gray and Jose Baselga

a review of what has been done. impacts and challenges, even reasons for the past 40yr war on cancer. what is the state of things in 2011 and what is the roadmap for the next 10-20 yrs. what will be the challenges awaiting us.


## Statistical Methods in Integrative Genomics-- Sylvia Richardson, George C. Tseng, and Wei Sun

> 1. All models have their explicit and implicit assumptions. Model fitting to the underlying data structure largely determines the success of omics data analysis.
2. In data integration, certain biological mechanisms and prior knowledge are often known across different omics data. Proper modeling of such prior knowledge is crucial to enhance statistical power and identify biologically interpretable results.
3. IncorporatingpriorbiologicalinformationusingBayesianhierarchicalmodelingisavery powerful method of data integration.
4. Integration of multiple types of omics data involves ultrahigh-dimensional problems. Feature selection and its related model selection problem are major issues when devel- oping a novel method.
5. Network-based methods are effective approaches to integrating multiple types of data and biological knowledge.

*we have to know tumor purity*
*hoizontal<->vertical* from stat to bio

- Clustering
presentation of METABRIC. foundational for tumor heterogeneity detection. MDI & BCC for bayesian clustering integrating many datasources.
some fou

- Regression
regressing on large p small n datasets or multi omics/response models. integrating also prior (integration) information from given knowledge
with bayesian modeling of eQTL variation impact on gene expression


- Grahical models (same as regression, integrating structural relationship prior information)
with the representation of a miRNA effect on gene expression
with the representation of eQTL impact on gene expression

PARADIGM: to model the DAG of the interation between CN, Gene expression, protein abundance, activity of complex, prot, etc...) and finds the value of unobserved variable given observed ones. 

OmicKriging: predicting phenotype from a set of phenotype's similary matrix

CONEXIC (copy number and expression in cancer) to detect modules in which copy number affects the expression of a driver gene, which in turn regulates the expression of a group of genes.

HotNet: identifies significantly altered subnetworks in an interaction net- work by a network diffusion approach, which can be understood as a random walk on a gene-gene interaction graph. In other words, a somatic mutation in gene A may also affect gene A’s neighbors in the interaction graph. After network diffusion, HotNet evaluates the frequency of a subnetwork being altered across patients and find those subnetworks that were recurrently altered. Network diffusion provides a network-smoothed version of the consequences of somatic mutations. clustering the network-smoothed mutation profiles by nonnegative matrix factorization


-----
 Zellner’s g-prior: give $y_{i}=x_{i}^{\top }\beta +\varepsilon _{i}.$
 Zellner's g-prior for ${\displaystyle \beta } \beta$  is a multivariate normal distribution with covariance matrix proportional to the inverse Fisher information matrix for ${\displaystyle \beta } \beta$ .
 like so : ${\displaystyle \beta |\psi \sim {\text{MVN}}[\beta _{0},g\psi ^{-1}(X^{\top }X)^{-1}].}$

-----

## The Cancer Genome Atlas Pan-Cancer analysis project-- The Cancer Genome Atlas Research Network, John N Weinstein, Eric A Collisson, Gordon B Mills, Kenna R Mills Shaw5, Brad A Ozenberge...

really a presentation of TCGA and its goals and objectives as of 2013. Most specifically a project to computationally analyse a set of ~3000 tumors from 6 data types (RPPA meth CN mut miRNA eRNA) from 12 tumor organ types.

> • What is the spectrum of nucleotide- and dinucleotide-level changes associated with different carcinogenic etiologies (for example, tobacco, pathogens or inflammation) operating in different parts of the body?
• Will integration of additional data sources, including additional tumor types from TCGA and other projects, increase the power of analysis in useful ways?
• How can characterization based on molecular changes complement pathological analysis for classification of cancers into tumor lineages with potentially different clinical management?
• Can molecular profiles effectively categorize cancers for therapeutic decision-making?
• Are there predictive expression-based signatures for genomic events that transcend tissues, reflecting pathways disrupted by the alterations?
• Will comprehensive protein analysis through emerging mass spectrometry approaches in the Clinical Proteomic Tumor Analysis Consortium (CPTAC) and other efforts extend the power of the genomic, transcriptomic and proteomic analyses in TCGA?
• Will whole genome analysis demonstrate the influence of mobile elements, mutations in non-coding regions and connections to constitutional risk-associated loci?
• How are changes in protein families distributed across different tumor types?
• Are aberrations in specific protein domains or pathways distributed differentially across tumor lineages?
• Beyond the known examples, including in cervical, head and neck, esophageal and hepatocellular cancers, can we identify other cancer types that show virally mediated initiation?
• Are bacteria associated with different cancer lineages (as Fusobacteria are in colorectal cancer43)?
• Can the answers to any of these questions help in the design of novel therapies and clinical trials, with the ultimate goal of improving patient outcomes?


## The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensitivity-- Jordi Barretina, Giordano Caponigro, Nicolas Stransky, Kavitha Venkatesan, Adam A. Margolin, Sungjoon Kim, Christopher J. Wilson4, Joseph Leha, Gregory V. Kryukov, Dmitriy Sonkin, Anupama Reddy, Manway Liu, Lauren Murray, Michael F. Berger, John E. Monahan...

Here there is a presentation of CCLE and examples of what can be done by using CCLE's data (with additional experiments) to understand relationship between genes plasma cell lineage correlated with sensitivity to IGF1 receptor, AHR expression was associated with MEK inhibitor efficacy in NRAS-mutant lines and SLFN11 expression predicted sensitivity to topoisomerase inhibitors. using elastic net modelling studies identified key pre- dictors or mechanistic effectors of drug response.




## DeepNano: Deep recurrent neural networks for base calling in MinION nanopore reads--- Vladimir Boza,Broňa Brejova, Toma svinař*

a simple vanilla bidirecRNN to associate bp to reading events from the oxford nanopore minION machine. it achieves similar results to oxford's LSTM algorithm while being opensource and faster. 
it uses longrange relationships information to estimate the actual values. 

*some things are not explaned nor well document (maybe in the code).*
*further tests of the accuracy accross more data types etc would be essential to assess the actual quality of this algorithm*

## Systematic investigation of genetic vulnerabilities across cancer cell lines reveals lineage-specific dependencies in ovarian cancer -- Hiu Wing Cheunga, Glenn S. Cowleyb, Barbara A. Weirb, Jesse S. Boehmb, Scott Rusinb, Justine A. Scottb, Alexandra Eastb, Levi D. Alib, Patrick H. Lizotte...


after using the project achilles data and making specific analyses. the researchers found that PAX8 was a specific dependency in ovarian cancers.

----
woe weight of evidence

---


## Systematic identification of genomic markers of drug sensitivity in cancer cells-- Mathew J. Garnett, Elena J. Edelman, Sonja J. Heidorn, Chris D. Greenman, Anahita Dastur, King Wai Lau, Patricia Greninger...

a presentation of what will become project PRISM. using results from 130 compounds to 600 CCL. finding known and a lot of unexpected correlations. using regular MANOVA analysis, elastic net prediction to find most predictable transcriptionalvfeatures for drug sensitivty.


*interesting use of some algos*

---
MSI: microsatelitte instability

capillary sequencing: similar to electrophoresis with a laser that makes each nucleotide shine a specific color which helps in sequencing the dna

PICNIC: predict copy number from microarray data

RMA: Robust Multi-Array Average (for gene expression data)

heteroscedasticity variability in variance

---

## Advancing the aging biology toolkit-- TROY K COODY AND ADAM L HUGHES

a presentation from Calico of a new method to segregate old cells (here for yeast) in order to do better analysis between the two and understand what might explain aging for further research. 

## Models of human core transcriptional regulatory circuitries-- Violaine Saint-André, Alexander J. Federation, Charles Y. Lin

Here is described a framework to guess the CRC from simple CHIP data of various human tissues. to understand cell types and more about the CRC from this data. It shows this framework mainly in analysing ESC but also provide the same analysis on 80 different cell type.


*can we guess CRC and SE from simple CHIP data of each cells? 
can we infer the cell type from it? can we infer the cell type from only a small subset of RNAs which encodes CRC?*

*use it for the next further trial of my data*
https://hoffmanlab.org/proj/virchip/

----
CRC: core transcriptional regulatory circuitry

hESC: human ESC
CNA: copy number alteration

RTK: receptor tyrosine kinases
PI3K: phosphoinositide 3- kinase

----


## Pan-cancer network analysis identifies combinations of rare somatic mutations across pathways and protein complexes-- Mark D M Leiserson, Fabio Vandin, Hsin-Ta Wu, Jason R Dobson


a network analysis using a heat diffusion model accross network of interconnected genes identifies mutation (heat) that display important network for the cancers accross thousands of cancer and tens of cancer types. this analysis focus on 3 interesting pathways: 
- SWI/SNF chromatin-remodeling complex
- BAP1 complex
- cohesin and condensin complexes
- MHC class I proteins
- the telomerase complex

they also found 92 mutated gene with usually low score in non networked single gene analysis

It might be used on any gene data with a value measure for each gene!

*Q: How do they guess link to cancer from only presence in the netwtork?*

*N: why don't we stop looking at what is mutated and start looking at what is not mutated? like looking at what specific circuitry cancers rely upon to stay alive, that other regular cells might not need?*

---
GSEA gene set enrichment analysis

---

## Auto-Encoding Variational Bayes -- Diederik P. Kingma, Max Welling

presentation of an estimator of variational lower bounds for approximate inference with continuous latent variables. and the presentation of an Auto Encoder (like) variational bayes which learns an even beter approximate inference using SGVB. For the case of i.i.d. datasets and continuous latent variables per datapoint.


## Towards systematic functional characterization of cancer genome-- Jesse S. Boehm, and William C. Hahn, BroadInstitute

A demonstration of the many techniques to perform functional characterization of genes: 
- RNAI
- ORF
- transposons
- small molecule
- (now much more, like crispr screens etc...)

*Q: I don't really get the concept of depleted shRNA, don't we only look at the amount of cells? do we look at how many shRNA are left to have a notion of usage?*

---
Transformation: The process by which a normal cell acquires cellular phenotypes of a cancer cell

ORF: Open Reading Frame

xenograft: transplanting tissue into another organism
PDX: patient derived xenograph 

primary cells: cells coming directly from living tissues

---

## A Combination CDK4/6 and IGF1R Inhibitor Strategy for Ewing Sarcoma -- Lillian M. Guenther, Neekesh V. Dharia, Linda Ross, Amy Conway1, Amanda L. Robichaud...

using ORF resistance screens and knowledge from the achilles project with in vitro and xenograft models.

*it presents a wide variety of tests used to demonstrate such things using mainly experimental wet-lab(biocell) procedures*



----
SA-b-gal staining: detecting secent cells (dying)
nucleation: self assembly 

---

## Core Transcriptional Regulatory Circuit Controlled by the TAL1 Complex in Human T Cell Acute Lymphoblastic Leukemia-- Takaomi Sanda, Lee N. Lawton, M. Inmaculada Barrasa, Peng Fan, Holger Kohlhamme... 

identifying it with other TF binders and position allowed to find a feedback circuit comprised of GATA3, and RUNX1 activating MYB. which shows the supreme importance of TAL1 in this case. In fine understanding some of the mechanisms behind T ALL. 

---
primagraft: xenograft without any pre in vitro culture

CCRF-CEM: 	A T lymphoblastoid line obtained from the peripheral blood of a 4 year old Caucasian female with acute lymphoblastoid leukaemia. These may be grown to a high density in a spinner type suspension culture. Cells are reported to be free of virus particles as determined by electron microscopy.

ectopic: abnormal


---


## V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation-- Fausto Milletari1, Nassir Navab, Seyed-Ahmad Ahmadi

Presenting a new model that relies solely on 3D convolution/deconvolution to present a heat map of probability to be in foreground. It achieves very good results but might lack training data compared to 2D systems which can reuse learnings. It uses a lot of feature wise transformation and no maxpooling(only conv).

*N: it seems that it takes too few pixels to learn interesting features (might take NxMxM pixels with N<M)


*N: important use of [featurewise transfo](https://distill.pub/2018/feature-wise-transformations/)*

---
foreground: the ROI (else background)

---


## CRISPR-Cas9 screen reveals a MYCN-amplified neuroblastoma dependency on EZH2-- Liying Chen, Gabriela Alexe, Neekesh V. Dharia, Linda Ross, Amanda Balboni Ini...

Here we can see an analysis that start to be recurrent to other related papers where results from achilles and now from crispr screens allows the test of a pathway / transcruption factor. here EZH2 in MYCN amplifyed neuroblsotame. The analsysis tries to identify druggable mechanisms, correlations to other protein expressions and TFs. 

> We assessed the clinical relevance of EZH2 inhibition, both in vitro and in vivo, using multiple perturbation approaches, such as selective small-molecule EZH2 inhib- itors, shRNA-mediated knockdown, and CRISPR-Cas9 knockout. We also studied the epigenetic networks and their response to EZH2 inhibition in MYCN-amplified neuroblastoma and explored the underlying molecular mechanisms of the sensitivity to EZH2 inhibitors using biochemical, genomic, and epigenom- ic approaches.


## The variability of expression of many genes and most functional pathways is observed to increase with age in brain transcriptome data.-- Veronika R. Kedlian, Handan Melike Donertas, Janet M. Thornton

Knowing that there is evidence for increaser in variability of expression accross cell lines in the human genome with age. Researchers looked at brain cells (frontal/pre frontal) and discovered a slight increase in the variability of expression accross different techniques (measures of variations, comparisons)
They *most importantly* did a go search and discovered that this increase in variability was mostly for genes related to 
ageing processes.

----
BP GO – Biological Process Gene Ontology,
DE – differentially expressed genes,
DV – differentially variable genes,
Dvar – measure of change in the expression variability with age, GO – Gene Ontology,
GSEA – Gene Set Enrichment Analysis,
IQR – interquartile range,
KEGG – Kyoto Encyclopedia of Genes and Genomes, PMI – post-mortem interval,
QN – quantile normalization,
RIN – RNA integrity number,
Rho – Spearman correlation estimate,
SVA – Surrogate Variable Analysis

-----

## EWS/FLI Confers Tumor Cell Synthetic Lethality to CDK12 Inhibition in Ewing Sarcoma-- Amanda Balboni Iniguez, Bjorn Stolte, Emily Jue Wang, ...

> Here we report that Ewing sarcoma is a disease with exquisite sensitivity to the covalent small-molecule CDK7/12/13 inhib- itors, THZ1 and THZ531. These compounds act, in part, through inhibition of CDK12 and the subsequent suppression of genes involved in DNA damage repair

explained by the fusion protein EWS/FLI

## Cell Detection in Microscopy Images with Deep Convolutional Neural Network and Compressed Sensing-- Yao Xue and Nilanjan Ray

using compressed sensing in two different manners to encode the position of features in microscopy imaging of cells thus reducing dimensions and possible prediction error from a vanilla CNN. looking at theoretical proof the CNNCS works and experimental demonstration on different datasets achieving sota results.


## COSMIC: exploring the world’s knowledge of somatic mutations in human cancer-- Simon A. Forbes, David Beare, Prasad Gunasekaran, Kenric Leung, Nidhi Bindal, Harry Boutselakis, Minjie Ding...

A description of the COSMIC database



## IMPACT: Genomic Annotation of Cell-State-Specific Regulatory Elements Inferred from the Epigenome of Bound Transcription Factors-- Tiffany Amariuta, Yang Luo, Steven Gazal, Emma E. Davenport...

A similar work to what Brendan Frey has been doing with neural networks but with logistic regressing Except here, it is trying to infer bound AND unbound region from sequence and more explicitly, infer regulatory power of each nucleotides for a particular cell state and TF given a set of regulatory features such as open Chromatin, methylation marks etc...


## Extensive Variation in Chromatin States Across Humans-- Maya Kasowski, Sofia Kyriazopoulou-Panagiotopoulou, Fabian Grubert, Judith B. Zaugg,Anshul Kundaje, Yuling Liu, Alan P. Boyle, Qiangfeng Cliff Zhang, Fouad Zakharia, Damek V. Spacek, Jingjing Li, Dan Xie, Anthony Olarerin-George, Lars M. Steinmetz, John B. Hogenesch, Manolis Kellis, Serafim Batzoglou

Paper presenting the early finding in chromatin variation accross human genre without much variation in gene expression (can be related to cell type/state?). Some marks are highly inherited. They also showed that places of this variability are also high GWAS region. Which is a base results of enhancers and chromatin modification


## ChromHMM: automating chromatin- state discovery and characterization-- Jason Ernst, Manolis Kellis

A presentation of ChromHMM which is a markovian models to infer chromatin modification and create chrom states from reads from Chip seq of this chromatin. (denoising kinda?)

## Histone modifications at human enhancers reflect global cell-type-specific gene expression-- Nathaniel D. Heintzman, Gary C. Hon, R. David Hawkins1, Pouya Kheradpour, Alexander Stark, Manolis Kellis...

another landmark paper from 2009 explaining the viariability in chromatin modification, its link with TFBS regulatory power and (for some of them H3K27 for ex) its implication in specific cellular states.

## Strelka2: fast and accurate calling of germline and somatic variants-- Sangtae Kim, Konrad Scheffler, Aaron L. Halpern, Mitchell A. Bekritsky

a variant caller for germline and somatic sequencing. Improves liquid model analysis mainly since take in account P() of being contaminated. It models sequencing noise via e (1) the genotype probability computed by the core variant probability model, (2) root-mean-square mapping quality,(3) strand bias, (4) the fraction of reads consistent with locus haplo- type model, and (5) the complexity of the reference context.


## STAR: ultrafast universal RNA-seq aligner--PacBio

star is the first and most used algorithm specifically designed for aligning rna seq data (especially paired end reads) from 3rd gen sequencer (longer reads). it is 30 times faster than previous algo and uses a two step algo:
- seed searching (Maximal mappable array) implemented through uncompressed suffix arrays which account for mismatches, low quality read ends, multiple solutions and gaps (introduced by splicing)
- Clustering, stitching and scoring based on proximity of each read, accounting for overlapping reads and distant reads based on a user provided threshold

## STAR-Fusion: Fast and Accurate Fusion Transcript Detection from RNA-Seq-- Brian J. Haas1, Alex Dobin, Nicolas Stransky, Bo Li, Aviv Regev...

star fusion uses the output from star on porblematic mappings to reprocess the reads in order to find potential fusions, remmapping based on coordinate overlap (using interval trees). 
Finally it filters the output by removing fusions with minimal supports (depending on the support type), merging closeby fusions, removing lowly supported isoforms. removing too similar gene fusion isoforms and when there is too many fusion for the same gene.


## Title: Exploring genetic interaction manifolds constructed from rich phenotypes -- Thomas M. Norman, Max A. Horlbeck, Joseph M. Replogle

A presentation of a vision to repoduce from perturb seq screen + transcriptome analysis, the genetic interaction of each genes. From this, guess the manifold of cell state. 
They present a first simple and criticable example of it but address more a vision and an idea than anything else. Are perturb seq accurate enough for guessing interactions? Can all possible state be estimated from such method?


## RSEM: accurate transcript quantification from RNA-Seq data with or without a reference genome-- Bo Li, Colin Dewey

this package used in the GTEx pipeline uses EM algo to quantify gene expression given alignment or reconstructing the transcriptome from scratch. EM is mainly used to take in account isoforms and give Bayesian posterior probability. It takes in account quality score of reads and gives CI. It can also be used as a generative model from the weights learnt from each gene
>Taking advantage of this module, we have deter- mined that a large number of short SE reads is best for gene-level quantification, while PE reads may improve within-gene isoform frequencies for the mouse and human transcript sets. 


## [Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples](https://www.nature.com/articles/nbt.2514)


## NGSEA: network-based gene set enrichment analysis for interpreting gene expression phenotypes with functional gene sets-- Heonjong Han, Sangyoung Lee, and Insuk Lee

This method is using the GSEA method (with AE) and rescore these by adding the average value of their connected gene in the network given by https://www.inetbio.org/humannet/ they then showed that it was improving on regular GSEA and discovered more data than what Broad's Cmap found for drug targets for example.   


## Reverse engineering cellular networks-- Califano Lab (ARAcne)

Presentation of this algorithm that can compute Mutual information between pairs of genes categorized by concentration of their related output molecules. This then NxN matrix can then be used to find networks. these are then filtered on confidence interval and DPIs to create resulting network. the more condition on the cell the better the results. *might be interesting to use on Apollo data*


## limma powers differential expression analyses for RNA-sequencing and microarray studies-- Matthew E. Ritchie, Belinda Phipson, Di Wu...


a presentation of the tool suite based on analysis of count data from gene products of different assay types. Based on a GLM taking in account a wide range of dependencies between genes, experiments, assays etc.. and allowing to analysis data at all stages of processing. 
It is presented pre processing stage of RNA seq and micro array data. DE computations. Expr. Prof. Association, Hypthesis testing


## An oncogenic super-enhancer formed through somatic mutation of a noncoding intergenic element-- Marc R. Mansour, Brian J. Abraham, Lars Anders, Alla Berezovskaya, Alejandro Gutierrez, Adam D. Durbin

A following paper on the reason behind an overexpression of a TF which drives oncogenecity in AML, which can be explained by the binding of MYB opening chromatine and  due to a mutation on non coding region creating an MYB TFBS. 


## [Aging is associated with a systemic length-driven transcriptome imbalance](https://www.biorxiv.org/content/10.1101/691154v1.full)
high length transc. is associated with gene regulation and dna binding. It may be seen as a non critical state of the cell. This is caused by the many different insults in the cell that forces it, little by little to act in this critical state it cannot escape.


## Predicting Splicing from Primary Sequence with Deep Learning-- Kishore Jaganathan, Sofia Kyriazopoulou Panagiotopoulou, Jeremy F. McRae, Siavash Fazel Darbandi, David Knowles, Yang I. Li, Jack A. Kosmicki, Juan Arbelaez, Wenwu Cui, Grace B. Schwartz, Eric D. Chow, Efstathios Kanterakis, Hong Gao, Amirali Kia, Serafim Batzoglou, Stephan J. Sanders, and Kyle Kai-How Farh

[presentation](https://docs.google.com/presentation/d/1uMa0qYcTopxR6AQVouirs_MDCnCEvw5Wls5Ap_FUtCY/edit#slide=id.g59623d53cc_0_81)


## Network-based inference of protein activity helps functionalize the genetic landscape of cancer-- Mariano J. Alvarez, Yao Shen, Federico M. Giorgi, Califano Lab...

*Aracne outperforms Chip experiments, only with RNA seq data*
-> does not get the same information thought: Regulators and regulons is different from TFB and DNA acetylation
Knowing regulons (genesets regulated by a regulator) we can then express a set of statistical analysis whereby looking at rna seq data, estimating the effect of regulons, from the expression of genes and of regulators of these genes. trying to remove other effects. this is done by comparing RNAseq to other batches of RNA seq to get predictive power. Then can be used Enrichment analysis test on ranks of expression to determine the effect of specific genes on regulons and specific regulons on genes. This acts as a network inference of "protein" (not really) "activity" 
An interesting thing is to be able to infer mutations that are likely to cause up or down regulation effect in this network. (CCLE)

All in all it tries to unsupervisely attain the same result as CRC analysis (it might get btw more predictive power if using a hiererchical system based on CRCs(and here you need ChIP))


## [Three-dimensional total internal reflection fluorescence nanoscopy with sub-10 nm resolution](https://www.biorxiv.org/content/10.1101/693994v1.full)

getting sub-10nm resolution in the 3D. an amelioration from super res DNA paint. by having a computation of distance to both emiting surface and receiving surface bu knowing the internal physics of the two. 
enabling the direct recognition of protein assemblies at the molecular level.


## Inferring protein 3D structure from deep mutation scans-- Nathan J. Rollins1,5, Kelly P. Brock1,2,5, Frank J. Poelwijk

Using mutation scans where mutating and translating an rna will lead to a protein of a likely different affinity to a kown bindinig protein. If the change of two position leads to a different change expected from adding the unique change at these two positions. Then we expect the two regions to be near each other in the protein.
Using that they were able to prove that it works for region of highest increase. But did not show recreation of known protein structure from this data. 


## Deep learning at base-resolution reveals motif syntax of the cis-regulatory code-- Kundaje lab

> These results indicate that while local sequence context (1 kb) is sufficient to accurately capture the shape of ChIP-nexus profiles and positions of binding footprints, longer sequences or other measurements such as local chromatin state may be required to better predict TF occupancy (45)

Using a CNN with deconv layer in the end to predict binding profile from sequence based on chip exo data (like chip seq but on a per bp basis). They found it learnt syntax specific binding profile. most of the time unregarding on the cell type (i.e. the current binding profile which is also influenced by the chromatin state). Inspecting the learnt parameters with many toolings and domain knowledge. They could find cooperative binding in step specific manner based on motifs spacing, motif linked to binding of other TFs, matching footprints. They found specific binding to tRNA genes of oct4. influence of transposons and filtering of them based on Information content of the learnt motif instances. periodic patterns in nanog binding showing behavior of nucleosome unwinding. All in all making of rules of the cis regulation syntax shown in theory and some experiment. such as the TF collective model, billboard model enhanceosome model. 


## Hallmarks of Cancer: The Next Generation-- Douglas Hanahan1,2,* and Robert A. Weinberg3,*

We present again the 6 hallmarks, with new major pathways insights into each with a clearer picture of the linked cell circuitry. It also showed 2 additional hallmarks and 2 enabling characteristics that have emerged in the past decade: reprogrammation of the energy metabolism, evading immune destruction, genome instability tumor promoting inflammation. A new view on the importanfce of the tumor micro environment s gven with CSC, endothelial C, Pericytes, Immune infla. C, Cancer Assoc. Fibroblasts, C of the tumor stroma..
And a view of the resulting extracellular signaling network. which drives, e.g. metastatic dissemination.  
Summarizing the research and knowledge in cancer biology of the past 15 years it shows the promise of targeted therapies and how to think about them and the future of cancer research.


## Next-generation characterization of the Cancer Cell Line Encyclopedia-- CDS

Here is presented a brief summary of the depmap omics project (previously CCLE), trying to do multi omics analysis of thousands of cancer cell lines. Here Mahmoud Ghandi correlated each different dataset with an other or with exome wide RNAi screens (project achilles) to find a some biological signal. 


## Off-target toxicity is a common mechanism of action of cancer drugs undergoing clinical trials-- Ann Lin @CDS JC

It seems to be a wake up call for pharmaceutical companies and an example of zombie effect in research. Some stragihtfoward test showed that the mechanism was off target for RNAi discovered dependencies and that the drugs were, as well. It showed a lot of the reasons why and hopes to place the burden of proof to drug companies. to recentrate efforts on understanding MOA and to get more big data information on rnai and use cripr tool as much as possible today.


## Scalable whole-exome sequencing of cell-free DNA reveals high concordance with metastatic tumors-- Viktor Adalsteinsson, Gavin Ha, Samuel Freeman, Atish Choudhury

IN this document, it is shown that with sufficiently good models of quality of DNA from blood biopsies, it is possible to achieve very similar results to regular DNA analysis of biopsies. This is proven by doing correlation analysis and using the data for application of target discovery, neoantigen therapies. Moreover it is shown that by its broad sampling of the body's activity, cfDNA seems to be better in discovering subclonal population and finding mechanism of resistance of these populations, thus allowing better prediction of resistance to therapies


## Organization and regulation of gene transcription-- Patrick Cramer

A review of the mechanism of gene transcription with chromatine and transcription factor at the biomolecular level. Making sense of transcription initiation, chromatine openning, transcription pausing, splicing, end of transcription and the auto organization of TF into condensates at specific tads to recruit the T Initiation C and others, to recruit the T elongation Factors.


## Dynamic regulation of transcriptional states by chromatin and transcription factors-- Ty C. Voss and Gordon L. Hager

This paper presents the idea that fine grained transcriptional modification occurs often and starts to be discovered with new imaging techniques and modeled. This can only occurs thanks to   chromatin remodelers allowing regions to be accessed by transcriptional factories. It also shows the machinery in the context of transcriptional burst and hit and run model. with cobinding explanation and the multi range of inhibition.


## Liquid versus tissue biopsy for detecting acquired resistance and tumor heterogeneity in gastrointestinal cancers-- Aparna R. Parikh, Ignaty Leshchiner, Liudmila Elagina

showing off the ability of blood biopsy to detect a lot of clonal and sub clonal population and find some of the mutations and copy number relevant for cancer resistance mechanisms. allowing to find a better set of targeted therapies. (in depth)


## Activity-by-Contact model of enhancer specificity from thousands of CRISPR perturbations-- Fulco, Lander..

A presentation of a new model of enhancer-gene interaction based on simple dynamics extracted from thousands of crisprI experiments on enhancers.


## Passenger Hotspot Mutations in Cancer-- Julian M. Hess, Andre Bernards, Jaegil Kim

a presentation of a model of bias in mutations on a bp level a contrario to most models on gene level. This is helped by the amount of wes profiling of cancer tissue. They show that some base level bias is at play based on simple metrics and provide a new statistical model to estimate background noise based on base level information of closest bases and test it on bases of known effect (deleterious in cancer genomes) log normal poisson 


## Scaling computational genomics to millions of individuals with GPUs-- Amaro Taylor-Weiner, François Aguet

They used pytorch and tensorflow to do reimplement existing algorithms.

## A genetics-led approach defines the drug target  landscape of 30 immune-related traits-- Hai Fang, The ULTRA-DD Consortium

This paper present a complex pipeline to do target prioritization based on pop genetics gwas studies genes of interest, annotation of them based on groupings in HiC data (co expression) mutation data etc... Then creating a graph based on PPI data. (more than just pathways but groups of interacting ones)
Based on this they validate that they find all of the most famous targets for common immune diseases such as arthrytis.
Calls to the higher need for annotation in depmap's prioritization.

## Structure-Based Function Prediction using Graph Convolutional Networks-- Ian M Fisk, Rick Bonneau

Presentation of two models. One using a language model LSTM to predict contact maps from protein 1st structure. One using a graphConvNet on the graph network based on a thresholding of a contact map, to predict GO terms i.e. functions of proteins and a tool to do feature extraction via activation map to decipher the residues that are predictive of function and which are often true known binding sites. 

## Visualization and analysis of single-cell RNA-seq data by kernel- based similarity learning-- Junjie Zhu, Serafim Batzoglou

presentation of a algorithm to learn a similarity matrix for sc RNAseq based on a finding a solution to an equation with 3 learned parameters, including the similarity matrix and a cluster structure by refining one of each paramterers sequentially until convergence. It also contains a diffusion step. It is a mathematical model based on some prior on the data (scRNA like structure and presence of clear clusters). It can be used for as inputs to dim reduction tasks and clustering tasks.  

## UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction--

Umap is a dimensionality reduction algorithm. It takes points defined by vectors of high dimensions: 2D vector= (x,y), 3D vector= (x,y,z), ND vector= (x,y,z,a,b,c,...n). and puts them back in lower dimensions. This allows for visualizing point clouds in 2D and also finding a subspace/ base / manifold in which the cloud data lies. This can be better visualizing in the 3D to 2D case 
This reduced vector is also called an embedding of the first one.

![scikit learn](../../dimred.jpg)
view of learning the shape of a "sheet of paper" only by knowing a set of points that lie on it.

Unlike many other famous techniques ([PCA](https://medium.com/@raghavan99o/principal-component-analysis-pca-explained-and-implemented-eeab7cb73b72), [MDS](d)...) it learns this structure by using local information about the points (neighbors), like [t-SNE](https://medium.com/@raghavan99o/principal-component-analysis-pca-explained-and-implemented-eeab7cb73b72).

Neighbor information is better encoded into a graph with edges representing distances to nearest points.

This distance is normalized by all distances this point has to its neighbors.

then for all the neighbors we create a set (a list of unique things): for all the edges. this set will be fuzzy as it also contains a value representing how much each neighbors is in the set of neighbors based on its distance to the center point.

We will then merge all the sets created for each point.
i.e. we will then merge the edges and keep only the ones with the lowest distances.

We then take each edges and considers them together as a graph.

*Note that we are thinking here about graph of nodes and edges but the topological logic could be applied to the faces made by each set of 3 edges and the volumes made by each set of 4 faces, etc ...*

We then take the core components of this graph using [spectral embedding](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py), where we basically take the [eigenvector](https://www.youtube.com/watch?v=PFDu9oVAE-g) of a [matrix of adjacency](https://en.wikipedia.org/wiki/Adjacency_matrix) (a square of numbers where rows represent the nodes of the graph and the columns represent the same thing and the values of the matrix are the distance between, each point)

It is a [decomposition](https://www.youtube.com/watch?v=PFDu9oVAE-g) of the information into two things, one that define a base for the object to exist in and the other defining the layout of the object. you need both to reconstruct the object.

Here we will only take the first 2 most important value of the base and considers it as what defines our object in 2 dimension (it can be any number lower than the initial number of dimension). The two values here are the dimensions and their dimensions are each of the different points

Finally we will try to improve this first version by a [minimization](https://en.wikipedia.org/wiki/Mathematical_optimization) process. There, we want to apply a physical-like force between the nodes so that close connected edges get closer together (up to a minimum distance)


![](../../images/umap.png) 
we can see the relation to the number of samples used and the max distance to create graph edges.

All in all, there is a theoretical explanation of the algorithm that can be seen in terms of learning [fuzzy](https://en.wikipedia.org/wiki/Fuzzy_logic) [simplicial sets](https://en.wikipedia.org/wiki/Simplicial_set) defining the local structure of the high dimensional data and of the lower dimensional one and making the two sets converge. 

The explanation defined in part 2 of the paper can be understood by anyone after reading [this book](https://books.google.com/books?id=xbL11KfgiEAC&printsec=frontcover&hl=fr&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) which will allow the reader to gain the vocabulary to understand the wikipedia pages defining the vocabulary used in the paper. :p 

More information about Riemannian topology can then be learned [here](http://www.math.ens.fr/~feydy/Teaching/geometrie_riemannienne_espaces_de_formes.pdf). It is in French however ;)


## Reproducible pharmacogenomic profiling of cancer cell line panels-- Peter m. Haverty, Eva Lin, Jenille Tan2, yihong yu...

A presentation of a meta analysis and replication test of large scale pharmacogenomic profiling of CCLs both at sanger and broad by independant panel as a response to another research. It showed that flaws in the critics of the reproducibiliity existed as it was not judging on the full dataset and it was not looking at the same thing as what the large scale studies where interested in.

It also shows that it is able to correlate both results by doind the analysis differently and to reproduce them (with more correlation to broad's)


## EZH2 oncogenic mutations drive epigenetic, transcriptional, and structural changes within chromatin domains-- Maria C. Donaldson-Collier1,5, Stephanie Sungalee, EPFL

This group is analysing an oncogenic mutation in a gene which is implied in the presence of histone modification at key location. They show that this mutation cause the presence of this modification everywhere and mostly in some sets of genes that are within Topologically associating domains. They found that the TADs might change a bit based on this modification and thus, change the transcriptional status of genes which are themselves tied to oncogenic states.

## Master Transcription Factors and Mediator Establish Super-Enhancers at Key Cell Identity Genes-- Young Lab

A paper I had already read before discovering and explaining what are super enhancers and how they differ from regular ones. It is in the context of muring ESCs. We can see their analysis by size. location in TAds, circuitry binding to TF and to cell state. cobinding and Mediator content. etc.. 


## DIGGIT: a Bioconductor package to infer genetic variants driving cellular phenotype -- Mariano J. Alvarez, James C. Chen and Andrea Califano

A very small paper. more of an abstract that does not explain the algorithm but shows a way to improve gwas studies by improving QTL estimation based on knowledge of master regulators and impacts of CNV on expression.
The paper was not precise enough for me to make any judgment on the logic. It is not a good paper.


## Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2 -- Michael I Love, Wolfgang Huber and Simon Anders

Here is a presentation of DESeq2 which improves on the previous version as it is trying to shrink the variance in the data based on the amount of support you get from the data itself. 
This will reduce the estimate of the fold change based on fitting the data to a NB distribution in a bayesian framework where the estimates of a MaxLikelyhood round are fitted again to a distribution with a prior as a zero centered Normal with a MAP round. The confidence values and the  ah ok ones pass a Wald Test which provide a z stat.

## TADs as the caller calls them-- Elzo de Wit

An approach to TADs consisting as a litterature review and opinion on the origin of TADs (as extrusion of cohesin loops) and their actual mechanisms. It serves as to diminish certain claims about the role of the TADs and precise their existence as a readout of a specific biological process. Instead of as a specific process themselves.  


## UNDERSTANDING AND IMPROVING INTERPOLATION IN AUTOENCODERS VIA AN ADVERSARIAL REGULARIZER-- David Berthelot, Ian Goodfellow...

This paper presented a novel strategy to better constraint the results of an autoencoder by enforcing it to produce a smooth transition between its learnt representations. This is done by using an adversarial procedure whereby a critic is trying to predict the interpolation amount and the encoder has to make the critic think that it is 0. This can help better learning the manifold of the data as shown in toy examples and MNIST results. However seems to still have some caveats in its current form.


## Transcriptional Amplification in Tumor Cells with Elevated c-Myc-- Charles Lin, Young Lab

A paper that shows that a contrario to other TFs, cMYC promotes the expression of all expressed genes but not unexpressed ones and thus serves as a general amplifier of expression in a cell. Explaining its upregulation in many cancer genomes. <-- Has been shown as wrong in the paper SLAM-seq defines direct gene-regulatory functions of the BRD4-MYC axis

## SLAM-seq defines direct gene-regulatory functions of the BRD4-MYC axis-- Matthias Muhar, Anja Ebert

A paper using slamseq to show that MYC only regulates a set of house keeping genes which can however appear as a global down-regulator/upregulator on less precise time scales. 

## Transcription Factors Activate Genes through the Phase-Separation Capacity of Their Activation Domains-- Ann Boija, Isaac A. Klein, Benjamin R. Sabari, Young's lab

Here is presented a work showing how the TF/Co-activator transcriptional condensate is organized and composed. This allows for a precise experimental definition of this condensate and its interaction in ESCs and shows how this could explain the MLL TFtoANY fusion proteins by the reliation of this condensate on proteins disordered regions which promotes this low level interaction between one another and the formation of condensate between TFsxCoact

## A Blueprint for Advancing Genetics-Based Cancer Therapy -- Bill Sellers

What is the problem of the drugability gap (what we now as oncogenic and what we can drug). How to do a "Human Cancer Genome"? Work on the understanding and targeting of resistance (by attacking the pathways in multiple locations). How to better use disease models (by high number of them and better model like GEM). And how that might translate to other diseases.

## Genome-wide somatic variant calling

## Predicting effects of noncoding variants with deep learning–based sequence model