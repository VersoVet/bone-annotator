# TransNet-SAM2: A Transformer-Foundation Model Framework for Prompt-Free Segmentation of White Blood Cells in Microscopic Blood Smear Images.

**Auteurs** : Julius Bamwenda, Mehmet Siraç Özerdem, Orhan Ayyildiz, Veysi Akpolat, İrem Akpolat
**Année** : 2026
**DOI** : 10.3390/diagnostics16111737

## Résumé

Background: Accurate segmentation of white blood cells (WBCs) in peripheral blood smear images is a fundamental step in computational hematology, enabling downstream tasks such as classification, morphological assessment, and quantitative analysis. However, reliable segmentation remains challenging due to staining variability, complex cellular morphology, overlapping structures, and limited availability of high-quality annotations. Aim and Methods: The aim of this study is to develop a robust and fully automated segmentation framework for white blood cells (WBCs) in microscopic blood smear images, providing a reliable foundation for subsequent computational analysis. We propose TransNet–SAM2, a hybrid deep learning architecture that integrates hierarchical transformer-based feature extraction with a foundation-model-based decoder for prompt-free segmentation. Specifically, a Swin Transformer backbone is employed to capture multi-scale contextual representations, which are subsequently aligned and fused through a feature adaptation module. The fused features are directly injected into the SAM2 mask decoder, replacing conventional prompt-based conditioning and enabling fully automatic segmentation. In addition, a weakly supervised self-training strategy is incorporated to utilize partially annotated data, improving model generalization while reducing annotation requirements. The proposed framework is evaluated using a clinically curated dataset from Dicle University, the publicly available Raabin-WBC dataset, and an additional external leukemic blast validation dataset (ALL-IDB) to assess robustness under both routine and atypical hematological conditions. Results: TransNet-SAM2 achieved a Dice coefficient of 0.95 ± 0.01 and IoU of 0.90 on internal testing, significantly outperforming U-Net (0.89), Mask R-CNN (0.90), and SAM2 (0.92) (p &lt; 0.05). In cross-dataset evaluation (Dicle training, Raabin-WBC testing), the framework maintained strong performance (Dice: 0.91, IoU: 0.84), demonstrating robustness to domain shifts. Ablation studies confirmed each component’s contribution, with the full model improving Dice by 6% over a CNN baseline. Qualitative analysis showed accurate boundary delineation even with cell overlap and background clutter. Conclusions: These findings indicate that the proposed framework provides a promising and scalable framework for WBC segmentation. While the current study focuses on segmentation, future work will investigate integration with classification and radiomics pipelines, as well as validation on more diverse clinical datasets, including bone marrow and leukemia samples.

## Méthodologie

{'study_design': "Développement et validation d'un framework d'apprentissage profond hybride (TransNet-SAM2) combinant un backbone Swin Transformer, un module d'adaptation de caractéristiques, et un décodeur de masque SAM2 sans prompt, avec une stratégie d'auto-apprentissage faiblement supervisée", 'intervention': 'Segmentation automatisée par TransNet-SAM2, comparée à U-Net, Mask R-CNN et SAM2 (baselines)', 'control': 'Modèles de segmentation existants: U-Net, Mask R-CNN, SAM2 (prompt-based)', 'primary_outcomes': ['Dice coefficient', 'IoU (Intersection over Union)'], 'secondary_outcomes': ['Précision (precision)', 'Rappel (recall)', 'Robustesse au domain shift (évaluation cross-dataset)', 'Temps de calcul par patch'], 'statistical_methods': ['Test de significativité statistique (p < 0.05) pour comparaison entre TransNet-SAM2 et les méthodes de référence', "Études d'ablation"], 'duration': None, 'setting': "Analyse computationnelle d'images de frottis sanguins microscopiques numérisées (pathologie digitale / hématologie computationnelle)"}

## Résultats

{'quantitative': [{'outcome': 'Dice coefficient (test interne, Dicle University)', 'value': '0.95 ± 0.01', 'unit': None, 'confidence_interval': None, 'p_value': 'p < 0.05', 'effect_size': None, 'source_section': 'Results/Abstract', 'source_quote': 'TransNet-SAM2 achieved a Dice coefficient of 0.95 ± 0.01 and IoU of 0.90 on internal testing, significantly outperforming U-Net (0.89), Mask R-CNN (0.90), and SAM2 (0.92) (p < 0.05).'}, {'outcome': 'IoU (test interne, Dicle University)', 'value': '0.90', 'unit': None, 'confidence_interval': None, 'p_value': 'p < 0.05', 'effect_size': None, 'source_section': 'Results/Abstract', 'source_quote': 'TransNet-SAM2 achieved a Dice coefficient of 0.95 ± 0.01 and IoU of 0.90 on internal testing, significantly outperforming U-Net (0.89), Mask R-CNN (0.90), and SAM2 (0.92) (p < 0.05).'}, {'outcome': 'Dice coefficient (évaluation cross-dataset, entraînement Dicle, test Raabin-WBC)', 'value': '0.91', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results/Abstract', 'source_quote': 'In cross-dataset evaluation (Dicle training, Raabin-WBC testing), the framework maintained strong performance (Dice: 0.91, IoU: 0.84), demonstrating robustness to domain shifts.'}, {'outcome': 'IoU (évaluation cross-dataset, entraînement Dicle, test Raabin-WBC)', 'value': '0.84', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results/Abstract', 'source_quote': 'In cross-dataset evaluation (Dicle training, Raabin-WBC testing), the framework maintained strong performance (Dice: 0.91, IoU: 0.84), demonstrating robustness to domain shifts.'}, {'outcome': "Amélioration du Dice du modèle complet par rapport à une baseline CNN (étude d'ablation)", 'value': '6%', 'unit': '% amélioration', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results/Abstract', 'source_quote': "Ablation studies confirmed each component's contribution, with the full model improving Dice by 6% over a CNN baseline."}, {'outcome': 'Précision (precision)', 'value': '0.96', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The reported precision (0.96) and recall (0.94) indicate that the model maintains both high specificity and sensitivity during segmentation, supporting its potential utility in automated blood smear analysis workflows.'}, {'outcome': 'Rappel (recall)', 'value': '0.94', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The reported precision (0.96) and recall (0.94) indicate that the model maintains both high specificity and sensitivity during segmentation, supporting its potential utility in automated blood smear analysis workflows.'}, {'outcome': "Amélioration du Dice par l'ajout de l'auto-apprentissage (self-training) - étude d'ablation", 'value': 'de 0.94 à 0.95', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The ablation study demonstrated that incorporating self-training improved the Dice score from 0.94 to 0.95, indicating that pseudo-labeled samples can provide useful complementary training information.'}, {'outcome': 'Temps de calcul par patch', 'value': '0.08', 'unit': 'secondes par patch', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The framework demonstrates computational efficiency (0.08 s per patch), supporting scalable analysis of large microscopy datasets.'}, {'outcome': 'Amélioration du Dice coefficient par rapport aux méthodes conventionnelles', 'value': '3-6%', 'unit': '% amélioration', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Discussion', 'source_quote': 'The proposed framework achieved a Dice coefficient of 0.95 on the Dicle University test set, representing a 3-6% improvement over conventional computational methods.'}], 'qualitative_findings': ['Analyse qualitative montrant une délinéation précise des frontières cellulaires même en cas de chevauchement des cellules et de fond encombré', 'Amélioration de la délinéation des frontières et de la séparation des instances par rapport aux méthodes de référence évaluées', 'Accord encourageant entre la quantification automatisée des leucocytes dérivée de la segmentation et le comptage différentiel manuel réalisé par des experts (comparaison préliminaire)', "Difficultés occasionnelles dans les régions présentant un chevauchement cellulaire sévère, une agrégation dense d'érythrocytes, des artefacts de coloration ou un faible contraste entre le cytoplasme et l'arrière-plan"], 'main_findings': ['TransNet-SAM2 surpasse significativement U-Net, Mask R-CNN et SAM2 en segmentation interne des WBC (Dice 0.95, IoU 0.90, p<0.05)', 'Le framework maintient de bonnes performances en évaluation cross-dataset sans fine-tuning spécifique (Dice 0.91, IoU 0.84), démontrant une robustesse au domain shift', 'La conception sans prompt (prompt-free) permet une segmentation entièrement automatisée adaptée aux workflows de pathologie digitale à haut débit', "La stratégie d'auto-apprentissage faiblement supervisée réduit la dépendance aux annotations denses tout en maintenant des performances compétitives", 'Le framework a été validé avec succès sur des images externes de blastes leucémiques (ALL-IDB), démontrant sa robustesse dans des conditions hématologiques atypiques']}

## Conclusions

TransNet-SAM2 est un framework hybride combinant apprentissage contextuel basé sur transformer et décodage par modèle de fondation, permettant une segmentation automatisée et sans prompt des globules blancs Le framework répond à des défis importants de l'analyse d'images en hématologie computationnelle : dépendance aux prompts manuels, généralisation limitée entre datasets, et rareté des données annotées densément Les résultats expérimentaux démontrent une forte performance de segmentation sur les datasets Dicle University, Raabin-WBC et ALL-IDB dans des conditions variées de coloration, d'imagerie et de morphologie Le framework doit être considéré comme un outil computationnel de support et non comme un remplacement du diagnostic clinique expert, de la cytométrie en flux ou de l'interprétation hématologique complète Des travaux futurs devront valider le framework sur des datasets multicentriques plus larges et cliniquement hétérogènes, incluant des sous-types leucémiques, des populations cellulaires transitionnelles et des échantillons de moelle osseuse

## Summary of the datasets used in this study.

| Dataset | Image Source | Cell Classes | Patch Size | Annotation Type | Purpose |
| --- | --- | --- | --- | --- | --- |
| Dicle University | Peripheral blood smear WSIs | Blast, Neutrophil, Lymphocyte | 256 × 256 | Pixel-level (QuPath) | Training/Validation/Testing |
| Raabin-WBC | Public hematology dataset | Multiple WBC types | 256 × 256 | Pixel-level | Cross-dataset evaluation |
| ALL-IDB | Public leukemia microscopy dataset | Leukemic blast cells | 256 × 256 | Pixel-level/Expert annotation | External leukemic blast validation |

## 2, 3, 4} These hierarchical representations capture both local fine-grained details and global contextual dependencies across the image. TransNet Backbone Architecture Specification The TransNet backbone employs the Swin Transformer architecture (Swin-Tiny) with 4 hierarchical stages. Each stage contains 2, 2, 6, and 2 transformer blocks respectively. The embedding dimension starts at 96 and doubles at each stage (96 → 192 → 384 → 768). Patch embedding uses a patch size of 4 × 4 pixels. Window sizes are set to 7 × 7 with shifted window partitioning in alternating blocks. Feature maps F 1 , F 2 , F 3 , F 4 are extracted

| at spatial resolutions of H 4 × W 4 , H 8 × W 8 , H 16 × W 16 , W 32 × W 32 , respectively. |
| --- |

## Summary of the datasets used in the study.

| Dataset | Total Im-ages/Patches | Patch Size | Train | Validation | Test/External Evaluation | Classes |
| --- | --- | --- | --- | --- | --- | --- |
| Dicle University | 14,720 patches | 256 × 256 | 10,304 | 2208 | 2208 | Blast, Neutrophil, Lymphocyte |
|  |  |  |  |  |  | Lymphocyte, Neutrophil, |
| Raabin-WBC | 11,200 patches | 256 × 256 | 7840 | 1680 | 1680 | Monocyte, Eosinophil, Basophil (used as unified |
|  |  |  |  |  |  | foreground) |
| ALL-IDB | 100 images | 256 × 256 | - | - | 100 | Leukemic blast cells |

## Training hyperparameters used for optimisation of the proposed TransNet-SAM2 framework.

| Parameter | Value |
| --- | --- |
| Optimizer | Adam |
| Initial learning rate | 1 × 10 -4 |
| Batch size | 8 |
| Number of epochs | 60 |
| Patch size | 256 × 256 |
| Loss function | BCE + Dice |
| Learning rate scheduler | Cosine decay |

## Segmentation performance comparison on the Dicle University dataset.

| Method | Dice | IoU | Precision | Recall |
| --- | --- | --- | --- | --- |
| U-Net | 0.89 ± 0.01 | 0.81 | 0.88 | 0.90 |
| Mask R-CNN | 0.90 ± 0.01 | 0.83 | 0.91 | 0.89 |
| StarDist | 0.91 ± 0.01 | 0.85 | 0.92 | 0.90 |
| TransUNet | 0.92 ± 0.01 | 0.86 | 0.91 | 0.90 |
| SAM-Adapter | 0.93 ± 0.01 | 0.87 | 0.94 | 0.92 |
| SAM2 | 0.92 ± 0.01 | 0.86 | 0.93 | 0.91 |
| TransNet-SAM2 | 0.95 ± 0.01 | 0.90 | 0.96 | 0.94 |

## Ablation study evaluating the contribution of each architectural component to overall segmentation performance (Dice coefficient).Note: ✓ indicates that the corresponding component is included in the configuration, whereas ✗indicates that the component is excluded.

| Configuration | TransNet Backbone | SAM2 Decoder | Cross-Scale Alignment | Self-Training | Dice |
| --- | --- | --- | --- | --- | --- |
| Baseline CNN | ✗ | ✗ | ✗ | ✗ | 0.89 |
| Transformer Backbone Only | ✓ | ✗ | ✗ | ✗ | 0.91 |
| TransNet + SAM2 | ✓ | ✓ | ✗ | ✗ | 0.93 |
| TransNet + SAM2 + Alignment | ✓ | ✓ | ✓ | ✗ | 0.94 |
| Full TransNet-SAM2 | ✓ | ✓ | ✓ | ✓ | ✓ |

## Cross-dataset segmentation performance (train: Dicle, test: Raabin-WBC).

| Method | Dice | IoU | Precision | Recall |
| --- | --- | --- | --- | --- |
| U-Net | 0.85 | 0.76 | 0.86 | 0.84 |
| StarDist | 0.87 | 0.79 | 0.88 | 0.86 |
| SAM2 baseline | 0.88 | 0.81 | 0.89 | 0.87 |
| TransNet-SAM2 (Proposed) | 0.91 | 0.84 | 0.92 | 0.90 |

## External validation results on leukemic blast cell segmentation using the ALL-IDB dataset.

| Method | Dice | IoU | Precision | Recall |
| --- | --- | --- | --- | --- |
| U-Net | 0.81 | 0.71 | 0.83 | 0.80 |
| StarDist | 0.84 | 0.75 | 0.85 | 0.83 |
| SAM2 baseline | 0.86 | 0.78 | 0.87 | 0.85 |
| TransNet-SAM2 (Proposed) | 0.89 | 0.82 | 0.90 | 0.88 |

## Correlation analysis between manual differential counts and TransNet-SAM2 segmentationderived leukocyte quantification, with breakdown by sample type.

| Cell Type | Sample Composition | Pearson r | p-Value |
| --- | --- | --- | --- |
|  | 15 peripheral blood smear |  |  |
| Neutrophils | samples (6 ALL, 4 AML, 5 | 0.93 | <0.001 |
|  | non-leukemia) |  |  |
|  | 15 peripheral blood smear |  |  |
| Lymphocytes | samples (6 ALL, 4 AML, 5 | 0.91 | <0.001 |
|  | non-leukemia) |  |  |
| Blast Cells | 10 leukemia samples (6 ALL, 4 AML) | 0.88 | <0.01 |

## Pearson correlation between TransNet-SAM2 automated quantification and flow cytometry reference counts.

| Cell Type | Pearson Correlation (r) | p-Value |
| --- | --- | --- |
| Neutrophils | 0.91 | <0.01 |
| Lymphocytes | 0.89 | <0.01 |
| Blast Cells | 0.87 | <0.05 |

### Formule


$$U-Net [4] ✗ ✓ ✗ ✗ Trans-UNet [11] ✓ ✓ ✗ ✗ SAM-Adapter [15] ✓ ✗ ✗ ✓ SAM2 [18] ✓ ✗ ✗ ✓ TransNet-SAM2 (Proposed) ✓ ✓ ✓ ✓$$

### Formule


$$H 4 × W 4 , H 8 × W 8 , H 16 × W 16 , H 32 × W 32$$

### Formule


$$F i ∈ R C i ×H i ×W i , i ∈ {1,$$

### Formule


$$F = { F 1 , F 2 , . . . F k },$$

### Formule


$$∼ F i = ϕ(F i ),$$

### Formule


$$∼ F i = U psample ∼ F i ,$$

### Formule


$$F aligned = k ∑ i=1 α i • Fi$$

### Formule


$$D = D -1 D -u$$

### Formule


$$ŷ-f iltered = y if max(p(x)) ≥ τ$$

### Formule


$$D -train = D -1 D -pseudo$$

### Formule


$$L -total = L -sup + λL -pseudo$$

### Formule


$$Algorithm 1 Weakly Supervised Self-Training 1. Train model f 0 using D -1 for E -warmup epoch 2. For each x ∈ D -u : Generatepseudo -label ŷ = f 0 (x), If confidence ≥ τ: Add (x, ŷ) to D -pseudo 3. Train model using D -1 D -pseudo 4. Repeat steps 2-3 for k iterations$$

### Formule


$$L BCE = - 1 N N ∑ i=1 [y i log( ŷi ) + (1 -y i )log(1 -ŷi )]$$

### Formule


$$L Dice = 1 - 2∑ N i=1 y i ŷi ∑ N i=1 y i + ∑ N i=1 ŷi$$

### Formule


$$L total = λ 1 L BCE + λ 2 L Dice$$

### Formule


$$L = L sup + λ L pseudo$$
