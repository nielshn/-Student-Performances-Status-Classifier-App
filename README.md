# 🎓 Proyek Akhir: Student Academic Status Prediction

## 🧠 Business Understanding

Business Understanding merupakan tahap awal yang krusial dalam proses data science karena menjadi dasar pemahaman konteks bisnis dan tujuan proyek.  
Lembaga pendidikan tinggi dihadapkan pada tantangan serius terkait tingginya angka mahasiswa yang mengalami dropout (putus studi) dan rendahnya tingkat kelulusan tepat waktu.  
Permasalahan ini berdampak langsung pada reputasi institusi, efisiensi operasional, serta alokasi sumber daya kampus. Jika tidak ditangani, institusi akan kesulitan dalam merancang kebijakan akademik yang efektif, kehilangan potensi lulusan berkualitas, dan menghadapi tekanan dari regulator maupun masyarakat.

**Mengapa isu ini penting?**

- Dropout menyebabkan pemborosan sumber daya (waktu, biaya, tenaga pengajar).
- Mahasiswa yang gagal lulus tepat waktu dapat menurunkan akreditasi dan kepercayaan publik.
- Institusi membutuhkan sistem prediksi berbasis data untuk mengidentifikasi mahasiswa berisiko sejak awal, sehingga intervensi dapat dilakukan secara proaktif.

**Dampak bisnis jika masalah tidak ditangani:**

- Penurunan jumlah lulusan dan reputasi kampus.
- Efisiensi operasional menurun akibat sumber daya yang tidak termanfaatkan optimal.
- Kesulitan dalam perencanaan dan pengambilan keputusan berbasis data.

### 🌟 Permasalahan Bisnis

- Tingginya tingkat dropout menyebabkan efisiensi operasional menurun dan reputasi institusi terganggu.
- Sulit mengidentifikasi mahasiswa yang berisiko sejak awal masa kuliah.
- Pimpinan akademik membutuhkan insight berbasis data untuk merancang kebijakan akademik yang lebih adaptif.

### 📌 Cakupan Proyek

- Analisis data akademik dan sosial ekonomi mahasiswa.
- Membangun model klasifikasi status mahasiswa: **Dropout**, **Enrolled**, atau **Graduate**.
- Menyediakan dashboard interaktif untuk visualisasi insight dan prediksi status.
- Deployment sistem prediksi untuk digunakan oleh pihak institusi pendidikan.

## ⚙️ Persiapan

**Sumber data**: Dataset Students Performance yang mencakup 4424 baris dan 37 fitur, terdiri dari informasi akademik awal, kondisi demografis, dan status akhir mahasiswa.

### Setup Environment

**Opsi 1: Menggunakan Anaconda**

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

**Opsi 2: Menggunakan pipenv**

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

**Opsi 3: Menggunakan pip langsung**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Cara Menjalankan Skrip Prediksi Python (.py)

File utama untuk prediksi adalah `predict.py`.  
Jalankan perintah berikut di terminal (pastikan sudah berada di folder project dan environment sudah aktif):

```bash
python predict.py --input data/sample_input.csv --output hasil_prediksi.csv
```

- `--input` : path ke file csv yang ingin diprediksi
- `--output` : path file hasil prediksi

Contoh:

```bash
python predict.py --input data/employee_test.csv --output data/prediksi_attrition.csv
```

## 📊 Business Dashboard

Dashboard interaktif dibangun menggunakan **Streamlit**, menampilkan:

- Distribusi status akademik berdasarkan usia, jenis kelamin, dan jalur studi.
- Perbandingan tingkat dropout dan kelulusan per program studi.
- Analisis korelasi antara status akhir dengan faktor sosial ekonomi (pendapatan, pendidikan orang tua).
- Visualisasi prediksi status mahasiswa baru berdasarkan input pengguna.

🔑 **Akses Dashboard**:

- **URL**: [http://localhost:3000](http://localhost:3000)
- **Email**: [root@mail.com](mailto:root@mail.com)
- **Password**: root123

### 📄 Ekspor Dashboard

Jika menggunakan Docker:

```bash
docker export metabase > metabase_dashboard_export.tar
```

## 🤖 Streamlit ML Prototype

Solusi machine learning telah di-deploy menggunakan **Streamlit** dalam file `app.py`.

### Menjalankan secara lokal:

```bash
streamlit run app.py
```

Akan terbuka di browser: [http://localhost:8501/](http://localhost:8501/)

### Akses versi online (Streamlit Cloud)

🔗 [Student Status Classifier App](https://studentsperformancesclassifier-niels.streamlit.app/)
![Student Status Classifier App](image.png)

### Fitur Aplikasi:

- Upload CSV data mahasiswa
- Prediksi status akademik (Dropout / Graduate / Enrolled)
- Tabel + visualisasi distribusi prediksi
- Export hasil ke file .csv

---

## 🤖 Modeling & Evaluation

Tiga model utama digunakan dan dibandingkan pada data uji:

### 1. Random Forest

| Class        | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| 0 (Dropout)  | 0.84      | 0.71   | 0.77     | 284     |
| 1 (Enrolled) | 0.81      | 0.90   | 0.86     | 442     |
| 2 (Graduate) | 0.47      | 0.45   | 0.46     | 159     |

- **Accuracy:** 0.76
- **Macro F1-score:** 0.69
- **Weighted F1-score:** 0.76

---

### 2. XGBoost

| Class        | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| 0 (Dropout)  | 0.83      | 0.73   | 0.78     | 284     |
| 1 (Enrolled) | 0.81      | 0.92   | 0.86     | 442     |
| 2 (Graduate) | 0.52      | 0.42   | 0.46     | 159     |

- **Accuracy:** 0.77
- **Macro F1-score:** 0.70
- **Weighted F1-score:** 0.76

---

### 3. CatBoost

| Class        | Precision | Recall | F1-score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| 0 (Dropout)  | 0.81      | 0.71   | 0.76     | 284     |
| 1 (Enrolled) | 0.82      | 0.91   | 0.86     | 442     |
| 2 (Graduate) | 0.50      | 0.45   | 0.47     | 159     |

- **Accuracy:** 0.76
- **Macro F1-score:** 0.70
- **Weighted F1-score:** 0.76

---

> **Catatan:**  
> Model **XGBoost** menunjukkan performa terbaik secara keseluruhan pada data uji, terutama pada kelas mayoritas (Enrolled dan Dropout), meskipun performa pada kelas Graduate masih perlu ditingkatkan. Model ini dipilih untuk deployment karena kombinasi akurasi, macro F1-score, dan ketahanannya terhadap data tidak seimbang.

---

## ✅ Conclusion

Berdasarkan analisis dan hasil modeling, ditemukan beberapa temuan utama terkait karakteristik mahasiswa yang berpotensi dropout dan insight bagi institusi pendidikan:

- **Karakteristik Mahasiswa Dropout:**  
  Mahasiswa yang berpotensi dropout umumnya memiliki nilai akademik rendah pada semester awal, tingkat kehadiran yang buruk, serta berasal dari latar belakang sosial ekonomi yang kurang mendukung (misal: pendapatan keluarga rendah, pendidikan orang tua rendah, atau tidak menerima beasiswa).
- **Faktor Risiko:**  
  Program studi tertentu, mahasiswa laki-laki, dan mereka yang tidak aktif dalam kegiatan akademik cenderung memiliki risiko dropout lebih tinggi.
- **Alasan Dropout:**  
  Selain faktor akademik, tekanan ekonomi dan kurangnya dukungan sosial menjadi alasan utama mahasiswa tidak melanjutkan studi.
- **Manfaat Model:**  
  Model prediksi ini dapat digunakan institusi untuk mengidentifikasi mahasiswa berisiko sejak awal semester, sehingga intervensi seperti mentoring, remedial, atau bantuan finansial dapat diberikan secara tepat sasaran.
- **Dampak Bisnis:**  
  Dengan sistem ini, kampus dapat meningkatkan tingkat kelulusan, menurunkan angka dropout, dan memperbaiki reputasi institusi melalui kebijakan berbasis data.

## 💡 Rekomendasi Action Items

- **Pemantauan Awal Mahasiswa Baru:** Gunakan model untuk mendeteksi mahasiswa yang berisiko dropout sejak awal dan beri dukungan personal.
- **Program Intervensi Berdasarkan Jalur Studi:** Fokuskan sumber daya pendampingan pada program studi dengan risiko dropout tinggi.
- **Perbaikan Kurikulum dan Metode Evaluasi:** Lakukan review pada mata kuliah yang memiliki korelasi kuat dengan kegagalan.
- **Dukungan Sosial dan Finansial:** Sediakan program bantuan untuk mahasiswa dengan kondisi sosial ekonomi rendah.
- **Monitoring Berkelanjutan:** Lanjutkan pengumpulan data untuk fine-tuning model dan peningkatan sistem.

## 🚀 Deployment

Model final XGBoost disimpan dalam format `.pkl` dan digunakan oleh aplikasi Streamlit untuk prediksi real-time berdasarkan input pengguna.

## 📂 Project Structure

```bash
├── data/                 # Dataset CSV
├── notebook/             # Notebook eksplorasi dan modeling
├── model/                # Model terlatih (joblib/pkl)
├── predict.py            # Skrip prediksi batch
├── app/                  # File dashboard Streamlit
├── requirements.txt      # Dependencies
└── README.md             # Laporan ini
```

## 👥 Author

Daniel Siahaan - Machine Learning @ LaskarAi 2025 - Student Academic Status Classification Project
