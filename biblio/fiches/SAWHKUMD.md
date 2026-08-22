# Automatic medical image annotation and keyword-based image retrieval using relevance feedback.

**Auteurs** : Byoung Chul Ko, JiHyeon Lee, Jae-Yeal Nam
**Année** : 2012
**DOI** : 10.1007/s10278-011-9443-5

## Résumé

This paper presents novel multiple keywords annotation for medical images, keyword-based medical image retrieval, and relevance feedback method for image retrieval for enhancing image retrieval performance. For semantic keyword annotation, this study proposes a novel medical image classification method combining local wavelet-based center symmetric-local binary patterns with random forests. For keyword-based image retrieval, our retrieval system use the confidence score that is assigned to each annotated keyword by combining probabilities of random forests with predefined body relation graph. To overcome the limitation of keyword-based image retrieval, we combine our image retrieval system with relevance feedback mechanism based on visual feature and pattern classifier. Compared with other annotation and relevance feedback algorithms, the proposed method shows both improved annotation performance and accurate retrieval results.

## Méthodologie

{'study_design': "Étude expérimentale comparative évaluant une méthode proposée (WCS-LBP + random forests, score de confiance, relevance feedback) contre des méthodes existantes (MSVM, feature reweighting, SVM-based feedback) sur une base d'images médicales annotées", 'intervention': "Méthode proposée : classification par local WCS-LBP combiné à random forests pour l'annotation, assignation de score de confiance par mot-clé via probabilités des random forests et graphe de relations corporelles, et relevance feedback basé sur caractéristiques visuelles et random forests", 'control': "Comparaison avec MSVM (multiclass SVM) pour l'annotation, méthode à score de confiance égal pour tous les mots-clés pour la recherche, et feature reweighting [2] ainsi que SVM-based feedback [9] pour le relevance feedback", 'primary_outcomes': ["Taux d'erreur d'annotation (error rate)", "Compte d'erreur (error count) sur les codes D et A", 'Précision moyenne de recherche (average retrieval precision)', 'Précision et rappel après relevance feedback'], 'secondary_outcomes': [], 'statistical_methods': ['Random Forests (RF)', 'Multiclass Support Vector Machine (MSVM)', "Calcul du taux d'erreur et du compte d'erreur (error rate, error count)", 'Précision et rappel moyens (average precision and recall)'], 'duration': None, 'setting': 'Système développé en Visual C++ 2008 (entraînement hors-ligne) et ASP.NET 3.5/C# (système de test en ligne), déployé sous le nom Medical Image Searching System (http://cvpr.kmu.ac.kr/miss2)'}

## Résultats

{'quantitative': [{'outcome': "Taux d'erreur et compte d'erreur d'annotation - MSVM avec local WCS-LBP", 'value': '25.5% (error rate); 57.31 (A); 36.96 (D)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'the annotation performance of the MSVM with local WCS-LBP shows 25.5% for error rate, 57.31(A) and 36.96(D) for error count'}, {'outcome': "Taux d'erreur et compte d'erreur d'annotation - RF avec local WCS-LBP (méthode proposée)", 'value': '20.3% (error rate); 38.8 (A); 23.1 (D)', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'RF with the WCS-LBP method showed 20.3% for error rate, 38.8(A) and 23.1(D) for error count, respectively'}, {'outcome': 'Précision moyenne de recherche (méthode proposée vs score de confiance égal)', 'value': '77% vs 71%', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'the overall performance of our approach outperforms the first method regardless of the number of top k as by average percentages of 77% and 71%'}, {'outcome': 'Précision et rappel moyens de la méthode proposée (relevance feedback) sans/après 3 itérations', 'value': '86.2%/82.6% sans feedback; 96.3%/90.1% après 3 itérations', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'The average precision and recall of the proposed method on four different top ks is about 86.2% and 82.6% without relevance feedback. However, after three iterations, the average precision and recall of the proposed method is increased to 96.3% and 90.1%.'}, {'outcome': 'Précision et rappel moyens - SVM-based feedback sans/après 3 itérations', 'value': '83.5%/78.1% sans feedback; 93.2%/85.7% après 3 itérations', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'SVM-based feedback showed average precision and recall on four different top ks is about 83.5% and 78.1% without relevance feedback. After three iterations, the average precision and recall is increased to 93.2% and 85.7%.'}, {'outcome': 'Précision et rappel moyens - Feature reweighting sans/après 3 itérations', 'value': '62.3%/61.7% sans feedback; 68.8%/68.3% après 3 itérations', 'unit': '%', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods/Results', 'source_quote': 'Feature reweighting method showed lowest average precision and recall on four different top ks is about 62.3% and 61.7% without relevance feedback. After three iterations, the average precision and recall is increased to 68.8% and 68.3%, respectively.'}], 'qualitative_findings': ["Pour la requête 'Cranium', les images de crâne sagittal initialement mal classées ont été retirées du top 10 et les images de crâne coronal mieux classées après une itération de relevance feedback"], 'main_findings': ["La méthode combinant local WCS-LBP avec random forests surpasse MSVM pour l'annotation d'images médicales (taux d'erreur et compte d'erreur plus faibles)", "L'assignation de scores de confiance différenciés par mot-clé améliore la précision moyenne de recherche par rapport à un score de confiance égal pour tous les mots-clés", 'Le mécanisme de relevance feedback proposé (basé sur RF) surpasse le feature reweighting et le SVM-based feedback en précision et rappel, avec une amélioration continue au fil des itérations']}

## Conclusions

La méthode proposée combinant local WCS-LBP et random forests améliore la performance d'annotation par mots-clés des images médicales L'assignation de scores de confiance par mot-clé via random forests et graphe de relations corporelles améliore la précision moyenne de recherche par rapport aux méthodes existantes Le mécanisme de relevance feedback basé sur les caractéristiques visuelles et random forests réduit l'écart sémantique et améliore la précision et le rappel de la recherche par rapport au feature reweighting et au SVM-based feedback Les auteurs prévoient d'appliquer leur méthode d'annotation par mots-clés et leur algorithme de recherche à d'autres types d'images médicales, telles que les images cellulaires, CT et IRM

## The final histogram for each sub-image is generated by concatenating the local histograms. Since there are 16 subregions, the final dimension of the local WCS-LBP histogram is 768 [(16×3)×16 subregions]. Finally, we concatenate all of the histograms to create the final local WCS-LBP histogram, as shown in Fig. 1. The concatenated final local WCS-LBP histogram is normalized to unit length using the Gaussian normalization method.

| 1 H and level 2, W 2 H . The lowpass filtered subimage |
| --- |
| W 2 LL is used by itself. |
| In addition, the major problems of medical images, |
| especially radiograph images are high overlapping be- |
| tween image classes (i.e., hand is connected with carpal |
| joint), we divide each sub-image into 4×4 local grids, |
| and extract 16 dimensional local wavelet CS-LBPs from |
| each sub-image. |

### Formule


$$I l ¼ fi 2 I n f ðviÞ j < tg; I r ¼ I n nI l :ð1Þ$$

### Formule


$$f ¼ arg max 1 T X T t¼1 Pðc i l t j Þ ( )ð2Þ$$

### Formule


$$-$$

### Formule


$$t i ¼ 2 1 þ expðg Â dis i Þð3Þ$$

### Formule


$$Cf i ¼ pðc i L j Þ þ t ið4Þ$$

### Formule


$$I ¼ x i ; y i ð Þ f g N i¼1$$

### Formule


$$Cf tþ1 i ¼ a Â Cf tÀ1 i þ ð1 À aÞ Â pðc i L j Þ ð5Þ$$

### Formule


$$Cf tþ1 i ¼ a Â Cf tÀ1 i À ð1 À aÞ Â pðc i L j Þ ð6Þ$$
