# VIBESegmentator: full body MRI segmentation for the NAKO and UK Biobank.

**Auteurs** : Robert Graf, Paul Platzek, Evamaria Olga Riedel, Constanze Ramschütz, Sophie Starck, Hendrik K Möller, Matan Atad, Henry Völzke, Robin Bülow, Carsten Oliver Schmidt, Julia Rüdebusch, Matthias Jung, Marco Reisert, Jakob Weiss, Maximilian T Löffler, Fabian Bamberg, Benedikt Wiestler, Johannes C Paetzold, Daniel Rueckert, Jan Stefan Kirschke
**Année** : 2026
**DOI** : 10.1007/s00330-025-12035-9

## Résumé

To present a publicly available deep learning-based torso segmentation model that provides comprehensive voxel-wise coverage, including delineations that extend to the boundaries of anatomical compartments.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

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
