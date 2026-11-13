# LATTE: Accelerating LiDAR Point Cloud Annotation via Sensor Fusion, One-Click Annotation, and Tracking



## Quote


three features of LATTE that aim to accelerate LiDAR point cloud annotation: sensor fusion, one-click annotation, and tracking.

three features of LATTE that aim to accelerate LiDAR point cloud annotation: sensor fusion, one-click annotation, and tracking.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.

To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking.


## Raw_Methods


In this section, we discuss in detail three features of LATTE that aim to accelerate LiDAR point cloud annotation: sensor fusion, one-click annotation, and tracking.

In this section, we discuss in detail three features of LATTE that aim to accelerate LiDAR point cloud annotation: sensor fusion, one-click annotation, and tracking.


## Raw_Conclusion


Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.

Efficiently annotating LiDAR point clouds at scale is crucial for the development of LiDAR-based detection and autonomous driving. However, annotating LiDAR point clouds is difficult due to the challenges of low resolution, complex annotating operations, and sequential correlation. To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU.


## Discussion


LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR grâce à la fusion de capteurs, à l’annotation en un clic et au suivi séquentiel. Selon les expérimentations rapportées, l’intégration complète de ces fonctionnalités multiplie la vitesse d’annotation par 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport aux outils de référence. Elle améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision au niveau des instances de 93,5 % contre 69,9 %. Ces résultats indiquent que LATTE peut simultanément réduire l’effort d’annotation et accroître la qualité des labels produits.

LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR grâce à la fusion de capteurs, à l’annotation en un clic et au suivi séquentiel. Selon les expérimentations rapportées, l’intégration complète de ces fonctionnalités multiplie la vitesse d’annotation par 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport aux outils de référence. Elle améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision au niveau des instances de 93,5 % contre 69,9 %. Ces résultats indiquent que LATTE peut simultanément réduire l’effort d’annotation et accroître la qualité des labels produits.


## Raw_Introduction


To address these problems, we propose LATTE, an opensourced LiDAR annotation tool, as shown in Fig. 1. We address the challenges above with the following solutions: 1) Sensor fusion: Cameras have much higher resolution than LiDAR sensors, and image-based detection algorithms are much more mature than LiDAR-based. LiDAR sensors are usually paired with cameras, and the two sensors are calibrated such that each point from the cloud can be projected to a corresponding pixel in the image. Therefore, we can apply camera-based image detection algorithms and transfer labels from an image to a 3D point cloud. The algorithm-generated labels are not perfect and are limited by the algorithm accuracy, projection and synchronization errors, but we can use them as pre-labels to help human annotators recognize objects and "fine-tune" the labels. 2) One-click annotation: We simplify the operational complexity for LiDAR annotation from drawing point-wise labels to drawing 3D bounding boxes, then to top-

To address these problems, we propose LATTE, an opensourced LiDAR annotation tool, as shown in Fig. 1. We address the challenges above with the following solutions: 1) Sensor fusion: Cameras have much higher resolution than LiDAR sensors, and image-based detection algorithms are much more mature than LiDAR-based. LiDAR sensors are usually paired with cameras, and the two sensors are calibrated such that each point from the cloud can be projected to a corresponding pixel in the image. Therefore, we can apply camera-based image detection algorithms and transfer labels from an image to a 3D point cloud. The algorithm-generated labels are not perfect and are limited by the algorithm accuracy, projection and synchronization errors, but we can use them as pre-labels to help human annotators recognize objects and "fine-tune" the labels. 2) One-click annotation: We simplify the operational complexity for LiDAR annotation from drawing point-wise labels to drawing 3D bounding boxes, then to top-


## Synthese


LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT). L’évaluation de LATTE montre que l’utilisation conjointe de la fusion de capteurs, de l’annotation en un clic et du suivi accélère l’annotation LiDAR d’un facteur 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport à la méthode de référence. Cette configuration améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 %. L’étude d’ablation confirme la contribution individuelle des trois fonctionnalités : la fusion de capteurs accélère l’annotation d’un facteur 2,4, l’annotation en un clic d’un facteur 3,8 et le suivi d’un facteur 4,74. Ces résultats indiquent que les gains d’efficacité obtenus avec LATTE ne s’accompagnent pas d’une dégradation de l’accord des annotations par rapport à la référence. LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR grâce à la fusion de capteurs, à l’annotation en un clic et au suivi séquentiel. Selon les expérimentations rapportées, l’intégration complète de ces fonctionnalités multiplie la vitesse d’annotation par 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport aux outils de référence. Elle améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision au niveau des instances de 93,5 % contre 69,9 %. Ces résultats indiquent que LATTE peut simultanément réduire l’effort d’annotation et accroître la qualité des labels produits.

LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT). L’évaluation de LATTE montre que l’utilisation conjointe de la fusion de capteurs, de l’annotation en un clic et du suivi accélère l’annotation LiDAR d’un facteur 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport à la méthode de référence. Cette configuration améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 %. L’étude d’ablation confirme la contribution individuelle des trois fonctionnalités : la fusion de capteurs accélère l’annotation d’un facteur 2,4, l’annotation en un clic d’un facteur 3,8 et le suivi d’un facteur 4,74. Ces résultats indiquent que les gains d’efficacité obtenus avec LATTE ne s’accompagnent pas d’une dégradation de l’accord des annotations par rapport à la référence. LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR grâce à la fusion de capteurs, à l’annotation en un clic et au suivi séquentiel. Selon les expérimentations rapportées, l’intégration complète de ces fonctionnalités multiplie la vitesse d’annotation par 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport aux outils de référence. Elle améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision au niveau des instances de 93,5 % contre 69,9 %. Ces résultats indiquent que LATTE peut simultanément réduire l’effort d’annotation et accroître la qualité des labels produits.

LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT).

LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT).


## Insight


methodology: LATTE articule trois mécanismes complémentaires — fusion de capteurs, annotation en un clic et suivi temporel — afin de réduire les difficultés perceptives, opérationnelles et répétitives associées à l’annotation des nuages de points LiDAR.

methodology: LATTE articule trois mécanismes complémentaires — fusion de capteurs, annotation en un clic et suivi temporel — afin de réduire les difficultés perceptives, opérationnelles et répétitives associées à l’annotation des nuages de points LiDAR.

methodology: LATTE répond aux difficultés liées à la faible résolution des nuages de points, à la complexité des opérations d’annotation et aux corrélations séquentielles en combinant la fusion de capteurs, l’annotation en un clic et le suivi.

methodology: LATTE répond aux difficultés liées à la faible résolution des nuages de points, à la complexité des opérations d’annotation et aux corrélations séquentielles en combinant la fusion de capteurs, l’annotation en un clic et le suivi.


## Methodologie


LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT).

LATTE est un outil open source conçu pour accélérer l’annotation des nuages de points LiDAR, une tâche rendue difficile par la faible résolution spatiale de ces données et par la complexité des annotations tridimensionnelles. Sa méthode combine la fusion LiDAR-caméra pour produire des préannotations, l’annotation en un clic fondée sur le regroupement automatique des points et le suivi temporel pour transférer les annotations entre images consécutives. L’intégration de ces fonctionnalités réduit le temps d’annotation d’un facteur 6,2 et le nombre d’opérations d’un facteur 3,7. Elle améliore également la qualité des annotations par rapport à la procédure de référence, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 % [Unknown](zotero://select/library/items/S9NPUTIT).


## Conclusion


« To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. » « Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU. »

« To solve these problems, we propose LATTE, an open-sourced Li-DAR annotation tool that features sensor-fusion, one-click annotation, and tracking. » « Based on our own experiments we estimate that LATTE achieves a 6.2x speedup compared with baseline annotation tools and delivers better label quality with 23.6% and 2.2% higher instance-level precision and recall, and 2.0% higher bounding box IoU. »


## Resultats


L’évaluation de LATTE montre que l’utilisation conjointe de la fusion de capteurs, de l’annotation en un clic et du suivi accélère l’annotation LiDAR d’un facteur 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport à la méthode de référence. Cette configuration améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 %. L’étude d’ablation confirme la contribution individuelle des trois fonctionnalités : la fusion de capteurs accélère l’annotation d’un facteur 2,4, l’annotation en un clic d’un facteur 3,8 et le suivi d’un facteur 4,74. Ces résultats indiquent que les gains d’efficacité obtenus avec LATTE ne s’accompagnent pas d’une dégradation de l’accord des annotations par rapport à la référence.

L’évaluation de LATTE montre que l’utilisation conjointe de la fusion de capteurs, de l’annotation en un clic et du suivi accélère l’annotation LiDAR d’un facteur 6,2 et réduit le nombre d’opérations d’un facteur 3,7 par rapport à la méthode de référence. Cette configuration améliore également la qualité des annotations, avec une intersection sur union de 87,5 % contre 85,5 %, un rappel de 85,1 % contre 82,9 % et une précision de 93,5 % contre 69,9 %. L’étude d’ablation confirme la contribution individuelle des trois fonctionnalités : la fusion de capteurs accélère l’annotation d’un facteur 2,4, l’annotation en un clic d’un facteur 3,8 et le suivi d’un facteur 4,74. Ces résultats indiquent que les gains d’efficacité obtenus avec LATTE ne s’accompagnent pas d’une dégradation de l’accord des annotations par rapport à la référence.


## Raw_Results


Ablation study: To study the effectiveness of each of the proposed features, we ask volunteers to use a variation of LATTE with only one feature enabled. When volunteers are only allowed to use the sensor fusion feature, we are able to achieve a 2.4 times speed-up in annotation time compared to the baseline while achieving higher IoU (+0.8%), recall (+2.1%), and significantly higher precision (+14.0%). In addition, the number of operations per instance on average reduces by 0.9, nearly an entire operation. This supports our claim that sensor fusion helps human annotators to better recognize objects from point clouds. With only oneclick annotation, our method shows a 3.8 times speedup in annotation time and 2.9 reduction in the number of annotation operations while achieving higher IoU, precision and recall. With only tracking, we show a speed-up of 4.74x while achieving better annotation agreement than the baseline. This is largely due to the fact that tracking saved redundant annotati

Ablation study: To study the effectiveness of each of the proposed features, we ask volunteers to use a variation of LATTE with only one feature enabled. When volunteers are only allowed to use the sensor fusion feature, we are able to achieve a 2.4 times speed-up in annotation time compared to the baseline while achieving higher IoU (+0.8%), recall (+2.1%), and significantly higher precision (+14.0%). In addition, the number of operations per instance on average reduces by 0.9, nearly an entire operation. This supports our claim that sensor fusion helps human annotators to better recognize objects from point clouds. With only oneclick annotation, our method shows a 3.8 times speedup in annotation time and 2.9 reduction in the number of annotation operations while achieving higher IoU, precision and recall. With only tracking, we show a speed-up of 4.74x while achieving better annotation agreement than the baseline. This is largely due to the fact that tracking saved redundant annotati


## Raw_A._Experiment_Setup


We asked nine volunteers to annotate these frames using LATTE with all three features (sensor fusion, one-click annotation, and tracking). We divide the data and volunteers such that each feature is evaluated on the entire dataset. In other words each frame is annotated using each feature so that every feature is evaluated on the same frames. This is to ensure that we are testing each feature on the same data.

We asked nine volunteers to annotate these frames using LATTE with all three features (sensor fusion, one-click annotation, and tracking). We divide the data and volunteers such that each feature is evaluated on the entire dataset. In other words each frame is annotated using each feature so that every feature is evaluated on the same frames. This is to ensure that we are testing each feature on the same data.