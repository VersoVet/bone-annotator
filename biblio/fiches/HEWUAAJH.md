# RepViT-MedSAM: Efficient Segment Anything in the Medical Images



## Resume


RepViT-MedSAM: Efficient Segment Anything in the Medical Images

Rep-MedSAM: Towards Real-Time and Universal Medical Image Segmentation

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

ExpertsMedSAM: Faster Medical Image Segment Anything with Mixture-of-Experts

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

Efficient Medical Segmentation Anything Model for Robust Lightweight Segmentation under Imperfect Data in Embedded Healthcare.

Healthcare Industry 5.0 is accelerating the deployment of medical imaging intelligence on embedded and edge devices, where medical data are often imperfect due to acquisition noise, low-contrast regions, and boundary ambiguity, while computational budgets remain tight. Although the Segment Anything Model (SAM) provides promptable segmentation, its heavy encoder hinders edge deployment and its zero-shot behavior can be unreliable for specialized medical imaging scenarios. This paper presents an efficient and lightweight medical image segmentation pipeline tailored for embedded healthcare systems. We replace the SAM image encoder with an Efficient Vision Transformer (EfficientViT) backbone and introduce offline knowledge distillation to transfer domain-aware feature representations from the Medical Segment Anything Model (MedSAM) to a compact student network. To emulate imperfect supervision in practical use, bounding-box prompts are generated from ground truth masks with random per-side

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

An efficient segment anything model for the segmentation of medical images.

This paper introduces the efficient medical-images-aimed segment anything model (EMedSAM), addressing the high computational demands and limited adaptability of using SAM for medical image segmentation tasks. We present a novel, compact image encoder, DD-TinyViT, designed to enhance segmentation efficiency through an innovative parameter tuning method called med-adapter. The lightweight DD-TinyViT encoder is derived from the well-known ViT-H using a decoupled distillation approach.The segmentation and recognition capabilities of EMedSAM for specific structures are improved by med-adapter, which dynamically adjusts the model parameters specifically for medical imaging. We conducted extensive testing on EMedSAM using the public FLARE 2022 dataset and datasets from the First Hospital of Zhejiang University School of Medicine. The results demonstrate that our model outperforms existing state-of-the-art models in both multi-organ and lung segmentation tasks.

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

Embedded framework for clinical medical image segment anything in resource limited healthcare regions.

The emergence of portable imaging devices improves medical image acquisition efficiency in resource-limited regions, but a shortage of medical personnel still limits timely diagnosis. We propose Embed-MedSAM, a fully automatic segmentation model with low deployment cost. Built on MedSAM, it integrates a lightweight RepViT encoder to reduce computation and applies two-stage distillation on over one million multimodal medical images to preserve the original model's visual representation. A self-prompting mechanism is also introduced, where the model generates pseudo labels to guide fine-grained segmentation. The training jointly optimizes KL divergence and segmentation losses to improve accuracy under prompt-free conditions. Embed-MedSAM shows excellent performance on 17 benchmark datasets covering 7 imaging modalities. Without external prompts, it improves average Dice score by nearly 16% over the second-best model. It also runs at nearly 30 FPS on iPhone 14, showing strong potential fo

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

Swin-LiteMedSAM: A Lightweight Box-Based Segment Anything Model for Large-Scale Medical Image Datasets

Medical imaging is essential for the diagnosis and treatment of diseases, with medical image segmentation as a subtask receiving high attention. However, automatic medical image segmentation models are typically task-specific and struggle to handle multiple scenarios, such as different imaging modalities and regions of interest. With the introduction of the Segment Anything Model (SAM), training a universal model for various clinical scenarios has become feasible. Recently, several Medical SAM (MedSAM) methods have been proposed, but these models often rely on heavy image encoders to achieve high performance, which may not be practical for real-world applications due to their high computational demands and slow inference speed. To address this issue, a lightweight version of the MedSAM (LiteMedSAM) can provide a viable solution, achieving high performance while requiring fewer resources and less time. In this work, we introduce Swin-LiteMedSAM, a new variant of LiteMedSAM. This model i

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

SAM3D: zero-shot semi-automatic segmentation in 3D medical images with the segment anything model

MedCLIP-SAM: Bridging Text and Image Towards Universal Medical Image Segmentation

LiteWaveRep-MedSAM: a lightweight medical image segmentation model based on wavelet transform and reparameterization.

As a representative of large-scale general medical image segmentation models, MedSAM's massive parameters incur high computational costs, severely limiting its real-time clinical deployment on mobile and edge devices. To address this challenge, this paper proposes LiteWaveRep-MedSAM-a lightweight, efficient model tailored for mobile deployment. Based on RepViT, it employs macro-level restructuring and incorporates improved wavelet transform and half-convolution techniques to construct the efficient and lightweight visual encoder LiteWaveRepViT. This design significantly reduces computational complexity while ensuring effective extraction of image details and efficient interaction of features. In the decoder, we designed multi-scale channel-adaptive reverse convolutions that achieve high-quality upsampling by solving a regularized least-squares problem in closed form. Thanks to these designs, LiteWaveRep-MedSAM's model parameters have been compressed to6.80Mand computational cost has be

Segment Anything in Medical Images with nnUNet

Refsam: Efficiently Adapting Segmenting Anything Model for Referring Video Object Segmentation

ProtoSAM-3D: Interactive semantic segmentation in volumetric medical imaging via a Segment Anything Model and mask-level prototypes

Gray’s Anatomy for Segment Anything Model: Optimizing Grayscale Medical Images for Fast and Lightweight Segmentation

Medical SAM 2: Segment medical images as video via Segment Anything Model 2

Medical image segmentation plays a pivotal role in clinical diagnostics and treatment planning, yet existing models often face challenges in generalization and in handling both 2D and 3D data uniformly. In this paper, we introduce Medical SAM 2 (MedSAM-2), a generalized auto-tracking model for universal 2D and 3D medical image segmentation. The core concept is to leverage the Segment Anything Model 2 (SAM2) pipeline to treat all 2D and 3D medical segmentation tasks as a video object tracking problem. To put it into practice, we propose a novel \emph{self-sorting memory bank} mechanism that dynamically selects informative embeddings based on confidence and dissimilarity, regardless of temporal order. This mechanism not only significantly improves performance in 3D medical image segmentation but also unlocks a \emph{One-Prompt Segmentation} capability for 2D images, allowing segmentation across multiple images from a single prompt without temporal relationships. We evaluated MedSAM-2 on

Segment anything model for medical images?

The Segment Anything Model (SAM) is the first foundation model for general image segmentation. It has achieved impressive results on various natural image segmentation tasks. However, medical image segmentation (MIS) is more challenging because of the complex modalities, fine anatomical structures, uncertain and complex object boundaries, and wide-range object scales. To fully validate SAM's performance on medical data, we collected and sorted 53 open-source datasets and built a large medical segmentation dataset with 18 modalities, 84 objects, 125 object-modality paired targets, 1050K 2D images, and 6033K masks. We comprehensively analyzed different models and strategies on the so-called COSMOS 1050K dataset. Our findings mainly include the following: (1) SAM showed remarkable performance in some specific objects but was unstable, imperfect, or even totally failed in other situations. (2) SAM with the large ViT-H showed better overall performance than that with the small ViT-B. (3) SA


## Synthese


L'étude vise à améliorer l'efficacité computationnelle et l'adaptabilité du Segment Anything Model (SAM) pour la segmentation d'images médicales, en développant un encodeur d'image léger (DD-TinyViT) et un mécanisme d'adaptation de paramètres (med-adapter) intégrés dans un nouveau modèle nommé EMedSAM.

Cet article de Scientific Reports (2024) répond au défi de l'efficacité computationnelle et de la précision du Segment Anything Model (SAM) appliqué aux images médicales, un domaine où SAM standard sous-performe en conditions zero-shot par rapport à des modèles spécialisés comme MedSAM. Les auteurs proposent EMedSAM, une architecture combinant deux innovations: DD-TinyViT, un encodeur d'image léger (21M paramètres contre 632M pour le ViT-H original de SAM) obtenu par distillation découplée sur le jeu de données SA-1B, et le med-adapter, un mécanisme d'adaptation de paramètres inséré entre l'encodeur et le décodeur pour ajuster dynamiquement le modèle aux spécificités des images médicales. Le modèle a été évalué sur quatre jeux de données couvrant différentes modalités d'imagerie (scanner CT pulmonaire, mammographie X-ray, IRM cérébrale, segmentation abdominale multi-organes), incluant des données propres au First Hospital of Zhejiang University School of Medicine. Les résultats montrent qu'EMedSAM atteint des performances état de l'art sur 13 organes du jeu de données FLARE 2022 et sur la segmentation pulmonaire, l'encodeur léger n'entraînant pas de perte de précision significative tandis que la combinaison encodeur léger et med-adapter produit un effet synergique supérieur à chaque composant pris isolément. Les auteurs concluent qu'EMedSAM offre un compromis efficacité-précision meilleur que SAM et MedSAM, avec une généralisation robuste à travers les modalités et tâches de segmentation médicale testées.

L'article présente Segment Anything Model (SAM), un modèle de segmentation promptable reposant sur trois composants (encodeur d'image ViT préentraîné par autoencodeur masqué, encodeur de prompts dense/épars, et décodeur de masques) et entraîné sur plus d'un milliard de masques issus de 11 millions d'images naturelles. Les auteurs évaluent deux variantes de taille (ViT-B et ViT-H) sur un large jeu de données médicales, COSMOS 1050K, en modes automatique et par prompt. Une évaluation multi-round comparant SAM à des méthodes interactives dédiées (FocalClick, SimpleClick) révèle que SAM excelle lors de la première interaction mais que sa capacité d'amélioration itérative reste limitée sur les images médicales. Un finetuning ciblé du décodeur de masques sur 45 objets médicaux typiques, avec encodeur d'image et encodeur de prompts gelés, améliore les performances de segmentation pour la majorité des objets testés, plus nettement pour ViT-H que pour ViT-B.


## Methodologie


L'article présente Segment Anything Model (SAM), un modèle de segmentation promptable reposant sur trois composants (encodeur d'image ViT préentraîné par autoencodeur masqué, encodeur de prompts dense/épars, et décodeur de masques) et entraîné sur plus d'un milliard de masques issus de 11 millions d'images naturelles. Les auteurs évaluent deux variantes de taille (ViT-B et ViT-H) sur un large jeu de données médicales, COSMOS 1050K, en modes automatique et par prompt. Une évaluation multi-round comparant SAM à des méthodes interactives dédiées (FocalClick, SimpleClick) révèle que SAM excelle lors de la première interaction mais que sa capacité d'amélioration itérative reste limitée sur les images médicales. Un finetuning ciblé du décodeur de masques sur 45 objets médicaux typiques, avec encodeur d'image et encodeur de prompts gelés, améliore les performances de segmentation pour la majorité des objets testés, plus nettement pour ViT-H que pour ViT-B.