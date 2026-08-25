# X2P-Net: Context-Aware 2D/3D Vertebra Localization.

**Auteurs** : Tao R, Ye K, Zhang W, Sun W, Yu D, Hang D, Zheng G.
**Année** : 2026
**DOI** : 10.3390/bioengineering13020178

## Résumé

In the context of minimally invasive spine surgery, accurately estimating the 3D coordinates of the vertebrae from intraoperative 2D X-ray images is crucial for aligning preoperative data with the patient's real-time posture. However, existing methods are hindered by the ill-posed nature of 2D-to-3D localization and the distinctive anatomical features of the spinal column, leading to ambiguities and reduced accuracy. In this paper, we introduce X2P-net, a novel prompt-guided and semantic context-enhanced 2D/3D vertebra detection framework. To achieve this, we design a novel Transformer architecture, referred to as BrickFormer, which can automatically extract the refined vertebral foreground context at low computational cost using a dual-attention mechanism. Comprehensive experiments were conducted to validate the proposed approach on two datasets: a large-scale synthetic dataset (BiSpineX) and a sheep spine dataset (SheepSpineX). Results obtained from these experiments demonstrate supe

## Méthodologie

{'study_design': None, 'intervention': None, 'control': None, 'primary_outcomes': [], 'secondary_outcomes': [], 'statistical_methods': [], 'duration': None, 'setting': None}

## Résultats

{'quantitative': [{'outcome': 'PCL 3D @10mm improvement, Brick-Former vs vanilla attention', 'value': '+2.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'the proposed Brick-Former demonstrates improved performance with an increase in PCL 3D @10mm by 2.2%'}, {'outcome': 'PCL 3D @20mm improvement, Brick-Former vs vanilla attention', 'value': '+1.6', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'PCL 3D @20mm by 1.6%'}, {'outcome': 'Average MPE 3D decrease, Brick-Former vs vanilla attention', 'value': '-1.14', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'a decrease in average MPE 3D by 1.14 mm'}, {'outcome': 'AUC 3D increase, Brick-Former vs vanilla attention', 'value': '+0.0129', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'an increase in AUC 3D by 0.0129'}, {'outcome': 'PCL 3D @10mm improvement, Brick-Former vs sparse attention', 'value': '3.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'our method achieved 3.7% and 0.7% improvements in PCL 3D @10mm and PCL 3D @20mm, respectively'}, {'outcome': 'PCL 3D @20mm improvement, Brick-Former vs sparse attention', 'value': '0.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'our method achieved 3.7% and 0.7% improvements in PCL 3D @10mm and PCL 3D @20mm, respectively'}, {'outcome': 'Average MPE 3D reduction, Brick-Former vs sparse attention', 'value': '1.73', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'a 1.73 mm reduction in average MPE 3D'}, {'outcome': 'AUC 3D increase, Brick-Former vs sparse attention', 'value': '0.0053', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 1', 'source_quote': 'a 0.0053 increase in AUC 3D'}, {'outcome': 'Computational cost increase from embedding dimension 4x4 to 16x16', 'value': '~20', 'unit': 'million FLOPs', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 2', 'source_quote': 'increasing the resolution from 4 × 4 to 16 × 16 raised the computational cost by approximately 20 million FLOPs'}, {'outcome': 'PCL 3D @10mm increase, top-k 4 to 8', 'value': '1.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'Increasing the top-k from 4 to 8 resulted in a 1.2% and 2.1% increase in PCL 3D @10mm and PCL 3D @20mm, respectively'}, {'outcome': 'PCL 3D @20mm increase, top-k 4 to 8', 'value': '2.1', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'Increasing the top-k from 4 to 8 resulted in a 1.2% and 2.1% increase in PCL 3D @10mm and PCL 3D @20mm, respectively'}, {'outcome': 'Average MPE 3D reduction, top-k 4 to 8', 'value': '1.2', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'a reduction in the average MPE 3D by 1.2 mm'}, {'outcome': 'AUC 3D increase, top-k 4 to 8', 'value': '0.0110', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 3', 'source_quote': 'an increase in AUC 3D by 0.0110'}, {'outcome': 'PCL 3D @10mm increase, pooling stride α=2 vs α=1', 'value': '1.8', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'when α was set to 2 (compared to α = 1), PCL 3D increased by 1.8% and 1.5% at the 10 mm and 20 mm thresholds, respectively'}, {'outcome': 'PCL 3D @20mm increase, pooling stride α=2 vs α=1', 'value': '1.5', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'PCL 3D increased by 1.8% and 1.5% at the 10 mm and 20 mm thresholds, respectively'}, {'outcome': 'MPE 3D decrease, pooling stride α=2 vs α=1', 'value': '0.25', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'MPE 3D decreased by 0.25 mm'}, {'outcome': 'AUC 3D increase, pooling stride α=2 vs α=1', 'value': '0.0117', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'AUC 3D increased by 0.0117'}, {'outcome': 'PCL 3D @10mm increase, pooling stride α=4 vs α=1', 'value': '2.2', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'When α was increased to 4, the performance improved, with PCL 3D increasing by 2.2% and 1.1% at the respective thresholds'}, {'outcome': 'PCL 3D @20mm increase, pooling stride α=4 vs α=1', 'value': '1.1', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'PCL 3D increasing by 2.2% and 1.1% at the respective thresholds'}, {'outcome': 'MPE 3D decrease, pooling stride α=4 vs α=1', 'value': '1.08', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'MPE 3D decreasing by 1.08 mm'}, {'outcome': 'AUC 3D increase, pooling stride α=4 vs α=1', 'value': '0.0117', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 4', 'source_quote': 'AUC 3D increasing by 0.0117'}, {'outcome': 'Average MPE 3D under x-axis prompt displacement', 'value': '<3.00', 'unit': 'mm', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'the average MPE 3D was below 3.00 mm'}, {'outcome': 'PCL 3D @20mm under x-axis prompt displacement', 'value': '>98.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'the PCL 3D @20mm remained above 98.7% for both views'}, {'outcome': 'Maximal change in MPE 3D, ground truth vs displaced prompts (x-axis)', 'value': '<0.01', 'unit': 'mm', 'confidence_interval': None, 'p_value': 'p=0.77 (LAT), p=0.42 (AP)', 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'the maximal change in terms of MPE 3D was less than 0.01 mm, and no statistically significant difference was detected (p-value = 0.77 for the LAT view and p-value = 0.42 for the AP view)'}, {'outcome': 'Maximal change in average MPE 3D at 10 pixels y-axis displacement', 'value': '0.06', 'unit': 'mm', 'confidence_interval': None, 'p_value': 'p=0.09 (LAT), p=0.83 (AP)', 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'the maximal change in terms of the average MPE 3D increased to 0.06 mm, although no statistically significant difference was detected when comparing the results using the ground truth centers with those using the displaced prompts (p-value = 0.09 for the LAT view, p-value = 0.83 for the AP view)'}, {'outcome': 'Maximal change in average MPE 3D at 20 pixels y-axis displacement', 'value': '0.14', 'unit': 'mm', 'confidence_interval': None, 'p_value': 'p<0.001 (both views)', 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'the maximal change in terms of the average MPE 3D increased to 0.14 mm, and the differences between the results using the ground truth centers and those using the displaced prompts were statistically significant (p-values < 0.001 for both views)'}, {'outcome': 'PCL 3D @20mm at 20 pixels y-axis displacement', 'value': '>98.7', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, paragraphe 5', 'source_quote': 'though the PCL 3D @20mm remained above 98.7%'}], 'qualitative_findings': ['Le mécanisme dual-attention de BrickFormer filtre efficacement les informations non pertinentes des caractéristiques de premier plan à haute résolution, améliorant ainsi la précision de la localisation.', "La précision de localisation vertébrale s'améliore avec l'augmentation de la dimension d'embedding, atteignant un pic à 16 × 16, probablement grâce à une résolution plus élevée des cartes de chaleur 2D prédites offrant plus d'informations contextuelles.", "Un top-k plus élevé implique un plus grand nombre de régions/caractéristiques impliquées dans le calcul d'attention fine lors de la deuxième étape.", "Un α plus grand correspond à un champ récepteur plus large pour le calcul d'attention sur les caractéristiques basse résolution, fournissant plus de contexte pour le calcul d'attention fine, ce qui améliore la précision de localisation.", "La performance de la méthode n'est pas sensible au déplacement du prompt le long de l'axe x pour les deux vues (LAT et AP).", "La méthode est plus sensible au déplacement du prompt le long de l'axe y, avec des différences statistiquement significatives observées à 20 pixels de déplacement, bien que l'ampleur du changement de performance reste faible."], 'main_findings': ["Le Brick-Former proposé surpasse à la fois le mécanisme d'attention vanilla et le mécanisme d'attention sparse sur toutes les métriques (PCL 3D @10mm, PCL 3D @20mm, MPE 3D moyen, AUC 3D).", "Une dimension d'embedding vertébral de 16 × 16 offre la meilleure précision de localisation, au prix d'un coût computationnel accru (~20 millions FLOPs supplémentaires par rapport à 4 × 4).", 'Un top-k de 8 améliore significativement la performance par rapport à un top-k de 4.', 'Un pooling stride α = 4 offre la meilleure performance parmi les configurations testées (α = 1, 2, 4) sur le dataset BiSpineX.', "La méthode proposée est robuste au déplacement du point-like prompt le long de l'axe x, mais montre une sensibilité statistiquement significative (bien que d'ampleur limitée) au déplacement le long de l'axe y à 20 pixels."]}

## Conclusions

X2P-Net, a prompt-guided and context-aware network, estimates 3D positions of vertebrae from biplanar X-ray images using a novel BrickFormer architecture The network includes a prompt-guided FE unit, an SCE unit, and a 3D multi-view feature fusion unit, leveraging vertebral context and positional information from the reference vertebra indicated by the prompt A generic and novel way to incorporate anatomical prior information of the spine was introduced using a set of learnable vertebral embeddings, trained to delineate each vertebral level using BrickFormer Comprehensive experiments on two datasets (BiSpineX and SheepSpineX) demonstrated the superior performance of the proposed method over other SOTA methods X2P-Net achieved better quantitative results than SOTA methods: on BiSpineX, PCL 3D @10mm of 96.9%, PCL 3D @20mm of 98.8%, average MPE 3D of 2.99 mm, and AUC 3D of 0.9923; on SheepSpineX, PCL 3D @10mm of 98.4%, PCL 3D @20mm of 100.0%, MPE 3D of 1.08 mm, and AUC of 0.9972 The method is computationally efficient (3.24M parameters, 130.8 GMacs, ~0.1 s inference time for a 512×512 image, ~3 GB GPU memory usage) Future work will focus on prospective clinical trials to validate the method in real-world surgical practice, with potential integration into MISS systems to support intraoperative guidance and enhance the safety and quality of spinal surgery

## Comparisons of 2D and 3D vertebra localization on the BiSpineX dataset with other SOTA methods. ↑: higher value indicates better results. ↓: lower value indicates better results. Pix: pixels. The best results are displayed in bold font.

|  |  | 2D localization (LAT view) |  |
| --- | --- | --- | --- | --- | --- |
| Methods | PCL 2D @10p(%) ↑ | PCL 2D @20p(%) ↑ | MPE 2D (pix) ↓ AUC 2D ↑ |
| SCN-Net [21] |  | 93.8 | 96.9 | 3.78 | 0.9735 |
| Spine-Trans [22] |  | 93.2 | 95.9 | 3.87 | 0.9689 |
| AdaFuse [57] |  | 91.1 | 95.8 | 4.61 | 0.9609 |
| ALG-Net [47] |  | 92.5 | 96.5 | 4.43 | 0.9716 |
| VOL-Net [47] |  | 92.3 | 96.5 | 4.33 | 0.9703 |
| Ours |  | 88.2 | 96.6 | 5.84 | 0.9701 |
|  |  | 2D localization (AP view) |  |
| Methods | PCL 2D @10p(%) ↑ | PCL 2D @20p(%) ↑ | MPE 2D (pix) ↓ AUC 2D ↑ |
| SCN-Net [21] |  | 90.0 | 96.8 | 4.96 | 0.9682 |
| Spine-Trans [22] |  | 88.1 | 96.5 | 5.26 | 0.9667 |
| AdaFuse [57] |  | 87.6 | 94.8 | 5.66 | 0.9586 |
| ALG-Net [47] |  | 88.6 | 95.9 | 5.39 | 0.9607 |
| VOL-Net [47] |  | 88.2 | 95.4 | 5.44 | 0.9584 |
| Ours |  | 85.2 | 96.0 | 6.14 | 0.9681 |
|  |  |  | 3D localization |  |
| Methods PCL SCN-Net [21] | 90.5 | 92.6 | 8.94 | 0.9274 |
| Spine-Trans [22] |  | 87.5 | 91.5 | 9.21 | 0.9166 |
| AdaFuse [57] |  | 95.8 | 97.9 | 3.95 | 0.9826 |
| ALG-Net [47] |  | 95.7 | 98.3 | 3.25 | 0.9846 |
| VOL-Net [47] |  | 95.4 | 98.0 | 3.49 | 0.9827 |
| Ours |  | 96.9 | 98.8 | 2.99 | 0.9923 |

## Comparisons of 3D vertebra localization with other SOTA methods on the SheepSpineX dataset. ↑: higher value indicates better results. ↓: lower value indicates better results. The best results are displayed in bold font.

| Method | 3D Localization PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ | AUC 3D ↑ |
| --- | --- | --- | --- | --- |
| SCN-Net [21] | 95.2 | 97.2 | 3.71 | 0.9854 |
| Spine-Trans [22] | 93.5 | 97.5 | 4.42 | 0.9803 |
| AdaFuse [57] | 97.2 | 99.7 | 2.41 | 0.9944 |
| ALG-Net [47] | 96.5 | 100.0 | 1.56 | 0.9948 |
| VOL-Net [47] | 96.3 | 99.8 | 1.63 | 0.9939 |
| Ours | 98.4 | 100.0 | 1.08 | 0.9972 |

## Results of the ablation study investigating the effectiveness of key components in our method. ↑: higher value indicates better results. ↓: lower value indicates better results. The best results are displayed in bold font.

| Components PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ | AUC 3D ↑ | Params ↓ | FLOPs ↓ |
| --- | --- | --- | --- | --- | --- | --- |
| No Prompt | 90.2 | 93.1 | 6.27 | 0.9653 | 3.04 M | 129.4 GMac |
| No SCE | 92.3 | 94.8 | 5.95 | 0.9657 | 3.00 M | 108.1 GMac |
| No Fusion | 92.8 | 96.5 | 5.90 | 0.9822 | 3.22 M | 123.6 GMac |
| Ours | 96.9 | 98.8 | 2.99 | 0.9923 | 3.24 M | 130.8 GMac |

## Results of investigating the influence of different attention mechanisms on the performance of the proposed method. ↑: higher value indicates better results. ↓: lower value indicates better results. The best results are displayed in bold font.

| Methods | PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ AUC 3D ↑ Params ↓ | FLOPs ↓ |
| --- | --- | --- | --- | --- | --- | --- |
| Vanilla attention [23] | 94.7 | 97.2 | 4.13 | 0.9794 | 3.24 M | 109.2 GMac |
| Sparse attention [63] | 93.2 | 98.1 | 4.72 | 0.9870 | 3.24 M | 111.2 GMac |
| Ours | 96.9 | 98.8 | 2.99 | 0.9923 | 3.24 M | 130.8 GMac |
|  | 4.4.3. Results on Investigating the Impact of Different Hyperparameters |  |

## Results of the ablation study investigating the impact of different hyperparameters. ↑: higher value indicates better results. ↓: lower value indicates better results. The best results are displayed in bold font. Results of Investigating the Sensitivity of Our Method to Prompt Displacement

|  |  | A. Impact of spatial dimensions of vertebral embeddings. |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Dimensions PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ | AUC 3D ↑ | Params ↓ | FLOPs↓ |
| 4 × 4 | 92.4 | 95.1 | 5.92 | 0.9661 | 3.08 M | 109.8 GMac |
| 8 × 8 | 93.2 | 96.7 | 4.19 | 0.9731 | 3.11 M | 114.0 GMac |
| 16 × 16 | 96.9 | 98.8 | 2.99 | 0.9923 | 3.24 M | 130.8 GMac |
|  |  |  | B. Impact of top-k value. |  |  |  |
| Top-k | PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ | AUC 3D ↑ | Params ↓ | FLOPs ↓ |
| 2 | 93.1 | 95.4 | 5.63 | 0.9665 | 3.24 M | 114.7 GMac |
| 4 | 95.7 | 97.9 | 3.59 | 0.9813 | 3.24 M | 120.0 GMac |
| 8 | 96.9 | 98.8 | 2.99 | 0.9923 | 3.24 M | 130.8 GMac |
|  |  | C. Impact of pooling stride α. |  |  |  |
| α | PCL 3D @10mm(%) ↑ PCL 3D @20mm(%) ↑ MPE 3D (mm) ↓ | AUC 3D ↑ | Params ↓ | FLOPs ↓ |
| 1 | 92.9 | 96.2 | 4.32 | 0.9689 | 3.24 M | 110.8 GMac |
| 2 | 94.7 | 97.7 | 4.07 | 0.9806 | 3.24 M | 114.7 GMac |
| 4 | 96.9 | 98.8 | 2.99 | 0.9923 | 3.24 M | 130.8 GMac |

### Formule


$$f i = VFE(I i ), ∀ i ∈ {lat, ap},(1)$$

### Formule


$$M p (x, y) = 1, (x, y) ∈ Ω p , 0, otherwise, Ω p = {(x, y) | x 0 -r ≤ x < x 0 + r, y 0 -r ≤ y < y 0 + r},(2)$$

### Formule


$$f p (x, y) = f i (x, y)M p (x, y), (x, y) ∈ Ω p .(3)$$

### Formule


$$M d (x, y) = ∥y -y 0 ∥ 2 , ∀(x, y). (4$$

### Formule


$$)$$

### Formule


$$Out = so f tmax    f i W Q • f p W K T √ d    • f p W V ,(5)$$

### Formule


$$f m (x, y) = f e (x, y) Md (x, y) + M d (x, y), ∀(x, y), Md (x, y) = 0, if M d (x, y) = 0, 1, if M d (x, y) > 0.(6)$$

### Formule


$$Attn 1 = so f tmax e n W Q1 • fm W K1 T √ d ,(7)$$

### Formule


$$Attn 2 = so f tmax e n W Q2 • ( f s W K2 ) T √ d .(8)$$

### Formule


$$ẽ = { ẽn | n = 1, . . . , N} with ẽn = Attn 2 • ( f s W V2 ),(9)$$

### Formule


$$L 2 O whMd α 2 + O kα 2 Md .$$

### Formule


$$Loss MSE = 1 2 × N × 16 × 16 ∑ i N ∑ n=1 16 ∑ x=1 16 ∑ y=1 (p i,n (x, y) -pi,n (x, y)) 2 , (10$$

### Formule


$$)$$

### Formule


$$Loss Dice = 1 - 1 2N ∑ i N ∑ n=1 2 16 ∑ x=1 16 ∑ y=1 p i,n (x, y) pi,n (x, y) 16 ∑ x=1 16 ∑ y=1 (p i,n (x, y)) 2 + 16 ∑ x=1 16 ∑ y=1 ( pi,n (x, y)) 2 , (11$$

### Formule


$$)$$

### Formule


$$Loss 2D = Loss MSE + Loss Dice . (12$$

### Formule


$$)$$

### Formule


$$Loss 3D = 1 N v N v ∑ n=1 l n -ln 2 2 . (13$$

### Formule


$$)$$

### Formule


$$Loss Overall = Loss 2D + Loss 3D . (14$$

### Formule


$$)$$

### Formule


$$PCL@τ = 1 N t N t ∑ n=1 THR τ l n , ln , THR τ l n , ln = 1, if l n -ln 2 < τ, 0, otherwise,(15)$$

### Formule


$$MPE = 1 N ∑ N i=0 ∥x i -xi ∥ 2 (16$$

### Formule


$$)$$
