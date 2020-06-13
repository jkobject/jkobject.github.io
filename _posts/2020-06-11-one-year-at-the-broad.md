---
title: "A year at the Broad Institute"
category: "work"
tags:
 - Computational Biology
 - Data Science
 - Associate Computationnal Biologist
header:
 teaser: " /images/dimred.jpg"
---


Umap is a dimensionality reduction algorithm. It takes points defined by vectors of high dimensions: 
- 2D vector= (x,y), 
- 3D vector= (x,y,z), 
- ND vector= (x,y,z,a,b,c,...n) 

And puts them back in lower dimensions. This allows for visualizing point clouds in 2D and also finding a subspace/ base / manifold in which the cloud data lies. 

This can be better seen in the 3D to 2D case. The reduced vector is also called an embedding of the first one.

![scikit learn](/assets/images/dimred.jpg){: .align-center}

_View of learning the shape of a "sheet of paper" only by knowing a set of points that lie on it._

Unlike many other famous techniques ([PCA](https://medium.com/@raghavan99o/principal-component-analysis-pca-explained-and-implemented-eeab7cb73b72), [MDS](d)...), it learns this structure by using local information. i.e. only looking at specific patches at a time. The neighbors of each points, like [t-SNE](https://medium.com/@raghavan99o/principal-component-analysis-pca-explained-and-implemented-eeab7cb73b72). This type of technique is called non linear as it can learn complex "bendy" shapes (like the S above).

Neighbor information is better encoded into a graph. With edges representing distances between points. and only displaying the edges to the nearest points in the neighborhood.

This distance is normalized by all distances this point has to its neighbors, meaning now the range of possible distances is transformed into a [0,1] range where the closest point will be at a distance 0 and the furthest point will be at a distance computed such that summing all the distances between all neighbors will get to $log2(#neibors)$.

Then for all the neighbors we create a set (a list of unique things) for all edges. 

This set will be "fuzzy", as it also contains a value representing how much each neighbors to a point is in the set of neighbors to this point, based on its distance to the center point.

We will do this for each point and then merge all the sets created for each point.
Meaning, we will merge the edges and keep only the ones with the lowest distances.

We then take each edges and consider them together as a graph or a skeleton.

**Pausing for a second**, we can really see that the only thing we have done here is defined edges between points and merging them together. However you have to understand that the same edge in two different set, will have two different distances as they have both been normalized by different sets of neighbors. Thus even a point far away from everything else will get one of its edges in the graph. 
These two edges would get merged by using the [t-conorm](https://en.wiktionary.org/wiki/t-conorm) (which a fuzzy logic way of taking the [norm](https://en.wikipedia.org/wiki/Norm_(mathematics)) of something) on their two respective lengths.

*Note that we are thinking here about graph of nodes and edges but the topological logic could be applied to the faces made by each set of 3 edges and the volumes made by each set of 4 faces, etc ... This would complexify the model (and render it impossible to compute) but also make it more closer to the theory underlying it*

We then take the core components of this graph using [spectral embedding](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py), where we basically take the [eigenvector](https://www.youtube.com/watch?v=PFDu9oVAE-g) of a [matrix of adjacency](https://en.wikipedia.org/wiki/Adjacency_matrix) (i.e. A square of numbers where rows represent the nodes of the graph and the columns represent the same nodes and the values of the matrix are the distance between, each point)

It is a [decomposition](https://www.youtube.com/watch?v=PFDu9oVAE-g) of the information into two things: one that define a base for the object to exist in and the other defining the layout of the object. You need both to reconstruct the object.

Here we will only take the first 2 most important value of the base and considers it as what defines our object in 2 dimension (but it could be any other number, lower than the initial number of dimension). The two values here are vectors: they represent the 2 dimensions of each points (x,y) and each of their value/dimensions represent each of the different points in our point cloud.

Finally we will try to improve this first version by a [minimization](https://en.wikipedia.org/wiki/Mathematical_optimization) process. There, we want to apply a physical-like force between the nodes so that close connected edges get closer together (up to a minimum distance)


![](/assets/images/umap.png){: .align-center}

*we can see the relation to the number of samples used and the max distance to create graph edges.*

All in all, there is a theoretical explanation of the algorithm that can be seen in terms of learning [fuzzy](https://en.wikipedia.org/wiki/Fuzzy_logic) [simplicial sets](https://en.wikipedia.org/wiki/Simplicial_set) defining the local structure of the high dimensional data and of the lower dimensional one and making the two sets converge. 

The explanation defined in part 2 of the paper can be understood by anyone after reading [this book](https://books.google.com/books?id=xbL11KfgiEAC&printsec=frontcover&hl=fr&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false) which will allow the reader to gain the vocabulary to understand the wikipedia pages defining the vocabulary used in the paper. :p 

More information about Riemannian topology can then be learned [here](http://www.math.ens.fr/~feydy/Teaching/geometrie_riemannienne_espaces_de_formes.pdf). It is in French however ;)