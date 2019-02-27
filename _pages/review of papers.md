---
title: "Review of Papers"
excerpt: "Here is the draft of a list of the papers I have read with a short personal summary of them"
sitemap: true
author_profile: true
layout: single
classes: wide
permalink: /papers-reviewed-draft/
skip_amp: false
toc: true
header:
  overlay_image: "assets/images/research.jpg"
  caption: "thanks to dribble for this amazing design"
---

--------------------------------------------------------------

## IN GENERAL

1. papers are using the same expressions for things that could be said in simpler manner
2. papers are displaying citation + p values + data. within text: should be a hoverable link. 
summary should exist as in CELL with a table of content and nice image at the first Page. 
3. tables should be interactive and secondary material should be within the paper. or readily available from it. 
4. the paper, its data, its code, its bio methods and everything it cites should be accessible. 
5. there should be a table for complicated words/acronyms with explanations.
6. for other types of info (places/genes/labs/companies there should be links)
7. there should always be a corresponding press release/medium article corresponding to it. with simpler explanations.



#### SUMMARY

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

### EVALUATION

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

### SYNTHESIS

What is the crux of the research problem?
What are some alternative approaches to address the problem?
What is a better way to substantiate the claim of the authors?
What is a good argument against the case made by the authors?
How can the research results be improved?
Can the research results be applied to another context?
What are the open problems raised by this work?
Can we do better than the authors?



-----------------------------------------------------------------

### Attention in a bayesian framework - sahani

-> atention as a byesian inference. to improve impoverish stimulus
appearance of a limitation == bottleneck in such framework


shouldn't you know about P to compute this minimization ? page 7

pb : 




### neural coding  Peter latham

neurons send and receive outputs which noise can be correlated meaning that there is in fact information in it. This can have a huge effect when looking at big number of neurons. We have to knwo the correlation to understand the coding as the neurons do 

the effect of correlation can be expressed as the variation of I_shuffled ( for encoding) & of I_diag for decoding information adn saying if correlation are important in this process. those values can be from 0 to 40% of the total information of the neurons

ICA ?
independent component analysis. if we admit that a signal is composed of multiple independent sources, each of them emitting an information (thus the corresponding random variable expresses Dependant outcomes) It is possible to each sources ( or each independent components) from the signal according to $y = Wx + o$ with W a matrix (like a Neural net) x the input and o the noise. it is part of unsupervised learning of features

pb : the noise is not gaussian as estimated here. 



### cracking the neural code --peter latham



The Equivalence of Information-Theoretic and Likelihood-Based Methods for Neural Dimensionality Reduction Manesh sahani

This paper is reviewing many modern information theoretic and stochastic methods to decipher the information encoded in spikes according to stimulus. It expresses concerns and solutions for the MID methods and present some new architectures as well. 


pb :



self calibrating NN for dimensionality reduction Chklovskii

A NN that is calibrating itself to its input and reduce the dimensionality the best way possible according to minimization rules. present online and offline with rules and reguralizers which creates update rules that can be attributed to hebbian & anti hebbian behavior in neurons.

pb : not really biologically plausible





### Alex graves talk at IJCNN


can use ActiveComputationTimeNN to know where are the important part of the data 
DifferentiableNeuralComputer? NTM

DecoupledNeuralInterface to stop using backprop ( as efficient)



### neural turing machine Graves

where does the vector emission of the heads comes from ? 
the NN
for examples the shifts are produced by a softmax layer applied to the output of the controller 
softmax : mise a l'expo de chaques val du vect avec normalization sur le vector ( sum =1)

cross entropy : objective function that uses entropy function of two stat distribution and the log loss function

objective function :  fonction d'apprentissage that needs to be minimized ( it gets the output and the hoped output)



Evolving Neural Networks through Augmenting Topologies - Kenneth O stanley

really nice paper, explained well, but few complexity though.

What if this evolving architecture leads you to train your growing NN over simplification of your data and it gets more and more complex (for images for example) and you could have different types of neurons with different acti function ...



### Predicting the sequence specificities of DnA- and RnA-binding proteins by deep learning Brendan Frey

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


### Deep-learning-free Text and Sentence Embedding  --Sanjeev Arora
[link](http://www.offconvex.org/2018/06/17/textembeddings/)

like word2vec but for phrases

- you weight each word by its inverse smoothed frequency
- you sum the weighted vectors 
- you remove the component that is present in any possible phrases (corresponds to points etc..)

to produce phrases you have a discourse vector representing the subject
and you have a proba function of a vector appearing at pos t given discourse vector. ct moves as a random walk

### How do we capture structure in relational data --Sanjeev

we want to have a representation of the vertices (points) that is similar
when vertices pertain to a similar neighborhood do this by learning a representation that allows us to guess what will be the next given the preceding in a random walk

with node2vec there is 2 ways to look at neighborhoods (homophily or structural) and you can interpolate between the two with 2 hyper params

### Cancer Metastasis Detection With Neural Conditional Random Field --Yi Li

we want to use an information of the neighborhood of images the we find by computing an additional term on the inference of each elements according to their similarity/ distance to others and their labels. this creates a differentiable loss function (Conditional Random Field) that allows for fast computations etc. 80% success 

### Systematic identification of phosphorylation- mediated protein interaction switches

phosphorilation plays a regulatory role in prot-prot interaction by modifying the efficiency of functional domains.

from binding, enzymatic functions ...

(only using simple probabilistic methods given the presence of such amino acids and other chemical parameters..) -not well explained thought

there is much to do here but needs even more data and need clear characterization of the multiple effects of the folding in the chemical processes of phospho switches


### A polymorphism in the tumor suppressor p53 affects aging and longevity in mouse models

p53 if polymorph increase cancer probability but also increases life expectancy by preventing the knowing off of genes useful in cell replication and decreases stem cell exhaustion.

### gene2vector

really just applying the word2vect algorithm on protein sequences and inferring some interesting results like the destructuring or presence of proteins  

### Multi-Omics factor analysis - a framework for unsupervised integration of multi-omic data sets -- Ricard Argelaguet et al.

you integrate each data by doing a PCA on them basically.
but it uses a Latent factor model which is formulated in a bayesian way by Bayesian way. it i able to recover sparse features which explain well the underlying variations in the data and are able to thus predict outcomes in clinical data and importance features in pluripotent cell differentiation
NICE.

It is super efficient computationally (compared to similar methods)

### Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks -- David Kelley

you can learn the functional activity of ncDNA with a CNN and DNA seq (==FAIRE seq) data (ground truth here)

>understanding the DNA–protein interactions as a function of the un- derlying sequence.

Given training data, models parameterized by machine learning can effectively predict protein binding, DNA accessibility, histone modifications, and DNA methylation from the sequence


provide much information on relationship to diseases and allow fast training by reusing the weights to train on other datasets the first CNN weights are predictive of known binding configurations as well as unknown ones. (should be investigated)

### Machine theory of Mind

How to interpret and predict another agent's thinking according to its behavior.
>This “learning to learn” about new agents is what we mean by meta-learning

principal characteristics is that the network can learn that the agent hold false belief about their environment

### Analysis of Genomic Sequence Motifs for Deciphering Transcription Factor Binding and Transcriptional Regulation in Eukaryotic Cells --Valentina Boeva

>A eukaryotic genome contains a variety of structured patterns. A far from exhaustive list of genomic patterns includes (i) tandem repeats and transposable elements, (ii) stretches of GC- or AT-rich sequences (e.g., CpG islands in mammalian genomes), (iii) binding sites of DNA associated proteins (e.g., transcription factor binding sites), (iv) splice sites, and (v) DNA and RNA binding sites of non- coding RNA molecules. Different patterns may overlap each other. Therefore, although this review is focused on motifs for transcription factor binding sites (TFBSs), we provide a short overview of other types of genomic patterns.

This is an overview of the different Trans Fact Bind Sites TFBS and the Motifs Repeats, AT-GC rich sequences, splice sites, miRNA binding sites, techniques and DB to use, find, retrieve known or unknownTFBS.

_contains DB links to unknown DB of PWM motifs for TFBS_

discovery of Shadow binding sites that are low affinity binding sites that alone are not capable of retaining the TF long enough to ensure activation/repression, but instead are used to maintain a high concentration of TF in the vicinity of the primary binding sites


### GPU Kernels for Block-Sparse Weights --Scott Gray, openAI

increasing drastically computation speed on NN with blocks of zero valued weights, allowing to deepen or widen dense NN for same computational efficiency and better accuracy.

They use LSTMs with internal networks and connects them according to the small world paradigm (very good results)

--> would be nice to learn the sparsity structure
according to a predefined sparsity structure, a small world and block sparse  property

Available on tensorflow ops.
(best use multiples of 32x32 and small float values 16 bits etc..
best minibatch is 64 (for cache dilution)

### node2vec: Scalable Feature Learning for Networks -- Aditya Grover, stanford

How to embed a node from a network using a flexible notion of neighborhood (from random walks)

able to classify predict ... from this representation, which involves just creating an encoding matrix that is learnt by asyncSGD by trying to predict the neighborhood given the representation 


*questions*

What if we set out to encode not solely the local neighborhood but also some information of the distant neighborhood considering the prior that the network has the small world property?


### MicroRNA signature analysis in colorectal cancer: identification of expression profiles in stage II tumors associated with aggressive disease --Kah Hoong Chang

_touse_

Very High quality paper with a demonstration that 3 circulating miRNA
Can provide information on the colorectal cancer and its reaction to different treatment strategies, for personalized curration of the cancer, this association amongst more than 400 different miRNA (using micro array + microfluidics PCR)  was performed using an ANN to learn how to classify patients

### Efficient and Robust Automated Machine Learning --Matthias Feurer, Freiburg University

they build on the work of auto weka to solve the CASH optimization (hyperparams and model) problem, to create state of the art algo with sota performance using a tree based Bayesian method (random forest based) called SMAC. They improve this model by having a first instantiation step using meta learning: they have a model that have learnt what are the best instantiation for a given dataset using meta feature of the dataset such as entropy, number of points, classes etc... .
and secondly they use an ensembl of their best algo and not just one

### Vicus: Exploiting local structures to improve network-based analysis of biological data -- Bo Wang, Serafim Batzoglou

_touse_


They propose a new method to the manifold learning problem (dim reduction, clustering, classification etc..) Which uses local dimension learning to do its magic instead of the usual laplacian eigenvectors which learn comparing global euclidean distances.

It is basically the same thing as the laplacian but only it is constrained to do its computation on a local subgraph of close by datapoints

_contains DB links to unknown DB of single cell RNA (12-15, 24)_

### Active learning of cortical connectivity from two-photon imaging data --Mart ́ın A. Bertra ́n, Duke Uni

using bi photon imaging to look at a set of neuron activities and inferring some networks of connections given some stimulus using active learning. 
Basically, what edge should be added to the network that would maximize the likelihood of the model. (edges are weighted)
They model it with a GLM trying to optimize the BIC value of the model. to find whether promising edges to be added can be, it tries to drive the spiking rate of the model up.


### Finding Syntax in Human Encephalography with Beam Search --John Hale, Oxf, DeepMind

>a pattern of results recommends the RNNG+beam search combination as a mechanistic model of the syntactic processing that occurs during normal human language comprehension

RNNG are generative models (here for text) that rely on RNN. they can create a sentence or form a grammar tree of words given a sentence, a tree that you can parse within using beam search this parsing gives you information such as word surprisal and you can use these different statistics given the tree to generate different phrases that will create a predictable effect on the human brain meaning the way their syntax is generated is predictable of the human language comprehension. 

The guys basically made a point in cognitive neuroscience using ANN and advanced computer science. __MADNESS__

### GLOW: FLow based generative network --OpenAI

It is a particular kind of generative NN that is fully reversible thus encode^-1 == decode it is like an auto-encoder but without the re parametrization trick and with a latent space that is the same size as the input space. in the latent space you just have a multi dim Gaussian you can then interpolate to generate new inputs. 
(costly to train though)

### Prediction of acute myeloid leukemia risk in healthy individuals --Eran Segal, Moritz Gerstung

age-related clonal haematopoiesis is a phenomenon is a phenomenon that exists during aging but also is an indicator of AML 7yr before getting it (leukemia form). Here they try to differentiate between the two using deep sequencing methods they find a group of SNPs and markers in parts of the sequences that explains together much of the data but not enough separately. they then did the same on regular blood samples of patients and have seen that information on the size of hematopoetic cells (blood) have a correlation with age related diseases but also pre AML conditions. thus enabling a first easy screening of risky patients.

### A synthetic-diploid benchmark for accurate variant-calling evaluation -- Mc Arthur

trying to create a new benchmark for variant calling tools (matching reads to a reference genome and inferring the SNPs) this is faster than de novo WGS which is super costly and long. (this is part of NGS) they use a particular type of cell lines (human) called CHM which are diploids but fully homozygous and allows to use PACbio sequences without mixing the two genomes

### Meta-analysis of the diagnostic and clinical utility of genome and exome sequencing and chromosomal microarray in children with suspected genetic diseases -- Michelle Clark

A literature and statistical review of 10 years of genomics medicine for infant genetic diseases diagnostics. better use WES/WGS than previous method called CMA (molecular analysis) better sequence infant and 2 parents as well than jsut infant. a lot of heterogeneity and thus. take stats in this study with a grain of salt.

### Multi-scale deep tensor factorization learns a latent representation of the human epigenome -- Jacob Schreiber UW

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
### Machine learning applications in genetics and genomics -- William Noble, UW

a review of every possible machine learning applications in genomics 

### BioAmbients: An abstraction for biological compartments

Ambient Calculus, a further abstraction of PI calculus, can be the mathematical base to design a framework for abstracting biological compartments

Basically how to design a framework for a code allowing us to simulate cells and their inner/outer processes. Bio ambient seems to be the most general mathematical framework. Available in BioSpi

further improvement such as duplicate, divide, erase, destroy, 3D... needs to be achieved

### Personal clinical history predicts antibiotic resistance in urinary tract infections -Yelin,Snitser,Novich

Using Israel's DB and stat explore they have shown that there is relation to many parameter from urinary tracks infection and other factors and related them to biological known factors. using those predictive factors, one would be able to predict the risk of such infection and to prevent it. Among the interesting factors, relation with location (old age institute etc) pharmaceutical history, cross relations eg between age/sex. 

### Deciphering regulatory DNA sequences and noncoding genetic variants using neural network models of massively parallel reporter assays - Rajiv Movva, Kundaje

_touse_

We can see how using a NN model trained to predict regulatory effects of SNP on non coding sequences from Multi array analysis datasets works well. It was used together with SNPs found in GWAS for some genetically correlated cardiac diseases. some interesting results but MPRA dataset is of poor quality in general (low correlation)
Big step forward thought.

### Clinical Concept Embeddings Learned from Massive Sources of Medical Data -- Andrew L Beam1, Benjamin Kompa UNC, Harvard

They manage to show 100,000 clinical concepts embeddings from 3 different data-sources, they compare them to other state of the art methods on different sets of benchmark they created using clinical data sources. They achieve the biggest dataset of embedding with sota results on most of the softs·

### pooled screens in human cells, David Feldman el al

there is the introduction of doing targeted fluorescent in situ sequencing ( sequencing of specific genes from within the cell by using the fluorescence sequencing method of sequencing by synthesis.) in addition, inferring the specificities of the cell (morphology, dynamics and interaction) and to link genetic variations to 

### Manifold-tiling Localized Receptive Fields are Optimal in Similarity-preserving Neural Networks, Pehlevan, Tepper FI CCB

we can see a bio plausible NN optimization function relying on Hebb. anti Hebb. neurons which can uncover the manifold in a set of data (Here done with symmetric datasets) even for highly dim. datasets. Also showing a link to kernel learning (Here it is obviously an unsupervised learning technique,)

### Can deep learning improve genomic prediction of complex human traits? - Pau Bellot et al

tried to regress human traits values (waist, hips, height, bone
106 heel mineral density (BHMD), body mass index (BMI), systolic blood pressure (SBP)) using MLP, CNN & LR over SNPs from WGAS. 
*very stupid idea if you ask me. it is not how CNN are supposed to work. It is really treating DL as magic here*

### Learning Graph-Level Representation for Drug Discovery -- Junying Li et. al.

They use GCN to extract embeddings from a network representing atoms linked together (i.e. a molecule). They use a dummy super node to represent the entire molecule in one feature and they are able to classify the molecule between ones that works and ones that don't

###  MultiPLIER: a transfer learning framework reveals systemic features of rare autoimmune disease -- Jaclyn N. Taroni et. al.

_touse_

multiplier is a method of using Plier (an NMF method to extract features related to gene interactions) on a large compendium of data from many gene interaction modification in multiple diseased over multiple tissues from MicroArray data. learning on a huge multivariate dataset allows the unsupervised embeddings to be richer and more precise in what they convey. They demonstrated that they were able to find feature (and thus genetic interactions for many different complex diseases. the model tries also to make similar vectors from similar tissues and diseases, aligned.
*quality paper*

### On entropy and information in gene interaction networks -- Z. S. Wallace1, S. B. Rosenthal

An information concept to extract from interaction networks, some subsets that are correlated or related together. It is complementary to other enrichment methods and can find relationships amongst diseases, metabolic pathways and genes with relation to phenotypic characteristics.
and recover many interesting relationships that have been found by researchers along the way.

_DisGeNet_
_InBioMap_
_UNIPROT_
_MSigDB_
_GeneOntology_

*plus présenter les derniers problèmes et questionement durant les résultats (ou on en est maintenant)*

*raconter aussi les résultat légèrement en mode histoire de ce qu'on a fait.*

### Allele-specific binding of RNA-binding proteins reveals functional genetic variants in the RNA -- Ei-Wen Yang, Jae Hoon Bahn

_eCLIP-Seq_

GV of diseases DB:
_GWAS, COSMIC, ClinVar, CIVIC and iGAP_

_touse_


A method to find Allele specific binding events using eCLIP-seq data (trancriptome-wide protein RNA interaction data) which gives enough data to do it in an allele specific manner, the method filters out biases in the data and appears to give SOTA results. It predicted functional SNV and how they act as regulators from direct observation instead of correlation inference
"we expect that allele-specific analyses of eCLIP will be an essential approach to deciphering the function of non-coding variants in the RNA."

### In silico prediction of high-resolution Hi-C interaction matrices --Shilu Zhang1, Deborah Chasman.

_touse_

to predict the contact count of two genomic regions from their one-dimensional regulatory signals which output from HiC-Reg can be used to identify significant interactions using peak-calling algorithms that have as good experimental support as those from true counts.
a regression-based framework to predict interactions between pairs
of regions across multiple cell lines by integrating published Hi-C datasets with one-dimensional regulatory genomic datasets.

### Winner-Take-All Autoencoders -- Brendan Frey

winner-take-all spatial and lifetime sparsity methods to train auto-encoders that learn to do fully-connected and convolutional sparse coding which jointly trains the encoder and decoder paths by direct back-propagation, and does not require an iterative EM-like optimization technique during training. sota results especially when doing semi supervised training

### Dissecting splicing decisions and cell-to-cell variability with designed sequence libraries -- Eran Segal, Martin Mikl

rationally designed libraries, consisting of altogether 32,789 variants, to address fundamental questions in splicing regulation considering the process in its entirety, from the processing of the RNA to the level of the final functional gene product. They could reproducibly detect even small changes in splicing ratios and quantitatively predict splicing of novel variants with high accuracy (R2 between 0.76 and 0.85)
cells evolved to have seemingly “suboptimal” splice sites, which maximizes the potential for dynamic regulation, but can also serve to ensure optimality at the level of protein isoforms. They have established an assay that is able to assess the cell-to-cell variability of splicing decisions in large scale by measuring the protein output of alternative isoforms and shown that the level of stochasticity can be encoded in the DNA.

__Highly rich paper__

### Quantum Entanglement in Neural Network States -- Dong-Ling Deng, Xiaopeng Li

the entanglement proper- ties of neural-network quantum states in the RBM architecture. and proof that all short-range RBM states satisfy an area law of entanglement for arbitrary dimensions and bipartition geometry
For some maximal volume- law entanglement RBM representation is remarkably efficient, requiring only a small number of parameters scaling linearly with the system size which show the power of NN to describe massive entanglement
Further explore the link between ANN and entangled quantum states...

### Cancer archetypes co-opt and adapt the transcriptional programs of existing cellular states -- Maayan Baron1, Isabella S. Kim

__quality paper__

study of the gene expression of individual cancer cells in zebrafish and human melanomas. three recurring gene expression patterns across melanoma cancer cells which we refer to as ‘archetypes’ because they appear to be co-opted cellular states with distinct spatial location
cancer cells between human and zebrafish melanomas exhibit the same transcriptional program.
not yet purview into the origin of archetypes. found cooperation across cancer cell lines as they form a tumor in vivo

### Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk -- Troyanskaya, FI
__addition of the second paper "Predicting effects of noncoding variants with deep learning–based sequence model",__ especially the method part of it.

_touse_

they have used a deep CNN with a lot of different Weighted patterns to predict regulatory profile (chromatin, methylation etc...) from a raw DNA sequence. using ENCODE datasets given specific cell types. this gave them the ability to predict a cell specific profile as well as to predict variation in regulatory profiles caused by variants, using a linear model (made from non linear basis function of from the different profiles data, they are able to regress how much each the regulatory features of the non coding sequence before the  Transcription Start Site (and a bit of the sequence after) influence the expression profile of different the gene.) they were able to retrieve expression for famous protein and how they change with different cells and to retrieve SNPs causing variation in expression that were also shown from GWAS information (even better than in GWAS) and to find interesting disease correlations as well.

### One-Shot Imitation Learning -- Ilya Sutskever, Pieter Abbeel

a paper displaying the use of DQN with two distinct networks, one with an attentional mechanism (LSTLM) that sets a set of subtasks to achieve the objective, one to control the robot given the subtasks(MLP) (or even just reconstruct the sets of tasks given the final state it needs to achieve) Here the attentional system helps to subdivide the sets of tasks given to the MLP, results are SOTA for the type of tasks (first to achieve that) 

### MCM2 promotes symmetric inheritance of modified histones during DNA replication -- Nataliya Petryk, Maria Dalby

_not very interesting_

special sequencing technique revealed that parental histone segregation is almost symmetrical with a weak inherent preference for the leading strand. making it possible for MCM2 to recycle parental histones to the lagging strand (Fig. 3F, right), while a separate pathway deposits pa- rental histones on the leading strand. In this vein, it is conceivable that histone segregation can be regulated during development to drive asymmetric cell fates.

### Deep surveying of alternative splicing complexity in the human transcriptome by high-throughput sequencing -- Qun Pan, Ofer Shai, Frey

_old article_ 2008

explaining how the splicing complexity can be understood using RNA seq and how there may be a lot of possible transcripts from one sequence with different alternative splicing according to some regulatory sequences. one interesting aspect is that it shows how much there is and the amount we did not really knew about previously.

### Sequential regulatory activity prediction across chromosomes with convolutional neural networks. --David R. Kelley, Yakir A. Reshef

_touse_

bassenji is another DL algorithm to quantify regulatory features (certain - DNase seq, histone, Chip-seq) from CAGE experiments. it is using a CNN with expending layers (which multiply the ROI by a factor of 2 at each layers). it is from 16 month ago and appears to be less good than more recent work but provide trainings for coverage, GC%, EM for multi-reading alignment etc..
It shows link to eQTL found similarities and GWAS data, perform prediction of why some diseases happens etc, while preventing bias from LD. finally it is giving new research ideas (more data, finding more distant reg activities, better cell specific data, more precise data) and post transcriptional regulation activities etc...

### Deciphering the splicing code --- Yoseph Barash, Frey

_touse_

Kinda the previous version to deepBind. Here they describe an information theoretic method based on regression for prediction of variation of splicing probabilities compared to the baseline activity. this is used by taking in account typical base patterns that would create specific sec shape or bindings for the splicing to happen in a specific manner. This allowed the discovery of new features that make alternative splicing possible and of variation in different tissue with phenotypic logics behind.

### IMPALA -- DeepMind

A new DeepQN framework for the in parallel training of multiple actors and diminishing the delay/dissimilarity between the actors and the learners (and the learners to themselves) this framework/architecture is made possible by a new learning method that tries to combat the off policy (dissimilarity in policy) between the different agents. it uses previous work on batch A2C, Importance sampling, and other mathematically/experimentally driven techniques to compute the best possible gradient for episodes (a,s,r). 

### Unsupervised embedding of single-cell Hi-C data - Jie Liu, Galip Gurkan Yardımcı, UW

a paper displaying how one can use a previous technique called HiCRep which smooths the Hi-C contact matrix and then computes a weighted similarity measure separately at each genomic distance. Then averages the results for the cell itself. Finally followed by a Multidimensional Scaling (MDS) of the resulting matrix to reduce the dimensionality while preserving distance relations, allows to recover angle distance between datapoints (representing cells) which allows the classification of different cell phases. It can be done with high throughput scHiC data since using a subset of contacts still allows to recover the ground truth, especially if used in combination with a bag  of more deeply sequenced cells.

### An integrated encyclopedia of DNA elements in the human genome -- ENCODE

__start of the Engineer's map__

a detailed explanation of the types of data and means to get them from the encode collaboration. And an overview of this data. Interesting feedbacks from it. It displays the different things that might be achieved using it. 
Moreover it provides access and a biologically oriented summary of numerous research that have been undertaken by the consortium's researchers. Especially their results and how they fit in a more general summary of this kind of functional genomics data.


### Engineering Stem Cell Organoids -- Xiaolei Yin Benjamin E. Mead


an overview of the different use, techniques, and methods for the construction of organoids or organoids like objects from human stem cells. recapitulating OoC HoC etc. And talking about how a mix of these methods is required for the future of organoids engineering. 

### Advantages and limitations of current network inference methods -- Riet De Smet and Kathleen Marchal

a survey of the different network inference methods in genomics, to predict the regulatory network (in bacterial genomes) with the different algorithms that are available and their mathematical framework. The different DB that are available and the problematics and usages that everyone can have from these according to one's needs.

### Optimization Techniques on Riemannian Manifolds -- Steven Smith

two algorithms: Newton’s method and the conjugate gradient method on Riemannian manifolds, are presented and shown to possess resp. quadratic and super-linear convergence

### The Tsetlin Machine - A Game Theoretic Bandit Driven Approach to Optimal Pattern Recognition with Propositional Logic -- Granmo

the tsetlin machine is a form of machine learning techniques which uses tsetlin automaton the same way a neural network uses a neuron. However it is more computationally grounded by being in the framework of propositional logic. The paper shows how to reach an equilibrium in learning even from very noisy data by finding the right hyperparameter handling error assignment. it proves that it will be able to learn anything and then shows some sota results on some datasets. Moreover the paper derives CNN and RNN like structures from tsetlin machines.


### The Genetics of Transcription Factor DNA Binding Variation -- Deplancke 

	Since most of variant associated with phenotypic changes in mammals are from non coding region, the paper establishes the different mode of genetic variation mediated changes to TF binding. sets up the ways in which they have previously been uncovered, some examples and the difficulties behind this problem. It then goes on to highlight the possible technological (sequencing & computational(ML))-based techniques that might help in solving it.


### SegAnnDB interactive Web-based genomic segmentation --Hocking

a less interesting paper that reuses a mathematical framework to help on analysis (segmentation) of cancer genomes into different categories (CN variation, breakpoints(DNA deleted, inverted, or swapped)) by using a mathematical+vision framework to understand the user input segmentation and further them to the entirety of the cell genome in a supervised fashion.  

### Defining a Cancer Dependency Map -- Aviad Tsherniak, Francisca Vazquez, Phil G. Montgomery BroadInstitute

Researchers from CDS team at the broad present their ongoing effort to analyze a wide range of cancer cell lines to infer their dependencies (survival, reproduction) on different genes. To do so they are using genome scale loss of function RNAi screens (knocking down specific genes using silencing RNA which will get infiltrated by lentiviral infection in vitro on microArray live cell chips which is highly multiplexed (looking at the expression of the co-infected GFP RNA in each cases)). Each input RNA (shRNA ~100,000) will infect some cells and silence some genes. They contain a seed which will help in the binding to the desired mRNA.  
However, Because of this seed, this will also create off target effects (down-regulating other genes than the desired one by partial binding of the miRNA seed) it is using a linear regression model to understand the true effect of each shRNA in silencing a particular gene. (The model was in fact very similar in intuition to a NMF but was just a linear regression: to divide the dataset (cell line perturbation per shRNA) into two distinct part: cell line perturbation per gene knock down and cell line perturbation (instead of gene knock down) per shRNA with seed k) <-- could be done in a more efficient fashion by using an NMF which divide it and add a third matrix term which would contain the off target effect relation across shRNAs. 
The two matrix found allow one to understand specific cases where specific cell lines require a particular gene more than another and more than the regular cell. it is called: a differential dependency and might represent important therapeutic target. 
By taking the strongest ones (6std from the mean) they found 769 such genes for the 500 cell lines. they then used another non linear regression model with gene mutations, gene copy number, gene expression from the Cancer Cell Line Encyclopedia (CCLE).
They then carefully analyzed the different types of predictive MDPs (Marker dependency pairs) and specific MDPs for 86% of the dependencies.
However, to find a full range of MDP and predictive models for each, they estimate they would need to increase the amount of cell lines to >5000, to account for other types of dependencies such as ones that are not single cell specific (but are important in group behavior).
--> moreover, what happen for gene combination effects and in this case, time dependent gene known down effect? is there a non linear relationship between gene knockdown and gene knockoff? what about the many different type of cancer cells and their inter relationship present in a tumor?
how many other features can be added? (long range TF?) can one reuse some pretrained DL for genomic and find what molecular features in the sequence explain each types? 


### Improved estimation of cancer dependencies from large-scale RNAi screens using model-based normalization and data integration -- james McFarland BroadInstitute

*basically about explanaing demeter2*

explaining similar things as previously with a bit more emphasis in the comparative aspect and computational aspect of Demeter2 to other types of data. a larger dataset (790dtp). in the better explanation of the model and its results. interesting and deeper explanation of the computation in the methods:
the demeter2 model uses a Bayesian model with variational inference of some params and MAP estimates of others. it explains the full procedure to infer each params using scipy and Edward. in this model a lot has been used to find the best set of parameters / hyperparameters. comparing with ground truth or prior knowledge and values to set to test the strength of each.


### Genetic and transcriptional evolution alters cancer cell line drug response -- Uri Ben-David1, Benjamin Siranosian, Gavin Ha, Helen tang, Yaara Oren, Kunihiko Hinohara, craig Strathdee, Joshua Dempster, Nicholas lyons, robert Burns, Anwesha Nag, Guillaume Kugener, Beth cimini, Peter tsvetkov, Yosef Maruvka1, ryan O’rourke, Anthony Garrity, Andrew tubelli, Pratiti Bandopadhay, Aviad tsherniak

Here we look at the problems arising from the culture of cancer cell lines in research application. because of random mutations, changes in their environment, cancer cell lines undergo evolution. this creates strong differences to the in vivo scenario. The paper tries to infer the possible differences and how they might arise (medium, population bottleneck). They have dev a tool to compute the distance to a reference. They also show how to use this such as to understand cancer cooperation (with single cell seq) and correlation genotype-phenotype. 



### Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer and Beyond -- Mikel Artetxe, Holger Schwenk.

the papers show the power of many different languages used to create a same embeddings for all. it displays encoding techniques and train / test strategies and a new test set. It proves to be sota on most test set used. I uses a bi-LSTM encoder of 5 layers, 83 languages and an LSTM decoder  with skip connections 


### CytoGAN: Generative Modeling of Cell Images -- Imaging Platform Broad Institute of MIT and Harvard

this work uses a regular LSGAN to learn the important feature from a dataset of cell images. they show that it is not sota but can infer better latent factors which encode phenotypic information about the cell. both in the generator and discriminator. They show how to preprocess the image to get the best results. the work would need additional information to be reproducible.


### Pathway perturbations in signaling networks: Linking genotype to phenotype --Babu for Barth EPFL

>> what about gene knockdown datasets... might be very interesting. 
drug interference data sets as well.
I heard of central regulators which are specific and specifically expressed in specific cancer cell lines and that knowing that information allows one to understand the specificities of the cell line (like its reaction to drugs etc..)

In here we look at several different signaling pathways which have highly oncogenic potentials. looking at them via a What mutation, how it should work, what happens when mutations. How can it be fixed.
We are really looking at the causal explanation of a phenotype by a mutation/alt. splicing/ translocation/... .

### Pharmacogenomics of GPCR Drug Targets --  Masuho, Leonie J. Jahn, Kirill A. Martemyanov, David E. Gloriam, M. Madan Babu

Here we analyze how different drugs affecting primarily or secondarily the GPCR membrane receptors of cells can have different effects considering the naturally occurring mis-sense variation in the human population on these corresponding protein coding genes.

> how comme they never thought of doing the same in pharmacollogy??
> what about the non coding variants in the population it will reflect also some differential effects in the signaling pathway and even variation in the proportion of membrane receptors

### 

> I really want to see how the pipeline to integrate the entire G cycle looks like.


### Papers Gilchrist
#### Combining Models of Protein Translation and Population Genetics to Predict Protein Production Rates from Codon Usage Patterns

#### Explaining complex codon usage patterns with selection for translational efficiency, mutation bias, and genetic drift

#### Estimating Gene Expression and Codon-Specific Translational Efficiencies, Mutation Biases, and Selection Coefficients from Genomic Data Alone

####  Quantifying codon usage in signal peptides: Gene expression and amino acid T usage explain apparent selection for inefficient codons

I had the time to read the papers you sent me and they were very good. The third one presented a great introduction to CUB and a good model which attains a very high score. I would guess that this model could not get the same score for other species. I still think that a model of CUB would always be reductionist as the CUB is a proxy for so many different processes and adaptations of the cell. The many fine grained Bayesian model that you present however seems to make sense and creating a model is to me the only way to test a theory. The ability to regress values such as the protein synthesis rate is impressive and it does not seem trivial to me that this should be the case. The model that you have developed seems very suited for answering questions about the CUB as shown for example in "quantifying codon usage in signal peptides". 

### Where genome biology is going next
multiple researchers giving their view of where genomics is heading

### A topological and conformational stability alphabet for multipass membrane proteins -- Patrick Barth

Here is the study of multipass transmembrane proteins which are composed of many transmembrane helices. they have a specific confirmation which is dictated by their sequence. interaction between helices yields the specific shape of thee multipass prot.
specific residues which help connect the helices and give them their shape seems to be coevolving, stabilizing the shape and are determinant of the topology. For the first time this study analyzed trimers of helices insetead of dimers.  


### Primer on Deep Learning in Genomics

### A guide to DL in healthcare -- Andre Esteva, Alexandre robicquet

Some simple yet necessary ideas about how one would best use DL in healthcare and what are the future and promises of it.

### Mammalian Genes Are Transcribed with Widely Different Bursting Kinetics

in this paper it is explained briefly (with more precision about the models in the supplementary materials) the rational behind bursting kinetics in mamlian genes. We look at a model going from in/activation; trancription rates; translation rates and degradations. using markovian prob. models. per coding genes. then correlates it with exeperimental fluo activity thanks to a poissonian noise model. the entirety of the model is then parametrized by EM algo thx to baum welsh algorithm. the computation of the states (bc it is a markov. model.) is done with the viterbi algorithm. The signal in the images were deconvolved using wavelet temporal analysis. the results described how different profiles of protein activity were highly periodic with different types of kinetics. also shown in the analysis of the states/params of the model for different mRNA. this difference could be seen also for similar genes accross cell lines.

### what are super enhancers? -- Sebastian Pott & Jason D Lieb
_very important_

Explainingwhat are enhancers. open questions about them at the functional level.
then turns out how to compute super enhancers. their possible differences with regular ones and possible similarity which would make them just reegular enhancers specific of the particular expression of the cell line.
it turns out to display 5 questions about super enhancer and if they truly are mechanistically different.
And a framework to find it out.

> how do gene dependancy relate to SEn? using the same Crispr screening technique
One Should Compute SEn without using merging of regular one according to the paper. Might help answering the question as well.

### Super-Enhancers in the Control of Cell Identity and Disease -- Denes Hnisz, Brian J. Abraham, Tong Ihn Lee
_very important_


> might be interesting to reuse softs such as DeepPeakCaller and DeepBind

> Maybe one might find the equivalent of superENhancer for lesser TF type when looking only at these.

> Sen are concepts associated with TF master TF, enhancer, cell fate, cell differenciation/pluripotency (see for of Pr. Gioele La manno EPFL, transcription regulation (cis & trans) (also via enhancerRNAs), 

> it would be valuable to identify the master transcription factors that control all cell states.

> if alteration in superenhancer drive cell specificity. what if some cancer were some form of local valley in cell specificity out of which the cell can't escape. this could be seen by looking at differences in superenhancer region through stages of cancer or types of cancer from a same cell line through the eyeyes of what La Manno has done.

> when you look at Senh accross cell lines and cancers and you see ~ a thiord which are cell line specific. do the other 2/3 are shared accross cell? cell types? cell groups? random noise, i.e. not acual Senh?

First the discovery that super enhancer are linked with cancer hallmark, disease SNPs, specific per cell types, linked with specific core transcription factors, miRNA ncRNA. might explain cell diff, fate, etc.. they create feedback loop. can be transcribed into eRNA (which may contribute to gene activation) and are not only enriched in TF but also in RNA Polymerase II, Cofactors, and Chromatin Regulators. It is also a dataset of 86 cell type (human) 

### Network In Network -- Min Lin, Qiang Chen, Shuicheng Yan

putting MLP instead of regular convolution for each layer of a CNN. ReLu then finishing by a global average pooling layer feeding to a logistic regression classifier.


### Selective Inhibition of Tumor Oncogenes by Disruption of Super-Enhancers -- Jakob Love, Heather A. Hoke, Charles Y. Lin

You have some enhancer of MYC, MCL1, IRF4, PRDM1 ... which are strongly bound by BRD4 and MED1. we know that reducing the level of BRD4 by using a JQ1 tratment which will lead to a bromodomain inhibition of BRD4 and thus restrict binding of itself and its coFactors. In many types of cancer cells. this leads to a selective desctruction of them and not of regular cells. This is explained in this paper by stating that these cells are known to have very strong super enhancers to these genes and thus it is places which relies more heavily on BRD4 and which are more essential to these cell lines. Giving ideas to explain and discover more oncogenic targets.

### ATARiS: Computational quantification of gene suppression phenotypes from multisample RNAi screens-- Diane D. Shao, Aviad Tsherniak, Shuba Gopal, Barbara A. Weir

The beginning of the DepMap, before large scale and demeter. Discovering how a lot of data can help uncovering gene dependency in cancer from rnaI. Using  a Matrix Factorization. Moreover as many RNAi can affect a gene. After it, a refinment step is performed to find a subset of best performing ones according to the profiles found by the matrix factorization problem.
showing ability to:
- identify fuctional relationship between genes
- identify nocel cancer associated genes.
- identify genomic predictor of gene dependency

> did not  get fig 4C ...


### Pan-cancer genome and transcriptome analyses of 1,699 paediatric leukaemias and solid tumours-- Xiaotu Ma1, Yu Liu, Yanling Liu, Ludmil B. Alexandrov, Michael n. Edmonson

A paper recapitulating the creation a first analysis of 1699 pediatric leukimia tumors at the transcription and genomic level. understanding similarities and differencies btween them/ them and adult leukimia. and some interesting new genes and genetic features. Additionaly a more thoruough analysis of WT1 D447N. 
>for which I was not 100% confident on my comprehension


### Curiosity-driven Exploration by Self-supervised Prediction-- Deepak Pathak Pulkit Agrawal

> what about training on the ability to predict the distribution dynamics instead of just prediction error on the next state (else might be triggered by simple noise or stochastic distributions)

agent is trained on minimizing the prediction error of state t+1 from state t and action t (*may be better with reusing all previous states in some form*)

### The landscape of genomic alterations across childhood cancers--Susanne N. Gröbner, Barbara C. Worst, Joachim Weischenfeldt Ivo Buchhalter, Kortine Kleinheinz, Vasilisa A. Rudneva Pascal D. Johann

Another presentation of a dataset containing a thousand tumours (most of them ALL and central nervous system related) with identification of regular driver genes, structural and CN variants and germline/somatic variants. with a study of the particular processes in childhood cancers as well as potential drug targets related to the discoveries listed here.

### A Landscape of Pharmacogenomic Interactions in Cancer-- Francesco Iorio, Theo A. Knijnenburg, Daniel J. Vis

A look at the pharmacogenomic landscape (response to 265 drugs) of 1,001 human cancer cell lines from 11,289 tumors points to new treatment applications for hundreds of known anti-cancer drugs. to determine:
- the extent to which cancer cell lines recapitulate oncogenic alterations in primary tumors.
- which oncogenic alterations associate with drug sensitivity, 
- whether logic combinations of multiple alterations better explain drug sensitivity.
- the relative contribution of different molecular data types, either individually or in combination, in predicting drug response

> here it seems that the gene expression data only helps to infer the cell type > thus the dependancy according to that. thus a two step model (cell type > specific sensitivity) might be more appropriate
> Here I think you need to model some of the specific proteins to understand better what explains the sensitivity and what events (SNP, CNV, ...) might help you understand that. (see work from Patrick Barth)
 
---
CFE  cancer functional events
RACS recurrently aberrant copy number segments

----

### Unsupervised embedding of single-cell Hi-C data -- Jie Liu, Galip Gu rkan Yardımcı UW



### Detecting Circular RNA from High-throughput Sequence Data with de Bruijn Graph -- Xin Li and Yufeng Wu


### Advancing the aging biology toolkit -- TROY K COODY AND ADAM L HUGHES



------------

