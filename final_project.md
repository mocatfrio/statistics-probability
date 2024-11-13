# Case-based Final Project
## Analisis Faktor-faktor yang Mempengaruhi Kepuasan Pengguna Pada Produk atau Layanan Teknologi Informasi

### Deskripsi Project

Mahasiswa diminta melakukan analisis data untuk memahami faktor-faktor yang mempengaruhi tingkat kepuasan pengguna pada suatu produk ataupun layanan teknologi informasi, misalnya aplikasi, layanan online, atau sistem informasi. Data yang digunakan dapat mengambil dari *Open Data Sources* seperti Kaggle. 

### Tujuan Project

1. Mengaplikasikan konsep statistika, probabilitas, dan analisis data untuk memahami kepuasan pengguna.
2. Menganalisis variabel random dan distribusi probabilitas pada data kepuasan pengguna.
3. Melakukan uji hipotesis dan perbandingan antara kelompok pengguna yang berbeda.
4. Menerapkan regresi linear sederhana dan berganda untuk memprediksi kepuasan pengguna berdasarkan faktor-faktor yang relevan.

## **Tahapan Pengerjaan Project**

### Preparation

1. Bentuklah kelompok dengan **maksimal 4 anggota** (boleh sama dengan kelompok pada Project 1).
2. Carilah dataset yang relevan dengan topik Final Project dari Kaggle atau Open Data Sources lainnya. Setelah itu, masukkan nama anggota kelompok dan link Kaggle pada link berikut.
  <a href="https://docs.google.com/spreadsheets/d/1zV1VG8xux2OGQLea_9F23PWHl3GLSvRtu6kEQpFYgdY/edit?usp=sharin" style="background-color: #4169E1; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;">Spreadsheet Kelompok dan Link Kaggle</a>
3. Setiap kelompok tidak diperkenankan menggunakan dataset yang sama.
4. Buatlah repositori GitHub (boleh menggunakan repo Project 1, tetapi beda folder) dari sekarang untuk mengunggah progress pengerjaan Final Project setiap minggunya.


### Week 10: Random Variable and Probability Distribution
#### Tujuan
Memahami distribusi variabel acak untuk setiap variabel dalam data 

#### Langkah-langkah
1. Deskriptif Statistik: Tampilkan statistik deskriptif untuk setiap variabel.
2. Distribusi Probabilitas: Lakukan uji distribusi pada setiap variabel untuk mengamati apakah variabel-variabel tersebut mengikuti distribusi tertentu (misalnya, normal, uniform, dll). Anda dapat menggunakan visualisasi histogram dan density plot, atau menerapkan metode uji statistik yang sesuai.
3. Menghitung Probabilitas: Hitung probabilitas kejadian tertentu, seperti "pelanggan memiliki kepuasan di atas 4".

### Week 11: Sampling and Sampling Distribution
#### Tujuan
Menggunakan teknik sampling untuk membuat distribusi sampling dari rata-rata kepuasan pelanggan dan melihat sebarannya.

#### Langkah-langkah
1. Sampling: Buatlah beberapa sampel acak dari data.
2. Distribusi Sampling: Hitung mean dari setiap sampel dan visualisasikan distribusi sampling mean ini.
3. Interval Kepercayaan: Buat interval kepercayaan 95% untuk rata-rata kepuasan.

### Week 12: Hypothesis Testing
#### Tujuan
Melakukan uji hipotesis pada mean kepuasan pengguna.

#### Langkah-langkah
1. Tentukan hipotesis nol (misalnya, mean kepuasan = 3) dan hipotesis alternatif.
2. Uji Z atau Uji T: Pilih uji statistik yang sesuai dan uji hipotesis.
3. Signifikansi: Hitung p-value dan simpulkan.
   
### Week 13: Comparison of Two Populations
#### Tujuan
Membandingkan rata-rata kepuasan pengguna berdasarkan dua kategori berbeda, misalnya pengguna yang berusia di bawah 30 tahun dan yang berusia di atas 30 tahun.

#### Langkah-langkah
1. Bagi Populasi: Buat dua sub-kelompok berdasarkan usia.
2. Uji Dua Populasi: Lakukan uji T untuk membandingkan rata-rata kepuasan kedua kelompok.
   
### Week 14: Analysis of Variance (ANOVA)
#### Tujuan
Menganalisis apakah ada perbedaan signifikan dalam rata-rata kepuasan berdasarkan beberapa kategori (misalnya, tiga kelompok usia: muda, dewasa, dan lanjut usia).

#### Langkah-langkah
1. Kelompokkan Usia: Bagi usia menjadi beberapa kategori.
2. ANOVA: Lakukan ANOVA untuk mengetahui apakah ada perbedaan signifikan antar kelompok.

### Week 15: Simple Linear Regression and Correlation
Mengetahui apakah ada hubungan antara faktor A atau faktor B dengan kepuasan dan seberapa kuat hubungan tersebut.

#### Langkah-langkah
1. Korelasi Pearson: Hitung korelasi Pearson antara variabel.
2. Regresi Linear: Gunakan regresi linear sederhana untuk memprediksi kepuasan berdasarkan faktor A atau faktor B.

### Week 16: Multiple Regression
#### Tujuan
Menentukan apakah lebih dari satu faktor mempengaruhi kepuasan dengan menggunakan regresi berganda.

#### Langkah-langkah
1. Regresi Berganda: Terapkan regresi linear berganda dengan kepuasan sebagai variabel dependen dan kualitas_layanan, harga, serta fitur sebagai variabel independen.
2. Evaluasi Model: Lihat koefisien setiap variabel dan nilai R-squared untuk mengetahui kekuatan prediksi model.

## Contoh Project

[Contoh Final Project](final-project-example/final-project-example.ipynb)