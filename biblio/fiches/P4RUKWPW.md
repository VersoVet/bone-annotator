# Language-Guided Segmentation of Medical Images: A Review of Foundation Models.

**Auteurs** : Saqib Qamar
**Année** : 2026
**DOI** : 10.3390/bioengineering13070803

## Résumé

Vision-language foundation models have transformed medical image segmentation over the past three years. These models pair large image encoders with text prompts, so a single model can segment many anatomical structures, lesion types, and imaging modalities through natural language. This survey reviews vision-language foundation models designed for medical image segmentation. We describe the technical background from contrastive vision-language pretraining to the Segment Anything Model and its medical variants. We propose a three-part taxonomy that covers text-prompt-guided models, large-language-model-embedded architectures, and hybrid frameworks. We examine adaptation strategies such as full fine-tuning, Low-Rank Adaptation, adapters, and prompt engineering. We organize the literature by modality and cover computed tomography, magnetic resonance imaging, pathology, chest radiography, and ultrasound. We discuss clinical uses such as organ segmentation, tumor delineation, and radiother

## Méthodologie

{'study_design': "Revue narrative structurée avec recherche documentaire par mots-clés (termes de segmentation, termes médicaux, noms de méthodes), criblage par titre/résumé puis par texte intégral selon critères d'inclusion/exclusion, suppression des doublons, puis extraction de données (année, architecture, modalité cible, jeux de données d'entraînement/évaluation, stratégie d'adaptation, Dice maximal rapporté, statut de peer-review, disponibilité du code) pour les méthodes retenues", 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': 'Période de recherche couvrant les publications de 2021 à janvier 2026, avec emphase sur 2024-2026', 'setting': None}

## Résultats

{'quantitative': [{'outcome': "Taille de l'ensemble d'entraînement de SAM (Segment Anything Model)", 'value': "plus d'un milliard de masques sur onze millions d'images", 'unit': 'masques / images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background - Segment Anything and Medical Variants', 'source_quote': 'Trained on over one billion masks across eleven million images, it accepts visual prompts (points, boxes, rough masks) and returns a mask via a heavy Vision Transformer image encoder'}, {'outcome': "Taille de l'ensemble de données de MedSAM", 'value': 'plus de 1,5 million de paires image-masque sur dix modalités', 'unit': 'paires image-masque', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background - Segment Anything and Medical Variants', 'source_quote': 'It collected more than 1.5 million image-mask pairs across ten modalities and fine-tuned the SAM mask decoder while keeping the image encoder mostly frozen, using bounding-box prompts.'}, {'outcome': "Taille de l'ensemble de données de SAM-Med2D", 'value': "environ 4,6 millions d'images et 19,7 millions de masques", 'unit': 'images / masques', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background - Segment Anything and Medical Variants', 'source_quote': 'SAM-Med2D scaled the dataset to roughly 4.6 million images and 19.7 million masks and added encoder adapter layers to bridge the natural-medical gap'}, {'outcome': 'Score de Dice médian de BiomedParse', 'value': 'supérieur à 90%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Method Taxonomy - Text-Prompt-Guided Segmentation', 'source_quote': 'reaching a median Dice score above 90% and outperforming bounding-box methods on irregular shapes'}, {'outcome': 'Proportion de paramètres mis à jour par SAM2LoRA', 'value': 'moins de 5%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Background - Segment Anything and Medical Variants', 'source_quote': 'SAM2LoRA reaches state-of-the-art retinal fundus segmentation while updating fewer than five percent of the parameters'}, {'outcome': "Taille de l'ensemble de données BiomedParseData", 'value': 'six millions de triplets image-masque-description harmonisés depuis 45 jeux de données', 'unit': 'triplets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Benchmark Datasets', 'source_quote': 'the CVPR 2025 challenge adds 3D benchmark data [22]... BiomedParseData provides six million image-mask-description triples harmonized from forty-five datasets with GPT-4 [21]'}, {'outcome': 'Taille du jeu de données MIMIC-CXR', 'value': 'plus de 370 000 images avec rapports en texte libre', 'unit': 'images', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Modality Review - Chest Radiography', 'source_quote': 'MIMIC-CXR alone contains more than 370,000 images with free-text reports'}], 'qualitative_findings': ['SAM fonctionne bien sur des objets à fort contraste avec des frontières claires mais peine sur les petites lésions, les structures à faible contraste et les volumes 3D', "La radiographie thoracique et la dermatologie surpassent le CT abdominal et l'histopathologie dans les évaluations zero-shot de SAM", "Les modèles contrastifs ont tendance à ignorer la négation dans les prompts textuels (ex: 'foie sans tumeur' ressemble à 'foie avec tumeur')", 'Les prompts compositionnels combinant plusieurs contraintes ne sont que partiellement gérés, même par des modèles de raisonnement comme LISA'], 'main_findings': ["Les modèles vision-langage ont transformé la segmentation d'images médicales en trois ans, un seul modèle pouvant segmenter de nombreuses structures anatomiques, types de lésions et modalités d'imagerie via le langage naturel", "La période 2024-2026 a produit plus d'avancées que la décennie précédente dans ce domaine", 'Des modèles comme BiomedParse, MedSAM2 et SAT segmentent désormais de nombreuses modalités et structures à partir de prompts textuels, tandis que LoRA et les adapters rendent le déploiement pratique', "Quatre défis ouverts majeurs ont été identifiés : la dépendance aux prompts, l'hallucination de masques, la lenteur de l'inférence volumétrique (3D), et les données annotées limitées", 'La grande majorité des modèles examinés sont des prototypes de recherche évalués rétrospectivement sur des benchmarks publics, non des outils validés cliniquement']}

## Conclusions

Cette revue a examiné les modèles de fondation vision-langage pour la segmentation d'images médicales à travers le contexte technique, une taxonomie en trois parties, les stratégies d'adaptation, et la littérature organisée par modalité et application clinique Les progrès ont été rapides, la période 2024-2026 ayant produit plus d'avancées que la décennie précédente Quatre défis ouverts ont été identifiés : la dépendance aux prompts, l'hallucination, la vitesse d'inférence, et la rareté des données Le potentiel bénéfice clinique est substantiel (réduction du temps et du coût de segmentation, résultats plus cohérents entre institutions, nouvelles applications comme le report radiologique ancré et l'aide à la décision conversationnelle) mais la plupart de ces bénéfices restent à démontrer par une validation clinique prospective plutôt que par des benchmarks rétrospectifs

## Overview of vision-language and segmentation foundation models for medical images. The table covers fifty-three methods from 2021 to 2026, grouped into six categories. Reported Dice values are the peak values stated by the original authors on their own benchmarks. These Dice scores are not directly comparable and do not constitute a ranking, because they were obtained on different datasets, modalities, tasks, label definitions, and evaluation protocols; they are listed only to indicate the order of magnitude of reported performance within each method's own setting. A dash (-) indicates that a single Dice score was not reported.

| Method | Year | Architecture | Modality | Datasets | Dice Adaptation |
| --- | --- | --- | --- | --- | --- | --- |
| SAM-Based Models |  |  |  |  |  |
| SAM [9] |  | ViT-H + prompt enc. | Natural images | SA-1B (1B masks) | - | Pretrain |
| MedSAM [43] |  | SAM + medical FT | Multi-modal | 1.5M med. image pairs | 0.85 | Full FT |
| SAM-Med2D [72] |  | SAM + adapter | 10 modalities | 4.6M imgs, 19.7M masks | 0.83 | Adapter |
| SAM-Med3D [73] |  | Native 3D SAM | Volumetric | 21K imgs, 131K masks | 0.78 | Full FT |
| SAMed [85] |  | SAM + LoRA | Multi-organ CT | Synapse BTCV | 0.82 | LoRA (0.1%) |
| Med-SA [76] |  | SAM + Adpt. + LoRA | 5 modalities | 17 tasks | 0.84 | Adpt. + LoRA |
| AdaptiveSAM [83] |  | SAM + bias tuning | Surg., US, X-ray | Multiple | 0.81 | Bias tuning |
| SegVol [79] |  | Volumetric SAM | CT | 200 organs, 96K vol. | 0.83 | Full FT |
| 3DSAM-adapter [84] |  | SAM 2D→3D adapt. | CT (tumour) | LiTS, KiTS, pancreas CT | 0.86 | Adapter |
| SAM-OCTA [120] |  | SAM + OCTA prompt tuning | Retinal OCTA | ROSE, OCTA-500 | 0.87 | Full FT |
| SAM2LoRA [88] |  | SAM 2 + LoRA | Retinal fundus | 11 datasets | 0.93 | LoRA (<5%) |
| MedSAM2 [77] |  | SAM 2 + medical FT | Image + video | Multi-modal | 0.86 | Full FT |
| MedSAM3 [87] |  | SAM 3 + LoRA | Multi-modal | Concept-aware | 0.84 | LoRA |
| EmbedMedSAM [121] SAM embed. + edge optim. | Multi-modal | Resource-limited settings | 0.82 | Adapter |
| Text-Prompt-Guided Models |  |  |  |  |
| LViT [20] |  | U-Net + text fusion | Chest X-ray | QaTa-COV19 | 0.83 | Full FT |
| Cross-modal CR [95] |  | Cross-modal recon. CLIP | CT, MRI | Multiple organ datasets | 0.84 | Full FT |
| CLIP-Driven UM [19] |  | CLIP queries + Swin | Abdominal CT | BTCV, LiTS, KiTS | 0.86 | Full FT |
| Universal VLM [99] |  | Extensible CLIP + dec. | Abdominal CT/MRI BTCV, 15 organs | 0.87 | PEFT |
| ZePT [93] |  | CLIP query disentangle | Pan-tumour CT | Multi-source | 0.77 | Self-prompt |
| BiomedParse [21] |  | SEEM + GPT-4 harm. | 9 modalities | BiomedParseData (6M) | 0.94 | Full pretrain |
| BiomedParse-V [22] |  | FVE + ISD module | CT, MRI, micro. | CVPR 2025 challenge | 0.86 | Full pretrain |
| MedSegX [100] |  | Generalist FM + open vocab | Multi-modal | 100+ datasets | 0.85 | Full pretrain |
| SAT [92] |  | CLIP + transf. dec. | Radiology | 70+ datasets | 0.84 | Full FT |

## Cont.

| Method | Year | Architecture | Modality | Datasets | Dice Adaptation |
| --- | --- | --- | --- | --- | --- | --- |
| LLM-Embedded Architectures |  |  |  |  |
| LISA [23] |  | MLLM + ⟨SEG⟩ tok. | Nat. + reasoning | ReasonSeg, refCOCO | - | Full FT (LLM) |
| LISA++ [24] |  | LISA + inst. reasoning | Nat. + medical | Extended ReasonSeg | - | Full FT |
| ChatRadio-Valuer [122] LLM + rad. impression dec. | Chest X-ray | Multi-inst. CXR | - | Full FT |
| MedPLIB [103] |  | MLLM + SAM-Med2D | Multi-mod. med. | MeCoVQA | 0.81 | LoRA + Adpt. |
| M3D [25] |  | 3D MLLM + decoder | 3D CT | M3D-Seg | 0.79 | Full FT |
| Show & Segment [123] |  | In-context MLLM + dec. | Multi-modal med. | 12 diverse datasets | 0.83 | Zero-shot |
| Hybrid and Other Frameworks |  |  |  |  |
| MedCLIP-SAM [113] |  | MedCLIP + SAM | Multi-modal | Multiple | 0.80 | Hybrid |
| SaLIP [114] |  | SAM + CLIP cascade | Multi-modal | Multiple | 0.74 | Zero-shot |
| VILA-M3 [96] |  | VLM + medical expert know. | Multi-modal | BTCV, LiTS, BraTS | 0.86 | PEFT |
| SegFM3D [80] |  | 3D foundation model | Multi-modal 3D | Multi-source | 0.83 | Pretrain |
| Specialized Foundation Models |  |  |  |  |
| MoME (lesion) [124] |  | Mixture of mod. experts | Brain MRI lesions | Multi-source MRI | 0.80 | Full FT |
| UniverSeg [125] |  | Few-shot universal | 16 modalities | MegaMedical | 0.72 | Few-shot |
| GenSeg [126] |  | Diffusion gen. + seg. | Multi-modal | Ultra low-data regimes | 0.81 | Hybrid gen. |
| SegMamba-V2 [127] |  | Mamba SSM 3D long-range | Volumetric CT/MRI Multi-organ 3D | 0.88 | Full FT |
| TotalSeg. [39] |  | nnU-Net based | CT (104 structs.) | 1204 CTs | 0.94 | Full train |
| TotalSeg. MRI [40] |  | Seq.-independent | MRI (multi-organ) | 616 MRI + 527 CT | 0.84 | Full train |
| BrainSegFounder [128] |  | Self-sup. 3D ViT | Brain MRI | Multi-source neuroimaging | 0.91 | PEFT |
| SAMUS [81] |  | SAM + US adapt. | Ultrasound | Multi-source US | 0.80 | Adapter |
| SegAnyBone [82] |  | SAM + bone FT | MRI bones | Multi-seq. MRI | 0.82 | Full FT |
| Self-imp. FM [129] |  | Generative FM + self-imp. | CT, MRI, X-ray | Multi-organ, multi-modal | 0.85 | Full pretrain |
| LCTfound [130] |  | Lung CT ViT FM | Chest CT | LIDC-IDRI, NLM, LUNA16 | 0.89 | Full pretrain |
| Merlin [131] |  | CT VLM + report gen. | Chest CT | Radiology reports + seg. | - | Full pretrain |
| Decipher-MR [132] |  | 3D MRI VLM encoder | Multi-seq. MRI | Diverse MRI tasks | - | Full pretrain |
| CT-CLIP [59] |  | Volumetric CLIP | Chest CT | CT-RATE (50K) | - | Pretrain |
| Deep Learning Baselines (CNN/Transformer, no text prompt) |  |  |  |
| Confidence-SS [133] |  | CNN-Trans. semi-sup. | Skin lesion | ISIC 2016, PH2 | 0.91 | Semi-supervised |
| H-Self-Support [134] |  | Hierarchical self-support | Brain MRI (tumour) | BraTS 2021 | 0.92 | Self-supervised |
| Dense Enc.-Dec. [102] |  | CNN enc.-dec. skip conn. | Skin lesion | ISIC 2018, PH2 | 0.87 | Full FT |
| RD2A [2] |  | Residual dense + ASPP | Brain MRI (tumour) | BraTS 2019 | 0.89 | Full FT |
| ScaleFusionNet [101] |  | Trans. multi-scale FPN | Skin lesion | ISIC 2017/2018, PH2 | 0.90 | Full FT |
| UNet-Mamba [5] |  | UNet + Mamba-like attn. | Multi-modal | ACDC, Synapse, polyp sets | 0.91 | Full FT |

## Comparison of adaptation strategies for vision-language foundation models. The choice depends on dataset size, deployment scenario, and accuracy requirements.

| Strategy | Trainable GPU Mem. | Accuracy | Storage | Example |
| --- | --- | --- | --- | --- | --- |
| Full fine-tuning | 100% | Very high | Highest | Full model copy | MedSAM |
| LoRA | 0.1-1% | Low | Near best | Small adapter | SAMed |
| Adapter modules | 1-5% | Low | Strong | Small modules | Med-SA |
| Bias tuning | <0.5% | Very low | Good | Bias deltas only | AdaptiveSAM |
| Visual prompt tuning <0.1% | Minimal | Variable | Prompt tokens | VPT variants |
| Prompt engineering | 0% | None | Variable | Text only | BiomedParse |
| Conv-LoRA | 0.5-2% | Low | Strong | Small modules | Conv-LoRA SAM |
| NAS-LoRA | 1-3% | Low | Strong | Searched arch | NAS-LoRA |
| DoRA | 0.2-1% | Low | Strong | Magnitude+dir. | DoRA variants |

## Common evaluation metrics for medical image segmentation. The choice of metric depends on the clinical question and the structure that is segmented.

| Metric | Range | Property | Best Used for |
| --- | --- | --- | --- |
| Dice Score | [0, 1] | Overlap, small-structure sensitive | Volume overlap reporting |
| IoU (Jaccard) Hausdorff Distance 95% Hausdorff (HD95) Average Surface Dist. | [0, 1] [0, ∞) mm Worst-case boundary error Conservative overlap [0, ∞) mm Percentile boundary error [0, ∞) mm Mean boundary error | Detection metric comparison Outlier sensitivity studies Radiotherapy organs at risk Boundary quality reporting |
| Normalized Surface Dist. [0, 1] | Boundary within tolerance | Clinically acceptable boundary |
| Lesion-wise Dice | [0, 1] | Per-lesion overlap | Multi-focal disease |
| Sensitivity/Recall | [0, 1] | Detection rate | Screening applications |
| Specificity | [0, 1] | False-positive rate | Specificity-critical tasks |
| Recognition Accuracy | [0, 1] | Object presence detection | Text-prompted segmentation |

## Summary of widely used benchmark datasets for medical image segmentation, organized by modality. Recent datasets such as BiomedParseData and CT-RATE specifically support visionlanguage pretraining and text-prompted segmentation. Abdominal CT relies on BTCV, AMOS, FLARE, LiTS, KiTS, and the Medical Segmentation Decathlon [144,145,183-185]. Brain and cardiac MRI use the BraTS series and ACDC [150-152], and echocardiography adds EchoNet/EchoCLIP [153]. Chest X-ray benefits from MIMIC-CXR, CheXpert, PadChest, NIH ChestX-ray14, and VinDr-CXR [168], while pathology draws on Quilt-1M, PMC-CLIP, GLaS, and CAMELYON

| Dataset | Year | Modality | Size | Annotation Type Primary Use |
| --- | --- | --- | --- | --- | --- |
| BTCV (Synapse) |  | CT | 30 scans, 13 organs | Voxel mask | Multi-organ benchmark |
| AMOS22 |  | CT, MRI | 500 CT + 100 MRI, 15 organs Voxel mask | Multi-organ versatility |
| LiTS |  | CT | 131 scans (liver+tumor) | Voxel mask | Liver tumor segmentation |
| KiTS19/21 | 2019/21 CT | 300/489 scans | Voxel mask | Kidney tumor |
| FLARE 2022 |  | CT | 2200 unlabeled + 50 labeled Voxel mask | Low-resource segmentation |
| BraTS 2021 |  | MRI | 2000+ multi-seq cases | Voxel mask | Brain tumor segmentation |
| ACDC |  | MRI | 100 patients | Voxel mask | Cardiac chamber seg. |
| TotalSeg |  | CT | 1228 scans, 104 structs | Voxel mask | Universal anatomy |
| TotalSeg-MRI |  | MRI | 616 MRI + 527 CT, 80 structs Voxel mask | MRI universal |
| MIMIC-CXR |  | CXR | 377K images + reports | Image-text | VLP, classification |
| CheXpert |  | CXR | 224K images + labels | Image labels | Pathology classification |
| PadChest |  | CXR | 160K images + reports | Image-text | VLP |
| VinDr-CXR |  | CXR | 18K with bounding boxes | Bounding box | Detection |
| NIH ChestXray14 |  | CXR | 112K images | Image labels | Classification |
| MSD |  | Multi | 10 segmentation tasks | Voxel mask | Generalization |
| ISIC |  | Dermatology | 25K images | Mask + class | Skin lesion |
| HAM10000 |  | Dermatology | 10K images | Class + mask | Skin lesion |
| BUSI |  | Ultrasound | 780 images | Mask | Breast lesion |
| Quilt-1M |  | Pathology | 1M image-text pairs | Text caption | Pathology VLP |
| GLaS |  | Pathology | 165 H&E images | Mask | Gland segmentation |
| Camelyon16/17 | 2016/17 Pathology | 400+/1000+ WSI | Mask + class | Metastasis detection |
| BiomedParseData |  | 9 modalities | 6M image-mask-text | Mask + text | Text-prompted seg. |
| CT-RATE |  | Chest CT | 50K volumes + reports | Volume + text | 3D VLP |
| LIDC-IDRI |  | CT | 1018 lung nodule scans | Mask + class | Lung nodule |
| REFUGE2 |  | Retinal fundus 1200 images | Mask + class | Glaucoma assessment |

## Study-quality and evidence assessment of the main models reviewed. Columns report peerreview status, approximate training-data scale, whether external or multi-site validation is reported, the qualitative risk that public evaluation benchmarks overlap large or web-scale pretraining corpora (data leakage), open code, and clinical validation status. Overlap risk is a qualitative judgment, not a measured quantity. Very few reviewed models report prospective or multi-site external clinical validation, which is the main gap between reported benchmark performance and clinical readiness.

| Model | Peer Review | Train-Data Scale | External/Multi-Site Val. | Leakage Risk | Open Code Clinical Validation |
| --- | --- | --- | --- | --- | --- | --- |
| MedSAM [43] | Peer-rev. | 1.5M image-mask pairs, 10 modalities | Held-out internal; limited external | Moderate | Yes | None (prospective) |
| SAM-Med2D [72] | Preprint | 4.6M images, 19.7M masks | Internal; limited external | Moderate | Yes | None |
| CLIP-Driven UM [19] Peer-rev. | 14 partial-label CT datasets | BTCV/LiTS/KiTS cross-dataset splits; some | Moderate | Yes | None |
|  |  |  | Held-out; |  |  |  |
|  |  | 6M triples, 45 | presence |  |  |  |
| BiomedParse [21] | Peer-rev. | datasets, 9 | discriminator; | High | Yes | None |
|  |  | modalities | limited external |  |  |  |
|  |  |  | sites |  |  |  |
| BiomedParse-V [22] | Peer-rev. (wksp) | Volumetric extension of above | CVPR 2025 challenge data | High | Partial | None |
| SAT [92] | Peer-rev. | 70+ CT/MRI/PET | Cross-dataset radiology | High | Yes | None |
|  |  | datasets | (public) |  |  |  |
| LISA [23] | Peer-rev. | Reasoning-seg + refCOCO (natural) | Natural-image benchmarks | N/A (general) Yes | None |
|  |  | MeCoVQA |  |  |  |  |
| MedPLIB [103] | Peer-rev. | region-text | Internal | Moderate | Yes | None |
|  |  | dataset |  |  |  |  |
|  |  | Reuses |  |  |  |  |
| MedCLIP-SAM [113] | Peer-rev. | MedCLIP + SAM (no | Multiple public sets | Moderate | Yes | None |
|  |  | retrain) |  |  |  |  |
| SaLIP [114] | Peer-rev. (wksp) | Training-free (zero-shot) | Multiple public sets | Low | Yes | None |
| SegVol [79] | Peer-rev. | 96K unlabeled + 6K labeled CT vol. | Internal held-out | Moderate | Yes | None |
| MedSAM2 [77] | Preprint | Multi-modal image + video | Internal | Moderate | Yes | None |
| TotalSegmentator [39] Peer-rev. | 1204 CT, 104 structures | Reproduced across sites; adopted in workflows | Low | Yes | Partial (re-search/some clinical) |
| UniverSeg [125] | Peer-rev. | MegaMedical, 16 modalities (few-shot) | Cross-dataset few-shot | Moderate | Yes | None |
| CT-CLIP/Merlin [59] | Peer-rev. | 50K CT volumes + reports | Held-out CT-RATE; zero-shot | High | Partial | None |
|  |  | (CT-RATE) | detection |  |  |  |
