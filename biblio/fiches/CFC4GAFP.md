# PELE scores: pelvic X-ray landmark detection with pelvis extraction and enhancement.



## Resume


PELE scores: pelvic X-ray landmark detection with pelvis extraction and enhancement.

Pelvic X-ray (PXR) is widely utilized in clinical decision-making associated with the pelvis, the lower part of the trunk that supports and balances the trunk. In particular, PXR-based landmark detection facilitates downstream analysis and computer-assisted diagnosis and treatment of pelvic diseases. Although PXR has the advantages of low radiation and reduced cost compared to computed tomography (CT), it characterizes the 2D pelvis-tissue superposition of 3D structures, which may affect the accuracy of landmark detection in some cases. However, the superposition nature of PXR is implicitly handled by existing deep learning-based landmark detection methods, which mainly design the deep network structures for better detection performances. Explicit handling of the superposition nature of PXR is rarely done.

PFUS1: Premier pelvic floor ultrasound segmentation dataset. A resource for advancing research.

Fig. 1. Sharp angle values obtained with different patient positioning, demonstrating changes in pelvic inclination on an anteroposterior radiograph.

Learning to detect anatomical landmarks of the pelvis in X-rays from arbitrary views.

Minimally invasive alternatives are now available for many complex surgeries. These approaches are enabled by the increasing availability of intra-operative image guidance. Yet, fluoroscopic X-rays suffer from projective transformation and thus cannot provide direct views onto anatomy. Surgeons could highly benefit from additional information, such as the anatomical landmark locations in the projections, to support intra-operative decision making. However, detecting landmarks is challenging since the viewing direction changes substantially between views leading to varying appearance of the same landmark. Therefore, and to the best of our knowledge, view-independent anatomical landmark detection has not been investigated yet.

Multi-landmark environment analysis with reinforcement learning for pelvic abnormality detection and quantification

Landet: an efficient physics-informed deep learning approach for automatic detection of anatomical landmarks and measurement of spinopelvic alignment.

An efficient physics-informed deep learning approach for extracting spinopelvic measures from X-ray images is introduced and its performance is evaluated against manual annotations.

Optimization and benchmarking of image segmentation for improved landmark detection in lower limb X-rays and accurate coronal plane alignment of the knee classification_supp1-3572342.pdf

Fig. 1. Sharp's angle for different pelvic positions with changes in pelvic inclination on an anteroposterior radiograph.

Fig. 3. Method for measuring pelvic bone parameters: a, medial surface of the right pelvic bone; b, lateral surface of the right pelvic bone; c, pelvis. 1, anterior inferior iliac spine; 2, intersection point of the Y-shaped cartilage growth plate with the pubic crest; 3, intersection point of the Y-shaped cartilage growth plate with the obturator crest; 4, ischial spine; 5, reference point on the body of the S1 vertebra.

Two-stage multi-task deep learning framework for simultaneous pelvic bone segmentation and landmark detection from CT images.

Pelvic bone segmentation and landmark definition from computed tomography (CT) images are prerequisite steps for the preoperative planning of total hip arthroplasty. In clinical applications, the diseased pelvic anatomy usually degrades the accuracies of bone segmentation and landmark detection, leading to improper surgery planning and potential operative complications.

Learning-based landmark detection in pelvis x-rays with attention mechanism: data from the osteoarthritis initiative

Abstract
               Patients with developmental dysplasia of the hip can have this problem throughout their lifetime. The problem is difficult to detect by radiologists throughout x-ray because of an abrasion of anatomical structures. Thus, the landmarks should be automatically and precisely located. In this paper, we propose an attention mechanism of combining multi-dimension information on the basis of separating spatial dimension. The proposed attention mechanism decouples spatial dimension and forms width-channel dimension and height-channel dimension by 1D pooling operations in the height and width of spatial dimension. Then non-local means operations are performed to capture the correlation between long-range pixels in width-channel dimension, as well as that in height-channel dimension at different resolutions. The proposed attention mechanism modules are inserted into the skipped connections of U-Net to form a novel landmark detection structure. This landmark detection method was trained and evaluated through five-fold cross-validation on an open-source dataset, including 524 pelvis x-ray, each containing eight landmarks in pelvis, and achieved excellent performance compared to other landmark detection models. The average point-to-point errors of U-Net, HR-Net, CE-Net, and the proposed network were 3.5651 mm, 3.6118 mm, 3.3914 mm and 3.1350 mm, respectively. The results indicate that the proposed method has the highest detection accuracy. Furthermore, an open-source pelvis dataset is annotated and released for open research.

Anatomical landmark detection on bi-planar radiographs for predicting spinopelvic parameters.

Accurate landmark detection is essential for precise analysis of anatomical structures, supporting diagnosis, treatment planning, and monitoring in patients with spinal deformities. Conventional methods rely on laborious landmark identification by medical experts, which motivates automation. The proposed deep learning pipeline processes bi-planar radiographs to determine spinopelvic parameters and Cobb angles without manual supervision.

Table 1: Table depicting each cervical vertebrae (ordered) and some measurements.

Enhanced landmark detection model in pelvic fluoroscopy using 2D/3D registration loss


## Quote


Case report with clinical, pelvic ultrasound (US), and non-contrast pelvic MRI correlation before tissue expulsion, followed by pathologic examination and 3-month imaging follow-up

manual measurements obtained from anteroposterior pelvic X-rays exhibit considerable errors and poor reproducibility. This is primarily due to the strong subjectivity involved in different observers' identification of anatomical landmarks


## Insight


methodology: L’intégration d’une perte d’estimation de pose dans un U-Net de détection de landmarks pelviens vise à corriger la limitation des pertes de segmentation pixel-wise, qui ne pénalisent pas directement l’erreur géométrique de localisation, en couplant détection 2D et estimation de pose caméra pour le recalage 2D/3D.

methodology: Il s'agit de la première étude à appliquer une stratégie de landmarking (détection de points de repère) directement sur des échographies de hanche pour le diagnostic de la DDH, une approche jusque-là principalement utilisée sur des radiographies pelviennes, malgré la plus grande variabilité inhérente à l'imagerie échographique par rapport à l'imagerie radiographique.

methodology: Le rapport repose sur une vignette clinique monocas incluant un bilan biologique, un examen pelvien, une échographie pelvienne et une confirmation anatomopathologique du diagnostic.

radiographic evaluation: Des radiographies pelviennes ont été réalisées avant, immédiatement après, et à plusieurs intervalles postopératoires, avec une attention particulière portée à l'alignement symétrique des fémurs et des ailes iliaques pour assurer la précision des mesures.


## Raw_Sex_Estimates


Results can be found in the second table of Appendix 9. All criteria on each single pelvis provided estimates for the same sex.


## Raw_Results


measuring NA (Fig. 4). Main e®ects were found in both factors (p < 0:001), namely pelvic tilt and femoral elevation.


## Synthese


La détection de landmarks anatomiques sur fluoroscopie pelvienne constitue un enjeu clinique pour la planification chirurgicale et l’alignement biomécanique, notamment en arthroplastie totale de hanche, mais demeure limitée par la variabilité anatomique, les superpositions osseuses et la géométrie irrégulière du bassin. Les approches fondées sur un U-Net entraîné par segmentation avec une perte pixel-wise de type cross-entropy ne pénalisent pas directement l’erreur spatiale de localisation, ce qui peut produire des cartes de probabilité satisfaisantes tout en décalant les landmarks de plusieurs pixels. Les auteurs proposent d’intégrer une perte d’estimation de pose issue du recalage 2D/3D, couplant localisation 2D et estimation de la pose caméra θ ∈ SE(3), afin de pénaliser explicitement la distance euclidienne entre coordonnées prédites et de référence. Trois stratégies d’entraînement sont comparées sur des projections générées via DiffDRR (rotations aléatoires ∈ [−45°, 45°], translations ∈ [−50, 50]) : perte de pose seule, perte composite, et fine-tuning séquentiel après pré-entraînement par segmentation. Le fine-tuning d’un epoch avec perte d’estimation de pose améliore la précision par rapport au baseline (8,58 mm vs 8,45 mm sur le jeu de vues nouvelles ; 5,58 mm vs 5,09 mm sur le sujet tenu à l’écart), tandis que l’entraînement conjoint composite ou par perte de pose seule dégrade ou fait diverger l’apprentissage. Dans une comparaison expérimentale portant sur un U-Net de détection de landmarks en fluoroscopie pelvienne, le fine-tuning séquentiel avec une pose estimation loss (PEL) composite après pré-entraînement par segmentation a amélioré la précision par rapport au U-Net baseline. Les RMSE moyens du baseline étaient de 8,58 mm (jeu interne) et 5,58 mm (jeu externe), contre 8,45 mm (+1,5 %) et 5,09 mm (+8,8 %) pour le modèle fine-tuné. À l’inverse, l’entraînement conjoint avec PEL composite a multiplié l’erreur par environ 2,4 (interne) et 2,1 (externe) par rapport au baseline, tandis que la PEL seule a conduit à une divergence (DIV). Tous les modèles ont présenté une erreur plus faible sur le jeu externe que sur le jeu interne, avec des réductions de RMSE d’environ 35 % (baseline) et 40 % (fine-tuning). Les auteurs reconnaissent que, malgré des gains de précision obtenus par fine-tuning séquentiel, plusieurs limites méthodologiques persistent. Les images d’évaluation ont été simulées avec DiffDRR et peuvent ne pas reproduire le bruit, les artéfacts et la variabilité de la fluoroscopie peropératoire réelle, de sorte que l’efficacité clinique reste à confirmer. L’étude se limite à huit landmarks pelviens et le recours à L-BFGS dans la boucle d’entraînement allonge le temps de calcul. Les résultats indiquent néanmoins qu’un fine-tuning d’une époque avec une perte d’estimation de pose améliore la précision par rapport au U-Net baseline (8,45 mm vs 8,58 mm en interne ; 5,09 mm vs 5,58 mm en externe), alors que l’optimisation jointe (perte composite ou PEL seule) dégrade ou fait diverger l’apprentissage. Les auteurs proposent comme perspectives une validation sur fluoroscopies cliniques annotées, des estimateurs de pose moins coûteux, une pondération adaptative des pertes et l’ajout de cohérence temporelle pour les séquences vidéo.