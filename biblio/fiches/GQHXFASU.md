# Towards a general computed tomography image segmentation model for anatomical structures and lesions

**Auteurs** : Xi Ouyang, Dongdong Gu, Xuejian Li, Wenqi Zhou, Qianqian Chen, Yiqiang Zhan, Xiang Sean Zhou, Feng Shi, Zhong Xue, Dinggang Shen
**Année** : 2024
**DOI** : 10.1038/s44172-024-00287-0

## Résumé

Numerous deep-learning models have been developed using task-specific data, but they ignore the inherent connections among different tasks. By jointly learning a wide range of segmentation tasks, we prove that a general medical image segmentation model can improve segmentation performance for computerized tomography (CT) volumes. The proposed general CT image segmentation (gCIS) model utilizes a common transformer-based encoder for all tasks and incorporates automatic pathway modules for task prompt-based decoding. It is trained on one of the largest datasets, comprising 36,419 CT scans and 83 tasks. gCIS can automatically perform various segmentation tasks using automatic pathway modules of decoding networks through text prompt inputs, achieving an average Dice coefficient of 82.84%. Furthermore, the proposed automatic pathway routing mechanism allows for parameter pruning of the network during deployment, and gCIS can also be quickly adapted to unseen tasks with minimal training samples while maintaining great performance.

## Méthodologie

{'study_design': 'gCIS consists of three sub-structures: (1) A transformer-based encoder that extracts features from various medical images and forms a common interactive latent space; (2) a prompt text encoder that provides prompt embedding to guide the sub-pathway selection through the routing layers; and (3) a decoder that processes data through different sub-pathways to generate the corresponding segmentation results based on automatic routing using the AP modules.', 'intervention': "Transformer-based image encoder: adapted Swin transformer into a 3D structure consisting of four stages, each containing two transformer blocks using regular-window-partitioning multi-head self-attention modules; patch embedding layer with patch size of 2 × 2 × 2 and 48 output channels; five-level downsampling operations with 1/2 scale; 8.06 million parameters total; partial weights transferred from ImageNet pre-trained weights, rest randomly initialized. Prompt encoder: text prompts for each segmentation task (e.g., 'pulmonary arteries', 'heart') encoded via a pre-trained text encoder (63 million parameters, 12 layers, width of 512, 8 attention heads) passed to each AP module. Decoder with automatic pathway modules: seven AP modules along the decoding pipeline; deconvolutional layers connect the first five AP modules to restore feature map resolution; last two AP modules process feature maps at original resolution; each AP module consists of a fully connected routing layer and M=6 sub-pathways formed by residual blocks; routing layer calculates probability of selecting each sub-pathway and picks the most suitable one; output feature maps from encoder at each resolution concatenated with outputs from previous decoder stage via skip connection.", 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ["L'article présente une comparaison entre le modèle proposé gCIS et d'autres méthodes de l'état de l'art, démontrant sa performance supérieure en tant que modèle de fondation", "Des études d'ablation sont introduites pour évaluer l'efficacité du pré-entraînement multi-tâches à grande échelle", "gCIS démontre une grande performance d'adaptation à des tâches préalablement non vues (unseen tasks)"], 'main_findings': ["gCIS surpasse les méthodes état de l'art existantes selon les résultats comparatifs présentés", "Le pré-entraînement multi-tâches à grande échelle a un effet bénéfique démontré par les études d'ablation", "gCIS s'adapte avec de bonnes performances à de nouvelles tâches non vues lors de l'entraînement"]}

## Conclusions

gCIS, un modèle général de segmentation d'images CT équipé d'un encodeur basé sur les transformers et de décodeurs sélectifs à chemins adaptatifs (AP), améliore efficacement les performances des tâches de segmentation et élimine les effets secondaires des tâches aberrantes observés dans le MTL traditionnel Le module AP permet la sélection automatique de sous-chemins, permettant à plusieurs tâches de partager des caractéristiques communes tout en conservant des paramètres spécifiques à la tâche Pour de nouvelles tâches, les chemins les plus analogues peuvent être automatiquement identifiés à partir de la couche de routage sur la base du prompt textuel, puis affinés davantage, ce qui simplifie et accélère la création de nouveaux modèles Le modèle multi-tâches gCIS enrichi de modules AP démontre une performance supérieure comparée à ses homologues mono-tâches, ce qui souligne l'effet synergique de l'utilisation de davantage de tâches de segmentation et de leurs données associées gCIS démontre sa supériorité par rapport à d'autres modèles état de l'art optimisés indépendamment pour chaque tâche Le clustering des pathways montre que des tâches similaires se regroupent naturellement, indiquant des corrélations robustes entre les tâches de segmentation gCIS peut être élagué (pruned) en modèles plus petits spécifiques à une tâche avec des paramètres réseau réduits, illustrant son adaptabilité pour un déploiement pratique

## Quantitative comparison of Dice scores (%) for segmentation of 6 non-tubular-structure organs and 1 tumor, and clDice scores (%) for 7 tubular-structure organs Mean and standard deviation (mean ± std) of corresponding metrics are reported. nnU-Net and Cascaded Vb-Net are two state-of-the-art models, while the sole-path general computed tomography image segmentation (gCIS) model represents the gCIS model with no automatic pathway module and trained for individual tasks. The number of training and testing cases ("training/testing") are given below the task name. Two-tailed student's t-test is used to compare the results with those obtained by gCIS.

| Lung tumor (57/6) | 77.12 ± 11.08 | 59.11 ± 27.86 | 76.40 ± 7.65 | 69.76 ± 12.41 | 80.75 ± 8.71 | Head & neck artery (3664/729) | 81.64 ± 7.52* | 91.29 ± 3.42* | 91.70 ± 3.84* | 44.29 ± 10.07* | 93.28 ± 2.74 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Thyroid (334/38) | 89.23 ± 4.51 | 83.00 ± 7.35* | 85.15 ± 10.34* | 38.97 ± 11.45* | 88.90 ± 3.94 | Lower limbs artery (634/73) | 79.23 ± 6.71* | 75.80 ± 7.87* | 78.37 ± 7.06* | 18.91 ± 2.83* | 82.38 ± 6.21 |
| Cardiac (330/20) | 87.86 ± 10.19* | 91.26 ± 5.49 | 89.62 ± 8.71 | 83.54 ± 3.57* | 93.01 ± 3.48 | Aorta (1694/20) | 99.83 ± 0.50 | 96.46 ± 2.58* | 94.92 ± 6.67* | 68.87 ± 7.08* | 99.88 ± 0.35 |
| Sacrum (266/35) | 92.57 ± 16.17 | 90.54 ± 16.07 | 91.16 ± 15.77 | 78.76 ± 14.05* | 94.86 ± 1.32 | Pulmonary vein (352/20) | 90.29 ± 4.41 | 87.59 ± 5.86* | 88.38 ± 4.34* | 36.43 ± 5.99* | 92.08 ± 2.71 |
| Bladder (501/57) | 90.79 ± 7.80 | 86.13 ± 17.18* | 83.13 ± 13.41* | 76.90 ± 16.38* | 91.68 ± 5.62 | Pulmonary artery (1153/20) | 87.32 ± 2.97 | 85.88 ± 3.30* | 85.86 ± 4.13* | 37.03 ± 6.21* | 88.58 ± 2.46 |
| Lung (345/20) | 98.80 ± 0.29* | 98.14 ± 0.35* | 98.40 ± 0.36* | 97.16 ± 0.59* | 98.61 ± 0.29 | Coronary (6065/155) | 84.43 ± 6.86* | 88.10 ± 7.12* | 86.68 ± 5.89* | 41.74 ± 5.53* | 90.72 ± 5.10 |
| Stomach (1626/183) | 90.91 ± 10.80 | 91.59 ± 14.43 | 90.45 ± 11.94* | 77.86 ± 10.20* | 92.59 ± 8.29 | Airway (108/20) | 82.96 ± 3.50 | 78.49 ± 7.01* | 83.10 ± 5.66 | 35.00 ± 5.14* | 84.47 ± 3.37 |
| Method | nnU-Net | Cascaded Vb-Net | sole-path gCIS | MedSAM | gCIS | Method | nnU-Net | Cascaded Vb-Net | sole-path gCIS | MedSAM | gCIS |
| Metric | Dice (%) |  |  |  |  | Metric | clDice (%) |  |  |  |  |

## Comparison with general computed tomography image segmentation (gCIS) model and other methods for the segmentation of renal artery using different training examples

| Training Number | Method | Dice (%) | clDice (%) | Tsens (%) | Tprec (%) |
| --- | --- | --- | --- | --- | --- |
| 1 | nnU-Net | 82.56 ± 11.52 | 56.17 ± 15.02 | 41.88 ± 15.18 | 97.45 ± 2.18 |
|  | Cascaded Vb-Net | 71.53 ± 18.68 | 45.59 ± 12.85 | 27.99 ± 12.05 | 87.12 ± 10.51 |
|  | gCIS | 84.84 ± 5.44 | 67.04 ± 9.30 | 55.07 ± 8.39 | 87.30 ± 14.47 |
| 5 | nnU-Net | 89.81 ± 3.30 | 77.40 ± 8.58 | 65.45 ± 11.24 | 98.47 ± 1.56 |
|  | Cascaded Vb-Net | 85.79 ± 3.03 | 61.57 ± 9.95 | 47.13 ± 11.12 | 96.11 ± 4.12 |
|  | gCIS | 88.64 ± 3.23 | 80.77 ± 6.81 | 71.43 ± 8.64 | 94.30 ± 6.92 |
| 201 | nnU-Net | 92.19 ± 2.40 | 82.52 ± 4.74 | 72.76 ± 7.32 | 96.31 ± 2.96 |
|  | Cascaded Vb-Net | 88.94 ± 2.49 | 78.65 ± 7.05 | 67.68 ± 9.13 | 95.67 ± 2.84 |
|  | gCIS | 92.13 ± 2.38 | 86.18 ± 4.68 | 79.86 ± 8.59 | 94.24 ± 2.58 |

## Comparison with general computed tomography image segmentation (gCIS) model and other methods for the segmentation of renal vein

| Method | Dice (%) | clDice (%) | Tsens (%) | Tprec (%) |
| --- | --- | --- | --- | --- |
| nnU-Net | 90.76 ± 2.20 | 80.45 ± 5.34 70.04 ± 8.11 96.84 ± 2.76 |
| Cascaded | 88.66 ± 2.27 79.30 ± 6.15 68.29 ± 9.56 95.12 ± 1.13 |
| Vb-Net |  |  |  |  |
| gCIS | 90.53 ± 1.82 85.34 ± 3.84 78.85 ± 7.32 93.78 ± 3.89 |
| Mean and standard deviation (mean ± std) of the metrics are reported. |  |
