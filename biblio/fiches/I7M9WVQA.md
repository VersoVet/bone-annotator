# A probabilistic segment anything model for ambiguity‑aware medical image segmentation

**Auteurs** : Tyler Ward, Abdullah Imran
**Année** : 2026
**DOI** : 10.1117/12.3086125

## Résumé

Recent advances in promptable segmentation, such as the Segment Anything Model (SAM), have enabled flexible, high-quality mask generation across a wide range of visual domains. However, SAM and similar models remain fundamentally deterministic, producing a single segmentation per object per prompt, and fail to capture the inherent ambiguity present in many real-world tasks. This limitation is particularly troublesome in medical imaging, where multiple plausible segmentations may exist due to annotation uncertainty or inter-expert variability. In this paper, we introduce Probabilistic SAM, a probabilistic extension of SAM that models a distribution over segmentations conditioned on both the input image and prompt. By incorporating a latent variable space and training with a variational objective, our model learns to generate diverse and plausible segmentation masks reflecting the variability in human annotations. The architecture integrates a prior and posterior network into the SAM framework, allowing latent codes to modulate the prompt embeddings during inference. The latent space allows for efficient sampling during inference, enabling uncertainty-aware outputs with minimal overhead. We evaluate Probabilistic SAM on the public LIDC-IDRI lung nodule dataset and demonstrate its ability to produce diverse outputs that align with expert disagreement, outperforming existing probabilistic baselines on uncertainty-aware metrics. Our code is available at:

## Méthodologie

{'study_design': "Extension probabiliste de SAM utilisant des autoencodeurs variationnels conditionnels (CVAE), intégrant un réseau a priori p(z|x) et un réseau postérieur q(z|x, y) dans l'architecture SAM ; les codes latents modulent les embeddings de prompt avant décodage", 'intervention': "Probabilistic SAM : entraînement via un objectif variationnel (ELBO) avec échantillonnage d'un vecteur latent z depuis le réseau postérieur pendant l'entraînement, projeté et ajouté aux embeddings de prompt avant décodage par le décodeur de masque SAM ; à l'inférence, z est échantillonné depuis le réseau a priori p(z|x) et le processus est répété pour produire un ensemble diversifié de masques plausibles", 'control': 'Comparaison avec Probabilistic U-Net et Dropout SAM comme méthodes de référence', 'primary_outcomes': ['Generalized Energy Distance (GED)', 'Intersection over Union (IoU)', 'Dice Similarity Coefficient (DSC)'], 'secondary_outcomes': ["Métriques de qualité d'incertitude (uncertainty-aware metrics)"], 'statistical_methods': ['One-tailed paired t-test'], 'duration': None, 'setting': 'Jeu de données public LIDC-IDRI de nodules pulmonaires'}

## Résultats

{'quantitative': [{'outcome': 'Generalized Energy Distance (GED)', 'value': '0.2910', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 4.39% par rapport à Probabilistic U-Net', 'source_section': 'Results', 'source_quote': "Our model achieves a GED of 0.2910 and an IoU of 0.7849 compared to Probabilistic U-Net's 0.3349 and 0.5557, an improvement of 4.39% and 22.92%, respectively."}, {'outcome': 'Intersection over Union (IoU)', 'value': '0.7849', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 22.92% par rapport à Probabilistic U-Net', 'source_section': 'Results', 'source_quote': "Our model achieves a GED of 0.2910 and an IoU of 0.7849 compared to Probabilistic U-Net's 0.3349 and 0.5557, an improvement of 4.39% and 22.92%, respectively."}, {'outcome': 'Dice Similarity Coefficient (DSC)', 'value': '0.8255', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 14.56% par rapport à Dropout SAM', 'source_section': 'Results', 'source_quote': 'Probabilistic SAM also achieves a higher DSC (0.8255) compared to Dropout SAM (0.6799), an improvement of 14.56%.'}], 'qualitative_findings': ['Probabilistic SAM produit des sorties diverses alignées avec le désaccord entre experts'], 'main_findings': ['Probabilistic SAM surpasse Probabilistic U-Net en GED (0.2910 vs 0.3349) et en IoU (0.7849 vs 0.5557)', 'Probabilistic SAM surpasse Dropout SAM en DSC (0.8255 vs 0.6799)', 'Un test t apparié unilatéral confirme la significativité des résultats (phrase tronquée dans le texte source)']}

## Conclusions

Probabilistic SAM permet la génération de segmentations diverses et conscientes de l'incertitude à partir d'une seule image et d'un seul prompt Le modèle capture avec succès la variabilité entre annotateurs sur le jeu de données LIDC-IDRI Probabilistic SAM surpasse les méthodes probabilistes et de dropout de référence

## Quantitative evaluation of our proposed Probabilistic SAM against existing work on probabilistic segmentation.Probabilistic SAM is significantly better than the compared methods including Probabilistic U-Net, in terms of all the evaluation metrics (p-values <0.05 ). This demonstrates Probabilistic SAM's enhanced ability to model uncertainty. Qualitative comparison further confirms the superiority of our Probabilistic SAM model. Visual comparison in Fig.3demonstrates that Probabilistic SAM predicted segmentation outputs are better aligned with the ground truth annotations compared to its Probabilistic U-Net counterpart.

| Model | GED (↓) DSC (↑) IoU (↑) |
| --- | --- | --- | --- |
| Dropout U-Net | 0.5156 | 0.5591 | 0.3880 |
| Dropout SAM | 0.5025 | 0.6799 | 0.5150 |
| Probabilistic U-Net | 0.3349 | 0.5818 | 0.5557 |
| Probabilistic SAM | 0.2910 | 0.8255 0.7849 |

### Formule


$$L recon = L BCE (y, ŷ) + L Dice (y, ŷ), (1$$

### Formule


$$)$$

### Formule


$$L BCE (y, ŷ) = - 1 N N i=1 [y i log ŷi + (1 -y i ) log(1 -ŷi ],(2)$$

### Formule


$$2 i y i ŷi + ϵ i y i + i ŷi + ϵ .(3)$$

### Formule


$$L total = L recon + β • D KL [q(z|x, y)∥p(z|x)].(4)$$
