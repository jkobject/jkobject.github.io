# Gene Regulation Landscape — detailed construction notes
### From DNA to proteins — reductionist architecture (v7)

*Clawd · 2026-05-01 / updated 2026-06-18 · 37 mechanisms · 2 meta-principles · 7 layers*

These are the original detailed working notes used to construct the Gene
Regulation Landscape. They contain the full mechanism catalogue, edge list, and
reduction principles. The rendered figure was generated from the Graphviz source
file [`gene-reg-v7.dot`](/assets/documents/gene-reg-v7.dot). The current rendered
v7 graph contains 37 mechanism boxes, 2 starred meta-principles, 72 mechanism
relations, and 8 meta-overlay links.

The notes below are preserved in French because they were the original working
document.

---

# Cartographie des mécanismes de régulation génétique
### De l'ADN aux protéines — Architecture réductionniste (v7)

*Clawd · 2026-05-01 / mis à jour 2026-06-18 · 37 mécanismes · 2 métaprincipes · 7 couches*

---

## Résumé exécutif

La cellule régule l'expression de ses gènes à **7 niveaux emboîtés**, de l'organisation tridimensionnelle du génome à la dégradation sélective des protéines. On dénombre 37 mécanismes distincts dans les boîtes du graphe, plus 2 métaprincipes transversaux marqués par des étoiles (**LLPS** et **DECAY**). Une analyse transversale révèle aussi **3 stratégies** récurrentes : (A) contrôle de l'accessibilité physique d'un substrat, (B) écriture/lecture/effacement d'une marque réversible, (C) couplage cinétique entre deux processus. Tout le reste est une implémentation moléculaire de l'un de ces trois principes à un niveau différent.

---

## I. Les 7 couches — Explication et mécanismes

### Couche 0 — GÉNOME 3D
*Le génome n'est pas linéaire mais tridimensionnel. L'organisation spatiale détermine quels enhancers peuvent parler à quels promoteurs.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **ZONES** | Compartiments A/B | Grandes régions chromatiniennes (~5–20 Mb) détectées par Hi-C. Compartiment **A** = euchromatine transcriptionnellement active (H3K27ac, H3K4me3). Compartiment **B** = hétérochromatine inactive (H3K27me3, H3K9me3, méthylation ADN, lamina nucléaire). La transition A↔B accompagne la différenciation cellulaire. |
| **FENCES** | TADs (Topologically Associating Domains) | Domaines d'interactions préférentielles de ~0.1–2 Mb délimités par des frontières CTCF convergentes. Mécanisme : Cohesin extrude activement des boucles jusqu'à blocage par paires CTCF convergentes → insulation des interactions inter-domaine. Empêche les fusions enhancer-promoteur aberrantes. |
| **BRIDGES** | Boucles Enhancer→Promoteur | Contacts physiques spécifiques entre un enhancer distal et son promoteur cible à l'intérieur d'un TAD. Médiés par Mediator (pont TF-Pol II), Cohesin (stabilisation), YY1, ZNF143. Peuvent dépasser 1 Mb de distance linéaire. |
| **HUBS** | Super-enhancers / Condensats Pol II | Clusters d'enhancers ordinaires couvrant 5–50 kb, très denses en TF maîtres, BRD4, Mediator, Pol II. Correspondent physiquement à des **condensats de phase liquide** (LLPS). Très sensibles à JQ1 (inhibiteur BET). Pilotent les gènes d'identité cellulaire et les oncogènes. |

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
| **KEYS** | Facteurs de transcription (TF) | Protéines à domaines de liaison à l'ADN (séquence-spécifiques) et domaines d'activation/répression. **Activateurs** : recrutent HATs (p300/CBP → H3K27ac), KMTs (MLL → H3K4me3), CRC (SWI/SNF), Mediator → Pol II. **Répresseurs** : recrutent HDACs, PRC, NuRD. **Pioneer factors** (FOXA1, OCT4, GATA3) : peuvent ouvrir la chromatine compacte. ~1600 TF humains. Les TF maîtres (OCT4, SOX2, MYC) définissent les super-enhancers. Feedback : les protéines synthétisées via IRES (ATF4, HIF-1α) sont elles-mêmes des TF. Le protéasome active des TF en dégradant leurs inhibiteurs (IκBα → NF-κB). |
| **SCRIBE** | Pol II + pausing | ARN polymérase II : enzyme ~550 kDa, 12 sous-unités. La queue CTD (répétition YSPTSPS ×52) est un hub de signalisation : **Ser5-P** (CDK7/TFIIH) = initiation/capping ; **Ser2-P** (CDK9/P-TEFb) = élongation ; **Ser7-P** = ARN non-codants. **Pausing proximal** : Pol II stalled 25–50 bp après le TSS par NELF + DSIF. Libération par P-TEFb (recrutée par BRD4 des super-enhancers). ~30–50 % des gènes mammifères sont pausés — permet une réponse rapide et un contrôle précis. **Couplage** : SETD2 (H3K36me3 writer) est lié à la Pol II Ser2-P → H3K36me3 est déposé pendant l'élongation. METTL3/14 est recruté par la CTD → m6A co-transcriptionnel. |

---

### Couche 3 — CO-TRANSCRIPTIONNEL
*Traitements de l'ARN nascent couplés à la progression de Pol II.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **SHIELD** | 5' Capping | Ajout d'une 7-méthylguanosine (m7G) sur le 5' de l'ARN nascent dès ~25-30 nt, co-transcriptionnellement via la Ser5-P CTD. Protection contre les 5'→3' exonucléases. La coiffe est reconnue par eIF4E (initiation traductionnelle) et par CBC (nuclear cap-binding complex → export). Échange CBC → eIF4E lors de l'export nucléaire. |
| **SPLICER** | Splicing alternatif | Excision des introns et jonction des exons par le **spliceosome** (U1/U2/U4/U6/U5 snRNPs + ~150 protéines). ~95 % des gènes multi-exoniques humains produisent plusieurs isoformes. Modes : exon skipping, intron retention, 5'/3' alternative SS, exons mutuellement exclusifs. **Régulation cinétique** : la vitesse d'élongation de Pol II contrôle l'inclusion des exons ("window of opportunity" — Pol II lente → temps pour reconnaître exons faibles). **Code épigénétique** : H3K36me3 recrute MRG15 → PTB/PSF → exon inclusion ; H3K9me3 → Pol II lente → exon skipping. |
| **TRIMMER** | Polyadénylation alternative (APA) | ~70 % des gènes mammifères ont plusieurs sites de clivage/polyadénylation → isoformes avec 3'UTR de longueurs différentes. Mécanism : complexe CPA (CPSF, CstF, CFI/II) reconnaît la séquence AAUAAA ~20 nt en amont du site polyA. Conséquence : 3'UTR long → plus de sites miRNA et de sites RBP exposés → régulation post-transcriptionnelle plus intense. |
| **RECODER** | A→I Editing (ADAR) | Les **ADARs** (Adenosine Deaminases Acting on RNA) hydrolysent les adénosines en inosines dans des dsRNA. L'inosine est lu comme guanosine → recoding de l'information génétique. **ADAR1 p150** : induit par l'interféron (IRF3/7), cytoplasmique, marque les dsRNA endogènes Alu comme "self". **ADAR2** : constitutif, nucléaire, spécialiste du recoding neuronal (GluR-B Q→R site). Couplage avec le splicing : A→I editing au 5'SS d'éléments Alu → prévention de l'exonisation → prévention du NMD. |

---

### Couche 4 — POST-TRANSCRIPTIONNEL
*Régulation des ARNm matures dans le noyau et le cytoplasme.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **STAMP** | m6A épitranscriptome | **N6-méthyladénosine (m6A)** : modification chimique la plus abondante des ARNm eucaryotes (~3–5 sites par ARNm). **Writers** : complexe METTL3/14/WTAP ; déposé co-transcriptionnellement. **Erasers** : FTO, ALKBH5. **Readers directs** : YTHDF1 (→ recrutement eIF3 → initiation ↑) ; YTHDF2 (→ CCR4-NOT déadénylation → decay ↑) ; YTHDF3 (→ traduction ↑) ; YTHDC1 (nucléaire → SRSF3/SRSF10 → splicing). **Readers indirects** : HNRNPC/HNRNPA2B1 (m6A switch structural → accessibilité). m6A agit simultanément sur splicing, export, stabilité et traduction → mécanisme transversal, pas un seul mécanisme. |
| **READERS** | RBPs régulateurs | ~1500 protéines de liaison à l'ARN (RNA-Binding Proteins) humaines. Modules de liaison : RRM, KH, CCCH zinc finger, PAZ, DEAD-box. Régulent toutes les étapes : splicing (SR proteins comme SRSF1-12 = activateurs ; hnRNPs comme PTBP1 = répresseurs) ; stabilité (HuR/ELAVL1 stabilise via ARES ; TTP/ZFP36 déstabilise via ARES → CCR4-NOT) ; traduction (FMRP réprime initiation) ; localisation (Staufen1 → SMD) ; IRES (ITAFs : PTB, DAP5/eIF4G2, hnRNPQ activent IRES). Mutations dans les RBPs → nombreuses maladies (ALS, SMA, syndrome X fragile). |
| **DARTS** | miRNA-RISC | MicroARNs de ~22 nt. Biogenèse : pri-miRNA (Pol II) → **Drosha**/DGCR8 → pre-miRNA (~70 nt hairpin) → export Exportine-5 → **Dicer**/TRBP → miRNA duplex → chargement dans **AGO2** → RISC actif. Mécanisme : appariement imparfait (seed 7 nt, positions 2–8) du miRNA avec le 3'UTR → recrutement CCR4-NOT/TNRC6 → déadénylation + décapping + inhibition traductionnelle. ~2500 miRNA humains, chacun régule ~200–1000 ARNm. |
| **SPONGE** | lncRNA cytoplasmiques | lncRNAs (>200 nt) à localisation cytoplasmique. **ceRNA / éponge à miRNA** : circRNA CDR1as (>70 sites miR-7), HULC, HOTAIR cytoplasm. → séquestrent des miRNAs → décompression des ARNm cibles. **Activation traductionnelle** : UCHL1-AS (domaine SINEB2) → recrutement de polyribosomes. **Répression traductionnelle** : lincRNA-p21 → recrutement de Rck (hélicase répresseur). **Décoy** : GAS5 (glucocorticoid decoy) imite les GRE → séquestre GR. |
| **CENSOR** | NMD (Nonsense-Mediated mRNA Decay) | Surveillance des ARNm aberrants portant des codons stop prématurés (PTCs). Mécanisme : lors de la traduction, si un ribosome termine à >50–55 nt en amont d'un **EJC** (Exon Junction Complex) → recrutement de UPF1/UPF2/UPF3 → phosphorylation UPF1 par SMG1 → dégradation rapide (décapping + exonucléases). ~5–10 % du transcriptome humain est régulé physiologiquement par NMD (splicing productif vs improductif alternatif). Lien editing : A→I editing au 5'SS d'un exon Alu → prévention exonisation → pas de PTC → pas de NMD (circuit ADAR-SPLICER-CENSOR). |
| **TIMER** | Stabilité / dégradation des ARNm | La demi-vie des ARNm varie de ~20 min (proto-oncogènes) à >24 h (globine). Voie principale : **déadénylation** (CCR4-NOT/PAN2-PAN3 → queue polyA) → **décapping** (DCP1/2 → suppression m7G) → **dégradation 5'→3'** (XRN1). Voie alternative : **exosome** (dégradation 3'→5', complexe ~14 sous-unités). Régulateurs : ARE-binding proteins (HuR stabilise ; TTP déstabilise), miRNAs (→ CCR4-NOT), m6A (YTHDF2 → CCR4-NOT). |
| **CLIPS** | RNA G-quadruplexes (rG4) | Structures secondaires quaternaires formées de tétrades de guanines (G4) stabilisées par des ions K+. Présents dans les 5'UTR (→ bloquent la progression du ribosome 43S → inhibition traduction cap-dépendante), 3'UTR, régions de pause Pol II, télomères. Déroulés par des helicases : DHX36, eIF4A, RHAU. Régulation : m6A peut déstabiliser les rG4 en modifiant la structure secondaire de l'ARN. Interaction avec IRES : rG4 dans 5'UTR peut moduler l'accessibilité des IRES. |
| **VAULT** | Stress granules / P-bodies | Deux types de **condensats cytoplasmiques** (LLPS) de stockage/dégradation des ARNm. **Stress granules** (G3BP1, TIA-1, PABPC) : stockage temporaire des ARNm sous stress → dissolution lors de la résolution → libération vers la traduction. **P-bodies** (DCP1/2, XRN1, CNOT) : sites de décapping et dégradation. Échange dynamique de matière entre SG et PB. Formation déclenchée par : ISR (eIF2α-P), stress oxidatif, chaleur, infection virale. |

---

### Couche 5 — TRADUCTIONNEL
*Contrôle de la synthèse protéique au niveau du ribosome.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **FORGE** | mTOR → initiation cap-dépendante | **mTORC1** phosphoryle 4E-BP1 → libère eIF4E → assemblage du complexe **eIF4F** (eIF4E-eIF4G-eIF4A). eIF4F recrute le 43S PIC → scanning 5'UTR → reconnaissance AUG (contexte Kozak optimal : GCCRCCAUGG). Régulation : insuline/nutriments → PI3K/AKT → mTORC1 actif ; AMPK → mTORC1 inhibé. eIF4A (DEAD-box hélicase) déroule les structures secondaires du 5'UTR pendant le scanning. |
| **BRAKE** | ISR / eIF2α-P | **Integrated Stress Response** : 4 kinases phosphorylent eIF2α Ser51 : **GCN2** (AA deprivation → uncharged tRNA) ; **PERK** (ER stress → UPR branch) ; **HRI** (hème deprivation) ; **PKR** (dsRNA viral). eIF2α-P séquestre eIF2B (GEF) → diminution du ternary complex (eIF2-GTP-Met-tRNA) → répression globale de la traduction cap-dépendante. **Paradoxe ATF4** : sous eIF2α-P, ATF4/GCN4 est sélectivement traduit via bypass des uORFs inhibiteurs (delayed reinitiation). |
| **DECOY** | uORFs (upstream ORFs) | ~50 % des ARNm eucaryotes contiennent ≥1 uORF dans leur 5'UTR. Effet général : les uORFs séquestrent les ribosomes → réduction de la traduction du mORF principal. **Mécanisme de réinitiation** : uORF court → ribosome conserve certains eIFs → réinitiation en aval (efficacité proportionnelle à la longueur de l'uORF et la distance inter-ORF). **Mécanisme ATF4 sous stress** : eIF2α-P → TC limitant → ribosomes bypassent les uORFs inhibiteurs distaux → induction sélective du mORF ATF4. Interaction avec IRES : uORFs et IRES coexistent sur certains ARNm et se régulent mutuellement ("zipper model"). |
| **BYPASS** | IRES (Internal Ribosome Entry Sites) | Structures secondaires dans le 5'UTR qui recrutent directement le 40S ribosomal sans coiffe ni scanning. Mécanisme : IRES ± **ITAFs** (IRES trans-acting factors — PTB, DAP5/eIF4G2, hnRNPQ, Annexine A2) → positionnement du ribosome au voisinage de l'AUG. Activés quand la traduction cap-dépendante est bloquée (stress, ISR, infection virale). Exemples physiologiques : **ATF4, HIF-1α, VEGF-A, FGF2, p53 isoformes**. circRNA : traduction IRES-dépendante (ou m6A-dépendante) de circARN. |
| **TEMPO** | Codon usage + modifications tRNA + ribosomes spécialisés | **Codon usage bias** : codons synonymes traduits à des vitesses différentes selon l'abondance des tRNA cognats → influence le folding co-traductionnel et le stalling. **Modifications tRNA** (>100 types) : wobble modifications (mnm5U, mcm5s2U) → fidélité du décodage ; m1A, m3C → structure tRNA ; absence → frameshifting ou stalling. **Ribosomes spécialisés** : variation dans les protéines ribosomales (RPL10A vs RPL10 ; RPS25 pour certains IRES) ou modifications rRNA (pseudouridylation, 2'OMe par snoRNAs) → sélection préférentielle de certains ARNm. Ribosomopathies : DBA (Diamond-Blackfan anemia), Treacher Collins. |
| **INSPECTOR** | Surveillance traductionnelle (RQC/NGD/NSD) | Mécanismes de surveillance qui détectent et dégradent les ARNm et polypeptides défectueux. **NGD** (No-Go Decay) : ribosome bloqué sur structure secondaire ou pseudoknot → endonucléase PELO + HBS1L → clivage ARNm. **NSD** (Non-Stop Decay) : ribosome atteint la fin de l'ARNm sans codon stop → Ski7 (levure) / PELO (mammifère) → dégradation. **RQC** (Ribosome-associated Quality Control) : ribosome coincé → **LTN1 E3 ligase** → ubiquitination polypeptide nascent → dégradation 26S. NEMF **CAT-tailing** : ajout d'alanine/thréonine sur le polypeptide bloqué → signal de dégradation. |

---

### Couche 6 — POST-TRADUCTIONNEL
*Modifications et dégradation des protéines après leur synthèse.*

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **PHOSPHO** | Phosphorylation / O-GlcNAcylation | **Phosphorylation** : ~500 kinases humaines phosphorylent Ser/Thr/Tyr → changements de conformation, création/destruction de sites d'interaction, activation/inactivation d'enzymes et TF (NF-κB, STAT1/3/5, SMAD, ERK→ELK1). ~30 % du protéome est phosphorylé. Réversible par ~200 phosphatases. **O-GlcNAcylation** : OGT ajoute GlcNAc sur Ser/Thr (mêmes sites que phospho) → "yin-yang" switch métabolique/signalisation. La phosphorylation active les kinases eIF2α (PERK, GCN2 → ISR), CDK9 (Pol II CTD Ser2), DDR kinases (ATM/ATR → PARP1). |
| **UBI** | Ubiquitin code | La **cascade E1-E2-E3** (~2 E1, ~40 E2, ~600 E3 ligases humaines) conjugue l'ubiquitine sur les Lys des substrats. La topologie des chaînes polyUb détermine le destin : **K48** (4+ Ub) → protéasome 26S ; **K63** → signalisation (NF-κB, DDR, endocytose) ; **K11** → dégradation mitotique ; **M1/linéaire** → NF-κB signalisation. Activation par dégron : souvent **phospho-dégron** (phospho → reconnaissance par E3 SCF-F-box ou APC/C). |
| **SUMO_NEDD** | SUMOylation / Neddylation (UBL family) | Protéines **Ubiquitin-Like** (UBL) conjuguées par des cascades analogues. **SUMO1/2/3** : conjuguées par SAE1/SAE2 (E1), UBC9 (E2 unique), ~10 SUMO E3 ligases. Effets : changements de localisation nucléaire, recrutement de co-répresseurs, protection contre l'ubiquitination. Souvent phospho-dépendant : motif **PDSM** (ψKxExxSP → SUMOylation sur K activée par phospho sur S). **Neddylation** : NEDD8 conjugué sur Cullines (CRL E3 ligases) → activation → ciblage de substrats vers le protéasome. Lien SUMO-Ubiquitin : **STUbL** E3 ligases (RNF4, RNF111) reconnaissent les chaînes polySUMO → ubiquitination → protéasome. |
| **PROTEASOME** | Ubiquitin-Protéasome (26S UPS) | Le **26S protéasome** = **20S** (chambre catalytique avec 3 activités protéasiques : chymotrypsin-like, trypsin-like, caspase-like) + 2 × **19S regulatory particle** (reconnaît K48-polyUb, déubiquitine, déplie, transloque vers 20S). Dégrade ~80 % de toutes les protéines. Régulation par **condensats** : RAD23B/hHR23B phase-sépare avec les chaînes polyUb → foci nucléaires protéolytiques. La dégradation de certains inhibiteurs (IκBα, β-catenin) **active des TF** (NF-κB, TCF) → feedback vers la transcription. |
| **AUTOPHAGY** | Autophagie sélective | Dégradation lysosomale sélective de protéines/organites ubiquitinés. **p62/SQSTM1** : récepteur cargo qui lie les chaînes K63/K48-polyUb + LC3/GABARAP sur les autophagosomes. **p62 phase-sépare** avec les chaînes polyUb → condensats → initiation de la séquestration autophagique. Flux : autophagosome (double membrane, LC3-II) + lysosome → autophagolysosome → dégradation. Les acides aminés libérés atteignent la surface lysosomale → signalisation Ragulator → **réactivation de mTORC1** (feedback majeur). |
| **CHAPERONES** | Chaperones / UPR | **Chaperones** : Hsp70/Hsc70 (assistance co-traductionnelle) ; Hsp90 (maturation kinases, TF, récepteurs stéroïdiens) ; CCT/TRiC (folding en chambre isolée — actine, tubuline). Lien avec l'ubiquitination : **CHIP** (C-terminus of Hsp70-Interacting Protein) = E3 ubiquitin ligase qui ubiquitine les substrats mal foldés liés à Hsp70/Hsp90 → protéasome. **UPR** (Unfolded Protein Response, ER stress) : **PERK** (phosphoryle eIF2α = branche ISR), **IRE1** (épissage non-conventionnel de XBP1 mRNA), **ATF6** (TF activateur de gènes chaperonnage ER). |
| **PAR** | ADP-ribosylation / PARP / PAR | **PARP1** (Poly ADP-Ribose Polymérase 1) détecte les cassures ADN (DDR) et synthétise des chaînes de **PAR** (Poly-ADP-Ribose) sur lui-même et d'autres protéines (Asp, Glu, Lys). Activé par les kinases DDR (ATM/ATR, phospho-dépendant). PAR est une molécule multivalente → nucléation rapide de **condensats de phase** (LLPS) au niveau des dommages ADN → recrutement de la machinerie de réparation. Les longues chaînes PAR recrutent aussi des E3 ubiquitin ligases → lien PAR-ubiquitination. Inhibiteurs PARP (olaparib) = thérapeutique cancer (synthetic lethality avec BRCA1/2). |

---

### Métaprincipes transversaux

| Nom code | Nom complet | Définition exacte |
|----------|-------------|-------------------|
| **LLPS** | Liquid-Liquid Phase Separation | Processus thermodynamique par lequel des macromolécules (protéines IDR-riches, ARN, protéines de liaison à l'ARN) se concentrent spontanément en une phase dense distincte (condensat liquide). Conduit par des **interactions multivalentes** : domaines IDR (Intrinsically Disordered Regions), répétitions RGG, tyrosines, interactions ARN-protéine. LLPS n'est **pas un mécanisme de régulation** : c'est le principe physique exploité par plusieurs mécanismes. Instances biologiques : super-enhancers (BRD4 + Mediator + Pol II CTD), stress granules (G3BP1 + TIA-1 + ARNm), P-bodies (DCP1/2 + XRN1), condensats protéolytiques (hHR23B + polyUb), condensats de réparation ADN (PAR + FUS + RPA). |
| **DECAY** | Turnover / clearance | Métaprincipe de retrait d'une molécule du système : dégradation d'ARNm (TIMER, CENSOR), dégradation protéasomale (PROTEASOME), autophagie sélective (AUTOPHAGY), et plus généralement bascule entre stockage temporaire et élimination. DECAY n'est pas un seul complexe moléculaire ; c'est une sortie fonctionnelle récurrente. |

---

## II. Catalogue des relations (72 arêtes mécanistiques + 8 liens méta)

### Code couleur
| Couleur | Type | Signification |
|---------|------|---------------|
| 🟢 Vert `#27ae60` | Activation directe | A recrute/active/dépose B |
| 🔴 Rouge `#c0392b` | Répression directe | A bloque/empêche B (arrowhead=tee) |
| 🟡 Jaune `#f4d03f` | Couplage Pol II | Mécanisme lié à la progression de Pol II |
| 🟠 Orange `#e67e22` | Couplage co-transcriptionnel | Régulation couplée à la transcription |
| 🟣 Violet `#8e44ad` | Mécanisme post-Tx / m6A / RBP | Régulation post-transcriptionnelle |
| ⚫ Gris `#566573` | PTM / signalisation post-trad | Régulation post-traductionnelle |
| 🔵 Bleu `#2e86c1` | Structural / 3D | Organisation tridimensionnelle |
| 🔵 Cyan `#5dade2` (pointillé) | LLPS | Participation au principe LLPS |
| 🩷 Rose `#f472b6` (pointillé) | DECAY | Participation au principe turnover / clearance |

### Abréviations et notation des labels DOT

| Terme | Sens |
|-------|------|
| `tx` | Transcription. Le graphe évite de l'utiliser pour la traduction afin de ne pas créer d'ambiguïté. |
| `co-tx` | Co-transcriptionnel : couplé à la progression de Pol II ou à l'ARN naissant. |
| `A` | Principe d'accessibilité : rendre un substrat disponible ou inaccessible. |
| `B` | Principe marque/lecture : une marque réversible produit un effet selon son lecteur et son contexte. |
| `C` | Principe de couplage cinétique : la vitesse d'un processus change l'issue d'un autre. |
| `initiation ↑` | Augmentation de l'initiation de la traduction. |
| `RQC` | Ribosome-associated Quality Control. Surveillance des ribosomes bloqués et dégradation du peptide naissant. |
| `NGD` | No-Go Decay. Dégradation liée à un ribosome bloqué sur l'ARNm. |
| `NSD` | Non-Stop Decay. Dégradation liée à un ARNm sans codon stop fonctionnel. |
| `SUMO` | Small Ubiquitin-like Modifier. Petite protéine conjuguée aux substrats comme marque post-traductionnelle. |
| `NEDDylation` | Conjugaison de NEDD8, notamment sur les cullines pour activer des E3 ligases CRL. |
| italique | Dans les descriptions, l'italique sert aux noms de gènes/protéines quand cela aide la lecture ; les boîtes du graphe restent des noms de mécanismes. |

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
| GUIDES | SILENCER | **PIRNAGUIDE** | piRNA-PIWI guident DNMT3L/3A vers les transposons → méthylation *de novo* |
| GUIDES | WRITER-R | **LNCRNAPRC2** | lncRNAs scaffolds (XIST, HOTAIR) recrutent PRC2 → H3K27me3 régional |

#### Épigénétique → Transcription
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| OPENER | KEYS | **OPENS-TF** | L'acétylation des histones relâche les nucléosomes → accès des TF |
| WRITER-R | KEYS | **SILENCES-TF** ⊣ | H3K27me3/H3K9me3 → chromatine compacte → exclusion des TF |
| SHUFFLER | KEYS | **REMODELS** | Les CRC repositionnent/éjectent des nucléosomes → fenêtre de liaison TF |
| WRITER-A | SCRIBE | **RECRUITS-POL2** | H3K4me3 recrute TAF3 (TFIID) → Pol II recruitment |
| HUBS | SCRIBE | **RELEASES-PAUSE** | P-TEFb concentrée dans les SE → phosphoryle Ser2-CTD → libération Pol II |
| ZONES (A) | WRITER-A | **COMPART-A** (back) | Les compartiments A co-localisent avec H3K27ac/K4me3 (causalité circulaire) |
| ZONES (B) | WRITER-R | **COMPART-B** (back) | Les compartiments B co-localisent avec H3K27/9me3 |
| SILENCER | ZONES | **METH-TO-B** | Méthylation CpG → recrutement MBD → compaction → compartiment B |

#### Transcription → Épigénétique (feedbacks)
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| KEYS | OPENER | **TF-HAT** | TF activateurs recrutent p300/CBP → dépôt H3K27ac sur les enhancers cibles |
| KEYS | WRITER-A | **TF-KMT** | TF recrutent MLL1-4/KMT2 → dépôt H3K4me3 aux promoteurs actifs |
| KEYS | SHUFFLER | **TF-CRC** (back) | TF recrutent SWI/SNF → remodeling sur leurs gènes cibles |

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
| SCRIBE | SPONGE | **POL2-LNCRNA** | Pol II transcrit les lncRNAs cytoplasmiques (UCHL1-AS, lincRNA-p21...) |
| SCRIBE | GUIDES | **POL2-NCRNAEPI** | Pol II transcrit les précurseurs piRNA et lncRNAs épigénétiques |
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
| STAMP | TIMER | **M6A-DECAY** | YTHDF2 recrute CCR4-NOT → déadénylation accélérée → decay |
| STAMP | CLIPS | **M6A-G4** | m6A déstabilise la structure secondaire → destabilize G-quadruplexes adjacents |
| DARTS | TIMER | **MIRNA-DECAY** | AGO2-RISC recrute CCR4-NOT → déadénylation + décapping |
| SPONGE | DARTS | **CERNA** ⊣ | lncRNA ceRNA séquestre les miRNA → décompression des ARNm cibles |
| CENSOR | TIMER | **NMD-DECAY** | UPF1-P recrute SMG6 (endonucléase) + SMG5/7 → dégradation rapide |
| TIMER | VAULT | **MRNA-SG** (bidirectionnel) | ARNm non traduits → stress granules ; SG dissolus → ARNm libérés |
| READERS | TIMER | **RBP-STABILITY** | HuR/ELAVL1 (stabilise AREs) vs TTP/ZFP36 (déstabilise AREs → CCR4-NOT) |
| CLIPS | BYPASS | **G4-IRES** | rG4 dans 5'UTR peut moduler l'accessibilité de l'IRES (zipper model) |
| VAULT | FORGE | **SG-RELEASE** | Résolution du stress → dissolution des SGs → ARNm libérés vers les ribosomes |

#### Post-transcriptionnel → Traductionnel
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| STAMP | FORGE | **M6A-INIT** | YTHDF1 recrute eIF3 → stimule l'initiation cap-dépendante |
| STAMP | BYPASS | **M6A-IRES** | m6A dans le 5'UTR → traduction cap-indépendante (sous stress) |
| READERS | FORGE | **FMRP-REPRESS** ⊣ | FMRP lie les polysomes et bloque l'élongation |
| READERS | BYPASS | **ITAF-IRES** | ITAFs (PTB, DAP5, hnRNPQ) = RBPs qui activent/inhibent les IRES |
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
| BRAKE | BYPASS | **ISR-IRES** | Cap-dep bloqué → switch vers IRES (ATF4, HIF-1α, c-Myc) |
| DECOY | FORGE | **UORF-COMPETE** ⊣ | uORFs séquestrent les ribosomes → réduction traduction mORF principal |
| FORGE | INSPECTOR | **STALL-RQC** | Traduction active → stalling sur codons rares ou structures → RQC/NGD |
| TEMPO | INSPECTOR | **CODON-STALL** | Codons rares → pause ribosomale prolongée → NGD/NSD/RQC |
| TEMPO | CHAPERONES | **COTRANSL-FOLD** | Rythme de traduction (codon usage) → cinétique de repliement co-traductionnel |
| INSPECTOR | PROTEASOME | **RQC-26S** | CAT-tailing du polypeptide nascent bloqué → reconnaissance LTN1 → dégradation |

#### Traduction → Transcription (feedback)
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| BYPASS | KEYS | **IRES-TF-LOOP** (**) | ATF4 (ISR), HIF-1α (hypoxie), c-Myc (IRES) synthétisés → TF qui reprogramment la transcription → boucle de rétroaction |

#### Post-traductionnel intra
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| PHOSPHO | UBI | **PHOSPHO-DEGRON** | Phospho-dégron reconnu par E3 SCF (β-TrCP, Fbxw7) ou APC/C |
| PHOSPHO | SUMO_NEDD | **PDSM** | Motif PDSM (ψKxExxSP) → phospho de la Ser → activation SUMOylation de la Lys |
| PHOSPHO | PAR | **DDR-PARP** | ATM/ATR activés par DSBs → phosphorylent et activent PARP1 |
| PHOSPHO | KEYS | **PHOSPHO-TF** | Phosphorylation active/inactive les TF (IKK→IκB→NF-κB, JAK→STAT, MAPK→ELK1) |
| UBI | PROTEASOME | **K48-PROTEASOME** | K48-polyUb (4+) → dégradation par le 26S protéasome |
| UBI | AUTOPHAGY | **K63-AUTOPHAGY** | K63-polyUb → récepteur p62/SQSTM1 → autophagosomes |
| SUMO_NEDD | UBI | **STUBLS** | polySUMO → reconnu par RNF4/RNF111 (STUbL E3) → ubiquitination → protéasome |
| PAR | PROTEASOME | **PAR-CONDENSATE** | PAR chaînes longues → nucléation de condensats protéolytiques → protéasome |
| CHAPERONES | BRAKE | **UPR-ISR** | PERK (branche UPR) = kinase eIF2α → ISR = pont ER stress–ISR |
| CHAPERONES | UBI | **CHIP-E3** | CHIP (Hsp70/90-associated E3) ubiquitine les protéines mal foldées → 26S |
| AUTOPHAGY | FORGE | **AUTOPHAGY-MTOR** | Acides aminés libérés → Ragulator/RRAG GTPases surface lysosomale → mTORC1 réactivé |
| PROTEASOME | KEYS | **PROTEASOME-TF** | Dégradation des inhibiteurs de TF (IκBα→NF-κB ; β-catenin→TCF/LEF) |

#### Post-traductionnel → Transcription / Pol II
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| PHOSPHO | SCRIBE | **CDK9-CTD** | CDK9/P-TEFb (phosphorylé et activé) → Ser2-CTD → libération de la pause Pol II |
| PHOSPHO | BRAKE | **KINASE-EIF2A** | GCN2, PERK, HRI, PKR phosphorylent eIF2α Ser51 → BRAKE activé |

#### Métaprincipes transversaux
| Source | Cible | Nom | Mécanisme |
|--------|-------|-----|-----------|
| LLPS | HUBS | **LLPS-SE** | LLPS forme les condensats de transcription = super-enhancers |
| LLPS | VAULT | **LLPS-SG-PB** | LLPS forme les stress granules et P-bodies |
| LLPS | PROTEASOME | **LLPS-PROTEASOME** | LLPS forme les condensats protéolytiques (hHR23B + polyUb) |
| LLPS | PAR | **LLPS-PAR** | Les chaînes PAR nucléent des condensats de réparation ADN |
| DECAY | TIMER | **DECAY-MRNA** | Turnover des ARNm par deadenylation, decapping et exonucléases |
| DECAY | CENSOR | **DECAY-NMD** | NMD comme branche de surveillance et élimination des ARNm aberrants |
| DECAY | PROTEASOME | **DECAY-PROTEASOME** | Dégradation protéique ubiquitine-dépendante |
| DECAY | AUTOPHAGY | **DECAY-AUTOPHAGY** | Clearance lysosomale sélective de protéines, agrégats ou organites |

---

## III. Overlaps et fusions — Ce qui a été consolidé

| Entités fusionnées | Justification |
|--------------------|---------------|
| Super-enhancers + Condensats de transcription | Même structure biologique, deux techniques (ChIP-seq vs microscopie LLPS) |
| Compartiments A/B + État épigénétique global | Corrélation forte ; les compartiments *émergent* des marques mais ne sont pas identiques |
| YTHDF1 + YTHDF2 + YTHDF3 → **STAMP** | Un seul signal (m6A), 3 lecteurs = 3 sorties d'un même mécanisme |
| Codon usage + tRNA modifications + Ribosome hétérogénéité → **TEMPO** | Trois facettes du même principe "efficacité de décodage" |
| SWI/SNF + ISWI + CHD + INO80 → **SHUFFLER** | Même principe ATP-dependent, 4 sous-familles |
| eRNAs (enhancer RNAs) | Sous-produits de l'activité enhancer = readout, pas mécanisme propre |
| ISR branch PERK / UPR | PERK est à la fois une kinase ISR et la branche PERK de l'UPR : intégré via CHAPERONES → BRAKE |
| siRNA / miRNA | Partagent RISC/AGO2 ; siRNA chez les animaux = variante outil expérimental surtout → fusionné dans DARTS |
| ceRNA hypothesis | Conséquence de la saturation du pool miRNA = cas particulier de SPONGE + DARTS |

---

## IV. Architecture mentale finale — 3 stratégies fondamentales

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
              UBI (K48 → PROTEASOME ; K63 → AUTOPHAGY)
              PHOSPHO (phospho → activation ou dégradation selon le substrat)

Stratégie C — COUPLAGE CINÉTIQUE
  "La vitesse du processus A détermine le résultat du processus B"
  Instances : Pol II rate → SPLICER (kinetic window)
              H3K36me3 déposé par SCRIBE → SPLICER (même couplage, autre niveau)
              TC limiting (BRAKE) → DECOY bypass → FORGE sélectif ATF4
              Codon pause (TEMPO) → CHAPERONES co-traductionnel
              IRES-TF loop (synthèse ATF4 → reprogrammation transcriptomique)
```

---

## V. Bases de données et ressources

| Ressource | URL | Contenu |
|-----------|-----|---------|
| ENCODE | https://encodeproject.org | ChIP-seq, ATAC-seq, CTCF, histone marks, 150+ cell types |
| Roadmap Epigenomics | https://egg2.wustl.edu/roadmap | 127 types cellulaires, méthylation + histones |
| GTEx | https://gtexportal.org | eQTLs tissue-spécifiques |
| FANTOM5 | https://fantom.gsc.riken.jp/5 | TSS atlas, eRNAs, lncRNAs |
| miRBase | https://mirbase.org | Catalogue miRNA |
| POSTAR3 | http://postar.ncrnalab.org | Sites de liaison RBPs (CLIP-seq) |
| RMBase v3 | https://rmbase.sysu.edu.cn | Sites de modifications ARN (m6A, m5C, Ψ...) |
| G4IMOTIF | — | G-quadruplexes dans les transcriptomes |
| PhosphoSitePlus | https://phosphosite.org | Sites PTM (phospho, ubiq, acétyl, méthyl) |
| STRING | https://string-db.org | Interactions protéine-protéine |
| UniProt | https://uniprot.org | Annotations protéines + PTMs |

## VI. Références fondamentales

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

*v7 — 37 mécanismes, 2 métaprincipes, 72 relations mécanistiques + 8 liens méta*
*Fichier : `assets/documents/gene-regulation-landscape-details.md`*
*Diagramme : `assets/documents/gene-reg-v7.dot` + `assets/images/gene-reg-v7.png`*
