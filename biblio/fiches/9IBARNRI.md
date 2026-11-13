# PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation



## Resume


PSAM: Prompt-based Segment Anything Model Adaption for Medical Image Segmentation

Segment Anything Model (SAM) for Medical Image Segmentation: A Preliminary Review

Trans-SAM: Transfer Segment Anything Model to medical image segmentation with Parameter-Efficient Fine-Tuning

RepViT-MedSAM: Efficient Segment Anything in the Medical Images

The Role of Segment Anything Model (SAM) In Medical Image Segmentation: A Comprehensive Review

SwiftMedSAM: An Ultra-lightweight Prompt-Based Universal Medical Image Segmentation Model for Highly Constrained Environments

Towards an automated Segment Anything Model (SAM) for lesion segmentation in oncological PET/CT images

How Segment Anything Model (Sam) Boost Medical Image Segmentation: A Survey

Part-aware Prompted Segment Anything Model for Adaptive Segmentation

Precision medicine, such as patient-adaptive treatments assisted by medical image analysis, poses new challenges for segmentation algorithms in adapting to new patients, due to the large variability across different patients and the limited availability of annotated data for each patient. In this work, we propose a data-efficient segmentation algorithm, namely Part-aware Prompted Segment Anything Model ($P^2SAM$). Without any model fine-tuning, $P^2SAM$ enables seamless adaptation to any new patients relying only on one-shot patient-specific data. We introduce a novel part-aware prompt mechanism to select multiple-point prompts based on the part-level features of the one-shot data, which can be extensively integrated into different promptable segmentation models, such as SAM and SAM 2. Moreover, to determine the optimal number of parts for each specific case, we propose a distribution-guided retrieval approach that further enhances the robustness of the part-aware prompt mechanism. $P^

S-SAM: SVD-based Fine-Tuning of Segment Anything Model for Medical Image Segmentation

Medical image segmentation has been traditionally approached by training or fine-tuning the entire model to cater to any new modality or dataset. However, this approach often requires tuning a large number of parameters during training. With the introduction of the Segment Anything Model (SAM) for prompted segmentation of natural images, many efforts have been made towards adapting it efficiently for medical imaging, thus reducing the training time and resources. However, these methods still require expert annotations for every image in the form of point prompts or bounding box prompts during training and inference, making it tedious to employ them in practice. In this paper, we propose an adaptation technique, called S-SAM, that only trains parameters equal to 0.4% of SAM's parameters and at the same time uses simply the label names as prompts for producing precise masks. This not only makes tuning SAM more efficient than the existing adaptation methods but also removes the burden of

LeSAM: Adapt Segment Anything Model for Medical Lesion Segmentation.

The Segment Anything Model (SAM) is a foundational model that has demonstrated impressive results in the field of natural image segmentation. However, its performance remains suboptimal for medical image segmentation, particularly when delineating lesions with irregular shapes and low contrast. This can be attributed to the significant domain gap between medical images and natural images on which SAM was originally trained. In this paper, we propose an adaptation of SAM specifically tailored for lesion segmentation termed LeSAM. LeSAM first learns medical-specific domain knowledge through an efficient adaptation module and integrates it with the general knowledge obtained from the pre-trained SAM. Subsequently, we leverage this merged knowledge to generate lesion masks using a modified mask decoder implemented as a lightweight U-shaped network design. This modification enables better delineation of lesion boundaries while facilitating ease of training. We conduct comprehensive experime

A review of the Segment Anything Model (SAM) for medical image analysis: Accomplishments and perspectives

AutoSAM: Adapting SAM to Medical Images by Overloading the Prompt Encoder

EviPrompt: A Training-Free Evidential Prompt Generation Method for Adapting Segment Anything Model in Medical Images

ST-SAM: A Spatio-Temporal Enhanced Segment Anything Model for Echocardiogram Video Segmentation

ProtoSAM-3D: Interactive semantic segmentation in volumetric medical imaging via a Segment Anything Model and mask-level prototypes

Research on Medical Image Segmentation Based on SAM and Its Future Prospects.

The rapid advancement of prompt-based models in natural language processing and image generation has revolutionized the field of image segmentation. The introduction of the Segment Anything Model (SAM) has further invigorated this domain with its unprecedented versatility. However, its applicability to medical image segmentation remains uncertain due to significant disparities between natural and medical images, which demand careful consideration. This study comprehensively analyzes recent efforts to adapt SAM for medical image segmentation, including empirical benchmarking and methodological refinements aimed at bridging the gap between SAM's capabilities and the unique challenges of medical imaging. Furthermore, we explore future directions for SAM in this field. While direct application of SAM to complex, multimodal, and multi-target medical datasets may not yet yield optimal results, insights from these efforts provide crucial guidance for developing foundational models tailored to

Volumetric medical image segmentation via fully 3D adaptation of Segment Anything Model

RefSAM3D: Adapting the Segment Anything Model with cross-modal references for three-dimensional medical image segmentation

The Segment Anything Model (SAM), originally built on a two-dimensional vision transformer, excels at capturing global patterns in two-dimensional natural images but faces challenges when applied to three-dimensional (3D) medical imaging modalities such as computed tomography and magnetic resonance imaging. These modalities require capturing spatial information in volumetric space for tasks such as organ segmentation and tumor quantification. To address this challenge, we introduce RefSAM3D, an adaptation of SAM for 3D medical imaging by incorporating a 3D image adapter and cross-modal reference prompt generation. Our approach modifies the visual encoder to handle 3D inputs and enhances the mask decoder for direct 3D mask generation. We also integrate textual prompts to improve segmentation accuracy and consistency in complex anatomical scenarios. By employing a hierarchical attention mechanism, our model effectively captures and integrates information across different scales. Extensiv

Segment anything model 2: an application to 2D and 3D medical images

Segment Anything Model (SAM) has gained significant attention because of its ability to segment various objects in images given a prompt. The recently developed SAM 2 has extended this ability to video inputs. This opens an opportunity to apply SAM to 3D images, one of the fundamental tasks in the medical imaging field. In this paper, we extensively evaluate SAM 2's ability to segment both 2D and 3D medical images by first collecting 21 medical imaging datasets, including surgical videos, common 3D modalities such as computed tomography (CT), magnetic resonance imaging (MRI), and positron emission tomography (PET) as well as 2D modalities such as X-ray and ultrasound. Two evaluation settings of SAM 2 are considered: (1) multi-frame 3D segmentation, where prompts are provided to one or multiple slice(s) selected from the volume, and (2) single-frame 2D segmentation, where prompts are provided to each slice. The former only applies to videos and 3D modalities, while the latter applies to

Rep-MedSAM: Towards Real-Time and Universal Medical Image Segmentation

Lung Segment Anything Model (LuSAM): A Prompt-integrated Framework for Automated Lung Segmentation on ICU Chest X-Ray Images

<jats:italic toggle="yes">Abstract
                  — The Segment Anything Model (SAM) is a
state-of-the-art deep learning architecture for image seg- mentation
that allows users to segment arbitrary objects in images using points,
or bounding boxes. SAM uses a novel two-stage approach that first
encodes the input image into a high-dimensional embedding, and then
generates object masks using the embedding and the input prompt. This
ap- proach allows SAM to produce high-quality segmentation even for
objects that were not seen during training, and to handle complex input
prompts with multiple objects and attributes. We evaluate SAM on the
open source Chest X- ray dataset known as Japanese Society of
Radiological Technology (JSRT) dataset and another dataset obtained from
Emory Hospital, Atlanta, Georgia,USA and show that it achieves
state-of-the-art performance in terms of Stability Score and Jaccard
Index including the perfor- mance across different demographic data

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation


## Synthese


L'adaptation directe du modèle Segment Anything (SAM) aux images médicales, notamment volumétriques, s'avère sous-optimale car ses capacités de discrimination reposent sur des prompts positionnels (points, boîtes englobantes) dépourvus de sémantique de haut niveau, mal adaptés aux frontières ambiguës entre tumeurs et tissus environnants. Les approches existantes d'adaptation 2D vers 3D, conçues pour des données vidéo ou via des modules de fusion additionnels, ne parviennent pas à traiter de manière isotrope l'information spatiale tridimensionnelle propre à l'imagerie médicale, tout en posant des problèmes de mémoire et de stabilité numérique liés à l'augmentation du nombre de tokens. Les auteurs proposent donc 3DSAM-adapter, une méthode d'adaptation paramétriquement efficace qui modifie de façon holistique l'encodeur d'image, l'encodeur de prompt (via un échantillonneur visuel et des requêtes globales remplaçant l'encodage positionnel) et le décodeur de masque, afin de réutiliser un maximum de poids pré-entraînés tout en capturant les motifs spatiaux 3D. Sur le plan expérimental, cette approche est évaluée de façon comparative face à nn-UNet et à d'autres méthodes d'adaptation sur quatre jeux de données de segmentation tumorale.

L'objectif de cette étude est d'adapter le Segment Anything Model (SAM), initialement conçu pour la segmentation interactive d'images naturelles 2D, à la tâche de segmentation d'images médicales 3D en régime one-shot, c'est-à-dire avec un seul exemple annoté disponible. Ce travail est motivé par trois limites majeures de SAM identifiées par les auteurs : sa dépendance structurelle aux interactions utilisateur (points, boîtes englobantes), l'écart de distribution important entre les images naturelles sur lesquelles il a été entraîné et les images médicales, et son coût de calcul élevé qui freine son adoption clinique. Les hypothèses sous-jacentes sont que la capacité de généralisation de l'encodeur de SAM peut être transférée efficacement vers un encodeur léger via une distillation de connaissances en deux étapes, et qu'une supervision mutuelle entre un encodeur général et un encodeur médical spécifique, couplée à un décodeur autoprompting, permet d'obtenir une segmentation performante sans annotation interactive ni coût computationnel prohibitif.

S-SAM propose une adaptation efficace du Segment Anything Model (SAM) à la segmentation d'images médicales, en s'affranchissant du besoin de prompts experts tels que des points ou des boîtes englobantes. La méthode repose sur un fine-tuning basé sur la décomposition en valeurs singulières (SVD) de l'encodeur d'image de SAM, complété par une couche Text Affine Layer (TAL), des matrices de mise à l'échelle et de décalage, ainsi que l'entraînement des positional embeddings et des couches layernorm. Cette approche permet d'utiliser de simples noms de classes comme prompts textuels, à la place des annotations expertes habituellement requises. Évalué sur cinq jeux de données publics couvrant des modalités variées (endoscopie, radiographie, échographie, CT et histologie), S-SAM égale ou surpasse les méthodes état de l'art et les techniques d'adaptation existantes de SAM, tout en nécessitant significativement moins de paramètres entraînables. Les auteurs notent toutefois que la performance de S-SAM peut être affectée par des disparités de taille entre classes, ouvrant la voie à des travaux futurs sur des fonctions de perte pondérées.


## Methodologie


L'adaptation directe du modèle Segment Anything (SAM) aux images médicales, notamment volumétriques, s'avère sous-optimale car ses capacités de discrimination reposent sur des prompts positionnels (points, boîtes englobantes) dépourvus de sémantique de haut niveau, mal adaptés aux frontières ambiguës entre tumeurs et tissus environnants. Les approches existantes d'adaptation 2D vers 3D, conçues pour des données vidéo ou via des modules de fusion additionnels, ne parviennent pas à traiter de manière isotrope l'information spatiale tridimensionnelle propre à l'imagerie médicale, tout en posant des problèmes de mémoire et de stabilité numérique liés à l'augmentation du nombre de tokens. Les auteurs proposent donc 3DSAM-adapter, une méthode d'adaptation paramétriquement efficace qui modifie de façon holistique l'encodeur d'image, l'encodeur de prompt (via un échantillonneur visuel et des requêtes globales remplaçant l'encodage positionnel) et le décodeur de masque, afin de réutiliser un maximum de poids pré-entraînés tout en capturant les motifs spatiaux 3D. Sur le plan expérimental, cette approche est évaluée de façon comparative face à nn-UNet et à d'autres méthodes d'adaptation sur quatre jeux de données de segmentation tumorale.


## Raw_Problem_Setup


Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).

Given a Segment Anything Model f SAM , we aim to apply f SAM to the current image sample x t to obtain segmentation masks according to the particular medical image segmentation task at hand. Since SAM and its variants require points and/or bounding boxes as prompts for generating segmentation masks, we assume that each object of interest in x t is given at least a prompt (e.g., a center point or a bounding box). This problem setup was utilized in previous work (e.g., [17,11]).


## Quote


Comment adapter le Segment Anything Model (SAM) à la segmentation d'images médicales 3D en one-shot, en surmontant sa dépendance aux interactions utilisateur, les écarts de distribution entre images naturelles et médicales, et son coût de calcul élevé ?