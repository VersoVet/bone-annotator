# LiDSCUNet++: A lightweight depth separable convolutional UNet++ for vertebral column segmentation and spondylosis detection.



## Resume


LiDSCUNet++: A lightweight depth separable convolutional UNet++ for vertebral column segmentation and spondylosis detection.

Accurate computer-aided diagnosis systems rely on precise segmentation of the vertebral column to assist physicians in diagnosing various disorders. However, segmenting spinal disks and bones becomes challenging in the presence of abnormalities and complex anatomical structures. While Deep Convolutional Neural Networks (DCNNs) achieve remarkable results in medical image segmentation, their performance is limited by data insufficiency and the high computational complexity of existing solutions. This paper introduces LiDSCUNet++, a lightweight deep learning framework based on depthwise-separable and pointwise convolutions integrated with UNet++ for vertebral column segmentation. The model segments vertebral anomalies from dog radiographs, and the results are further processed by YOLOv8 for automated detection of Spondylosis Deformans. LiDSCUNet++ delivers comparable segmentation performance while significantly reducing trainable parameters, memory usage, energy consumption, and computati

ADNet++: A few-shot learning framework for multi-class medical image volume segmentation with uncertainty-guided feature refinement

VertXNet: Automatic Segmentation and Identification of Lumbar and Cervical Vertebrae from Spinal X-ray Images

Manual annotation of vertebrae on spinal X-ray imaging is costly and time-consuming due to bone shape complexity and image quality variations. In this study, we address this challenge by proposing an ensemble method called VertXNet, to automatically segment and label vertebrae in X-ray spinal images. VertXNet combines two state-of-the-art segmentation models, namely U-Net and Mask R-CNN to improve vertebrae segmentation. A main feature of VertXNet is to also infer vertebrae labels thanks to its Mask R-CNN component (trained to detect 'reference' vertebrae) on a given spinal X-ray image. VertXNet was evaluated on an in-house dataset of lateral cervical and lumbar X-ray imaging for ankylosing spondylitis (AS) patients. Our results show that VertXNet can accurately label spinal X-rays (mean Dice of 0.9). It can be used to circumvent the lack of annotated vertebrae without requiring human expert review. This step is crucial to investigate clinical associations by solving the lack of segmen

A Dual Coordinate System Vertebra Landmark Detection Network with Sparse-to-Dense Vertebral Line Interpolation

Precise surveillance and assessment of spinal disorders are important for improving health care and patient survival rates. The assessment of spinal disorders, such as scoliosis assessment, depends heavily on precise vertebra landmark localization. However, existing methods usually search for only a handful of keypoints in a high-resolution image. In this paper, we propose the S2D-VLI VLDet network, a unified end-to-end vertebra landmark detection network for the assessment of scoliosis. The proposed network considers the spatially relevant information both from inside and between vertebrae. The new vertebral line interpolation method converts the training labels from sparse to dense, which can improve the network learning process and method performance. In addition, through the combined use of the Cartesian and polar coordinate systems in our method, the symmetric mean absolute percentage error (SMAPE) in scoliosis assessment can be reduced substantially. Specifically, as shown in the

A Deep Learning-Based Fully Automated Vertebra Segmentation and Labeling Workflow.

Aims/Background Spinal disorders, such as herniated discs and scoliosis, are highly prevalent conditions with rising incidence in the aging global population. Accurate analysis of spinal anatomical structures is a critical prerequisite for achieving high-precision positioning with surgical navigation robots. However, traditional manual segmentation methods are limited by issues such as low efficiency and poor consistency. This work aims to develop a fully automated deep learning-based vertebral segmentation and labeling workflow to provide efficient and accurate preoperative analysis support for spine surgery navigation robots.
                  Methods In the localization stage, the You Only Look Once version 7 (YOLOv7) network was utilized to predict the bounding boxes of individual vertebrae on computed tomography (CT) sagittal slices, transforming the 3D localization problem into a 2D one. Subsequently, the Density-Based Spatial Clustering of Applications with Noise (DBSCAN) clustering algorithm was employed to aggregate the 2D detection results into 3D vertebral centers. This approach significantly reduces inference time and enhances localization accuracy. In the segmentation stage, a 3D U-Net model integrated with an attention mechanism was trained using the region of interest (ROI) based on the vertebral center as input, effectively extracting the 3D structural features of vertebrae to achieve precise segmentation. In the labeling stage, a vertebra labeling network was trained by combining deep learning architectures—ResNet and Transformer, which are capable of extracting rich intervertebral features, to obtain the final labeling results through post-processing based on positional logic analysis. To verify the effectiveness of this workflow, experiments were conducted on a dataset comprising 106 spinal CT datasets sourced from various devices, covering a wide range of clinical scenarios.
                  Results The results demonstrate that the method performed excellently in the three key tasks of localization, segmentation, and labeling, with a Mean Localization Error (MLE) of 1.42 mm. The segmentation accuracy metrics included a Dice Similarity Coefficient (DSC) of 0.968 ± 0.014, Intersection over Union (IoU) of 0.879 ± 0.018, Pixel Accuracy (PA) of 0.988 ± 0.005, mean symmetric distance (MSD) of 1.09 ± 0.19 mm, and Hausdorff Distance (HD) of 5.42 ± 2.05 mm. The degree of classification accuracy reached up to 94.36%.
                  Conclusion These quantitative assessments and visualizations confirm the effectiveness of our method (vertebra localization, vertebra segmentation and vertebra labeling), indicating its potential for deployment in spinal surgery navigation robots to provide accurate and efficient preoperative analysis and navigation support for spinal surgeries.

Panoptic Segmentation and Labelling of Lumbar Spine Vertebrae using Modified Attention Unet

Segmentation and labeling of vertebrae in MRI images of the spine are critical for the diagnosis of illnesses and abnormalities. These steps are indispensable as MRI technology provides detailed information about the tissue structure of the spine. Both supervised and unsupervised segmentation methods exist, yet acquiring sufficient data remains challenging for achieving high accuracy. In this study, we propose an enhancing approach based on modified attention U-Net architecture for panoptic segmentation of 3D sliced MRI data of the lumbar spine. Our method achieves an impressive accuracy of 99.5\% by incorporating novel masking logic, thus significantly advancing the state-of-the-art in vertebral segmentation and labeling. This contributes to more precise and reliable diagnosis and treatment planning.

Deep learning segmentation of mandible with lower dentition from cone beam CT.

This study aimed to train a 3D U-Net convolutional neural network (CNN) for mandible and lower dentition segmentation from cone-beam computed tomography (CBCT) scans.

ComBiNet: Compact Convolutional Bayesian Neural Network for Image Segmentation

Leveraging deep learning semantic segmentation for imaging coral skeletons.

Micro-computed tomography and semantic segmentation provide insights into the structural hierarchy of biomineralized tissues, as exemplified by stony coral skeletons. Non-destructive imaging reveals mechanistic aspects of skeletal growth, including variations in porosity, density, and skeletal thickness across species and in the context of disease. Recent developments in semantic segmentation based on convolutional neural network models are poised to transform the streamlined analysis of large 3D tomography datasets, surpassing the performance of traditional segmentation methods. In this work, a series of U-Net deep learning models were trained and applied on exemplary micro-CT datasets from stony corals pertaining to Montastraea cavernosa and Porites astreoides species for the segmentation of pores and skeleton. The models were statistically evaluated, revealing that Attention U-Net was the top performer with respect to computational efficiency, accuracy, and generalizability, followe


## Raw_Full_Text


.1148/radiol.2021204021 
51. Guinebert S, Petit E, Bousson V, Bodard S, Amoretti N, Kastler B. Automatic semantic 
segmentation and detection of vertebras and intervertebral discs by neural networks. 
Comput Methods Programs Biomed Update [Internet]. 1 janv 2022 [cité 1 juill 
2024];2:100055. 
Disponible 
sur: 
https://www.sciencedirect.com/science/article/pii/S2666990022000076 
52. Liu F, Zhou Z, Jang H, Samsonov A, Zhao G, Kijowski R. Deep convolutional neural network 
and 3D deformable approach for tissue segmentation in musculoskeletal magnetic 
resonance imaging. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];79(4):2379‑91. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/10.1002/mrm.26841 
53. Zhou Z, Zhao G, Kijowski R, Liu F. Deep convolutional neural network for segmentation of 
knee joint anatomy. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];80(6):2759‑70. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/

.1148/radiol.2021204021 
51. Guinebert S, Petit E, Bousson V, Bodard S, Amoretti N, Kastler B. Automatic semantic 
segmentation and detection of vertebras and intervertebral discs by neural networks. 
Comput Methods Programs Biomed Update [Internet]. 1 janv 2022 [cité 1 juill 
2024];2:100055. 
Disponible 
sur: 
https://www.sciencedirect.com/science/article/pii/S2666990022000076 
52. Liu F, Zhou Z, Jang H, Samsonov A, Zhao G, Kijowski R. Deep convolutional neural network 
and 3D deformable approach for tissue segmentation in musculoskeletal magnetic 
resonance imaging. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];79(4):2379‑91. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/10.1002/mrm.26841 
53. Zhou Z, Zhao G, Kijowski R, Liu F. Deep convolutional neural network for segmentation of 
knee joint anatomy. Magn Reson Med [Internet]. 2018 [cité 1 juill 2024];80(6):2759‑70. 
Disponible 
sur: 
https://onlinelibrary-wiley-com.ezproxy.u-
paris.fr/doi/abs/


## Insight


methodology: Un modèle de segmentation Attention U-Net modifié, entraîné sur 162 radiographies latérales thoraco-lombaires et lombaires de chiens étiquetées manuellement par 13 cliniciens vétérinaires, a été développé pour segmenter simultanément le corps vertébral et détecter la spondylose déformante par classification pixel par pixel.

methodology: Les architectures de réseaux telles que ResNet, VGGNet, Inception Net, DenseNet et U-Net illustrent une tendance générale à l'approfondissement des réseaux convolutifs afin d'améliorer la visualisation des anomalies osseuses, alors que l'application du DL aux images CT pour la détection de fractures reste nettement moins étudiée que celle sur les radiographies standards.

methodology: Les réseaux de neurones convolutifs profonds (DCNN) ont permis d'automatiser et d'améliorer la précision de la détection et de la segmentation cellulaire dans les images de microscopie tissulaire, notamment via des approches complémentaires de segmentation sémantique (U-Net) et de segmentation d'instance (Mask R-CNN, NuSeT).


## Synthese


Cet article, publié en 2023 dans le Journal of Applied Clinical Medical Physics, s'inscrit dans la problématique de la segmentation automatique des vertèbres lombaires en imagerie tomodensitométrique (CT), une tâche cliniquement essentielle pour la détection d'anomalies vertébrales et l'aide au traitement chirurgical, mais dont la réalisation manuelle par les radiologues demeure chronophage, coûteuse et sujette à une variabilité inter-observateur significative. Les auteurs proposent une méthode d'apprentissage profond en deux étapes séquentielles : un premier réseau de localisation fondé sur une architecture UNet, prenant en entrée des volumes de taille 96*96*128*1, qui génère une carte de chaleur (heatmap) permettant de localiser la colonne lombaire dans l'image CT, suivi d'un recadrage (cropping) automatique fondé sur un seuillage des valeurs Hounsfield (voxels dont la valeur HU dépasse 0,3 fois la valeur HU maximale de l'image) et d'une expansion de la boîte englobante de 0,1 fois la taille de l'image dans chaque dimension. La seconde étape repose sur un réseau de segmentation 3D original dénommé XUNet, opérant sur des volumes recadrés de taille 64*64*128*1, dont l'encodeur à quatre couches (canaux 32, 64, 128, 256) intègre à sa quatrième couche un bloc de type Inception à faible nombre de paramètres combinant des noyaux de convolution de tailles 1*1*1, 3*3*3 et 5*5*5, et dont le décodeur à trois couches réalise une fusion de caractéristiques multi-échelles avant une couche Softmax finale produisant le masque de segmentation. La méthode a été validée sur un total de 656 volumes CT tridimensionnels de la colonne lombaire, provenant de deux sources distinctes : le jeu de données public VerSe 2020 (156 échantillons, évalués par validation croisée à 5 plis) et un jeu de données hospitalier interne (500 échantillons, répartis en 400 pour l'entraînement et 100 pour le test), avec des vérités terrain établies par des radiologues. Les comparaisons quantitatives (Tables 1 et 2) et qualitatives (visualisations 2D et 3D) montrent que la méthode proposée surpasse un UNet classique ainsi que la méthode IFCN (iterative fully convolutional neural method), et atteint une performance comparable à celle de nnUnet, bien que les valeurs numériques exactes de ces comparaisons ne soient pas disponibles dans le texte intégral fourni pour cette synthèse. Une étude d'ablation (Table 3) confirme la contribution indépendante du module de positionnement/localisation et du module Inception à la performance globale du modèle, sans que les valeurs chiffrées précises ne soient non plus accessibles dans les extraits disponibles. Les auteurs concluent que cette approche en deux étapes constitue une méthode performante et automatisable de segmentation des vertèbres lombaires, potentiellement transférable à la pratique clinique pour la détection d'anomalies vertébrales et l'assistance à la planification chirurgicale, en remplacement de la délinéation manuelle. Les principales limites identifiables à partir des éléments disponibles concernent l'absence de restitution des valeurs chiffrées exactes de performance (métriques de type Dice, IoU ou distances de surface ne sont pas explicitées dans les extraits fournis), ce qui restreint la possibilité d'une appréciation quantitative rigoureuse et d'une comparaison statistique formelle avec les méthodes concurrentes.


## Quote


A UNet++ segmentation algorithm was employed to segment bone axes... Subsequently, a linear regression module was utilized to derive the HVA and IMA from the segmentation results.

By using advanced models like I3D and VGG-16 for phase classification, SSD for anatomical landmark detection, and U-Net-based approaches for segmentation, VFSS assessments become more objective and precise.

Deep learning using a U-NET demonstrates promise in the automated segmentation of vertebrae on lateral chest radiographs.

methods used for vertebrae localization and vertebrae segmentation are presented respectively in detail incl. data preparation for training and testing, Dense-U-Net architecture, and postprocessing of predicted results

While a convolutional ensemble model (comprising VGG-16, Inception, ResNet, and EfficientNet architectures) was used for image classification, U-Net architecture was used for segmentation. The DL-trained AI model was developed to identify teeth, evaluate remaining periodontal bone height, and compare results with clinician assessments.


## Discussion


Cette étude propose BS-Net, un modèle de segmentation vertébrale lombaire fondé sur UNet et intégrant un module de traitement conjoint des contours (MEP) et un module de fusion bilatérale contextuelle (CBF), complété par un post-traitement par champs aléatoires conditionnels (CRF) afin d'affiner les bords segmentés. La méthode du rectangle englobant minimal (Minimum Bounding Rectangle) a été retenue, après comparaison de plusieurs approches géométriques, pour automatiser le calcul du glissement vertébral. Les résultats expérimentaux montrent que BS-Net surpasse plusieurs modèles de segmentation sémantique de référence en précision de segmentation et en détection des contours vertébraux, les études d'ablation confirmant l'effet synergique des modules MEP, CBF et des fonctions de perte liées aux contours. La robustesse et la généralisabilité du modèle ont été validées sur des jeux de données publics tels que SPIDER IRM, et la méthode de quantification du spondylolisthésis présente une bonne cohérence avec les mesures manuelles. Les auteurs soulignent toutefois des limites persistantes en présence d'implants métalliques, de déformations sévères ou de dégénérescence marquée, cas dans lesquels la segmentation des marges vertébrales peut échouer, et proposent d'orienter les travaux futurs vers l'intégration de données multimodales diversifiées et de mécanismes d'expert-in-the-loop.

Cette étude démontre qu'un réseau de neurones entièrement convolutif unique, entraîné pour une segmentation itérative vertèbre par vertèbre, surpasse une approche multiclasse conventionnelle de type 3D U-net en simplifiant le problème en une tâche binaire de classification de voxels par instance. Le même réseau parvient à combiner de façon concurrente trois tâches — segmentation, identification anatomique et classification de complétude — sans dégradation des performances de segmentation, tout en limitant la charge d'entraînement et d'inférence à un modèle unique. L'approche, entièrement supervisée et évaluée sur des jeux de données CT et IRM hétérogènes (incluant des scans à faible dose, des morphologies déformées et un jeu de données lombaire totalement indépendant de l'entraînement), généralise mieux que les méthodes antérieures typiquement conçues pour un seul type d'image. La stratégie de parcours du rachis de haut en bas s'est révélée légèrement moins performante que le parcours inverse sur les scans thoraciques à faible dose, en raison de la petite taille et des artefacts affectant les vertèbres cervicales supérieures.


## Conclusion


La méthode de segmentation automatique des vertèbres lombaires en deux étapes (positionnement par UNet puis segmentation par XUNet 3D multi-échelle basé sur des blocs Inception) proposée dans cet article permet d'obtenir une bonne performance de segmentation des vertèbres lombaires, validée à la fois sur le jeu de données public VerSe 2020 et sur un jeu de données hospitalier. Cette méthode automatique pourrait être appliquée en pratique clinique à la détection d'anomalies vertébrales et à l'aide au traitement chirurgical, en remplaçant la délinéation manuelle chronophage et sujette à variabilité inter-observateur.

L'approche machine-agnostic proposée permet une segmentation automatique robuste des vertèbres lombaires et des IVD à partir d'images IRM issues de scanners variés, avec un DSC de 91.03%, un IoU de 83.66% et une précision au pixel de 99.78% Les méthodes de segmentation traditionnelles sont souvent sous-performantes pour cette tâche en raison du faible contraste des images et de la variabilité inter- et intra-scanner, problème que ce modèle cherche à surmonter Cette approche pourrait faciliter l'automatisation du diagnostic de plusieurs troubles et maladies liés à la colonne vertébrale, sous réserve d'une expansion future du jeu de données et d'un raffinement du modèle


## Resultats


Cette étude évalue des architectures d'apprentissage profond 2D, notamment les réseaux de neurones convolutifs (CNN) et les réseaux de croyance profonde (DBN), pour la classification et la détection de nodules pulmonaires à partir du dataset LIDC, comprenant 1 010 patients et 2 545 nodules de diamètre supérieur à 3 mm, avec validation croisée leave-one-out. Ces méthodes permettent de s'affranchir de l'extraction manuelle de features, contrairement aux systèmes CAD traditionnels. Plusieurs approches combinant CNN 2D à divers classificateurs (autoencodeur, ensemble de classificateurs, architecture DetectNet dérivée de YOLO, Faster R-CNN modifié) atteignent des performances élevées, certaines proches du niveau des radiologues, pour la classification de la malignité et la détection des nodules. L'exploitation de multiples plans (axial, coronal, sagittal) permet de conserver partiellement l'information tridimensionnelle tout en limitant les ressources de calcul requises par rapport aux approches 3D complètes.