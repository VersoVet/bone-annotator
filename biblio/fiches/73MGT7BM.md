# Segment Anything Model for Semi-Supervised Medical Image Segmentation via Selecting Reliable Pseudo-Labels



## Resume


Segment Anything Model for Semi-Supervised Medical Image Segmentation via Selecting Reliable Pseudo-Labels

Semi-supervised learning has become a hot topic due to its less dependence on annotated data compared to fully supervised methods. This advantage is more pronounced in the medical imaging field where obtaining labeled data is difficult. One of the most classic and intuitive methods in semi-supervised segmentation is to generate pseudo-labels for unlabeled images. However, this method can also introduce unreliable pseudo-labels that may provide incorrect guidance to the model and degrade its performance. The reliability of pseudo-labels is hard to assess due to the lack of ground truth labels for unlabeled images. In this paper, a SSL framework was presented, in which we proposed a simple but effective  strategy to select reliable pseudo-labels by leveraging the Segment Anything Model (SAM) for segmentation.  Concretely, the SSL model trained with domain knowledge provides the generated pseudo-labels as prompts to the SAM. Reliable pseudo-labels usually make SAM to conduct predictions c

Pseudo Label-based Multi-View Annotation for Semi-Supervised Medical Image Segmentation

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

Volumetric medical image segmentation via fully 3D adaptation of Segment Anything Model

Segment anything model for few-shot medical image segmentation with domain tuning

Reducing Reliance on Expensive Annotations in Medical Image Segmentation Via Diffusion Models and Segment Anything Model

SAM-guided Cross Pseudo Supervision Learning for Semi-supervised Medical Image Segmentation.

Precise identification of lesions in medical images is crucial for accurate diagnosis and successful treatment. Nevertheless, the limited availability of annotations, coupled with the intricate nature of lesion characteristics, imposes significant constraints on the model's representational capacity. The recently developed vision foundation model, Segment Anything Model (SAM), featuring its unique capability for prompt interaction, has demonstrated remarkable capabilities in natural image segmentation. However, it encounters performance degradation in medical scenarios due to the absence of domain-specific medical knowledge. To address the aforementioned issues, we propose a novel SAM-assisted semi-supervised framework for accurate lesion segmentation, even in scenarios with extremely limited annotations. Concretely, our approach adopts a dual-branch architecture, where each branch incorporates a SAM (ViT-Base) model fine-tuned with adapters. We further design a point prompts generator

SamDSK: Combining Segment Anything Model with Domain-Specific Knowledge for Semi-Supervised Learning in Medical Image Segmentation

The Segment Anything Model (SAM) exhibits a capability to segment a wide array of objects in natural images, serving as a versatile perceptual tool for various downstream image segmentation tasks. In contrast, medical image segmentation tasks often rely on domain-specific knowledge (DSK). In this paper, we propose a novel method that combines the segmentation foundation model (i.e., SAM) with domain-specific knowledge for reliable utilization of unlabeled images in building a medical image segmentation model. Our new method is iterative and consists of two main stages: (1) segmentation model training; (2) expanding the labeled set by using the trained segmentation model, an unlabeled set, SAM, and domain-specific knowledge. These two stages are repeated until no more samples are added to the labeled set. A novel optimal-matching-based method is developed for combining the SAM-generated segmentation proposals and pixel-level and image-level DSK for constructing annotations of unlabeled

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

A probabilistic segment anything model for ambiguity‑aware medical image segmentation

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

Learning Weakly Supervised Semantic Segmentation Through Cross-Supervision and Contrasting of Pixel-Level Pseudo-Labels

Customized Segment Anything Model for Medical Image Segmentation

We propose SAMed, a general solution for medical image segmentation. Different from the previous methods, SAMed is built upon the large-scale image segmentation model, Segment Anything Model (SAM), to explore the new research paradigm of customizing large-scale models for medical image segmentation. SAMed applies the low-rank-based (LoRA) finetuning strategy to the SAM image encoder and finetunes it together with the prompt encoder and the mask decoder on labeled medical image segmentation datasets. We also observe the warmup finetuning strategy and the AdamW optimizer lead SAMed to successful convergence and lower loss. Different from SAM, SAMed could perform semantic segmentation on medical images. Our trained SAMed model achieves 81.88 DSC and 20.64 HD on the Synapse multi-organ segmentation dataset, which is on par with the state-of-the-art methods. We conduct extensive experiments to validate the effectiveness of our design. Since SAMed only updates a small fraction of the SAM par

Learning with Limited Annotations: A Survey on Deep Semi-Supervised Learning for Medical Image Segmentation

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

Rethinking Semi-Supervised Medical Image Segmentation: A Variance-Reduction Perspective

Medical Image Segmentation Foundation Models. CVPR 2024 Challenge: Segment Anything in Medical Images on Laptop

S-SAM: SVD-based Fine-Tuning of Segment Anything Model for Medical Image Segmentation

Medical image segmentation has been traditionally approached by training or fine-tuning the entire model to cater to any new modality or dataset. However, this approach often requires tuning a large number of parameters during training. With the introduction of the Segment Anything Model (SAM) for prompted segmentation of natural images, many efforts have been made towards adapting it efficiently for medical imaging, thus reducing the training time and resources. However, these methods still require expert annotations for every image in the form of point prompts or bounding box prompts during training and inference, making it tedious to employ them in practice. In this paper, we propose an adaptation technique, called S-SAM, that only trains parameters equal to 0.4% of SAM's parameters and at the same time uses simply the label names as prompts for producing precise masks. This not only makes tuning SAM more efficient than the existing adaptation methods but also removes the burden of

Cross Prompting Consistency with Segment Anything Model for Semi-supervised Medical Image Segmentation

Semi-supervised learning (SSL) has achieved notable progress in medical image segmentation. To achieve effective SSL, a model needs to be able to efficiently learn from limited labeled data and effectively exploiting knowledge from abundant unlabeled data. Recent developments in visual foundation models, such as the Segment Anything Model (SAM), have demonstrated remarkable adaptability with improved sample efficiency. To harness the power of foundation models for application in SSL, we propose a cross prompting consistency method with segment anything model (CPC-SAM) for semi-supervised medical image segmentation. Our method employs SAM's unique prompt design and innovates a cross-prompting strategy within a dual-branch framework to automatically generate prompts and supervisions across two decoder branches, enabling effectively learning from both scarce labeled and valuable unlabeled data. We further design a novel prompt consistency regularization, to reduce the prompt position sens

Iterative Confidence-Based Pseudo-Labeling for Semi-Supervised Lung Cancer Segmentation Under Annotation Scarcity

Efficient Medical Segmentation Anything Model for Robust Lightweight Segmentation under Imperfect Data in Embedded Healthcare.

Healthcare Industry 5.0 is accelerating the deployment of medical imaging intelligence on embedded and edge devices, where medical data are often imperfect due to acquisition noise, low-contrast regions, and boundary ambiguity, while computational budgets remain tight. Although the Segment Anything Model (SAM) provides promptable segmentation, its heavy encoder hinders edge deployment and its zero-shot behavior can be unreliable for specialized medical imaging scenarios. This paper presents an efficient and lightweight medical image segmentation pipeline tailored for embedded healthcare systems. We replace the SAM image encoder with an Efficient Vision Transformer (EfficientViT) backbone and introduce offline knowledge distillation to transfer domain-aware feature representations from the Medical Segment Anything Model (MedSAM) to a compact student network. To emulate imperfect supervision in practical use, bounding-box prompts are generated from ground truth masks with random per-side


## Conclusion


SamDSK, une nouvelle méthode d'apprentissage semi-supervisé, utilise le Segment Anything Model (SAM) pour entraîner un modèle de segmentation d'images médicales SAM est utilisé dans un système d'appariement optimal proposé pour sélectionner et affiner les prédictions de segmentation des images non étiquetées Ce travail initie une nouvelle direction pour l'apprentissage semi-supervisé en segmentation d'images médicales, où le modèle de segmentation fondation peut être exploité comme un outil précieux


## Discussion


Cette conclusion présente SamDSK, une nouvelle méthode d'apprentissage semi-supervisé pour la segmentation d'images médicales, qui exploite le Segment Anything Model (SAM) au sein d'un système d'appariement optimal chargé de sélectionner et d'affiner les prédictions de segmentation issues d'images non étiquetées. La méthode repose sur une procédure itérative multi-tours combinant entraînement du modèle de segmentation et expansion progressive de l'ensemble étiqueté, ce qui permet d'améliorer graduellement le modèle cible tout en enrichissant le jeu de données d'entraînement. Les expériences menées sur trois jeux de données, en comparaison avec plusieurs méthodes de SSL récentes, confirment l'efficacité et les avantages de SamDSK. Les auteurs identifient comme perspective de recherche future l'extension de SamDSK à d'autres modalités d'imagerie médicale et à d'autres scénarios de segmentation.