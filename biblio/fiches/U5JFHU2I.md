# Exploring Artificial Intelligence in Orthopedic Surgery: A Review of Perception, Decision, and Execution Systems.

**Auteurs** : Li D, Liu W, Niloy MMH, Yi Z, Xu L.
**Année** : 2026
**DOI** : 10.3390/s26092591

## Résumé

Artificial intelligence (AI) has become an indispensable tool in orthopedic surgery. It provides new methods to increase surgical precision, improve patient safety, and support personalized treatment plans. This review presents a comprehensive analysis of AI-assisted orthopedic surgery across three core domains. Based on 89 recent studies, this review organizes findings around a perception-decision-execution framework. It groups diverse AI applications into certain categories while highlighting the mutuality across domains. Perception systems have progressed from basic CNN-based segmentation models to advanced transformer architectures. They support multi-modal data fusion and enable uncertainty quantification. Decision systems have moved far beyond rigid rule-based methods and evolve into data-driven models that support surgical planning, accurate risk prediction and continuous outcome optimization. And execution systems have advanced from passive navigation tools to active robotic as

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Comparison of key characteristics across 89 studies.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kuok et al. [3] | Perception | Spine | CT | 5 cases | k-fold Cross-Validation | Dice similarity coefficient | Retrospective Study |
| Zhang et al. [13] | Perception | Knee cartilage | Multimodal MRI | 209 patients + 57 healthy volunteers | Internal Validation | Accuracy, Precision, Recall, F-measure | Retrospective Study |
| NISHIO et al. [14] | Perception, Execution | Knee | Video | 6 videos with 218 clips | Internal Validation | Accuracy | Preclinical Study |
| Kadkhodamohammadi et al. [15] | Perception | Knee | Video | 18 videos | 6-fold cross-validation | F1-score, phase transition error | Retrospective Study |
| Sun et al. [16] | Perception | Cervical spine | Vibration, sound | 68,000 sets | Internal Validation | Accuracy | Preclinical Study |
| Dunnhofer et al. [17] | Perception | Knee cartilage | Ultrasound | 6 volunteers 18,278 annotated 2D slices | k-fold Cross-Validation | Dice Similarity Coefficient | Preclinical Study |
|  |  |  |  | 10 cases with 2 CT scans each + |  |  |  |
|  |  |  |  | 112 left and 113 right femur |  |  |  |
| Liu et al. [18] | Perception | Femoral neck femur | CT | images (Pelvic Reference Data: https://doi.org/10.7937/TCIA. | Random Hold-out | Dice coefficient; length error; displacement error | Retrospective Study |
|  |  |  |  | 2019.WOSKQ5OO, accessed on |  |  |  |
|  |  |  |  | 19 April 2026) |  |  |  |
| Liu et al. [19] | Perception, Decision | Knee femur tibia patella fibula | CT | 538 patients 241,566 CT images | Random Hold-out | Dice coefficient; IOU; ASD; HD; bone resection thickness accuracy; alignment accuracy | Prospective Clinical Trial |
| Lu et al. [20] | Perception | Spine | CT | 116 patients (VerSe2020: https://doi.org/10.17605/OSF. IO/T98FZ, accessed on 19 April 2026) | Random Hold-out | Mean Localization Error; Dice classification accuracy Similarity Coefficient; IoU; Pixel Accuracy; Mean Surface Distance; Hausdorff Distance; | Retrospective Study |
| Jonmohamadi et al. [21] | Perception | Knee femur ACL tibia meniscus | Arthroscopy video | 3868 images | k-fold Cross-Validation | Dice similarity coefficient | Preclinical Study |
| Ali et al. [22] | Perception | Knee bone ACL meniscus | Arthroscopic multispectral video | not reported | k-fold Cross-Validation | Dice similarity coefficient | Preclinical Study |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ali and Pandey [23] | Perception | Knee multiple structures | Arthroscopy video | 4128 phantom stereo frames + 12,695 cadaver stereo frames | Random Hold-out | L1 error; L1 gradient error; coefficient DSSIM; SSIM; Dice similarity | Preclinical Study |
| Antico et al. [24] | Perception | Knee femoral cartilage | Ultrasound | 18,278 images | k-fold Cross-Validation | Dice similarity coefficient; boundary uncertainty Dice similarity coefficient with | Preclinical Study |
|  |  |  |  |  |  | Area Under ROC Curve; Dice |  |
| Antico et al. [25] | Perception | Knee femoral cartilage | 4D ultrasound | 16,973 2D images | Random Hold-out | Similarity Coefficient; Dice Similarity Coefficient with | Preclinical Study |
|  |  |  |  |  |  | Boundary Uncertainty |  |
|  |  |  |  |  | 3k-fold | Dice-Sorensen coefficient; |  |
| Lee et al. [26] | Perception | Spine neural tissue | Endoscopic video | 2942 frames | Cross-Validation and Random | Jaccard index; precision; recall; average precision; processing | Retrospective Study |
|  |  |  |  |  | Hold-out | time |  |
|  |  |  |  | 16 videos (EndoVis 2018 |  |  |  |
|  |  |  |  | (Robotic Scene Segmentation |  |  |  |
| Li et al. [27] | Perception | Kidney laparoscopy | RGB video | Challenge): https://endovissub2018-roboticscenesegmentation. | Internal Validation | CP, CR, CF1, OP, OR, OF1, HL, mAP | Preclinical Study |
|  |  |  |  | grand-challenge.org/Data/, |  |  |  |
|  |  |  |  | accessed on 19 April 2026) |  |  |  |
| Zou et al. [28] | Perception | Nasopharynx | CT and MR | 99 patients | Random Hold-out | precision; recall; target registration error | Retrospective Study |
| Yu et al. [29] | Perception | Spine | CT and X-ray | 12 CT scans with X-ray pairs | not reported | mAP; matching accuracy | Retrospective Study |
|  |  |  |  | 18 patients + 4 cadavers (2016 |  |  |  |
|  |  |  |  | Low Dose CT Grand Challenge: |  | detection rate; detection error; |  |
| Fan et al. [30] | Perception | Spine | C-arm CBCT | https: | Random Hold-out | F1 score; intensity difference; | Preclinical Study |
|  |  |  |  | //doi.org/10.21227/4yqw-2364, |  | fiducial registration error |  |
|  |  |  |  | accessed on 19 April 2026) |  |  |  |
| Broessner et al. [31] | Perception | Scaphoid | US and CT | 2376 US images+ 105 scaphoid models | Random Hold-out | MAE(R); MAE(t); SDE | Preclinical Study |
| Banach et al. [32] | Perception | Knee | Arthroscopy video | 8 sequences + 1 cadaveric knee | Random Hold-out | Position Error; Rotation Error | Preclinical Study |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | 110 CT/X-ray pairs + 30 CT |  |  |  |
|  |  |  |  | scans for chest + 6 patients for |  |  |  |
| Geng et al. [33] | Perception | Chest and pelvis | CT and X-ray | pelvis (Regi2D3D public dataset: https://github.com/rg2/Regi2 | Random Hold-out | TRE; GFR; translation error; rotation error | Retrospective Study |
|  |  |  |  | D3D-IPCAI2020, accessed on 19 |  |  |  |
|  |  |  |  | April 2026) |  |  |  |
| Shrestha et al. [34] | Perception | Pelvis | CT and X-ray | 6 CT scans + 48,600 simulated X-rays + real X-rays from 6 specimens | Random Hold-out | proj. mTRE; mTRE; GFR | Retrospective Study |
|  |  |  |  | 52 CT scans (Verse: https: |  |  |  |
| Chen and Zhang [35] | Perception | Spine | CT and X-ray (simulated) | //github.com/anjany/verse, accessed on 19 April 2026) + | Random Hold-out | mTRE; pose error; registration time | Retrospective Study |
|  |  |  |  | 1000 simulated X-rays |  |  |  |
| Ju et al. [36] | Perception | Pelvis | CT and X-ray | 5000 synthetic DRRs per patient+ 10 real X-rays | Random Hold-out | MAE; SSIM; NCC | Preclinical Study |
|  |  |  |  | 2.25M simulated X-ray images |  |  |  |
|  |  |  |  | (HaN-Seg: https: |  |  |  |
|  |  |  |  | //doi.org/10.1002/mp.16197, |  |  |  |
|  |  |  |  | accessed on 19 April 2026), |  |  |  |
|  |  |  |  | (BIMCV-COVID19+: |  |  |  |
| Ye et al. [37] | Perception | Head, chest, pelvis | CT and X-ray | https://github.com/BIMCV-CSUSP/BIMCV-COVID-19, | Random Hold-out | MAE; mTRE; GFR | Retrospective Study |
|  |  |  |  | accessed on 19 April 2026), |  |  |  |
|  |  |  |  | (CTPelvic1k: |  |  |  |
|  |  |  |  | https://github.com/ |  |  |  |
|  |  |  |  | MIRACLE-Center/CTPelvic1K, |  |  |  |
|  |  |  |  | accessed on 19 April 2026) |  |  |  |
|  |  |  |  | 20,000 synthetic X-rays from |  |  |  |
|  |  |  |  | 20 CTs (NIH Cancer Imaging |  |  |  |
| Bier et al. [38] | Perception | Pelvis | X-ray (synthetic and real) | Archive: https://www. cancerimagingarchive.net/, | Random Hold-out | mean prediction error; detection accuracy | Retrospective Study |
|  |  |  |  | accessed on 19 April 2026); real |  |  |  |
|  |  |  |  | X-rays from 5 cadavers |  |  |  |
| Wang et al. [39] | Perception | Bone | Fluoroscopy | not reported | Internal Validation | Location accuracy error, Time | Preclinical Study |
| Lee et al. [40] | Perception, Decision | Hip | RGB video | 51 participants | Random Hold-out | prediction accuracy; Gini importance; chi-square test | Retrospective Study |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Viviers et al. [41] | Perception | Spine screw | X-ray and optical | 18,600 images from LINEMOD (LINEMOD dataset: https: //bop.felk.cvut.cz/datasets/, custom X-ray accessed on 19 April 2026) and | Random Hold-out | ADD-S; ADD; 3D translation time error; 3D angle error; 2D reprojection error; inference | Preclinical Study |
| Cho et al. [42] | Perception | Spine | Endoscopic video | 2310 frames from 9 videos | Random Hold-out cross-validation and 9-fold | recall; precision; F1-score | Preclinical Study |
| Cui et al. [43] | Perception | Spine | Endoscopic video | 65 patients with 22,454 images | Internal Validation | Sensitivity, Specificity, Accuracy | Retrospective Study |
| Ji et al. [44] | Perception, Execution | Spine lamina | Electrical impedance | 246 groups 177,912 force-impedance pairs | Random Hold-out | Accuracy; time delay; Pearson correlation coefficient breakthrough distance; | Preclinical Study |
|  |  |  |  | 1850 frames (Endovis dataset: |  |  |  |
|  |  |  |  | https://endovissub2017- |  |  |  |
| Sun et al. [45] | Perception | Surgical instrument | Laparoscopic video | roboticinstrumentsegmentation. grand-challenge.org/, accessed | Random Hold-out | PCK; classification accuracy; inference speed | Retrospective Study |
|  |  |  |  | on 19 April 2026); 5000 training, |  |  |  |
|  |  |  |  | 3000 test frames |  |  |  |
| Lan et al. [46] | Perception | Knee joint | A-mode ultrasound | 1017 samples | not reported | classification accuracy; tracking precision (mm) | Preclinical Study |
|  |  |  | Acoustic |  |  |  |  |
| Sun et al. [47] | Perception | Bone | microphone | 5120 samples | Random Hold-out | Accuracy | Preclinical Study |
|  |  |  | signal |  |  |  |  |
|  |  |  |  | 8 video sequences (EndoVis2017 |  |  |  |
|  |  |  |  | dataset: |  |  |  |
| Zhang et al. [48] | Perception | Surgical instrument | Endoscopic video | https://endovissub2017-roboticinstrumentsegmentation. | Random Hold-out | IoU | Retrospective Study |
|  |  |  |  | grand-challenge.org/, accessed |  |  |  |
|  |  |  |  | on 19 April 2026) |  |  |  |
| Nwoye and Padoy [49] | Perception | Surgical tool | Laparoscopic video | 20 videos+ 35,000 frames+ 65,000 boxes (CholecTrack20 dataset: https://doi.org/10.730 April 2026) 3/syn53182642, accessed on 19 | Random Hold-out | HOTA; DetA; LocA; AssA; FPS MOTA; MOTP; MT; PT; ML; IDF1; IDSW; Frag; #Dets; #IDs; | Retrospective Study |
|  |  |  |  |  |  | https://doi.org/10.3390/s26092591 |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | LND (1147 training, 373 test w/o |  |  |  |
|  |  |  |  | occlusion, 238 test w/ |  |  |  |
| Xu et al. [50] | Perception | Surgical instrument | Endoscopic video | occlusion)+MBF (1069 training, 209 test w/o occlusion, 387 test w/ occlusion) (SurgRIPE dataset: https://www.synapse.org/ | Random Hold-out | ADD; Avg Acc; Translation Error; Rotation Error; proj2d; mmd5 | Retrospective Study |
|  |  |  |  | Synapse:syn51471789, accessed |  |  |  |
|  |  |  |  | on 19 April 2026) |  |  |  |
|  |  |  |  | 8 video (SurgRIPE dataset: |  |  |  |
|  |  |  |  | https://www.synapse.org/ |  |  |  |
| Yang et al. [51] | Perception | Surgical instrument | Endoscopic video | Synapse:syn51471789, accessed on 19 April 2026) + 590 images (kvasir-instrument dataset: https://doi.org/10.17605/OSF. | Random Hold-out and 5-fold cross-validation | Dice; mIOU | Retrospective Study |
|  |  |  |  | IO/KP6MY, accessed on 19 |  |  |  |
|  |  |  |  | April 2026) |  |  |  |
|  |  |  |  | 8k images (CholecSeg8k: |  |  |  |
| Sheng et al. [52] | Perception | Surgical instruments | Endoscopic video | https://www.kaggle.com/ accessed on 19 April 2026) + 20 datasets/newslab/cholecseg8k, | Internal Validation | mIoU | Preclinical Study |
|  |  |  |  | videos |  |  |  |
| Jonmohamadi et al. [53] | Perception | Knee femur ACL meniscus | Arthroscopy video | 38,500 frames + 12,000 frames | External Validation | ATE; photometric reprojection loss | Preclinical Study |
|  |  |  |  |  |  | Lateral deviation; axial angle; |  |
| Abel et al. [54] | Perception, Decision | Lumbar spine | MRI and CT | 16 patients | Internal Validation | sagittal angle; vertebral length; vertebral width; pedicle | Retrospective Study |
|  |  |  |  |  |  | height; pedicle width; ICC |  |
| LewandrowskI et al. [55] Perception | Lumbar spine | MRI | 3560 patients 17,800 disc levels | Random Hold-out | accuracy; sensitivity; specificity | Retrospective Study |
| Fang and Wang [56] | Perception | Knee cartilage | MRI | 1043 images | Random Hold-out | SEN; SPE; PPV; NPV; FPR; BER; ACC; AUC | Retrospective Study |
| Ghauri et al. [57] | Perception | Spine | X-ray | 967 images | Random Hold-out | accuracy; precision; recall; sensitivity; specificity; AUC | Retrospective Study |
| Xiang et al. [58] | Perception | Lumbar spine nucleus pulposus | Ultrasound | 152 samples | Random Hold-out | Accuracy; Precision; Sensitivity; Specificity; F1 | Retrospective Study |
|  |  |  |  |  |  | https://doi.org/10.3390/s26092591 |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Random Hold-out; |  |  |
| Voinea et al. [59] | Perception | Knee joint | MRI | 1556 exams | Monte-Carlo cross-validation; k-fold | accuracy; precision; recall; F1; ROC-AUC | Retrospective Study |
|  |  |  |  |  | Cross-Validation |  |  |
| Burlison et al. [60] | Perception | Knee femur | CT and MR | 424 image pairs | External Validation | Pearson's r; CCC; R-squared; bias; limits of agreement | Retrospective Study |
| Antico et al. [61] | Perception | Knee femoral cartilage | Ultrasound | 38,656 images | 5k-fold Cross-Validation | accuracy; specificity; agreement; Cohen's kappa sensitivity; AUC; percent | Preclinical Study |
|  |  |  |  | 1024 image pairs (Flickr1024: |  |  |  |
|  |  |  |  | https://yingqianwang.github. |  |  |  |
|  |  |  |  | io/Flickr1024, accessed on 19 |  |  |  |
|  |  |  | Stereo | April 2026) for training; 150 test |  |  |  |
| Wang et al. [62] | Perception | Surgical scene | endoscopic | pairs (EndoVis2017 dataset: | External Validation PSNR; SSIM | Preclinical Study |
|  |  |  | video | https://endovissub2017- |  |  |  |
|  |  |  |  | roboticinstrumentsegmentation. |  |  |  |
|  |  |  |  | grand-challenge.org/, accessed |  |  |  |
|  |  |  |  | on 19 April 2026) |  |  |  |
|  |  |  | Diffuse |  |  |  |  |
| Gunaratne et al. [63] | Perception | Human joint tissue | reflectance and auto-fluorescence | 3060 spectra | k-fold Cross-Validation | accuracy | Preclinical Study |
|  |  |  | spectroscopy |  |  |  |  |
| Gunaratne et al. [64] | Perception | Knee joint | Diffuse reflectance spectroscopy | 3043 spectra | k-fold Cross-Validation | accuracy; sensitivity | Preclinical Study |
| Cui et al. [65] | Perception | Spine nerve and dura mater | Endoscopic video | 4829 images | Random Hold-out | accuracy; sensitivity; specificity | Retrospective Study |
| Yao et al. [66] | Perception | Spine spinal cord nucleus pulposus nerve root adipose tissue | Ultrasound | 758 samples | Random Hold-out | Accuracy; Precision; Latency Sensitivity; Specificity; F1; | Preclinical Study |
| Hopkins et al. [67] | Decision | Spine | Clinical data | 4046 patients | k-fold Cross-Validation | AUC; sensitivity; specificity; PPV; NPV | Retrospective Study |
|  |  |  |  |  |  | https://doi.org/10.3390/s26092591 |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Zhang et al. [4] | Decision | Spine | CT | not reported | Internal Validation | not reported | Preclinical Study |
| Cui [68] | Decision | Spine | not reported | not reported | Internal Validation | Accuracy, time, success rate, adaptability score | Preclinical Study |
|  |  |  |  |  |  | Safe rate; insertion ratio; |  |
| Ao et al. [69] | Decision | Spine pedicle screw | CT, ultrasound, surface reconstruction | 5 human models+5 water phantoms+ 35 real vertebrae | External Validation | breach rate; classification; direction error; Gertzbein-Robbins | Preclinical Study |
|  |  |  |  |  |  | trajectory distance |  |
| Fauser et al. [70] | Decision | Temporal bone | CT | 24 patients | 2k-fold Cross-Validation | Dice coefficient; sensitivity; planning success rate | Retrospective Study |
| Siemionow et al. [71] | Decision | Lumbar spine pedicle | CT | 20 patients | not reported | Zidichavsky Score; Ravi Grade; Gertzbein Grade | Retrospective Study |
| Wang et al. [72] | Decision | Pelvis | CT | 481 annotated CT scans for training+ 12 patients for testing | External Validation | Surgical time; VAS; ECOG; screw placement accuracy | Prospective Clinical Trial |
| Campagner et al. [73] | Decision | Spine lumbar | Biomarkers and clinical data | 72 patients | External Validation accuracy; AUC; F1 score | Retrospective Study |
| Sánchez-Guillén et al. [74] Decision | Musculoskeletal system | Survey data | 651 surgeons | Internal Validation | accuracy; sensitivity; specificity; predictive values | Retrospective Study |
| Dasci et al. [75] | Decision | Hip | ChatGPT-4o and Google Search | 40 FAQs | not reported | response accuracy score; Rothwell classification; source categorization; Cohen's kappa | Retrospective Study |
| Pasha and Flynn [76] | Decision | Spine | X-ray | 67 AIS patients | Internal Validation | silhouette value; classification accuracy; likelihood ratio | Retrospective Study |
| Karhade et al. [77] | Decision | Spine | Clinical and laboratory variables | 4304 patients | External Validation | AUC, Brier score, Calibration, Decision-curve analysis | Retrospective Study |
| Toyoda et al. [78] | Decision | Lumbar spine | Clinical and radiographic data | 331 patients | 10k-fold Cross-Validation | accuracy; sensitivity; specificity; PPV; NPV | Retrospective Study |
| Chen et al. [79] | Decision | L5-S1 lumbar disc | MRI CT X-ray clinical data | 309 patients (https://doi.org/10 .5281/zenodo.15565334, accessed on 19 April 2026) | Random Hold-out | accuracy; sensitivity; specificity; PPV; NPV; F1; AUC | Retrospective Study |
|  |  |  |  |  |  | https://doi.org/10.3390/s26092591 |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Musculoskeletal |  |  |  |  |
| Zhang et al. [80] | Decision | Knee | multibody dynamics | 343 sets | 5k-fold Cross-Validation | RMSE; Pearson correlation coefficient | Retrospective Study |
|  |  |  | simulation data |  |  |  |  |
| Ahammad et al. [81] | Decision | Spine | Sensor data | 310 cases (https://archive.ics.uci.edu/ dataset/212/vertebral-column, accessed on 19 April 2026) | Internal Validation | TP rate; accuracy; error rate; precision; recall; standard error | Retrospective Study |
| Liao et al. [82] | Decision | Spine | Clinical data | 1136 patients | Internal Validation | AUC; accuracy; RMSE | Retrospective Study |
| Cavazos et al. [83] | Decision | Knee | Clinical data | 2093 patients | Random Hold-out | AUC; accuracy; sensitivity; specificity | Retrospective Study |
| Yamada et al. [84] | Decision | Lumbosacral spine L5-S1 L5-L6 | MRI and CT | 52 patients | Internal Validation | JOA score; VAS | Retrospective Study |
| Liu et al. [85] | Decision | Pelvis | CT | 40 public CT + 10 patients (PelvisAtlas dataset: https://github.com/I-STAR/ 2026) PelvisAtlas, accessed on 19 April | Internal Validation | Reconstruction error, Force Non-parametric test prediction error, Modeling time, Pearson correlation, | Retrospective Study |
|  |  |  |  |  |  | 3D RMS, IoU, Chamfer |  |
| Thibeault et al. [86] | Decision | Spine | X-ray & 3D model | 816 samples | random hold-out | distance, Cobb angle difference, lordosis angle | Retrospective Study |
|  |  |  |  |  |  | difference |  |
| Kim et al. [87] | Decision | Elbow joint | IMU sensor | 180 measurements | Internal Validation | Precision, Recall, F1-Score, classification accuracy | Retrospective Study |
| Nonnenmacher et al. [88] Decision | Hip | Clinical data | 235 patients | Internal Validation | AIC, p-value | Retrospective Study |
| Subramanian et al. [89] | Decision | Spine | Text | not reported | not reported | not reported | Simulated Deployment |
| Elmakias and Dabran [90] Decision | Neck, wrist | VR sensor | 176 recordings | Internal Validation | Accuracy | Preclinical Study |
| Shen [91] | Execution | Knee joint | CT | not reported | not reported | not reported | Preclinical Study |
| Torun and Öztürk [92] | Execution | Bone | Closed-loop sensor signals | 90 holes | 5-fold cross-validation | Overall accuracy, time Breakthrough accuracy, CPU | Preclinical Study |

## Cont.

| Authors | Tasks | Anatomy | Modality | Dataset Size | Validation Type | Evaluation Metrics | Clinical Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Li et al. [93] | Execution | Spine | Force, position, optical | 1054 samples | Internal Validation | Accuracy, recognition rate | Preclinical Study |
|  |  |  |  |  |  | Positional error, rotational |  |
| Andress et al. [94] | Execution | Femur/Pelvis | Fluoroscopy, RGB, AR | not reported | Internal Validation | error, RMSE, precision, distance error, procedure time, | Preclinical Study |
|  |  |  |  |  |  | X-ray count |  |
| Pan et al. [95] | Execution | Spine | Fluoroscopy, optical tracking, depth camera | 20 patients + 10 dogs | Prospective Validation | Positioning error, Orientation error, Fluoroscopy times, VAS, ODI | Prospective Clinical Trial |
|  |  |  | AR, optical |  |  |  |  |
| Huang et al. [96] | Execution | Spine | tracking, | 20 dogs | Internal Validation | Distance error, Angle error | Preclinical Study |
|  |  |  | fluoroscopy |  |  |  |  |
| Pan et al. [97] | Execution | Pelvis | Wearable sensors | 20 subjects + 1000 action sets | 5-fold cross-validation | Accuracy, Precision, Recall, F1-Score | Preclinical Study |
| Pan et al. [98] | Execution | Pelvis | Wearable sensors | 6804 action segments | 5-fold cross-validation | Accuracy, F1-Score | Preclinical Study |
| Chen et al. [99] | Execution | Surgical robotics | Kinematic data | 8 subjects+ 103 trials | LOUO cross-validation | Accuracy, RMSE, MAE, MAPE, execution time | Preclinical Study |
