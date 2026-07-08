# 🏥 Sistem Prediksi Tingkat Kesehatan Individu

Sistem prediksi tingkat kesehatan individu berbasis **Machine Learning** menggunakan algoritma **Logistic Regression** berdasarkan indikator gaya hidup dan kondisi fisik pengguna.

---

## 📝 Deskripsi Sistem

Sistem ini merupakan aplikasi berbasis **Artificial Intelligence (AI)** yang digunakan untuk memprediksi kondisi kesehatan seseorang berdasarkan data yang dimasukkan oleh pengguna.

Pengguna mengisi beberapa informasi dasar seperti jenis kelamin, usia, tinggi badan, berat badan, durasi tidur, tingkat aktivitas fisik, dan jumlah langkah harian. Sistem kemudian menghitung **Body Mass Index (BMI)** secara otomatis dari tinggi dan berat badan, kemudian seluruh data diproses menggunakan algoritma **Logistic Regression** untuk menghasilkan prediksi kondisi kesehatan.

### Tujuan Sistem

- Membantu pengguna memperoleh gambaran awal mengenai kondisi kesehatannya.
- Memberikan prediksi berdasarkan pola gaya hidup menggunakan Machine Learning.
- Meningkatkan kesadaran pengguna terhadap pentingnya menjaga pola hidup sehat.

---

## 🚀 Definisi Masalah dalam AI

### A. Identifikasi Masalah

Banyak orang belum memiliki waktu atau akses untuk melakukan pemeriksaan kesehatan secara rutin. Oleh karena itu, diperlukan sebuah sistem yang mampu memberikan prediksi kondisi kesehatan awal secara cepat dan mudah berdasarkan kebiasaan hidup sehari-hari.

### B. Tujuan Sistem

- Mengembangkan sistem prediksi kesehatan berbasis Machine Learning.
- Memberikan hasil prediksi secara otomatis berdasarkan data pengguna.
- Menjadi media edukasi mengenai pengaruh gaya hidup terhadap kesehatan.

### C. Input dan Output Sistem

### Input

- Gender
- Age
- Height
- Weight
- BMI (dihitung otomatis)
- Sleep Duration
- Physical Activity Level
- Daily Steps

### Output

- Hasil prediksi kondisi kesehatan berdasarkan model Logistic Regression.
- Nilai probabilitas (confidence score) dari hasil prediksi.

---

### D. Metode AI

Metode yang digunakan adalah **Machine Learning - Logistic Regression**.

**Alasan pemilihan metode:**

- Cocok untuk permasalahan klasifikasi.
- Mudah diimplementasikan.
- Cepat dalam proses pelatihan maupun prediksi.
- Memiliki performa yang baik untuk dataset dengan karakteristik sederhana hingga menengah.

---

### E. Pengumpulan Dataset

Dataset diperoleh melalui dua sumber utama:

1. Dataset kesehatan dari **Kaggle**.
2. Data tambahan dari **kuesioner** yang disebarkan kepada responden.

---

# 🧠 Karakteristik Pengetahuan

Sistem memanfaatkan beberapa jenis pengetahuan dalam proses prediksi.

## 1. Pengetahuan Numerik

Berupa data yang memiliki nilai numerik, antara lain:

- Usia
- Tinggi badan
- Berat badan
- BMI
- Durasi tidur
- Jumlah langkah harian

## 2. Pengetahuan Kategorikal

Berupa atribut yang memiliki kategori tertentu, seperti:

- Gender
- Physical Activity Level

## 3. Pengetahuan Probabilistik

Logistic Regression menghasilkan nilai probabilitas yang menunjukkan tingkat keyakinan model terhadap hasil prediksi.

Contoh:

Status Kesehatan : Baik

Analisis:
Pola hidup dan pola tidur Anda menunjukkan kondisi yang baik berdasarkan data yang dimasukkan.

Rekomendasi:
• Pertahankan pola tidur
• Tetap aktif berolahraga
• Pertahankan gaya hidup sehat

---

# 📊 Representasi Pengetahuan

Sistem menggunakan **model klasifikasi Logistic Regression** yang mempelajari hubungan antara variabel masukan dengan label kesehatan dari dataset pelatihan.

Untuk mempermudah proses analisis, data direpresentasikan dalam bentuk atribut-atribut terstruktur seperti usia, BMI, aktivitas fisik, durasi tidur, dan jumlah langkah harian. Model kemudian memanfaatkan hubungan antar atribut tersebut untuk menghasilkan prediksi kondisi kesehatan beserta nilai probabilitasnya.
