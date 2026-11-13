# DeepDRR -- A Catalyst for Machine Learning in Fluoroscopy-guided Procedures



## Raw_Discussion


The framework combines novel learning-based algorithms for 3D material decomposition from CT and 2D scatter estimation with fast, analytic models for energy and material dependent forward projection and noise injection. On a surrogate task, i. e. the prediction of anatomical landmarks in X-ray images of the pelvis, we demonstrate that models trained on DeepDRRs generalize to clinical data without the need of re-training or domain adaptation, while the same model trained on conventional DRRs is unable to perform. Our future work will focus on improving volumetric segmentation by introducing more materials, in particular metal, and scatter estimation that could benefit from a larger training set size. In conclusion, we understand realistic in silico generation of X-ray images, e. g. using the proposed framework, as a catalyst designed to benefit the implementation of machine learning in fluoroscopy-guided procedures. Our framework seamlessly integrates with the software environment curre

We proposed DeepDRR, a framework for fast and realistic generation of synthetic X-ray images from diagnostic 3D CT, in an effort to ease the establishment of machine learning-based approaches in fluoroscopy-guided procedures.


## Quote


We proposed DeepDRR, a framework for fast and realistic generation of synthetic X-ray images from diagnostic 3D CT, in an effort to ease the establishment of machine learning-based approaches in fluoroscopy-guided procedures.

This led us to conduct a prospective study with the goals of: programming deep learning software to help make the diagnosis of PFF on radiographs; to evaluate its performance. We hypothesized that deep learning software can be programmed to help make the diagnosis of PFF using a limited number of radiographs.

Deep Learning-based Model for Automatic Bone Stromal Cell Segmentation of Fluorescence Microscopy Images

Bo-Net: Deep Learning-based Model for Automatic Bone Stromal Cell Segmentation of Fluorescence Microscopy Images

Bo-Net: Deep Learning-based Model for Automatic Bone Stromal Cell Segmentation of Fluorescence Microscopy Images

In conclusion, we understand realistic in silico generation of X-ray images, e. g. using the proposed framework, as a catalyst designed to benefit the implementation of machine learning in fluoroscopy-guided procedures.


## Conclusion


DeepDRR permet, selon les auteurs, une génération rapide et réaliste de radiographies synthétiques à partir de CT diagnostiques 3D. L'association d'une décomposition des matériaux et d'une estimation de la diffusion fondées sur l'apprentissage avec une projection analytique et une injection réaliste du bruit produit des données adaptées à l'entraînement de modèles. Sur la tâche de substitution étudiée, les modèles entraînés sur DeepDRRs se généralisent aux données cliniques sans réentraînement ni adaptation de domaine, contrairement au même modèle entraîné sur des DRRs conventionnels. Les auteurs considèrent la simulation réaliste in silico des radiographies comme un catalyseur potentiel du développement de l'apprentissage automatique pour les procédures guidées par fluoroscopie. La force de la conclusion sur la détection des repères est limitée dans le texte fourni par l'absence de métriques quantitatives de précision, d'intervalles de confiance, de valeurs p et de tailles d'effet.

The proposed deep learning-based framework shows promising capability for denoising interventional X-ray fluoroscopy images. The results from the catheter detection show that the network does not affect the results of such an algorithm when used as a pre-processing step. The extensive qualitative and quantitative evaluations suggest that the network may be of benefit to reduce radiation dose when applied in real time in the catheter laboratory.


## Synthese


DeepDRR a été développé pour répondre au manque de radiographies cliniques nombreuses, diversifiées et annotées nécessaires à l’apprentissage de modèles destinés aux procédures guidées par fluoroscopie. L’objectif principal était de construire un simulateur rapide et réaliste produisant, à partir de CT diagnostiques 3D, des images radiographiques intégrant la composition matérielle, le spectre énergétique, la diffusion et les principales sources de bruit du détecteur. Les auteurs ont testé l’hypothèse selon laquelle ce réalisme supplémentaire réduirait suffisamment l’écart entre données synthétiques et données réelles pour qu’un modèle entraîné exclusivement sur des DeepDRRs se généralise directement à des radiographies inédites, sans réentraînement ni adaptation de domaine. Des objectifs complémentaires portaient sur l’exactitude de la segmentation volumétrique et de l’estimation de la diffusion, ainsi que sur la rapidité de génération des projections [Unknown](zotero://select/library/items/SJCW62ZQ).

DeepDRR répond au besoin de disposer de données d’entraînement réalistes et abondantes pour développer des modèles d’apprentissage automatique destinés aux procédures guidées par fluoroscopie, alors que l’annotation et la collecte de radiographies cliniques sont difficiles. L’objectif était de déterminer si un cadre associant décomposition des matériaux, estimation de la diffusion, projection analytique polychromatique et injection de bruit pouvait produire rapidement, à partir de CT diagnostiques 3D, des radiographies synthétiques permettant une généralisation directe aux images cliniques. L’étude méthodologique a utilisé des volumes CT pelviens, des simulations Monte Carlo pour l’apprentissage de l’estimation de la diffusion et des radiographies inédites acquises lors d’études sur cadavres, mais les nombres de CT, de cadavres et de radiographies réelles ne sont pas précisés. La décomposition volumétrique fondée sur l’apprentissage distinguait trois matériaux — air, tissus mous et os — tandis qu’un réseau convolutif à dix couches estimait la composante diffusée dans le domaine de projection. La formation de l’image reposait également sur une projection analytique dépendante de l’énergie et des matériaux selon la loi de Beer-Lambert, puis sur la simulation du bruit quantique, du couplage entre pixels et du bruit électronique de lecture. Le taux de mauvaise classification de la segmentation volumétrique était de 2,03 ± 3,63 %, sans intervalle de confiance à 95 %, valeur p ou taille d’effet rapportés. Le réseau d’estimation de la diffusion, entraîné sur 330 images et évalué sur 30 images, obtenait une erreur quadratique moyenne égale à 6,4 % de l’énergie totale de l’image de diffusion, là encore sans mesure d’incertitude ni test statistique. Une projection de 615 × 479 pixels pouvait être simulée en 2,0 s, indépendamment du nombre de photons, avec un protocole applicatif comprenant un spectre d’anode en tungstène à 120 kV, une filtration de 4,3 mm d’aluminium et une dose annoncée de 5 × 10^5 photons par pixel. Sur la tâche de substitution consistant à prédire séquentiellement 23 repères anatomiques pelviens, le modèle entraîné exclusivement sur des DeepDRRs s’est généralisé qualitativement aux radiographies cliniques inédites et aux images ne montrant qu’une anatomie partielle, sans réentraînement ni adaptation de domaine, contrairement au même cadre entraîné sur des DRRs conventionnels mono-matériau et mono-énergétiques. Ces résultats soutiennent l’intérêt scientifique de DeepDRR comme générateur de données in silico intégrable aux environnements d’apprentissage profond, mais ils ne démontrent pas quantitativement une efficacité clinique, car aucune erreur de localisation, aucun taux de détection, aucun intervalle de confiance à 95 % et aucune valeur p ne sont fournis pour la tâche applicative. Les principales limites sont ainsi le caractère qualitatif de la comparaison finale, l’absence d’effectifs complets et d’analyses statistiques, la validation sur une tâche de substitution et des études cadavériques, la représentation limitée à trois matériaux et la taille modeste du jeu d’apprentissage de l’estimateur de diffusion [Unknown](zotero://select/library/items/SJCW62ZQ).

Cette revue narrative examine les approches de deep learning appliquées à l'analyse de la Video Fluoroscopic Swallowing Study (VFSS), un outil diagnostique de référence pour l'évaluation de la dysphagie et de ses complications, notamment l'aspiration et la pneumonie d'aspiration. Les auteurs structurent les méthodes existantes autour de trois tâches principales — classification, détection et segmentation — en s'appuyant sur des architectures telles que les CNN (VGG, I3D, ResNet), les modèles de détection (SSD, HRNet) et les réseaux de segmentation (U-Net et ses variantes). Sur le plan méthodologique, la modélisation temporelle des séquences vidéo repose historiquement sur les réseaux de neurones récurrents (RNN), tandis que les modèles à base de transformateurs, grâce au mécanisme d'auto-attention, permettent de capturer des dépendances à longue portée sur l'ensemble de la séquence de manière plus efficace. Les auteurs soulignent également que la rareté des jeux de données VFSS accessibles publiquement, liée à des contraintes éthiques et de confidentialité, constitue une limite structurelle majeure pour le développement et la validation de ces modèles.


## Methodologie


La méthodologie repose sur une approche de deep learning appliquée à des images de microscopie à fluorescence. Le design précis de l'étude (architecture du modèle, jeux de données d'entraînement, protocole de validation) n'est pas spécifié dans les éléments extraits disponibles.

Cette revue narrative examine les approches de deep learning appliquées à l'analyse de la Video Fluoroscopic Swallowing Study (VFSS), un outil diagnostique de référence pour l'évaluation de la dysphagie et de ses complications, notamment l'aspiration et la pneumonie d'aspiration. Les auteurs structurent les méthodes existantes autour de trois tâches principales — classification, détection et segmentation — en s'appuyant sur des architectures telles que les CNN (VGG, I3D, ResNet), les modèles de détection (SSD, HRNet) et les réseaux de segmentation (U-Net et ses variantes). Sur le plan méthodologique, la modélisation temporelle des séquences vidéo repose historiquement sur les réseaux de neurones récurrents (RNN), tandis que les modèles à base de transformateurs, grâce au mécanisme d'auto-attention, permettent de capturer des dépendances à longue portée sur l'ensemble de la séquence de manière plus efficace. Les auteurs soulignent également que la rareté des jeux de données VFSS accessibles publiquement, liée à des contraintes éthiques et de confidentialité, constitue une limite structurelle majeure pour le développement et la validation de ces modèles.


## Table


Tableau: Quantum and electronic readout noise injection. The individual steps of Deep-DRR are visualized schematically in Fig.1and explained in greater detail in the remainder of this section. The fully automated pipeline will be made open source upon publication of this manuscript. HU) and bone in presence of low mineral density. This is problematic since, despite similar HU, the attenuation characteristic of bone is substantially different of soft tissue
| 4) Material Decomposition: Material decomposition in 3D CT for MC simulation |
| --- |
| is traditionally accomplished by thresholding, since a given material has a char- |
| acteristic HU range [12]. This works well for large HU discrepancies, e. g. air |
| ([-1000] HU) and bone ([200, 3000] HU), but may fail otherwise, particularly |
| between soft tissue ([-150, 300] |
| : We propose DeepDRR, a Python, PyCUDA, and PyTorch-based |
| framework for fast and automatic simulation of X-ray images from CT data. |
| It consists of 4 major modules: 1) Material decomposition in CT volumes using |
| a deep segmentation ConvNet; 2) A material-and spectrum-aware ray-tracing |
| forward projector; 3) A neural network-based Rayleigh scatter estimation; and |


## Raw_Task-Based_Evaluation


Fundamentally, the goal of DeepDRR is to enable the learning of models on synthetically generated data that generalizes to unseen clinical fluoroscopy with-out re-training or other domain adaptation strategies. To this end, we consider anatomical landmark detection in X-ray images of the pelvis from arbitrary views [9]. The authors annotated 23 anatomical landmarks in CT volumes of the pelvis (Fig. 3, last column) and generated DRRs with annotations on a spherical segment covering 120 • and 90 • in RAO/LAO and CRAN/CAUD, respectively. Then, a sequential prediction framework is learned and, upon convergence, used to predict the 23 anatomical landmarks in unseen, real X-ray images of cadaver studies. The network is learned twice: First, on conventionally generated DRRs assuming a single material and mono-energetic spectrum, and second, on Deep-DRRs as described in Sec. 2.2. Images had 615 × 479 pixels with 0.616 2 mm pixel size. We used the spectrum of a tungsten anode operated at 120 kV