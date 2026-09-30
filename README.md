# Tugas Pengganti IT Incubation – SDG 4

## Judul
**Prediksi Kelulusan Siswa Menggunakan Logistic Regression untuk Mendukung SDG 4 – Pendidikan Berkualitas**

## Kesesuaian dengan ketentuan tugas
| Ketentuan | Implementasi |
|---|---|
| 1 permasalahan SDGs | SDG 4 – Pendidikan Berkualitas |
| 1 task | Klasifikasi |
| 1 algoritma/model | Logistic Regression |
| Random Forest | Tidak digunakan |
| Preprocessing | Mapping target, train-test split, StandardScaler |
| Training | Logistic Regression pada data training |
| Evaluasi | Accuracy, classification report, confusion matrix |
| Deployment | Streamlit |

## Dataset
`dataset_siswa_sdg4.csv` berisi 150 data simulasi. Fitur:
- Kehadiran_Persen
- Jam_Belajar_per_Hari
- Nilai_Tugas
- Nilai_Ujian

Target:
- `Ya` = 1
- `Tidak` = 0

**Catatan:** data merupakan simulasi untuk pembelajaran, bukan data siswa nyata.

## Hasil evaluasi
Dengan `test_size=0.20`, `random_state=42`, dan `stratify=y`:
- Data training: 120
- Data testing: 30
- Accuracy: **80.00%**
- Confusion matrix:
  ```
  [[11, 4],
   [ 2,13]]
  ```

Classification report:
- Tidak Lulus — precision 84.62%, recall 73.33%, F1 78.57%
- Lulus — precision 76.47%, recall 86.67%, F1 81.25%

## Menjalankan notebook
1. Buka `Tugas_IT_Incubation_SDG4.ipynb` di Google Colab.
2. Upload `dataset_siswa_sdg4.csv` jika diminta.
3. Jalankan semua sel dari atas sampai bawah.
4. Model dan scaler akan tersimpan sebagai file `.pkl`.

## Menjalankan Streamlit di komputer
Pastikan berada di folder project, lalu:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Aplikasi biasanya dibuka pada alamat lokal yang ditampilkan oleh Streamlit.

## Deployment
Untuk memperoleh **link aplikasi online**, upload seluruh file project ke GitHub lalu deploy `app.py` menggunakan Streamlit Community Cloud. Link online tidak dapat dibuat hanya dari file ZIP; proses deployment harus dilakukan pada akun hosting.
