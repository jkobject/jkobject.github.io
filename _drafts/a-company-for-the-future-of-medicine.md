---
title: "A Future for healthcare"
excerpt: "An idea for building a truly preventative and personalized medicine, future. "
category: "Biology & Medecine"
---

Avoir un système de santé via la récupérations de données en béton via des tests intenses sur les souris.  une preuve de concept qui permetrait de convaincre les gens de donner leur data. SI on augmente le taux de survie de X chez les souris ça peut convraincre... on peut ensuite faire la meme chose avec des cochons (groupe test et groupe temoin et regarder ce que ça permet)
meme choses pour les opérations chirurgicales robotiques
le problème de la santé du 21 eme siecle c'est que personne ne veut donner ses données et ne veut être monitoré. les gens sont plus attentifs a la possibilité de mourir le plus vite possible et de donner leurs organes quand ça va pas que de donner leurs scanner, rythmes cardiaques et autres données volatolomiques a des proffessionels pour potentiellement ne jamais soufrir de maladies graves et chroniques et faire avancer la recherhce

IA qui dit les maladies que tu as le plus de chance d'avoir. 
Entreprise remplaçant la secu en monitoran tout dans des big data 
Hopital du futur pour riche au début et qui suit le développement et augmentation dépense médicale qui remplacerait les problemes inhérents de la sécu


We are now facing a big issue. We know of many mechanism of aging, cancer, overweight...
However most of these diseases imply not curing them but preventing them before they happen.
It can be done through better lifestyle. Which a lot of people are undertaking with more or less efficiency and often getting trapped by fake meds. that can even harm them.
Why actual medicine did not rushed into this. We know how to have mice live 40% longer, make them cancer free or prevent them from getting overweight whatever their diet since decades. Why hasn't this knowledge been transfer to humans? one reason is FDA regulation. How can you test this? It would take thousands of people and many decades. It is untestable in humans. One way would be to create a pharmaceutical company that act in everyway like a regular one but does not get FDA approval and sell its products as food supplements. Its challenge would be to convince the right people that this is 100 times more potent than what they used before but might have some danger. And to put in place the right monitoring mechanisms to prove both harmlessness and potency of these drugs.


for a patient and clinic prediction what one would want to gt is a system which hierarchically classify things that one can measure clinically to predict in the end a disease (one might see that as a network of interconnected values (hidden ones that one might not have the opportunity to measures and how they related to one another and the probability of each given the other). in this system you could just say you cough and get a really approximate result of what is most likely to happen to you. then you can add more measures, ages, sizes, sex, skin look, eye look etc, etc, x ray etc. what is interesting given this and that. such a network can be loosely built by hand, expecially whan binary/real values can be given. but for most complex conditions, it has to be learnt.(what images are predicting etc) however, one cannot learn such a complex system, in fact, even us humans as groups of millions of individuals diificulty manage to understand it even after generations. But one might use this knowledge to prespecify weights and decisions in this network given measures using what doctors use. this is the hand currated part. then one might also want to subtrain different parts of the architecture such as image recognition for skin problems and what diseases it is most likely to predict and then condition those prediction on hand tuned parameters and add them in the full model. the goal is to output two things, both an action/attentional values over the many possible measures one might need to understand more about the disease and also a prediction of what is most likely happening. 

in this system, it would be of help both for the clinitian community to categorize in one network, the realtionship of each measures to outcomes etc. 

This system can then be hand improved by physician looking at what they know is and isn't happening and learn more correlation and weights from this clinician feedback. 

obviously it needs to be a graphical model to have the uncertainty of each measures and outcomes

once one is training this model, it may be used in a reinforcement learning framework where one want's to train a model to select an action given a state. Here given the highly hierarchical sets of action that mahy be taken. it might be good to train a model to select a set of models etc... 

hereyou don't need to run all possible experiment. the model would reuse probability and correlations to guess what the outcome would be if we change this or that parameter

--> this system needs to become an insurance company at one point. 



What if we could let user store all their medical information in a “safe” on our server freely and securely. So that hospitals and doctors could have access to it by requesting permissions to you or a family member. On the other side, we would  let registered companies or researchers ask for data directly to our clients, basically rent it by big batches. They could then use it to explore the information at only one need. They need to produce outputs that could be beneficial to the user and this output belongs to the user. For example I am using ML to detect and train the probability of cancer according to ... then the output can either be a research paper, that will be sent to the user and the data would then need to be returned.  or a new algorithm to detect early stages of cancer. or just a complete fail. what happens is the user sees how wants his data, what for, can accept and then see the output. his contribution is stored and can be retrieved. If money is made by selling an algorithm trained on his data, he will get a fraction of it. the website as well. 
For the company that is selling we can say that the data is 50% of its algorithm and so the website and its underlying user shares the rest. ( 40% for the users and 10% for the website that stores and keeps everything clean etc.. ) (modifié)

I know that sometimes their medical records are kept by the doctor or the hospital but we could have a process whereby a user gives us the name of the institution he went in and we send a request to this institution with a link to authenticate and send the data.
the website has three front ends. One for the data holder, One for companies and researchers requiring the data, one for the hospitals and doctors possessing some data. 
the goal is to be trustworthy, secure, acknowledged and to apply a lot of big data analytics to present, order, format the information in the best way possible.
