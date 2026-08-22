# 2D–3D reconstruction of distal forearm bone from actual X-ray images of the wrist using convolutional neural networks

**Auteurs** : Ryoya Shiode, Kabashima Mototaka, Yuta Hiasa, Kunihiro Oka, Tsuyoshi Murase, Yoshinobu Sato, Yoshito Otake
**Année** : 2021
**DOI** : 10.1038/s41598-021-94634-2

## Résumé

AbstractThe purpose of the study was to develop a deep learning network for estimating and constructing highly accurate 3D bone models directly from actual X-ray images and to verify its accuracy. The data used were 173 computed tomography (CT) images and 105 actual X-ray images of a healthy wrist joint. To compensate for the small size of the dataset, digitally reconstructed radiography (DRR) images generated from CT were used as training data instead of actual X-ray images. The DRR-like images were generated from actual X-ray images in the test and adapted to the network, and high-accuracy estimation of a 3D bone model from a small data set was possible. The 3D shape of the radius and ulna were estimated from actual X-ray images with accuracies of 1.05 ± 0.36 and 1.45 ± 0.41 mm, respectively.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

### Formule


$$L step1 = L label D E y noised , y 1 E y noised 1 , L step2 = L label D(P(x)), y + 1 |P(x)| 1 , L step3 = L label D(P(x)), y + 1 |P(x)| 1 + 2 E y -E(D(P(x))) 2 , ASD = 1 |S A | + |S B |   � p A ∈S A min p B ∈S B d � p A , p B � + � p B ∈S B min p A ∈S A d � p A , p B �  $$
