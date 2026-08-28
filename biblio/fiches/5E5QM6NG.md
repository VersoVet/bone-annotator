# Learning to detect anatomical landmarks of the pelvis in X-rays from arbitrary views.

**Auteurs** : Bastian Bier, Florian Goldmann, Jan-Nico Zaech, Javad Fotouhi, Rachel Hegeman, Robert Grupp, Mehran Armand, Greg Osgood, Nassir Navab, Andreas Maier, Mathias Unberath
**Année** : 2019
**DOI** : 10.1007/s11548-019-01975-5

## Résumé

Minimally invasive alternatives are now available for many complex surgeries. These approaches are enabled by the increasing availability of intra-operative image guidance. Yet, fluoroscopic X-rays suffer from projective transformation and thus cannot provide direct views onto anatomy. Surgeons could highly benefit from additional information, such as the anatomical landmark locations in the projections, to support intra-operative decision making. However, detecting landmarks is challenging since the viewing direction changes substantially between views leading to varying appearance of the same landmark. Therefore, and to the best of our knowledge, view-independent anatomical landmark detection has not been investigated yet.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Table 1

| Individual landmark belief and error | # | Average belief | Average error (pixel) | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | 0.79 | 7.60 | 9.42 | 5.35 | 7.13 | 7.89 |
| 2 |  | 0.84 | 6.68 | 5.66 | 7.67 | 6.63 | 6.05 |
| 3 |  | 0.83 | 6.86 | 9.13 | 7.81 | 5.07 | 5.26 |
| 4 |  | 0.87 | 7.69 | 8.79 | 10.2 | 7.11 | 4.70 |
| 5 |  | 0.85 | 7.53 | 8.11 | 8.47 | 6.63 | 6.62 |
| 6 |  | 0.82 | 5.63 | 4.72 | 5.21 | 5.97 | 6.35 |
| 7 |  | 0.78 | 7.90 | 7.96 | 7.48 | 8.29 | 7.99 |
| 8 |  | 0.77 | 10.1 | 5.87 | 12.1 | 7.70 | 15.3 |
| 9 |  | 0.90 | 5.26 | 5.15 | 5.08 | 5.55 | 5.07 |
| 10 |  | 0.88 | 7.19 | 7.60 | 6.90 | 5.80 | 8.41 |
| 11 |  | 0.89 | 6.43 | 5.77 | 5.99 | 6.86 | 6.83 |
| 12 |  | 0.91 | 7.78 | 8.96 | 7.23 | 5.71 | 8.55 |
| 13 |  | 0.92 | 4.47 | 5.64 | 4.10 | 4.67 | 3.24 |
| 14 |  | 0.90 | 5.64 | 3.70 | 7.00 | 5.24 | 6.18 |
| 15 |  | 0.85 | 9.04 | 8.77 | 9.54 | 7.75 | 10.3 |
| 16 |  | 0.82 | 7.23 | 6.55 | 6.95 | 7.26 | 8.18 |
| 17 |  | 0.81 | 19.9 | 20.0 | 24.2 | 15.2 | 21.1 |
| 18 |  | 0.80 | 15.3 | 11.2 | 16.6 | 14.5 | 19.3 |
| 19 |  | 0.74 | 9.56 | 10.4 | 10.4 | 9.80 | 7.09 |
| 20 |  | 0.77 | 8.59 | 5.78 | 12.9 | 6.83 | 8.91 |
| 21 |  | 0.51 | 9.40 | 14.3 | 6.86 | 13.9 | 8.51 |
| 22 |  | 0.44 | 13.7 | 9.73 | 25.0 | 10.1 | 16.2 |
| 23 |  | 0.51 | 26.0 | 24.2 | 17.6 | 39.3 | 29.8 |
| Average |  | 9.10 ± 7.38 |  |  |  |  |  |

## Quantitative evaluation for the detection results on the X-ray images of the cadaver specimens Reprojection Errors (RPE) given in pixels. ref RPE is the error of the reference pose estimated from the metallic beads in order to project the 3D labels into the 2D X-ray images. Landmark RPE is the RPE of the metallic markers, using poses estimated with automatic anatomical landmark detections. Landmark Error is the distance of the detections to the ground truth positions. With a pixel size of 0.193 mm/px, the metric error on the detector is given in mm

|  | Sequence | ref RPE | Landmark RPE | Landmark error |
| --- | --- | --- | --- | --- |
|  | #1: specimen 1 | 2.45 | 74.31 | 120.9 (23.33 mm) |
|  | #2: specimen 1, with fracture | 5.46 | 173.6 | 97.82 (18.87 mm) |
|  | #3: specimen 1, with tool | 2.88 | 177.4 | 63.67 (12.28 mm) |
|  | #4: specimen 2 | 2.86 | 119.4 | 127.9 (24.68 mm) |
|  | #5: specimen 2 | 2.99 | 115.3 | 79.89 (15.41 mm) |
| s |  |  |  |  |
| t |  |  |  |  |
| l u s |  |  |  |  |
| e |  |  |  |  |
| r |  |  |  |  |
| n |  |  |  |  |
| o |  |  |  |  |
| i |  |  |  |  |
| t |  |  |  |  |
| c |  |  |  |  |
| e |  |  |  |  |
| t |  |  |  |  |
| e D |  |  |  |  |
| e |  |  |  |  |
| s |  |  |  |  |
| o |  |  |  |  |
| p |  |  |  |  |
| d e |  |  |  |  |
| t a m |  |  |  |  |
| i |  |  |  |  |
| t s E |  |  |  |  |
| Example 1 | Example 2 | Example 3 | Example 4 | Example 5 |

### Formule


$$C = T t=1 P p=1 ||b p t -b * t || 2 2 (1)$$

### Formule


$$0 T -w i r T i y i r T i w i r T i 0 T -x i r T i ⎛ ⎝ p 1 p 2 p 3 ⎞ ⎠ = 0.(2)$$
