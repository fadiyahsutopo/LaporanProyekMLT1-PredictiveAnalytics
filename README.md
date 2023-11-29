# Laporan Proyek Machine Learning - Fadiyah Sutopo
## Domain Proyek
Di Indonesia, jumlah penumpang transportasi udara internasional berjumlah sebanyak 1.4 juta orang di bulan Juni 2023. Jumlahnya naik sebesar 10.66% jika dibandingkan dengan bulan sebelumnya yaitu bulan Mei 2023. Kemudian pada periode Januari-Juni 2023, jumlah penumpang transportasi udara dengan tujuan luar negeri berjumlah sebanyak 7.1 juta orang, naik 311.56% dibandingkan dengan jumlah penumpang tahun sebelumnya di periode yang sama [1]. Peningkatan ini seringkali diiringi oleh risiko yang mungkin timbul. Hal ini tentu sejalan dengan adanya layanan asuransi yang dapat membantu pelanggannya apabila terdampak kerugian atau risiko selama melakukan perjalanan.

Layanan asuransi merupakan serangkaian elemen dan interaksi yang muncul di antara perusahaan penyedia, lingkungan yang ada, dan pelanggan, untuk memenuhi kebutuhan pelanggan [2]. Layanan asuransi sendiri memiliki banyak jenis, salah satunya merupakan layanan asuransi perjalanan. Asuransi perjalanan merupakan jenis asuransi yang berada di lingkup turisme dan rekreasi, dengan tujuan untuk memenuhi kebutuhan finansial pelanggan dari risiko yang akan muncul ketika melakukan aktivitas perjalanan [2].

Perkembangan teknologi saat ini memungkinkan perusahaan atau organisasi dalam mengamati dan memahami perilaku pelanggan mereka, tak terkecuali perusahaan atau organisasi penyedia layanan asuransi perjalanan. Dengan menggunakan berbagai teknik analisis data dan *machine learning*, perusahaan atau organisasi dapat mempelajari dan memanfaatkan data historis pelanggan mereka, dengan tujuan untuk mengoptimalkan strategi pemasaran. Selain itu, perusahaan dapat memprediksi faktor apa saja yang dapat memengaruhi pembelian asuransi perjalanan. Hal ini akan membuat perusahaan atau organisasi dapat memberikan penawaran yang relevan.

## Business Understanding

### Problem Statements
- Fitur apa saja yang memiliki pengaruh terhadap pembelian asuransi perjalanan?
- Manakah algoritma machine learning terbaik yang dapat memprediksi pembelian asuransi perjalanan berdasarkan data historis yang tersedia?

### Goals
- Mengetahui fitur apa yang memiliki pengaruh terhadap pembelian asuransi perjalanan dan dapat meningkatkan tingkat pembelian asuransi
- Mengetahui algoritma *machine learning* terbaik yang dapat memprediksi pembelian asuransi perjalanan berdasarkan data historis yang tersedia

### Solution Statements
- Menggunakan tiga algoritma *machine learning* yaitu *K-Nearest Neighbor*, *Random Forest*, dan *Boosting* untuk mengetahui algoritma terbaik yang dapat memprediksi pembelian asuransi perjalanan
- Menggunakan metrik evaluasi hasil pengujian *Mean Squared Error (MSE)* untuk mengukur hasil prediksi 

## Data Understanding
Data yang digunakan dalam penelitian ini merupakan dataset Kaggle, **Travel Insurance Prediction Data** dan dapat diakses melalui tautan berikut: [Travel Insurance Prediction Data](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data)

*Dataset* ini digunakan untuk memprediksi ketertarikan *customer* dalam membeli asuransi perjalanan di tahun 2019.

*Dataset* ini memiliki 1987 baris dengan 10 kolom fitur dengan 9 fiturnya digunakan untuk menemukan pola pada data dan 1 fiturnya merupakan target.

### Variabel-variabel pada Travel Insurance Prediction Data
- Index: berisi angka dari 0 sampai 1986
- Age: usia dari *customer*
- Employment Type: sektor pekerjaan *customer*
- GraduateOrNot: apakah *customer* lulus atau tidak dari perguruan tinggi
- AnnualIncome: penghasilan per tahun *customer*
- FamilyMembers: jumlah anggota keluarga yang tinggal bersama *customer*
- ChronicDisease: apakah *customer* memiliki penyakit kronis
- FrequentFlyer: apakah *customer* sering memesan tiket pesawat
- EverTravelledAbroad: apakah *customer* pernah pergi ke luar negeri
- TravelInsurance: apakah *customer* membeli asuransi perjalanan atau tidak

### Exploratory Data Analysis
**Deskripsi variabel yang terdapat di dalam dataset**

Tabel 1. Deskripsi variabel dalam dataset.
|#|Column|Non-Null|Count|Dtype| 
|---|---|---|---|---|
|0|Unnamed: 0|1987|non-null|int64|
|1|Age|1987|non-null|int64|
|2|Employment Type|1987|non-null|object|
|3|GraduateOrNot|1987|non-null|object|
|4|AnnualIncome|1987|non-null|int64| 
|5|FamilyMembers|1987|non-null|int64| 
|6|ChronicDiseases|1987|non-null|int64| 
|7|FrequentFlyer|1987|non-null|object|
|8|EverTravelledAbroad|1987|non-null|object|
|9|TravelInsurance|1987|non-null|int64|

Berdasarkan tabel di atas, dapat dilihat bahwa *dataset* ini memiliki 6 kolom dengan tipe data int64 dan 4 kolom dengan tipe data *object*


**Deskripsi statistik setiap variabel**

Tabel 2. Deskripsi statistik variabel
| |Unnamed: 0|Age|AnnualIncome|FamilyMembers|ChronicDiseases|TravelInsurance|
|---|---|---|---|---|---|---|
|count|1987.000000|1987.000000|1.987000e+03|1987.000000|1987.000000|1987.000000|
|mean|993.000000|29.650226|9.327630e+05|4.752894|0.277806|0.357323|
|std|573.741812|2.913308|3.768557e+05|1.609650|0.448030|0.479332|
|min|0.000000|25.000000|3.000000e+05|2.000000|0.000000|0.000000|
|25%|496.500000|28.000000|6.000000e+05|4.000000|0.000000|0.000000|
|50%|993.000000|29.000000|9.000000e+05|5.000000|0.000000|0.000000|
|75%|1489.500000|32.000000|1.250000e+06|6.000000|1.000000|1.000000|
|max|1986.000000|35.000000|1.800000e+06|9.000000|1.000000|1.000000|

#### Melihat Outliers

![Outlier_Age](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/Outlier_Age.png)

Gambar 1. Box-plot untuk variabel Age

Berdasarkan Gambar 1, tidak terlihat adanya *outliers* pada variabel Age

![Outlier_AnnualIncome](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/Outlier_AnnualIncome.png)

Gambar 2. Box-plot untuk variabel AnnualIncome

Berdasarkan Gambar 2, tidak terlihat adanya *outliers* pada variabel AnnualIncome

![Outlier_FamilyMembers](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/Outlier_FamilyMembers.png)

Gambar 3. Box-plot untuk variabel FamilyMembers

Berdasarkan Gambar 3, tidak terlihat adanya *outliers* pada variabel FamilyMembers

![Outlier_ChronicDiseases](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/Outlier_ChronicDiseases.png)

Gambar 4. Box-plot untuk variabel ChronicDiseases

Berdasarkan Gambar 4, tidak terlihat adanya *outliers* pada variabel ChronicDiseases

![Outlier_TravelInsurance](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/Outlier_TravelInsurance.png)

Gambar 5. Box-plot untuk variabel TravelInsurance

Berdasarkan Gambar 5, tidak terlihat adanya *outliers* pada variabel TravelInsurance

#### Univariate Analysis untuk Categorical Features

![univariate_Employment Type](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/univariate_Employment%20Type.png)

Gambar 6. Distribusi variabel EmploymentType

Pada Gambar 6, jumlah *customer* yang berasal dari sektor pekerjaan Private Sector/Self Employed lebih banyak dibanding *customer* yang berasal dari Government Sector

![univariate_GraduateOrNot](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/univariate_GraduateOrNot.png)

Gambar 7. Distribusi variabel GraduateOrNot

Pada Gambar 7, jumlah *customer* yang sudah lulus perguruan tinggi jumlahnya lebih banyak dibanding *customer* yang tidak/belum lulus perguruan tinggi

![univariate_FrequentFlyer](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/univariate_FrequentFlyer.png)

Gambar 8. Distribusi variabel FrequentFlyer

Pada Gambar 8, jumlah *customer* yang sering memesan tiket pesawat jumlahnya lebih sedikit dibanding *customer* yang jarang memesan tiket pesawat

![univariate_EverTravelledAbroad](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/univariate_EverTravelledAbroad.png)

Gambar 9. Distribusi variabel EverTravelledAbroad

Pada Gambar 9, jumlah *customer* yang belum pernah bepergian ke luar negeri jumlahnya lebih banyak dibanding *customer* yang sudah pernah bepergian ke luar negeri

#### Univariate Analysis untuk Numerical Features

![univariate_NumFeatures](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/univariate_NumFeatures.png)

Gambar 10. Distribusi variabel numerik

Berdasarkan Gambar 10, Dapat disimpulkan bahwa:
- Data didominasi oleh customer yang berusia 28 tahun
- Kategori jumlah anggota keluarga yang tinggal bersama customer terbanyak adalah 4 orang dan tersedikit adalah 9 orang
- Jumlah customer yang tidak memiliki chronic disease atau penyakit kronis lebih dari setengah jumlah customer yang memiliki penyakit kronis
- Jumlah customer yang tidak memiliki asuransi perjalanan lebih banyak daripada customer yang memiliki asuransi perjalanan

#### Multivariate Analysis

![multivariate_analysis](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/multivariate_analysis.png)

Gambar 11. Distribusi analisis *multivariate*

Berdasarkan Gambar 11, dapat disimpulkan bahwa:
- Pada fitur EmploymentType, kategori Private Sector/Private Employed memiliki pengaruh terhadap pembelian asuransi perjalanan
- Rata-rata pembelian asuransi perjalanan terhadap fitur GraduateOrNot cenderung mirip
- Fitur FrequentFlyer dengan kategori Yes memiliki pengaruh yang signifikan terhadap pembelian asuransi perjalanan
- Pada fitur EverTravelledAbroad, customer sudah pernah pergi ke luar negeri memiliki pengaruh yang tinggi terhadap pembelian asuransi perjalanan


## Data Preparation
Pada bagian ini, dilakukan 3 tahap data preparation yaitu:
- *Encoding* fitur kategori
- *Train-Test-Split*
- Standarisasi
Penjelasan dari setiap tahap adalah sebagai berikut.
### Encoding Fitur Kategori

*Encoding* fitur kategori dilakukan menggunakan teknik *one-hot-encoding* yang telah disediakan oleh *library scikit-learn*. Teknik *one-hot-encoding* digunakan untuk mengubah data kategorikal menjadi bentuk numerik.

Pada *dataset* ini, terdapat fitur yang berisi data kategorikal "Yes" dan "No". Teknik *one-hot-encoding* akan mengubah "Yes" menjadi "1" dan "No" menjadi "0". Hasilnya adalah sebagai berikut:

Tabel 3. Hasil dari teknil *one-hot-encoding*
|index|Age|AnnualIncome|FamilyMembers|ChronicDiseases|TravelInsurance|Employment Type\_Government Sector|Employment Type\_Private Sector/Self Employed|GraduateOrNot\_No|GraduateOrNot\_Yes|FrequentFlyer\_No|FrequentFlyer\_Yes|EverTravelledAbroad\_No|EverTravelledAbroad\_Yes|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|31|400000|6|1|0|1|0|0|1|1|0|1|0|
|1|31|1250000|7|0|0|0|1|0|1|1|0|1|0|
|2|34|500000|4|1|1|0|1|0|1|1|0|1|0|
|3|28|700000|3|1|0|0|1|0|1|1|0|1|0|
|4|28|700000|8|1|0|0|1|0|1|0|1|1|0|

### Train-Test-Split
Memecah atau membagi *dataset* menjadi *data training* dan *data testing* menggunakan *library scikit-learn train_test_split* dengan 'test_size = 0.2' atau proporsinya 80:20, 80% *data training* dan 20% *data testing* sehingga didapat:
- Total jumlah seluruh data: 1987
- Total data train: 1589
- Total data test: 398

### Standarisasi
Melakukan standarisasi pada fitur numerik menggunakan teknik *StandardScaler* yang telah disediakan oleh *library scikit-learn* agar diperoleh nilai *mean* = 0 dan standar deviasi = 1

Tabel 4. Hasil dari teknik standarisasi menggunakan *StandardScaler*
| |Age|AnnualIncome|FamilyMembers|ChronicDiseases|
|---|---|---|---|---|
|count|1589.00|1589.00|1589.00|1589.00|
|mean|-0.00|0.00|0.00|-0.00|
|std|1.00|1.00|1.00|1.00|
|min|-1.59|-1.70|-1.72|-0.60|
|25%|-0.56|-0.90|-0.47|-0.60|
|50%|-0.22|-0.10|0.16|-0.60|
|75%|0.81|0.84|0.78|1.65|
|max|1.84|2.31|2.66|1.65|

## Modeling
Pada bagian ini menggunakan tiga buah algoritma *machine learning* yaitu *K-Nearest Neighbor*, *Random Forest*, dan *Boosting*

#### K-Nearest Neighbor (KNN)
K-Nearest Neighbors (KNN) merupakan algoritma supervised sederhana yang dapat mengatasi permasalahan klasifikasi dan regresi [3]. KNN melatih dataset menggunakan data training untuk mengklasifikasikan datanya yang identik dengan query pada data testing [4].

Kelebihan dari algoritma KNN adalah memiliki tingkat kompleksitas yang rendah dan bisa melakukan klasifikasi lebih cepat dibandingkan algoritma machine learning lainnya [4].

Kekurangan dari algoritma KNN adalah algoritma ini tidak mempertimbangkan kelas minoritas dan besaran bobot data sehingga dapat membuat akurasinya turun apabila data yang digunakan memiliki banyak noise [4].

#### Random Forest
Random Forest merupakan algoritma supervised learning dengan metode ensemble learning untuk melakukan klasifikasi, regresi, dan tugas lainnya, yang cara kerjanya adalah dengan membangun banyak pohon keputusan dan akan menghasilkan prediksi [5].

Kelebihan dari algoritma Random Forest adalah algoritma ini dapat menangani dan membuat model prediksi dari dataset yang memiliki volume besar [6]. Selain itu, algoritma ini juga dapat menangani data kontinu, data kategorikal, data sparse, dan data yang memiliki kecenderungan [7].

Kekurangan dari algoritma Random Forest adalah apabila terdapat data yang hilang, maka harus ditangani terlebih dahulu sebelum algoritma ini diaplikasikan [7]. Kemudian pengaruh dari hiperparameter pada algoritma ini dapat membingungkan [8].

#### Boosting
Algoritma Boosting merupakan algoritma machine learning yang memanfaatkan klasifikator lemah untuk pembelajaran kontinu sehingga dapat menghasilkan klasifikator yang kuat [9]. 

Kelebihan dari Algoritma Boosting adalah dapat meningkatkan nilai akurasi dengan cara memperkecil tingkat error yang terdapat di klasifikator lemah [10].

Kekurangan dari Algoritma Boosting adalah sulit untuk menentukan jumlah klasifikator lemah, nilai akurasi dapat menurun apabila data yang digunakan tidak seimbang, memakan waktu, dan sensitif terhadap data abnormal [11].

## Evaluasi Model
Pada bagian ini, evaluasi model diakukan dengan menggunakan metrik *Mean Squared Error (MSE)*. Metrik ini akan menghitung jumlah selisih kuadrat dari rata-rata nilai sebenarnya dengan nilai prediksi. Persamaan *MSE* dirumuskan sebagai berikut:

$$ MSE = {1 \over N} \sum_{i=1}^{N}(y_i - ypred_i)^2 $$

Keterangan:
- N = jumlah dataset
- yi = nilai sebenarnya
- y_pred = nilai prediksi

Hasil dari evaluasi setiap model dengan menggunakan metrik *MSE* adalah sebagai berikut:

Tabel 5. Hasil evaluasi setiap model menggunakan metrik *MSE*
|index|train|test|
|---|---|---|
|KNN|0\.00012999528005034613|0\.00014686714824120603|
|RF|6\.564873652971358e-05|0\.00015558030895626248|
|Boosting|0\.00013823843590799224|0\.00012509991577759657|

Kemudian hasil di atas ditampilkan menggunakan *bar chart* sebagai berikut

![plot_mse](https://raw.githubusercontent.com/fadiyahsutopo/LaporanProyekMLT1-PredictiveAnalytics/main/img/plot_mse.png)

Gambar 12. Diagram hasil evaluasi setiap model menggunakan metrik *MSE*

Selanjutnya dilakukan prediksi menggunakan data *test* dan memperoleh hasil sebagai berikut

Tabel 6. Hasil prediksi setiap model menggunakan data *test*
|index|y\_true|prediksi\_KNN|prediksi\_RF|prediksi\_Boosting|
|---|---|---|---|---|
|327|0|0\.43|0\.0|0\.08|

Berdasarkan hasil pengujian, terlihat bahwa algoritma *Random Forest* memberikan hasil yang mendekati y_true atau nilai aktual.

## Conclusion

Berdasarkan penjelasan di atas, kesimpulan dari laporan ini adalah:
- Faktor yang memengaruhi pembelian asuransi perjalanan adalah jenis sektor pekerjaan, jumlah frekuensi penerbangan, dan pernah bepergian ke luar negeri.
- Di antara ketiga algoritma *machine learning* yang digunakan untuk melakukan pengujian, algoritma *Random Forest* memberikan hasil prediksi yang mendekati nilai aktual. dalam memberikan prediksi mengenai pembelian asuransi perjalanan.

## References
[1]	Badan Pusat Statistik, “Perkembangan Pariwisata dan Transportasi Nasional Juni 2023,” Jakarta, 2023.

[2]	J. W. Przybytniowski, “SERVQUAL METHOD IN STUDYING SERVICE QUALITY OF TRAVEL INSURANCE,” Business: Theory and Practice, vol. 24, no. 1, pp. 282–290, Jun. 2023, doi: 10.3846/btp.2023.17406.

[3]	B. Mahesh, “Machine Learning Algorithms - A Review,” International Journal of Science and Research (IJSR), vol. 9, no. 1, Jan. 2020.

[4]	S. Uddin, I. Haque, H. Lu, M. A. Moni, and E. Gide, “Comparative performance analysis of K-nearest neighbour (KNN) algorithm and its different variants for disease prediction,” Sci Rep, vol. 12, no. 1, p. 6256, Apr. 2022, doi: 10.1038/s41598-022-10358-x.

[5]	L. Zhu, D. Qiu, D. Ergu, C. Ying, and K. Liu, “A study on predicting loan default based on the random forest algorithm,” Procedia Comput Sci, vol. 162, pp. 503–513, 2019, doi: 10.1016/j.procs.2019.12.017.

[6]	J. L. Speiser, M. E. Miller, J. Tooze, and E. Ip, “A comparison of random forest variable selection methods for classification prediction modeling,” Expert Syst Appl, vol. 134, pp. 93–101, Nov. 2019, doi: 10.1016/j.eswa.2019.05.028.

[7]	T. D. Buskirk, “Surveying the Forests and Sampling the Trees: An overview of Classification and Regression Trees and Random Forests with applications in Survey Research,” Surv Pract, vol. 11, no. 1, pp. 1–13, Jan. 2018, doi: 10.29115/SP-2018-0003.

[8]	Y. Ao, H. Li, L. Zhu, S. Ali, and Z. Yang, “The linear random forest algorithm and its advantages in machine learning assisted logging regression modeling,” J Pet Sci Eng, vol. 174, pp. 776–789, Mar. 2019, doi: 10.1016/j.petrol.2018.11.067.

[9]	P. Chen and C. Pan, “Diabetes classification model based on boosting algorithms,” BMC Bioinformatics, vol. 19, no. 1, p. 109, Dec. 2018, doi: 10.1186/s12859-018-2090-9.

[10]	G. Abdurrahman, “Klasifikasi Penyakit Diabetes Melitus Menggunakan Adaboost Classifier,” JUSTINDO (Jurnal Sistem dan Teknologi Informasi Indonesia), vol. 7, no. 1, pp. 59–66, Mar. 2022, doi: 10.32528/justindo.v7i1.4949.

[11]	J. Yang, C. Zhao, H. Yu, and H. Chen, “Use GBDT to Predict the Stock Market,” Procedia Comput Sci, vol. 174, pp. 161–171, 2020, doi: 10.1016/j.procs.2020.06.071.
