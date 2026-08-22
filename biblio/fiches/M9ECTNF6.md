# OneLabeler: A Flexible System for Building Data Labeling Tools

**Auteurs** : Yu Zhang, Yun Wang, Haidong Zhang, Bin Zhu, Siming Chen, Dongmei Zhang
**Année** : 2022
**DOI** : 10.1145/3491102.3517612

## Résumé

Labeled datasets are essential for supervised machine learning. Various data labeling tools have been built to collect labels in different usage scenarios. However, developing labeling tools is time-consuming, costly, and expertise-demanding on software development. In this paper, we propose a conceptual framework for data labeling and OneLabeler based on the conceptual framework to support easy building of labeling tools for diverse usage scenarios. The framework consists of common modules and states in labeling tools summarized through coding of existing tools. OneLabeler supports configuration and composition of common software modules through visual programming to build data labeling tools. A module can be a human, machine, or mixed computation procedure in data labeling. We demonstrate the expressiveness and utility of the system through ten example labeling tools built with OneLabeler. A user study with developers provides evidence that OneLabeler supports efficient building of d

## Méthodologie

{'study_design': "Étude utilisateur qualitative en session individuelle d'environ deux heures, structurée en quatre phases: recueil d'expérience préalable (~15 min), formation à OneLabeler (~30 min), réalisation de quatre tâches de construction d'outils de labellisation avec OneLabeler (~50 min), et recueil de retours d'expérience (~15 min)", 'intervention': "Utilisation du système OneLabeler par les participants pour accomplir quatre tâches: (1) construire un outil de segmentation d'image similaire à celui de la Fig. 3C sans template prédéfini, pour évaluer la construction de workflows à partir de zéro; (2) adapter un workflow existant à un nouveau scénario d'usage; (3) construire des workflows complexes sur mesure; (4) tâche ouverte pour construire un outil de labellisation personnalisé pour un usage réel (reproduction d'un outil déjà construit ou extension d'OneLabeler avec des modules personnalisés), avec fourniture d'une spécification textuelle des fonctionnalités souhaitées pour chaque tâche", 'control': None, 'primary_outcomes': ["Utilisabilité d'OneLabeler (facilité d'apprentissage et d'utilisation)", "Efficacité de la construction d'outils de labellisation diversifiés"], 'secondary_outcomes': ["Compréhension des concepts de base et de l'usage d'OneLabeler", "Capacité à adapter un workflow existant à un nouveau scénario d'usage", 'Capacité à construire des workflows complexes sur mesure', "Capacité d'OneLabeler à être utilisé pour un outil de labellisation personnalisé en conditions réelles"], 'statistical_methods': [], 'duration': 'Environ deux heures par participant', 'setting': "Session de formation et de réalisation de tâches avec présentation d'un site de documentation sur OneLabeler"}

## Résultats

{'quantitative': [{'outcome': 'Trials completed correctly without hints (T1, T2, T3)', 'value': '18', 'unit': 'trials out of 24', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'Out of the 24 trials in total (8 participants × 3 tasks), the participants could finish the tasks correctly in 18 trials without hints from the experimenter.'}, {'outcome': 'Trials requiring hints from experimenter (T1, T2, T3)', 'value': '6', 'unit': 'trials', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'Four participants (P1, P3, P4, P6) needed hints in six trials to make their results exactly the same as the specification given in the instructions.'}, {'outcome': 'Participants needing hints (T1, T2, T3)', 'value': '4', 'unit': 'participants', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'Four participants (P1, P3, P4, P6) needed hints in six trials to make their results exactly the same as the specification given in the instructions.'}, {'outcome': 'Participants who chose to reproduce their own labeling tool (Task 4)', 'value': '3', 'unit': 'participants', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'For Task 4, three of the participants (P4, P6, P7) chose to reproduce their own labeling tools'}, {'outcome': 'Participants who selected the alternative webpage classification tool (Task 4)', 'value': '5', 'unit': 'participants', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'The other five participants selected the alternative to build a predefined webpage classification tool.'}, {'outcome': 'Participants who completed Task 4 independently', 'value': '5', 'unit': 'out of 8 participants', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'Five out of the eight participants (P1, P2, P4, P7, P8) completed Task 4 independently.'}, {'outcome': 'Participants who completed Task 4 with experimenter help', 'value': '3', 'unit': 'participants', 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Results, 7.2.1 Task Completion', 'source_quote': 'The other three participants (P3, P5, P6) completed Task 4 after receiving help from the experimenter.'}], 'qualitative_findings': ['All participants were able to complete the first three tasks (T1, T2, T3).', 'P4 and P7 developed a text labeling tool similar to Fig. 3D for Task 4.', 'P6 built a tool for pairwise comparison of images for Task 4.', "The experimenter helped P6 with the coding part because P6's tool required creating a new data type for image pairs, and P6 was unfamiliar with the web development skills needed for the customization.", 'P3 and P5 had no web development experience and could not complete the coding part when building the webpage classification tool.', 'After the experimenter helped P3 and P5 develop the required customized module, they were able to construct the workflow to achieve the desired labeling tool.'], 'main_findings': ['All participants successfully completed Tasks 1, 2, and 3, with most trials completed correctly without experimenter hints (18/24).', 'For the more open-ended Task 4, most participants (5/8) completed it independently, while participants lacking web development experience required experimenter assistance specifically for the coding/customization portion, not the workflow construction itself.']}

## Conclusions

Les auteurs ont proposé un cadre conceptuel pour l'étiquetage de données et le système OneLabeler basé sur ce cadre pour faciliter la construction d'outils d'étiquetage pour différents scénarios d'usage Le cadre a été construit en identifiant des états et modules communs par codage de la littérature et en résumant les contraintes de composition des modules pour construire des outils d'étiquetage Chaque processus modulaire peut être instancié comme une procédure de calcul humaine, machine, ou mixte OneLabeler fournit une interface de programmation visuelle utilisant les modules du cadre conceptuel comme blocs de construction OneLabeler intègre diverses implémentations réutilisables permettant aux développeurs de créer des outils d'étiquetage avec peu ou pas de code OneLabeler fournit des fonctionnalités de vérification statique et de prévisualisation pour assister le développement et le débogage OneLabeler supporte la personnalisation, permettant aux développeurs d'étendre davantage ses capacités L'expressivité d'OneLabeler a été démontrée via une étude de cas de construction de dix outils d'étiquetage Une étude utilisateur a été menée pour évaluer l'utilisabilité et recueillir des retours d'utilisateurs potentiels Les résultats de l'étude utilisateur suggèrent qu'OneLabeler est facile à apprendre et permet aux utilisateurs potentiels de construire des outils d'étiquetage efficacement

## Summary of task completion status and time (in minutes).

| Participant | Task 1 | Time | Task 2 | Time | Task 3 | Time | Task 4 | Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | complete | 9 | complete | 5 | complete with hint (state initialization) | 13 | complete | 12 |
| P2 | complete | 13 | complete | 4 | complete | 17 | complete | 11 |
| P3 | complete with hint (parameter) | 15 | complete with hint (parameter) | 4 | complete | 12 | partially complete | 14 |
| P4 | complete | 29 | complete | 5 | complete with hint (linting message) | 25 | complete | 4 |
| P5 | complete | 16 | complete | 3 | complete | 14 | partially complete | 12 |
| P6 | complete with hint (parameter) | 15 | complete | 9 | complete with hint (state initialization) | 25 | partially complete | 22 |
| P7 | complete | 9 | complete | 5 | complete | 18 | complete | 4 |
| P8 | complete | 8 | complete | 8 | complete | 13 | complete | 11 |

## Occurrences of states in the literature. The final codes are abbreviated by initials (e.g., "DO" refers to "data objects"). Slash (/) is used in final codes when the flowchart contains no states or the flowchart's states are excluded in the coding procedure.

| ID | Paper | Venue | Year | Figure Index | Final Codes |
| --- | --- | --- | --- | --- | --- |
| 1 | Fails2003Interactive [27] | IUI | 2003 | 2 | / |
| 2 | Hoi2005Semi [32] | CVPR | 2005 | 1 | DO, L, S |
| 3 | Tian2007Face [66] | CVPR | 2007 | 1 | DO, L, S, F |
| 4 | Cui2007EasyAlbum [19] | CHI | 2007 | 13 | DO, L, F |
| 5 | Hua2008Online [33] | MM | 2008 | 2 | DO |
| 6 | Rooij2010MediaTable [21] | CG&A | 2010 | 3 | DO, L, S |
| 7 | Wang2011Active [73] | TIST | 2011 | 3 | DO, L, M |
| 8 | Wang2011Active [73] | TIST | 2011 | 5 | DO, L, M |
| 9 | Wang2011Active [73] | TIST | 2011 | 7 | DO |
| 10 | Hoeferlin2012Inter [31] | VAST | 2012 | 1(b) | DO, L, M |
| 11 | Tang2013Towards [65] | TOMM | 2013 | 2 | DO, L, S |
| 12 | Zahalka2014Towards [80] | VAST | 2014 | 9 | DO, L, M, F |
| 13 | Bryan2014ISSE [13] | CHI | 2014 | 5 | DO |
| 14 | Paiva2015Approach [53] | TVCG | 2015 | 1 | DO |
| 15 | Russakovsky2015Best [58] | CVPR | 2015 | 2 | L, S |
| 16 | Liao2016Visualization [43] | TMM | 2016 | 1 | DO, L, F |
| 17 | Ye2016Face [78] | MM | 2016 | 1 | DO, L, S |
| 18 | Kucher2017Active [36] | TIIS | 2017 | 1 | DO, L, M |
| 19 | Ratner2017Snorkel [55] | VLDB | 2017 | 2 | DO, L, M |
| 20 | Bernard2018VIAL [6] | TVC | 2018 | 1 | DO, L, S |
| 21 | Bernard2018VIAL [6] | TVC | 2018 | 2 | DO, L, S |
| 22 | Felix2018Exploratory [28] | UIST | 2018 | 1 | L |
| 23 | Zhang2018Collaborative [82] | MM | 2018 | 2 | DO, L |
| 24 | Shang2019Annotating [63] | ICMR | 2019 | 2 | / |
| 25 | Xiang2019Interactive [75] | VAST | 2019 | 2 | DO, L, S |
| 26 | Liu2019Interactive [46] | TVCG | 2019 | 3 | DO, L |
| 27 | Choi2019AILA [18] | CHI | 2019 | 6 | / |
| 28 | Wang2019DeepIGeoS [72] | TPAMI | 2019 | 1 | DO, L |
| 29 | Halter2019VIAN [30] | CGF | 2019 | 2 | DO, L, S, F |
| 30 | Evensen2020Ruler [25] | EMNLP | 2020 | 2 | DO, S, M |
| 31 | Baeuerle2020Classifier [4] | CGF | 2020 | 1 | DO, L |
| 32 | Lekschas2020Peax [40] | CGF | 2020 | 3 | DO, L |
| 33 | Oelen2021Crowdsourcing [52] | IUI | 2021 | 2 | DO, L, M |
| 34 | Rietz2021Cody [57] | CHI | 2021 | 4 | DO, L, M |
| 35 | Zhang2021ChartNavigator [83] | TKDE | 2021 | 1 | DO, F |
| 36 | Zhang2021MI3 [85] | TIIS | 2021 | 3 | DO, L, S, M |

## Occurrences of modules in the literature. The final codes are abbreviated by initials (e.g., "IL" refers to "interactive labeling").

| ID | Paper | Venue | Year | Figure Index | Final Codes |
| --- | --- | --- | --- | --- | --- |
| 1 | Fails2003Interactive [27] | IUI | 2003 | 2 | IL, MT, DL |
| 2 | Hoi2005Semi [32] | CVPR | 2005 | 1 | IL, DOS, MT |
| 3 | Tian2007Face [66] | CVPR | 2007 | 1 | IL, DOS, FE |
| 4 | Cui2007EasyAlbum [19] | CHI | 2007 | 13 | IL, DOS, FE |
| 5 | Hua2008Online [33] | MM | 2008 | 2 | DOS |
| 6 | Rooij2010MediaTable [21] | CG&A | 2010 | 3 | IL, DOS, LI |
| 7 | Wang2011Active [73] | TIST | 2011 | 3 | IL, DOS, MT |
| 8 | Wang2011Active [73] | TIST | 2011 | 5 | IL, DOS, MT |
| 9 | Wang2011Active [73] | TIST | 2011 | 7 | IL, DOS, MT, QA |
| 10 | Hoeferlin2012Inter [31] | VAST | 2012 | 1(b) | IL, DOS, MT |
| 11 | Tang2013Towards [65] | TOMM | 2013 | 2 | IL, DOS, SA |
| 12 | Zahalka2014Towards [80] | VAST | 2014 | 9 | IL, MT, FE, LI |
| 13 | Bryan2014ISSE [13] | CHI | 2014 | 5 | IL, MT |
| 14 | Paiva2015Approach [53] | TVCG | 2015 | 1 | IL, DOS, MT, FE, DL |
| 15 | Russakovsky2015Best [58] | CVPR | 2015 | 2 | IL, DOS, DL |
| 16 | Liao2016Visualization [43] | TMM | 2016 | 1 | IL, DOS, MT |
| 17 | Ye2016Face [78] | MM | 2016 | 1 | MT |
| 18 | Kucher2017Active [36] | TIIS | 2017 | 1 | IL |
| 19 | Ratner2017Snorkel [55] | VLDB | 2017 | 2 | MT |
| 20 | Bernard2018VIAL [6] | TVC | 2018 | 1 | IL, DOS, FE, DL, SA |
| 21 | Bernard2018VIAL [6] | TVC | 2018 | 2 | IL, DOS, MT, FE, DL |
| 22 | Felix2018Exploratory [28] | UIST | 2018 | 1 | IL, QA, LI |
| 23 | Zhang2018Collaborative [82] | MM | 2018 | 2 | IL, DL |
| 24 | Shang2019Annotating [63] | ICMR | 2019 | 2 | IL |
| 25 | Xiang2019Interactive [75] | VAST | 2019 | 2 | IL, DOS, DL |
| 26 | Liu2019Interactive [46] | TVCG | 2019 | 3 | IL, DOS, FE, DL, QA |
| 27 | Choi2019AILA [18] | CHI | 2019 | 6 | IL, DOS, FE |
| 28 | Wang2019DeepIGeoS [72] | TPAMI | 2019 | 1 | IL, DL, SA |
| 29 | Halter2019VIAN [30] | CGF | 2019 | 2 | IL, FE, DL |
| 30 | Evensen2020Ruler [25] | EMNLP | 2020 | 2 | IL, DOS, MT |
| 31 | Baeuerle2020Classifier [4] | CGF | 2020 | 1 | MT, DL, QA |
| 32 | Lekschas2020Peax [40] | CGF | 2020 | 3 | IL, DOS |
| 33 | Oelen2021Crowdsourcing [52] | IUI | 2021 | 2 | IL, DOS, DL |
| 34 | Rietz2021Cody [57] | CHI | 2021 | 4 | IL, MT, DL |
| 35 | Zhang2021ChartNavigator [83] | TKDE | 2021 | 1 | DOS, FE |
| 36 | Zhang2021MI3 [85] | TIIS | 2021 | 3 | IL, DOS, MT, FE, DL, QA, SA |

## Coding the flowchart in AILA

| Preliminary Code | Theme | Final Code |
| --- | --- | --- |
| preprocessing -stemming | feature extraction | FE |
| preprocessing -bag of words | feature extraction | FE |
| preprocessing -term-document matrix | feature extraction | FE |
| preprocessing -word vector | feature extraction | FE |
| preprocessing -sentence vector | feature extraction | FE |
| document analysis -re-ordering -selecting | data object selection | DOS |
| document analysis -re-ordering -sorting | data object selection | DOS |
| document classifier -interactive attentive module -attention weight | preprocessing | / |
| document classifier -interactive attentive module -prediction score | preprocessing | / |
| labeling interface -document embedding | data object selection | DOS |
| labeling interface -document visualization | labeling interface | IL |

### Formule


$$1 class DataObjectSelection { 2 /*$$
