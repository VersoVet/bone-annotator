# Adapl: Adaptive Pseudo Labeling for Deep Active Learning in Image Classification



## Resume


Adapl: Adaptive Pseudo Labeling for Deep Active Learning in Image Classification

BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation

Active learning based image annotation

Active learning for hierarchical multi-label classification

Deep Active Re-Labeling: Toward Noise-Resilient Annotation Efficiency

Semantic-Gap-Oriented Active Learning for Multilabel Image Annotation

Iterative Pseudo-Labeling with Deep Feature Annotation and Confidence-Based Sampling

DILIE: Deep Internal Learning for Image Enhancement

Suggestive Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Attention, Suggestion and Annotation: A Deep Active Learning Framework for Biomedical Image Segmentation

Deep learning based active learning technique for data annotation and improve the overall performance of classification models

LabelMe: Online Image Annotation and Applications

Adaptive image denoising using a deep neural network with a noise correction map

Smart Data Annotation: Accelerating Data Labeling Processes through Deep Learning

Effective image annotation via active learning

Diverse Image Annotation

Deep Learning and Data Labeling for Medical Applications

UniSAL: Unified Semi-supervised Active Learning for histopathological image classification.

Histopathological image classification using deep learning is crucial for accurate and efficient cancer diagnosis. However, annotating a large amount of histopathological images for training is costly and time-consuming, leading to a scarcity of available labeled data for training deep neural networks. To reduce human efforts and improve efficiency for annotation, we propose a Unified Semi-supervised Active Learning framework (UniSAL) that effectively selects informative and representative samples for annotation. First, unlike most existing active learning methods that only train from labeled samples in each round, dual-view high-confidence pseudo training is proposed to utilize both labeled and unlabeled images to train a model for selecting query samples, where two networks operating on different augmented versions of an input image provide diverse pseudo labels for each other, and pseudo label-guided class-wise contrastive learning is introduced to obtain better feature representati

DBrAL: A Novel Uncertainty-Based Active Learning Based on Deep-Broad Learning for Medical Image Classification

M-VAAL: Multimodal Variational Adversarial Active Learning for Downstream Medical Image Analysis Tasks.

Recent Advancements and Future Prospects in Active Deep Learning for Medical Image Segmentation and Classification

A survey on Image Data Augmentation for Deep Learning

DIAL: Deep Interactive and Active Learning for Semantic Segmentation in Remote Sensing

Supervised Learning of Semantic Classes for Image Annotation and Retrieval

AdaResU-Net: Multiobjective adaptive convolutional neural network for medical image segmentation


## Discussion


Dans leur revue, les auteurs soulignent que le Deep Active Learning (DeepAL) conjugue l’extraction automatique de caractéristiques propres au deep learning et la réduction des coûts d’annotation de l’active learning, ce qui en fait une approche particulièrement prometteuse lorsque les labels exigent une expertise élevée. Ils documentent toutefois d’importantes incohérences entre études — performances du random sampling baseline et résultats de méthodes DeepAL divergents sous des protocoles apparemment comparables — et appellent à une plateforme d’évaluation unifiée, à une meilleure reproductibilité et à des expériences répétées avec initialisations variées. Les directions de recherche identifiées portent principalement sur l’amélioration des stratégies de sélection (incertitude, diversité, hybrides), l’optimisation des méthodes d’entraînement (données labellisées, non labellisées, GAN, apprentissage hybride) et l’indépendance aux tâches, tandis que l’entraînement incrémental, encore peu exploré, apparaît prometteur pour limiter le coût computationnel. En conclusion, les auteurs présentent ce travail comme la première revue systématique du domaine, structurée autour de l’optimisation des stratégies de requête, de l’expansion des données labellisées, de la généricité des modèles, des stratégies d’arrêt, des applications et des perspectives futures.


## Quote


Active learning, however, acquires the labels for some unlabeled images from domain experts, which can ensure accurate annotation.

Here we introduce ActiveLab, a straightforward active learning algorithm that estimates when such re-labeling will be more effective than labeling an entirely new example.

this paper proposes ILM-ASSL for domain-adaptive semantic segmentation. It learns massive unlabeled data semi-supervised to improve the accuracy in the target domain and provides an accurate selection model for active learning. Then, combined with the predictive uncertainty sample selection strategy of active learning, manual intervention is used to correct the pseudo-labels.


## Insight


methodology: Le DeepAL combine la capacité du deep learning à traiter des données d’images de haute dimension et à extraire automatiquement des caractéristiques avec le potentiel de l’active learning à réduire efficacement les coûts d’annotation, ce qui le rend particulièrement pertinent lorsque les labels nécessitent une expertise élevée et sont difficiles à obtenir.