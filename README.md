# Riset heuristik masalah transportasi

Diperbarui **2 Oktober 2026** (Asia/Jakarta); hasil eksperimen utama tetap bertanggal 1 Oktober 2026. **Mulai dari [hasil riset dan kesimpulan berbahasa Indonesia](report/hasil_riset_dan_kesimpulan.md).** Laporan mencakup semua metode, hasil positif/negatif, shortlist, dan eksperimen pertama yang dapat dipresentasikan. IHW dilewati sesuai permintaan pengguna; JHM diuji dengan batas implementasi yang dijelaskan secara terbuka.

## Peta berkas

- [Panduan isi setiap folder](STRUKTUR_FOLDER.md) dan [indeks setiap berkas](FILE_INDEX.md).
- [Dokumentasi dan demo tiga modifikasi](modifications/README.md): [VAM](modifications/vam_top2_rollout.md), [THP](modifications/thp_top2_rollout.md), [MRM](modifications/mrm_orientation_ensemble.md). Masing-masing memisahkan algoritma, referensi konsep dan batas kebaruan.
- [Laporan rinci 35 bagian](report/research_report.md), [status penelitian](progress.md), [inventaris lima paper lokal](paper_inventory.md), [inventaris literatur eksternal](report/source_inventory.md).
- [Terminologi dan algoritma](report/terminology_and_algorithms.md), [ide modifikasi dan kebaruan](report/modification_catalog.md), [contoh manual THP dan bukti optimum](report/manual_example.md).
- [Semua matriks inti](report/benchmark_catalog.md), [reproduksi](report/reproduction_tables.md), [statistik lengkap](report/performance_tables.md), [hasil per kasus shortlist](report/candidate_results.md), [ablasi](report/ablation_tables.md).
- [Pendalaman JHM](report/jhm_analysis.md), [hasil terbatas](report/jhm_results.md), [audit sembilan matriks JNM dan aplikasi nyata BCE](report/jhm_supplement.md).
- [Ringkasan CSV utama](results/summary.csv), [JHM CSV](results/jhm_restricted.csv), [sertifikat optimum](results/optimal_certificates.json), [versi lingkungan](results/environment.json).
- [Audit akhir angka, sertifikat, alokasi, tabel, dan tautan](results/artifact_audit.txt).

Paper lokal tetap berada di folder aslinya. Hasil ekstraksi teks hanya alat bantu membaca; angka penting diperiksa terhadap halaman PDF. Kode sendiri berada di `methods/`, `modifications/`, `solver/`, dan `experiments/`. Kode penulis yang diunduh disimpan sebagai sumber audit dan tidak dijalankan sebagai executable.

## Menjalankan ulang

Untuk mencoba ketiga contoh tanpa menimpa CSV eksperimen, jalankan `python -m research.modifications.demo` dari root workspace. Gunakan `--method thp --trace` untuk langkah alokasi atau `--json` untuk keluaran lengkap. Kode modifikasi sebelumnya sudah ada di `modifications/variants.py`; demo menyediakan akses yang lebih mudah.

Untuk **satu soal yang sama pada ketiganya**, gunakan `python -m research.modifications.demo --problem L05_Example1`. [Contoh bersama](modifications/README.md#contoh-soal-bersama) dan bagian 6 setiap dokumen modifikasi menampilkan seluruh tableau, perhitungan kandidat/completion atau orientasi, alokasi, serta biaya akhirnya. `python -m research.modifications.worked_example` membangun ulang bagian contoh dari kode dan menyimpan bukti perhitungannya.

Jalankan dari root workspace `Risop`, menggunakan Python dengan paket dalam [requirements.txt](requirements.txt). Versi yang digunakan tersimpan dalam environment JSON. Data dan hasil sudah tersedia; tidak perlu mengunduh ulang sumber hanya untuk membaca atau menjalankan benchmark inti. Perintah eksperimen berikut menulis ulang berkas hasil terkait.

```powershell
python -m research.experiments.run_baselines
python -m research.experiments.run_modifications
python -m research.experiments.run_modifications --random
python -m research.experiments.verify
python -m research.experiments.diagnostics
python -m research.experiments.enumerate_ties
python -m research.experiments.timing
python -m research.experiments.summarize
python -m research.experiments.run_jhm
python -m research.experiments.jhm_supplement
python -m research.experiments.audit_artifacts
```

`jhm_supplement` memerlukan PDF lokal `IBFS/ibfs.pdf` untuk mengekstrak ulang input 2×94. Skrip `build_datasets.py` dan `extract_claims.py` merekonstruksi data dari berkas sumber yang disimpan; gunakan bila melakukan audit ekstraksi, bukan untuk mengubah input diam-diam setelah eksperimen. Protokol utama ada di [protocol.md](experiments/protocol.md), protokol JHM di [jhm_protocol.md](experiments/jhm_protocol.md).

## Batas cakupan

Suite utama: 84 input kanonik dari 86 matriks mentah dan 140 kemunculan sumber, 14 baseline, 24 modifikasi, 300 input acak tetap. Sepuluh kemunculan sumber tambahan JHM disimpan terpisah; enam adalah duplikat inti. Mean JHM terbatas dan BCE yang hanya berhasil pada subset tidak boleh dibandingkan dengan mean metode yang menyelesaikan seluruh suite. Semua klaim kebaruan dibatasi oleh literatur yang benar-benar dapat diperiksa.

Untuk memperbarui daftar berkas sesudah menambah artefak, jalankan `python research/document_tree.py`. Metadata internal Git dan lingkungan virtual dikecualikan dari indeks.
