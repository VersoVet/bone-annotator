# Enhancing lung segmentation in chest X-rays via SAM with anatomical priors and boundary-aware loss.

**Auteurs** : Senthinathan L, Arunthavarajah K, Tharshikan L, Rajeethan R, JacobSelvakumar P, Raveendran K, Thiruthanigesan K.
**Année** : 2026
**DOI** : 10.1038/s41598-026-57878-4

## Résumé

Accurate lung segmentation in chest X-rays is a foundational step for computer-aided diagnosis of respiratory diseases such as pneumonia, tuberculosis, and lung cancer. While the Segment Anything Model (SAM) has demonstrated remarkable zero-shot segmentation capabilities on natural images, its direct application to medical imaging remains limited due to domain shift, low contrast, and ambiguous anatomical boundaries. To address these challenges, we propose a lightweight yet effective adaptation of SAM that integrates (i) a Mask Autoencoder (MAE) as an anatomical prior to enforce global shape consistency, and (ii) a composite loss function combining Binary Cross-Entropy (BCE), Dice, and Boundary losses to jointly optimize pixel-level accuracy, region overlap, and edge fidelity. Our parameter-efficient fine-tuning strategy trains only 0.3% of SAM's parameters, specifically the mask decoder, while freezing the image and prompt encoders. Evaluated on the MedSeg Chest X-ray Lung Dataset, ou

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Hybrid loss design is critical for addressing class imbalance and edge precision. Med-SAM employs Dice + BCE, leveraging Dice for global overlap and BCE for pixel-level stability. However, residual boundary errors, common in low-contrast X-rays, necessitate explicit edge-focused terms. Literature supports Boundary loss, Hausdorff-based surrogates, and Tversky variants for penalizing FP/FN asymmetry. Our composite loss combines BCE (pixel discrimination), Dice (region overlap), and Boundary loss (edge refinement), directly targeting SAM's known weaknesses at lung-heart interfaces and costophrenic recesses.

| Segmentation: Why |
| --- |
| BCE-Dice-Boundary? |

## Comparative summary of related work on SAM adaptation for medical image segmentation challenges remain in achieving anatomical consistency and precise boundary delineation. Furthermore, studies emphasize the importance of prompt design, hybrid loss functions, and efficient handling of 2D and 3D data. Building on these insights, our work introduces a novel framework that combines PEFT-based adaptation with an Autoencoder constraint and a composite BCE-Dice-Boundary loss, specifically tailored to address domain shift, class imbalance, and edge ambiguity in lung segmentation from chest X-rays

|  |  |  |  |  |  | ACCEPTED MANUSCRIPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Limitations |  |  | Poor performance on low- | contrast and ambiguous | boundaries; no domain adap- | tation | High compute and data | requirements; lacks lightweight | deployment |  | Still prompt-dependent; | requires adapter design; lim- | ited anatomical priors | Sensitive to class imbalance; | lacks explicit boundary opti- | mization | Not SAM-based; limited to | volumetric projections; no | prompt interactivity | Addresses domain gap, | improves edge precision, | and enforces anatomical | consistency |
| Modalities | Tested |  | X-ray, CT, | MRI, US |  |  | 10 modalities | (CT, MRI, US, | Fundus, Der- | moscopy) | CT, MRI, US, | Fundus, Der- | moscopy | X-ray, CT, US, | Histology |  | CT (3D vol- | umes) |  | Chest X-ray | (lung seg- | mentation) |
| Loss | Func- | tion | N/A |  |  |  | Dice + | BCE |  |  | Dice + | BCE |  | Dice + | BCE |  | Dice / | Tver- | sky | BCE | + | Dice | + | Bound- | ary + | AE | loss |
| Adaptation Trainable Prompt | Strategy Params Type |  | Zero-shot SAM 0% Points / Boxes A R T I C L E evaluation Full fine-tuning (MedSAM) ∼636M Boxes (pre-ferred) Adapter-based PEFT (Med-∼2% (≈13M) Points / Boxes | SA) | SVD-based ∼0.4% Text + Points I N tuning (S-SAM) | Projection-Full model N/A P R E S S based UNet (IP-UNet) SAM + Autoencoder constraint ≈0.3% Boxes (lung fields) |
| Study |  |  | Mazurowski et al. | (2023) [19] |  |  | Ma et al. (2024) [8] |  |  |  | Wu et al. (2025) [20] |  |  | Paranjape et al. (2024) | [21] |  | Aung et al. (2023) [22] |  |  | Our Work |

## Dataset composition and fixed split protocol used for all experiments.

| Subset | Percentage Image-Mask Pairs | Usage |
| --- | --- | --- | --- |
| Training | 70% | 560 | Model optimization |
| Validation | 15% | 120 | Model selection and early stopping |
| Test | 15% | 120 | Final held-out evaluation |

## Final training configuration used consistently across all experiments.The Mask Autoencoder employs a symmetric encoder-decoder with 4 convolutional blocks per stage (each: 3×3 Conv, stride 1, padding 1, followed by BatchNorm and ReLU), channel dimensions [32, 64, 128, 256], input patch size 16 × 16, and latent dimension d = 128. The encoder compresses the 128 × 128 input mask to z ∈ R 128 ; the decoder mirrors this structure to reconstruct the mask. Training uses AdamW (lr = 1 × 10 -4 ), batch size 8, for 22 epochs with BCE loss. After convergence, only the encoder is frozen and reused for anatomical regularization during SAM fine-tuning.

| Parameter | Final Setting |
| --- | --- |
| SAM backbone | ViT-B |
| SAM input resolution | 1024 × 1024 |
| Image encoder | Frozen |
| Prompt encoder | Frozen |
| Trainable SAM component | Mask decoder only |
| Trainable SAM parameters | ≈1.9M (≈0.3%) |
| Optimizer | AdamW |
| Learning rate | 1 × 10 -4 |
| Batch size | 8 |
| Maximum training budget | 22 epochs |
| MAE training | 22 epochs |
| U-Net baseline training | Up to 22 epochs with early stopping |
| SAM fine-tuning | Up to 22 epochs with early stopping |
| Early stopping monitor | Validation Dice |
| Early stopping patience | 5 epochs |
| Minimum improvement threshold 1 × 10 -4 |
| Checkpoint selection | Best validation Dice |
| Final evaluation | Held-out test set, evaluated once |
| Loss weights (λ1, λ2, λ3, λ4) | (1.0, 1.0, 0.5, 0.3) |

## Consolidated ablation study under the finalized unified protocol. All results are reported from the best validation-Dice checkpoint using the same fixed dataset split, maximum 22-epoch schedule, and early-stopping criterion. Dice measures region overlap, HD95 measures boundary error where lower is better, and parameter efficiency is reported relative to the U-Net baseline.

| Method | Trainable | Dice HD95 Param. | Primary Role |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Params |  |  | Eff. |  |  |  |
| U-Net baseline | 31M | 0.823 12.4 1.0× | Conventional CNN segmenta- |
|  |  |  |  |  | tion baseline. |  |
| Vanilla SAM | 636M | 0.721 28.1 0.05× | Zero-shot | foundation-model |
|  |  |  |  |  | baseline without medical adap- |
|  |  |  |  |  | tation. |  |  |
| SAM + Bound- | 1.9M | 0.845 | 9.8 | 16.3× | Decoder-only | PEFT | with |
| ary Loss | (≈0.3%) |  |  |  | boundary-aware refinement. |
| AE-PEFT | 1.9M | 0.873 7.2 16.3× | Decoder-only PEFT with |
| (Ours) | (≈0.3%) |  |  |  | boundary-aware | loss |
|  |  |  |  |  | and | Autoencoder-based |
|  |  |  |  |  | anatomical regularization. |

## Comparison with representative SAM-based and parameter-efficient medical segmentation methods. Dice is reported in percentage form; 87.3% corresponds to 0.873 in Table4.

| Method | Dice (%) Trainable Params (%) Inference (ms) |
| --- | --- | --- | --- |
| SAM | 72.1 | 100 | 200 |
| MedSAM | 81.2 | 100 | 250 |
| S-SAM | 84.6 | 0.4 | 85 |
| SAM-PARSER | 85.1 | 0.4 | 92 |
| Ours, AE-PEFT | 87.3 | 0.3 | 78 |

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$

### Formule


$$L total = λ 1 L BCE + λ 2 L Dice + λ 3 L Boundary + λ 4 L AE(1)$$

### Formule


$$L AE = M -MAE dec (MAE enc ( M )) 2 2 (2)$$

### Formule


$$HD95 = percentile 95 (D)(3)$$

### Formule


$$ACCEPTED MANUSCRIPT A R T I C L E I N P R E S S$$
