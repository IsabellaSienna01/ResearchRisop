# Dokumentasi dan program modifikasi

Diperbarui **2 Oktober 2026**. Folder yang sudah digunakan proyek ini bernama **`research/modifications/`** (jamak). Inilah folder modifikasi yang dimaksud; tidak dibuat salinan `modification/` agar kode dan dokumen tetap satu tempat.

**Untuk mengikuti satu soal yang sama pada ketiga algoritma, mulai dari [contoh soal bersama](#contoh-soal-bersama).** Bagian 6 pada setiap dokumen menunjukkan semua iterasi dengan angka. Jalankan `python -m research.modifications.demo --problem L05_Example1` untuk mencocokkan hasil ketiganya pada soal tersebut.

Langkah ketiga rancangan sebelumnya tersedia di [bagian 31 laporan utama](../report/research_report.md#31-detailed-proposed-modifications). Sekarang masing-masing mempunyai dokumen terpisah:

| Dokumen | Nama varian dalam kode | Isi |
|---|---|---|
| [VAM dua kandidat](vam_top2_rollout.md) | `VAM_top2_rollout` | Baseline, pembentukan kandidat yang tepat, rumus completion, pseudocode, referensi, status kebaruan, hasil, perintah |
| [THP dua kandidat](thp_top2_rollout.md) | `THP_top2_rollout` | Perbedaan dua tingkat penalti asli dengan dua sel eksperimen; keputusan yang berubah dan contoh manual |
| [MRM pilihan orientasi](mrm_orientation_ensemble.md) | `MRM_orientation_ensemble` | Tiga konstruksi lengkap, aturan dummy/seri, bukti non-worsening sederhana, keterbatasan benchmark |

## Apakah original?

**Kode Python dan spesifikasi eksperimen dibuat dalam proyek ini. Itu tidak membuktikan bahwa ide algoritmanya baru.** Ketiganya diklasifikasikan sebagai **C: kombinasi/adaptasi ide yang sudah ada**, menurut klasifikasi audit kebaruan. Kode ini bukan kode resmi penulis paper dan bukan reproduksi suatu paper yang menamai persis ketiga varian tersebut.

VAM/THP memadukan baseline dan pembatasan kandidat dengan prinsip heuristic completion/rollout. MRM memilih biaya terbaik dari konstruksi orientasi yang berkaitan dengan keluarga metode rentang terdahulu. Referensi langsung, referensi konsep, dan pilihan implementasi proyek dipisahkan dalam setiap dokumen. Pernyataan yang dapat dipertanggungjawabkan adalah: **kecocokan persis belum ditemukan pada literatur yang sudah diperiksa; kebaruan belum ditetapkan**. Hasil eksperimen yang baik tidak membuktikan novelty.

## Program yang sudah dapat dijalankan

- [variants.py](variants.py): implementasi 24 varian; fungsi `solve_variant(C, s, d, name, trace=False)` dan daftar `VARIANTS`.
- [__init__.py](__init__.py): menyediakan impor `VARIANTS` dan `solve_variant`.
- [demo.py](demo.py): menjalankan contoh untuk tiga varian terpilih, menghitung baseline dan optimum pembanding, lalu menampilkan hasil. Tidak mengubah CSV penelitian.
- [worked_example.py](worked_example.py): memeriksa setiap perhitungan pada soal bersama dan membangun ulang bagian contoh bertanda pada keempat Markdown serta JSON buktinya.

Jalankan dari `C:\Users\iss5i\Documents\Risop`, bukan dari dalam folder `research`:

```powershell
python -m research.modifications.demo
python -m research.modifications.demo --method vam --trace
python -m research.modifications.demo --method thp --problem L05_Example2
python -m research.modifications.demo --method mrm --json
python -m research.modifications.demo --list-problems
```

Default tanpa argumen menghasilkan:

| Varian | Input default | Baseline | Modifikasi | Optimum |
|---|---|---:|---:|---:|
| VAM top-2 | L05_Example1 | 1095 | 985 | 985 |
| THP top-2 | L05_Example1 | 1045 | 985 | 985 |
| MRM ensemble | E01_Example1 | 3710 | 3460 | 3460 |

Default MRM sengaja memakai benchmark lintas-paper yang tercatat di laporan. Pada contoh itu, 3710 merupakan biaya MRM yang **kita hitung**, bukan biaya MRM yang dilaporkan Hosseini 2017. `--problem` dapat memilih salah satu dari 86 ID mentah pada `benchmarks.json`; sepuluh kemunculan suplemen JHM tidak masuk daftar demo ini. `--json` mencetak hasil lengkap ke terminal; `--trace` menambahkan jejak. Indeks sel pada JSON mulai dari 0.

Dependensi tersedia di [requirements.txt](../requirements.txt). Jika lingkungan Python belum memilikinya, instal dengan `python -m pip install -r research/requirements.txt`. Instalasi bukan bagian yang dilakukan otomatis oleh demo. Untuk memakai data sendiri, fungsi Python menerima matriks dan margin langsung:

```python
from research.modifications import solve_variant

C = [[6,3,1,4], [7,6,2,1], [10,4,5,9], [7,7,7,3]]
s = [50,55,75,60]
d = [90,65,30,55]
hasil = solve_variant(C, s, d, "THP_top2_rollout", trace=True)
print(hasil["cost"])        # 985.0
print(hasil["allocation"])  # matriks pengiriman akhir
```

Input berupa biaya hingga dan nonnegatif, supply/demand nonnegatif, dan dimensi konsisten. Ketidakseimbangan ditangani dengan dummy biaya nol. Itu asumsi pemodelan, bukan harga kekurangan pasokan untuk semua aplikasi. Dukungan alokasi diperiksa bebas siklus; degenerasi dilengkapi dengan sel basis nol. Hasil mencakup `cost`, `allocation`, `feasible`, `basic`, `degenerate`, `basis`, `dummy`, dan `trace`. MRM juga mengembalikan `orientation` (0=baris, 1=kolom). Biaya selalu memakai matriks biaya asli.

Untuk seluruh benchmark, gunakan skrip yang sudah ada:

```powershell
python -m research.experiments.run_modifications
python -m research.experiments.run_modifications --random
python -m research.experiments.summarize
```

Dua perintah pertama menjalankan **semua 24 variasi**, bukan hanya shortlist, dan menulis ulang CSV terkait. Perintah kedua juga membentuk ulang 300 input dari seed yang sama. Untuk sekadar mempelajari tiga contoh, cukup jalankan demo. [Panduan folder](../STRUKTUR_FOLDER.md) menjelaskan aliran data dan semua artefak.

<!-- BEGIN SHARED WORKED EXAMPLE -->
## Contoh soal bersama

**Ketiga dokumen kini memakai L05 Example 1 yang sama**, agar perbedaan keputusan terlihat pada matriks identik. Ini soal dari paper THP lokal, [Amaliah et al. (2021)](https://doi.org/10.1109/ICTS52701.2021.9608005). Masing-masing dokumen memuat tableau setiap iterasi, penjelasan seri, pembaruan margin, matriks akhir dan verifikasi optimum, seperti penyajian contoh numerik dalam paper.

| Sumber | D1 | D2 | D3 | D4 | Supply |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 |
| S2 | 7 | 6 | 2 | 1 | 55 |
| S3 | 10 | 4 | 5 | 9 | 75 |
| S4 | 7 | 7 | 7 | 3 | 60 |
| Demand | 90 | 65 | 30 | 55 | 240 |

Supply dan demand masing-masing 240, sehingga tidak memakai dummy. Indeks berikut mulai 1. Setiap algoritma dimulai lagi dari tabel awal, bukan melanjutkan hasil algoritma lain.

| Algoritma | Langkah keputusan pada soal ini | Hasil |
| --- | --- | --- |
| [VAM](vam_top2_rollout.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai) | 1. Penalti dua minimum → calon x44 dan x13. 2. Completion memberi 1095 dan 985 → pilih x13=30. 3. Ulangi evaluasi: x24=55, x32=65, x11=20, x41=60, x31=10. | 1095 → 985 |
| [THP](thp_top2_rollout.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai) | 1. Dua tingkat rentang tertinggi menghasilkan calon x13 dan x24; F seri 1045 → x13=30. 2. Pada iterasi berikutnya F(x24)=1015, F(x32)=955 → x32=65. 3. Lanjut x24=55, x31=10, x11=20, x41=60. | 1045 → 985 |
| [MRM](mrm_orientation_ensemble.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai) | 1. Dari awal jalankan default (kolom): 1045. 2. Ulangi dari awal dengan rows: 985. 3. Ulangi dari awal dengan columns: 1045. 4. Pilih seluruh alokasi rows. | 1045 → 985 |

Penjelasan panjang VAM/THP menunjukkan **setiap kandidat dan seluruh urutan completion sementara**; penjelasan MRM menunjukkan **setiap langkah kedua orientasi**, termasuk alokasi nol untuk eliminasi. Pada VAM/THP, F mengecualikan biaya yang sudah dikomit; biaya itu ditampilkan sebagai B agar angka 955 tidak keliru dibaca sebagai total akhir 985.

Ketiganya menghasilkan matriks yang sama:

| Alokasi | D1 | D2 | D3 | D4 | Jumlah baris | Supply |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 20 | 0 | 30 | 0 | 50 | 50 |
| S2 | 0 | 0 | 0 | 55 | 55 | 55 |
| S3 | 10 | 65 | 0 | 0 | 75 | 75 |
| S4 | 60 | 0 | 0 | 0 | 60 | 60 |
| Jumlah kolom | 90 | 65 | 30 | 55 | 240 | — |
| Demand | 90 | 65 | 30 | 55 | 240 | — |

`Z=20×6+30×1+55×1+10×10+65×4+60×7=985`, sama dengan optimum LP dan batas dual yang ditunjukkan di setiap dokumen. Biaya MRM di sini dihitung proyek, bukan klaim MRM dari paper THP.

Jalankan semuanya pada soal bersama tersebut:

```powershell
python -m research.modifications.demo --problem L05_Example1
python -m research.modifications.demo --problem L05_Example1 --trace --json
```

Angka tableau, setiap completion, dan hasil akhir dicocokkan dengan fungsi program. Bukti terstruktur: [worked_example_L05_Example1.json](../results/worked_example_L05_Example1.json). Untuk membangun ulang bagian contoh pada ketiga Markdown dan README:

```powershell
python -m research.modifications.worked_example
```

Perintah tersebut memperbarui bagian contoh yang diberi penanda dan JSON contoh saja; aturan algoritma serta CSV suite utama tetap sama.
<!-- END SHARED WORKED EXAMPLE -->
