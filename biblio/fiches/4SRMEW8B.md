# Automatic annotation of hip anatomy in fluoroscopy for robust and efficient 2D/3D registration.

**Auteurs** : Robert B Grupp, Mathias Unberath, Cong Gao, Rachel A Hegeman, Ryan J Murphy, Clayton P Alexander, Yoshito Otake, Benjamin A McArthur, Mehran Armand, Russell H Taylor
**Année** : 2020
**DOI** : 10.1007/s11548-020-02162-7

## Résumé

Fluoroscopy is the standard imaging modality used to guide hip surgery and is therefore a natural sensor for computer-assisted navigation. In order to efficiently solve the complex registration problems presented during navigation, human-assisted annotations of the intraoperative image are typically required. This manual initialization interferes with the surgical workflow and diminishes any advantages gained from navigation. In this paper, we propose a method for fully automatic registration using anatomical annotations produced by a neural network.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Landmark detection errors across all trained networks for each landmark.

| Landmark | Pixels | Error | mm | False Negative Rate False Positive Rate |
| --- | --- | --- | --- | --- |
| L. FH | 1.9 ± 0.9 | 3.0 ± 1.5 | 0.02 | 0.02 |
| R. FH | 3.2 ± 1.9 | 5.0 ± 3.0 | 0.04 | 0.01 |
| L. GSN | 4.4 ± 2.0 | 6.8 ± 3.1 | 0.20 | 0.00 |
| R. GSN | 4.7 ± 2.3 | 7.3 ± 3.6 | 0.14 | 0.01 |
| L. IOF | 2.8 ± 4.0 | 4.3 ± 6.2 | 0.23 | 0.01 |
| R. IOF | 2.3 ± 3.3 | 3.5 ± 5.1 | 0.16 | 0.02 |
| L. MOF | 3.7 ± 3.2 | 5.8 ± 5.0 | 0.17 | 0.04 |
| R. MOF | 3.4 ± 1.9 | 5.2 ± 3.0 | 0.17 | 0.02 |
| L. SPS | 3.1 ± 2.4 | 4.7 ± 3.7 | 0.27 | 0.02 |
| R. SPS | 3.7 ± 2.9 | 5.8 ± 4.5 | 0.22 | 0.01 |
| L. IPS | 1.9 ± 1.6 | 3.0 ± 2.4 | 0.17 | 0.02 |
| R. IPS | 1.5 ± 1.0 | 2.3 ± 1.6 | 0.15 | 0.01 |
| L. ASIS | 9.0 ± 9.6 14.0 ± 14.9 | 0.29 | 0.01 |
| R. ASIS | 3.9 ± 3.7 | 6.0 ± 5.7 | 0.14 | 0.01 |
| All | 3.2 ± 3.4 | 5.0 ± 5.2 | 0.17 | 0.01 |

## Pelvis and femur registration errors from successful pelvis registrations using the three intraoperative approaches and broken down by cadaver specimen. Femur registrations errors are reported for all successful pelvis registrations which have sufficient visibility of a femur.

| Regi. Method | Spec. | # Success | Pelvis Errors Rot. ( • ) Trans. (mm) | # | Femur Errors Rot. ( • ) Trans. (mm) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 32 (29%) 0.1 ± 0.1 | 0.3 ± 0.2 | 13 0.4 ± 0.2 | 0.3 ± 0.3 |
| 1: Naive | 2 3 4 5 | 15 (14%) 0.1 ± 0.2 1 (4%) < 0.1 4 (8%) 0.1 ± 0.1 13 (24%) 0.1 ± 0.1 | 0.8 ± 1.9 0.2 0.4 ± 0.4 0.4 ± 0.3 | 5 0.7 ± 0.4 0 -0 -3 0.4 ± 0.2 | 0.4 ± 0.5 --0.7 ± 0.4 |
|  | 6 | 1 (4%) | 0.1 | 0.3 | 1 | 0.6 | 0.2 |
|  | All | 66 (18%) 0.1 ± 0.1 | 0.4 ± 0.9 | 22 0.4 ± 0.3 | 0.4 ± 0.3 |
|  | 1 | 99 (89%) 0.1 ± 0.1 | 0.8 ± 1.1 | 73 1.7 ± 5.2 | 0.6 ± 0.5 |
| 2: PnP Init. | 2 3 4 5 6 | 96 (92%) 0.1 ± 0.2 19 (79%) 0.2 ± 0.2 38 (79%) 0.2 ± 0.2 40 (73%) 0.1 ± 0.1 7 (29%) 0.1 ± 0.1 | 1.0 ± 1.4 1.6 ± 3.1 1.4 ± 1.8 0.7 ± 0.9 0.8 ± 1.0 | 59 1.2 ± 1.0 2 0.9, 0.8 27 1.3 ± 1.2 20 0.8 ± 0.8 2 1.3, 0.6 | 0.5 ± 0.4 0.4, 1.0 0.4 ± 0.4 0.6 ± 0.7 0.4, 0.1 |
|  | All 299 (82%) 0.1 ± 0.2 | 1.0 ± 1.5 183 1.4 ± 3.4 | 0.5 ± 0.5 |
| 3: Combined | 1 101 (91%) 0.1 ± 0.1 2 99 (95%) 0.2 ± 0.2 3 18 (75%) 0.2 ± 0.2 4 41 (85%) 0.2 ± 0.2 5 47 (85%) 0.1 ± 0.1 6 7 (29%) 0.3 ± 0.3 | 1.0 ± 1.5 1.4 ± 1.7 2.8 ± 3.4 2.1 ± 2.9 0.9 ± 1.2 3.0 ± 3.2 | 73 1.8 ± 5.2 61 1.3 ± 1.0 2 1.1, 1.1 29 1.6 ± 1.3 24 0.8 ± 0.8 3 1.0 ± 0.7 | 0.6 ± 0.5 0.7 ± 0.8 1.0, 1.3 0.6 ± 1.0 0.5 ± 0.6 0.3 ± 0.2 |
|  | All 313 (86%) 0.2 ± 0.2 | 1.4 ± 2.0 192 1.5 ± 3.3 | 0.6 ± 0.7 |

## Amount of downsampling along each 2D image dimension applied during each optimization. Next, the right femur is registered, again keeping the pelvis fixed. Both of these registrations use CMA-ES. Contrary to the previous registrations, these only search the 3D space of rotations, with the center of rotation fixed at the ipsilateral femoral head center. Regularization is applied to the total rotation magnitude using a folded normal distribution with µ = 45 • and σ = 45 • . Table S-4 lists the CMA-ES parameters. Once again, successful registrations of each object are manually verified.

| Object | Strategy | Factor |
| --- | --- | --- |
|  | DE | 32× |
| Pelvis Attempt 1 | Grid CMA-ES | 32× 8× |
|  | BOBYQA | 4× |
|  | Grid | 32× |
| Pelvis Attempt 2 | PSO BOBYQA 1 | 32× 8× |
|  | BOBYQA 2 | 4× |
| Femurs | CMA-ES | 8× |
| All Objects | BOBYQA | 4× |
| pose estimate. |  |  |

## The se(3) increments used for each grid search. • 5 • 0 • 20 20 25Table S-4 CMA-ES population size and initial σ parameters.

| Pelvis Attempt |  | 1 | 2 | Dimension 3 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 1 • 1 • 1 • | 2 | 2 10 |
| 2 7.5 Object Pop. Size | 1 | 2 | Dimension 3 4 | 5 | 6 |
| Pelvis | 100 15 • 15 • 30 • 50 50 100 |
| Femur | 100 30 • 25 • 15 • | - | - | - |
|  |  |  |  |  |  | Conv. 3x3, ReLU, Batch Norm. |
|  |  |  |  |  |  | Conv. 1x1 |
|  |  | F out x N x N |  |  |  | Sum |
| Input |  |  |  |  |  | Output |
| F in x N x N | F out x N x N | F out x N x N |  |  |  | F out x N x N |

## Operations performed during data augmentation. • , +5 • ) Shear angle from U (-2 • , +2 • ) Scale from U (0.9, 1.1) Local Corruption With probability 0.25 Number of rectangular regions from U ({1, 2, 3, 4, 5}) Region dimensions from N (d, d), d = 0.15 × image width Location uniformly sampled, rejection sampling to ensure region is within image Additive noise from N (0, 0.2m), m is the range of intensities in a region to that used when creating the training data set in "Pelvis Attempt 1." For intraoperative method 3, combing intensity features and landmarks, a single landmark is used to recover translation when computing the initial AP pose. Since any single landmark is not visible in all images, the following order of preference is used to select a landmark: L. FH, R. FH, L. IOF, R. IOF, L. IPS, R. IPS, L. MOF, R. MOF, L. SPS, R. SPS, L. GSN, R. GSN, L. ASIS, R. ASIS. For regularization, σ = 19.4 mm. During CMA-ES registration of the pelvis, 8× downsampling is used along with the parameters listed in Table S-4. For BOBYQA registration of the pelvis, 4× downsampling is used along with the BOBYQA box constraints for "Pelvis Attempt 1" in Table S-2.

| Method | Description |  |
| --- | --- | --- | --- |
| Intensity Inversion | With probability 0.5 |
| Additive Random | N (0, σ), σ ∼ U (0.005, 0.01) |
| Noise |  |  |
| Gamma Correction γ ∼ U (0.7, 1.3) |  |
| Affine Warp | Translation direction uniformly |
|  | sampled |  |
|  | Translation magnitude from |
|  | U (0, 20) pixels |  |
|  | Rotation | angle | from |
|  | U (-5 |  |

### Formule


$$min θ P ,θ LF ,θ RF ∈SE(3) λS (P (θ P , θ LF , θ RF ) , I) + (1 -λ) R (θ P , θ LF , θ RF )(1)$$

### Formule


$$P ) = 1 2σ 2 N L l=1 P p (l) 3D ; θ P -p (l) 2D 2 2(2)$$

### Formule


$$R depth (p; θ P ) =      d (p; θ P ) 2 if d (p; θ P ) ≥ 1 100 [0.7 -d (p; θ P )] 2 if d (p; θ P ) ≤ 0.7 0 otherwise(5)$$

### Formule


$$R up (p, q; θ P ) =          P (q; θ P ) row -P (p ; θ P ) row 2 if P (q; θ P ) row < P (p ; θ P ) row 0 otherwise(6)$$

### Formule


$$D (w) = 1 N C N C k=12$$

### Formule


$$M (k) (x, y; w) 2 + x,y M (k) (x, y) 2(7)$$

### Formule


$$H (w) = 1 N L N L l=1 N CC h (l) (w), h (l)(10)$$

### Formule


$$L (w) = -D (w) + 1 2 (H (w) + 1)(11)$$
