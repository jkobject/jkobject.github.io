---
title: "Creating a cell model"
excerpt: "Let's think about some idea for bridging genotype to phenotype"
category: "Frustrations and Solutions"
header:
 teaser: "/assets/images/cell_model.jpeg"
---

I always very much liked the fact that a lot of objectives of big companies and research lab in the AI space started with some hypothesis ➡️ model before going to find out how to build something that gets close to it.

Making theories first in biology has been a constant MIA part of the scientific process for this experimentally driven field.

Regarding computational biology, things are better regarding specific models and ideas. But goals themselves have also often lacked a clear description / hypothesis / model.

A few key goals of modern biology / comp. biology is to understand how genotype influences phenotype. or basically, how a cell works.

This has often been defined in terms of what are the available technologies and statistical power achievable with current cost constrains. Known methods recoup GWAS analysis, differential expression analysis, single cell expression atlases, RNAvelocities and other ML models to predict expression of genotype.

Here I am playing with the idea of defining one model (amongst many other) to map genotype to phenotype, with little regards to cost and technology constraints. The goal is to start of discussion on the possible models, complexity requirements and missing technological breakthroughs.

## 1. the theory

$$Cs_t = fc(Cs_{t-1} | G, E)$$

Where:

- $$G$$ = Genotype = a current representation of the genotype of the cell (snps, indels, SVs)
- $$E$$ = nvironment = ressources, media, cell-cell interactions that the cell can have.
- $$fc()$$ = the cell function is actually the component that we are trying to learn and gives how the cell actually works.
- $$Cs$$ = Cell-state = cell processes, all the proteins inside the cell and their interactions, all pathway activation levels and current state.

For pathways activation we mean a vector $$Pa$$ where $$Pa = [a, PS]$$, with:

- $$a$$ = activation value $$[0-1]$$
- $$PS$$ = pathway state = representation of where the pathway is in its activation, what it is doing compared to what it can do.

No open chromatin, no DNA location, no methylation/.., no TF, no epigenomics.
This is because $$Epi_t = fp(Cs_1, .... Cs_t)$$
⬅️ likely a simplification.

Given that a cell can become epigenomically blank etc... given this fact, $${Epi_t}$$ s can be learn as part of the $$fc()$$ function in this simplification.

It is true that in good vitro condition $$E ~ E_t$$

But in high cell amounts this is not true and $$E_{t}=\sum_{\forall i} fe(Cs_{i,t}) + E_{t-1}$$

Where $$fe()$$ determines how each cell is removing/adding to the environment given its cell state)

Moreover in cell complexes: each cells are actually taking a cell specific $$E_{i,t}$$ where $$E_{i,t}=\sum_{\forall j} fe_{j,i}(Cs_j) + E_t$$

Where $$k_{i,j}()$$ is a function that determines what the cell j does to cell i given cell $$j$$'s state. where $$k_{i,j}()$$ outputs a very sparse matrix as most cells do not interact)

## 2. the main components

You can see this as a RL problem. with an agent's state and an environment.

The agent possesses a fixed state ($$G$$), and environment ($$E$$) and a current state ($$Cs_t$$)

The goal is then to let the agent learn $$fc()$$ given a good measure of $$Cs$$, $$E$$ and $$G$$.

But this is actually the crux of the problem:

1. There is no good measures of each.
2. There is no good representation of each.
3. Reading $$Cs$$ often means killing the cell.

Fortunately 2. might be solved as introducing additional components that could unsuperviselly learn representations of each component given good measure of each.

Which actually leads me to the next point: __good measures__

## 3. _good measures_ & simplifications given current data sources

We will now separate the measures from the representations by calling:

- $$Er = fre(E)$$
- $$Csr = frc(Cs)$$
- $$Gr = frg(G)$$

Where we now try to learn, $$fc()$$, $$fre()$$, $$frc()$$, $$frg()$$ (and could also try to learn: $$fp()$$, $$fe()$$ and $$k_{i,j}()$$ s)

And where:

$$Csr_t = fc(Csr_{t-1} | Gr, Er)$$

First, let's talk about $$E$$:

We have defined 3 increasingly complex annotations for $$E$$ (we will call each $$E1$$, $$E2$$, $$E3$$).

E1 could be computed by having the cell measured from a virtually steady state in vitro environment. creating a representation Er of the different environments the cells have been analysed under seems pretty trivial.

We could be feeding it some kind of a matrix of concentration of different elements and how these.

For more complex $$Es$$, there is challenges. $$E2$$ requires you to learn first $$fc()$$ but also $$fe()$$. $$fe()$$ is in a way what people call the secretome and technics have emerged to measure it. For $$E3$$, one would need to also learn $$k_{i,j}()$$. This seems very complex as a lot remains to be learnt in cell-cell interactions. Spatial-transcriptomic techniques however are starting to help in figuring out $$k_{i,j}()$$.

Then $$G$$:

To get a good $$Gr$$ one would want to use available sequencing data (especially long read for them nice SVs) in order to define a personalized reference genome that can be fed in complex models such as enformer or basset, ..., to -instead of making predictions on binding, etc- learn to create a small representation that let them predict the next bp in the genomic sequence.

There is a lot to do here. how do we best represent this personalized genome? what is the set of possible genomes? A FASTA file seems to be the worst way to do so. bu there is little other ideas...

Using annotations based on epigenomics and prior knownledge,might help in defining this representation.

Then there is $$Cs$$:

For this there is many venues: ....

To wrap it all up a future direction is evidently to learn all functions as one end to end AI model. This would also for much better transfer learning, missing data etc...
However it would require a astronomical amount data, mostly paired across modalities.

## 4. remarks

Theses processes are not continuous in time and do not work in a stepwise manner.

Diffusion coefficients, stretchings and other chemical / mechanical processes might no be well learned in this framework.

## 5. conclusion

By having this model, we have defined a set of directions to learn a genotype to phenotype mapping.

This could be hinting at set of experiment to gather as many possible measurements to learn each functions.

From getting a cell line and a stem cell population and changing the in vitro media widely while measure the response via single cell RNAseq or super resolution microscopy.
