# Large-vocabulary segmentation for medical images with text prompts

**Auteurs** : Ziheng Zhao, Yao Zhang, Chaoyi Wu, Xiaoman Zhang, Xiao‐Hua Zhou, Ya Zhang, Yanfeng Wang, Weidi Xie
**Année** : 2025
**DOI** : 10.1038/s41746-025-01964-w

## Résumé

This paper aims to build a model that can Segment Anything in 3D medical images, driven by medical terminologies as Text prompts, termed as SAT. Our main contributions are three-fold: (i) We construct the first multimodal knowledge tree on human anatomy, including 6502 anatomical terminologies; Then, we build the largest and most comprehensive segmentation dataset for training, collecting over 22K 3D scans from 72 datasets, across 497 classes, with careful standardization on both image and label space; (ii) We propose to inject medical knowledge into a text encoder via contrastive learning and formulate a large-vocabulary segmentation model that can be prompted by medical terminologies in text form. (iii) We train SAT-Nano (110M parameters) and SAT-Pro (447M parameters). SAT-Pro achieves comparable performance to 72 nnU-Nets-the strongest specialist models trained on each dataset (over 2.2B parameters combined)-over 497 categories. Compared with the interactive approach MedSAM, SAT-Pro consistently outperforms across all 7 human body regions with +7.1% average Dice Similarity Coefficient (DSC) improvement, while showing enhanced scalability and robustness. On 2 external (cross-center) datasets, SAT-Pro achieves higher performance than all baselines (+3.7% average DSC), demonstrating superior generalization ability.Medical image segmentation aims to identify and delineate regions of interest (ROIs) like organs, lesions, and tissues in diverse medical images, which plays a crucial role in numerous clinical applications, such as disease diagnosis, treatment planning, and disease progression tracking 1-5 , as well as in medical research 6,7 . Traditionally, radiologists perform manual segmentation to measure volume, shape, and location in a slice-wise manner, which is both time-consuming and challenging to scale with the growing volume of medical data. Consequently, there is a pressing need for automated and robust medical image segmentation methods in clinical settings, to enhance efficiency and scalability.Recent advancements in medical image analysis have been marked by a surge in deep learning. These developments have yielded a spectrum of segmentation models, each trained for specific tasks 3,8-13 , often referred to as 'specialist' models. While these models demonstrate impressive segmentation capabilities, their major drawback lies in their narrow specialization. Designed and optimized for distinct ROIs and imaging modalities, these models [14][15][16][17][18][19] require distinct preprocessing methods for each dataset. As a result, they often fall short in diverse and dynamic clinical environments, where adaptability to new conditions and imaging techniques is essential.There is a growing interest in developing foundation models for medical image segmentation 20,21 , by adapting the pre-trained segment anything model (SAM) 22 models from the computer vision community. However, while transferring to medical scenarios, these models trained on natural images suffer from fundamental limitations: (i) models typically perform 2D slice segmentation, which is later fused into 3D volumes through post-processing. This approach overlooks the crucial contextual information in 3D radiological imaging; (ii) models often require point or box inputs as prompts, thus are interactive segmentation models, requiring considerable manual effort for use in practice; (iii) models suffer from significant domain gaps, from image statistics to domain-specific medical knowledge.In this paper, we present the first knowledge-enhanced foundation model for 3D medical volume segmentation, with medical terminology as text prompt, termed as SAT. In practice, our model can effectively take 3D volumes as visual inputs along with text prompts to seamlessly tackle various medical image segmentation tasks, across modalities, anatomies, and body regions. As illustrated in Fig. 1, our proposed method distinguishes itself from previous medical segmentation paradigms, that can be seamlessly applied to clinical practice or integrated with any large language model. Specifically, we make the following contributions in Fig. 2:On dataset construction, we construct a knowledge tree on anatomy concepts and definitions throughout the human body. On the visual side, we

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'Nombre de cibles anatomiques couvertes', 'value': '497', 'unit': 'cibles anatomiques', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'It includes 497 anatomical targets across 8 regions and various lesions of the human body, assembled from 72 distinct datasets.'}, {'outcome': 'Nombre de régions anatomiques couvertes', 'value': '8', 'unit': 'régions', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'It includes 497 anatomical targets across 8 regions and various lesions of the human body, assembled from 72 distinct datasets.'}, {'outcome': 'Nombre de jeux de données assemblés', 'value': '72', 'unit': 'jeux de données', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'It includes 497 anatomical targets across 8 regions and various lesions of the human body, assembled from 72 distinct datasets.'}, {'outcome': 'Ratio de split train/test par dataset dans SAT-DS', 'value': '8:2', 'unit': 'ratio', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'Specifically, we split each dataset in SAT-DS into train and test splits in 8:2 ratio, a combination of these test splits is used for internal evaluation, i.e., in-domain data.'}], 'qualitative_findings': ['SAT est proposé en deux variantes, SAT-Pro et SAT-Nano, pour équilibrer coût computationnel et performance.', 'SAT est comparé à trois catégories de méthodes: modèles spécialistes (nnU-Nets, SwinUNETR, U-Mamba), modèles de segmentation interactive (MedSAM), et modèles de segmentation guidés par texte (BiomedParse).', "L'évaluation est menée sur des jeux de données internes (in-domain, issus de SAT-DS) et externes (AbdomenAtlas 1.1 et LiQA), ces derniers étant exclus de l'entraînement de tous les modèles comparés, simulant un scénario de test multi-centres.", "L'évaluation externe ne comporte pas de nouvelles classes, car les cibles de segmentation du corps humain sont relativement limitées et fixes.", "Les résultats sont présentés selon plusieurs axes: par région, par classe et par jeu de données, les évaluations par classe et par région étant calculées par moyenne macro à partir des différents jeux de données (ex. le 'brainstem' en CT est moyenné à partir de HAN Seg, PDDCA et SegRap2023 Task 1).", "Une étude d'ablation sur l'encodeur de texte est présentée pour évaluer l'impact de l'injection de connaissances.", 'Des résultats qualitatifs illustrent le potentiel de SAT comme interface entre langage et segmentation.'], 'main_findings': ['SAT est un modèle fondation de segmentation à large vocabulaire pour images médicales 3D, utilisant des prompts textuels pour gérer un large éventail de tâches hétérogènes.', 'SAT est évalué de manière exhaustive face à des modèles spécialistes, des modèles de segmentation interactive et des modèles de segmentation guidés par texte, sur des données internes et externes.']}

## Conclusions

SAT constitue une avancée importante vers un modèle de segmentation universel pour l'imagerie médicale, capable de traiter au sein d'un seul modèle généraliste des images et cibles de segmentation diverses provenant de différents scénarios cliniques, remplaçant ainsi le besoin de dizaines de modèles spécialistes SAT-Pro obtient des résultats compétitifs par rapport à un ensemble de 72 modèles spécialistes, avec des performances comparables à nnU-Net et U-Mamba, et supérieures à SwinUNETR, tout en réduisant la taille du modèle à 20% ou moins de celle de l'ensemble SAT-Pro montre une meilleure capacité de généralisation que tous les modèles spécialistes sur des jeux de données multicentriques externes, démontrant une excellente transférabilité inter-centres SAT-Ft (fine-tuné sur un jeu de données spécifique) permet d'améliorer encore les performances, équilibrant ainsi les besoins cliniques entre solutions généralistes et modèles spécialistes En tant que méthode automatique guidée par texte, SAT offre une alternative aux modèles de segmentation interactifs, avec une précision et une robustesse accrues, en particulier sur les cibles de forme irrégulière, tout en réduisant le temps d'inférence utilisateur et les coûts associés SAT surpasse BiomedParse (travail concurrent de segmentation 2D guidée par texte) en termes d'applicabilité (images radiologiques 3D) et de performance, en domaine comme hors domaine Les lois d'échelle observées dans les grands modèles de langage s'appliquent également à la segmentation médicale à large vocabulaire : SAT-Pro (447M) surpasse SAT-Nano (110M) sur la plupart des régions et classes La construction du premier graphe de connaissances multimodal sur l'anatomie humaine et l'injection de connaissances améliorent significativement la performance de segmentation, en particulier pour les classes 'tail' (rares) SAT peut servir d'agent reliant langage et segmentation, capable de segmenter des cibles à partir des sorties de modèles de langage et de supporter le visual grounding dans divers scénarios cliniques, ce qui en fait un outil performant et efficace collaborant avec les grands modèles de langage

## Download links of the 72 datasets in SAT-DS

| Dataset |
| --- |

### Formule


$$D ¼ fðx 1 ; y 1 ; T 1 Þ; . . . ; ðx K ; y K ; T K Þg, where x i 2 R H × W × D × C denotes the image scan, y i 2 R H × W × D × M$$

### Formule


$$ŷi ¼ Φ SAT ðΦ visual ðx i Þ; Φ text ðT i ÞÞ;ð1Þ$$

### Formule


$$z ¼ Φ text ðtÞ; t 2 ½t i ; p i ; t i þ r ij ; r ij þ t j ; z 2 R d ;ð2Þ$$

### Formule


$$V i ¼ fv i1 ; v i2 ; . . . ; v iS g ¼ Φ visual ðx i Þ; v is 2 R H s × W s × D s × d s ;ð3Þ$$

### Formule


$$z ¼ F pooling ðΦ visual ðx i Þ; y i Þ; z 2 R d :ð4Þ$$

### Formule


$$L knowledge ¼ À 1 N X N i¼1 ðlog expðz i Á z 0 =τÞ P N k¼1 1 i≠k expðz i Á z 0 =τÞ þ log expðz i Á z 0 =τÞ P N k¼1 1 i≠k expðz k Á z 0 =τÞ Þ;ð5Þ$$

### Formule


$$z i ¼ Φ text ðt i Þ; z i 2 R d :ð6Þ$$

### Formule


$$u i ¼ Φ dec ðV i Þ; u i 2 R H × W × D × d 0 ;ð7Þ$$

### Formule


$$q i ¼ Φ query ðV i ; z i Þ; q i 2 R d :ð8Þ$$

### Formule


$$ŷi ¼ σðgðq i Þ Á u i Þ; ŷi 2 R H × W × D ;ð9Þ$$

### Formule


$$L ¼ À 1 M X M m¼1 1 C X C c¼1 p c;m Á log s c;m |fflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflffl{zfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflffl} Binary Cross Entropy Loss þð1 À 2 P M i¼1 P C c¼1 p c;m Á s c;m P M m¼1 P C c¼1 p 2 c;m þ P M m¼1 P C c¼1 s 2 c;m |fflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflffl{zfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflfflffl} Dice Loss Þð10Þ$$

### Formule


$$DSCðP; GÞ ¼ 2jP T Gj jPj þ jGj :ð11Þ$$

### Formule


$$NSDðP; GÞ ¼ j∂P T B ∂G j þ j∂G T B ∂P j j∂Pj þ j∂Gj ;ð12Þ$$
