# Panduan isi folder research

Diperbarui **2 Oktober 2026**. Folder ini menyimpan satu rantai penelitian: **sumber → transkripsi data → implementasi → eksperimen → hasil → analisis**. Baca [kesimpulan berbahasa Indonesia](report/hasil_riset_dan_kesimpulan.md) untuk substansi riset dan [dokumentasi tiga modifikasi](modifications/README.md) untuk algoritma/cara menjalankan.

[FILE_INDEX.md](FILE_INDEX.md) mencantumkan **setiap berkas yang ada**, path, dan kegunaannya, termasuk unduhan mentah, metadata sumber, gambar halaman, dan cache Python. Panduan ini menjelaskan hubungan antarberkas agar daftar panjang tersebut mudah dipahami.

Pengecualian indeks adalah metadata internal Git (`.git/`), konfigurasi alat tersembunyi, dan lingkungan virtual. `.git/` menyimpan riwayat serta konfigurasi version control, bukan sumber/hasil penelitian; isinya tidak diubah atau dimasukkan dalam indeks.

## 1. Struktur besar dan aliran data

```text
research/
├── README.md                 pintu masuk, tautan, perintah reproduksi
├── STRUKTUR_FOLDER.md        panduan yang sedang dibaca
├── FILE_INDEX.md             daftar setiap berkas dan fungsi
├── progress.md              pekerjaan selesai, sengaja dilewati, dan keterbatasan
├── paper_inventory.md       inventaris lima PDF lokal beserta koreksi penemuan data
├── requirements.txt         paket Python yang digunakan
├── *.py                     utilitas unduhan, ekstraksi, dan pembentukan data
├── papers/                  sumber mentah, ekstraksi teks, provenance, gambar audit
├── datasets/                input yang sudah distandardisasi
│   ├── published/           matriks/claims dari paper dan dataset penulis
│   └── generated/           300 matriks acak yang dipakai bersama
├── methods/                 baseline dan kontrak algoritma
├── modifications/           kode varian, tiga dokumen terpisah, demo
├── solver/                  LP untuk optimum pembanding
├── experiments/             pelaksana eksperimen dan pemeriksaan
├── results/                 output komputasi: CSV, JSON, sertifikat, grafik
└── report/                  penjelasan, interpretasi hasil, rekomendasi
```

`papers/` menjawab **“sumber aslinya apa?”**; `datasets/` menjawab **“angka input yang benar-benar diuji apa?”**; `methods/` dan `modifications/` menjawab **“aturan yang dijalankan apa?”**; `results/` menjawab **“hasil komputasinya apa?”**; `report/` menjawab **“apa kesimpulannya dan seberapa kuat buktinya?”**

LP di `solver/` hanya menjadi ground truth. VAM/THP completion memanggil heuristik baseline untuk menghitung sisa biaya, bukan LP. MRM memilih hasil termurah dari konstruksinya sendiri. Karena itu perbandingan terhadap optimum tetap terpisah dari pemilihan heuristik.

## 2. Berkas di root research

| Berkas | Fungsi dan kapan digunakan |
|---|---|
| [README.md](README.md) | Ringkasan navigasi dan perintah umum; mulai di sini |
| [progress.md](progress.md) | Status tiap tahap dan keterbatasan; IHW dilewati, JHM tetap parsial |
| [paper_inventory.md](paper_inventory.md) | Judul, penulis, tahun, DOI, metode, contoh, dan klaim lima PDF yang diberikan pengguna |
| [requirements.txt](requirements.txt) | Daftar dependensi; versi saat eksperimen ada di `results/environment.json` |
| [__init__.py](__init__.py) | Penanda paket Python agar `python -m research...` dapat dipakai; bukan algoritma |
| [extract_local.py](extract_local.py) | Memindai PDF lokal, mengekstrak teks, membentuk manifest; dipakai saat audit sumber |
| [read_text.py](read_text.py) | Menampilkan rentang baris teks dengan nomor baris; alat bantu membaca, tidak menghitung solusi |
| [render_pages.py](render_pages.py) | Mengubah halaman PDF terpilih menjadi gambar untuk memeriksa transkripsi |
| [fetch_source.py](fetch_source.py) | Mengunduh satu sumber yang sudah dipilih ke `papers/external/`, mencatat URL/waktu/hash |
| [prepare_downloads.py](prepare_downloads.py) | Menyusun antrean URL dari halaman sumber yang telah diperoleh |
| [fetch_batch.py](fetch_batch.py) | Mengunduh antrean dan mencatat hasil; tidak menjalankan kode penulis yang diunduh |
| [build_datasets.py](build_datasets.py) | Transkripsi/parsing matriks menjadi JSON, deduplikasi, pencatatan input yang dikeluarkan |
| [extract_claims.py](extract_claims.py) | Memisahkan angka hasil yang diklaim sumber dari matriks input; menyimpan klaim yang belum dapat dicocokkan |
| [document_tree.py](document_tree.py) | Membuat ulang `FILE_INDEX.md` dari berkas yang benar-benar ada; tidak menjalankan eksperimen |

Utilitas ekstraksi/unduhan diperlukan untuk audit sumber atau menambah sumber. Untuk mencoba modifikasi, gunakan demo; tidak perlu mengulang unduhan atau pembentukan dataset.

## 3. papers: sumber dan jejak asal data

| Subfolder/berkas | Isi dan makna |
|---|---|
| [local_manifest.json](papers/local_manifest.json) | Path PDF asli, ukuran, hash SHA-256, jumlah halaman, metadata, dan lokasi ekstraksi |
| `local_text/L01.txt`–`L05.txt` | Ekstraksi lima PDF pengguna: BCE, RBSM, SSM, AIP, THP. Teks tidak menggantikan pemeriksaan tabel PDF |
| `external/` | PDF/HTML/teks dan suplemen yang diunduh dari penerbit/penulis; ID E01, E02, dst. berhubungan dengan inventaris sumber |
| `external/*.source.json` | Provenance untuk berkas dengan nama dasar sama: URL yang diminta/final, waktu pengambilan, hash, ukuran; beberapa memuat informasi TLS/user agent |
| `external/download_queue.json` | Daftar sumber yang dijadwalkan untuk diunduh, bukan bukti semua unduhan berhasil |
| `external/download_outcomes.json` | Hasil antrean: berhasil, sudah ada, atau gagal; sumber yang gagal bisa tidak mempunyai file lokal |
| `external/rbsm_n*.txt`, `rbsm_S*.txt` | Matriks mentah dataset penulis RBSM; label tidak otomatis sama dengan seluruh kasus di paper |
| `external/rbsm_metodeS2new.cpp` | Kode C++ penulis untuk audit perbedaan paper/kode; disimpan, tidak dijadikan executable baseline kita |
| `page_checks/*.png` | Gambar halaman yang dibaca untuk memeriksa angka/rumus. Misalnya `L01_real.png` untuk aplikasi 2×94, `E19_appendix.png` untuk Appendix A |

PDF asli pengguna **tidak dipindahkan** ke sini; tetap berada di folder workspace seperti `IBFS/` dan `RBSM/`, sesuai manifest. Tidak setiap sumber eksternal mempunyai PDF lokal: beberapa hanya diakses melalui browser. E21 hanya sampul; E22 hanya bab awal; E18 JHM tidak berhasil diunduh penuh. Periksa [source_inventory.md](report/source_inventory.md), bukan menganggap nama `.pdf` berarti artikel penuh.

## 4. datasets: input eksperimen

| Berkas | Makna |
|---|---|
| [published/occurrences.json](datasets/published/occurrences.json) | 140 kemunculan contoh pada sumber, termasuk pengulangan; memuat locator dan klaim |
| [published/benchmarks.json](datasets/published/benchmarks.json) | 86 matriks mentah berbeda berdasarkan biaya/supply/demand; input utama program |
| [published/canonical_ids.json](datasets/published/canonical_ids.json) | 84 ID untuk ringkasan setelah menghapus dua duplikasi yang setara setelah balancing |
| [published/exclusions.json](datasets/published/exclusions.json) | Input yang tidak diterima beserta alasan; angka hilang tidak diisi dengan dugaan |
| [published/reported_claims.csv](datasets/published/reported_claims.csv) | 819 klaim angka sumber yang dipertahankan terpisah; bukan 819 matriks terverifikasi |
| [published/csm_matrix_extraction.txt](datasets/published/csm_matrix_extraction.txt) | Ekstraksi antara untuk audit tabel CSM; bukan input benchmark final |
| [published/jhm_supplement.json](datasets/published/jhm_supplement.json) | Sepuluh kemunculan tambahan: sembilan Appendix A JNM dan satu L01 2×94; enam duplikat inti; tidak dicampur ke mean 84 kasus |
| [generated/seed20261001.json](datasets/generated/seed20261001.json) | 300 masalah acak tersimpan, lima ukuran dan tiga distribusi biaya; semua metode memakai input yang sama |

Jangan menjumlahkan 140, 86, dan 84 sebagai kasus berbeda: ketiganya lapisan representasi dari data inti yang sama. Jangan pula menganggap label N01/P1 dari dua sumber menunjukkan matriks sama tanpa memeriksa isinya.

## 5. methods, modifications, dan solver

| Berkas | Tanggung jawab |
|---|---|
| [methods/__init__.py](methods/__init__.py) | Daftar 14 baseline dan fungsi `solve()` yang meneruskan ke implementasi sesuai metode |
| [methods/common.py](methods/common.py) | Validasi input, balancing/dummy, biaya, kelayakan, dukungan bebas siklus, basis nol dan degenerasi |
| [methods/constructive.py](methods/constructive.py) | NWCM, LCM, VAM, LDVAM, RAM, TDM1, TDM2, TDSM, THP; urutan kandidat dan konstruksi sisa |
| [methods/repair.py](methods/repair.py) | SSM, CSM, RBSM, BCE dalam kontrak yang didokumentasikan; tidak menyembunyikan kegagalan |
| [methods/mrm.py](methods/mrm.py) | MRM versi narasi dengan orientasi default/paksa |
| [methods/jhm.py](methods/jhm.py) | JHM terbatas dan empat variasinya; terpisah dari baseline penuh karena cabang multi-excess belum terverifikasi |
| [modifications/variants.py](modifications/variants.py) | 24 variasi kecil termasuk tiga shortlist; satu file bersama mencegah duplikasi logika |
| [modifications/__init__.py](modifications/__init__.py) | Ekspor fungsi `solve_variant()` dan registry `VARIANTS` |
| [modifications/demo.py](modifications/demo.py) | Demo satu contoh tiap shortlist atau ID yang dipilih; tidak menimpa CSV hasil penelitian |
| [modifications/worked_example.py](modifications/worked_example.py) | Menghitung ulang semua langkah soal bersama L05, memeriksa kecocokan dengan kode, dan memperbarui bagian contoh bertanda pada empat Markdown beserta JSON bukti |
| [modifications/README.md](modifications/README.md) dan tiga Markdown metode | Langkah asli/modifikasi, formula, referensi, batas kebaruan dan cara menjalankan masing-masing |
| [solver/optimal_lp.py](solver/optimal_lp.py) | Model LP transportasi menggunakan SciPy/HiGHS dan pemeriksaan sertifikat primal–dual |
| [solver/__init__.py](solver/__init__.py) | Penanda paket solver |

Tidak ada file terpisah `vam.py`, `thp.py`, dst. karena beberapa metode berbagi kerangka konstruksi yang sama. Pemisahan dilakukan lewat fungsi dan nama metode. Ketiga modifikasi **sudah mempunyai kode yang dijalankan**, bukan hanya rancangan Markdown.

## 6. experiments: menjalankan dan mengaudit

| Berkas | Input → output / maksud |
|---|---|
| [protocol.md](experiments/protocol.md) | Aturan eksperimen utama: varian, seed, data bersama, metrik, larangan memakai optimum dalam pemilihan |
| [jhm_protocol.md](experiments/jhm_protocol.md) | Batas cabang JHM, seri, varian, dan pengecualian |
| [run_baselines.py](experiments/run_baselines.py) | Data inti → 14 baseline, LP, tabel reproduksi, alokasi dan sertifikat |
| [run_modifications.py](experiments/run_modifications.py) | Data inti → 24 varian; `--random` membentuk ulang 300 input seed tetap dan menjalankan baseline+varian |
| [run_jhm.py](experiments/run_jhm.py) | Data inti/acak → JHM terbatas, empat varian, pengecualian, reproduksi/seri, ringkasan dan verifikasi |
| [jhm_supplement.py](experiments/jhm_supplement.py) | Mengekstrak tambahan E19/L01, menghitung LP dan metode; menulis audit terpisah. Membutuhkan PDF `IBFS/ibfs.pdf` |
| [verify.py](experiments/verify.py) | Pemeriksaan algoritma, contoh acuan, enumerasi optimum kecil, dan sifat rollout |
| [diagnostics.py](experiments/diagnostics.py) | Eksperimen sensitivitas skala biaya dan beberapa aturan seri |
| [enumerate_ties.py](experiments/enumerate_ties.py) | Enumerasi seluruh seri yang diperbolehkan pada mismatch kecil; membedakan efek seri dari inkonsistensi angka |
| [timing.py](experiments/timing.py) | Sampel pengukuran waktu terkontrol; bukan benchmark performa perangkat keras universal |
| [summarize.py](experiments/summarize.py) | Membaca CSV yang sudah ada → statistik, tabel Markdown otomatis, sensitivitas sumber, grafik, versi lingkungan |
| [audit_artifacts.py](experiments/audit_artifacts.py) | Membaca hasil tersimpan, memeriksa hitungan/agregat, sertifikat/alokasi, tabel dan tautan. Tidak menala ulang algoritma |
| [__init__.py](experiments/__init__.py) | Penanda paket untuk pemanggilan `python -m` |

Skrip eksperimen umumnya **menulis ulang output terkait**. `summarize.py` tidak menghitung ulang semua heuristik, tetapi memperbarui laporan yang dihasilkan otomatis. Hindari mengedit angka manual dalam laporan otomatis; perbaiki sumber data/skripnya dan jelaskan perubahan protokol.

## 7. results: apa arti kelompok keluaran?

| Berkas/kelompok | Makna |
|---|---|
| `baseline.csv`, `modifications.csv`, `random_benchmark.csv` | Hasil tiap kasus/metode: biaya, optimum, gap, akurasi, status, waktu; masing-masing 1.204, 2.064, 11.400 percobaan |
| `reproduction.csv` | Perbandingan angka paper dengan hitungan ulang, termasuk mismatch dan tidak tersedia; audit historis inti 207 baris |
| `summary.csv` | Agregat metode/varian: mean, median, maksimum, simpangan baku, hits, perbaikan, memburuk, ties; denominator penting |
| `random_by_size_distribution.csv` | Agregat per ukuran dan distribusi biaya; membantu menghindari kesimpulan dari mean gabungan saja |
| `source_sensitivity.csv` | Analisis ulang ringkasan ketika matriks sumber berkonflik dikeluarkan |
| `baseline_allocations.json`, `modification_allocations.json` | Matriks X hasil konstruksi dan jejak yang disimpan; JSON lebih rinci daripada CSV biaya |
| `worked_example_L05_Example1.json` | Bukti contoh yang sama untuk tiga modifikasi: seluruh simulasi completion, margin per iterasi, tiga konstruksi MRM dan optimum; angka yang dijelaskan pada masing-masing Markdown |
| `optimal_certificates.json`, `random_optimal_certificates.json` | Solusi optimum, dual, residual dan informasi kelayakan untuk input inti/acak |
| `currency_sensitivity.csv`, `tie_diagnostics.csv`, `tie_enumeration.csv` | Audit pengaruh unit biaya, konvensi seri, dan ruang kemungkinan hasil seri |
| `controlled_timing.csv`, `environment.json` | Waktu terkontrol dan versi Python/paket/platform yang digunakan |
| `gap_comparison.png`, `gap_comparison.svg` | Grafik ringkasan tiga arah; SVG cocok untuk pembesaran, CSV tetap sumber angkanya |
| `verification.txt`, `artifact_audit.txt` | Ringkasan pemeriksaan algoritma dan pemeriksaan artefak terakhir |
| `jhm_restricted.csv`, `jhm_summary.csv`, `jhm_allocations.json` | Semua percobaan JHM parsial, agregat dengan subset berpasangan, dan alokasi |
| `jhm_reproduction.csv`, `jhm_tie_sensitivity.csv`, `jhm_verification.txt` | Klaim JHM lokal, efek seri, dan pemeriksaan khusus |
| `jhm_supplement.csv`, `jhm_supplement_reproduction.csv` | Hasil 430 percobaan tambahan dan kecocokan klaim sumber; terpisah dari inti |
| `jhm_supplement_allocations.json`, `jhm_supplement_optimal.json` | Alokasi dan sertifikat LP tambahan |

Kolom `status=ok` berarti eksekusi mengembalikan hasil yang diperiksa; itu bukan selalu optimum. `failed` mencatat kegagalan interpretasi/program pada kasus tersebut. `unverified` pada JHM berarti cabang belum terverifikasi. Sel kosong bukan nol. Mean dari kasus berhasil saja tidak boleh dibandingkan sembarangan dengan metode yang selesai pada semua kasus.

## 8. report: dokumen untuk dibaca dan ditulis dalam tugas

| Berkas | Kegunaan |
|---|---|
| [hasil_riset_dan_kesimpulan.md](report/hasil_riset_dan_kesimpulan.md) | Sintesis berbahasa Indonesia; semua metode, hasil, shortlist, dan roadmap |
| [research_report.md](report/research_report.md) | Laporan rinci 35 bagian sesuai permintaan awal |
| [terminology_and_algorithms.md](report/terminology_and_algorithms.md) | Akronim, sumber, jenis metode, balancing, aturan algoritma dan konvensi implementasi |
| [source_inventory.md](report/source_inventory.md) | Referensi lengkap, DOI, klasifikasi, tingkat akses dan kegunaan benchmark |
| [search_log.md](report/search_log.md) | Pencarian yang dilakukan dan keterbatasan akses; bukan bukti pencarian seluruh literatur |
| [modification_catalog.md](report/modification_catalog.md) | Ide untuk setiap metode, formula, risiko, prior art, status teruji/belum |
| [benchmark_catalog.md](report/benchmark_catalog.md) | Semua input inti, margin, sumber, klaim dan optimum; dihasilkan otomatis |
| [reproduction_tables.md](report/reproduction_tables.md) | Versi terbaca tabel kecocokan klaim; dihasilkan otomatis |
| [performance_tables.md](report/performance_tables.md) | Statistik lengkap semua konfigurasi; dihasilkan otomatis |
| [candidate_results.md](report/candidate_results.md) | Hasil tiap kasus tiga shortlist; dihasilkan otomatis |
| [ablation_tables.md](report/ablation_tables.md) | Pemisahan dampak tiap komponen modifikasi; dihasilkan otomatis |
| [manual_example.md](report/manual_example.md) | Demonstrasi THP 4×4, keputusan pembeda, perhitungan biaya dan bukti optimum |
| [jhm_analysis.md](report/jhm_analysis.md) | Penjelasan JHM, sumber parsial, algoritma terbatas, modifikasi, hasil negatif |
| [jhm_results.md](report/jhm_results.md) | Tabel hasil JHM terbatas; dihasilkan otomatis |
| [jhm_supplement.md](report/jhm_supplement.md) | Matriks dan hasil audit sumber tambahan JHM/L01; dihasilkan otomatis |

## 9. Cara mulai dan hal yang tidak perlu diubah

Untuk memahami proyek, urutannya: **kesimpulan → satu dokumen modifikasi → demo → contoh manual → hasil tiap kasus → referensi sumber**. Untuk menambah eksperimen, tetapkan aturan dulu, simpan nama varian baru, gunakan input sama, lalu regenerasi ringkasan.

```powershell
python -m research.modifications.demo
python -m research.modifications.demo --method thp --trace
python -m research.experiments.audit_artifacts
python research/document_tree.py
```

Perintah pertama dan kedua hanya menampilkan hasil; ketiga menulis ringkasan audit; keempat memperbarui indeks berkas. Semua dijalankan dari root `Risop`.

`__pycache__/`, `*.pyc`, dan `*.pyo` merupakan cache otomatis Python, bukan sumber metode atau hasil ilmiah. Cache dikecualikan dari indeks berkas dan diabaikan oleh aturan `.gitignore`; Python dapat membuatnya kembali saat program dijalankan. Berkas mentah `papers/` dan dataset yang menjadi dasar eksperimen sebaiknya dipertahankan agar asal angka dapat diaudit. Inventaris ini tidak mengklaim setiap paper yang ditemukan sudah direproduksi; batas akses dan implementasi tetap tercatat pada laporan.
