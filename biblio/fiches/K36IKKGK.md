# Automatic Ground Truths: Projected Image Annotations for Omnidirectional Vision

**Auteurs** : Victor Stamatescu, Peter Barsznica, Manjung Kim, Kin K. Liu, Mark McKenzie, Will Meakin, Gwilyn Saunders, Sebastien C. Wong, Russell S. A. Brinkworth
**Année** : 2017

## Résumé

We present a novel data set made up of omnidirectional video of multiple objects whose centroid positions are annotated automatically. Omnidirectional vision is an active field of research focused on the use of spherical imagery in video analysis and scene understanding, involving tasks such as object detection, tracking and recognition. Our goal is to provide a large and consistently annotated video data set that can be used to train and evaluate new algorithms for these tasks. Here we describe the experimental setup and software environment used to capture and map the 3D ground truth positions of multiple objects into the image. Furthermore, we estimate the expected systematic error on the mapped positions. In addition to final data products, we release publicly the software tools and raw data necessary to re-calibrate the camera and/or redo this mapping. The software also provides a simple framework for comparing the results of standard image annotation tools or visual tracking syst

## Méthodologie

{'study_design': "Mise en place expérimentale combinant une caméra sphérique RICOH THETA m15 (double objectif fisheye, champ de vision 4π stéradians) fixe et un système de capture de mouvement VICON (8 caméras Bonita B10) enregistrant à environ 40 Hz la position (X, Y, Z) et l'orientation (pitch, roll, yaw) de chaque objet cible avec une précision sub-millimétrique ; les positions 3D sont ensuite projetées automatiquement (mapping) en coordonnées 2D de centroïdes dans l'image via calibration caméra (mire en damier) et calibration de pose (baguette VICON)", 'intervention': None, 'control': None, 'primary_outcomes': ["Positions 2D des centroïdes des objets cibles annotées automatiquement dans l'image", "Estimation de l'erreur systématique attendue sur les positions mappées"], 'secondary_outcomes': ["Comparaison des annotations automatiques avec des outils d'annotation d'image standards ou des systèmes de suivi visuel"], 'statistical_methods': [], 'duration': None, 'setting': "Laboratoire de l'UniSA (University of South Australia)"}

## Résultats

{'quantitative': [], 'qualitative_findings': ['Le système VICON permet un suivi 3D des objets avec une précision sub-millimétrique grâce à une constellation unique de marqueurs sur chaque objet', "Le mapping automatique des positions 3D vers 2D évite l'annotation humaine ad hoc, sujette à erreurs, et permet d'estimer systématiquement l'erreur sur les annotations de vérité terrain"], 'main_findings': ["Création de l'ensemble de données omnidirectionnelles UniSA comprenant 43 vidéos sphériques annotées d'objets mobiles et stationnaires dans des scénarios variés et complexes", "Développement d'une approche automatique inédite de mapping de vérité terrain 3D vers 2D, non implémentée auparavant dans les benchmarks publics de suivi visuel sans intervention humaine", 'Mise à disposition publique des données brutes (calibration et coordonnées mondiales) et des outils logiciels associés']}

## Conclusions

L'approche proposée constitue, à la connaissance des auteurs, la première mise en œuvre d'un mapping automatique de vérité terrain 3D vers l'image sans intervention d'annotateurs humains dans les benchmarks publics de suivi visuel L'ensemble de données UniSA omnidirectionnel peut être utilisé pour entraîner et évaluer des algorithmes de détection, suivi et reconnaissance fine d'objets multiples Un aspect clé du jeu de données est que la caméra peut être recalibrée et les annotations de vérité terrain re-mappées en conséquence

## Re-projection error in Session 1.

|  | mean (pixels) σ (pixels) Points |
| --- | --- | --- | --- |
| Left lens | 7.23 | 4.06 | 72 |
| Right lens | 5.80 | 4.21 | 56 |

## Re-projection error in Session 2.

|  | mean (pixels) σ (pixels) Points |
| --- | --- | --- | --- |
| Left lens | 6.73 | 3.21 | 48 |
| Right lens | 5.88 | 3.41 | 30 |

## Re-projection error in Session 3.

|  | mean (pixels) σ (pixels) Points |
| --- | --- | --- | --- |
| Left lens | 6.82 | 4.31 | 36 |
| Right lens | 5.17 | 2.52 | 22 |

### Formule


$$s m = A[R|t]M s   u v 1   =   f x 0 c x 0 f y c y 0 0 1     r 11 r 12 r 13 t 1 r 21 r 22 r 23 t 2 r 31 r 32 r 33 t 3       X Y Z 1     (1)$$

### Formule


$$  x y z   = R   X Y Z   + t x = x/z y = y/z x = x 1 + k 1 r 2 + k 2 r 4 + k 3 r 6 1 + k 4 r 2 + k 5 r 4 + k 6 r 6 +2p 1 x y + p 2 (r 2 + 2x 2 ) y = y 1 + k 1 r 2 + k 2 r 4 + k 3 r 6 1 + k 4 r 2 + k 5 r 4 + k 6 r 6 +p 1 (r 2 + 2y 2 ) + 2p 2 x y where r 2 = x 2 + y 2 u = f x × x + c x v = f y × y + c y(2)$$

### Formule


$$  x y z   = R   X Y Z   + t(3)$$

### Formule


$$r = x 2 + y 2 + z 2 θ = arccos z x 2 + y 2 + z 2 φ = arctan y x(4)$$
