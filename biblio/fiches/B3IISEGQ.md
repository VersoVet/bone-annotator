# Sam-Rsp: A New Few-Shot Segmentation Method Based on Segment Anything Model and Rough Segmentation Prompts



## Resume


Sam-Rsp: A New Few-Shot Segmentation Method Based on Segment Anything Model and Rough Segmentation Prompts

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Self‐Prompting Segment Anything Model for Few‐Shot Medical Image Segmentation

ABSTRACT
                  Segmenting unlabelled medical images with a minimal amount of labelled data is a daunting task due to the complex feature landscapes and the prevalent noise and artefacts characteristic of medical imaging processes. The SAM has showcased the potential of large‐scale image segmentation models for achieving zero‐shot generalisation across previously unseen objects. However, directly applying SAM to medical image segmentation without incorporating prior knowledge of the target task can lead to unsatisfactory results. To address this, we enhance SAM by integrating prior knowledge of medical image segmentation tasks. This enables it to quickly adapt to few‐shot medical image segmentation tasks while ensuring efficient parameter training. Our method employs an ensemble learning strategy to train a simple classifier, producing a coarse mask for each test image. Importantly, this coarse mask generates more accurate prompt points and boxes, thus improving SAM's capacity for prompt‐driven segmentation. Furthermore, to refine SAM's ability to produce more precise masks, we introduce the Isolated Noise Removal (INR) module, which efficiently removes noise from the coarse masks. In addition, our novel Multi‐point Automatic Prompt (MPAP) module is designed to independently generate multiple effective and evenly distributed point prompts based on these coarse masks. Additionally, we introduce an innovative knee joint dataset benchmark specifically for medical image segmentation, contributing further to the research field. Extensive evaluations on three benchmark datasets confirm the superior performance of our approach compared to existing methods, demonstrating its efficacy and significant progress in the domain of few‐shot medical image segmentation.

Boosting Few-Shot Semantic Segmentation Via Segment Anything Model

In semantic segmentation, accurate prediction masks are crucial for downstream tasks such as medical image analysis and image editing. Due to the lack of annotated data, few-shot semantic segmentation (FSS) performs poorly in predicting masks with precise contours. Recently, we have noticed that the large foundation model segment anything model (SAM) performs well in processing detailed features. Inspired by SAM, we propose FSS-SAM to boost FSS methods by addressing the issue of inaccurate contour. The FSS-SAM is training-free. It works as a post-processing tool for any FSS methods and can improve the accuracy of predicted masks. Specifically, we use predicted masks from FSS methods to generate prompts and then use SAM to predict new masks. To avoid predicting wrong masks with SAM, we propose a prediction result selection (PRS) algorithm. The algorithm can remarkably decrease wrong predictions. Experiment results on public datasets show that our method is superior to base FSS methods i

Hemo-FS-SAM2: Few-Shot Tuning on Hemorrhage Segmentation of Segment Anything Model 2

Unlocking the Power of SAM 2 for Few-Shot Segmentation

A Survey on Segment Anything Model (SAM): Vision Foundation Model Meets Prompt Engineering

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

SAM-MPA: Applying SAM to Few-shot Medical Image Segmentation using Mask Propagation and Auto-prompting

Medical image segmentation often faces the challenge of prohibitively expensive annotation costs. While few-shot learning offers a promising solution to alleviate this burden, conventional approaches still rely heavily on pre-training with large volumes of labeled data from known categories. To address this issue, we propose leveraging the Segment Anything Model (SAM), pre-trained on over 1 billion masks, thus circumventing the need for extensive domain-specific annotated data. In light of this, we developed SAM-MPA, an innovative SAM-based framework for few-shot medical image segmentation using Mask Propagation-based Auto-prompting. Initially, we employ k-centroid clustering to select the most representative examples for labelling to construct the support set. These annotated examples are registered to other images yielding deformation fields that facilitate the propagation of the mask knowledge to obtain coarse masks across the dataset. Subsequently, we automatically generate visual

Self-prompting Large Vision Models for Few-Shot Medical Image Segmentation

Part-aware Prompted Segment Anything Model for Adaptive Segmentation

Precision medicine, such as patient-adaptive treatments assisted by medical image analysis, poses new challenges for segmentation algorithms in adapting to new patients, due to the large variability across different patients and the limited availability of annotated data for each patient. In this work, we propose a data-efficient segmentation algorithm, namely Part-aware Prompted Segment Anything Model ($P^2SAM$). Without any model fine-tuning, $P^2SAM$ enables seamless adaptation to any new patients relying only on one-shot patient-specific data. We introduce a novel part-aware prompt mechanism to select multiple-point prompts based on the part-level features of the one-shot data, which can be extensively integrated into different promptable segmentation models, such as SAM and SAM 2. Moreover, to determine the optimal number of parts for each specific case, we propose a distribution-guided retrieval approach that further enhances the robustness of the part-aware prompt mechanism. $P^

LoRA-Tuned Segment Anything Model for Few-Shot Polyp Segmentation in Colonoscopy Images

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

Prompt Once, Segment Everything: Leveraging SAM 2 Potential for Infinite Medical Image Segmentation with a Single Prompt

Semantic segmentation of medical images holds significant potential for enhancing diagnostic and surgical procedures. Radiology specialists can benefit from automated segmentation tools that facilitate identifying and isolating regions of interest in medical scans. Nevertheless, to obtain precise results, sophisticated deep learning models tailored to this specific task must be developed and trained, a capability not universally accessible. Segment Anything Model (SAM) 2 is a foundational model designed for image and video segmentation tasks, built on its predecessor, SAM. This paper introduces a novel approach leveraging SAM 2’s video segmentation capabilities to reduce the prompts required to segment an entire volume of medical images. The study first compares SAM and SAM 2’s performance in medical image segmentation. Evaluation metrics such as the Jaccard index and Dice score are used to measure precision and segmentation quality. Then, our novel approach is introduced. Statistical

Prompt-SAM: A Vision-Language and SAM based Hybrid Framework for Prompt-Augmented Zero-Shot Segmentation

Abstract Recent advancements in deep learning have greatly improved computer vision tasks like object detection, image classification, and segmentation. Despite these successes, traditional supervised learning methods still depend on large annotated datasets, which are often expensive and time consuming to create. To overcome this limitation, we present a zero-shot segmentation framework that combines the strengths of CLIP (Contrastive Language-Image Pretraining), its segmentation-focused variant CLIPSeg, and the Segment Anything Model (SAM). This approach first uses the zero-shot classification ability of CLIP or CLIPSeg to produce initial segmentation cues. These cues, such as point and box prompts, are then refined by SAM to generate accurate segmentation masks. Using this prompt-based strategy, the system can perform segmentation without requiring labeled data, making it suitable for a wide range of domains, including both natural scenes and medical imaging. Our experiments on benc

AGSAM: Agent-Guided Segment Anything Model for Automatic Segmentation in Few-Shot Scenarios

Precise medical image segmentation of regions of interest (ROIs) is crucial for accurate disease diagnosis and progression assessment. However, acquiring high-quality annotated data at the pixel level poses a significant challenge due to the resource-intensive nature of this process. This scarcity of high-quality annotated data results in few-shot scenarios, which are highly prevalent in clinical applications. To address this obstacle, this paper introduces Agent-Guided SAM (AGSAM), an innovative approach that transforms the Segment Anything Model (SAM) into a fully automated segmentation method by automating prompt generation. Capitalizing on the pre-trained feature extraction and decoding capabilities of SAM-Med2D, AGSAM circumvents the need for manual prompt engineering, ensuring adaptability across diverse segmentation methods. Furthermore, the proposed feature augmentation convolution module (FACM) enhances model accuracy by promoting stable feature representations. Experimental evaluations demonstrate AGSAM’s consistent superiority over other methods across various metrics. These findings highlight AGSAM’s efficacy in tackling the challenges associated with limited annotated data while achieving high-quality medical image segmentation.

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

Rethinking Few-Shot Medical Image Segmentation by SAM2: A Training-Free Framework with Augmentative Prompting and Dynamic Matching

The reliance on large labeled datasets presents a significant challenge in medical image segmentation. Few-shot learning offers a potential solution, but existing methods often still require substantial training data. This paper proposes a novel approach that leverages the Segment Anything Model 2 (SAM2), a vision foundation model with strong video segmentation capabilities. We conceptualize 3D medical image volumes as video sequences, departing from the traditional slice-by-slice paradigm. Our core innovation is a support-query matching strategy: we perform extensive data augmentation on a single labeled support image and, for each frame in the query volume, algorithmically select the most analogous augmented support image. This selected image, along with its corresponding mask, is used as a mask prompt, driving SAM2's video segmentation. This approach entirely avoids model retraining or parameter updates. We demonstrate state-of-the-art performance on benchmark few-shot medical image

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Enhancing the Reliability of Segment Anything Model for Auto-Prompting Medical Image Segmentation with Uncertainty Rectification

The Segment Anything Model (SAM) has recently emerged as a groundbreaking foundation model for prompt-driven image segmentation tasks. However, both the original SAM and its medical variants require slice-by-slice manual prompting of target structures, which directly increase the burden for applications. Despite attempts of auto-prompting to turn SAM into a fully automatic manner, it still exhibits subpar performance and lacks of reliability especially in the field of medical imaging. In this paper, we propose UR-SAM, an uncertainty rectified SAM framework to enhance the reliability for auto-prompting medical image segmentation. Building upon a localization framework for automatic prompt generation, our method incorporates a prompt augmentation module to obtain a series of input prompts for SAM for uncertainty estimation and an uncertainty-based rectification module to further utilize the distribution of estimated uncertainty to improve the segmentation performance. Extensive experimen


## Raw_Discussion


Few-shot methods in medical image segmentation often struggle with the need for large amounts of annotated data for pre-training. To address this issue, we propose the SAM-MPA framework, which leverages SAM for few-shot segmentation of medical images, effectively circumventing the demand for extensive labeled data. By automatically generating high-quality prompts for SAM, we successfully unlock its potential, achieving impressive segmentation results with just a handful of annotated samples (1, 5, or 10 masked images).

Few-shot methods in medical image segmentation often struggle with the need for large amounts of annotated data for pre-training. To address this issue, we propose the SAM-MPA framework, which leverages SAM for few-shot segmentation of medical images, effectively circumventing the demand for extensive labeled data. By automatically generating high-quality prompts for SAM, we successfully unlock its potential, achieving impressive segmentation results with just a handful of annotated samples (1, 5, or 10 masked images).


## Raw_Introduction


In response to the issue, the Segment Anything Model (SAM [11]) has recently emerged as a promising approach. Trained on over 1 billion masks, SAM demonstrates a powerful generalized few shot segmentation capability, able to segment any subject using visual prompts, even those hasn't seen before. Several studies have already applied SAM to medical imaging, yielding promising segmentation results [2,12,13,24,26]. They primarily focus on fine-tuning SAM and manually providing prompts. However, there are two significant challenges. (1) Fine-tuning methods typically require anywhere from hundreds [12,24,26] to millions [2,13] of masked training images. In contrast, FSS aims to achieve satisfactory segmentation performance on medical images using only a handful of masked samples (typically 1, 5, or 10 instances). ( 2) The practice of manually supplying prompts is labor-intensive and highly inefficient. Given these considerations, we propose to explore the application of SAM for FSS using au

In response to the issue, the Segment Anything Model (SAM [11]) has recently emerged as a promising approach. Trained on over 1 billion masks, SAM demonstrates a powerful generalized few shot segmentation capability, able to segment any subject using visual prompts, even those hasn't seen before. Several studies have already applied SAM to medical imaging, yielding promising segmentation results [2,12,13,24,26]. They primarily focus on fine-tuning SAM and manually providing prompts. However, there are two significant challenges. (1) Fine-tuning methods typically require anywhere from hundreds [12,24,26] to millions [2,13] of masked training images. In contrast, FSS aims to achieve satisfactory segmentation performance on medical images using only a handful of masked samples (typically 1, 5, or 10 instances). ( 2) The practice of manually supplying prompts is labor-intensive and highly inefficient. Given these considerations, we propose to explore the application of SAM for FSS using au


## Discussion


Cette conclusion présente SamDSK, une nouvelle méthode d'apprentissage semi-supervisé pour la segmentation d'images médicales, qui exploite le Segment Anything Model (SAM) au sein d'un système d'appariement optimal chargé de sélectionner et d'affiner les prédictions de segmentation issues d'images non étiquetées. La méthode repose sur une procédure itérative multi-tours combinant entraînement du modèle de segmentation et expansion progressive de l'ensemble étiqueté, ce qui permet d'améliorer graduellement le modèle cible tout en enrichissant le jeu de données d'entraînement. Les expériences menées sur trois jeux de données, en comparaison avec plusieurs méthodes de SSL récentes, confirment l'efficacité et les avantages de SamDSK. Les auteurs identifient comme perspective de recherche future l'extension de SamDSK à d'autres modalités d'imagerie médicale et à d'autres scénarios de segmentation.


## Methodologie


Cet article propose une méthode de self-prompting pour adapter le modèle de segmentation générique SAM (Segment Anything Model) au domaine médical dans un cadre few-shot, sans nécessiter le fine-tuning complet du modèle. L'approche repose sur l'insertion d'un simple classifieur linéaire pixel-wise, entraîné sur l'espace d'embedding de SAM, qui génère automatiquement des prompts (points et boîtes englobantes) à partir d'un masque grossier prédit, éliminant ainsi le besoin d'annotations interactives manuelles. Une étude d'ablation démontre la complémentarité des deux types de prompts : la boîte englobante apporte une information de taille et de position approximative, tandis que le point corrige les erreurs de localisation dues à des pixels mal classifiés, leur combinaison produisant les meilleurs résultats. Évaluée sur les jeux de données Kvasir-SEG et ISIC2018 avec seulement 20 images d'entraînement, la méthode surpasse les approches de fine-tuning existantes (MedSAM, SAMed) ainsi que SAM non-prompté, tout en réduisant le temps d'entraînement de plus de 30 minutes à environ 30 secondes.

Cette étude constitue la première synthèse exhaustive consacrée au Segment Anything Model (SAM), un modèle de fondation pour la segmentation d'images conçu selon le paradigme des grands modèles de langage pré-entraînés, capables de généralisation zero-shot et few-shot via l'ingénierie de prompts. Les auteurs y examinent les trois composantes fondatrices ayant permis le succès de SAM — la tâche de pré-entraînement, l'architecture du modèle et les données d'entraînement à grande échelle — en s'appuyant sur des travaux antérieurs tels que CLIP et ALIGN, qui ont démontré la faisabilité d'encodeurs vision-langage alignés par apprentissage contrastif. L'architecture de SAM repose sur un encodeur d'image de forte capacité produisant une représentation interrogeable de manière efficace par divers types de prompts, générant des masques d'objets à une vitesse quasi temps réel, y compris plusieurs masques valides assortis de scores de confiance en cas de prompts ambigus. Par ailleurs, la synthèse relève que les méthodes fondées sur NeRF demeurent limitées par leur coût computationnel et leur empreinte mémoire élevés, freinant leur passage à l'échelle pour la compréhension de scènes 3D de grande taille, et identifie l'amélioration de leur efficacité comme une piste de recherche prioritaire pour la compréhension de scènes en temps réel.


## Synthese


Cet article propose une méthode de self-prompting pour adapter le modèle de segmentation générique SAM (Segment Anything Model) au domaine médical dans un cadre few-shot, sans nécessiter le fine-tuning complet du modèle. L'approche repose sur l'insertion d'un simple classifieur linéaire pixel-wise, entraîné sur l'espace d'embedding de SAM, qui génère automatiquement des prompts (points et boîtes englobantes) à partir d'un masque grossier prédit, éliminant ainsi le besoin d'annotations interactives manuelles. Une étude d'ablation démontre la complémentarité des deux types de prompts : la boîte englobante apporte une information de taille et de position approximative, tandis que le point corrige les erreurs de localisation dues à des pixels mal classifiés, leur combinaison produisant les meilleurs résultats. Évaluée sur les jeux de données Kvasir-SEG et ISIC2018 avec seulement 20 images d'entraînement, la méthode surpasse les approches de fine-tuning existantes (MedSAM, SAMed) ainsi que SAM non-prompté, tout en réduisant le temps d'entraînement de plus de 30 minutes à environ 30 secondes.

Cette étude constitue la première synthèse exhaustive consacrée au Segment Anything Model (SAM), un modèle de fondation pour la segmentation d'images conçu selon le paradigme des grands modèles de langage pré-entraînés, capables de généralisation zero-shot et few-shot via l'ingénierie de prompts. Les auteurs y examinent les trois composantes fondatrices ayant permis le succès de SAM — la tâche de pré-entraînement, l'architecture du modèle et les données d'entraînement à grande échelle — en s'appuyant sur des travaux antérieurs tels que CLIP et ALIGN, qui ont démontré la faisabilité d'encodeurs vision-langage alignés par apprentissage contrastif. L'architecture de SAM repose sur un encodeur d'image de forte capacité produisant une représentation interrogeable de manière efficace par divers types de prompts, générant des masques d'objets à une vitesse quasi temps réel, y compris plusieurs masques valides assortis de scores de confiance en cas de prompts ambigus. Par ailleurs, la synthèse relève que les méthodes fondées sur NeRF demeurent limitées par leur coût computationnel et leur empreinte mémoire élevés, freinant leur passage à l'échelle pour la compréhension de scènes 3D de grande taille, et identifie l'amélioration de leur efficacité comme une piste de recherche prioritaire pour la compréhension de scènes en temps réel.


## Conclusion


SamDSK, une nouvelle méthode d'apprentissage semi-supervisé, utilise le Segment Anything Model (SAM) pour entraîner un modèle de segmentation d'images médicales SAM est utilisé dans un système d'appariement optimal proposé pour sélectionner et affiner les prédictions de segmentation des images non étiquetées Ce travail initie une nouvelle direction pour l'apprentissage semi-supervisé en segmentation d'images médicales, où le modèle de segmentation fondation peut être exploité comme un outil précieux