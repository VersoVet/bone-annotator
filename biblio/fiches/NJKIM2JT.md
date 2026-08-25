# FluoroSAM: A Language-promptable Foundation Model for Flexible X-ray Image Segmentation.

**Auteurs** : Benjamin D Killeen, Liam J Wang, Blanca Iñígo, Han Zhang, Mehran Armand, Russell H Taylor, Greg Osgood, Mathias Unberath
**Année** : 2026
**DOI** : 10.1007/978-3-032-04981-0_24

## Résumé

Language promptable X-ray image segmentation would enable greater flexibility for human-in-the-loop workflows in diagnostic and interventional precision medicine. Prior efforts have contributed task-specific models capable of solving problems within a narrow scope, but expanding to broader use requires additional data, annotations, and training time. Recently, language-aligned foundation models (LFMs) - machine learning models trained on large amounts of highly variable image and text data thus enabling broad applicability - have emerged as promising tools for automated image analysis. Existing foundation models for medical image analysis focus on scenarios and modalities where large, richly annotated datasets are available. However, the X-ray imaging modality features highly variable image appearance and applications, from diagnostic chest X-rays to interventional fluoroscopy, with varying availability of data. To pave the way toward an LFM for comprehensive and language-aligned analy

## Méthodologie

{'study_design': "Développement d'un modèle de fondation language-aligned (LFM) pour la segmentation d'images X-ray, entraîné from scratch sur un dataset synthétique massif (FluoroSeg), puis évalué quantitativement sur des images X-ray réelles (interventionnelles et radiographies thoraciques)", 'intervention': 'Entraînement de FluoroSAM avec prompts textuels, points et masques, utilisant un encodeur SwinTransformer et un encodeur de texte combinant CLIP figé + MLP avec bottleneck de quantification vectorielle (VQ)', 'control': 'Comparaison implicite avec MedSAM et SAM comme modèles pairs', 'primary_outcomes': ['Performance de segmentation sur images X-ray interventionnelles réelles', 'Performance de segmentation sur radiographies thoraciques (CXR) avec segmentations pulmonaires annotées manuellement'], 'secondary_outcomes': ['Robustesse de la segmentation face à des prompts textuels variables (étude utilisateur limitée)'], 'statistical_methods': [], 'duration': "Entraînement de 10 epochs, temps total d'entraînement de 6 jours", 'setting': "Environnement de simulation computationnelle pour génération d'images synthétiques + évaluation sur images cliniques réelles"}

## Résultats

{'quantitative': [{'outcome': "Vitesse de génération d'images de simulation", 'value': '6.5 ± 15.7', 'unit': 'images par seconde', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Methods', 'source_quote': 'the simulation environment is able to generate 6.5 ± 15.7 images per second, depending on the exam, with a total of 2.95M images generated in about 6 GPU days'}], 'qualitative_findings': ["Résultats qualitatifs cohérents avec l'hypothèse que la VQ améliore la robustesse de la segmentation face à des prompts textuels variables", "FluoroSAM avec VQ a correctement segmenté le fémur en répondant à la question « What's the bone next to the hip? »"], 'main_findings': ['Sur les images X-ray interventionnelles, FluoroSAM surpasse ses pairs même avec un prompting textuel seul', "Sur les CXR, FluoroSAM s'adapte aux segmentations pulmonaires annotées manuellement bien qu'entraîné uniquement sur des données synthétiques, alors que MedSAM inclut cette tâche dans ses données d'entraînement"]}

## Conclusions

FluoroSAM est capable de segmenter une large gamme de structures anatomiques et d'outils non-anatomiques dans des images X-ray synthétiques, interventionnelles et thoraciques FluoroSAM constitue un catalyseur clé pour l'interaction homme-machine dans le domaine des rayons X, ouvrant de nouvelles perspectives en imagerie diagnostique et interventionnelle La capacité à interpréter un large éventail de prompts textuels positionne FluoroSAM comme une base pour de futures applications autonomes et de type human-in-the-loop
