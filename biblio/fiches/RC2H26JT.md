# Labeling confidence for uncertainty-aware histology image classification



## Resume


Labeling confidence for uncertainty-aware histology image classification

Trustworthy learning with (un)sure annotation for lung nodule diagnosis with CT

Labeling instructions matter in biomedical image analysis

U-MedSAM: Uncertainty-Aware MedSAM for Medical Image Segmentation

Dual Annotation Learning with Selective Uncertainty for Medical Image Segmentation with Noisy Labels

Label-Efficient Breast Cancer Histopathological Image Classification.

The automatic classification of breast cancer histopathological images has great significance in computer-aided diagnosis. Recently, deep learning via neural networks has enabled pattern detection and prediction using large, labeled datasets; whereas, collecting and annotating sufficient histological data using professional pathologists is time consuming, tedious, and extremely expensive. In the proposed paper, a deep active learning framework is designed and implemented for classification of breast cancer histopathological images, with the goal of maximizing the learning accuracy from very limited labeling. This method involves manual annotation of the most valuable unlabeled samples, which are then integrated into the training set. The model is then iteratively updated with an increasing training set. Here, two selection strategies are discussed for the proposed deep active learning framework: An entropy-based strategy and a confidence-boosting strategy. The proposed method has been

Uncertainty‐aware iterative learning for noisy‐labeled medical image segmentation

<jats:title>Abstract</jats:title>
                  Medical image segmentation from noisy labels is an important task since obtaining high‐quality annotations is extremely difficult and expensive. There are a lot of approaches proposed for such task. However, some issues like the overfitting on noisy annotations, the limited learning of boundary features, and no consideration of the corrupted local pixels are still not solved. Therefore, a novel approach named uncertainty‐aware iterative learning (UaIL) is proposed for medical image segmentation with noisy labels. UaIL iteratively and jointly trains two deep networks using the original images and their argumented ones through a joint loss function including softened label loss, hard label loss and consistency loss, which encourages UaIL to produce segmentations that are robust to the perturbations in arbitrary semantic space. The uncertainty of labels is estimated based on the predictions in iterative learning, then the original labels

Uncertainty Prediction for Deep Learning-based Image Denoising in Low-dose CT Imaging

A survey of image labelling for computer vision applications

A Trustworthy Framework for Medical Image Analysis with Deep Learning

Reliable Label-Efficient Learning for Biomedical Image Recognition.

The use of deep neural networks for biomedical image analysis requires a sufficient number of labeled datasets. To acquire accurate labels as the gold standard, multiple observers with specific expertise are required for both annotation and proofreading. This process can be time-consuming and labor-intensive, making high-quality, and large-annotated biomedical datasets difficult. To address this problem, we propose a deep active learning framework that enables the active selection of both informative queries and reliable experts. To measure the uncertainty of the unlabeled data, a dropout-based strategy is integrated with a similarity criterion for both data selection and random error elimination. To select the reliable labelers, we adopt an expertise estimator to learn the expertise levels of labelers via offline-testing and online consistency evaluation. The proposed method is applied to classification tasks on two types of medical images including confocal endomicroscopy images and

When uncertainty guides learning: a highly effective approach to kidney disease classification in CT imaging.

The high cost of expert annotations significantly hinders the advancement of deep learning models for clinical medical imaging. This work introduces an efficient entropy-based active learning framework that achieves outstanding classification performance for renal abnormalities (Normal, Cyst, Stone, Tumor) in CT scans while requiring only a minimal amount of labeled data. The dataset comprises 12,446 CT slices split 70/15/15 into training (8,716), validation (1,865), and test (1,865) partitions via stratified sampling. Starting with only 200 randomly selected images and employing predictive entropy for uncertainty sampling on a pretrained ResNet-50 backbone, the proposed method attains 99.71% ± 0.25% mean test accuracy (95% CI: [99.30, 99.94]) across five independent runs after just six query cycles on the standard 12,446-image CT kidney dataset. Our method uses only 2,000 labeled training images, representing 22.9% of the 8,716-image training partition (a 77.1% reduction in required annotations relative to full supervision of the training set). This performance matches or exceeds prior fully supervised methods trained on the complete labeled training partition while demonstrating substantially improved sample efficiency, particularly in early annotation cycles where entropy-guided selection converges significantly faster than random sampling. Statistical testing across five repeated runs confirms that results are stable (Shapiro-Wilk
                    p
                    = 0.148). The framework exhibits exceptional sample efficiency as described by an empirically fitted power-law curve with a fitted exponent of 1.2, and empirically observed uncertainty decay with a rate of 0.92. These results offer both practical insights into annotation efficiency and substantial application value in the medical imaging domain.

Investigate Uncertainty Estimation in Transfer Learning Based Active Learning for Medical Image Segmentation

DBrAL: A Novel Uncertainty-Based Active Learning Based on Deep-Broad Learning for Medical Image Classification


## Quote


we propose a selection strategy based on prediction uncertainty with a single image as the smallest selection unit... which further reduces the labeling cost

In summary, we present a framework for uncertainty representation in healthcare, evaluated with a biomedical image segmentation task.

In summary, we present a framework for uncertainty representation in healthcare, evaluated with a biomedical image segmentation task.


## Insight


implications: La gestion de l'incertitude, notamment via des labels basés sur le niveau de confiance, fait actuellement défaut dans les flux d'annotation des images échographiques utilisées pour l'anesthésie régionale, et les auteurs appellent à une standardisation du 'ground truth' associée à des stratégies multi-évaluateurs.


## Conclusion


A transfer learning-based active learning framework can significantly reduce the size of required labeled training data while maintaining high accuracy of the classification of tumors in brain MRI. The proposed method can save 40-70% of the labeling cost while maintaining stability and robustness of CNN performance for brain tumor classification. By using 30% of the training dataset conditioned on excluding top and bottom 10% of the uncertainty list, the uncertainty sampling method achieved AUC of 82.89% and 82.00% on the imbalanced and balanced datasets, respectively, which was comparable or better than the baseline AUC. The proposed uncertainty method outperforms random sampling.


## Raw_Human_Feedback_In_Inductive_Logic_Learning


The overview of our image labeling approach.

The overview of our image labeling approach.


## Raw_D._Uncertainty_Rectification_Module


However, we argue that this simple 'correction' may not improve the performance or even introduce additional segmentation errors, since regions with high uncertainty may not necessarily correspond to false positives or negatives, especially for complex organs with different shapes and volumes. In some cases, they may be ambiguous or complex regions where the target is unclear or difficult to define. To this end, we propose to rectify uncertain regions based on the assumptions that 1) pixels that have similar intensity and 2) are close to each other in the image are likely to belong to the same class. Instead of setting a fixed threshold for the selection of high uncertainty areas, we use a class-specific threshold for confidence-based filtering as follows: where S ŷ and S b represent the area of the ensembled segmentation mask and corresponding bounding box, respectively. Lower ratio indicates that the target occupies a smaller portion of the bounding box and there might be more uncert

However, we argue that this simple 'correction' may not improve the performance or even introduce additional segmentation errors, since regions with high uncertainty may not necessarily correspond to false positives or negatives, especially for complex organs with different shapes and volumes. In some cases, they may be ambiguous or complex regions where the target is unclear or difficult to define. To this end, we propose to rectify uncertain regions based on the assumptions that 1) pixels that have similar intensity and 2) are close to each other in the image are likely to belong to the same class. Instead of setting a fixed threshold for the selection of high uncertainty areas, we use a class-specific threshold for confidence-based filtering as follows: where S ŷ and S b represent the area of the ensembled segmentation mask and corresponding bounding box, respectively. Lower ratio indicates that the target occupies a smaller portion of the bounding box and there might be more uncert


## Discussion


Cette section examine la sensibilité du cadre proposé à plusieurs paramètres clés, incluant la taille du jeu de données pré-labellisées, le choix de la mesure d'incertitude et la stratégie d'assignation des labelers. Les auteurs montrent qu'un nombre insuffisant d'échantillons pré-labellisés dégrade l'initialisation de l'estimateur d'expertise et donc la performance globale, bien que l'effet se stabilise au-delà d'une certaine taille de jeu de données. La comparaison des mesures d'incertitude révèle que la stratégie de fusion combinant dropout et transformation aléatoire des données surpasse les métriques classiques telles que l'entropie croisée et la marge inter-classes, en termes de précision et de vitesse de convergence. Concernant l'assignation des tâches, le mécanisme proposé équilibre la charge entre labelers de fiabilité variable sans sacrifier la précision de classification, tout en maintenant un temps de traitement par itération inférieur à une seconde, compatible avec un usage clinique réel. En conclusion, le cadre d'apprentissage actif profond proposé permet de sélectionner conjointement les données informatives et les labelers fiables en modélisant à la fois les erreurs aléatoires et les erreurs d'expertise, offrant une solution pratique pour l'annotation de données d'imagerie médicale avec des experts de niveaux de compétence hétérogènes.


## Raw_Uncertainty_Estimation


In deep learning, uncertainty estimation is an essential task that can lead to significant improvements in the reliability and trustworthiness of deep models, which is particularly important in medical imaging where the uncertainty can be used to identify areas of concern or to provide additional information to the clinician [41], [42]. The quantification of uncertainty involves two fundamental types: aleatoric uncertainty which represents inherent noise or variation in the data learned by the model, and epistemic uncertainty which quantifies the inherent lack of knowledge about the underlying model architecture and parameters [43]. For image segmentation, this uncertainty acknowledges that there may be uncertainty in determining whether a pixel belongs to the object or the background. The model assigns a probability value that represents the confidence or uncertainty associated with each pixel's classification, enabling a more nuanced and informative representation of the segmentation

In deep learning, uncertainty estimation is an essential task that can lead to significant improvements in the reliability and trustworthiness of deep models, which is particularly important in medical imaging where the uncertainty can be used to identify areas of concern or to provide additional information to the clinician [41], [42]. The quantification of uncertainty involves two fundamental types: aleatoric uncertainty which represents inherent noise or variation in the data learned by the model, and epistemic uncertainty which quantifies the inherent lack of knowledge about the underlying model architecture and parameters [43]. For image segmentation, this uncertainty acknowledges that there may be uncertainty in determining whether a pixel belongs to the object or the background. The model assigns a probability value that represents the confidence or uncertainty associated with each pixel's classification, enabling a more nuanced and informative representation of the segmentation


## Raw_Introduction


(2) Evaluate and compare the efficacy of different uncertainty metrics for medical image segmentation.

(2) Evaluate and compare the efficacy of different uncertainty metrics for medical image segmentation.


## Synthese


L’objectif principal est d’investiguer les représentations d’incertitude en segmentation d’images médicales via MCU-Net (U-Net associé au Monte Carlo Dropout) et d’évaluer leur utilité pour un système human-in-the-loop de référencement automatique des cas incertains. Ce travail s’inscrit dans le besoin, en santé numérique, de ne pas se limiter à une prédiction ponctuelle mais d’identifier les zones où le modèle est épistémiquement incertain, afin d’éviter une confiance excessive dans des sorties ambiguës. Les objectifs opérationnels incluent la comparaison de quatre métriques d’incertitude, la détermination d’un seuil τ, et l’évaluation sur la segmentation des vaisseaux rétiniens (DRIVE). L’hypothèse implicite est qu’une représentation d’incertitude épistémique, couplée à un seuil, permet de localiser les cas difficiles et de les orienter vers un professionnel de santé, avec une logique d’évaluation patient par patient.

L’objectif principal est d’investiguer les représentations d’incertitude en segmentation d’images médicales via MCU-Net (U-Net associé au Monte Carlo Dropout) et d’évaluer leur utilité pour un système human-in-the-loop de référencement automatique des cas incertains. Ce travail s’inscrit dans le besoin, en santé numérique, de ne pas se limiter à une prédiction ponctuelle mais d’identifier les zones où le modèle est épistémiquement incertain, afin d’éviter une confiance excessive dans des sorties ambiguës. Les objectifs opérationnels incluent la comparaison de quatre métriques d’incertitude, la détermination d’un seuil τ, et l’évaluation sur la segmentation des vaisseaux rétiniens (DRIVE). L’hypothèse implicite est qu’une représentation d’incertitude épistémique, couplée à un seuil, permet de localiser les cas difficiles et de les orienter vers un professionnel de santé, avec une logique d’évaluation patient par patient.