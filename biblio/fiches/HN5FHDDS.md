# A Self Supervised StyleGAN for Image Annotation and Classification with Extremely Limited Labels

**Auteurs** : Dana Cohen Hochberg, Hayit Greenspan, Raja Giryes
**Année** : 2023
**DOI** : 10.1109/tmi.2022.3187170

## Résumé

The recent success of learning-based algorithms can be greatly attributed to the immense amount of annotated data used for training. Yet, many datasets lack annotations due to the high costs associated with labeling, resulting in degraded performances of deep learning methods. Self-supervised learning is frequently adopted to mitigate the reliance on massive labeled datasets since it exploits unlabeled data to learn relevant feature representations. In this work, we propose SS-StyleGAN, a self-supervised approach for image annotation and classification suitable for extremely small annotated datasets. This novel framework adds self-supervision to the StyleGAN architecture by integrating an encoder that learns the embedding to the StyleGAN latent space, which is well-known for its disentangled properties. The learned latent space enables the smart selection of representatives from the data to be labeled for improved classification performance. We show that the proposed method attains str

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## COMPARISON (LOWER IS BETTER) OF DIFFERENT CONFIGURATIONS OF SS-STYLEGAN AND STYLEGAN FOR THE LITS DATASET. THE

| CONFIGURATIONS INCLUDE A DIFFERENT NUMBER OF SHARED LAYERS |
| --- | --- | --- |
| BETWEEN THE ENCODER AND DISCRIMINATOR. |
| Model | Shared Layers FID |
| SS-StyleGAN | 15 | 28.0 |
| SS-StyleGAN | 14 | 23.8 |
| SS-StyleGAN | 13 | 17.3 |
| SS-StyleGAN | 12 | 11.6 |
| SS-StyleGAN | 11 | 16.4 |
| StyleGAN2 | - | 16.3 |

## IMPACT OF EMBEDDING INTO THE Z AND W LATENT SPACE ON THE CLASSIFICATION PERFORMANCE (HIGHER IS BETTER). THE RESULTS ARE DISPLAYED FOR TRAINING WITH 50 LABELED IMAGES.

| Dataset | Model | Accuracy Sensitivity Specificity Precision | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| LiTs | SS-StyleGAN(Z loss, Z space) | 0.58 ± 0.02 | 0.57 ± 0.03 | 0.59 ± 0.02 | 0.40 ± 0.03 | 0.58 ± 0.02 |
| LiTs | SS-StyleGAN(W loss, Z space) | 0.56 ± 0.03 | 0.55 ± 0.03 | 0.60 ± 0.07 | 0.38 ± 0.04 | 0.57 ± 0.04 |
| LiTs | SS-StyleGAN | 0.89 ± 0.02 | 0.89 ± 0.03 | 0.89 ± 0.06 | 0.79 ± 0.04 | 0.89 ± 0.02 |
| COVID-19 | SS-StyleGAN(W loss, Z space) | 0.72 ± 0.06 | 0.76 ± 0.09 | 0.69 ± 0.05 | 0.75 ± 0.09 | 0.72 ± 0.06 |
| COVID-19 | SS-StyleGAN | 0.92 ± 0.03 | 0.97 ± 0.03 | 0.89 ± 0.05 | 0.97 ± 0.02 | 0.93 ± 0.02 |

## STUDY FOR DIFFERENT TYPES OF DIMENSION REDUCTION AND CLASSIFICATION METHODS FOR THE COVID-19 AND LITS DATASETS WHEN TRAINING WITH 10, 20 AND 50 LABELED IMAGES. RESULTS DISPLAYED ARE AVERAGE AUC RESULTS OVER 5 EXPERIMENTS (HIGHER IS BETTER). OUR CHOSEN CONFIGURATION IS DISPLAYED IN BOLD.

| Images Dimension Reduction Method Classification Method AUC (COVID-19) AUC (LiTs) |
| --- | --- | --- | --- | --- |
| 10 | - | NN | 0.57 ± 0.04 | 0.59 ± 0.03 |
| 10 | PCA | NN | 0.61 ± 0.10 | 0.63 ± 0.12 |
| 10 | PCA | MLP | 0.57 ± 0.08 | 0.70 ± 0.02 |
| 10 | PCA | Linear | 0.63 ± 0.13 | 0.70 ± 0.07 |
| 10 | t-SNE | Linear | 0.77 ± 0.02 | 0.65 ± 0.03 |
| 10 | t-SNE | NN | 0.82 ± 0.03 | 0.72 ± 0.02 |
| 20 | - | NN | 0.59 ± 0.07 | 0.61 ± 0.03 |
| 20 | PCA | NN | 0.74 ± 0.05 | 0.66 ± 0.03 |
| 20 | PCA | MLP | 0.76 ± 0.06 | 0.75 ± 0.04 |
| 20 | PCA | Linear | 0.79 ± 0.06 | 0.74 ± 0.06 |
| 20 | t-SNE | Linear | 0.79 ± 0.01 | 0.65 ± 0.05 |
| 20 | t-SNE | NN | 0.87 ± 0.04 | 0.78 ± 0.06 |
| 50 | - | NN | 0.63 ± 0.04 | 0.66 ± 0.04 |
| 50 | PCA | NN | 0.82 ± 0.04 | 0.68 ± 0.04 |
| 50 | PCA | MLP | 0.89 ± 0.03 | 0.84 ± 0.04 |
| 50 | PCA | Linear | 0.89 ± 0.04 | 0.82 ± 0.02 |
| 50 | t-SNE | Linear | 0.78 ± 0.03 | 0.69 ± 0.01 |
| 50 | t-SNE | NN | 0.93 ± 0.02 | 0.89 ± 0.02 |

## CLASSIFICATION RESULTS ON THE TEST SET FOR THE COVID-19 DATASET WHEN TRAINING WITH 10, 20 AND 50 IMAGES FROM ALL EXPERIMENTS (HIGHER IS BETTER).

| Images | Model | Accuracy Sensitivity Specificity Precision | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | EfficientNet | 0.56 ± 0.04 | 0.51 ± 0.41 | 0.54 ± 0.42 | 0.45 ± 0.25 | 0.50 ± 0.10 |
| 10 | MoCo v2 | 0.61 ± 0.04 | 0.44 ± 0.14 | 0.76 ± 0.15 | 0.62 ± 0.03 | 0.60 ± 0.03 |
| 10 | MoCo v2 (TL) | 0.65 ± 0.04 | 0.71 ± 0.21 | 0.61 ± 0.21 | 0.74 ± 0.06 | 0.66 ± 0.03 |
| 10 | MoCo v2 (FPS) | 0.79 ± 0.04 | 0.75 ± 0.10 | 0.73 ± 0.09 | 0.78 ± 0.08 | 0.79 ± 0.04 |
| 10 | Learning Loss | 0.45 ± 0.22 | 0.75 ± 0.42 | 0.26 ± 0.42 | 0.60 ± 0.37 | 0.50 ± 0.03 |
| 10 | VAAL | 0.37 ± 0.12 | 0.74 ± 0.43 | 0.22 ± 0.44 | 0.23 ± 0.33 | 0.47 ± 0.06 |
| 10 | SS-StyleGAN (RS) | 0.79 ± 0.06 | 0.71 ± 0.17 | 0.85 ± 0.11 | 0.81 ± 0.10 | 0.78 ± 0.05 |
| 10 | SS-StyleGAN (FPS) | 0.82 ± 0.03 | 0.86 ± 0.06 | 0.79 ± 0.10 | 0.86 ± 0.04 | 0.82 ± 0.03 |
| 20 | EfficientNet | 0.56 ± 0.07 | 0.60 ± 0.32 | 0.47 ± 0.25 | 0.62 ± 0.22 | 0.53 ± 0.16 |
| 20 | MoCo v2 | 0.60 ± 0.11 | 0.40 ± 0.15 | 0.84 ± 0.10 | 0.57 ± 0.21 | 0.61 ± 0.07 |
| 20 | MoCo v2 (TL) | 0.67 ± 0.17 | 0.85 ± 0.31 | 0.42 ± 0.43 | 0.48 ± 0.50 | 0.63 ± 0.21 |
| 20 | MoCo v2 (FPS) | 0.83 ± 0.02 | 0.77 ± 0.04 | 0.90 ± 0.02 | 0.79 ± 0.06 | 0.83 ± 0.02 |
| 20 | Learning Loss | 0.59 ± 0.17 | 0.20 ± 0.44 | 0.83 ± 0.38 | 0.72 ± 0.18 | 0.52 ± 0.04 |
| 20 | VAAL | 0.30 ± 0.03 | 0.99 ± 0.01 | 0.02 ± 0.04 | 0.02 ± 0.03 | 0.51 ± 0.02 |
| 20 | SS-StyleGAN (RS) | 0.79 ± 0.07 | 0.77 ± 0.15 | 0.80 ± 0.10 | 0.83 ± 0.08 | 0.79 ± 0.07 |
| 20 | SS-StyleGAN (FPS) | 0.87 ± 0.04 | 0.94 ± 0.04 | 0.81 ± 0.07 | 0.93 ± 0.04 | 0.87 ± 0.04 |
| 50 | EfficientNet | 0.59 ± 0.11 | 0.44 ± 0.37 | 0.70 ± 0.30 | 0.64 ± 0.18 | 0.59 ± 0.20 |
| 50 | MoCo v2 | 0.84 ± 0.07 | 0.88 ± 0.12 | 0.79 ± 0.09 | 0.92 ± 0.04 | 0.83 ± 0.08 |
| 50 | MoCo v2 (TL) | 0.78 ± 0.21 | 0.91 ± 0.01 | 0.73 ± 0.23 | 0.90 ± 0.04 | 0.81 ± 0.13 |
| 50 | MoCo v2 (FPS) | 0.87 ± 0.03 | 0.85 ± 0.06 | 0.89 ± 0.03 | 0.89 ± 0.04 | 0.87 ± 0.03 |
| 50 | Learning Loss | 0.68 ± 0.04 | 0.25 ± 0.29 | 0.89 ± 0.12 | 0.72 ± 0.13 | 0.57 ± 0.10 |
| 50 | VAAL | 0.52 ± 0.22 | 0.61 ± 0.53 | 0.49 ± 0.50 | 0.49 ± 0.46 | 0.55 ± 0.10 |
| 50 | SS-StyleGAN (RS) | 0.90 ± 0.03 | 0.87 ± 0.08 | 0.93 ± 0.06 | 0.90 ± 0.07 | 0.90 ± 0.04 |
| 50 | SS-StyleGAN (FPS) | 0.92 ± 0.03 | 0.97 ± 0.03 | 0.89 ± 0.05 | 0.97 ± 0.02 | 0.93 ± 0.02 |

## CLASSIFICATION RESULTS ON THE TEST SET FOR THE LITS DATASET WHEN TRAINING WITH 10, 20 AND 50 IMAGES FROM ALL EXPERIMENTS (HIGHER IS BETTER).

| Images | Model | Accuracy Sensitivity Specificity Precision | AUC |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | EfficientNet | 0.66 ± 0.03 | 0.76 ± 0.15 | 0.41 ± 0.28 | 0.56 ± 0.24 | 0.62 ± 0.07 |
| 10 | MoCo v2 | 0.59 ± 0.17 | 0.75 ± 0.38 | 0.43 ± 0.42 | 0.25 ± 0.28 | 0.49 ± 0.03 |
| 10 | MoCo v2 (FPS) | 0.64 ± 0.08 | 0.74 ± 0.20 | 0.43 ± 0.20 | 0.48 ± 0.10 | 0.58 ± 0.10 |
| 10 | Learning Loss | 0.42 ± 0.25 | 0.33 ± 0.57 | 0.67 ± 0.57 | 0.19 ± 0.16 | 0.50 ± 0.01 |
| 10 | VAAL | 0.69 ± 0.18 | 0.72 ± 0.35 | 0.62 ± 0.46 | 0.42 ± 0.33 | 0.67 ± 0.16 |
| 10 | SS-StyleGAN (RS) | 0.72 ± 0.06 | 0.77 ± 0.11 | 0.61 ± 0.17 | 0.57 ± 0.07 | 0.69 ± 0.07 |
| 10 | SS-StyleGAN (FPS) | 0.72 ± 0.03 | 0.71 ± 0.12 | 0.72 ± 0.05 | 0.56 ± 0.05 | 0.72 ± 0.02 |
| 20 | EfficientNet | 0.67 ± 0.14 | 0.69 ± 0.21 | 0.67 ± 0.15 | 0.54 ± 0.19 | 0.70 ± 0.15 |
| 20 | MoCo v2 | 0.80 ± 0.06 | 0.96 ± 0.03 | 0.50 ± 0.24 | 0.91 ± 0.07 | 0.73 ± 0.10 |
| 20 | MoCo v2 (FPS) | 0.65 ± 0.08 | 0.79 ± 0.18 | 0.38 ± 0.15 | 0.50 ± 0.12 | 0.58 ± 0.02 |
| 20 | Learning Loss | 0.51 ± 0.22 | 0.45 ± 0.50 | 0.62 ± 0.54 | 0.45 ± 0.50 | 0.54 ± 0.07 |
| 20 | VAAL | 0.77 ± 0.07 | 0.88 ± 0.09 | 0.48 ± 0.34 | 0.47 ± 0.34 | 0.68 ± 0.15 |
| 20 | SS-StyleGAN (RS) | 0.74 ± 0.07 | 0.77 ± 0.07 | 0.67 ± 0.17 | 0.59 ± 0.06 | 0.72 ± 0.02 |
| 20 | SS-StyleGAN (FPS) | 0.80 ± 0.01 | 0.79 ± 0.04 | 0.76 ± 0.17 | 0.62 ± 0.02 | 0.78 ± 0.06 |
| 50 | EfficientNet | 0.75 ± 0.05 | 0.79 ± 0.11 | 0.66 ± 0.13 | 0.61 ± 0.10 | 0.82 ± 0.04 |
| 50 | MoCo v2 | 0.82 ± 0.06 | 0.97 ± 0.07 | 0.55 ± 0.32 | 0.94 ± 0.12 | 0.76 ± 0.16 |
| 50 | MoCo v2 (FPS) | 0.67 ± 0.01 | 0.78 ± 0.04 | 0.43 ± 0.05 | 0.48 ± 0.03 | 0.61 ± 0.01 |
| 50 | Learning Loss | 0.78 ± 0.05 | 0.97 ± 0.01 | 0.31 ± 0.18 | 0.76 ± 0.10 | 0.64 ± 0.08 |
| 50 | VAAL | 0.84 ± 0.03 | 0.87 ± 0.13 | 0.80 ± 0.13 | 0.73 ± 0.08 | 0.83 ± 0.04 |
| 50 | SS-StyleGAN (RS) | 0.83 ± 0.03 | 0.88 ± 0.06 | 0.72 ± 0.11 | 0.76 ± 0.08 | 0.80 ± 0.04 |
| 50 | SS-StyleGAN (FPS) | 0.89 ± 0.02 | 0.89 ± 0.03 | 0.89 ± 0.06 | 0.79 ± 0.04 | 0.89 ± 0.02 |

## CLASSIFICATION RESULTS ON AN UNSEEN COVID-19 TEST DATASET WITH OUR METHOD WHEN TRAINING WITH 10, 20 AND 50 IMAGES FROM ALL EXPERIMENTS (HIGHER IS BETTER).

| Images Accuracy Sensitivity Specificity Precision | AUC |
| --- | --- | --- | --- | --- | --- |
| 10 | 0.87 ± 0.07 | 0.78 ± 0.20 | 0.91 ± 0.07 | 0.92 ± 0.06 | 0.84 ± 0.09 |
| 20 | 0.98 ± 0.02 | 0.95 ± 0.04 | 0.99 ± 0.01 | 0.98 ± 0.02 | 0.97 ± 0.03 |
| 50 |  |  |  |  |  |

### Formule


$$L Enc = -λE x,w∼P (x,w) [log(P (w|x)] + βL M SE (x real , G(Enc(x real ))),(1)$$

### Formule


$$) M |Σ(x)|) -0.5(w -Enc(x)) T Σ -1 (x)(w -Enc(x)).(2)$$
