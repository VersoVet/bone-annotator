# InstaDam: Open-Source Platform for Rapid Semantic Segmentation of Structural Damage

**Auteurs** : Vedhus Hoskere, Fouad Amer, Doug Friedel, Wanxian Yang, Yu Tang, Yasutaka Narazaki, Matthew D. Smith, Mani Golparvar-Fard, Billie F. Spencer
**Année** : 2021
**DOI** : 10.3390/app11020520

## Résumé

The tremendous success of automated methods for the detection of damage in images of civil infrastructure has been fueled by exponential advances in deep learning over the past decade. In particular, many efforts have taken place in academia and more recently in industry that demonstrate the success of supervised deep learning methods for semantic segmentation of damage (i.e., the pixel-wise identification of damage in images). However, in graduating from the detection of damage to applications such as inspection automation, efforts have been limited by the lack of large open datasets of real-world images with annotations for multiple types of damage, and other related information such as material and component types. Such datasets for structural inspections are difficult to develop because annotating the complex and amorphous shapes taken by damage patterns remains a tedious task (requiring too many clicks and careful selection of points), even with state-of-the art annotation softwar

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': [], 'main_findings': []}

## Conclusions

InstaDam est une plateforme logicielle open source pour l'annotation pixel par pixel rapide des dommages structurels InstaDam propose diverses techniques de traitement d'image (IPTs) pour générer des masques accélérant le processus d'annotation Le logiciel inclut des outils d'annotation développés en Qt C++ et un framework de gestion de données cloud développé en Python avec Flask InstaDam offre une réduction de 63% du temps d'annotation par rapport aux logiciels d'annotation existants InstaDam améliore la cohérence entre annotateurs pour plusieurs types de défauts couramment annotés tels que les fissures et les câbles L'analyse des données utilisateur montre que les IPTs implémentés sont largement utilisés, indiquant le besoin de tels outils La combinaison des fonctionnalités d'InstaDam permet des annotations efficaces et cohérentes, facilitant le développement de grands ensembles de données pour les inspections structurelles

## Computation time for different image processing techniques.

| IPT | Processing Time for 1 MP Image (ms) | IPT Parameters |
| --- | --- | --- |
| Common parameters | 0.65 | invert |
| Threshold | 1.24 | threshold |
| Otsu | 1.85 | NA |
| Morphology | 2.77 | erode, dilate, open close |
| Local Adaptive Threshold | 3.06 | strength, detail |
| Gaussian blur | 5.25 | kernel size, threshold, |
| Canny edge | 21.32 | threshold min, threshold max, kernel size |
| Color distance | 25.26 | R, G, B, fuzziness |
| Ridge filter | 50.02 | scale |
| Guided filter | 50.44 | threshold, diameter, sigma |
