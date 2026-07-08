# 🏥 Sistem-Prediksi-Kesehatan

Sistem prediksi tingkat kesehatan individu berbasis *Machine Learning* menggunakan metode *Logistic Regression* berdasarkan pola gaya hidup.

---

## 📝 Deskripsi Sistem
Sistem ini merupakan aplikasi berbasis *Artificial Intelligence* (AI) yang digunakan untuk memprediksi tingkat kesehatan individu berdasarkan pola gaya hidup pengguna. 

Sistem bekerja dengan menerima beberapa data masukan (*input*) dari pengguna seperti usia, berat badan, tinggi badan, pola tidur, kebiasaan alkohol, dan kebiasaan merokok. Data tersebut kemudian diproses menggunakan metode *Machine Learning Logistic Regression* untuk menghasilkan prediksi berupa:
* **Kategori kesehatan pengguna:** Sehat, Kurang Sehat, atau Tidak Sehat.
* **Skor kesehatan:** Ditampilkan dalam bentuk persentase atau skala tertentu.

**Tujuan Utama:** Membantu pengguna mengetahui kondisi kesehatan awal secara sederhana berdasarkan kebiasaan hidup sehari-hari sehingga dapat meningkatkan kesadaran terhadap pentingnya pola hidup sehat.

---

## 🚀 Langkah-Langkah Definisi Masalah dalam AI

### A. Identifikasi Masalah
Banyak individu kurang menyadari kondisi kesehatannya karena sulit melakukan pemeriksaan kesehatan secara rutin. Oleh karena itu, diperlukan sistem yang mampu memberikan prediksi kesehatan awal secara cepat, mudah, dan sederhana.

### B. Menentukan Tujuan Sistem
* Memprediksi tingkat kesehatan individu secara dini.
* Membantu pengguna memahami kondisi kesehatannya secara mandiri.
* Memberikan hasil prediksi objektif berdasarkan data gaya hidup.

### C. Menentukan Input dan Output
* **Input Sistem:**
  * Usia
  * Berat badan
  * Tinggi badan
  * Durasi tidur
  * Olahraga
* **Output Sistem:**
  * **Kategori:** 1. Sehat, 2. Kurang sehat, 3. Tidak sehat.
  * **Skor Kesehatan:** Berupa nilai kepastian/probabilitas.

### D. Menentukan Metode AI
Metode yang digunakan adalah **Machine Learning – Logistic Regression**.
> **Alasan pemilihan:** Metode ini sangat cocok untuk kasus klasifikasi data, strukturnya sederhana, mudah diimplementasikan, serta memiliki akurasi yang baik untuk karakteristik data yang sederhana.

### E. Pengumpulan Dataset
Dataset diperoleh dan digabungkan dari dua sumber utama:
1. Platform kompetisi sains data (**Kaggle**).
2. Penyebaran **Kuesioner Pengguna** secara mandiri.

---

## 🧠 Karakteristik Pengetahuan Terkait Aplikasi AI

Sistem ini mengolah tiga karakteristik pengetahuan utama:

### 1. Pengetahuan Bersifat Numerik
Data kesehatan kuantitatif berupa angka, meliputi:
* Umur
* BMI (*Body Mass Index* - dihitung otomatis dari rumus berat badan dan tinggi badan)
* Durasi tidur
* Frekuensi konsumsi alkohol
* Intensitas kebiasaan merokok

### 2. Pengetahuan Bersifat Klasifikasi
Sistem secara cerdas mengelompokkan pengguna ke dalam salah satu dari tiga kategori hasil:
* 🟢 **Sehat**
* 🟡 **Kurang Sehat**
* 🔴 **Tidak Sehat**

### 3. Pengetahuan Probabilistik
Hasil akhir dari algoritma *Logistic Regression* berupa nilai peluang (probabilitas) yang merepresentasikan tingkat keyakinan sistem.
* *Contoh:* Kemungkinan Sehat = **85%** | Kemungkinan Tidak Sehat = **15%**

---

## 📊 Representasi Pengetahuan

Sistem ini menggunakan model **Tabel Keputusan (Decision Table)** sebagai representasi pengetahuannya. 

Pemilihan model ini didasarkan karena sistem menggunakan kombinasi atribut numerik dan kategorikal yang diproses oleh *Logistic Regression*. Tabel keputusan mempermudah visualisasi dan pemetaan hubungan logis antara variasi data masukan (*input*) dengan hasil akhir klasifikasi kesehatan (*output*).
