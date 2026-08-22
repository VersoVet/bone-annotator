# Efficient labeling of retinal fundus photographs using deep active learning

**Auteurs** : Samantha K. Paul, Ian Pan, Warren M. Sobol
**Année** : 2022
**DOI** : 10.1117/1.jmi.9.6.064001

## Résumé

Purpose: To compare the performance of four deep active learning (DAL) approaches to optimize label efficiency for training diabetic retinopathy (DR) classification deep learning models.Approach: 88,702 color retinal fundus photographs from 44,351 patients with DR grades from the publicly available EyePACS dataset were used. Four DAL approaches [entropy sampling (ES), Bayesian active learning by disagreement (BALD), core set, and adversarial active learning (ADV)] were compared to conventional naive random sampling. Models were compared at various dataset sizes using Cohen's kappa (CK) and area under the receiver operating characteristic curve on an internal test set of 10,000 images. An independent test set of 3662 fundus photographs was used to assess generalizability.Results: On the internal test set, 3 out of 4 DAL methods resulted in statistically significant performance improvements (p < 1 × 10 -4 ) compared to random sampling for multiclass classification, with the largest observed differences in CK ranging from 0.051 for BALD to 0.053 for ES. Improvements in multiclass classification generalized to the independent test set, with the largest differences in CK ranging from 0.126 to 0.135. However, no statistically significant improvements were seen for binary classification. Similar performance was seen across DAL methods, except ADV, which performed similarly to random sampling.Conclusions: Uncertainty-based and feature descriptor-based deep active learning methods outperformed random sampling on both the internal and independent test sets at multiclass classification. However, binary classification performance remained similar across random sampling and active learning methods.

## Conclusions

PDF non cohérent: Contenu HTML au lieu de PDF
