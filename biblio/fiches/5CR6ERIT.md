# DGPDT: Detection-Guided and Prompt-Driven Transformers for Automated and Generalizable Cobb Angle Estimation.



## Resume


DGPDT: Detection-Guided and Prompt-Driven Transformers for Automated and Generalizable Cobb Angle Estimation.

Accurate Cobb angle measurement is essential for scoliosis assessment but remains labor-intensive and observer-dependent. We introduce DGPDT (Detection-Guided Prompt-driven Transformer), a unified transformer-based framework that integrates vertebra detection and foundation-model segmentation for generalizable spinal analysis. A Roboflow Detection Transformer (RF-DETR) with a DINOv2 backbone localizes vertebrae, followed by post-processing to ensure anatomical continuity. The resulting bounding boxes serve as automatic prompts for a fine-tuned Segment Anything Model 2.1 (SAM 2.1), which generates high-resolution vertebral masks. Cobb angles are then computed from vertebral masks, enabling estimation of both main and compensatory curves. Evaluations on the in-house (TVGH-SpineXR) and external (SpineWeb-16) datasets demonstrate encouraging performance on both internal and external datasets, achieving mean Dice coefficients of 0.944 and 0.781, respectively, and mean absolute Cobb angle er

Fully Automated Femoral Neck-Shaft Angle Measurement Based on Keypoint Detection

Segmentation-guided coordinate regression for robust landmark detection on X-rays: application to automated assessment of lower limb alignment_supp1-3394895.pdf

AGMB-Transformer: Anatomy-Guided Multi-Branch Transformer Network for Automated Evaluation of Root Canal Therapy.

Accurate evaluation of the treatment result on X-ray images is a significant and challenging step in root canal therapy since the incorrect interpretation of the therapy results will hamper timely follow-up which is crucial to the patients' treatment outcome. Nowadays, the evaluation is performed in a manual manner, which is time-consuming, subjective, and error-prone. In this article, we aim to automate this process by leveraging the advances in computer vision and artificial intelligence, to provide an objective and accurate method for root canal therapy result assessment. A novel anatomy-guided multi-branch Transformer (AGMB-Transformer) network is proposed, which first extracts a set of anatomy features and then uses them to guide a multi-branch Transformer network for evaluation. Specifically, we design a polynomial curve fitting segmentation strategy with the help of landmark detection to extract the anatomy features. Moreover, a branch fusion module and a multi-branch structure

A deep learning-based automatic segmentation of zygomatic bones from cone-beam computed tomography images: A proof of concept.

To investigate the efficiency and accuracy of a deep learning-based automatic segmentation method for zygomatic bones from cone-beam computed tomography (CBCT) images.

Towards clinically applicable automated mandibular canal segmentation on CBCT.

To develop a deep learning-based system for precise, robust, and fully automated segmentation of the mandibular canal on cone beam computed tomography (CBCT) images.

Segmentation-Guided Coordinate Regression for Robust Landmark Detection on X-Rays: Application to Automated Assessment of Lower Limb Alignment

Preclinical evaluation of a clinical prototype transrectal diffuse optical tomography system for monitoring photothermal therapy of focal prostate cancer.

<h4>Significance</h4>Our work demonstrates in preclinical models that continuous-wave transrectal diffuse optical tomography (TRDOT) can be used to accurately monitor photothermal therapy (PTT) and, in particular, the progression of the photocoagulation boundary toward the rectum. When used in patients, this should prevent rectal damage during PTT, thereby achieving maximum treatment efficacy while ensuring safety, using a technology platform suitable for wide dissemination.<h4>Aim</h4>We aim to validate that TRDOT measurements analyzed using a shape-based image-reconstruction algorithm (SBDOT) allow localization of the photocoagulation boundary during PTT within ±1  mm toward the rectum in the transverse plane.<h4>Approach</h4>TRDOT measurements were performed in tissue-simulating phantoms, ex vivo tissues, and an in vivo canine prostate model. The accuracy and sensitivity of reconstructing the size and location of the coagulation zone were determined, based on changes in the tissue a

Automatic landmark identification in cone-beam computed tomography.

To present and validate an open-source fully automated landmark placement (ALICBCT) tool for cone-beam computed tomography scans.

Automated vertebrae localization and identification by decision forests and image-based refinement on real-world CT data.

Development of a fully automatic algorithm for the automatic localization and identification of vertebral bodies in computed tomography (CT).


## Quote


Our computer-assisted system, W-Transformer, achieves a low SMAPE of 8.26% in Cobb angle detection.

TSFGDTDBN outperforms existing deep learning methods, delivering higher accuracy, lower error rates, and faster prediction times.


## Conclusion


Le framework de deep learning proposé, combinant modélisation duale des plateaux vertébraux, HRNet, Swin-Transformer et détection de courbure par SVD, permet une estimation de l'angle de Cobb plus précise et plus interprétable cliniquement que les méthodes existantes Le Vertebral Wedging Index (VWI) constitue une métrique complémentaire à l'angle de Cobb, capturant des déformations structurelles pronostiques que l'angle de Cobb traditionnel ne détecte pas Cette approche soutient la détection précoce de l'AIS, la planification de traitements personnalisés et le suivi de la progression de la maladie


## Insight


efficacy: Le modèle W-Transformer, conçu pour dépasser les limites des méthodes existantes basées sur les landmarks ou la segmentation, atteint un SMAPE global de 8,26% pour l'estimation de l'angle de Cobb à partir de radiographies.

clinical application: En combinant prétraitement d'image et extraction de caractéristiques avancée, le TSFGDTDBN réduit le temps nécessaire à la prédiction de l'ostéoporose, ce qui en fait un outil exploitable dans des systèmes d'aide à la décision clinique en temps réel pour optimiser l'évaluation de la santé osseuse.

conclusion: Les angles de Sharp, CE et Tönnis mesurés par le modèle de réseau de neurones convolutif basé sur le deep learning peuvent être utilisés avec une précision élevée pour le diagnostic de la DDH et de la BDDH, constituant un outil précieux d'aide aux radiologues.

efficacy: Le modèle TSFGDTDBN surpasse les méthodes d'apprentissage profond existantes (DenseNet201, VGG-19, ViT, Deep CNN) en offrant une précision plus élevée, des taux d'erreur plus faibles et des temps de prédiction plus rapides pour la détection de l'ostéoporose à partir d'images radiographiques.

efficacy: La TRDOT associée à l'algorithme de reconstruction SBDOT localise la frontière de photocoagulation avec une précision de ±1 mm par rapport à la référence (visualisation directe post-excision et/ou IRM), atteignant l'objectif de précision fixé pour la translation clinique, sur un ensemble d'expériences en fantômes, ex vivo et in vivo (modèle canin, N=6).

implications: Les auteurs suggèrent que l'estimation directe des angles de Cobb à partir des landmarks, plutôt qu'un calcul géométrique classique, pourrait accroître la robustesse au bruit de prédiction.
Actuellement, les angles de Cobb (MT, PT, TL/L) sont calculés à partir des landmarks prédits via un algorithme géométrique déterministe reposant sur la pente de chaque vertèbre, ce qui rend le calcul final directement sensible à toute erreur locale de prédiction des coins vertébraux. Les auteurs proposent, comme piste future, de remplacer cette étape géométrique par un modèle d'apprentissage capable d'estimer directement les angles à partir des landmarks (ou même de bout en bout), ce qui pourrait offrir une robustesse accrue face au bruit inhérent aux prédictions individuelles des landmarks et potentiellement combler l'écart de performance avec le meilleur score du leaderboard (21.71% vs 25.69% obtenu).

efficacy: Le framework proposé, combinant prédiction duale des angles des plateaux vertébraux et extraction de courbure par SVD, atteint 83,45% de précision diagnostique et 2,55° d'erreur absolue moyenne pour l'estimation de l'angle de Cobb sur une cohorte de 630 patients, surpassant les méthodes de référence Seg4Reg et VLTENet.


## Discussion


Les auteurs présentent W-Transformer, un système entièrement automatique de détection de repères vertébraux et de mesure de l'angle de Cobb, qui combine une architecture encodeur-décodeur avec un transformer pour capturer le contexte global, une branche de renforcement avec supervision intermédiaire pour limiter les chevauchements et détections manquées, et un module de prédiction amélioré pour affiner la localisation finale des repères. La corrélation de Pearson globale entre les angles estimés et la vérité terrain manuelle dépasse 0,9, avec des performances particulièrement élevées pour la région PT (0,9489, p < 0,001), suivie de la région TL (0,9149, p < 0,001) puis MT (0,8817, p < 0,001). Le modèle atteint une précision diagnostique globale de 0,9702 et une sensibilité de 0,9577 pour la scoliose, sans différence statistiquement significative avec la mesure manuelle (test t de Student apparié, p > 0,05). Comparé aux méthodes de l'état de l'art évaluées sur la même base AASCE MICCAI 2019, W-Transformer obtient un SMAPE de 8,26%, comparable ou supérieur à celui de méthodes utilisant un backbone similaire (ResNet18), tout en présentant une variabilité réduite (moins de 4°) et une distribution d'erreurs plus concentrée entre 0° et 5°. Les auteurs concluent que l'amélioration de la précision des repères vertébraux, plutôt que le recours à une ligne centrale rachidienne, constitue une stratégie plus fiable pour l'estimation de l'angle de Cobb, notamment chez les patients jeunes où la ligne centrale reste moins informative en cas de scoliose sévère.

La discussion souligne que le modèle TSFGDTDBN, fondé sur les réseaux de croyance profonde (DBN) comme modèles génératifs probabilistes, permet d'extraire des caractéristiques complexes et cachées à partir de données d'imagerie médicale de haute dimension pour la prédiction de l'ostéoporose. Les résultats expérimentaux montrent que ce modèle atteint une exactitude, une précision et un rappel élevés, tout en réduisant significativement le temps de prédiction de la maladie, ce qui le rend adapté à une intégration dans des systèmes d'aide à la décision clinique (CDSS) en temps réel. En conclusion, l'intégration d'étapes de prétraitement et d'une extraction de caractéristiques sophistiquée permet au TSFGDTDBN d'obtenir des prédictions plus rapides et plus précises que les méthodes d'apprentissage profond existantes, telles que DenseNet201, VGG-19, ViT et Deep CNN. Ce modèle apparaît ainsi comme un outil prometteur pour la détection précoce et la surveillance continue de l'ostéoporose, favorisant une intervention médicale rapide et un renforcement des soins préventifs, avec un minimum de ressources requises.


## Synthese


L'article situe le problème de l'estimation automatique de l'angle de Cobb dans le contexte du diagnostic de la scoliose, une déformation rachidienne dont l'évaluation manuelle sur radiographies souffre de variabilité inter- et intra-observateur. Les auteurs recensent deux grandes familles d'approches par apprentissage profond existantes : les méthodes fondées sur les landmarks, qui localisent les quatre coins de chaque vertèbre avant de calculer l'angle, et les méthodes fondées sur la segmentation, qui délimitent la colonne ou les vertèbres individuellement. Ils soulignent que les méthodes à base de landmarks se sont surtout concentrées sur l'amélioration de la prédiction des points anatomiques sans nécessairement optimiser l'estimation finale de l'angle de Cobb, tandis que les méthodes de segmentation, bien que parfois plus précises, exigent des images de haute qualité et généralisent mal. Cette analyse de la littérature motive la proposition du modèle W-Transformer, une architecture hybride basée sur les transformers, présentée comme une réponse aux limites combinées de ces deux approches.


## Methodologie


L'article situe le problème de l'estimation automatique de l'angle de Cobb dans le contexte du diagnostic de la scoliose, une déformation rachidienne dont l'évaluation manuelle sur radiographies souffre de variabilité inter- et intra-observateur. Les auteurs recensent deux grandes familles d'approches par apprentissage profond existantes : les méthodes fondées sur les landmarks, qui localisent les quatre coins de chaque vertèbre avant de calculer l'angle, et les méthodes fondées sur la segmentation, qui délimitent la colonne ou les vertèbres individuellement. Ils soulignent que les méthodes à base de landmarks se sont surtout concentrées sur l'amélioration de la prédiction des points anatomiques sans nécessairement optimiser l'estimation finale de l'angle de Cobb, tandis que les méthodes de segmentation, bien que parfois plus précises, exigent des images de haute qualité et généralisent mal. Cette analyse de la littérature motive la proposition du modèle W-Transformer, une architecture hybride basée sur les transformers, présentée comme une réponse aux limites combinées de ces deux approches.