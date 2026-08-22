# Cat Skin Disease Detection System Using You Only Look Once (YOLO) v8 Algorithm

**Auteurs** : Bunga Meilita, Wiyli Yustanti
**Année** : 2024
**DOI** : 10.26740/jeisbi.v5i2.60656

## Résumé

Kucing adalah hewan peliharaan yang popular di Indonesia, dengan jumlah populasi mencapai 4,80 juta ekor pada tahun 2022. Meskipun menggemaskan dan menyenangkan, kucing rentan terkena penyakit, terutama penyakit kulit speerti jamur. Pemilik hewan masih banyak yang kurang memahami gejala penyakit kulit kucing, sehingga penanganan penyakit tidak tepat yang bisa memperparah kondisi kucing. Solusi untuk mengatasi permasalah tersebut dengan mengimplementasikan algoritma You Only Look Once (YOLO) v8 yang dapat dijalankan secara realtime untuk mendeteksi penyakit kulit kucing jamu, scabies, lain dan sehat melalui aplikasi android. Berdasarkan hasil uji didapatkan Map score sebesar 0.788, precission sebesar 0.727, recall sebesar 0.769, dan F1-Score sebesar 0.75. Hasil pengujian white box berhasil berjalan pada semua test case yang ada. Hasil blackbox testing yaitu aplikasi bisa berjalan sesuai yang diharapkan, selain itu hasil uji pada fitur camera detector dengan pengujian ditiga jarak yang b

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Yolov8n.pt". Proses Training akan dilakukan di platform Google Collaboratory. Sebelum melakukan training akun google collaboratory disambungakn dulu dengan akun gdrive, hal ini dilakukan untuk mengantisipasi hilangnya data hasil training jika terjadi error atau runtime yang terputus. Langkah pertama untuk training dengan algoritma YOLOv8 yaitu mengcloning repository github YOLOv8, hal ini dilakukan agar bisa menambahkan parameter baru untuk mengatasi imbalance class. Gbr. 2 Code Melakukan Cloning YOLOv8Pada penelitian ini dilakukan Teknik class weight untuk mengatasi imbalance class. Class weight adalah metode yang bisa diterapkan dalam machine learning untuk menangani ketidakseimbangan kelas dengan memberikan tingkat bobot yang lebih tinggi kepada kelas yang minoritas

|  | TABEL I |
| --- | --- |
|  | PARAMETER TRAINING |
| ss | Nilai |
| Epoch | 50 dan 100 |
| Batch size | 16, 32, 64 |
| Learning rate | 0.1 -0.00001 |
| optimizer | SGD, Adam, AdamW, NAdam, RAdam, RMS |
|  | Prop |
| Pada proses training ini, menggunakan pretrained |
| weight " |  |

## Development Deployment merupakan tahapan akhir dari penelitian ini. Deployment merupakan tahapan dimana peneliti melakukan implementasi sistem agar menjadi aplikasi yang bisa digunakan oleh pengguna.proses deployment dilakukan dengan menggunakan Bahasa pemrograman Kotlin, sedangkan testing aplikasi menggunakan white box testing, black box testing dan uji analisis. Pada Tabel II Didapatkan hasil paling optimal dari keseluruhan experiment yaitu dengan menggunakan epoch 100, batch size 16, optimizer AdamW, learning rate 0.00125, dan dengan skala pemabgain dataset 90% data training dan 10% data testing. Hasil experiment terbaik didapatkan score mAP yang bernilai 0.788, precision yang bernilai 0.727, recall yang bernilai 0.769, dan F1-Score yang berniali 0.747. Berikut grafik-grafik training model.

|  |  |  |  |  |  | E-ISSN 2774-3993 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (Journal of Emerging Information Systems and Business Intelligence) |
| 90:10 | 100 | 32 | 0.758 0.751 | 0.684 | 0.716 |
| 90:10 | 100 | 64 | 0.766 0.742 | 0.717 | 0.729 |
| !git clone |  |  |  |  |
| https://github.com/ultralytics/ultralytics |  |
| !cd ultralytics |  |  |  |
| !pip install -e . |  |  |  |
|  |  |  |  |  |  | III. HASIL DAN PEMBAHASAN |
|  |  |  |  |  | A Hasil Training dan evaluasi |
|  |  |  |  |  | Proses training model yang dirancang dibagi menjadi |
|  |  |  |  |  | beberapa bagian berdasarkan hyperparameter dan skala |
|  |  |  |  |  | pembagia data yang suddah ditentukan sebelumnya. Adapun |
|  |  |  |  |  | hasil training dari masing-masing data dapat dilihat pada |
|  |  |  |  |  | Tabel II. |
| !yolo train data=data.yaml model=yolov8n.pt epochs=50 imgsz=320 batch=16 optimizer='auto' |  | TABEL III HASIL TRAINING |
|  |  |  |  |  | Skala | Epoch Batch | mAP Precision Recall | F1 |
|  |  |  |  |  | dataset | Size | Score |
|  |  |  |  |  | 70:30 | 50 | 16 | 0.584 0.642 | 0.589 | 0.606 |
|  |  |  |  |  | 70:30 | 50 | 32 | 0.578 0.629 | 0.602 | 0.615 |
|  |  |  |  |  | 70:30 | 50 | 64 | 0.563 0.646 | 0.52 | 0.576 |
|  |  |  |  |  | 70:30 | 100 | 16 | 0.587 0.608 | 0.59 | 0.599 |
|  |  |  |  |  | 70:30 | 100 | 32 | 0.611 0.64 | 0.59 | 0.614 |
|  |  |  |  |  | 70:30 | 100 | 64 | 0.571 0.629 | 0.558 | 0.591 |
|  |  |  |  |  | 80:20 | 50 | 16 | 0.696 0.706 | 0.645 | 0.674 |
|  |  |  |  |  | 80:20 | 50 | 32 | 0.681 0.678 | 0.641 | 0.659 |
|  |  |  |  |  | 80:20 | 50 | 64 | 0.691 0.723 | 0.658 | 0.689 |
|  |  |  |  |  | 80:20 | 100 | 16 | 0.701 0.726 | 0.626 | 0.672 |
|  |  |  |  |  | 80:20 | 100 | 32 | 0.702 0.02 | 0.648 | 0.674 |
|  |  |  |  |  | 80:20 | 100 | 64 | 0.682 0.757 | 0.611 | 0.676 |
|  |  |  |  |  | 90:10 | 50 | 16 | 0.779 0.671 | 0.755 | 0.711 |
|  |  |  |  |  | 90:10 | 50 | 32 | 0.776 0.74 | 0.704 | 0.722 |
|  |  |  |  |  | 90:10 | 50 | 64 | 0.778 0.778 | 0.686 | 0.729 |
|  |  |  |  |  | 90:10 | 100 | 16 | 0.788 0.727 | 0.769 | 0.747 |
|  |  |  |  |  | 181 |

## Setelah mengevaluasi model deteksi penyakit kulit kucing, selanjutnya yait mengexport model ke format tflite. Export model ini dilakukan untuk proses deployment, pada Gbr. 9 merupakan kode untuk melakukan export model.

|  |  | TABEL IIIII |  |  |
| --- | --- | --- | --- | --- |
|  | HASIL EVALUASI |  |  |
| Process | mAP | Precision | Recall | F1 |
|  |  |  |  | Score |
| Validasi/Testing 0.788 | 0.727 | 0.769 | 0.747 |
| Train | 0.788 | 0.727 | 0.769 | 0.747 |

### Formule


$$F$$

### Formule


$$Smartphone I II III IV V 1 ✓ ✓ ✓ ✓ ✓ 2 ✓ ✓ ✓ ✓ ✓ 3 ✓ ✓ ✓ ✓ ✓ 4 ✓ ✓ ✓ ✓ ✓ 5 ✓ ✓ ✓ ✓ ✓ 6 ✓ ✓ ✓ ✓ ✓ 7 ✓ ✓ ✓ ✓ ✓ 8 ✓ ✓ ✓ ✓ ✓ 9 ✓ ✓ ✓ ✓ ✓ 10 ✓ ✓ ✓ ✓ ✓ 11 ✓ ✓ ✓ ✓ ✓ 12 ✓ ✓ ✓ ✓ ✓ 13 ✓ ✓ ✓ ✓ ✓ 14 ✓ ✓ ✓ ✓ ✓$$
