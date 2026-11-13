# Accurate segmentation of pulmonary arteries and veins via a human-in-the-loop framework with application in COPD.



## Resume


Accurate segmentation of pulmonary arteries and veins via a human-in-the-loop framework with application in COPD.

Pulmonary vascular diseases may affect arteries and veins through different physiological mechanisms, necessitating separate assessment of the two vascular trees. However, manual analysis of chest computed tomography (CT) images is time-consuming, subjective, and challenging to scale for clinical studies. To address this, we propose a novel Human-in-the-Loop (HITL) framework for annotation and model training to develop an automated pulmonary artery-vein segmentation model. Through three iterative HITL rounds, we constructed 30 gold-standard annotated datasets and trained three deep learning models. The optimal model achieved strong performance, with a Dice coefficient of 86.2%, IoU of 75.7%, sensitivity of 85.8%, and precision of 88.1%. This model was then applied to segment pulmonary arteries and veins in CT scans from patients with chronic obstructive pulmonary disease (COPD). Quantitative analysis revealed that, as COPD progresses, the volume and surface area of both pulmonary arter

Human-in-the-loop image segmentation and annotation

Troubleshooting image segmentation models with human-in-the-loop

Analysis of in vivo single cell behavior by high throughput, human-in-the-loop segmentation of three-dimensional images

A human-in-the-loop method for pulmonary nodule detection in CT scans

AbstractAutomated pulmonary nodule detection using computed tomography scans is vital in the early diagnosis of lung cancer. Although extensive well-performed methods have been proposed for this task, they suffer from the domain shift issue between training and test images. Unsupervised domain adaptation (UDA) methods provide a promising means to mitigate the domain variance; however, their performance is still limited since no target domain supervision is introduced. To make the pulmonary nodule detection algorithm more applicable in clinical practice and further boost the performance across domains, we propose a human-in-the-loop method in a semi-supervised fashion to enhance the model generalization ability when transferred from source domain to target domain. Specifically, we first train a detector model on source domain, and then the pre-trained detector is utilized with our proposed uncertainty-guided sample selection scheme (USSS) to find a few target domain samples worth annotating most and obtain their human annotations. Finally, the annotated and the rest unlabeled target domain samples are used together to refine the pre-trained model via our proposed zoom-in and zoom-out constraint (ZZC) strategy. We evaluate our method on the Nodule Analysis 2016 (LUNA16) and TianChi datasets. Experimental results show that our method surpasses recent competitive methods on source domain and also achieves surprising performance on target domain.

A self-training framework for semi-supervised pulmonary vessel segmentation and its application in COPD.

BackgroundIt is fundamental for accurate segmentation and quantification of the pulmonary vessel, particularly smaller vessels, from computed tomography (CT) images in chronic obstructive pulmonary disease (COPD) patients.ObjectiveThe aim of this study was to segment the pulmonary vasculature using a semi-supervised method.MethodsIn this study, a self-training framework is proposed by leveraging a teacher-student model for the segmentation of pulmonary vessels. First, the high-quality annotations are acquired in the in-house data by an interactive way. Then, the model is trained in the semi-supervised way. A fully supervised model is trained on a small set of labeled CT images, yielding the teacher model. Following this, the teacher model is used to generate pseudo-labels for the unlabeled CT images, from which reliable ones are selected based on a certain strategy. The training of the student model involves these reliable pseudo-labels. This training process is iteratively repeated un

Human and AI collaboration for pulmonary nodule segmentation

Medical expert annotators are scarce, and blind reliance on artificial intelligence (AI) can be misleading, motivating approaches in which humans, particularly junior medical trainees or even non-medical personnel, collaborate with AI to achieve robust medical segmentation. Although the Segment Anything Model (SAM) shows promise for general-purpose image segmentation, its performance in human-AI collaboration for specialized medical tasks has not been thoroughly evaluated. Here we present Hi-Seg, a human-in-the-loop segmentation framework for pulmonary nodules built on SAM. Humans iteratively refine prompts through trial-and-error learning and semantic reasoning, progressively guiding SAM toward higher-quality masks. Using chest CT scans from 1,179 patients across 12 centers, we conducted the first large-scale external validation of collaborative human-SAM segmentation. Across all annotator groups, Hi-Seg achieved a mean Dice score of almost 85%, outperforming five state-of-the-art dee

Human-in-the-Loop-A Deep Learning Strategy in Combination with a Patient-Specific Gaussian Mixture Model Leads to the Fast Characterization of Volumetric Ground-Glass Opacity and Consolidation in the Computed Tomography Scans of COVID-19 Patients.

<b>Background/Objectives:</b> The accurate quantification of ground-glass opacities (GGOs) and consolidation volumes has prognostic value in COVID-19 patients. Nevertheless, the accurate manual quantification of the corresponding volumes remains a time-consuming task. Deep learning (DL) has demonstrated good performance in the segmentation of normal lung parenchyma and COVID-19 pneumonia. We introduce a Human-in-the-Loop (HITL) strategy for the segmentation of normal lung parenchyma and COVID-19 pneumonia that is both time efficient and quality effective. Furthermore, we propose a Gaussian Mixture Model (GMM) to classify GGO and consolidation based on a probabilistic characterization and case-sensitive thresholds. <b>Methods:</b> A total of 65 Computed Tomography (CT) scans from 64 patients, acquired between March 2020 and June 2021, were randomly selected. We pretrained a 3D-UNet with an international dataset and implemented a HITL strategy to refine the local dataset with delineation

Learning With Context Feedback Loop for Robust Medical Image Segmentation


## Quote


We proposed an efficient human-in-the-loop framework for troubleshooting segmentation models, and demonstrated its promise under realistic settings.

In this research, we incorporate the human-in-the-loop technique into TTA. The resultant HiTTA framework, along with a divergence loss, boosts the adaptation of deep learning-based medical image segmentation model to differing data distributions across various medical institutions.

In this research, we incorporate the human-in-the-loop technique into TTA. The resultant HiTTA framework, along with a divergence loss, boosts the adaptation of deep learning-based medical image segmentation model to differing data distributions across various medical institutions.

Building on this idea, we further introduce an interactive segmentation approach based on human-in-the-loop learning. This mechanism integrates expert knowledge into the model's prediction process, enabling dynamic optimization and iterative updates guided by user interactions, which enhances both segmentation accuracy and interpretability.

suitable for integration with real time human-inthe-loop systems


## Insight


efficacy: La stratégie Human-in-the-Loop a permis d'atteindre les seuils de qualité de segmentation définis par des radiologistes experts (DSC ≥ 0,95 pour le parenchyme pulmonaire normal et ≥ 0,8 pour la pneumonie à COVID-19) après seulement trois cycles itératifs de correction.

efficacy: Le fine-tuning ciblé sur des cas limites détectés via un cadre human-in-the-loop améliore significativement la performance du modèle de segmentation cible, y compris sa robustesse à des cas limites non vus lors d'itérations ultérieures.

methodology: Le système proposé combine un agent IA conversationnel opérant par commandes vocales avec les modèles de fondation BiomedParse et SAM2, dans une architecture human-in-the-loop où l'utilisateur en VR peut affiner les masques de segmentation via pointage par la tête, regard ou contrôleurs manuels avant un rendu 3D à échelle réelle.

methodology: L'intégration d'une boucle de supervision faible avec intervention humaine (human-in-the-loop) constitue une stratégie visant à optimiser l'efficacité de l'annotation pour l'apprentissage profond appliqué à la segmentation cellulaire.


## Raw_Conclusion


In this research, we incorporate the human-in-the-loop technique into TTA. The resultant HiTTA framework, along with a divergence loss, boosts the adaptation of deep learning-based medical image segmentation model to differing data distributions across various medical institutions. By seamlessly integrating clinician feedback into the TTA process, HiTTA is able to align model predictions more closely to clinical preferences, dramatically enhancing model utility in real clinical settings. Our extensive experiments on a cross-domain, multi-annotator, and joint OD/OC segmentation dataset underscore the pivotal role that human expertise plays in refining AI model performance. This sets a solid foundation for expanding future work to other medical image segmentation tasks and optimizing human-AI collaboration, thus paving the way for adaptable, efficient AI tools to transform medical diagnostic and treatment processes.

In this research, we incorporate the human-in-the-loop technique into TTA. The resultant HiTTA framework, along with a divergence loss, boosts the adaptation of deep learning-based medical image segmentation model to differing data distributions across various medical institutions. By seamlessly integrating clinician feedback into the TTA process, HiTTA is able to align model predictions more closely to clinical preferences, dramatically enhancing model utility in real clinical settings. Our extensive experiments on a cross-domain, multi-annotator, and joint OD/OC segmentation dataset underscore the pivotal role that human expertise plays in refining AI model performance. This sets a solid foundation for expanding future work to other medical image segmentation tasks and optimizing human-AI collaboration, thus paving the way for adaptable, efficient AI tools to transform medical diagnostic and treatment processes.


## Synthese


De nombreuses pathologies affectent directement le système vasculaire, mais la caractérisation complète de la structure hiérarchique et tridimensionnelle des vaisseaux sanguins par imagerie demeure un défi majeur. Bien que les réseaux de neurones convolutifs constituent aujourd'hui l'approche de référence pour la segmentation sémantique en imagerie médicale, la plupart des modèles existants sont entraînés sur un jeu de données limité à une seule pathologie, un seul organe et une seule modalité d'imagerie, notamment pour la vascularisation rétinienne en deux dimensions ou cérébrale en trois dimensions. Des outils comme Cellpose ont introduit en imagerie cellulaire une approche alternative de type human-in-the-loop, combinant un modèle général pré-entraîné et un fine-tuning rapide sur les données de l'utilisateur final, réduisant ainsi le besoin d'annotation manuelle ; des équivalents propriétaires existent pour la segmentation vasculaire, mais aucun outil open-source comparable n'était disponible. Cette étude vise donc à exploiter la structure tubulaire universelle des vaisseaux sanguins pour développer un modèle de segmentation 3D généralisable à travers modalités et organes, en privilégiant la diversité des données d'entraînement plutôt que leur volume, afin de produire un modèle pouvant être spécialisé pour de nouvelles tâches avec un minimum de données annotées par l'utilisateur.


## Methodologie


De nombreuses pathologies affectent directement le système vasculaire, mais la caractérisation complète de la structure hiérarchique et tridimensionnelle des vaisseaux sanguins par imagerie demeure un défi majeur. Bien que les réseaux de neurones convolutifs constituent aujourd'hui l'approche de référence pour la segmentation sémantique en imagerie médicale, la plupart des modèles existants sont entraînés sur un jeu de données limité à une seule pathologie, un seul organe et une seule modalité d'imagerie, notamment pour la vascularisation rétinienne en deux dimensions ou cérébrale en trois dimensions. Des outils comme Cellpose ont introduit en imagerie cellulaire une approche alternative de type human-in-the-loop, combinant un modèle général pré-entraîné et un fine-tuning rapide sur les données de l'utilisateur final, réduisant ainsi le besoin d'annotation manuelle ; des équivalents propriétaires existent pour la segmentation vasculaire, mais aucun outil open-source comparable n'était disponible. Cette étude vise donc à exploiter la structure tubulaire universelle des vaisseaux sanguins pour développer un modèle de segmentation 3D généralisable à travers modalités et organes, en privilégiant la diversité des données d'entraînement plutôt que leur volume, afin de produire un modèle pouvant être spécialisé pour de nouvelles tâches avec un minimum de données annotées par l'utilisateur.


## Conclusion


This study presents a semi-supervised learning framework based on nnFormer for pulmonary vessel segmentation using CT images from patients with COPD, incorporating interactive annotation and a teacher-student consistency training strategy to mitigate limited annotated data, achieving a DSC of 0.850 and a precision of 0.903 These results outperform fully supervised approaches including UNETR, Swin UNETR, and nnU-Net Compared to the fully supervised version of nnFormer, the proposed approach improves segmentation precision by 2.3% while maintaining comparable DSC performance The framework demonstrates an enhanced capability to delineate the complete pulmonary vasculature, particularly finer vessels, expected to facilitate more accurate quantitative analysis of pulmonary vessels across different stages of COPD The Semi2 model achieves a precision of 0.903, a notable improvement over the Fully-supervised model's 0.880 As COPD severity increases (GOLD 1 through GOLD 4), there is an expansion in lung vasculature (increased TBV and surface area) but a decrease in the proportion of blood in the smallest vessels (BV5 and BV5/TBV), possibly reflecting compromised microcirculation As COPD becomes more severe, there is a decrease in the number of the smallest vessels and an increase in the number of larger vessels, possibly reflecting pathological changes such as inflammation and remodeling The iterative self-training mechanism and Transformer-based network architecture exhibit strong generalization potential for broader applications in segmenting tubular structures in other biomedical imaging contexts, such as retinal vessels and coronary arteries

Formulation d'un nouveau problème de vision par ordinateur visant à exposer efficacement les échecs des modèles de segmentation les plus performants et à apprendre de ces échecs pour améliorer la généralisation dans le monde réel Proposition d'un cadre efficace de troubleshooting avec humain dans la boucle (human-in-the-loop) pour les modèles de segmentation, dont la promesse a été démontrée dans des conditions réalistes

Le cadre proposé de segmentation de la cicatrice, avec une conception 'human-in-the-loop', permet une quantification de la cicatrice myocardique rapide, précise et hautement reproductible à partir de LGE-CMR. Cette approche pourrait offrir une performance plus cohérente dans les flux de travail cliniques de routine. En intégrant un entraînement tenant compte de l'incertitude avec des prompts guidés par le clinicien, le système offre une quantification de la cicatrice rapide, cohérente et interprétable à travers des données hétérogènes. Sa conception légère et son architecture interactive en temps réel en font une solution pratique pour standardiser l'interprétation des CMR dans divers environnements d'imagerie.


## Discussion


L'approche Human-in-the-Loop (HITL), entraînée sur un jeu de données international puis ré-entraînée sur des scanners CT locaux, a permis d'atteindre les critères de qualité fixés par les radiologues (DSC ≥0,95 pour le parenchyme pulmonaire normal et ≥0,8 pour la pneumonie COVID-19) après seulement trois cycles de correction, avec une amélioration progressive de la qualité de segmentation à chaque cycle. La segmentation automatisée obtenue après ces trois cycles s'est révélée comparable à celle produite manuellement à partir de zéro par sept équipes d'experts (DSC de 0,98 ± 0,01 pour le parenchyme normal et 0,86 ± 0,03 pour la pneumonie COVID-19), démontrant que la méthode HITL combine efficacité temporelle et précision diagnostique. L'analyse de Bland-Altman a confirmé un bon accord entre le pourcentage d'infection (PI) dérivé de la méthode HITL et les délinéations manuelles des experts, avec des marges d'erreur inférieures à 5 % aussi bien sur les scanners CT non contrastés que rehaussés par contraste. Enfin, le modèle de mélange gaussien (GMM) a mis en évidence, au sein des voxels identifiés comme pneumonie COVID-19, des histogrammes d'unités Hounsfield suggérant la présence de deux distributions gaussiennes sous-jacentes, apportant une caractérisation probabiliste complémentaire du verre dépoli (GGO) et de la consolidation, bien qu'aucun seuil standardisé de HU ne soit actuellement reconnu pour ces motifs.