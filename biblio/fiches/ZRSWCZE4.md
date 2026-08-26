# Embracing Imperfect Datasets: A Review of Deep Learning Solutions for Medical Image Segmentation

**Auteurs** : Nima Tajbakhsh, Laura Jeyaseelan, Qian Li, Jeffrey N. Chiang, Zhihao Wu, Xiaowei Ding
**Année** : 2019
**DOI** : 10.48550/arxiv.1908.10454

## Résumé

The medical imaging literature has witnessed remarkable progress in high-performing segmentation models based on convolutional neural networks. Despite the new performance highs, the recent advanced segmentation models still require large, representative, and high quality annotated datasets. However, rarely do we have a perfect training dataset, particularly in the field of medical imaging, where data and annotations are both expensive to acquire. Recently, a large body of research has studied the problem of medical image segmentation with imperfect datasets, tackling two major dataset limitations: scarce annotations where only limited annotated data is available for training, and weak annotations where the training data has only sparse annotations, noisy annotations, or image-level annotations. In this article, we provide a detailed review of the solutions above, summarizing both the technical novelties and empirical results. We further compare the benefits and requirements of the surveyed methodologies and provide our recommended solutions. We hope this survey article increases the community awareness of the techniques that are available to handle imperfect medical image segmentation datasets.

## Méthodologie

{'study_design': "Revue narrative de la littérature organisant les solutions existantes selon deux grandes catégories de limitations des jeux de données : annotations rares (scarce annotations) et annotations faibles (weak annotations, incluant annotations éparses, bruitées ou au niveau de l'image)", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Littérature sur la segmentation d'images médicales par réseaux de neurones convolutifs profonds"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['Les méthodologies pour le problème des annotations rares peuvent être classées en trois catégories selon les exigences en données : faibles, moyennes et élevées', 'Le CRF-based post-processing montre des résultats mitigés pour la segmentation 3D', "Les représentations d'images 3D modifiées apportent des gains moyens au prix de l'entraînement de plusieurs modèles 2D", "L'apprentissage semi-supervisé avec pseudo-annotations montre des résultats mitigés, sauf pour les méthodes utilisant des architectures avancées gérant le bruit d'annotation", "Les techniques d'adaptation de domaine sont efficaces mais difficiles à adopter en raison de l'instabilité de l'entraînement adversarial", "L'apprentissage auto-supervisé (self-supervised pre-training) est considéré comme l'une des approches les plus prometteuses de sa catégorie", "L'apprentissage actif et la segmentation interactive sont recommandés en priorité lorsque l'annotation de données supplémentaires est nécessaire"], 'main_findings': ["Les limitations des jeux de données de segmentation d'images médicales se répartissent en deux grandes catégories : annotations rares et annotations faibles", "Un cadre multi-tâches combinant apprentissage semi-supervisé et approches basées CAM peut traiter simultanément les problèmes d'annotations rares et faibles lors de l'utilisation conjointe de plusieurs jeux de données", 'Le Tableau 7 synthétise les méthodologies recommandées selon les exigences en données (faibles, moyennes, élevées) sous forme de guide stratégique']}

## Conclusions

La revue couvre les limitations de données associées aux jeux de données de segmentation d'images médicales, à savoir les annotations rares et les annotations faibles Pour le problème des annotations rares, un éventail de solutions a été passé en revue, allant des solutions semi-automatisées impliquant des experts humains (apprentissage actif, segmentation interactive) aux solutions entièrement automatisées exploitant des données non annotées ou synthétiques du même domaine, ou des données annotées de domaines similaires Pour le problème des annotations faibles, des solutions capables de gérer des annotations éparses, bruitées ou uniquement au niveau de l'image ont été étudiées Les méthodologies ont été comparées en termes de ressources de données requises, difficulté d'implémentation et gains de performance, en mettant en avant celles offrant le meilleur compromis coût-bénéfice Les auteurs espèrent que cette revue augmentera la sensibilisation de la communauté aux stratégies de gestion des annotations rares et faibles, et inspirera de futurs efforts de recherche dans ce domaine

## Comparison between image synthesis methods suggested for medical image segmentation. MRI CycleGAN is used to generate pairs of synthesized MR images from labeled CT slices Zhang et al. (2018d) Cross-domain synthesis CT ↔MRI CycleGAN with shape consistency loss is used to translate between MR and CT scans Fu et al. (2018a) Same-domain synthesis 3D Microscopy CycleGAN with spatially constraints is used to synthesize 3D microscopy images Guibas et al. (2017) Same-domain synthesis Fundus Conditional GAN and Vanilla are used to generate a vessel mask and the corresponding fundus image

| Publication | Synthesis Type | Domains | Description |
| --- | --- | --- | --- |
| Chartsias et al. (2017) Cross-domain synthesis CT → Shin et al. (2018) Same-domain synthesis MRI | Conditional GAN to generate synthetic MR images given a lesion mask and a brain segmentation mask |
| Jin et al. (2018) | Same-domain synthesis CT | Conditional GAN is used to synthesize pleural nodules in the nodule-free CT slices |
| Tang et al. (2018) | Same-domain synthesis CT | Conditional GAN is used to synthesize higher contrast preprocessed images |
| Tang et al. (2019b) | Same-domain synthesis CT | Conditional GAN is used to synthesize CT lymph node images given lymph node mask |
| Tang et al. (2019a) | Same-domain synthesis X-ray | Conditional GAN is used to synthesize X-ray images with desired abnormalities |
| Mahapatra et al. (2018) | Same-domain synthesis X-ray | Conditional GAN is used to synthesize X-ray images with desired abnormalities |
| Abhishek and Hamarneh (2019) Same-domain synthesis Skin images | Conditional GAN is used to synthesize skin images from user-defined lesion masks |
| Zhao et al. (2019a) | Same-domain synthesis MRI | Hybrid spatial-intensity transformation network is used to synthesize MR images |
| Chaitanya et al. (2019) | Same-domain synthesis MRI | Hybrid spatial-intensity transformation network is used to synthesize task-driven MR images |
| Xu and Niethammer (2019) | Same-domain synthesis MRI | Spatial transformation network is used to synthesize task-driven MR images |
| a model trained using traditional data augmentation and 3 |
| points increase in Dice over atlas-based data augmentation. |
| Noteworthy, the suggested method is tested in a 1-shot medical |

## Overview of the papers leveraging external labeled datasets. The suggested method, among other factors, differ in terms of presence of target domain labels and the domain in which segmentation is performed. The Figure column on the right shows the matching data flow from Figure 2.

| Publication | Availability of Target Domain Segmentation Masks | Segmentation Domain | Modality | Figure |
| --- | --- | --- | --- | --- |
| Transfer Learning |  |  |  |  |
| Ma et al. (2019) |  | Target | 2D→2D | (a) |
| Qin (2019) |  | Target | 2D→2D | (a) |
| Liu et al. (2018) |  | Target | 2D→3D | (a) |
| Yu et al. (2018) |  | Target | 2D→3D | (a) |
| Domain Adaptation |  |  |  |  |
| Huo et al. (2018a) |  | Target | MRI, CT | (a) |
| Huo et al. (2018b) |  | Target | MRI, CT | (a) |
| Chen et al. (2019b) |  | Target | bSSFP, LGE | (a) |
| Chen et al. (2018) |  | Source | X-ray | (b) |
| Zhang et al. (2018c) |  | Source | DRR, X-ray | (b) |
| Chen et al. (2019a) |  | Target | MRI, CT | (c) |
| Giger (2018) |  | Source | MRI, CT | (b) |
| Chartsias et al. (2017) |  | Both | MRI, CT | (i) |
| Zhang et al. (2018d) |  | Both | MRI, CT | (i) |
| Dou et al. (2018) |  | Both | MRI, CT | (e) |
| Valindria et al. (2018) |  | Both | MRI, CT | (d),(e),(f),(g),(h) |
| Dataset Fusion |  |  |  |  |
| Harouni et al. (2018a) |  | All domains | MRI,CT,US,X-ray | (d) |
| Dmitriev and Kaufman (2019) |  | All domains | CT | (d) |

## Algorithm 2: Interactive segmentation Input : Initial model M 0 , unlabeled image I, number of iterations N , feedback operation R,

|  | conversion operation C |
| --- | --- | --- |
|  | Output: Updated model M N |
| 1 for i ← 1 to N do |
|  | / * generate segmentation map | * / |
| 2 | S i ← M i-1 (I); |
|  | / * get feedback from an expert | * / |
| 3 | F i ← R(S i , I); |
|  | / * convert to a new annotation | * / |
| 4 |  |

## Comparison between self-supervised training methods that can directly or indirectly aid medical image segmentation. Image-to-image Learn how to weakly localize anatomical landmarks in MR images Approximate landmark positions models are then fine-tuned for the task of instrument segmentation in colonoscopy videos with varying fractions of the training set. When only 25 images are used for fine-tuning, the instrument segmentation model pre-trained via self-supervised learning achieves a Dice score of 0.61, which outperforms the counterpart model pre-trained using Microsoft COCO dataset and the model trained from scratch, both with a Dice score of 0.57.

| Publication | Network | Type | Surrogate task Description | Annotation |
| --- | --- | --- | --- | --- |
| Jamaludin et al. (2017) | Encoder | Image-to-scalar Predict if two longitudinal studies belong to the same patient | 1(same)/0(different) |
| Zhang et al. (2017a) | Encoder | Image-to-scalar Predict the order of two slices random selected from the same CT scan | 0(top)/1(bottom) |
| Tajbakhsh et al. (2019a) | Encoder | Image-to-scalar Predict the degree of rotation applied to a chest CT scan | θ 90 • (θ ∈ {0, 90, 180, 270}) |
| Spitzer et al. (2018) | Siamese | Image-to-scalar Predict the distance between two patches sampled from the same MR image Float distance |
| Gildenblat and Klaiman (2019) Siamese | Image-to-scalar Predict if two patches sampled from the same MR image are spatially near | 1(near)/0(far) |
| Alex et al. (2017) | Encoder-decoder Image-to-image Learn how to remove noise from MR image patches | Original patch before injecting noise |
| Ross et al. (2018) | Encoder-decoder Image-to-image Learn how to colorize gray-scale colonoscopy frames | Original frame before removing color |
| Tajbakhsh et al. (2019a) | Encoder-decoder Image-to-image Learn how to colorize gray-scale tele-med skin images | Original image before removing color |
| Zhou et al. (2019b) | Encoder-decoder Image-to-image Learn how to restore the image from various degradation transformations | Original image before degradation |
| Bai et al. (2019) | Encoder-decoder |  |  |  |

## Comparison between the methods based on semi-supervised learning with pseudo annotations for medical image segmentation. The suggested methods differ in how the initial labeled dataset is constructed, how pseudo annotations for unlabeled data are generated, and whether or not any special treatment is applied to the unreliable regions in pseudo annotation masks. for unlabeled data. While the semi-supervised learning methods based on pseudo annotations commonly follow the iterative process stated above, they differ in how they initialize the base model, how they generate pseudo masks, and whether or not they use a mechanism to handle label noise in pseudo segmentation masks. We have compared the semi-supervised learning methods that use pseudo annotations from these perspectives in Table5, and further review them as follows.Without initially labeled dataset:Zhang et al. (2018b)  train a cyst segmentation model using unlabeled chest CT scans. Since the dataset is completely unlabeled, the authors generate the initial ground truth using K-means clustering followed by a refinement stage through graph cuts. The segmentation model is trained using the pseudo masks and then the model is applied back to the data to generate refined pseudo masks.

| Publication | Initial annotations by Pseudo masks generated by | Label noise handled by |
| --- | --- | --- | --- |
| Zhang et al. (2018b) K-means | Single segmentation model | N/A |
| Bai et al. (2017) | Expert | Single segmentation model + CRF N/A |
| Zhou et al. (2018a) | Expert | Ensemble segmentation model | N/A |
| Zhao et al. (2019b) | Expert | Single segmentation model | N/A |
| Nie et al. (2018) | Expert | Single segmentation model | Discriminator network |
| Min et al. (2018) | Expert | Ensemble segmentation model | Consensus by two parallel networks |
| Xia et al. (2020) | Expert | Ensemble segmentation model | Consensus by multi-view networks |
|  |  | The |  |
| training process alternates between updating the segmentation |  |
| model and refining pseudo masks. The authors train the |  |
| segmentation model on 166 CT scans and use 17 CT scans |  |
| including 5 mild, 6 moderate, and 6 severe cases for testing. In |  |
| 3 iterations, the suggested method achieves 12-point increase |  |
| in Dice over a model trained using the initial pseudo mask |  |
| generated by K-means. |  |  |  |

## Semi-supervised methods suggested for medical image segmentation that do not use pseudo annotations. The suggested methods combine the segmentation task with an unsupervised task, allowing the model to use both labeled and unlabeled images during training. Transformation consistency Segmentation model is trained to achieve equivariance to image rotation or flipping

| Publication | Unsupervised task | Description |
| --- | --- | --- |
| Li et al. (2019b) |  |  |
| Cui et al. (2019) | Transformation consistency Segmentation model is mentored by a mean teacher network to achieve equivariance to image perturbations |
| Chen et al. (2019c) | Image reconstruction | Segmentation model is trained along with a class-specific image reconstruction network |
| Chartsias et al. (2018) Image reconstruction |  |

## By using the boundary loss for brain lesion segmentation, authors evaluate on two MRI datasets (ISLES with 74 training plus 20 testing and WMH of 50 training plus 10 testing) and report an 8% gain in Dice and a 10% gain in Hausdorff score over a baseline that uses generalized Dice as the loss function on ISLES dataset compared to marginal improvement on the WMH dataset.

| Karimi and Salcudean (2019) explore three approximations to |
| --- |
| Hausdorff distance such that it can be directly minimized. The |
| authors report performance on multiple applications including |
| 2D prostate ultrasound (450/225), 3D prostate MRI (80/30), |
| 3D Liver CT (100/31) and 3D Pancreas CT (200/82), resulting |
| in 18% to 45% reduction in Hausdorff distance without |
| degrading other performance metrics such as Dice similarity |
| coefficient. |
| More recently, Duan et al. ( |

## Top-down overview of the methodologies suggested for the problems of scarce and weak annotations, where the methodologies are grouped by the underlying general and specific strategies. We have further used color encoding to show the required data resources of each methodology. Methodologies highlighted in green require no further data resources in addition to the original limited annotated dataset available for training; thus, they should be used wherever possible. Methodologies highlighted in orange require access to additional unlabeled data from the same domain or labeled data from a similar domain. Methodologies highlighted in red require experts in the loop; and thus, may not always be a viable option.

| Problem I: Scarce Annotations |  |  |  |
| --- | --- | --- | --- |
| General Strategy | Specific Strategy | Methodology | Description |
|  |  | Same-domain data synthesis | Training a segmentation model with additional labeled data generated by an image synthesis model |
|  | Augmenting the limited data with new artificial examples | Data augmentation by mixing images Traditional data augmentation | Training a segmentation model with additional labeled data generated by blending the labeled images Training a segmentation model with additional labeled data generated by spatial and intensity transformation |
|  |  | Semi-supervised learning with pseudo labels | Annotating unlabeled images using models' own predictions and then using the augmented dataset for training a segmentation model |
|  | Leveraging additional unlabeled data | Semi-supervised learning without pseudo labels | Training a segmentation model with both labeled and unlabeled data |
|  | from the same domain | Self-supervised pre-training | Pre-training a model using unlabeled medical data and then fine-tuning the model for the target segmentation task |
|  |  | Transfer learning | Training a segmentation model from the knowledge learned from natural images (ImageNet or COCO) |
|  |  | Dataset fusion | Training a universal segmentation model from heterogeneous datasets by learning to discriminate between the datasets |
|  | Leveraging external labeled data from | Domain adaptation w/ target labels | Training a segmentation model using shared feature representations learned across multiple domains |
| Expanding the dataset | a similar domain | Domain adaptation w/o target labels | by translating from one domain to the other Training a segmentation model using only source domain labels |
|  | Collecting additional annotations with experts in the loop | Active learning Interactive segmentation | Selecting unlabeled images for annotation judiciously based on model predictions Accelerating the annotation process by propagating the user changes throughout the segmentation mask |
|  | Leveraging additional tasks | Multi-task learning | Training a segmentation model with additional heads, each for a separate classification task |
| Training w/ regularization | Imposing additional constraints Leveraging more informative or compressed input data | Shape regularization Altered image representation | Training a segmentation model by imposing shape constraints on predicted segmentation masks Training a segmentation model with a more compact or informative image representation |
| Post-training refinement | Using post-processing methods to refine segmentations | CRF-based post segmentation | Using CRF as a post-processing or as a trainable module in the segmentation network |
| Problem II: Weak Annotations |  |  |  |
|  | Learning with sparse annotations | Selective loss w/ and w/o mask completion | Training a segmentation model by excluding unannotated pixels from backpropagation |
|  | Learning with noisy annotations | Robust loss w/ and w/o iterative label refinement | Training a segmentation model with mechanisms that downgrade unreliable annotations during training |
| Leveraging weak annotations | Learning with image-level annotations Class activation maps | Training a classification model with global average pooling and using activation maps as class-specific segmentation |

### Formule


$$x = λx i + (1 -λ)x j ỹ = λy i + (1 -λ)y j$$

### Formule


$$Output: Labeled dataset L T , updated model M T 1 L 0 ← ∅; 2 for i ← 1 to T do / * phase 1: query batch selection * / 3 Q t ← A(U t-1 , M t-1 , k); 4 annotate samples in Q t ; / * phase 2: update model * / 5 L t ← L t-1 ∪ {(x, y)|x ∈ Q t , y ∈ Y t }; 6 M t ← fine-tuning M t-1 using L t ; 7 U t ← U t-1 \Q t ; 8 end 9 return L T , M T$$

### Formule


$$A i ← C(F i ); 5 M i ← fine-tuning M i-1 with A i ; 6 end 7 return S N$$

### Formule


$$Updated model M T 1 M 0 ← training base model with L; 2 for i ← 1 to T do / * generate pseudo segmentation masks * / 3 S i ← F (M i-1 , U ); 4 D i ← L ∪ {(x, s)|x ∈ U , s ∈ S i }; 5 M i ← fine-tuning M i-1 using D i ; 6 end 7 return M T$$

### Formule


$$ζ l ← l (M l (M c (L))); 2 ζ u ← u (M u (M c (U )) + u (M u (M c (L)); 3 minimize(ζ l + ζ u ); 4 return M$$

### Formule


$$Dist(∂G, ∂S) = ∂G ||q ∂S (p) -p|| 2 dp,(1)$$

### Formule


$$E(x | I) = ∑ i φ u (x i ) + ∑ i =j φ p (x i , x j ).$$
