---
title: "The new way we’ll do science"
excerpt: "Papers should become human-readable views over a graph of data, tools, results, and certificates."
category: "Frustrations and Solutions"
date: 2026-06-15
header:
 teaser: "/assets/images/science-library-british.jpg"
---

Science still has a strange little habit.

A lab spends three years collecting samples. Someone writes a preprocessing script. Someone else changes a threshold. A model gets trained on version 3 of a dataset, evaluated with a slightly different split, plotted into Figure 4, summarized in one cautious sentence, then cited for the next decade as “Smith et al. showed X.”

Then all of that becomes a PDF.

We cite the PDF. Count it. Rank it. Put it on CVs. Feed it to review committees. Argue about the journal it appeared in. Sometimes we even say a result was “shown in this paper,” as if the paper were a clean unit of knowledge rather than a box full of objects with different failure modes.

That made some sense when scientific publishing was constrained by print. A paper had to be a compressed story. It had to carry the context, method, result, certificate, interpretation, and credit in one portable package. But online, this is starting to look ridiculous. The internet changed distribution; it did not really change the scientific object. Most scientific knowledge still travels around as a linear article, with a few links and supplementary files stapled to the side.

The problem is not the PDF. The problem is that we treat the paper as the atomic unit of scientific trust.

A paper is a bundle. Inside it are datasets, protocols, pieces of code, models, statistical tests, experimental observations, thresholds, figures, statements, conditions of validity, and sometimes long formal proofs. Some of these objects are robust. Some are fragile. Some are reusable. Some are just scaffolding for the story.

A citation to a paper is a terrible pointer. It rarely says whether we depend on the dataset, the model, the preprocessing step, the theorem, the statistical test, one figure, the code, the protocol, or merely the framing. It gestures toward a bundle and says: trust me, it’s somewhere in there.

![The British Library: scientific trust still mostly moves through document-shaped objects](/assets/images/science-library-british.jpg)

*The British Library, via Wikimedia Commons / public domain.*

The objects inside a paper do not fail in the same way. A dataset can be contaminated. A model can leak. A protocol can be underspecified. A statistical test can be invalid under the wrong distribution. A proof can have a gap. A benchmark can be saturated or gamed. Lumping all of that into one citation is not sophistication. It is loss of information.

That is not good enough anymore.

AI makes this harder to ignore. It does not create the weakness of the paper; it makes the weakness impossible to hide. When plausible scientific prose becomes cheap, prose can no longer be the main carrier of trust. The bottleneck will not be writing more papers. The bottleneck will be sorting real scientific objects from fluent scientific-looking text.

So maybe the paper should stop being the fundamental unit of science.

Not disappear. That would be stupid. Humans need narrative. We need introductions, intuition, motivation, argument, taste. A good paper is still one of the best ways to understand why something matters. But the paper should become the human-readable view, not the underlying structure.

The underlying structure should look more like a graph.

A useful way to split the bundle is into four kinds of objects: **data, tools, results, and certificates**. Or, when the word is right, certificates can simply be called **proofs**.

Data are the things science can work on. Tools are the things that transform data. Results are data that have become scientific outputs. Certificates are the checks, proofs, protocols, or validation records that explain why a result deserves trust under particular conditions.

This is not meant to be a grand ontology of everything. It is just a cleaner grammar for what papers already contain.

## Data

Data are information objects science can manipulate.

They can be raw observations: telescope readings, sequencing reads, microscope images, survey responses, sensor traces, lab notebook entries. They can also be processed objects: normalized matrices, embeddings, annotations, fitted parameters, benchmark tables, simulation outputs, figures, or previous results.

The important move is that results are also data.

A result is not made of different material. It is data playing a particular role. Yesterday’s result becomes tomorrow’s input. A table in one paper becomes the dataset for another. A theorem becomes a premise. A trained model becomes something others test, fine-tune, criticize, or build on.

So “data” and “result” are not separated by substance. They are separated by function.

## Tools

Tools transform data into data.

```text
T(D) = D'
```

A tool can be code, a model, a statistical test, a microscope, a lab protocol, a sequencing platform, a survey instrument, a normalization step, a proof tactic, or a human annotation procedure. A pipeline is a tool made of tools.

Models belong here. They are not a separate top-level category. A model is a tool that maps inputs to outputs.

Sometimes the model predicts. Sometimes it simulates. Sometimes it represents a mechanism. Sometimes it is a null or reference model: a tool that generates the data we would expect to see if nothing interesting were happening, conditional on the input.

That last case matters. Many empirical results are comparisons between observed data and data generated, implied, or expected by a reference tool.

![A null model generates reference data conditional on an input](/assets/images/science-null-model.svg)

## Results

Results are scientific outputs produced by applying tools to data.

```text
T(D) = R
```

A result can be a figure, a table, a theorem, a trained model, a fitted parameter, a correlation, a benchmark score, a derived dataset, a discovered structure, a ranking, a map, a simulation output, a negative result, or a failed replication.

Papers usually turn results into sentences:

> “Y is associated with X.”

> “This model outperforms the baseline.”

> “This perturbation shifts cells toward this state.”

> “This theorem follows from these definitions.”

Those sentences matter. They are how humans read science. But they are not the primitive object. They are statements: natural-language renderings of results, often with some hint of the certificate behind them.

The result itself should be inspectable underneath the sentence. What data produced it? What tool transformed the data? Under what conditions? With what certificate?

## Certificates, or proofs

Now the tricky word: proof.

In mathematics, “proof” is the right word. A proof can be long, formal, compositional, and machine-checkable. Lean makes this obvious: a theorem is not just a sentence in a PDF; it can be attached to a proof object whose dependencies are explicit.

In empirical science, “proof” sounds too strong. Biology does not prove things the way number theory proves things. A wet-lab experiment is not a theorem. A single-cell dataset is not an axiom. Most empirical conclusions are probabilistic, model-dependent, protocol-dependent, and fragile.

But replacing “proof” with “evidence” loses the idea. Evidence is too loose. It mixes everything: replication, validation, plausibility, authority, intuition, reviewer confidence, and vibes with p-values. That is not what we want.

So the better word is **certificate**, with “proof” kept as the important special case.

A certificate is a formal, verifiable object that records the relation between data, tools, result, and conditions: what was run, what was checked, what assumptions or protocols mattered, and why this result is allowed to stand.

In math, a certificate can be a proof. In computer science, it can be a type check, a formal verification trace, a reproducible execution, a proof-carrying artifact. In biology, it may be a statistical test under a null model. In clinical science, it may be a prespecified analysis plan plus an estimate and confidence interval. In machine learning, it may be an evaluation protocol, benchmark split, metric computation, and reproducibility record.

Most certificates are not grand. Most are tiny.

A biology paper might contain dozens of them. Given dataset `D`, tool `T`, reference model `M0`, observed result `R`, and threshold `t`, the observed result falls in a specified tail of the distribution generated by `M0`. Under those conditions, the result can be rendered in prose as: `Y` is statistically associated with `X`.

Nobody writes this as a proof. Usually it is scattered across Methods, Results, supplementary tables, code, and reviewer imagination. But the skeleton is there.

The point is not to pretend empirical science has mathematical certainty. The point is to make the scientific bridge explicit.

## Conditions

No tool works everywhere. No certificate is valid in the void.

A statistical test has conditions. A model has conditions. A microscope has calibration settings. A theorem has axioms and definitions. A clinical trial has inclusion criteria. A benchmark has a split, a metric, and rules. A chemical reaction has temperature, solvent, concentration, pressure, and purity. An economic estimate has a population, time period, identification strategy, and data source.

These are not all the same kind of thing, but they play a similar role. They describe where a tool can be used and where a certificate should be trusted.

I prefer “conditions” to “assumptions” because it is broader and less philosophical. Some conditions are assumptions. Others are parameters, protocols, thresholds, versions, calibrations, operating regimes, cohorts, random seeds, or environmental facts.

They should not become a fifth top-level object. Otherwise the ontology starts breeding categories and dies the usual semantic-web death.

Conditions attach to tools and certificates. A tool declares the conditions under which it is meant to operate. A certificate records the conditions under which a result was checked.

Some things will play different roles in different contexts. That is fine. A protocol can be a tool; a protocol version can be a condition. A null model is a tool; choosing that null model for a particular test is part of the certificate’s conditions. The ontology is role-based, not noun-based.

## The shape underneath the paper

So the grammar becomes:

```text
Data D
Tool T, usable under conditions C_T
Result R = T(D)
Certificate P checks the relation between D, T, R, and conditions C_P
Statement S renders R and P in natural language
```

A paper today says:

> We used method X on dataset Y and found Z.

The structure underneath is closer to:

```text
D = the data
T = the tool, model, protocol, or analysis
R = the result
P = the certificate that checks the relation
C = the conditions under which the tool and certificate apply
S = the sentence humans read
```

For example:

```text
D = cohort + expression matrix + phenotype labels
T = preprocessing pipeline + regression model + statistical test
M0 = null/reference tool generating expected data under no association
R = coefficient, p-value, effect size, confidence interval
P = certificate comparing R to M0 under conditions C
S = “Gene X is statistically associated with phenotype Y in this cohort.”
```

That is already much better than a sentence with a citation.

It is also not exotic. Software already works more like this than science does. Package managers know dependencies. Compilers know types. Build systems know versions. Git knows history. CI systems know whether checks passed. Repositories know releases. Containers know environments.

Science has the ingredients, but they are scattered across PDFs, code repositories, lab notebooks, supplementary files, databases, and social trust.

## The same grammar across fields

The point is not that every field should look like mathematics. The point is that many fields already contain the same hidden structure.

In mathematics, the mapping is clean. Definitions, axioms, and previous theorem objects are data. Inference rules and proof assistants are tools. Theorems and lemmas are results. Formal proofs are certificates. A math paper is often a human-readable path through a proof graph that could, in principle, be made explicit.

In physics, data might be detector events, telescope measurements, simulation outputs, calibration records, or previous constants. Tools might be instruments, reconstruction pipelines, physical models, numerical solvers, or statistical tests. Results might be a measured parameter, a detected signal, a confidence interval, a phase diagram, or a failed detection. Certificates include calibration checks, significance estimates, uncertainty propagation, simulation validation, and agreement with independent instruments.

In chemistry, data might be spectra, reaction yields, molecular structures, assay measurements, or computational conformations. Tools include synthesis protocols, instruments, purification methods, molecular dynamics simulations, quantum chemistry packages, and reaction models. Results include a new compound, a measured binding affinity, a reaction mechanism, a crystal structure, or a predicted material property. Certificates include NMR assignments, mass spectrometry, controls, replication, purity checks, computational convergence, and comparison to known standards.

In economics, data might be surveys, administrative records, prices, transactions, labor statistics, or historical archives. Tools include regressions, structural models, natural experiments, instruments, simulations, and causal identification strategies. Results include estimates, elasticities, forecasts, counterfactuals, rankings, and policy effects. Certificates include robustness checks, standard errors, identification assumptions, placebo tests, preregistration, sensitivity analyses, and replication on another dataset.

In biology, the same grammar applies to count matrices, perturbation labels, protocols, microscopes, statistical tests, null models, controls, phenotypes, and dose-response curves. In machine learning, it applies to datasets, tokenizers, checkpoints, prompts, evaluation harnesses, metrics, benchmark splits, and leakage checks.

The fields differ. The objects differ. The standards of trust differ. But the paper is still doing the same overloaded job: packaging data, tools, results, certificates, conditions, and narrative into one object, then asking citations to point at the whole bundle.

![ATLAS detector event display: a result is already a structured object, not just a sentence](/assets/images/science-atlas-event.png)

*ATLAS Collaboration event display, via Wikimedia Commons, CC BY-SA 3.0.*

![A molecular spectroscope: tools and conditions are often physical machines and protocols](/assets/images/science-chemistry-spectrometer.jpg)

*Milda 444, Wikimedia Commons, CC BY-SA 4.0.*

![Economics in OpenAlex: even “the literature” can be data](/assets/images/science-economics-openalex.svg)

*OpenAlex economics works chart, Wikimedia Commons, CC BY 4.0.*


## Science as a graph

Once these objects are separated, they can be linked.

A dataset can be a new version of another dataset. A tool can compose several tools. A model can be trained by one tool and then become a tool in another graph. A result can depend on a dataset, a model checkpoint, a preprocessing pipeline, and a certificate. A certificate can depend on a null model, a statistical threshold, or a formal proof system.

And because results are data, the graph is cumulative:

```text
D0 --T1--> R1
R1 becomes D1
D1 --T2--> R2
P2 certifies R2 under conditions C2
```

This is what science already does. We just hide it in paragraphs.

The article becomes the view. The graph is where the data, tools, results, and certificates live.

![A network visualization: the shape of knowledge is already graph-like](/assets/images/science-c-elegans-network.jpg)

*C. elegans brain network visualization, via Wikimedia Commons, CC BY-SA 3.0.*

Not a blockchain-for-science gimmick. Not a PDF with a token attached. A real provenance layer for knowledge. Each object has a stable identifier. Each version is explicit. Each dependency is inspectable. Each contributor is attached to the thing they actually contributed. Each downstream use creates an edge in the graph.

## What AI changes

AI makes this shift more urgent, but also more possible.

It makes the current paper-shaped system more fragile because scientific prose is becoming cheap. Generating a plausible abstract, introduction, or related-work section is no longer the hard part. Soon, producing more paper-like objects will be easy. The scarce thing will be knowing what, inside that prose, should be trusted.

But AI also gives us a way out. Models can read old papers and propose the objects underneath: the datasets, tools, models, results, certificates, conditions, and citation dependencies. They can notice that two literatures rely on the same benchmark, that a result depends on a particular software version, that a citation is being used for a dataset rather than a result, or that a later paper quietly contradicts an earlier result.

This should not be fully automatic. The analogy is formalized mathematics. A model can help translate an informal proof into Lean, but the community still has to review whether the formalization captures the intended theorem. Scientific formalization should work the same way. AI can propose the graph. Humans, journals, reviewers, authors, curators, and communities can correct it.

![AI extracts structure; communities review it](/assets/images/science-ai-formalization.svg)

AI changes the economics of scientific prose. It does not automatically improve scientific trust. If the literature becomes easier to generate than to audit, the unit of trust has to move below the paragraph.

## Damage control

The killer feature is not better search. It is damage control.

Today, if a dataset turns out to be contaminated, if an analysis pipeline contains a bug, if a benchmark leaked, or if a statistical condition was violated, the consequences are hard to map. Which results depended on the broken object? Which are invalidated? Which are merely weakened? Which have independent support? Which need to be rerun?

In a graph-based system, an error could propagate as a structured signal. If tool `T` version 1.2 is marked as buggy, every result that depends on `T v1.2` can be flagged. Not necessarily retracted immediately, but marked as suspect until it is reproduced with a corrected tool, supported by another certificate path, or shown not to depend on the faulty component.

A dataset could be marked as contaminated. A model could be marked as leaking test data. A certificate could be marked as invalid because a condition was violated. A result could be marked as reproduced, contradicted, corrected, obsolete, or out of scope.

That would be uncomfortable. It would also be more honest. The correction should hit the broken object, not automatically burn the whole bundle. A retraction is often a graph update trapped inside a PDF-shaped ritual. Most scientific errors are not paper-shaped, and our correction mechanisms should not pretend they are.

## Credit

Credit would change too.

Right now, scientific credit is mostly paper-shaped. We count publications, citations, journal prestige, author order. These proxies are not useless, but they are crude. They reward the final narrative package more than the individual scientific objects that make progress possible.

Today, the person who builds the dataset, fixes the pipeline, writes the evaluation harness, validates the protocol, proves the lemma, reproduces the fragile result, or finds the bug often disappears behind the final author list. A graph would not magically make science fair. People will game any credit system worth having. But it would make useful objects harder to ignore.

You could measure how many datasets someone produced, how often a tool is reused, how many downstream results depend on a method, whether certificates survive later audits, and whether downstream work built on an object successfully. This is similar in spirit to citations, but more precise. Instead of citing a whole paper as a vague social gesture, you would depend on a specific object for a specific reason.

## Why now

None of these ideas are completely new. People have tried semantic web systems, nanopublications, research objects, ontologies, registries, identifiers, repositories, and provenance standards. Many of those projects were smart. Most did not become the default way science works.

The failure matters. It suggests the missing piece was not just a better vocabulary. It was timing, incentives, ergonomics, and automation. Too much manual annotation. Too little immediate benefit. Too much ontology design upfront. Too little help for the scientist trying to finish an analysis before midnight.

What has changed is that we now have most of the necessary machinery.

We have cheap computing. We have version control. We have package managers, containers, typed schemas, continuous integration, repositories, persistent identifiers, data archives, model hubs, proof assistants, formal proof libraries, knowledge graphs, and tokenized scientific text. Most importantly, we now have AI systems that can operate across prose, code, data, and formal structure.

That combination changes the problem. We no longer need every scientist to manually turn their work into a perfect graph. AI can draft the structure. It can extract candidate data objects, tools, results, certificates, conditions, and citation edges from existing papers. It can trace what a citation is actually doing: reusing a dataset, relying on a method, accepting a result, challenging a result, copying a benchmark, or inheriting a flawed condition.

The hard part will not be generating more scientific text. That will be easy. The hard part will be maintaining the architecture of trust underneath the text.

Future rigorous work will look less like “write another paper” and more like: define the objects clearly, expose their dependencies, say what each citation contributes, record what conditions apply, attach certificates where possible, and track whether each result is supported, contradicted, obsolete, reproduced, or still uncertain.

That is a different kind of scientific labor. It is closer to formalizing mathematics, maintaining open-source infrastructure, and curating a living knowledge graph than to simply publishing another PDF. It will still need human judgment. But AI can make the first pass cheap enough that communities can spend their effort on review, correction, and trust.

## Keep the story, expose the machinery

The goal is not to kill the paper. The goal is to stop asking it to be a database, a provenance system, a credit ledger, a lab notebook, a code repository, and a trust mechanism all at once.

Keep the essay. Keep the story. Keep the part where a scientist explains why the result is surprising, why the method is elegant, why the negative result matters, or why a strange observation might open a new field. That is not decoration. It is how humans understand science.

But underneath the story, the scientific objects should be exposed.

This dataset. This version. This tool. This model. This result. This certificate. This condition. This citation edge. This correction. This dependency. This trust status.

If a tool breaks, we should know what breaks downstream. If a result survives three independent certificate paths, we should see that too. If a citation is only borrowing a dataset, it should not be counted as support for a result. If someone built the dataset, maintained the benchmark, proved the lemma, or found the bug, the graph should make that visible.

A PDF is a good way to tell the story of a result. It is a bad place to hide the machinery of trust.

The next version of science should keep the story and expose the machinery.
