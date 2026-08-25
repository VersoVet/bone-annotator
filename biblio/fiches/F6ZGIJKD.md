# VIBESegmentator: full body MRI segmentation for the NAKO and UK Biobank.

**Auteurs** : Graf R, Platzek P, Riedel EO, Ramschütz C, Starck S, Möller HK, Atad M, Völzke H, Bülow R, Schmidt CO
**Année** : 2026
**DOI** : 10.1007/s00330-025-12035-9

## Résumé

<h4>Objectives</h4>To present a publicly available deep learning-based torso segmentation model that provides comprehensive voxel-wise coverage, including delineations that extend to the boundaries of anatomical compartments.<h4>Materials and methods</h4>We extracted preliminary segmentations from TotalSegmentator, spine, and body composition models for magnetic resonance tomography (MR) images, then improved them iteratively and retrained an nnUNet model. Using a random retrospective subset of German National Cohort (NAKO), UK Biobank, internal MR and computed tomography (CT) data (Training: 2897 series from 626 subjects, 290 female; mean age 53 ± 16; 3-fold-cross validation (20% hold-out). Internal testing 36 series from 12 subjects, 6 male; mean age 60 ± 11), we segmented 71 structures in torso MR and 72 in CT images: 20 organs, 10 muscles, 19 vessels, 16 bones, ribs in CT, intervertebral discs, spinal cord, spinal canal and body composition (subcutaneous fat, unclassified muscles a

## Méthodologie

{'study_design': "Stratégie d'entraînement itérative utilisant le framework nnUNet, où des labels nouvellement générés sont corrigés manuellement et utilisés pour améliorer le modèle à l'itération d'entraînement suivante ; utilisation de 3 folds sur les 5 folds standards de la validation croisée du framework nnUNet", 'intervention': "Entraînement d'un modèle nnUNet unifié pour la segmentation sémantique de 71 structures tissulaires en IRM et 72 en CT, à partir de séquences écho de gradient stitchées pour la séparation eau-graisse (UKBB, NAKO, champ de vue du cou au genou), séquences T2 HASTE torse, images en densité de protons (hanche), séquences Dixon six-points T1 écho de gradient (abdomen), séquences turbo spin écho T2 sagittales (rachis) de NAKO, ainsi que données IRM internes (incluant images avec contraste) et scans CT corps entier ; toutes les images rééchantillonnées à une résolution dans le plan axial de 1,4 mm et une résolution à travers le plan de 3 mm", 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': "Cohortes de population NAKO et UK Biobank, ainsi que données internes (IRM et CT) ; approbation éthique obtenue des comités d'éthique respectifs pour NAKO et UKBB (consentement éclairé recueilli) ; pour les données internes, approbation obtenue du comité d'éthique local (593/21 S-NP), consentement éclairé dispensé"}

## Résultats

{'quantitative': [{'outcome': "Nombre de coupes 2D dans le dataset d'entraînement final", 'value': '608,809', 'unit': 'coupes 2D', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The final training dataset consisted of 608,809 2D slices from 626 subjects, comprising a total of 2,897 series.'}, {'outcome': "Nombre de sujets dans le dataset d'entraînement final", 'value': '626', 'unit': 'sujets', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The final training dataset consisted of 608,809 2D slices from 626 subjects, comprising a total of 2,897 series.'}, {'outcome': "Nombre total de séries dans le dataset d'entraînement final", 'value': '2,897', 'unit': 'séries', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'The final training dataset consisted of 608,809 2D slices from 626 subjects, comprising a total of 2,897 series.'}], 'qualitative_findings': ['Des exemples de segmentation sont fournis sur des séquences VIBE (Fig. 3)', "Des exemples de segmentation sont fournis sur d'autres modalités IRM et sur CT (Fig. 4)"], 'main_findings': ["Le dataset d'entraînement final comprend 608,809 coupes 2D issues de 626 sujets, totalisant 2,897 séries", "Le modèle produit des segmentations illustrées sur des séquences VIBE ainsi que sur d'autres modalités IRM et sur CT"]}

## Conclusions

Le modèle proposé constitue une avancée significative dans le domaine de la segmentation IRM, offrant une approche détaillée et affinée de la segmentation full-torso, en particulier pour les grands jeux de données comme UKBB ou NAKO Le modèle peut être utilisé pour le traitement automatique et l'extraction de structures en IRM Il s'agit du modèle de segmentation full-torso le plus détaillé à ce jour, permettant une classification de presque tous les voxels dans le torse

## Dice score and 95% confidence interval (CI) on Freiburg Gradient Echo images

| Label name | This study | D'Antonoli et al | Häntze et al | Zhuang et al | Ma et al |
| --- | --- | --- | --- | --- | --- |
|  |  | TotalSegmentor MRI | MRSegmentator | MRISegmenter | Medsam2 |
|  | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] |
| Liver | 0.93 [0.92-0.93] | 0.93 [0.93-0.94] | 0.94 [0.93-0.94] | 0.88 [0.87-0.90] | 0.80 [0.75-0.84] |
| Pancreas | 0.81 [0.81-0.82] | 0.77 [0.76-0.78] | 0.74 [0.73-0.75] | 0.43 [0.38-0.48] | 0.73 [0.70-0.76] |
| Prostate | 0.79 a [0.78-0.80] | 0.80 [0.79-0.81] | N/A | N/A | 0.48 [0.45-0.50] |
| Aorta | 0.89 a [0.89-0.89] | 0.88 [0.88-0.89] | 0.87 [0.86-0.87] | 0.68 [0.68-0.69] | 0.68 [0.66-0.71] |

## Dice score and 95% confidence interval (CI) on internal test data of NAKO and UK Biobank Gradient Echo data

| Label name | Group | This study | D'Antonoli et al | Häntze et al | Zhuang et al | Ma et al |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | TotalSegmentator MRI | MRSegmentator | MRISegmenter | Medsam2 |
|  |  | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] |
| Sacrum | Bone | 0.95 [0.94-0.95] | 0.63 [0.61-0.65] | 0.72 [0.71-0.72] | 0.14 [0.11-0.17] 0.42 [0.39-0.46] |
| Humerus left | Bone | 0.94 [0.93-0.95] | 0.71 [0.70-0.73] | N/A | N/A | 0.65 [0.59-0.71] |
| Humerus right | Bone | 0.94 [0.93-0.94] | 0.72 [0.71-0.73] | N/A | N/A | 0.64 [0.57-0.70] |
| Scapula left | Bone | 0.91 [0.91-0.92] | 0.48 [0.47-0.50] | N/A | N/A | 0.19 [0.18-0.20] |
| Scapula right | Bone | 0.91 [0.90-0.92] | 0.48 [0.46-0.49] | N/A | N/A | 0.19 [0.17-0.20] |
| Clavicula left | Bone | 0.88 [0.86-0.89] | 0.45 [0.42-0.49] | N/A | N/A | 0.14 [0.11-0.17] |
| Clavicula right | Bone | 0.88 [0.87-0.89] | 0.37 [0.33-0.40] | N/A | N/A | 0.19 [0.15-0.23] |
| Femur left | Bone | 0.96 [0.96-0.97] | 0.82 [0.81-0.83] | 0.82 [0.82-0.82] | N/A | 0.38 [0.29-0.47] |
| Femur right | Bone | 0.96 [0.95-0.96] | 0.83 [0.83-0.84] | 0.83 [0.82-0.83] | N/A | 0.43 [0.34-0.53] |
| Hip left | Bone | 0.94 [0.94-0.95] | 0.70 [0.69-0.72] | 0.73 [0.72-0.73] | 0.05 [0.03-0.08] 0.22 [0.18-0.26] |
| Hip right | Bone | 0.94 [0.94-0.95] | 0.67 [0.66-0.69] | 0.73 [0.73-0.74] | 0.05 [0.03-0.07] 0.21 [0.18-0.25] |
| Sternum | Bone | 0.86 [0.84-0.88] | N/A | N/A | N/A | 0.21 [0.18-0.24] |
| Stomach | Digestion 0.89 [0.88-0.91] | 0.82 [0.80-0.84] | 0.84 [0.82-0.86] | 0.68 [0.62-0.74] 0.40 [0.35-0.46] |
| Pancreas | Digestion 0.87 [0.86-0.89] | 0.62 [0.57-0.67] | 0.68 [0.65-0.70] | 0.45 [0.36-0.54] 0.37 [0.31-0.43] |
| Esophagus a | Digestion 0.88 [0.87-0.89] | 0.49 [0.45-0.52] | 0.48 [0.45-0.51] | 0.15 [0.12-0.18] 0.09 [0.08-0.11] |
| Intestine | Digestion 0.92 [0.92-0.93] | 0.67 [0.64-0.69] | 0.75 [0.73-0.77] | 0.53 [0.50-0.56] 0.39 [0.34-0.43] |
| Duodenum | Digestion 0.85 [0.83-0.87] | 0.57 [0.52-0.61] | 0.61 [0.56-0.66] | 0.41 [0.34-0.48] 0.36 [0.30-0.41] |
| Adrenal gland right | Gland | 0.81 [0.78-0.83] | 0.56 [0.53-0.59] | 0.57 [0.53-0.60] | 0.39 [0.32-0.46] 0.24 [0.17-0.31] |
| Adrenal gland left | Gland | 0.82 [0.80-0.83] | 0.51 [0.47-0.56] | 0.61 [0.58-0.64] | 0.26 [0.16-0.36] 0.27 [0.22-0.31] |
| Thyroid gland | Gland | 0.76 [0.73-0.80] | N/A | N/A | N/A | 0.27 [0.18-0.34] |
| Gluteus maximus left | Muscle | 0.97 [0.97-0.97] | 0.72 [0.71-0.74] | 0.76 [0.75-0.77] | 0.00 [0.00-0.00] 0.81 [0.78-0.84] |
| Gluteus maximus right | Muscle | 0.97 [0.97-0.97] | 0.72 [0.71-0.73] | 0.78 [0.77-0.79] | 0.00 [0.00-0.00] 0.82 [0.80-0.83] |
| Gluteus medius left | Muscle | 0.94 [0.94-0.95] | 0.73 [0.70-0.75] | 0.78 [0.78-0.79] | 0.08 [0.05-0.11] 0.70 [0.66-0.73] |
| Gluteus medius right | Muscle | 0.96 [0.95-0.96] | 0.76 [0.74-0.78] | 0.82 [0.82-0.83] | 0.02 [0.01-0.03] 0.71 [0.68-0.74] |
| Gluteus minimus left | Muscle | 0.93 [0.92-0.94] | 0.55 [0.53-0.57] | 0.59 [0.57-0.60] | N/A | 0.40 [0.36-0.45] |
| Gluteus minimus right | Muscle | 0.93 [0.92-0.94] | 0.57 [0.55-0.59] | 0.62 [0.60-0.64] | N/A | 0.41 [0.37-0.44] |
| Autochthon left | Muscle | 0.96 [0.96-0.96] | 0.65 [0.64-0.66] | 0.65 [0.64-0.66] | 0.69 [0.66-0.72] 0.51 [0.46-0.56] |
| Autochthon right | Muscle | 0.96 [0.96-0.97] | 0.64 [0.63-0.66] | 0.65 [0.64-0.66] | 0.70 [0.66-0.73] 0.56 [0.53-0.59] |
| Iliopsoas left | Muscle | 0.95 [0.95-0.96] | 0.77 [0.75-0.78] | 0.72 [0.71-0.73] | 0.43 [0.37-0.48] 0.63 [0.57-0.68] |
| Iliopsoas right | Muscle | 0.95 [0.95-0.96] | 0.75 [0.73-0.76] | 0.71 [0.70-0.72] | 0.34 [0.29-0.39] 0.57 [0.49-0.63] |
| Spleen | Organ | 0.93 [0.92-0.94] | 0.90 [0.89-0.91] | 0.91 [0.90-0.92] | 0.79 [0.72-0.85] 0.85 [0.82-0.87] |
| Kidney right | Organ | 0.92 [0.91-0.93] | 0.89 [0.88-0.90] | 0.92 [0.91-0.93] 0.87 [0.84-0.89] 0.81 [0.77-0.84] |
| kidney left | Organ | 0.92 [0.91-0.92] | 0.91 [0.89-0.92] | 0.93 [0.93-0.94] 0.87 [0.84-0.89] 0.83 [0.81-0.86] |
| Gallbladder | Organ | 0.82 [0.78-0.85] | 0.56 [0.47-0.65] | 0.57 [0.49-0.65] | 0.58 [0.49-0.66] 0.54 [0.46-0.60] |
| Liver | Organ | 0.97 [0.97-0.97] | 0.92 [0.91-0.92] | 0.94 [0.94-0.95] | 0.89 [0.86-0.92] 0.85 [0.82-0.87] |
| Lung left | Organ | 0.97 [0.96-0.97] | 0.91 [0.90-0.92] | 0.91 [0.90-0.93] | 0.76 [0.73-0.79] 0.84 [0.81-0.87] |
| Lung right | Organ | 0.97 [0.97-0.98] | 0.92 [0.91-0.93] | 0.92 [0.90-0.93] | 0.80 [0.78-0.83] 0.86 [0.84-0.89] |
| Trachea | Organ | 0.90 [0.89-0.91] | N/A | N/A | N/A | 0.10 [0.09-0.13] |
| Urinary bladder | Organ | 0.94 [0.93-0.95] | 0.82 [0.78-0.86] | 0.86 [0.84-0.88] | N/A | 0.75 [0.69-0.81] |
| Prostate | Organ | 0.93 [0.92-0.94] | 0.74 [0.70-0.78] | N/A | N/A | 0.67 [0.62-0.73] |
| Heart | Organ | 0.96 [0.95-0.96] | 0.83 [0.82-0.84] | 0.88 [0.87-0.88] | N/A | 0.81 [0.79-0.82] |
| Spinal cord | Spine | 0.86 [0.84-0.88] | N/A | N/A | N/A | 0.12 [0.09-0.17] |
| IVD | Spine | 0.87 [0.86-0.89] | 0.72 [0.70-0.74] | N/A | N/A | 0.24 [0.22-0.26] |
| Vertebra body | Spine | 0.92 [0.92-0.93] | 0.81 [0.80-0.82] | 0.70 [0.70-0.71] | N/A | 0.54 [0.49-0.59] |
| Vertebra posterior elements Spine | 0.84 [0.83-0.85] | N/A | N/A | N/A | 0.15 [0.13-0.17] |
| Spinal channel | Spine | 0.89 [0.88-0.91] | 0.66 [0.64-0.67] | N/A | N/A | 0.13 [0.10-0.16] |

## Dice score and 95% confidence interval (CI) on Amos MR images training and test set combined

| Label name | This study | D'Antonoli et al | Häntze et al | Zhuang et al | Ma et al |
| --- | --- | --- | --- | --- | --- |
|  |  | TotalSegmentator MRI | MRSegmentator | MRISegmenter | Medsam2 |
|  | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] |
| Spleen | 0.96 [0.95-0.96] | 0.91 [0.90-0.91] | 0.93 [0.93-0.94] | 0.96 [0.95-0.97] | 0.93 [0.92-0.94] |
| Kidney right | 0.95 [0.95-0.95] | 0.92 [0.89-0.94] | 0.95 [0.94-0.95] | 0.94 [0.93-0.96] | 0.94 [0.93-0.94] |
| Kidney left | 0.95 [0.95-0.95] | 0.91 [0.89-0.92] | 0.94 [0.93-0.95] | 0.95 [0.92-0.96] | 0.94 [0.93-0.94] |
| Gallbladder | 0.86 [0.83-0.88] | 0.73 [0.66-0.79] | 0.72 [0.66-0.78] | 0.79 [0.73-0.84] | 0.78 [0.73-0.82] |
| Esophagus | 0.64 [0.61-0.66] | 0.64 [0.59-0.68] | 0.66 [0.62-0.70] | 0.61 [0.56-0.66] | 0.26 [0.22-0.29] |
| Liver | 0.96 [0.96-0.96] | 0.93 [0.93-0.93] | 0.96 [0.95-0.96] | 0.97 [0.96-0.97] | 0.93 [0.92-0.94] |
| Stomach | 0.90 [0.89-0.91] | 0.86 [0.83-0.89] | 0.87 [0.84-0.89] | 0.88 [0.84-0.90] | 0.44 [0.37-0.50] |
| Aorta | 0.84 [0.82-0.86] | 0.84 [0.82-0.85] | 0.89 [0.87-0.91] | 0.88 [0.86-0.91] | 0.45 [0.37-0.54] |
| Inferior vena cava | 0.83 [0.81-0.84] | 0.74 [0.71-0.76] | 0.83 [0.81-0.84] | 0.86 [0.84-0.88] | 0.43 [0.38-0.48] |
| Pancreas | 0.84 [0.83-0.86] | 0.76 [0.72-0.79] | 0.79 [0.75-0.82] | 0.85 [0.82-0.88] | 0.62 [0.57-0.66] |
| Adrenal gland right | 0.57 [0.54-0.59] | 0.51 [0.47-0.55] | 0.54 [0.50-0.57] | 0.60 [0.56-0.64] | 0.30 [0.26-0.34] |
| Adrenal gland left | 0.58 [0.55-0.62] | 0.56 [0.51-0.60] | 0.53 [0.48-0.58] | 0.62 [0.56-0.67] | 0.35 [0.31-0.40] |
| Duodenum | 0.71 [0.69-0.73] | 0.56 [0.51-0.60] | 0.58 [0.54-0.62] | 0.68 [0.64-0.71] | 0.29 [0.25-0.33] |

## Dice score and 95% confidence interval (CI) on Amos CT images training and test set combined Bold values indicate the best (or tied-best) result in each row Our model kept the delineation definition from MR. In CT images, there are constraining edges visible for adrenal glands but not from MR images

| Label name | This study | Wasserthal et al | Ma et al |
| --- | --- | --- | --- |
|  |  | Totalsegmentator CT | Medsam2 |
|  | Dice CI:[95%] | Dice CI:[95%] | Dice CI:[95%] |
| Spleen | 0.90 [0.89-0.91] | 0.94 [0.93-0.94] | 0.83 [0.81-0.85] |
| Kidney right | 0.92 [0.91-0.92] | 0.94 [0.93-0.95] | 0.85 [0.84-0.86] |
| Kidney left | 0.91 [0.91-0.92] | 0.93 [0.92-0.94] | 0.85 [0.84-0.86] |
| Gallbladder | 0.75 [0.73-0.77] | 0.81 [0.79-0.83] | 0.56 [0.54-0.58] |
| Esophagus | 0.65 [0.63-0.66] | 0.79 [0.78-0.81] | 0.22 [0.19-0.24] |
| Liver | 0.93 [0.92-0.93] | 0.96 [0.96-0.96] | 0.75 [0.72-0.78] |
| Stomach | 0.85 [0.83-0.86] | 0.89 [0.88-0.91] | 0.40 [0.37-0.42] |
| Aorta | 0.85 [0.85-0.85] | 0.92 [0.91-0.92] | 0.22 [0.19-0.25] |
| Inferior vena cava | 0.79 [0.79-0.80] | 0.83 [0.82-0.84] | 0.20 [0.18-0.23] |
| Pancreas | 0.73 [0.72-0.74] | 0.81 [0.79-0.82] | 0.46 [0.44-0.48] |
| Adrenal gland right | 0.49 [0.47-0.50] | 0.70 [0.68-0.71] | 0.35 [0.33-0.37] |
| Adrenal gland left | 0.54 [0.53-0.56] | 0.71 [0.69-0.73] | 0.34 [0.32-0.36] |
| Duodenum | 0.65 [0.64-0.67] | 0.69 [0.67-0.71] | 0.22 [0.20-0.24] |
| Urinary bladder | 0.73 [0.71-0.75] | 0.80 [0.78-0.82] | 0.56 [0.53-0.59] |
| Prostate | 0.45 [0.40-0.49] | 0.46 [0.42-0.51] | 0.62 [0.59-0.64] |
