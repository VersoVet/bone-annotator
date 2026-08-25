# Segment Anything Model 2: An Application to 2D and 3D Medical Images.

**Auteurs** : Haoyu Dong, Hanxue Gu, Yaqian Chen, Jichen Yang, Yuwen Chen, Maciej A Mazurowski
**Année** : 2026
**DOI** : 10.1109/tbme.2026.3653267

## Résumé

Segment Anything Model (SAM) has gained significant attention because of its ability to segment a variety of objects in images upon providing a prompt. Recently developed SAM 2 has extended this ability to video segmentation, and by substituting the third spatial dimension in 3D images for the time dimension in videos, it opens an opportunity to apply SAM 2 to 3D medical images. In this paper, we extensively evaluate SAM 2's ability to segment both 2D and 3D medical images using 80 prompt strategies across 21 medical imaging datasets, including 2D modalities (X-ray and ultrasound), 3D modalities (magnetic resonance imaging, computed tomography, and positron emission tomography), and surgical videos. We find that in the 2D setting, SAM 2 performs similarly to SAM, while in the 3D setting we observe that: (1) selecting the first mask is more effective than choosing the one with the highest confidence, (2) prompting the slice with the largest object appears is the most cost-effective stra

## Méthodologie

{'study_design': 'Évaluation comparative de SAM 2 selon deux configurations: segmentation 2D single-frame (prompts fournis sur chaque slice) et segmentation 3D multi-frame (prompts fournis sur une ou plusieurs slices sélectionnées dans le volume)', 'intervention': None, 'control': None, 'primary_outcomes': ['Performance de segmentation mesurée par Intersection over Union (IoU)'], 'secondary_outcomes': [], 'statistical_methods': ['IoU calculé uniquement sur les slices non vides pour permettre une comparaison entre segmentation 2D et 3D'], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [], 'qualitative_findings': ["La section RÉSULTATS fournie ne contient aucune donnée quantitative ou qualitative détaillée : elle indique uniquement qu'une investigation de l'impact de chaque composant a été menée pour la segmentation 3D multi-frame, avec un renvoi vers la Figure 5 pour la performance moyenne de toutes les combinaisons de modes et vers l'Appendice pour la performance par jeu de données."], 'main_findings': ["Le texte source fourni ne contient pas les valeurs chiffrées ni les résultats détaillés — ceux-ci sont présentés dans la Figure 5 et l'Appendice, non inclus dans cette section textuelle."]}

## Conclusions

SAM 2 exhibits similar performance to that of SAM under single-frame 2D segmentation. For the multi-mask outputs, selecting the first channel is better than selecting the channel with the largest confidence during propagation when having point prompts. For the initial frame selection, selecting multiple slices is better than selecting one slice with the cost of providing more prompts, and selecting the center slice tends to be the most cost-effective choice. For prompt selection, box prompts are more effective than point prompts with a higher cost of human effort. Bidirectional propagation, starting from the annotated slice, is a more effective strategy when compared to propagating from beginning to end. Interactive segmentation is useful only when the new slice is annotated manually, i.e., providing the ground truth mask, but not through prompts. The best average 3D performance of SAM 2 when providing one point prompt, one box prompt, and the ground truth mask to the entire volume is 0.3778, 0.5222, and 0.6198 IoU respectively.

## Correction-based Interactive prompting for Multi-Frame Segmentation Input: Slices S = {s 1 , s 2 , . . . , s n }, Sub-volume 1: S backward , Sub-volume 2: S forward , Initial Prompts Queue: P init = {}, SAM 2' Video Predictor: Predictor, Number of Interactive Loops: K Output: Final Predictions Pred final Step 1. Initialize Pred final = {}; P init ← Frame Prompt Gen(S, Fmode, Pmode); P loop ← P init ; Step 2. for loop = 1 to K do pred sinit = Predictor(P loop ); for i = s init to 1 do Pred si ← Predictor(s i ); Save Pred smin in Pred final ; Identify the slice s min in S backward with the lowest IoU (within 16 slices of annotated slices); p new ← GeneratePrompt(s min ); P loop ← P new ; Save Pred smin in Pred final ; Identify the slice s min in S forward with the lowest IoU (within 16 slices of annotated slices); p new ← GeneratePrompt(s min ); P loop ← P new ;

| Step 3. Reinitialize Predictor; |
| --- |
| P return Pred final ; |

## Reinitialization-based Interactive Prompting for Multi-Frame Segmentation Input: Slices S = {s 1 , s 2 , . . . , s n }, Initial Prompts Queue: P init = {}, Step 2. P red sinit = Predictor(P init ); Step 3 for i = s init to 1 do pred si ← Predictor(s i , P init ); Save pred si in Pred Save pred si in Pred final ; Step 7. Identify the slice s max with the largest error in Pred final ; Step 8. FN max ← FindMaxFN(s max ) # find largest false negative region; Step 9. p new ← GeneratePrompt(FN max ); Step 10. Add p new to P init ;

| SAM 2' Video Predictor: Predictor, |
| --- |
| Number of Interactive Loops: K, |
| Frame mode and Prompt mode: Fmode, Pmode |
| Output: Final Predictions Pred final |
| Initialize Pred final = {} ; |
| Initialize loop = 0 ; |
| P init ← Frame Prompt Gen(S, Fmode, Pmode) |
| for loop = 1 to K do |
| Step 1. Reinitialize Predictor; |
| return Pred final ; |
| on the new prompts. |

## 2D datasets evaluated in this paper: "num. masks" refers to the number of images with non-zero masks.

| Abbreviated dataset name | Full dataset name and citation | Modality | Num. classes | Object(s) of interest | Num. masks |
| --- | --- | --- | --- | --- | --- |
| Xray-Chest | Montgomery County and Shenzhen Chest X-ray Datasets [16] | X-ray | 1 | Chest | 704 |
| Xray-Hip | X-ray Images of the Hip Joints [13] | X-ray | 2 | Ilium, Femur | 140 |
| US-Breast | Dataset of Breast Ultrasound Images [1] | Ultrasound | 1 | Breast | 630 |
| US-Kidney | CT2US for Kidney Segmentation [35] | Ultrasound | 1 | Kidney | 4,586 |
| US-Muscle | Transverse Musculoskeletal Ultrasound Image Segmentations [23] | Ultrasound | 1 | Muscle | 4,044 |
| US-Ovarian-Tumor | Multi-Modality Ovarian Tumor Ultrasound (MMOTU) [40] | Ultrasound | 1 | Ovarian tumor | 1,469 |
