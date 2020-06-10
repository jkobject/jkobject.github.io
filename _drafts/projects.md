---
title: "Draft projects"
excerpt: "Here I will write all my project ideas!"
sitemap: true
permalink: /my_projects/
layout: default
published: false
---

## Creating a pharmaceutical as good supplement for things that are preventative

We are now facing a big issue. We know of many mechanism of aging, cancer, overweight...
However most of these diseases imply not curing them but preventing them before they happen.
It can be done through better lifestyle. Which a lot of people are undertaking with more or less efficiency and often getting trapped by fake meds. that can even harm them.
Why actual medicine did not rushed into this. We know how to have mice live 40% longer, make them cancer free or prevent them from getting overweight whatever their diet since decades. Why hasn't this knowledge been transfer to humans? one reason is FDA regulation. How can you test this? It would take thousands of people and many decades. It is untestable in humans. One way would be to create a pharmaceutical company that act in everyway like a regular one but does not get FDA approval and sell its products as food supplements. Its challenge would be to convince the right people that this is 100 times more potent than what they used before but might have some danger. And to put in place the right monitoring mechanisms to prove both harmlessness and potency of these drugs.

## Create a new platform for Bio Experiment:

Parse Geo and sra and.. to really create a Google of experiment. Will help people not even having to publish. As you would cite the experiments themselves, redo the experiments, comments, rank them... to really bring the possibility to meta analyse them and not redo experiments you don't need to redo based on the quality of the ones already done. I am not talking here only about sequencing but also WB, protein degradation, drug treatments... Each experiments would be searchable organized by replicates (accross labs) and citable (research paper associated or not)

## BIO Research idea (from Lee rubin)

Viral transduction of three transcription factors can reprogram adult somatic cells to induced pluripotent cells that possess many of the known characteristics of embryonic stem cells. Unfortunately, the potential for aberrant integration of foreign genetic material into the host’s genome and the expression of reprogramming factors with oncogenic potential limit the therapeutic utility of these cells. Such limitations could be overcome by identifying small molecules that compensate for the removal of each of the transcription factors by either inducing their endogenous expression or by mimicking their activities during the reprogramming process. To this end, we designed a series of high-content screens, each based on the activation of Oct4::GFP in mouse embryonic fibroblasts. Using carefully chosen annotated compound libraries, we identified small molecules capable of selectively replacing Sox2, Klf4 and Oct4. Induced pluripotent cells derived using the identified small molecules appropriately express all stem cell markers, can be directed to differentiate in vitro, form teratomas composed of tissue from all three embryonic germ layers, contribute to the inner cell mass of a blastocyst, and yield live chimeric offspring. Thus, somatic cells reprogrammed using the identified small molecule replacement compounds are likely bona fide induced pluripotent cells.

The small molecules that replaced Sox2 and Klf4 could be used to reprogram adult somatic cells with the efficiency achieved through overexpression of the transcription factors themselves. In addition, the use of such mechanistically annotated compounds allowed us to identify novel pathways in the reprogramming process. Finally, the chemical replacement of critical reprogramming factors demonstrates the feasibility of reprogramming adult somatic cells to a pluripotent state using solely small molecules. We are currently testing combinations of the small molecule replacers to provide a complete chemical reprogramming method.
--Lee Rubin

-------------------
## Clinical AI

for a patient and clinic prediction what one would want to gt is a system which hierarchically classify things that one can measure clinically to predict in the end a disease (one might see that as a network of interconnected values (hidden ones that one might not have the opportunity to measures and how they related to one another and the probability of each given the other). in this system you could just say you cough and get a really approximate result of what is most likely to happen to you. then you can add more measures, ages, sizes, sex, skin look, eye look etc, etc, x ray etc. what is interesting given this and that. such a network can be loosely built by hand, expecially whan binary/real values can be given. but for most complex conditions, it has to be learnt.(what images are predicting etc) however, one cannot learn such a complex system, in fact, even us humans as groups of millions of individuals diificulty manage to understand it even after generations. But one might use this knowledge to prespecify weights and decisions in this network given measures using what doctors use. this is the hand currated part. then one might also want to subtrain different parts of the architecture such as image recognition for skin problems and what diseases it is most likely to predict and then condition those prediction on hand tuned parameters and add them in the full model. the goal is to output two things, both an action/attentional values over the many possible measures one might need to understand more about the disease and also a prediction of what is most likely happening. 

in this system, it would be of help both for the clinitian community to categorize in one network, the realtionship of each measures to outcomes etc. 

This system can then be hand improved by physician looking at what they know is and isn't happening and learn more correlation and weights from this clinician feedback. 

obviously it needs to be a graphical model to have the uncertainty of each measures and outcomes

once one is training this model, it may be used in a reinforcement learning framework where one want's to train a model to select an action given a state. Here given the highly hierarchical sets of action that mahy be taken. it might be good to train a model to select a set of models etc... 

hereyou don't need to run all possible experiment. the model would reuse probability and correlations to guess what the outcome would be if we change this or that parameter


------------------------------------------


## Avion 3.0

petit avion grand voilage, utilisant du carburant peut chere (biocarbu/hyrdrogene...) autonome, avec aucun employé, les gens sont self policied et monitoré par une IA. film/netflix etc quoi qu'il arrive. plateau roulant/boisson a volontée etc.. Droit de sedater les enfants avec un xanax/somnifère dans la boisson . pas de sécurité parce que pas possible de détourner l'avion. murs antibruit, casque realité virtuelle avec diminution nausée lié aux mouvements de l'avion. beaucoup de plus de capteurs de vols, redondancex1000 et interne aussi. permettant de diminuer drastiquement toute possibilté de problème. logiciel de qualité aérospatial. ofc internet dans l'avion pour tous. 
pas de fenetres bc VR. bagages au poid + taille. Prix calculé sur place mais estimé en temps réel par rapport a la demande.siege reglable automatique par rapport a la taille de chacun ! diminution espace autour pour mettre plus de monde. possibilité d'être dans des couchettes. (plus organique/bordelique mais aussi psychologiquement acceptable -> moins de stress) + 2/3 espaces tables. screening des passagers dans l'avion. plus besoin d'aéroport. tour de controle decentralisée. accepte les passagers de dernière minutes. aéroport peut être juste une piste d'attérissage.  

---------------------------------------

## Banque
imagine une banque comme ça : Une Banque en ligne : on accepte tous en entrée. connecté à réseau social et autre.
entièrement transparente et décentralisée. Permet de switcher de "currency comme on veut ( bitcoin, euro, dollars...). permet de choisir les offres par rapport à ce que le client définis comme ce qu'il aime. ( écologie, économie, social, transport ... ) et les bénéfices sont a des taux variables par rapport à ça mais toujours au dessus de 0. La banque est possédée par ses clients qui peuvent décider de "bloquer un de leur compte épargne" cela permet de dire "j'achete tant de la banque" elle peut aussir gérer pour le client des actions chez .. et ..  (tout cela est évidement full intelligence artificielle) et l'argent n'appartient pas à la banque mais à chaques personnes. L'utilisateur choisi aussi son niveau de risque et tout. Il a accès à tout ce que fais la banque en son nom et peut décider de se retirer ou quoi de certains deal.  (pour un crédit par exemple a banque est sécurisée par rapport à la quantité d'info qu'elle a sur quelqu'un et donc comment elle peut planifier sur l'avenir. ( l'argent d'un mec qui veut du social ira dans un pret a la consomation d'un mec pauvre ou alors dans un projet d'entreprise d'un jeune de banlieu)...

Une Banque en ligne : on accepte tous en entrée. connecté à réseau social et autre.
entièrement transparente et décentralisée. Permet de switcher de "currency comme on veut ( bitcoin, euro, dollars...). permet de choisir les offres par rapport à ce que le client définis comme ce qu'il aime. ( écologie, économie, social, transport ... ) et les bénéfices sont a des taux variables par rapport à ça mais toujours au dessus de 0. La banque est possédée par ses clients qui peuvent décider de "bloquer un de leur compte épargne" cela permet de dire "j'achete tant de la banque" elle peut aussir gérer pour le client des actions chez .. et ..  (tout cela est évidement full intelligence artificielle) et l'argent n'appartient pas à la banque mais à chaques personnes. L'utilisateur choisi aussi son niveau de risque et tout. Il a accès à tout ce que fais la banque en son nom et peut décider de se retirer ou quoi de certains deal.  



## Assurance
 je repensais a ton truc de société d'assurance pour voiture autonome. Je me disais un truc marrant quand meme. A quoi ils servent les mecs dans les assurances ? 
Je veux dire Si j'ai un mec qui veut être assuré il a juste a mettre de l'argent dans un pot commun avec d'autre gens et ensuite si il a un probleme il se fait rembourser) si il a un accident il remplis un constat et se fait rembourser par l'assurance du gars. Il y a pas tant de paramètres que ça au final. le nombre de gars qui ont besoin de se faire rembourser ( ce qui sort ) ceux qui mettent de l'argent dans les assurances ( ce qui rentre ). tu résout l'équation et si tu as une bonne  trésorerie (pour courvrir les éventuels ups&downs) il devrait pas y avoir de pb. l'autre partie du métier d'assureur c'est de checker que le mec doit bien se faire rembourser. ça semble simple comme ça mais au final il faut des règles du genre : qui s'en assure ? un employé, non ?  comment ça marche ça ?
 http://www.iiminfo.org/CONSUMERS/HowInsuranceWorks
https://www.nerdwallet.com/blog/insurance/expert-faq-insurance-investigators-fight-fraud/
grosso modo c'est un algo qui fait tout le boulot et sinon il y a une petite team de mec chargé de mener l'enquête pour bien vérifier qu'il y a fraude. ( Dans le cas d'une voiture autonome tu sais direct d'ou viens de pb vu que tu as toutes les data de la voiture )
donc voila le concept tout con pour une voiture autonome, un programme informatique sur la blockchain (d'abord uniquement pour les possesseurs de tesla puis d'autres voitures ) qui t'assure directement après que tu aie put prouver que tu étais en conduite autonome. pas besoin de plus. 
tu as un cout d'infrastructure de 0.1% de ce que les autres assurances ont. tu te fais 0 benefs sur l'argent que les mecs mettent. juste en vendant des services annexe a cette blockchain tel que les appareil pour verifier que la voiture était en conduite autonome ou aussi les services de verification d'infraction.
 https://etherisc.com/
 limite meme pas, tu te fais de la tune en ayant un peu de la valeure de cette blockchain et si ta boite marche la valeure augmente et tu deviens riche, comme le mec avec le Ripple.
Putain les mecs ont un Loss Ratio de 60% !! sans compter les benefs des investissements. avec le systeme proposé la. sans compter le coup que c'est des voitures autonomes mais tu pourrais proposer au client une assurance 2fois moins chère. Si tu fais même 20% moins cher pour tout ce qui est construction ou fret ou assurance vie tu change le monde
[01:21, 11/1/2018] +33 6 52 66 34 43: https://www.statista.com/statistics/437126/loss-ratio-pc-insurance-usa/

---------------------------

Réseau de neurones qui lie des gif à des phrases / messages
Transformer une parti des messages en vidéos qui s'arrêtent automatiquement pour reproduire le sens du message

-------------------

## Reduction d'énergie de ouf ce serait : 
si tu as un truc qui te livre chez toi a intervale regulier et tout en mode amazon essentials ou intermarché delivery ( moins d'energie de transport vu que tu as pas besoin de marché partout et d'avoir chaques individus qui se dépace et prend la voiture..) tu le ferais en utilisant aucun plastiques. juste le mec a un cadis en metal. et tout est distribué dans différents type de récipients en aluminiums  (même style que les cannetes de coca, 100% recyclables à l'infinie ) 
https://www.azocleantech.com/article.aspx?ArticleID=585 
et qui seraient rendu au prochain passage pour être nétoyées ou recyclé et réutilisé. 
aluminium intake is not from cans 
https://enveurope.springeropen.com/articles/10.1186/2190-4715-23-37 


---------------------------------------------
## APIs

Les API sont partout et utilisées a merci par les dévellopeurs. Elle permettent d'acceder a quaisment toutes informations sur le web d'une façon beaucoup plus structurées que les interfaces grpahiques disponibles aux utilisateurs lambda. Elle sont toutefois extrêment brutes et donc inutilisable par le sutilisateurs. toutes formes de requêtes sont disponibles via les API rest. de query a des bases de données, des calculs et autres. de plus via l'arrivées de microservices ( des petites unités de resolutions de fonction simple via interface http) et du cloud computing permettant une scalabilité et versatilité sans précédent. Il semble que ce genre de communication ne face que grandir. Quel est le but d'un assistant virtuel se rapprochant le plus d'une intelligence généralisée ? 
Une entitée capable de répondre a tout types de requêtes et d'être flexible sur la capacité d'actions a effectuées. Cela nécéssite 3 choses fondamentales. Une représentation de l'information encodée de façon la plus versatile possible et une capacité d'encoder et de décoder cette information depuis n'importe quelle source (cross modalité).Une capacité a aller envoyer des requêtes complexes d'information a tout ce qui peut atteindre sa portée. Une capacité a aller utiliser des outils (reflexifs et algorithmiques nouveaux selon la tache a effectuée). 
On peut voir ici l'empleur de la tache a effectuée. Il y a un outils évident. Les IA récentes utilisants des résaux de neurones profonds. Cependant il y a un autre outils fondamental. Les APIs. Si nous arrivons a créer en principalité, une IA qui comprend les requêtes et/ou qui utilise le web pour les comprendres et les décomposes sous forme de taches elles même permise par la création de requête etc. Pour cela il doit être capable d'analyser des corpus de textes et memes des liens entre eux. il doit être capable de comprendre la requête. est ce que je suis beau ? création d'une requete google. je = utilisateur =  personne. beau + utilisateur ? beau + personne, + humain .. beau, inverse, moche.. philosophie : inutile, important. -> contradictoire.
essais en français , en anglais. requete maximisé sur ce site. API, demande photo pour trouver si beau ou moche


-----------------
## Hey I have an idea for a solution to the lack of data in biomed and bio info using ML.

What if we could let user store all their medical information in a “safe” on our server freely and securely. So that hospitals and doctors could have access to it by requesting permissions to you or a family member. On the other side, we would  let registered companies or researchers ask for data directly to our clients, basically rent it by big batches. They could then use it to explore the information at only one need. They need to produce outputs that could be beneficial to the user and this output belongs to the user. For example I am using ML to detect and train the probability of cancer according to ... then the output can either be a research paper, that will be sent to the user and the data would then need to be returned.  or a new algorithm to detect early stages of cancer. or just a complete fail. what happens is the user sees how wants his data, what for, can accept and then see the output. his contribution is stored and can be retrieved. If money is made by selling an algorithm trained on his data, he will get a fraction of it. the website as well. 
For the company that is selling we can say that the data is 50% of its algorithm and so the website and its underlying user shares the rest. ( 40% for the users and 10% for the website that stores and keeps everything clean etc.. ) (modifié)

I know that sometimes their medical records are kept by the doctor or the hospital but we could have a process whereby a user gives us the name of the institution he went in and we send a request to this institution with a link to authenticate and send the data.
the website has three front ends. One for the data holder, One for companies and researchers requiring the data, one for the hospitals and doctors possessing some data. 
the goal is to be trustworthy, secure, acknowledged and to apply a lot of big data analytics to present, order, format the information in the best way possible.


-----------------
We need to do as Soon as possible, a litterature review of cancer research.. 
This should give much introspection about hierarchy and generalitied underlying it 