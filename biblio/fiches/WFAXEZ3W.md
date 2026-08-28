# Segment anything model 2: an application to 2D and 3D medical images

**Auteurs** : Haoyu Dong, Hanxue Gu, Yaqian Chen, Jichen Yang, Yuwen Chen, Maciej A. Mazurowski
**Année** : 2024
**DOI** : 10.1109/tbme.2026.3653267

## Résumé

Segment Anything Model (SAM) has gained significant attention because of its ability to segment various objects in images given a prompt. The recently developed SAM 2 has extended this ability to video inputs. This opens an opportunity to apply SAM to 3D images, one of the fundamental tasks in the medical imaging field. In this paper, we extensively evaluate SAM 2's ability to segment both 2D and 3D medical images by first collecting 21 medical imaging datasets, including surgical videos, common 3D modalities such as computed tomography (CT), magnetic resonance imaging (MRI), and positron emission tomography (PET) as well as 2D modalities such as X-ray and ultrasound. Two evaluation settings of SAM 2 are considered: (1) multi-frame 3D segmentation, where prompts are provided to one or multiple slice(s) selected from the volume, and (2) single-frame 2D segmentation, where prompts are provided to each slice. The former only applies to videos and 3D modalities, while the latter applies to

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

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
