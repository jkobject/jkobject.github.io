# Gene Regulation Landscape — detailed construction notes
### From DNA to proteins — reductionist architecture (v7)

*Clawd · 2026-05-01 / updated 2026-06-18 · 37 mechanisms · 2 meta-principles · 7 layers*

These notes are the technical companion to the current Gene Regulation
Landscape v7 graph. They document the 37 mechanism boxes, 2 meta-principles, 73
mechanism relations, and 7 meta-style annotations used in the rendered figure.
The rendered figure was generated from the Graphviz source file
[`gene-reg-v7.dot`](/assets/documents/gene-reg-v7.dot). The content preserves
the original French working language while keeping the counts and mappings
aligned with the current graph.

---

# Cartographie des mécanismes de régulation génétique
### De l'ADN aux protéines — Architecture réductionniste (v7)

*Clawd · 2026-05-01 / mis à jour 2026-06-18 · 37 mécanismes · 2 métaprincipes · 7 couches*

---

## Résumé exécutif

La cellule régule l'expression de ses gènes à **7 niveaux emboîtés**, de l'organisation tridimensionnelle du génome à la dégradation sélective des protéines. On dénombre 37 mécanismes distincts dans les boîtes du graphe, plus 2 métaprincipes transversaux indiqués par des styles de bordure (**LLPS** et **DECAY**). Une analyse transversale révèle aussi **3 stratégies** récurrentes : (A) contrôle de l'accessibilité physique d'un substrat, (B) écriture/lecture/effacement d'une marque réversible, (C) couplage cinétique entre deux processus. Tout le reste est une implémentation moléculaire de l'un de ces trois principes à un niveau différent.

---

## Comment lire ces notes

- Les **37 mécanismes** sont les boîtes du graphe, réparties en 7 couches.
- Les **2 métaprincipes**, **LLPS** et **DECAY**, ne sont pas des boîtes mécanistiques ordinaires : ils sont indiqués par des styles de bordure sur les mécanismes concernés.
- Les **73 arêtes mécanistiques** décrivent des relations causales, de couplage ou de feedback entre mécanismes.
- Les **7 annotations méta** rattachent LLPS et DECAY aux mécanismes qui les incarnent.

## Notation du graphe et abréviations

| Terme | Sens |
|-------|------|
| `tx` | Transcription. Le graphe évite de l'utiliser pour la traduction afin de ne pas créer d'ambiguïté. |
| `co-tx` | Co-transcriptionnel : couplé à la progression de Pol II ou à l'ARN naissant. |
| `A` | Principe d'accessibilité : rendre un substrat disponible ou inaccessible. |
| `B` | Principe marque/lecture : une marque réversible produit un effet selon son lecteur et son contexte. |
| `C` | Principe de couplage cinétique : la vitesse d'un processus change l'issue d'un autre. |
| `⊣` | Répression, inhibition ou blocage direct. |
| `(back)` | Feedback ou relation de retour vers une couche amont. |
| `(bidirectionnel)` | Relation réciproque représentée comme couplage à double sens. |
| `(**)` | Couplage cinétique particulièrement important, relié au principe C. |
| `initiation ↑` | Augmentation de l'initiation de la traduction. |
| `RQC` | Ribosome-associated Quality Control. Surveillance des ribosomes bloqués et dégradation du peptide naissant. |
| `NGD` | No-Go Decay. Dégradation liée à un ribosome bloqué sur l'ARNm. |
| `NSD` | Non-Stop Decay. Dégradation liée à un ARNm sans codon stop fonctionnel. |
| `SUMO` | Small Ubiquitin-like Modifier. Petite protéine conjuguée aux substrats comme marque post-traductionnelle. |
| `NEDDylation` | Conjugaison de NEDD8, notamment sur les cullines pour activer des E3 ligases CRL. |
| gras | Dans l'image, le nom en haut de chaque boîte est le nom code du mécanisme et correspond à une entrée 1-to-1 du glossaire. |
| italique | Dans l'image et les descriptions, l'italique sert aux noms de gènes/protéines quand cela aide la lecture ; les boîtes du graphe restent des noms de mécanismes. |

## Glossaire des concepts non-gènes

| Terme | Sens |
|-------|------|
| Compartiments A/B | Domaines chromatinien vus en Hi-C ; A est plutôt actif/euchromatique, B plutôt inactif/hétérochromatique. |
| TAD | Domaine d'association topologique ; voisinage chromatinien isolé par des frontières comme CTCF/cohésine. |
| Boucle enhancer-promoteur | Contact 3D rapprochant un enhancer distal d'un promoteur cible. |
| Super-enhancer | Cluster dense d'enhancers enrichi en TF maîtres, Mediator, BRD4 et Pol II. |
| Condensat / LLPS | Séparation de phase liquide-liquide concentrant des molécules dans une phase dense sans membrane. |
| Méthylation ADN | Ajout de groupements méthyle sur l'ADN, souvent lié à la répression transcriptionnelle des promoteurs. |
| Marque histone | Modification chimique d'une histone, par exemple acétylation ou méthylation, lue par des protéines de chromatine. |
| Remodelage chromatine | Repositionnement, éjection ou échange de nucléosomes par des complexes ATP-dépendants. |
| ncRNA | ARN non-codant fonctionnel non traduit en protéine. |
| Pausing Pol II | Pause proximale de l'ARN polymérase II avant l'élongation productive. |
| Phosphorylation CTD | Phosphorylation de la queue CTD de Pol II coordonnant transcription et maturation de l'ARN. |
| 5' capping | Ajout d'une coiffe m7G à l'ARN naissant, nécessaire à la protection, l'export et la traduction. |
| Splicing alternatif | Choix régulé des exons produisant plusieurs isoformes depuis un même gène. |
| Polyadénylation alternative | Choix de sites de clivage/polyA différents, souvent avec changement de longueur du 3'UTR. |
| A-to-I editing | Édition adénosine-inosine ; l'inosine est souvent lue comme une guanosine. |
| m6A | N6-méthyladénosine, modification réversible de l'ARN interprétée par des readers. |
| RBP | RNA-binding protein, protéine de liaison à l'ARN. |
| miRNA-RISC | MicroARN chargé dans le complexe RISC pour réprimer ou déstabiliser des ARNm cibles. |
| ceRNA | Competing endogenous RNA ; ARN pouvant tamponner des miRNA via des sites cibles partagés. |
| NMD | Nonsense-mediated decay ; surveillance et dégradation des transcrits à codon stop prématuré. |
| Déadénylation / décapping | Retrait de la queue polyA et de la coiffe 5', engageant souvent un ARNm vers la dégradation. |
| RNA G-quadruplex | Structure ARN riche en guanines pouvant bloquer le scanning ou changer le destin de l'ARN. |
| Stress granule / P-body | Condensats cytoplasmiques ARN-protéine associés au stockage, à la répression ou au decay. |
| Traduction cap-dépendante | Initiation canonique par reconnaissance de la coiffe puis scanning du 5'UTR. |
| ISR / eIF2α-P | Integrated Stress Response ; phosphorylation d'eIF2α diminuant l'initiation globale mais favorisant certains ARNm. |
| uORF | Upstream open reading frame, ORF dans le 5'UTR pouvant détourner les ribosomes. |
| IRES / ITAF | Internal Ribosome Entry Site et facteurs auxiliaires permettant une initiation cap-indépendante. |
| RQC / NGD / NSD | Ribosome quality control, no-go decay et non-stop decay ; surveillance de la traduction anormale. |
| O-GlcNAc | Modification sucre réversible sur Ser/Thr pouvant interagir avec la phosphorylation. |
| Chaîne ubiquitine | Polymère d'ubiquitine dont le type de liaison, par exemple K48 ou K63, influence le destin du substrat. |
| SUMOylation | Conjugaison de SUMO, souvent impliquée dans les interactions nucléaires et l'assemblage de complexes. |
| Neddylation | Conjugaison de NEDD8, surtout aux cullines, activant des E3 ligases CRL. |
| Protéasome | Complexe protéolytique dégradant beaucoup de protéines ubiquitinées courtes ou endommagées. |
| Autophagie sélective | Clearance lysosomale de cargos spécifiques : agrégats, organites ou complexes ubiquitinés. |
| UPR | Unfolded Protein Response ; réponse au stress du réticulum endoplasmique. |
| PAR / ADP-ribosylation | Signalisation par poly-ADP-ribose, souvent autour des dommages ADN et des condensats. |

## Architecture réductionniste — 3 stratégies fondamentales

Le graphe ne cherche pas seulement à lister des mécanismes. Il les réduit à
trois logiques récurrentes qui réapparaissent à chaque couche.

```
Stratégie A — CONTRÔLE DE L'ACCESSIBILITÉ
  "Rend un substrat accessible ou inaccessible à sa machinerie"
  Instances : OPENER/SHUFFLER → TF access
              FENCES/BRIDGES → E-P proximity
              DARTS/SPONGE → mRNA availability
              VAULT → translational access

Stratégie B — MARQUE RÉVERSIBLE + LECTURE CONTEXTUELLE
  "La même marque produit des effets différents selon le lecteur et le contexte"
  Instances : SILENCER/WRITER-A/WRITER-R (histone code + DNA methylation)
              STAMP (m6A → YTHDF1 ou YTHDF2 selon le contexte)
              ROUTER (K48 → protéasome ; K63 → signalisation/autophagie)
              SWITCH (phospho → activation ou dégradation selon le substrat)

Stratégie C — COUPLAGE CINÉTIQUE
  "La vitesse du processus A détermine le résultat du processus B"
  Instances : Pol II rate → SPLICER (kinetic window)
              H3K36me3 déposé par SCRIBE → SPLICER (même couplage, autre niveau)
              TC limiting (BRAKE) → DECOY bypass → FORGE sélectif ATF4
              Codon pause (TEMPO) → MATURE co-traductionnel
              IRES-TF loop (synthèse ATF4 → reprogrammation transcriptomique)
```

## Carte des boîtes du graphe

| Couche | Mécanismes |
|--------|------------|
| 0 — Génome 3D | ZONES, FENCES, BRIDGES, HUBS |
| 1 — Épigénétique | SILENCER, OPENER, WRITER-A, WRITER-R, SHUFFLER, GUIDES |
| 2 — Transcription | KEYS, SCRIBE |
| 3 — Co-transcriptionnel | SHIELD, SPLICER, TRIMMER, RECODER |
| 4 — Post-transcriptionnel | STAMP, READERS, DARTS, SPONGE, CENSOR, TIMER, CLIPS, VAULT |
| 5 — Traductionnel | FORGE, BRAKE, DECOY, BYPASS, TEMPO, INSPECTOR |
| 6 — Post-traductionnel | SWITCH, ROUTER, TETHER, LICENSE, DESTROY, MATURE, PAR |
| Méta | LLPS, DECAY |

## I. Les 7 couches — Explication et mécanismes

### Couche 0 — GÉNOME 3D
*Le génome n'est pas linéaire mais tridimensionnel. L'organisation spatiale détermine quels enhancers peuvent parler à quels promoteurs.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **ZONES** | Compartiments A/B | Grandes régions chromatiniennes (~5–20 Mb) détectées par Hi-C. Compartiment **A** = euchromatine transcriptionnellement active (H3K27ac, H3K4me3). Compartiment **B** = hétérochromatine inactive (H3K27me3, H3K9me3, méthylation ADN, lamina nucléaire). La transition A↔B accompagne la différenciation cellulaire. |
| **FENCES** | TADs (Topologically Associating Domains) | Domaines d'interactions préférentielles de ~0.1–2 Mb souvent délimités par des frontières CTCF convergentes. Mécanisme dominant : Cohesin extrude des boucles jusqu'à blocage par paires CTCF convergentes → insulation partielle des interactions inter-domaine. Les frontières réduisent fortement les contacts enhancer-promoteur aberrants, mais ne les abolissent pas toujours ; l'effet sur l'expression dépend du locus et du type cellulaire. |
| **BRIDGES** | Boucles Enhancer→Promoteur | Contacts physiques spécifiques entre un enhancer distal et son promoteur cible, souvent mais pas exclusivement à l'intérieur d'un même TAD. Médiés ou stabilisés selon le contexte par Mediator, Cohesin, YY1, ZNF143, LDB1 et d'autres facteurs. Peuvent dépasser 1 Mb de distance linéaire. |
| **HUBS** | Super-enhancers / Condensats Pol II | Clusters d'enhancers ordinaires couvrant 5–50 kb, très denses en TF maîtres, BRD4, Mediator, Pol II. Ils peuvent former ou alimenter des condensats transcriptionnels enrichis en coactivateurs, mais "super-enhancer" (définition ChIP-seq) et "condensat" (objet physique dynamique) ne sont pas strictement synonymes. Très sensibles à JQ1 (inhibiteur BET) dans plusieurs modèles, surtout oncogéniques. Pilotent souvent les gènes d'identité cellulaire et certains oncogènes. |

---

### Couche 1 — ÉPIGÉNÉTIQUE
*Modifications héritables (ou semi-stables) de la chromatine qui changent l'accessibilité sans altérer la séquence ADN.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **SILENCER** | Méthylation ADN | Ajout d'un groupement méthyle sur la cytosine (5mC) aux dinucléotides CpG. **Writers** : DNMT1 (maintenance lors de la réplication), DNMT3A/3B (*de novo*). **Erasers** : TET1/2/3 (oxydation 5mC→5hmC→5fC→5caC, puis réparation BER). **Readers** : protéines MBD (recrutent HDACs → répression). Effet général : répression aux CpG islands des promoteurs. Exception : méthylation des corps de gènes → stabilisation de l'élongation Pol II. Seul mécanisme héritable par division cellulaire sans transcription. |
| **OPENER** | Acétylation des histones | Ajout d'un groupement acétyle sur les lysines d'histones (H3K27ac, H3K9ac, H4K16ac). **Writers (HATs)** : p300/CBP, GCN5, PCAF, MOF. **Erasers (HDACs)** : 18 HDACs en 4 classes. **Readers** : bromodomaines (BRD4, BRG1 de SWI/SNF). Mécanisme : l'acétyle neutralise la charge positive de la Lys → répulsion avec l'ADN négatif → relâchement du nucléosome → accès des TF et Pol II. H3K27ac = marque des enhancers actifs. |
| **WRITER-A** | Méthylation histones activatrice | H3K4me3 (promoteurs actifs), H3K4me1 (enhancers), H3K36me3 (corps de gènes en élongation), H3K79me2 (télomères/élongation). **Writers** : MLL1-4/KMT2A-D, SET1A/B (H3K4); SETD2 (H3K36me3, déposé par la Pol II Ser2-P pendant l'élongation). **Readers** : PHD fingers (TAF3, BPTF) pour H3K4me3 ; PWWP (DNMT3a, LEDGF) pour H3K36me3. Clé : H3K36me3 recrute des régulateurs du splicing (MRG15 → PTB) → couplage épigénétique-splicing. |
| **WRITER-R** | Méthylation histones répressive | H3K27me3 (gènes Polycomb, répression facultative), H3K9me3 (hétérochromatine constitutive), H4K20me3 (hétérochromatine). **Writers** : EZH1/2 (PRC2, H3K27me3) ; SUV39H1/2, SETDB1 (H3K9me3). **Readers** : CBX proteins/PRC1 (H3K27me3) ; HP1 family/CBX1/3/5 (H3K9me3). H3K27me3 et H3K27ac sont compétitifs sur le même résidu → switch binaire activation/répression. **Bivalent domains** (cellules souches) : H3K4me3 + H3K27me3 simultanés = gènes "poised" prêts à s'activer. |
| **SHUFFLER** | Remodelage chromatine ATP-dependent | Complexes utilisant l'énergie ATP pour repositionner, éjecter ou remplacer les nucléosomes. 4 familles : **SWI/SNF** (BAF, PBAF — activation et répression) ; **ISWI** (NuRD, CHRAC, NURF — espacement) ; **CHD** (CHD1-9 — activation) ; **INO80** (échange de variants d'histones H2A.Z). Recrutés par les TF et par les marques histones via leurs modules lecteurs. |
| **GUIDES** | ncRNA épigénétiques | Petits et longs ARN non-codants qui guident des complexes modificateurs de chromatine vers leurs loci cibles. **piRNA** (24–31 nt, PIWI clade) : silencing des transposons par méthylation ADN *de novo* dans la lignée germinale. **lncRNA scaffolds** (XIST, HOTAIR, KCNQ1OT1) : recrutent PRC2 → H3K27me3 régional. XIST = inactivation du chromosome X. HOTAIR (HOXC) → réprime HOXD via PRC2+LSD1. |

---

### Couche 2 — TRANSCRIPTION
*Contrôle de l'initiation et de la progression de l'ARN polymérase II.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **KEYS** | Facteurs de transcription (TF) | Protéines à domaines de liaison à l'ADN (séquence-spécifiques) et domaines d'activation/répression. **Activateurs** : recrutent HATs (p300/CBP → H3K27ac), KMTs (MLL → H3K4me3), CRC (SWI/SNF), Mediator → Pol II. **Répresseurs** : recrutent HDACs, PRC, NuRD. **Pioneer factors** (FOXA1, OCT4, GATA3) : peuvent ouvrir la chromatine compacte. ~1600 TF humains. Les TF maîtres (OCT4, SOX2, MYC) définissent les super-enhancers. Feedback : plusieurs protéines traduites par des routes non canoniques ou stress-dépendantes (ATF4 via uORF/réinitiation ; HIF-1α ou c-MYC via mécanismes proposés de type IRES selon contexte) sont elles-mêmes des TF. Le protéasome active des TF en dégradant leurs inhibiteurs (IκBα → NF-κB). |
| **SCRIBE** | Pol II + pausing | ARN polymérase II : enzyme ~550 kDa, 12 sous-unités. La queue CTD (répétition YSPTSPS ×52) est un hub de signalisation : **Ser5-P** (CDK7/TFIIH) = initiation/capping ; **Ser2-P** (CDK9/P-TEFb) = élongation ; **Ser7-P** = ARN non-codants. **Pausing proximal** : Pol II stalled 25–50 bp après le TSS par NELF + DSIF. Libération par P-TEFb (recrutée par BRD4 des super-enhancers). ~30–50 % des gènes mammifères sont pausés — permet une réponse rapide et un contrôle précis. **Couplage** : SETD2 (H3K36me3 writer) est lié à la Pol II Ser2-P → H3K36me3 est déposé pendant l'élongation. METTL3/14 est recruté par la CTD → m6A co-transcriptionnel. |

---

### Couche 3 — CO-TRANSCRIPTIONNEL
*Traitements de l'ARN nascent couplés à la progression de Pol II.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **SHIELD** | 5' Capping | Ajout d'une 7-méthylguanosine (m7G) sur le 5' de l'ARN nascent dès ~25-30 nt, co-transcriptionnellement via la Ser5-P CTD. Protection contre les 5'→3' exonucléases. La coiffe est reconnue par eIF4E (initiation traductionnelle) et par CBC (nuclear cap-binding complex → export). Échange CBC → eIF4E lors de l'export nucléaire. |
| **SPLICER** | Splicing alternatif | Excision des introns et jonction des exons par le **spliceosome** (U1/U2/U4/U6/U5 snRNPs + ~150 protéines). ~95 % des gènes multi-exoniques humains produisent plusieurs isoformes. Modes : exon skipping, intron retention, 5'/3' alternative SS, exons mutuellement exclusifs. **Régulation cinétique** : la vitesse d'élongation de Pol II contrôle l'inclusion des exons ("window of opportunity" — Pol II lente → temps pour reconnaître exons faibles). **Code épigénétique** : H3K36me3 recrute MRG15 → PTB/PSF → exon inclusion ; H3K9me3 → Pol II lente → exon skipping. |
| **TRIMMER** | Polyadénylation alternative (APA) | ~70 % des gènes mammifères ont plusieurs sites de clivage/polyadénylation → isoformes avec 3'UTR de longueurs différentes. Mécanisme : complexe CPA (CPSF, CstF, CFI/II) reconnaît la séquence AAUAAA ~20 nt en amont du site polyA. Conséquence : 3'UTR long → plus de sites miRNA et de sites RBP exposés → régulation post-transcriptionnelle plus intense. |
| **RECODER** | A→I Editing (ADAR) | Les **ADARs** (Adenosine Deaminases Acting on RNA) hydrolysent les adénosines en inosines dans des dsRNA. L'inosine est lu comme guanosine → recoding de l'information génétique. **ADAR1 p150** : induit par l'interféron (IRF3/7), cytoplasmique, marque les dsRNA endogènes Alu comme "self". **ADAR2** : constitutif, nucléaire, spécialiste du recoding neuronal (GluR-B Q→R site). Couplage avec le splicing : A→I editing au 5'SS d'éléments Alu → prévention de l'exonisation → prévention du NMD. |

---

### Couche 4 — POST-TRANSCRIPTIONNEL
*Régulation des ARNm matures dans le noyau et le cytoplasme.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **STAMP** | m6A épitranscriptome | **N6-méthyladénosine (m6A)** : modification chimique abondante des ARNm eucaryotes, enrichie près des stop codons, dans les longs exons et parfois dans les 5'UTR. **Writers** : complexe METTL3/14/WTAP ; dépôt souvent co-transcriptionnel. **Erasers** : FTO, ALKBH5. **Readers directs** : YTHDF1/2/3 et YTHDC1. Le modèle classique associe YTHDF1 à la traduction, YTHDF2 au decay, YTHDF3 à la coopération entre sorties, et YTHDC1 au splicing/export nucléaire ; des travaux récents soulignent aussi la redondance partielle des YTHDF cytoplasmiques et leur contribution commune au decay/compartimentage des ARNm m6A. **Readers indirects** : HNRNPC/HNRNPA2B1 (m6A switch structural → accessibilité). m6A agit simultanément sur splicing, export, stabilité et traduction → mécanisme transversal, pas un seul mécanisme. |
| **READERS** | RBPs régulateurs | ~1500 protéines de liaison à l'ARN (RNA-Binding Proteins) humaines. Modules de liaison : RRM, KH, CCCH zinc finger, PAZ, DEAD-box. Régulent toutes les étapes : splicing (SR proteins comme SRSF1-12 = activateurs ; hnRNPs comme PTBP1 = répresseurs) ; stabilité (HuR/ELAVL1 stabilise via ARES ; TTP/ZFP36 déstabilise via ARES → CCR4-NOT) ; traduction (FMRP réprime initiation) ; localisation (Staufen1 → SMD) ; IRES (ITAFs : PTB, DAP5/eIF4G2, hnRNPQ activent IRES). Mutations dans les RBPs → nombreuses maladies (ALS, SMA, syndrome X fragile). |
| **DARTS** | miRNA-RISC | MicroARNs de ~22 nt. Biogenèse : pri-miRNA (Pol II) → **Drosha**/DGCR8 → pre-miRNA (~70 nt hairpin) → export Exportine-5 → **Dicer**/TRBP → miRNA duplex → chargement dans **AGO2** → RISC actif. Mécanisme : appariement imparfait (seed 7 nt, positions 2–8) du miRNA avec le 3'UTR → recrutement CCR4-NOT/TNRC6 → déadénylation + décapping + inhibition traductionnelle. ~2500 miRNA humains, chacun régule ~200–1000 ARNm. |
| **SPONGE** | lncRNA cytoplasmiques | lncRNAs (>200 nt) à localisation cytoplasmique. **ceRNA / éponge à miRNA** : circRNA CDR1as (>70 sites miR-7), HULC, HOTAIR cytoplasm. peuvent séquestrer des miRNAs et décompresser des ARNm cibles lorsque la stoechiométrie miRNA/sites cibles, la colocalisation et l'affinité le permettent. La fonction ceRNA est donc plausible mais souvent surestimée sans validation quantitative. **Activation traductionnelle** : UCHL1-AS (domaine SINEB2) → recrutement de polyribosomes. **Répression traductionnelle** : lincRNA-p21 → recrutement de Rck (hélicase répresseur). **Décoy** : GAS5 (glucocorticoid decoy) imite les GRE → séquestre GR. |
| **CENSOR** | NMD (Nonsense-Mediated mRNA Decay) | Surveillance des ARNm aberrants portant des codons stop prématurés (PTCs). Mécanisme : lors de la traduction, si un ribosome termine à >50–55 nt en amont d'un **EJC** (Exon Junction Complex) → recrutement de UPF1/UPF2/UPF3 → phosphorylation UPF1 par SMG1 → dégradation rapide (décapping + exonucléases). ~5–10 % du transcriptome humain est régulé physiologiquement par NMD (splicing productif vs improductif alternatif). Lien editing : A→I editing au 5'SS d'un exon Alu → prévention exonisation → pas de PTC → pas de NMD (circuit ADAR-SPLICER-CENSOR). |
| **TIMER** | Stabilité / dégradation des ARNm | La demi-vie des ARNm varie de ~20 min (proto-oncogènes) à >24 h (globine). Voie principale : **déadénylation** (CCR4-NOT/PAN2-PAN3 → queue polyA) → **décapping** (DCP1/2 → suppression m7G) → **dégradation 5'→3'** (XRN1). Voie alternative : **exosome** (dégradation 3'→5', complexe ~14 sous-unités). Régulateurs : ARE-binding proteins (HuR stabilise ; TTP déstabilise), miRNAs (→ CCR4-NOT), m6A (YTHDF2 → CCR4-NOT). |
| **CLIPS** | RNA G-quadruplexes (rG4) | Structures secondaires quaternaires formées de tétrades de guanines (G4) stabilisées par des ions K+. Présents dans les 5'UTR (→ bloquent la progression du ribosome 43S → inhibition traduction cap-dépendante), 3'UTR, régions de pause Pol II, télomères. Déroulés par des helicases : DHX36, eIF4A, RHAU. Régulation : m6A peut déstabiliser les rG4 en modifiant la structure secondaire de l'ARN. Interaction avec IRES : rG4 dans 5'UTR peut moduler l'accessibilité des IRES. |
| **VAULT** | Stress granules / P-bodies | Deux types de **condensats cytoplasmiques** (LLPS) de stockage/dégradation des ARNm. **Stress granules** (G3BP1, TIA-1, PABPC) : stockage temporaire des ARNm sous stress → dissolution lors de la résolution → libération vers la traduction. **P-bodies** (DCP1/2, XRN1, CNOT) : sites de décapping et dégradation. Échange dynamique de matière entre SG et PB. Formation déclenchée par : ISR (eIF2α-P), stress oxydatif, chaleur, infection virale. |

---

### Couche 5 — TRADUCTIONNEL
*Contrôle de la synthèse protéique au niveau du ribosome.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **FORGE** | mTOR → initiation cap-dépendante | **mTORC1** phosphoryle 4E-BP1 → libère eIF4E → assemblage du complexe **eIF4F** (eIF4E-eIF4G-eIF4A). eIF4F recrute le 43S PIC → scanning 5'UTR → reconnaissance AUG (contexte Kozak optimal : GCCRCCAUGG). Régulation : insuline/nutriments → PI3K/AKT → mTORC1 actif ; AMPK → mTORC1 inhibé. eIF4A (DEAD-box hélicase) déroule les structures secondaires du 5'UTR pendant le scanning. |
| **BRAKE** | ISR / eIF2α-P | **Integrated Stress Response** : 4 kinases phosphorylent eIF2α Ser51 : **GCN2** (AA deprivation → uncharged tRNA) ; **PERK** (ER stress → UPR branch) ; **HRI** (hème deprivation) ; **PKR** (dsRNA viral). eIF2α-P séquestre eIF2B (GEF) → diminution du ternary complex (eIF2-GTP-Met-tRNA) → répression globale de la traduction cap-dépendante. **Paradoxe ATF4** : sous eIF2α-P, ATF4/GCN4 est sélectivement traduit via bypass des uORFs inhibiteurs (delayed reinitiation). |
| **DECOY** | uORFs (upstream ORFs) | ~50 % des ARNm eucaryotes contiennent ≥1 uORF dans leur 5'UTR. Effet général : les uORFs séquestrent les ribosomes → réduction de la traduction du mORF principal. **Mécanisme de réinitiation** : uORF court → ribosome conserve certains eIFs → réinitiation en aval (efficacité proportionnelle à la longueur de l'uORF et la distance inter-ORF). **Mécanisme ATF4 sous stress** : eIF2α-P → TC limitant → ribosomes bypassent les uORFs inhibiteurs distaux → induction sélective du mORF ATF4. Interaction avec IRES : uORFs et IRES coexistent sur certains ARNm et se régulent mutuellement ("zipper model"). |
| **BYPASS** | IRES (Internal Ribosome Entry Sites) | Éléments ARN capables de recruter le ribosome par une route moins dépendante de la coiffe. Mécanisme : IRES ± **ITAFs** (IRES trans-acting factors — PTB, DAP5/eIF4G2, hnRNPQ, Annexine A2) → positionnement du ribosome au voisinage de l'AUG. Les IRES viraux sont bien établis ; beaucoup d'IRES cellulaires restent plus controversés parce que les tests bicistroniques peuvent confondre cryptic promoters, splicing ou readthrough. Activés ou révélés quand la traduction cap-dépendante est bloquée (stress, ISR, infection virale). Exemples proposés/étudiés : **HIF-1α, VEGF-A, FGF2, p53 isoformes, c-MYC** ; ATF4 relève surtout de la réinitiation contrôlée par uORF plutôt que d'un IRES canonique. circRNA : traduction IRES-dépendante ou m6A-dépendante de certains circARN. |
| **TEMPO** | Codon usage + modifications tRNA + hétérogénéité ribosomale | **Codon usage bias** : codons synonymes traduits à des vitesses différentes selon l'abondance des tRNA cognats → influence le folding co-traductionnel et le stalling. **Modifications tRNA** (>100 types) : wobble modifications (mnm5U, mcm5s2U) → fidélité du décodage ; m1A, m3C → structure tRNA ; absence → frameshifting ou stalling. **Hétérogénéité ribosomale** : variation dans des protéines ribosomales (par exemple RPS25 pour certains IRES) ou modifications rRNA (pseudouridylation, 2'OMe par snoRNAs) peut biaiser la traduction de classes d'ARNm, mais le concept de "ribosomes spécialisés" reste expérimentalement difficile et doit être formulé comme une hypothèse contextuelle plutôt qu'un code général établi. Ribosomopathies : DBA (Diamond-Blackfan anemia), Treacher Collins. |
| **INSPECTOR** | Surveillance traductionnelle (RQC/NGD/NSD) | Mécanismes de surveillance qui détectent et dégradent les ARNm et polypeptides défectueux. **NGD** (No-Go Decay) : ribosome bloqué sur structure secondaire ou pseudoknot → endonucléase PELO + HBS1L → clivage ARNm. **NSD** (Non-Stop Decay) : ribosome atteint la fin de l'ARNm sans codon stop → Ski7 (levure) / PELO (mammifère) → dégradation. **RQC** (Ribosome-associated Quality Control) : ribosome coincé → **LTN1 E3 ligase** → ubiquitination polypeptide nascent → dégradation 26S. NEMF **CAT-tailing** : ajout d'alanine/thréonine sur le polypeptide bloqué → signal de dégradation. |

---

### Couche 6 — POST-TRADUCTIONNEL
*Modifications et dégradation des protéines après leur synthèse.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **SWITCH** | Phosphorylation / O-GlcNAcylation | **Phosphorylation** : ~500 kinases humaines phosphorylent Ser/Thr/Tyr → changements de conformation, création/destruction de sites d'interaction, activation/inactivation d'enzymes et TF (NF-κB, STAT1/3/5, SMAD, ERK→ELK1). ~30 % du protéome est phosphorylé. Réversible par ~200 phosphatases. **O-GlcNAcylation** : OGT ajoute GlcNAc sur Ser/Thr (mêmes sites que phospho) → "yin-yang" switch métabolique/signalisation. La phosphorylation active les kinases eIF2α (PERK, GCN2 → ISR), CDK9 (Pol II CTD Ser2), DDR kinases (ATM/ATR → PARP1). |
| **ROUTER** | Ubiquitin code | La **cascade E1-E2-E3** (~2 E1, ~40 E2, ~600 E3 ligases humaines) conjugue l'ubiquitine sur les Lys des substrats. La topologie des chaînes polyUb détermine le destin : **K48** (4+ Ub) → protéasome 26S ; **K63** → signalisation (NF-κB, DDR, endocytose) ; **K11** → dégradation mitotique ; **M1/linéaire** → NF-κB signalisation. Activation par dégron : souvent **phospho-dégron** (phospho → reconnaissance par E3 SCF-F-box ou APC/C). |
| **TETHER** | SUMOylation | Marque UBL surtout nucléaire. **SUMO1/2/3** sont conjuguées par SAE1/SAE2, **UBC9** et des E3 PIAS. Effets principaux : changer les interactions protéine-protéine, stabiliser des complexes nucléaires, recruter des co-répresseurs, moduler la réparation ADN et parfois protéger contre l'ubiquitination. Peut aussi créer un pont vers ROUTER via les **STUbL** (RNF4/RNF111), qui reconnaissent les chaînes polySUMO et déclenchent l'ubiquitination. Le nom TETHER insiste sur le rôle de recrutement/scaffold plutôt que sur la molécule SUMO elle-même. |
| **LICENSE** | Neddylation / activation des CRL | **NEDD8** est une UBL conjuguée surtout aux cullines. La neddylation active les **Cullin-RING ligases** (CRL), une grande famille d'E3 ubiquitin ligases, en favorisant le recrutement/positionnement des substrats et de l'E2. Ce n'est pas une voie de dégradation autonome : c'est un interrupteur en amont du système ROUTER qui augmente la capacité d'ubiquitination de substrats spécifiques. Le nom LICENSE reflète cette activation/licensing des CRL. |
| **DESTROY** | Destruction protéique : protéasome + autophagie sélective | Boîte fusionnée pour les deux grandes sorties de clearance protéique. **Protéasome 26S** : lit surtout K48-polyUb, déubiquitine, déplie et dégrade les protéines courtes ou endommagées. **Autophagie sélective** : récepteurs comme **p62/SQSTM1** relient les cargos ubiquitinés à **LC3/GABARAP** puis au lysosome, surtout pour agrégats, organites ou cargos volumineux. Les condensats polyUb peuvent concentrer ces cargos ; les acides aminés libérés par le lysosome réactivent mTORC1. |
| **MATURE** | Chaperones / UPR | **Chaperones** : Hsp70/Hsc70 (assistance co-traductionnelle) ; Hsp90 (maturation kinases, TF, récepteurs stéroïdiens) ; CCT/TRiC (folding en chambre isolée — actine, tubuline). Lien avec l'ubiquitination : **CHIP** (C-terminus of Hsp70-Interacting Protein) = E3 ubiquitin ligase qui ubiquitine les substrats mal foldés liés à Hsp70/Hsp90 → protéasome. **UPR** (Unfolded Protein Response, ER stress) : **PERK** (phosphoryle eIF2α = branche ISR), **IRE1** (épissage non-conventionnel de XBP1 mRNA), **ATF6** (TF activateur de gènes chaperonnage ER). |
| **PAR** | ADP-ribosylation / PARP / PAR | **PARP1** (Poly ADP-Ribose Polymérase 1) détecte les cassures ADN (DDR) et synthétise des chaînes de **PAR** (Poly-ADP-Ribose) sur lui-même et d'autres protéines (Asp, Glu, Lys). Activé et modulé par le contexte DDR, y compris ATM/ATR et d'autres PTM. PAR est une molécule multivalente → nucléation rapide de **condensats de phase** au niveau des dommages ADN → recrutement de facteurs comme FUS, XRCC1, RPA ou autres machines de réparation. Les chaînes PAR peuvent aussi recruter des facteurs ubiquitine/E3 et coupler réparation, remodelage et turnover local, mais le lien vers une "destruction" protéasomale générale est contexte-dépendant. Inhibiteurs PARP (olaparib) = thérapeutique cancer (synthetic lethality avec BRCA1/2). |

---

### Métaprincipes transversaux

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **LLPS** | Liquid-Liquid Phase Separation | Processus thermodynamique par lequel des macromolécules (protéines IDR-riches, ARN, protéines de liaison à l'ARN) se concentrent en une phase dense distincte ou dans un assemblage condensat-like. Conduit par des **interactions multivalentes** : domaines IDR (Intrinsically Disordered Regions), répétitions RGG, tyrosines, interactions ARN-protéine. LLPS n'est **pas un mécanisme de régulation unique** : c'est un principe physique exploité par plusieurs mécanismes, avec une preuve plus forte pour certains condensats (stress granules, PAR-damage foci) que pour d'autres. Instances biologiques : condensats transcriptionnels enrichis en BRD4/Mediator/Pol II CTD, stress granules (G3BP1 + TIA-1 + ARNm), P-bodies (DCP1/2 + XRN1), condensats protéolytiques/polyUb dans certains contextes, condensats de réparation ADN (PAR + FUS + RPA). |
| **DECAY** | Turnover / clearance | Métaprincipe de retrait d'une molécule du système : dégradation d'ARNm (TIMER, CENSOR), destruction protéique protéasomale ou lysosomale (DESTROY), et plus généralement bascule entre stockage temporaire et élimination. DECAY n'est pas un seul complexe moléculaire ; c'est une sortie fonctionnelle récurrente. |

---

## II. Catalogue des relations (73 arêtes mécanistiques + 7 annotations méta)

### Code couleur
| Couleur | Type | Signification |
|---------|------|---------------|
| 🟢 Vert `#27ae60` | Activation directe | A recrute/active/dépose B |
| 🔴 Rouge `#c0392b` | Répression directe | A bloque/empêche B (arrowhead=tee) |
| 🟡 Jaune `#f4d03f` | Couplage à Pol II | Mécanisme lié à la progression de Pol II |
| 🟠 Orange `#e67e22` | Couplage co-transcriptionnel | Régulation couplée à la transcription |
| 🟣 Violet `#8e44ad` | Mécanisme post-transcriptionnel / m6A / RBP | Régulation post-transcriptionnelle |
| ⚫ Gris `#566573` | PTM / signalisation post-trad | Régulation post-traductionnelle |
| 🔵 Bleu `#2e86c1` | Structural / 3D | Organisation tridimensionnelle |
| 🔵 Cyan `#22d3ee` (bordure pointillée) | LLPS | Participation au principe LLPS / condensats |
| 🩷 Rose `#f472b6` (bordure tiretée) | DECAY | Participation au principe turnover / clearance |

### Toutes les relations par couche source

#### 3D → 3D
| Source | Cible | Nom de la relation | Mécanisme |
|--------|-------|--------------------|-----------|
| ZONES | FENCES | **CONTAINS** | Les compartiments A/B contraignent la formation des TADs à l'intérieur |
| ZONES | WRITER-R | **ANCHORS-B** | Le compartiment B est ancré à la lamina et co-localise avec H3K9/27me3 |
| FENCES | BRIDGES | **DELIMITS** | Les frontières TAD insulent les boucles E-P à l'intérieur du même domaine |
| BRIDGES | HUBS | **ANCHORS-SE** | Les boucles E-P ancrent les super-enhancers à leurs promoteurs cibles |

#### 3D → Épigénétique
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| OPENER | HUBS | **H3K27AC-BRD4** | BRD4 lit H3K27ac via son bromodomaine → assemblage/maintien des hubs enhancer |
| HUBS | OPENER | **SE-ACETYLATION** | Les super-enhancers maintiennent un état local fortement acétylé |

#### Épigénétique → Épigénétique
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SILENCER | WRITER-R | **CO-RECRUIT** (bidirectionnel) | MBD → recrute SUV39H1 → H3K9me3 ; et inversement HP1 → recrute DNMT3 |
| OPENER | SHUFFLER | **ACETYL-REMODEL** | Les marques acétylées, via des readers bromodomaines, favorisent le recrutement de remodelers comme SWI/SNF/BAF |
| GUIDES | SILENCER | **PIRNAGUIDE** | piRNA-PIWI guident DNMT3L/3A vers les transposons → méthylation *de novo* |

#### Épigénétique → Transcription
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| OPENER | KEYS | **OPENS-TF** | L'acétylation des histones relâche les nucléosomes → accès des TF |
| WRITER-R | KEYS | **SILENCES-TF** ⊣ | H3K27me3/H3K9me3 → chromatine compacte → exclusion des TF |
| SHUFFLER | KEYS | **REMODELS** | Les CRC repositionnent/éjectent des nucléosomes → fenêtre de liaison TF |
| WRITER-A | SCRIBE | **RECRUITS-POL2** | H3K4me3 recrute TAF3 (TFIID) → Pol II recruitment |
| HUBS | SCRIBE | **RELEASES-PAUSE** | P-TEFb concentrée dans les SE → phosphoryle Ser2-CTD → libération Pol II |
| OPENER | ZONES | **ACETYL-TO-A** | H3K27ac et chromatine active favorisent l'appartenance au compartiment A |
| WRITER-R | ZONES | **REPRESS-TO-B** | H3K27me3/H3K9me3 et hétérochromatine favorisent l'appartenance au compartiment B |
| SILENCER | ZONES | **METH-TO-B** | Méthylation CpG → recrutement MBD → compaction → compartiment B |

#### Transcription → Épigénétique (feedbacks)
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| KEYS | OPENER | **TF-HAT** | TF activateurs recrutent p300/CBP → dépôt H3K27ac sur les enhancers cibles |
| KEYS | WRITER-A | **TF-KMT** | TF recrutent MLL1-4/KMT2 → dépôt H3K4me3 aux promoteurs actifs |
| KEYS | SHUFFLER | **TF-CRC** (back) | TF recrutent SWI/SNF → remodeling sur leurs gènes cibles |
| KEYS | GUIDES | **TF-NCRNA-EPI** | Les TF peuvent activer des loci piRNA/lncRNA qui guident ensuite des complexes chromatiniennes |
| KEYS | SPONGE | **TF-LNCRNA** | Les TF activent des loci lncRNA cytoplasmiques, ajoutant une sortie post-transcriptionnelle au programme transcriptionnel |

#### Transcription → Transcription
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| KEYS | SCRIBE | **INITIATES** | TF recrutent Mediator → assemblage du PIC → recrutement Pol II |
| KEYS | HUBS | **DEFINES-SE** | Les TF maîtres (OCT4, MYC, SOX2) définissent et maintiennent les SE |
| KEYS | RECODER | **IFN-ADAR** | IRF3/7 (TF de réponse IFN) transcrivent ADAR1p150 |

#### Transcription → Co-transcriptionnel
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SCRIBE | SHIELD | **CTD-CAP** | Ser5-P CTD recrute la guanylyltransférase → capping co-transcriptionnel |
| SCRIBE | SPLICER | **RATE-SPLICE** (**) | Vitesse d'élongation de Pol II = fenêtre d'opportunité pour l'inclusion des exons faibles |
| SCRIBE | TRIMMER | **CTD-CST** | Pol II Ser2-P recrute CstF → clivage et polyadénylation |
| SCRIBE | STAMP | **CTD-M6A** | METTL3/14 est recruté par la CTD co-transcriptionnellement → m6A |
| SCRIBE | ZONES | **TXN-TO-A** | L'activité transcriptionnelle contribue à maintenir les régions actives dans le compartiment A |
| WRITER-A | SPLICER | **HISTONE-SPLICE** (**) | H3K36me3 (déposé par SETD2 associé à Pol II) recrute MRG15 → PTB → exon inclusion |
| SCRIBE | WRITER-A | **SETD2-COUPLING** (**) | SETD2 est lié physiquement à Pol II Ser2-P → H3K36me3 déposé pendant l'élongation |

(**) = couplages cinétiques clés, principe C de la métaarchitecture

#### Post-transcriptionnel → Co-transcriptionnel (feedbacks)
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| STAMP | SPLICER | **M6A-SPLICE** (back) | YTHDC1 lie m6A nucléaire → recrute SRSF3 (inclusion) / SRSF10 (skipping) |
| READERS | SPLICER | **RBP-SPLICE** (back) | SR proteins (SRSF1-12) et hnRNPs régulent les ESEs/ESSs du spliceosome |
| RECODER | SPLICER | **ADAR-SPLICE** (bidirectionnel) | ADAR1/2 édite les 5'SS → modifie la reconnaissance par U1 snRNA |

#### Co-transcriptionnel → Post-transcriptionnel
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SPLICER | CENSOR | **SPLICE-NMD** | Les exons alternatifs introduisant des PTCs → NMD de l'isoforme |
| TRIMMER | DARTS | **APA-MIRNA** | 3'UTR long → exposition de sites miRNA supplémentaires |
| TRIMMER | READERS | **APA-RBP** | 3'UTR long → exposition de sites RBP supplémentaires |
| RECODER | CENSOR | **ADAR-NMD** | Exonisation Alu (PTC) → NMD ; ADAR1 édite le 5'SS → prévient l'exonisation |

#### Post-transcriptionnel intra
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| STAMP | TIMER | **M6A-DECAY** | Les YTHDF cytoplasmiques, avec un rôle classique de YTHDF2, recrutent ou favorisent CCR4-NOT/P-bodies → déadénylation accélérée → decay |
| STAMP | CLIPS | **M6A-G4** | m6A déstabilise la structure secondaire → déstabilisation des G-quadruplexes adjacents |
| DARTS | TIMER | **MIRNA-DECAY** | AGO2-RISC recrute CCR4-NOT → déadénylation + décapping |
| SPONGE | DARTS | **CERNA** ⊣ | lncRNA/circRNA ceRNA peut séquestrer des miRNA → décompression des ARNm cibles si la stoechiométrie et la colocalisation sont suffisantes |
| CENSOR | TIMER | **NMD-DECAY** | UPF1-P recrute SMG6 (endonucléase) + SMG5/7 → dégradation rapide |
| TIMER | VAULT | **MRNA-SG** (bidirectionnel) | ARNm non traduits → stress granules ; SG dissolus → ARNm libérés |
| READERS | TIMER | **RBP-STABILITY** | HuR/ELAVL1 (stabilise AREs) vs TTP/ZFP36 (déstabilise AREs → CCR4-NOT) |
| CLIPS | BYPASS | **G4-IRES** | rG4 dans 5'UTR peut moduler l'accessibilité de l'IRES (zipper model) |

#### Post-transcriptionnel → Traductionnel
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| STAMP | FORGE | **M6A-INIT** | m6A peut stimuler l'initiation via YTHDF1/eIF3 ou des mécanismes 5'UTR dépendants du contexte |
| STAMP | BYPASS | **M6A-IRES** | m6A dans le 5'UTR → traduction cap-indépendante (sous stress) |
| READERS | FORGE | **FMRP-REPRESS** ⊣ | FMRP lie les polysomes et bloque l'élongation |
| DARTS | FORGE | **MIRNA-TRANSL** ⊣ | RISC bloque la jonction 80S ou la réinitiation → inhibition traductionnelle |
| CLIPS | FORGE | **G4-BLOCK** ⊣ | rG4 en 5'UTR bloque la progression du ribosome 43S scanning |

#### Capping → Traduction
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SHIELD | FORGE | **CAP-EIF4E** | La coiffe m7G est reconnue par eIF4E → assemblage eIF4F → initiation |

#### Traductionnel intra
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| BRAKE | DECOY | **ISR-UORF** (**) | eIF2α-P → TC limitant → ribosomes bypassent les uORFs distaux → ATF4 |
| BRAKE | BYPASS | **ISR-IRES** | Cap-dep bloqué → favorise des routes alternatives ; ATF4 passe surtout par uORF/réinitiation, tandis que HIF-1α/c-Myc sont des exemples proposés de contrôle de type IRES |
| DECOY | FORGE | **UORF-COMPETE** ⊣ | uORFs séquestrent les ribosomes → réduction traduction mORF principal |
| FORGE | INSPECTOR | **STALL-RQC** | Traduction active → stalling sur codons rares ou structures → RQC/NGD |
| TEMPO | INSPECTOR | **CODON-STALL** | Codons rares → pause ribosomale prolongée → NGD/NSD/RQC |
| TEMPO | MATURE | **COTRANSL-FOLD** | Rythme de traduction (codon usage) → cinétique de repliement co-traductionnel |
| INSPECTOR | DESTROY | **RQC-26S** | CAT-tailing du polypeptide nascent bloqué → reconnaissance LTN1 → dégradation |

#### Traduction → Post-traductionnel
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| FORGE | MATURE | **COTRANSL-MATURATION** | La traduction naissante expose les chaînes aux chaperones co-traductionnelles et lance le repliement |
| FORGE | SWITCH | **MTOR-KINASES** | mTORC1 et les voies de croissance couplent l'initiation traductionnelle à AKT/S6K et à d'autres cascades kinases |

#### Post-traductionnel intra
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SWITCH | ROUTER | **SWITCH-DEGRON** | Phospho-dégron reconnu par E3 SCF (β-TrCP, Fbxw7) ou APC/C |
| SWITCH | TETHER | **PDSM** | Motif PDSM (ψKxExxSP) → phospho de la Ser → activation SUMOylation de la Lys |
| ROUTER | DESTROY | **ROUTER-DESTROY** | K48-polyUb → protéasome 26S ; K63-polyUb peut recruter p62/SQSTM1 → autophagie sélective |
| TETHER | ROUTER | **STUBLS** | polySUMO → reconnu par RNF4/RNF111 (STUbL E3) → ubiquitination → protéasome |
| LICENSE | ROUTER | **CRL-ACTIVATION** | Neddylation des cullines → activation des CRL E3 ligases → ubiquitination de substrats spécifiques |
| PAR | DESTROY | **PAR-CONDENSATE** | PAR longues chaînes → condensats DDR et recrutement contextuel de facteurs ubiquitine/protéostase → turnover local possible |
| MATURE | BRAKE | **UPR-ISR** | PERK (branche UPR) = kinase eIF2α → ISR = pont ER stress–ISR |
| DESTROY | FORGE | **LYSOSOME-MTOR** | Acides aminés libérés par la voie lysosomale → Ragulator/RRAG GTPases surface lysosomale → mTORC1 réactivé |
| DESTROY | KEYS | **DESTROY-TF** | Dégradation des inhibiteurs de TF (IκBα→NF-κB ; β-catenin→TCF/LEF) |

#### Post-traductionnel → Transcription / Pol II
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| SWITCH | SCRIBE | **CDK9-CTD** | CDK9/P-TEFb (phosphorylé et activé) → Ser2-CTD → libération de la pause Pol II |
| SWITCH | BRAKE | **KINASE-EIF2A** | GCN2, PERK, HRI, PKR phosphorylent eIF2α Ser51 → BRAKE activé |

#### Métaprincipes transversaux
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| LLPS | HUBS | **LLPS-SE** | LLPS/condensats transcriptionnels peuvent contribuer à l'activité des super-enhancers, sans identité stricte entre les deux concepts |
| LLPS | VAULT | **LLPS-SG-PB** | LLPS forme les stress granules et P-bodies |
| LLPS | DESTROY | **LLPS-DESTROY** | LLPS forme les condensats protéolytiques (hHR23B + polyUb) |
| LLPS | PAR | **LLPS-PAR** | Les chaînes PAR nucléent des condensats de réparation ADN |
| DECAY | TIMER | **DECAY-MRNA** | Turnover des ARNm par déadénylation, décapping et exonucléases |
| DECAY | CENSOR | **DECAY-NMD** | NMD comme branche de surveillance et élimination des ARNm aberrants |
| DECAY | DESTROY | **DECAY-DESTROY** | Dégradation protéique ubiquitine-dépendante ou clearance lysosomale sélective de protéines, agrégats ou organites |

---

## III. Overlaps et fusions — Ce qui a été consolidé

| Entités fusionnées | Justification |
|--------------------|---------------|
| Super-enhancers + Condensats de transcription | Concepts très liés mais non identiques : super-enhancer = définition génomique/ChIP-seq ; condensat = assemblage physique dynamique souvent enrichi en coactivateurs |
| Compartiments A/B + État épigénétique global | Corrélation forte ; les compartiments *émergent* des marques mais ne sont pas identiques |
| YTHDF1 + YTHDF2 + YTHDF3 → **STAMP** | Un seul signal (m6A), lecteurs partiellement spécialisés mais aussi redondants selon contexte cellulaire |
| Codon usage + tRNA modifications + Ribosome hétérogénéité → **TEMPO** | Trois facettes du même principe "efficacité de décodage" |
| SWI/SNF + ISWI + CHD + INO80 → **SHUFFLER** | Même principe ATP-dependent, 4 sous-familles |
| eRNAs (enhancer RNAs) | Sous-produits de l'activité enhancer = readout, pas mécanisme propre |
| ISR branch PERK / UPR | PERK est à la fois une kinase ISR et la branche PERK de l'UPR : intégré via MATURE → BRAKE |
| siRNA / miRNA | Partagent RISC/AGO2 ; siRNA chez les animaux = variante outil expérimental surtout → fusionné dans DARTS |
| ceRNA hypothesis | Cas particulier de SPONGE + DARTS, à garder comme mécanisme conditionnel dépendant de la stoechiométrie miRNA/sites cibles |

---

## Annexe A — Bases de données et ressources

| Ressource | URL | Contenu |
|-----------|-----|---------|
| ENCODE | https://encodeproject.org | ChIP-seq, ATAC-seq, CTCF, histone marks, 150+ cell types |
| Roadmap Epigenomics | https://egg2.wustl.edu/roadmap | 127 types cellulaires, méthylation + histones |
| GTEx | https://gtexportal.org | eQTLs tissue-spécifiques |
| FANTOM5 | https://fantom.gsc.riken.jp/5 | TSS atlas, eRNAs, lncRNAs |
| miRBase | https://mirbase.org | Catalogue miRNA |
| POSTAR3 | http://postar.ncrnalab.org | Sites de liaison RBPs (CLIP-seq) |
| RMBase v3 | https://rmbase.sysu.edu.cn | Sites de modifications ARN (m6A, m5C, Ψ...) |
| G4 motif resources | À vérifier | G-quadruplexes dans les transcriptomes |
| PhosphoSitePlus | https://phosphosite.org | Sites PTM (phospho, ubiq, acétyl, méthyl) |
| STRING | https://string-db.org | Interactions protéine-protéine |
| UniProt | https://uniprot.org | Annotations protéines + PTMs |

## Annexe B — Références fondamentales

- Kouzarides T. (2007). Chromatin modifications and their function. *Cell* 128(4):693-705.
- Wang X. & He C. (2014). Dynamic RNA modifications in posttranscriptional regulation. *Mol Cell* 56(1):5-12.
- Core L. & Adelman K. (2019). Promoter-proximal pausing of RNA polymerase II. *Nat Rev Genet* 20:700-714.
- Naftelberg S. et al. (2015). Regulation of alternative splicing through coupling with transcription and chromatin structure. *Annu Rev Biochem* 84:165-198.
- Dever TE et al. (2023). Translational control by uORFs. *Genes Dev* 37(11-12):474-489.
- Rhine K. et al. (2023). Regulation of biomolecular condensates by poly(ADP-ribose). *Chem Rev* 123:9065.
- Bhatt DL et al. (2020). Integrated Stress Response in gene regulation. *Nat Rev Mol Cell Biol*.
- Noda Y. et al. (2022). Regulation of A-to-I RNA editing and stop codon recoding. *Nat Commun* 13:2503.
- Robson et al. (2019). Regulatory functions of chromatin topology. *Nat Rev Genet* 20:489-499.
- Yau R. & Bhatt DL (2020). Ubiquitin-modulated phase separation of shuttle proteins. *J Mol Biol*.

---

*v7 — 37 mécanismes, 2 métaprincipes, 73 relations mécanistiques + 7 annotations méta*
*Fichier : `assets/documents/gene-regulation-landscape-details.md`*
*Diagramme : `assets/documents/gene-reg-v7.dot` + `assets/images/gene-reg-v7.png`*
