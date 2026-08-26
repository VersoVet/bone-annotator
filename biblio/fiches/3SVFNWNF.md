# Efficient Deep-Learning-Assisted Annotation for Medical Image Segmentation

**Auteurs** : Lichun Zhang, Zhi Chen, Honghai Zhang, Fahim Ahmed Zaman, Andreas Wahle, Xiaodong Wu, Milan Sonka
**Année** : 2023
**DOI** : 10.36227/techrxiv.23420516.v1

## Résumé

Image segmentation is a fundamental problem in medical image analysis.
Deep learning (DL) methods have achieved state-of-the-art (SOTA) results
in various medical image segmentation tasks. This success is largely
attributable to the use of large annotated datasets for training.
However, due to anatomical variations and complexity of medical image
data, annotations of large medical image datasets are not only
labor-intensive and time-consuming but also demand specialty-oriented
skills. In this paper, we report a novel segmentation quality assessment
(SQA) framework that combines active learning and assisted annotation to
dramatically reduce annotation effort both in image selection and
annotation querying from human experts. We propose a two-branch network
that integrates a spatial and channel-wise probability attention module
into the segmentation network to perform segmentation and predict
potential segmentation errors simultaneously. By directly assessing the
segmentation quality of

## Méthodologie

{'study_design': 'Revue narrative structurée selon le cadre PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) pour identifier et examiner les meilleures stratégies de segmentation de la paroi coronaire utilisant des techniques basées sur les transformers, évaluant leurs caractéristiques, leur rigueur scientifique et leur pertinence clinique', 'intervention': "Analyse des mécanismes d'auto-attention (self-attention) tels que proposés par Vaswani et al., architecture transformer composée de composants encodeur-décodeur (réseau feed-forward et couche d'auto-attention), extraction de patchs, encodage positionnel, et fusion des transformers avec les architectures de deep learning (notamment CNNs)", 'control': None, 'primary_outcomes': ['Précision de la segmentation des frontières lumen-intima (LI) et media-adventitia (MA) dans les scans IVUS', 'Précision diagnostique améliorée par les modèles transformers et attention'], 'secondary_outcomes': ['Identification des biais dans les systèmes de deep learning pour la segmentation IVUS', "Intégration de l'IA explicable (XAI) dans les structures DL"], 'statistical_methods': ["Analyse statistique descriptive des articles sélectionnés (processus de segmentation, métriques de performance, optimiseurs, fonctions de perte, taux d'apprentissage)"], 'duration': None, 'setting': "Revue de littérature scientifique dans le domaine de l'imagerie médicale (IVUS) et de l'intelligence artificielle"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['La segmentation manuelle en IVUS est chronophage, laborieuse et sujette aux erreurs, ce qui a motivé le développement de méthodes automatisées.', 'Les méthodes traditionnelles (seuillage, contours actifs, techniques basées sur les graphes) reposent sur des modèles mathématiques pour identifier les frontières des tissus mais peinent souvent face à la complexité et à la variabilité des images IVUS.', "L'approche de Kermani et al. détecte efficacement les bordures avec précision.", 'Le modèle de Giannoglou et al. propose une segmentation automatisée.', "Les avancées en ML fournissent des solutions robustes et adaptables : les MRF intègrent le contexte spatial, tandis que les RF et SVM utilisent des modèles statistiques et l'apprentissage d'ensemble pour améliorer la précision et gérer la variabilité des images IVUS.", 'Le DL, en particulier les CNN, a révolutionné la segmentation IVUS ; des architectures comme UNet et ses variantes améliorent la performance en apprenant des caractéristiques hiérarchiques à partir des données brutes.', "Des architectures avancées comme MFA-UNet et IVUS-UNet++ améliorent la précision et l'efficacité en incorporant l'agrégation de caractéristiques multi-échelles.", "Les mécanismes d'attention et les transformers, empruntés au traitement du langage naturel, capturent les dépendances à long terme et le contexte, éléments cruciaux pour la segmentation IVUS.", "Les modèles comme POST et MSP-GAN démontrent des améliorations significatives de la précision de segmentation grâce à l'incorporation du contexte temporel, de l'apprentissage adversarial génératif et de stratégies d'adaptation de domaine."], 'main_findings': ["Les méthodes de segmentation automatisée en IVUS peuvent être classées en quatre approches principales : méthodes traditionnelles, machine learning, deep learning (CNN), et mécanismes d'attention/transformers.", "Chaque catégorie d'approche apporte des améliorations progressives par rapport à la précédente : les méthodes traditionnelles sont limitées par la complexité des images, le ML apporte robustesse et adaptabilité, le DL (CNN) révolutionne la performance via l'apprentissage de caractéristiques hiérarchiques, et les transformers/mécanismes d'attention apportent des gains supplémentaires via la capture de dépendances à long terme et du contexte."]}

## Conclusions

IVUS imaging is crucial for accurate CVD diagnosis, but manual segmentation is time consuming and error prone Automated segmentation methods have been developed to improve efficiency and accuracy, with traditional techniques providing the foundation ML advancements, such as MRF, RF, and SVMs, offer robust solutions by incorporating spatial context and ensemble learning

## Comparative analysis of various IVUS architectures.

| Technique | Advantages | Disadvantages | Performance | Specific Application |
| --- | --- | --- | --- | --- |
|  |  | Conventional Techniques |  |  |
|  | Effective in removing |  |  |  |
| Thresholding | catheter artifacts, sequential border estimation, ad hoc mechanism for | May not perform well with complex and variable IVUS images | Jaccard measure: 0.84 ± 0.07 for Lumen, 0.82 ± 0.11 for MA border | Lumen-intima and media-adventitia (MA) borders segmentation |
|  | discontinuous borders |  |  |  |
| Active Contours | Fully automated, fast, and adaptive to the shape of the object | Sensitive to initialization, may get stuck in local minima | 96% reduction in analysis time compared to manual segmentation | Lumen and MA boundary segmentation |
|  | Machine Learning Techniques |  |
|  |  | Designing MRF and |  |  |
| Markov Random Field | Incorporates spatial context, robust segmentation | defining appropriate potential functions can be challenging, high | Not specified | Calcified plaque detection |
|  |  | computational cost |  |  |
| Random Forest | Captures non-linear relationships, handles high-dimensional data well, provides feature importance insights | May overfit with noisy data, less interpretable than simpler models | Not specified | Identifying specific morphological structures within vessel walls |
|  |  | Deep Learning Techniques |  |  |
|  | Preserves |  |  |  |
| Non-UNet-Scale Mutualized Perception | complementary information from adjacent scales, with similar local distinguishes objects | Complex architecture, training may require large amounts of data for | Not specified | Vessel boundary segmentation |
|  | features |  |  |  |
| Non-UNet-CSDN | Efficient segmentation, treats shallow and deep networks separately for efficiency high accuracy and | Complex architecture, training may require large amounts of data for | Not specified | Real-time segmentation |

## Cont.

| Technique | Advantages | Disadvantages | Performance | Specific Application |
| --- | --- | --- | --- | --- |
|  | Improves feature |  |  |  |
| UNet and its variants (MFA-UNet) | fusion and information retention, enables context retrieval from spatial-temporal | Complex architecture, may require large amounts of data for training | Optimized using Focal Tversky loss to address data imbalance | IVUS scan segmentation |
|  | perspectives |  |  |  |
|  | More effectively |  |  |  |
| UNet and its variants IVUS-UNet++ | captures fine-grained details of the foreground objects, network for multi-scale uses feature pyramid | Complex architecture, may require large training amounts of data for | Best JM and HD for both lumen and MA UNet++ and IVUS-Net border compared to | Lumen and MA border segmentation |
|  | feature utilization |  |  |  |
|  | Attention and Transformer-based Methods |  |
|  | Accurate segmentation |  |  |  |
|  | of vessel walls in IVUS | Complex architecture, | Integrated into |  |
| POST-IVUS | images, mimics cardiologists' | may require large amounts of data for | QCU-CMS1 software for automatic IVUS | IVUS image segmentation |
|  | perceptual organization | training | image segmentation |  |
|  | principle |  |  |  |
|  | Preserves intravascular |  |  |  |
| MSP-GAN | structures during domain adaptation, uses transformers for information global pathology | Complex architecture, may require large training amounts of data for | Ensures local structures correspondence translated images between source and | IVUS domain adaptation |
|  | preservation |  |  |  |

## Benchmarking table. ✓ indicates the presence or use of the specified feature, while ✗ denotes its absence.

| C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SN | Authors | NOF | Type of Data | Architecture Used | Attention | Transformer | #Patients/ #Images | CV | Results |
| R1 | Hammouche et al. [58] (2019) | 10 | Image | Helical active contour | ✗ | ✗ | 144/510 497/638 | K5 | Lumen detection accuracy of 99.42% and a minimal mean absolute error of 0.272 mm. |
| R2 | Giannoglou et al. [56] (2006) | 14 | Image | Active contour model | ✗ | ✗ | 97/970 | K5 | The study demonstrated a 96% reduction in analysis time compared to manual segmentation. |
|  |  |  |  |  |  |  |  |  | Enhanced traditional |
|  |  |  |  |  |  |  |  |  | snake algorithm, Otsu |
| R3 | Wang et al. [96] (2021) | 17 | Image | ML | ✗ | ✗ | 379, 300 | K10 | thresholding, morphological operations, and connected |
|  |  |  |  |  |  |  |  |  | component labeling were |
|  |  |  |  |  |  |  |  |  | incorporated |
| R4 | Vercio et al. [61] (2019) | 14 | Image | SVM with RF | ✓ | ✗ | 800 | - | High Dice similarity coefficient (DSC) of 0.91 for LI and 0.94 for MA. |
| R5 | Liu et al. [69] (2022) | 29 | Image | SMP | ✓ | ✓ | 378 | - | DSC of 0.96 for the lumen and 0.97 for the MA |
| R6 | Bargsten et al. [78] (2021) | 20 | Image | Capsule Network | ✓ | ✓ | - | - | Accuracy of 94.59% in lumen segmentation. |
| R7 | Proposed Study | 39 | Point | Transformers Attention and | ✓ | ✓ | 500 | K5 |  |

## learning, particularly CNNs like UNet and its variants, has revolutionized IVUS segmentation by learning hierarchical features from raw data. Advanced architectures like MFAUNet and IVUS-UNet++ further enhance accuracy and efficiency. Attention mechanisms and transformers have shown promise in capturing long-term dependencies and contextual information. Models like POST and MSP-GAN demonstrate significant improvements by incorporating temporal context and generative adversarial learning. The evolution of automated segmentation methods has significantly improved IVUS imaging in CVD diagnosis, and future research should continue to refine these methods for clinical applicability and effectiveness.

| 9 | MRI | Magnetic Resonance Imaging | 51 | PA | Pixel Accuracy |
| --- | --- | --- | --- | --- | --- |
| 10 | OCT | Optical Coherence Tomography | 52 | mIoU | Mean Intersection over Union |
| 11 | PRISMA | Preferred Reporting Items for Systematic Reviews and Meta-Analyses | 53 | FWIoU | Frequency Weighted Intersection over Union |
| 12 | SDL | Solo Deep Learning | 54 | TP | True Positive |
| 13 | HDL | Hybrid Deep Learning | 55 | TN | True Negative |
| 14 | CNN | Convolutional Neural Network | 56 | FP | False Positive |
| 15 | CRF | Conditional Random Field | 57 | FN | False Negative |
| 16 | FAM | Feature Aggregation Module | 58 | PPV | Positive Predictive Value |
| 17 | BConvLSTM | Bi-directional Convolutional Long Short-Term Memory | 59 | NPV | Negative Predictive Value |
| 18 | MFAUNet | Multi-scale Feature Aggregated UNet | 60 | FDR | False Discovery Rate |
| 19 | UNet++ | UNet Plus Plus | 61 | FOR | False Omission Rate |
| 20 | IoU | Intersection over Union | 62 | MSE | Mean Squared Error |
| 21 | JM | Jaccard Measure | 63 | RMSE | Root Mean Squared Error |
| 22 | HD | Hausdorff Distance | 64 | MAE | Mean Absolute Error |
| 23 | GAN | Generative Adversarial Network | 65 | RAE | Relative Absolute Error |
| 24 | MSP-GAN | Multilevel Structure-Preserved Generative Adversarial Network | 66 | RSE | Relative Squared Error |
| 25 | SMC | Super pixel-wise Multi-scale Contrastive Constraint | 67 | R2 | Coefficient of Determination |
| 26 | TF | Temporal Constraining and Fusion 68 | Adj. R2 | Adjusted R-squared |
| 27 | STR UNet | Selective Transformer Recurrent UNet | 69 | AIC | Akaike Information Criterion |
| 28 | MIC | Maximum Intensity Curve | 70 | BIC | Bayesian Information Criterion |
| 29 | RMM | Rayleigh Mixture Model | 71 | LOO-CV | Leave-One-Out Cross-Validation |
| 30 | MRF | Markov Random Field | 72 | K-fold CV | K-fold Cross-Validation |
| 31 | FCM | Fuzzy C-Means | 73 | Lasso | Least Absolute Shrinkage and Selection Operator |
| 32 | HMRF | Hidden Markov Random Field | 74 | Ridge | Ridge Regression |
| 33 | SVM | Support Vector Machine | 75 | Elastic Net | Elastic Net Regression |
| 34 | RF | Random Forest | 76 | PCA | Principal Component Analysis |
| 35 | FODPSO | Fractional-order Darwinian Particle Swarm Optimization | 77 | t-SNE | t-Distributed Stochastic Neighbor Embedding |
| 36 | PAD | Percentage of Area Difference | 78 | UMAP | Uniform Manifold Approximation and Projection |
| 37 | HSD | Hausdorff Surface Distance | 79 | NMF | Non-negative Matrix Factorization |
| 38 | Dice | Dice Coefficient | 80 | ICA | Independent Component Analysis |
| 39 | Precision | Precision Score | 81 | SVD | Singular Value Decomposition |
| 40 | Recall | Recall Score | 82 | LLE | Locally Linear Embedding |
| 41 | F1 | F1 Score | 83 | ISOMAP | Isometric Mapping |
| 42 | Kappa | Cohen's Kappa Score | 84 | MDS | Multidimensional Scaling |

### Formule


$$Attention(Q, K, V) = softmax QKT √ d k V$$
