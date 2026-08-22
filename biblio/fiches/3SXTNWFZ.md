# A durian leaf image dataset of common diseases in Vietnam for agricultural diagnosis.

**Auteurs** : Thanh TN, Nguyen LX, Cap T, Le T.
**Année** : 2025
**DOI** : 10.1016/j.dib.2025.111845

## Résumé

Agriculture plays a vital role in Vietnam's economy, with durian being a key high-value crop that supports millions of farmers. However, durian leaves are highly susceptible to pests, diseases, and environmental stressors, negatively impacting yield and quality. This study introduces a dataset of 2595 durian leaf images, categorized into six classes: 484 healthy leaves and 2111 diseased leaves spanning Blight (440), Colletotrichum (400), Algal (462), Phomopsis (411), and Rhizoctonia (398). The images were collected from durian orchards across Vietnam under diverse conditions, then background-removed, resized to 400 × 400 pixels, and manually annotated with expert guidance. This dataset provides a valuable resource for advancing research in automated plant disease detection, enabling the development of computer vision models for early diagnosis and precision farming, thereby supporting sustainable durian production and improved crop productivity.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Description of durian leaf diseases.

| No | Class name | Description | Visualization |
| --- | --- | --- | --- |
| 1 | Leaf_Healthy | The leaf is vibrant green, intact, and |  |
|  |  | unaffected by any harmful agents. |  |
| 2 | Leaf_Algal | Affected leaves often exhibit brown, |  |
|  |  | gray, or light green spots caused by |  |
|  |  | algae. |  |

## continued )

| No | Class name | Description | Visualization |
| --- | --- | --- | --- |
| 6 | Leaf_Blight | Symptoms of leaf blight are caused by |  |
|  |  | various factors or unidentified causes. |  |

## Proposed dataset split: training, validation, and test sets.

| Dataset | Ratio (%) | Number of Images | Notes |
| --- | --- | --- | --- |
| Train | 70 | 1814 | Used for model training, requires a large portion to learn features. |
| Validation | 15 | 387 | Used to tune hyperparameters and evaluate during training. |
| Test | 15 | 394 | Used to assess final model performance, independent of training. |
