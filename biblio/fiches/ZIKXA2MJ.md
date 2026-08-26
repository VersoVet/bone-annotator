# A probabilistic segment anything model for ambiguity‑aware medical image segmentation

**Auteurs** : Tyler Ward, Abdullah Imran
**Année** : 2026
**DOI** : 10.1117/12.3086125

## Résumé

Recent advances in promptable segmentation, such as the Segment Anything Model (SAM), have enabled flexible, high-quality mask generation across a wide range of visual domains. However, SAM and similar models remain fundamentally deterministic, producing a single segmentation per object per prompt, and fail to capture the inherent ambiguity present in many real-world tasks. This limitation is particularly troublesome in medical imaging, where multiple plausible segmentations may exist due to annotation uncertainty or inter-expert variability. In this paper, we introduce Probabilistic SAM, a probabilistic extension of SAM that models a distribution over segmentations conditioned on both the input image and prompt. By incorporating a latent variable space and training with a variational objective, our model learns to generate diverse and plausible segmentation masks reflecting the variability in human annotations. The architecture integrates a prior and posterior network into the SAM framework, allowing latent codes to modulate the prompt embeddings during inference. The latent space allows for efficient sampling during inference, enabling uncertainty-aware outputs with minimal overhead. We evaluate Probabilistic SAM on the public LIDC-IDRI lung nodule dataset and demonstrate its ability to produce diverse outputs that align with expert disagreement, outperforming existing probabilistic baselines on uncertainty-aware metrics. Our code is available at:

## Méthodologie

{'study_design': "Développement et évaluation d'un modèle probabiliste (Probabilistic SAM), extension de SAM basée sur un autoencodeur variationnel conditionnel (CVAE), intégrant un réseau prior p(z|x) et un réseau posterior q(z|x, y) au sein de l'architecture SAM pour moduler les embeddings de prompt via un vecteur latent", 'intervention': "Ajout d'un espace de variable latente à SAM : pendant l'entraînement, un vecteur latent z est échantillonné à partir du réseau posterior (conditionné sur l'image et le masque vérité terrain), projeté via un MLP et ajouté aux embeddings de prompt avant décodage par le décodeur de masque de SAM. À l'inférence, z est échantillonné depuis le réseau prior (conditionné uniquement sur l'image), permettant un échantillonnage répété pour produire un ensemble diversifié de masques plausibles", 'control': 'Comparaison avec Probabilistic U-Net et Dropout SAM comme méthodes de référence (baselines)', 'primary_outcomes': ['Generalized Energy Distance (GED)', 'Intersection over Union (IoU)', 'Dice Similarity Coefficient (DSC)'], 'secondary_outcomes': [], 'statistical_methods': ['Test t apparié unilatéral (one-tailed paired t-test)'], 'duration': None, 'setting': 'Recherche computationnelle / imagerie médicale, utilisant le jeu de données public LIDC-IDRI de nodules pulmonaires'}

## Résultats

{'quantitative': [{'outcome': 'Generalized Energy Distance (GED)', 'value': '0.2910', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 4,39% par rapport à Probabilistic U-Net', 'source_section': 'Results', 'source_quote': "Our model achieves a GED of 0.2910 and an IoU of 0.7849 compared to Probabilistic U-Net's 0.3349 and 0.5557, an improvement of 4.39% and 22.92%, respectively."}, {'outcome': 'Intersection over Union (IoU)', 'value': '0.7849', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 22,92% par rapport à Probabilistic U-Net', 'source_section': 'Results', 'source_quote': "Our model achieves a GED of 0.2910 and an IoU of 0.7849 compared to Probabilistic U-Net's 0.3349 and 0.5557, an improvement of 4.39% and 22.92%, respectively."}, {'outcome': 'Dice Similarity Coefficient (DSC)', 'value': '0.8255', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': 'Amélioration de 14,56% par rapport à Dropout SAM (0.6799)', 'source_section': 'Results', 'source_quote': 'Probabilistic SAM also achieves a higher DSC (0.8255) compared to Dropout SAM (0.6799), an improvement of 14.56%.'}], 'qualitative_findings': [], 'main_findings': ['Probabilistic SAM produit des masques de segmentation divers et plausibles alignés avec le désaccord entre experts', "Probabilistic SAM surpasse les méthodes de référence probabilistes et par dropout sur les métriques tenant compte de l'incertitude", "L'espace latent permet un échantillonnage efficace à l'inférence avec un surcoût minimal"]}

## Conclusions

Probabilistic SAM permet la génération de segmentations diverses et tenant compte de l'incertitude à partir d'une seule image et d'un seul prompt Le modèle capture avec succès la variabilité entre annotateurs sur le jeu de données LIDC-IDRI Le modèle surpasse les méthodes de référence probabilistes et par dropout

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
