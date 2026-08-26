# From Bounding Boxes to Visual Reasoning: An On-Policy Data Annotation Tool for Vision-Language Models

**Auteurs** : Like Zhang, Runliang Niu, Shiqi Wang, Xiyu Hu, Qianli Xing, Pan Wang, Qingzu He, Qi Wang
**Année** : 2026

## Résumé

Vision-language models (VLMs) are rapidly advancing toward sophisticated grounded structured visual reasoning. Training models for such advanced capabilities demands a new genre of data that seamlessly unifies spatial coordinates, open-vocabulary descriptions, structured attributes, and topological relationships into a singular representation. However, existing data annotation tools fundamentally fail to meet these intricate demands, suffering from three systematic bottlenecks: limited expressiveness, severe annotation-training decoupling, and poor data reusability. To bridge this infrastructure gap, we introduce an open-source annotation tool, ScreenAnnotator. First, we define a unified annotation atom schema that binds spatial, semantic, and structural primitives into a single unit. Second, we implement an on-policy annotation loop embedded with a Bayesian Annotation Verifier (BAV). Finally, we design a template-driven multi-task data synthesis process dynamically transforms static a

## Méthodologie

{'study_design': "Développement d'un outil open-source (SCREENANNOTATOR) évalué via une boucle d'annotation on-policy humain-modèle sur deux scénarios (flowcharts et écrans GUI), avec mesure de l'efficacité d'annotation, de la performance de détection, de la qualité du vérificateur bayésien, et de la performance d'un VLM fine-tuné sur les données synthétisées", 'intervention': "Boucle d'annotation on-policy alternant pré-annotation assistée par modèle (YOLOv11 + Qwen3-VL-4B-Instruct), correction humaine, et ré-entraînement immédiat du modèle, avec routage des annotations à risque via le Bayesian Annotation Verifier (BAV)", 'control': 'Modèle VLM de base (Qwen3-VL-8B-Instruct non fine-tuné) comparé au modèle fine-tuné sur les données synthétisées', 'primary_outcomes': ['Accept Rate (AR)', 'Completion Rate (CR)', "Temps d'annotation par image", 'Précision de détection (Detection F1)', 'Lift metric du BAV', 'Précision moyenne du VLM fine-tuné sur les tâches de raisonnement flowchart'], 'secondary_outcomes': ['Exact Match Rate (EMR) et 1-NED pour la reconnaissance de texte des nœuds', 'Précision par type de tâche (successor, predecessor, condition reasoning, two-hop, sorting, spatial inference, region, relative position, path traversal, counting, coordinate)'], 'statistical_methods': ["MC Dropout (T=30 passes) pour l'inférence bayésienne", "Entropie prédictive et information mutuelle pour l'estimation d'incertitude", 'Métrique de lift pour évaluer la priorisation des erreurs', 'Detection F1 à cinq seuils IoU {0.55, 0.65, 0.75, 0.85, 0.95}', 'Négative ELBO (evidence lower bound) comme fonction de perte pour le BAV'], 'duration': None, 'setting': "Annotation en boucle sur 5 images par round; flowchart: 100 images d'entraînement / 40 d'évaluation; GUI: 120 captures / 20 tenues en réserve pour évaluation"}

## Résultats

{'quantitative': [{'outcome': 'Accept Rate flowchart', 'value': 'nearly 100%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results', 'source_quote': 'The on-policy loop drives the annotation accept rate to nearly 100% on flowcharts and 77% on GUI screenshots'}, {'outcome': 'Accept Rate GUI screenshots', 'value': '77', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the accept rate increases from 0% in round 1 to 77% by round 20'}, {'outcome': 'Completion rate GUI screenshots', 'value': '40.6', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the completion rate drops from 100% to 40.6%'}, {'outcome': 'Précision moyenne du détecteur flowchart', 'value': '94.9', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'The accuracy of the flowchart detector ultimately reaches 94.9%'}, {'outcome': 'Précision moyenne du détecteur GUI', 'value': '64.4', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'the accuracy of the GUI detector reaches 64.4%'}, {'outcome': 'Lift@1% flowchart', 'value': '2.89', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'lift@1% reaches 2.89 by round 3 and remains at this level throughout the remaining rounds'}, {'outcome': 'Lift@1% GUI', 'value': '3.69', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'lift@1% climbs from 1.58 in round 1 to 3.69 by round 5, before stabilizing around 3.16-3.69 in later rounds'}, {'outcome': 'Précision moyenne VLM fine-tuné (flowchart QA)', 'value': '76.1', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract / Results', 'source_quote': 'In the flowchart scenario, fine-tuning a VLM yields 76.1% average accuracy, which is a 35.1% point absolute gain.'}, {'outcome': 'Précision moyenne VLM de base (flowchart QA)', 'value': '41.0', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': "the fine-tuned model achieves an average accuracy of 76.1%, substantially outperforming the base model's 41.0%, corresponding to an absolute improvement of 35.1%"}, {'outcome': 'Successor identification (avant/après fine-tuning)', 'value': '29.3% → 90.6%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Successor identification jumps from 29.3% to 90.6%'}, {'outcome': 'Condition reasoning (avant/après fine-tuning)', 'value': '25.9% → 74.4%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'condition reasoning rises from 25.9% to 74.4%'}, {'outcome': 'Spatial inference (avant/après fine-tuning)', 'value': '24.5% → 89.0%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Spatial inference exhibits the single largest absolute gain, rising from 24.5% to 89.0%'}, {'outcome': 'Path traversal (avant/après fine-tuning)', 'value': '74.3% → 95.5%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results', 'source_quote': 'Path traversal reaches 95.5% (up from 74.3%)'}], 'qualitative_findings': ["Les courbes d'accept rate et de completion rate confirment un transfert progressif de la charge d'annotation des humains vers le modèle au fil des rounds", "Le temps médian d'annotation par image ainsi que sa variance diminuent substantiellement au fil de la boucle on-policy", "Le BAV priorise efficacement les erreurs d'annotation pour re-révision sans supervision humaine de qualité"], 'main_findings': ["La boucle on-policy fait converger l'accept rate vers ~100% sur les flowcharts et 77% sur les écrans GUI", "Le temps d'annotation par image diminue régulièrement à mesure que les données labellisées s'accumulent", "Le BAV atteint des valeurs de lift bien supérieures à 1.0, confirmant sa capacité à prioriser les erreurs d'annotation", "Le fine-tuning d'un VLM sur les données synthétisées via templates produit un gain absolu de 35.1 points de pourcentage (76.1% vs 41.0%) sur les tâches de raisonnement flowchart, avec des gains constants sur les 12 types de tâches"]}

## Conclusions

SCREENANNOTATOR fournit un schéma unifié d'atome d'annotation liant coordonnées spatiales, descriptions en vocabulaire ouvert et attributs structurés La boucle d'annotation on-policy assure une co-évolution continue humain-modèle et un contrôle qualité auto-supervisé via le BAV Le processus de synthèse multi-tâches piloté par templates permet de transformer un effort d'annotation ponctuel en données d'entraînement VLM réutilisables et diversifiées L'outil améliore substantiellement l'efficacité d'annotation, détecte efficacement les erreurs d'annotation, et améliore significativement la performance des VLMs sur des tâches de raisonnement visuel complexes

## 1, we have k=3 and the actual budget fraction is 3/23 ≈ 0.130.

| The lift computation always uses the realized frac- |
| --- |
| tion k/N . |
| A.4 Human Scoring Rubric for Multi-Task |
| Evaluation in Flowchart Scenario |
| Each synthesized QA sample is scored by a human |
| judge on a [0, 1] scale. The rubric is designed so |
| that every instance of the same task type is graded |
| under a uniform standard. Scores are decomposed |
| into a textual component and a spatial (bounding |
| box) component, with task-specific weights sum- |
| marized in Table 2. |
| Textual answers. A fully correct textual re- |
| sponse receives full credit. Minor errors affecting |
| only one or two characters receive approximately |
| 60% credit. Responses that are substantially wrong |
| receive zero credit. |

## Per-task scoring weight decomposition. "Text" denotes the textual answer component and "Box" the spatial localization component.

| Task Type | Text Weight Box Weight |
| --- | --- | --- |
| Successor / Predecessor | 0.30 | 0.70 |
| Count | 0.30 | 0.70 |
| Two-hop | 0.2 / 0.4 / 0.4 (per node) |
| Path | 0.6 (path) + box quality |
| Condition | 0.20 + 0.30 | 0.50 |
| Spatial / Relative / Nearest / Region | 0.50 | 0.50 |
| Sorting | 0.80 | 0.20 |
| Coordinate | 0.50 | 0.50 |
| Bounding boxes. Spatial predictions are graded |
| on a five-level scale: 100% for a precisely local- |
| ized box, 80% for a box that covers the target with |
| slight misalignment, 50% for a box whose intent is |
| recognizable but whose localization is poor, 20% |
| for a box that is far from the target yet shows a |
| directional tendency, and 0% for a missing box, an |
| unparseable output, or a degenerate full-image box. |

### Formule


$$r θ (I, b, ℓ) = σ g θ (I, b) ℓ ≈ p θ (z = 1 | I, b, ℓ)$$

### Formule


$$(t) θ } T t=1$$

### Formule


$$H[z | I, b, ℓ] = -r log r -(1 -r) log(1 -r),(1)$$

### Formule


$$r = 1 T T t=1 r (t)$$

### Formule


$$I[z; θ | I, b, ℓ] = H[z | I, b, ℓ] - 1 T T t=1 H[z | I, b, ℓ, θ (t) ] (2)$$

### Formule


$$r θ (I, b, ℓ) = σ g θ (I, b) ℓ ≈ p θ (z = 1 | I, b, ℓ)(3)$$

### Formule


$$k = k 0 + log 2 (x 2 -x 1 )(y 2 -y 1 ) s 0(4)$$

### Formule


$$g = c x W , c y H , w W , h H , w h + ϵ (5)$$

### Formule


$$W = µ W + σ W ⊙ ε, ε ∼ N (0, I)(6)$$

### Formule


$$L = BCE weighted (ẑ, z)+λ KL l KL[q(θ l ) ∥ p(θ l )](7)$$

### Formule


$$lift@α = P k /P k/N(8)$$

### Formule


$$lift@α = P k /k P/N(9)$$
