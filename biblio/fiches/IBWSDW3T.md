# SAMCT: Segment Any CT Allowing Labor-Free Task-Indicator Prompts.

**Auteurs** : Xian Lin, Yangyang Xiang, Zhehao Wang, Kwang-Ting Cheng, Zengqiang Yan, Li Yu
**Année** : 2025
**DOI** : 10.1109/tmi.2024.3493456

## Résumé

Segment anything model (SAM), a foundation model with superior versatility and generalization across diverse segmentation tasks, has attracted widespread attention in medical imaging. However, it has been proved that SAM would encounter severe performance degradation due to the lack of medical knowledge in training and local feature encoding. Though several SAM-based models have been proposed for tuning SAM in medical imaging, they still suffer from insufficient feature extraction and highly rely on high-quality prompts. In this paper, we propose a powerful foundation model SAMCT allowing labor-free prompts and train it on a collected large CT dataset consisting of 1.1M CT images and 5M masks from public datasets. Specifically, based on SAM, SAMCT is further equipped with a U-shaped CNN image encoder, a cross-branch interaction module, and a task-indicator prompt encoder. The U-shaped CNN image encoder works in parallel with the ViT image encoder in SAM to supplement local features. Cr

## Méthodologie

{'study_design': "Développement d'un modèle de fondation (SAMCT) basé sur SAM, augmenté d'un encodeur d'image CNN en forme de U, d'un module d'interaction cross-branch et d'un encodeur de prompts task-indicator, évalué sur 30 jeux de données publics de CT couvrant 118 objets", 'intervention': "SAMCT: ajout d'une branche CNN en forme de U en parallèle de l'encodeur ViT de SAM, module d'interaction cross-branch pour échanger perception globale et caractéristiques locales, et encodeur de prompts task-indicator optionnel générant automatiquement des embeddings de prompts (points positifs, points négatifs, boîtes englobantes)", 'control': "Comparaison avec SAM original, plusieurs modèles SAM-based de l'état de l'art pour l'imagerie médicale, et 13 modèles spécifiques à la tâche (task-specific), incluant U-Net, CPFNet, CA-Net, AAU-net", 'primary_outcomes': ['Performance de segmentation (versatilité et généralisation) sur 118 objets à travers 30 jeux de données'], 'secondary_outcomes': ['Performance comparative des différents modes de prompts (point aléatoire, point central, boîte aléatoire, boîte englobante, point+boîte, task-indicator prompt)', "Résultats de l'étude d'ablation par composant"], 'statistical_methods': ["Perte Dice et entropie croisée binaire pour l'entraînement", "Perte d'entropie croisée additionnelle pour la classification foreground/background dans l'encodeur de prompts task-indicator"], 'duration': None, 'setting': "Recherche computationnelle / apprentissage profond appliqué à l'imagerie médicale CT"}

## Résultats

{'quantitative': [{'outcome': 'Nombre de paramètres du module task-indicator prompt encoder', 'value': '1.7', 'unit': 'M (millions de paramètres)', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'it is very lightweight with only 1.7M parameters, being highly extendable to other foundation models.'}, {'outcome': 'Taille du jeu de données CT5M', 'value': '1.1M images, 5M masques, 5821 patients, 118 objets, 30 jeux de données', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Introduction', 'source_quote': 'we construct and release a large CT dataset by collecting, pre-processing, and standardizing 30 public datasets, consisting of 5821 patients, 1.1M images, and 5M imagemask pairs, and covering 118 objects.'}, {'outcome': "Learning rate initial et batch size pour l'entraînement du task-indicator prompt encoder", 'value': '0.0003 (lr), 12 (batch size)', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'trained on the frozen SAMCT-CT5M with an initial learning rate of 0.0003 and a batch size of 12.'}], 'qualitative_findings': ["La position des prompts de type point a un impact crucial sur la performance des méthodes basées sur SAM, aucun type de point ne s'avérant systématiquement le meilleur", 'Les résultats de segmentation générés sous différents prompts de type boîte sont relativement stables et meilleurs que les différents prompts de type point', 'Le prompt combiné point central + boîte englobante atteint systématiquement la meilleure performance parmi les modes de prompt manuels', 'Le task-indicator prompt surpasse systématiquement tout prompt de type point, dépasse le prompt de boîte aléatoire pour foie, rein gauche, rein droit et tête fémorale gauche, approche le meilleur prompt manuel pour foie, rate, têtes fémorales gauche et droite, et surpasse même le meilleur prompt manuel pour rein gauche et rein droit'], 'main_findings': ['SAMCT surpasse systématiquement les modèles de fondation SOTA et les modèles spécifiques à la tâche SOTA en termes de versatilité et de généralisation', "La suppression de tout composant de SAMCT (encodeur CNN, module d'interaction cross-branch, encodeur de prompts task-indicator) nuit à la performance, validant les choix de conception", "Le task-indicator prompt, bien qu'il ne surpasse pas complètement le meilleur prompt manuel, est labor-free et plus facile à utiliser en contexte clinique"]}

## Conclusions

SAMCT est un modèle de fondation de segmentation pour la modalité CT intégrant trois composants originaux : un encodeur d'image CNN en forme de U pour le complément de caractéristiques locales, un module d'interaction cross-branch pour le transfert de connaissances, et un encodeur de prompts task-indicator pour une interaction labor-free Le task-indicator prompt fournit un nouveau paradigme pour des prompts labor-free, convertissant l'interaction semi-automatique de SAM en interaction entièrement automatique dans SAMCT, ce qui est plus pratique et favorable pour les applications cliniques Les expériences comparatives extensives démontrent la versatilité et la capacité de généralisation extraordinaires de SAMCT, surpassant les modèles de fondation médicaux SOTA et les modèles spécifiques à la tâche sur diverses tâches, même sans prompts manuels

## Comparison of foundation models designed for universal medical image segmentation. Our SAMCT is a comprehensive model that supplements local feature encoding and allows labor-free prompts

| Method | Input size | Prompts | Labor-free mode | ViT encoder | CNN encoder Prompt encoder Mask decoder |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MedSAM (Ma and Wang 2023) | 1024×1024 | box | ✗ | fine-tuning | ✗ | frozen | fine-tuning |
| SAMed (Zhang and Liu 2023) | 512×512 | - | - | LoRA tuning | ✗ | fine-tuning | fine-tuning |
| MSA (Wu et al. 2023) | 1024×1024 | point | ✗ | adapter tuning | ✗ | frozen | adapter tuning |
| SAM-Med2D (Cheng et al. 2023) | 256×256 | point&box&mask | ✗ | adapter tuning | ✗ | fine-tuning | fine-tuning |
| SAMCT | 256×256 | point/box/task-indicator |  | adapter tuning |  | frozen | forzen |

## Composition of CT5M. Datasets with * are invisible during training and are only used for generalization verification.

| Dataset | image | mask | Dataset | image | mask | Dataset | image | mask |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HE-BCT * (Hssayeni et al. 2020) | 1,070 | 316 | LCTSC * (Yang et al. 2017) | 14,338 | 38,342 | DZ Task07 (Antonelli et al. 2022) 26,719 11,320 |
| INSTANCE (Li et al. 2023b) | 2,981 | 892 COVID-19 Seg * (Igor.Slinko 2020) | 929 | 699 | CHAOS (Kavur et al. 2021) | 2,874 | 2,341 |
| HaN-Seg (Podobnik et al. 2023) | 7,581 | 24,990 | LNDB (Pedrosa et al. 2019) | 63,068 | 2,369 | DZ Task09 (Antonelli et al. 2022) | 3,650 | 1,050 |
| Totalsegmentator (Wasserthal et al. 2023) 312,400 3,837,723 | ATM * (Zhang et al. 2023) 190,724 124,231 | KiTS23 (Heller et al. 2023) 95,221 16,826 |
| HaN-OAR (Li and Chen 2020) | 6,151 | 13,356 | Pe-CT-SEG (Jordan et al. 2021) 110,083 618,599 | DZ Task10 (Antonelli et al. 2022) 13,486 | 1,280 |
| PDDCA * (Raudaschl et al. 2017) | 7,367 | 6,053 | DZ Task08 (Antonelli et al. 2022) | 21,120 | 12,852 | NIH-Pancreas (Roth et al. 2016) 18,942 | 6,881 |
| COVID-19-20 (Roth et al. 2022) | 13,705 | 4,956 | AMOS22 (Ji et al. 2022) | 41,430 129,237 | COVID-19 Scan * (Ma et al. 2021) | 3,520 | 1,844 |
| MosMed (Morozov et al. 2020) | 2,049 | 785 | WORD (Luo et al. 2022) | 24,218 | 59,192 | A-ACC-Ki67 (Moawad et al. 2023) | 6,008 | 1,400 |
| MM-WHS * (Zhuang et al. 2019) | 5,305 | 17,311 | BTCV * (Landman et al. 2015) | 3,779 | 12,175 | FUMPE (Masoudi et al. 2018) | 8,792 | 2,304 |
| DZ Task06 (Antonelli et al. 2022) | 17,657 | 1,646 | LiTS (Bilic et al. 2023) | 58,638 | 26,269 Pr-An-Ed-Ca * (Thompson et al. 2023) 23,359 23,191 |

## Object Mapping. H: Head and Neck, C: Chest, A: Abdomen, P: Pelvis, B:Bone, L: lesion, V: vessel. To analyze the object-specific performance of SAMCT, we calculate and plot the average Dice score of each object in Figs.5 and 6. For training visible datasets, most objects in chest, abdomen, bone, and pelvis have an average Dice score greater than 90%. Specifically, 44 out of 118 objects have an

| Object | ID | Object | ID | Object | ID | Object | ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| brainstem | H1 | left submandibular gland H2 | right submandibular gland H3 | optic chiasm | H4 |
| left optic nerve | H5 | right optic nerve | H6 | left parotid gland | H7 | right parotid gland | H8 |
| spinal cord | H9 | esophagus | H10 brain | H11 buccal mucosa | H12 |
| oral cavity | H13 | anterior segment (left eyeball) | H14 | anterior segment (right eyeball) | H15 | posterior segment (left eyeball) | H16 |
| posterior segment (right eyeball) | H17 left lacrimal gland | H18 right lacrimal gland | H19 lips | H20 |
| pituitary gland | H21 face | H22 left eye | H23 right eye | H24 |
| left lens | H25 right lens | H26 left temporal lobes | H27 right temporal lobes H28 |
| left inner ear | H29 right inner ear | H30 left middle ear | H31 right middle ear | H32 |
| cricopharyngeal inlet | H33 thyroid | H34 larynx-glottis | H35 larynx-supraglottic | H36 |
| left ventricle | C1 | right ventricle | C2 | left atrium | C3 | right atrium | C4 |
| myocardium | C5 | right lung | C6 | left lung | C7 | trachea | C8 |
| body | C9 | left breast | C10 right breast | C11 thymus | C12 |
| pancreas | A1 | spleen | A2 | right kidney | A3 | left kidney | A4 |
| gallbladder | A5 | liver | A6 | stomach | A7 | right adrenal gland | A8 |
| left adrenal gland | A9 | bladder | A10 prostate | A11 rectum | A12 |
| duodenum | A13 colon | A14 large Intestine | A15 large Intestine | A16 |
| gonads | A17 skin | A18 left autochthon | A19 right autochthon | A20 |
| utero cervix | P1 | left gluteus maximus | P2 | right gluteus maximus | P3 | left gluteus medius | P4 |
| right gluteus medius | P5 | left gluteus minimus | P6 | right gluteus minimus | P7 | left iliopsoas | P8 |
| right iliopsoas | P9 | mandible | B1 | left head of femur | B2 | right head of femur | B3 |
| temporomandibular joint (left) | B4 | temporomandibular joint (right) | B5 | arytenoid | B6 | left clavicula | B7 |
| right clavicula | B8 | left humerus | B9 | right humerus | B10 left rib | B11 |
| right rib | B12 left scapula | B13 right scapula | B14 vertebrae | B15 |
| spinal canal | B16 left hip | B17 right hip | B18 sacrum | B19 |
| hemorrhage | L1 | COVID-19 | L2 | lung tumor | L3 | pancreas tumor | L4 |
| colon cancer | L5 | pulmonary embolism | L6 | pulmonary nodule | L7 | liver tumor | L8 |
| kidney tumor | L9 | cyst | L10 adrenocortical carcinoma | L11 aorta | V1 |
| pulmonary artery | V2 | inferior vena cava | V3 | portal and splenic vein | V4 | left carotid artery | V5 |
| right carotid artery | V6 | hepatic vessel | V7 | left iliac artery | V8 | right iliac artery | V9 |
| left iliac vena | V10 right iliac vena | V11 |  |  |  |  |
| ble datasets, all data is used as the testing set to evaluate the | for data augmentation. |  |  |  |
| generalization ability of SAMCT. As for each training visi- | Quantitative Results. Comparison between SAMCT and |
| ble dataset, data is divided into training, validation, and test- | SAM is depicted in Fig. 4. Any bar in green has a pos- |
| ing sets. The segmentation performance of SAMCT on such | itive value in Fig. 4 indicates that SAMCT outperforms |
| visible testing sets reflects its versatility. Data partitioning | SAM when tested on a training visible dataset, where |
| of training visible datasets follows publicly available data | CHAOS (Kavur et al. 2021) is of the least performance |
| splits. For datasets without public data partitioning or with | improvements among training visible datasets, with an |
| only training set labels, they are randomly divided into train- | average increase of 35.49% in Dice and Totalsegmenta- |
| ing, validation, and testing sets in a 7:1:2 ratio. For datasets | tor (Wasserthal et al. 2023) is of the most performance im- |
| with only training and validation set labels, the validation set | provements with an average increase of 82.22% in Dice. It |
| is divided into validation and testing sets in a 1:1 ratio. |  | demonstrates the brilliant versatility of SAMCT on various |
| 4.2 Versatility and Generalization on CT5M |  | downstream tasks. As for the generalization performance of SAMCT, all training invisible datasets own noticeable per- |
| Setting. To train a powerful CT foundation model for | formance improvements, where LCTSC (Yang et al. 2017) |
| auxiliary annotation and clinical applications, we trained SAMCT on the complete training data of CT5M and eval- | is of the least improvements with an average increase of 26.51% in Dice and COVID-19 Seg (Igor.Slinko 2020) is |
| uated its versatility and generalization. During training, prompts were randomly sampled from positive points, neg- | of the most performance improvements with an average in-crease of 65.67% in Dice. It proves the prominent general- |
| ative points, and shifted bounding boxes generated from the | ization ability of SAMCT. |  |  |  |
| masks. SAMCT was trained by an Adam optimizer with an |  |  |  |  |
| initial learning rate of 0.0006 and a batch size of 48 for |  |  |  |  |
| 50 epochs where the learning rate is adjusted to 0.0001 on |  |  |  |  |
| the 10th epoch. Random rotation, random scaling, cropping, |  |  |  |  |
| contrast adjustment, and gamma augmentation were applied |  |  |  |  |

## Dice comparison of foundation models on three representative training visible datasets, including COVID-19-20

| Method | COVID-19 ICH | Liv | Spl | Lkid | Rkid | Sto | Gal | Eso | Pan | Duo | Col | Rec | Bla | LHF | RHF | Avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SAM (Kirillov et al. 2023) | 15.55 | 10.26 41.88 22.55 20.00 19.62 22.76 2.02 | 1.66 | 6.87 | 5.69 16.66 10.39 17.85 24.06 23.93 16.36 |
| SAM-Med2D (Cheng et al. 2023) | 69.69 | 73.11 95.24 94.16 94.12 94.26 92.14 78.14 78.88 80.94 73.15 79.76 89.27 94.27 94.35 94.33 85.99 |
| MedSAM (Ma and Wang 2023) | 67.65 | 69.36 94.59 95.51 95.25 95.45 93.23 84.99 81.84 82.94 78.38 80.92 89.09 94.74 95.05 94.38 87.09 |
| SAMed (Zhang and Liu 2023) | 77.33 | 74.36 95.24 93.68 93.52 92.82 92.92 83.18 82.07 84.63 79.57 83.34 90.43 94.07 94.03 93.42 87.79 |
| MSA (Wu et al. 2023) | 76.54 | 77.58 96.04 95.33 95.19 95.23 93.57 83.75 83.74 84.59 79.72 85.35 91.54 94.89 95.29 95.42 88.99 |
| SAMCT | 77.59 | 77.66 96.35 95.86 95.61 95.82 93.99 83.87 85.03 86.02 82.14 86.29 91.29 95.33 95.85 96.09 89.67 |

## 

| H: Head & Neck | C: Chest | A: Abdomen | L: Lesion | B: Bone | V: Vessel | Evaluated on visible dataset | Evaluated on invisible dataset |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | (i.e., CT5M), the U-shaped CNN image encoder, and the |
|  |  |  |  |  |  | cross-branch interaction in SAMCT. |
|  |  |  |  |  |  | 4.3 Comparison with Foundation Models Object |
|  |  |  |  |  |  | Setting. Experiments are conducted on a subset of CT5M, |
| Figure 5: H: Head & Neck | C: Chest | A: Abdomen | L: Lesion | consisting of COVID-19-20 (Roth et al. 2022), IN-STANCE (Results. Quantitative comparison results of different foun-B: Bone V: Vessel P: Pelvis Evaluated on visible dataset |
|  |  |  |  |  |  | dation models on three representative training visible |
|  |  |  |  |  |  | datasets are summarized in Table 4. Among SAM-based |
|  |  |  |  |  |  | models for medicine, all models can greatly improve the |
| ). SAMCT consistently outperforms SAM with large margins. | performance of SAM by learning more medical knowledge, where MedSAM (Ma and Wang 2023) and MSA (Wu et al. 2023) achieve the best performance in gallbladder and rec- |
|  |  |  |  |  |  | tum segmentation, respectively. Besides, MSA achieves the |
|  |  |  |  |  |  | best average Dice across 16 objects among comparison mod- |
| average Dice score greater than 90% and 68 out of 118 ob- | els. Comparatively, SAMCT achieves the second-best per- |
| jects have an average Dice score greater than 80%, validat- | formance in the segmentation of gallbladder and rectum and |
| ing the surprising versatility of SAMCT. Among 4,236,340 | outperforms all comparison models on the other 14 objects, |
| training image-mask pairs, the numbers of masks for H4, | leading to the best average Dice score of 89.67%. Quanti- |
| H5, H6, H12, H14, and H15 are only 146, 235, 241, 448, | tative comparison results of different foundation models on |
| 186, and 201, respectively, resulting in relatively poor per- | the training invisible BTCV (Landman et al. 2015) dataset |
| formance of SAMCT. Similarly, B5 and some other objects | are summarized in Table 5. SAM-based medical models are |
| in head and neck exhibit poorer performance due to rela- | still much superior compared to SAM on generalization, es- |
| tively limited training data. For training invisible datasets, | pecially for small-size objects, e.g., gallbladder and esoph- |
| 16 and 10 out of 39 objects have an average Dice score | agus, and low-contrast objects, e.g., stomach. Specifically, |
| greater than 80% and 90%, making SAMCT a powerful tool | MSA and MedSAM achieve the best performance in seg- |
| for clinically-assisted annotation. |  |  |  | menting esophagus and right kidney, with the Dice scores |
| Qualitative Results. Qualitative segmentation results of | of 84.15% and 90.69%, respectively. Compared to MSA |
| SAM and SAMCT are illustrated in Fig. 7. Visually, seg- | and MedSAM, though SAMCT performs slightly worse on |
| menting various medical objects via one model is challeng- | esophagus and right kidney, it is superior on the other 6 ob- |
| ing, especially for those with low contrast, blurry bound- | jects, leading to an improvement of 5.06% and 1.75% in av- |
| aries, small sizes, and complex shapes. Compared to SAM, | erage Dice across 8 objects. It should be noted that the best |
| SAMCT can accurately identify such hard objects, validat- | comparison models for training visible and invisible vali- |
| ing the effectiveness of constructing the large CT dataset | dation are different (i.e., MSA and MedSAM respectively) |

## , four 2D transformer-based methods, i.e., TransFuse (Zhang, Liu, and Hu 2021), Tran-sUNet (Chen et al. 2021), MISSFormer (Huang et al. 2022), and H2Former (He et al. 2023a), and five 3D methods, i.e., nnU-Net (Isensee et al. 2021), SwinUNETR (Hatamizadeh et al. 2021), UNETR (Hatamizadeh et al. 2022), nn-Former (Zhou et al. 2023), and MedNeXt (Roy et al. 2023). All task-specific models were trained on INSTANCE (Li et al. 2023b) and WORD (Luo et al. 2022) respectively following the same settings with SAMCT. Dice comparison of foundation models on the training invisible BTCV (Landman et al. 2015) dataset.

| Results. Quantitative comparison results of different |
| --- |
| methods on visible INSTANCE (Li et al. 2023b) and |
| WORD (Luo et al. 2022) are summarized in Table 6. Among |
| task-specific methods, MedNeXt (Roy et al. 2023) achieves |
| the best performance on INSTANCE and nnU-Net (Isensee |
| et al. 2021) achieves the best performance on WORD. Com- |
| paratively, SAMCT trained on either partial or complete |
| CT5M achieves better performance than all task-specific |

## Table 6 :

| Method | Dice | INSTANCE HD | IoU | Dice | WORD HD | IoU |
| --- | --- | --- | --- | --- | --- | --- |
| U-Net (Ronneberger, Fischer, and Brox 2015) 51.91 22.75 44.03 86.53 17.04 78.47 |
| CPFNet (Feng et al. 2020) | 52.30 22.45 43.58 83.74 18.41 74.64 |
| CA-Net (Gu et al. 2020) | 55.07 22.30 45.29 85.86 17.35 77.59 |
| AAU-net (Chen et al. 2022) | 56.91 20.30 48.24 86.63 16.46 78.42 |
| TransFuse (Chen et al. 2022) | 44.42 24.40 35.54 74.39 20.87 62.44 |
| TransUnet (Chen et al. 2021) | 51.75 22.10 43.42 85.38 17.37 76.84 |
| MISSFormer (Huang et al. 2022) | 58.18 21.35 48.26 84.16 17.99 75.16 |
| H2Former (He et al. 2023a) | 58.22 19.70 48.83 85.79 17.82 77.31 |
| SwinUNETR (Hatamizadeh et al. 2021) | 60.00 18.85 49.99 73.23 14.29 62.66 |
| nnFormer (Zhou et al. 2023) | 60.61 18.45 50.76 78.94 13.73 67.55 |
| UNETR (Hatamizadeh et al. 2022) | 60.97 18.75 50.81 75.27 13.63 65.38 |
| nnU-Net (Isensee et al. 2021) | 63.18 18.45 52.91 84.52 12.09 75.27 |
| MedNeXt (Roy et al. 2023) | 64.14 18.05 53.80 83.73 12.77 74.06 |
| SAMCT-Sub | 77.66 15.90 65.76 91.40 12.29 84.73 |
| SAMCT-CT5M | 64.49 19.45 52.88 87.23 4.33 87.57 |
| methods across the two datasets. Quantitative comparison |
| results of different methods on the invisible BTCV (Land- |
| man et al. 2015) dataset are summarized in Table 7. Ob- |
| viously, task-specific methods perform poorly on invisible |
| data due to domain shift. Comparatively, the performance of |
| SAMCT is much better, with average Dice scores of 86.32% |
| and 90.91% by SAMCT-Sub and SAMCT-CT5M, respec- |
| tively. Benefiting from the construction of CT5M, though |
| SAMCT-CT5M performs slightly worse in visible datasets |
| due to the lower proportion of training targets compared to |
| SAMCT-Sub, its performance on invisible datasets is much |

## Dice comparison of SAMCT and SOTA specific models on the training invisible BTCV

| Method | Liv | Spl | Lkid | Rkid | Sto | Gal | Eso | Pan | Avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPFNet (Feng et al. 2020) | 64.25 | 4.96 | 3.13 | 1.34 | 24.75 | 0.00 | 6.24 | 0.00 | 13.08 |
| U-Net (Ronneberger, Fischer, and Brox 2015) | 77.22 | 19.46 | 22.80 | 15.80 | 12.89 | 3.52 | 7.92 | 1.50 | 20.14 |
| CA-Net (Gu et al. 2020) | 70.77 | 28.18 | 10.82 | 16.04 | 23.46 | 0.54 | 31.02 | 3.42 | 23.03 |
| AAU-net (Chen et al. 2022) | 78.18 | 30.96 | 29.60 | 32.18 | 19.61 | 0.14 | 25.29 | 1.50 | 27.18 |
| TransUNet (Chen et al. 2021) | 68.67 | 9.46 | 1.71 | 0.74 | 19.08 | 3.58 | 2.43 | 1.60 | 13.41 |
| TransFuse (Zhang, Liu, and Hu 2021) | 77.13 | 4.04 | 4.73 | 3.76 | 14.55 | 3.33 | 0.40 | 0.01 | 13.49 |
| MISSFormer (Huang et al. 2022) | 65.45 | 21.74 | 8.75 | 2.99 | 15.35 | 3.68 | 9.26 | 2.68 | 16.24 |
| H2Former (He et al. 2023a) | 77.34 | 21.57 | 0.84 | 2.47 | 36.95 | 0.15 | 13.28 | 4.32 | 19.62 |
| SwinUNETR (Hatamizadeh et al. 2021) | 84.24 | 68.03 | 69.36 | 74.58 | 54.11 | 32.29 | 38.19 | 30.44 | 56.41 |
| nnFormer (Zhou et al. 2023) | 85.16 | 72.20 | 69.89 | 75.76 | 54.60 | 44.08 | 44.04 | 33.59 | 59.91 |
| UNETR (Hatamizadeh et al. 2022) | 84.49 | 66.32 | 71.66 | 76.83 | 55.22 | 30.32 | 36.60 | 32.98 | 56.80 |
| nnU-Net (Isensee et al. 2021) | 91.03 | 78.55 | 84.93 | 85.87 | 67.63 | 59.89 | 75.09 | 54.09 | 74.64 |
| MedNeXt (Roy et al. 2023) | 90.09 | 82.35 | 79.26 | 80.34 | 63.58 | 55.91 | 67.96 | 47.73 | 70.90 |
| SAMCT-Sub | 89.98 | 95.29 | 90.98 | 90.56 | 85.23 | 84.15 | 83.74 | 70.63 | 86.32 |
| SAMCT-CT5M | 96.33 | 96.13 | 93.38 | 93.13 | 91.14 | 82.99 | 82.72 | 91.42 | 90.91 |

## Component-wise ablation study of SAMCT on the COVID-19-20

| CNN CBI Adapter Dice | HD | IOU |
| --- | --- | --- | --- |
| • | • | • | 76.20 27.56 62.43 |
| • | • | • | 75.35 28.28 61.39 |
| • | • | • | 75.63 26.03 61.62 |
| • | • | • | 74.90 31.23 61.21 |

## Dice comparison of different prompts on objects from the WORD dataset. Cpoint+bbox represents using the joint center point and bounding box prompt. .82 94.23 94.22 93.77 93.98 task-indicator 95.30 94.03 94.29 94.50 92.96 92.99

| Prompt Mode | Liv | Spl | Lkid | Rkid | LHF | RHF |
| --- | --- | --- | --- | --- | --- | --- |
| random ponit | 90.18 93.82 93.50 91.40 90.11 91.54 |
| center point | 86.71 93.6 92.77 93.60 90.69 91.94 |
| random box | 95.27 94.57 93.62 93.66 92.90 93.66 |
| bounding box | 95.46 94.67 93.77 93.90 93.05 93.72 |
| cpoint+bbox | 95.49 94 |  |  |  |  |

### Formule


$$F 16 ∈ R 16dc× H 16 × W$$

### Formule


$$F 32 ∈ R 8dc× H 8 × W 8 , F 64 ∈ R 4dc× H 4 × W 4 , F 128 ∈ R 2dc× H 2 × W 2 , F 256 ∈ R dc×H×W are generated.$$

### Formule


$$F p ∈ R 1×dp in F trans correspond to a k × k window F w ∈ R k 2 ×dw in F cnn$$

### Formule


$$F c = Softmax( F p E q (F w E k ) T d p )(F w E v ),(1)$$

### Formule


$$A w = Softmax( F p (F w E w ) T d p ), A * w = e Aw-k -2 1 + e Aw-k -2 + 0.5,(2)$$

### Formule


$$A p ∈ R 1×1 of F p into A * p ∈ R k×k , A * w is multiplied by A *$$

### Formule


$${F ′ } = {F ′ 16 , F ′ 32 , F ′ 64 , F ′ 128 , F ′ 256 , F ′ vit }.$$

### Formule


$$A -= Softmax( P -E q -(F -E k -) T d p ), P e -= Gelu((A -(F -E v -))E -E 1 )E 2 ,(3)$$

### Formule


$$E q -, E k -, E v -, E -, E 1$$

### Formule


$$p = Softmax(A + (F + E v + )E + E c ),(4)$$
