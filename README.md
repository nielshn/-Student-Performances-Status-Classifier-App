# 🎓 Proyek Akhir: Student Academic Status Prediction

## 🧠 Business Understanding

Lembaga pendidikan tinggi menghadapi tantangan dalam menurunkan angka dropout dan meningkatkan tingkat kelulusan mahasiswa. Untuk itu, diperlukan pendekatan berbasis data yang dapat membantu mengidentifikasi mahasiswa yang berisiko gagal sejak awal masa studi.

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

- **URL (Streamlit Cloud):** [Link Project Streamlit](https://studentsperformancesclassifier-niels.streamlit.app/)
  ![Student Status Classifier App](image.png)

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

Berdasarkan analisis dan hasil modeling, ditemukan bahwa:

- Mahasiswa dari jalur studi tertentu seperti _Technology_ dan _Management_ memiliki tingkat dropout lebih tinggi.
- Faktor sosial ekonomi seperti tingkat pendapatan dan latar belakang pendidikan orang tua memiliki korelasi kuat dengan performa akademik.
- Mahasiswa dengan skor awal rendah pada mata kuliah dasar lebih berisiko mengalami dropout.
- Model prediksi memberikan akurasi tinggi dan membantu memetakan risiko akademik mahasiswa sejak awal semester.

Dengan sistem ini, pihak kampus dapat:

- Mengantisipasi potensi kegagalan akademik lebih dini
- Memberikan intervensi akademik secara terarah (mentoring, remedial, beasiswa)
- Menyusun kebijakan akademik berdasarkan data, bukan asumsi

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
