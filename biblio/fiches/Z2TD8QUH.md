# Self‐Prompting Segment Anything Model for Few‐Shot Medical Image Segmentation



## Resume


Self‐Prompting Segment Anything Model for Few‐Shot Medical Image Segmentation

ABSTRACT
                  Segmenting unlabelled medical images with a minimal amount of labelled data is a daunting task due to the complex feature landscapes and the prevalent noise and artefacts characteristic of medical imaging processes. The SAM has showcased the potential of large‐scale image segmentation models for achieving zero‐shot generalisation across previously unseen objects. However, directly applying SAM to medical image segmentation without incorporating prior knowledge of the target task can lead to unsatisfactory results. To address this, we enhance SAM by integrating prior knowledge of medical image segmentation tasks. This enables it to quickly adapt to few‐shot medical image segmentation tasks while ensuring efficient parameter training. Our method employs an ensemble learning strategy to train a simple classifier, producing a coarse mask for each test image. Importantly, this coarse mask generates more accurate prompt points and boxes, thus improving SAM's capacity for prompt‐driven segmentation. Furthermore, to refine SAM's ability to produce more precise masks, we introduce the Isolated Noise Removal (INR) module, which efficiently removes noise from the coarse masks. In addition, our novel Multi‐point Automatic Prompt (MPAP) module is designed to independently generate multiple effective and evenly distributed point prompts based on these coarse masks. Additionally, we introduce an innovative knee joint dataset benchmark specifically for medical image segmentation, contributing further to the research field. Extensive evaluations on three benchmark datasets confirm the superior performance of our approach compared to existing methods, demonstrating its efficacy and significant progress in the domain of few‐shot medical image segmentation.

Self-prompting Large Vision Models for Few-Shot Medical Image Segmentation

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Segment anything model for few-shot medical image segmentation with domain tuning

Sam-Rsp: A New Few-Shot Segmentation Method Based on Segment Anything Model and Rough Segmentation Prompts

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

LoRA-Tuned Segment Anything Model for Few-Shot Polyp Segmentation in Colonoscopy Images

EviPrompt: A Training-Free Evidential Prompt Generation Method for Adapting Segment Anything Model in Medical Images

Few-Shot Adaptation of Training-Free Foundation Model for 3D Medical Image Segmentation

Hemo-FS-SAM2: Few-Shot Tuning on Hemorrhage Segmentation of Segment Anything Model 2

Reducing Reliance on Expensive Annotations in Medical Image Segmentation Via Diffusion Models and Segment Anything Model

Gray’s Anatomy for Segment Anything Model: Optimizing Grayscale Medical Images for Fast and Lightweight Segmentation

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

SAM-MPA: Applying SAM to Few-shot Medical Image Segmentation using Mask Propagation and Auto-prompting

Medical image segmentation often faces the challenge of prohibitively expensive annotation costs. While few-shot learning offers a promising solution to alleviate this burden, conventional approaches still rely heavily on pre-training with large volumes of labeled data from known categories. To address this issue, we propose leveraging the Segment Anything Model (SAM), pre-trained on over 1 billion masks, thus circumventing the need for extensive domain-specific annotated data. In light of this, we developed SAM-MPA, an innovative SAM-based framework for few-shot medical image segmentation using Mask Propagation-based Auto-prompting. Initially, we employ k-centroid clustering to select the most representative examples for labelling to construct the support set. These annotated examples are registered to other images yielding deformation fields that facilitate the propagation of the mask knowledge to obtain coarse masks across the dataset. Subsequently, we automatically generate visual

Few-shot Medical Image Segmentation with Cycle-resemblance Attention

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

Brain Tumor MRI Segmentation Method Based on Segment Anything Model

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

Volumetric medical image segmentation via fully 3D adaptation of Segment Anything Model

A probabilistic segment anything model for ambiguity‑aware medical image segmentation

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

SAM3D: zero-shot semi-automatic segmentation in 3D medical images with the segment anything model

Foundation Models for Biomedical Image Segmentation: A Survey

Self-learning and One-Shot Learning Based Single-Slice Annotation for 3D Medical Image Segmentation


## Methodologie


Cet article propose une méthode de self-prompting pour adapter le modèle de segmentation générique SAM (Segment Anything Model) au domaine médical dans un cadre few-shot, sans nécessiter le fine-tuning complet du modèle. L'approche repose sur l'insertion d'un simple classifieur linéaire pixel-wise, entraîné sur l'espace d'embedding de SAM, qui génère automatiquement des prompts (points et boîtes englobantes) à partir d'un masque grossier prédit, éliminant ainsi le besoin d'annotations interactives manuelles. Une étude d'ablation démontre la complémentarité des deux types de prompts : la boîte englobante apporte une information de taille et de position approximative, tandis que le point corrige les erreurs de localisation dues à des pixels mal classifiés, leur combinaison produisant les meilleurs résultats. Évaluée sur les jeux de données Kvasir-SEG et ISIC2018 avec seulement 20 images d'entraînement, la méthode surpasse les approches de fine-tuning existantes (MedSAM, SAMed) ainsi que SAM non-prompté, tout en réduisant le temps d'entraînement de plus de 30 minutes à environ 30 secondes.


## Synthese


Cet article propose une méthode de self-prompting pour adapter le modèle de segmentation générique SAM (Segment Anything Model) au domaine médical dans un cadre few-shot, sans nécessiter le fine-tuning complet du modèle. L'approche repose sur l'insertion d'un simple classifieur linéaire pixel-wise, entraîné sur l'espace d'embedding de SAM, qui génère automatiquement des prompts (points et boîtes englobantes) à partir d'un masque grossier prédit, éliminant ainsi le besoin d'annotations interactives manuelles. Une étude d'ablation démontre la complémentarité des deux types de prompts : la boîte englobante apporte une information de taille et de position approximative, tandis que le point corrige les erreurs de localisation dues à des pixels mal classifiés, leur combinaison produisant les meilleurs résultats. Évaluée sur les jeux de données Kvasir-SEG et ISIC2018 avec seulement 20 images d'entraînement, la méthode surpasse les approches de fine-tuning existantes (MedSAM, SAMed) ainsi que SAM non-prompté, tout en réduisant le temps d'entraînement de plus de 30 minutes à environ 30 secondes.


## Raw_Problem_Setup


Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).

Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).