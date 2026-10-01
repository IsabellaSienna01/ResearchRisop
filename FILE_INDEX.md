# Indeks setiap berkas research

Dibuat oleh `python research/document_tree.py`. Ini daftar berkas saat generator terakhir dijalankan; tanggal riset dan pembaruan ada pada masing-masing dokumen. [Panduan hubungan folder](STRUKTUR_FOLDER.md) memberi penjelasan alur kerja.

Tercatat **245 berkas**. Cache bytecode Python, metadata internal .git, konfigurasi alat tersembunyi dan lingkungan virtual tidak diindeks. Deskripsi sumber menyatakan tingkat akses, bukan jaminan kebenaran klaim paper.

## research/ (root)

| Berkas | Maksud/kegunaan |
|---|---|
| [.gitignore](.gitignore) | Aturan Git untuk mengecualikan cache bytecode Python yang dapat dibuat ulang. |
| [__init__.py](__init__.py) | Penanda paket Python untuk impor dan pemanggilan python -m. |
| [build_datasets.py](build_datasets.py) | Transkripsi/parsing input, deduplikasi dan pencatatan pengecualian. |
| [document_tree.py](document_tree.py) | Generator indeks berkas ini; hanya menulis FILE_INDEX.md. |
| [extract_claims.py](extract_claims.py) | Ekstraksi klaim angka paper tanpa menganggap matriksnya sudah diketahui. |
| [extract_local.py](extract_local.py) | Pemindaian/ekstraksi PDF lokal dan pembentukan manifest sumber. |
| [fetch_batch.py](fetch_batch.py) | Pengunduh antrean sumber dan pencatat hasil; tidak mengeksekusi kode unduhan. |
| [fetch_source.py](fetch_source.py) | Unduhan satu sumber terpilih dan catatan provenance; bukan solver. |
| [FILE_INDEX.md](FILE_INDEX.md) | Indeks otomatis setiap berkas beserta kegunaannya. |
| [paper_inventory.md](paper_inventory.md) | Inventaris lima PDF pengguna, contoh, klaim, DOI dan koreksi penemuan input 2x94. |
| [prepare_downloads.py](prepare_downloads.py) | Pembentukan antrean URL unduhan dari halaman sumber yang disimpan. |
| [progress.md](progress.md) | Status tahap penelitian, pengecualian dan keterbatasan yang masih terbuka. |
| [read_text.py](read_text.py) | Pembaca rentang baris teks dengan nomor baris. |
| [README.md](README.md) | Pintu masuk, tautan laporan dan perintah reproduksi. |
| [render_pages.py](render_pages.py) | Merender halaman PDF terpilih untuk audit visual transkripsi. |
| [requirements.txt](requirements.txt) | Daftar paket Python; versi eksperimen tercatat dalam results/environment.json. |
| [STRUKTUR_FOLDER.md](STRUKTUR_FOLDER.md) | Panduan hubungan folder, data, kode, eksperimen dan laporan. |

## datasets/generated/

| Berkas | Maksud/kegunaan |
|---|---|
| [seed20261001.json](datasets/generated/seed20261001.json) | 300 matriks acak tetap untuk input bersama seluruh metode. |

## datasets/published/

| Berkas | Maksud/kegunaan |
|---|---|
| [benchmarks.json](datasets/published/benchmarks.json) | 86 input mentah unik untuk eksperimen inti. |
| [canonical_ids.json](datasets/published/canonical_ids.json) | 84 ID inti untuk ringkasan setelah deduplikasi setara balancing. |
| [csm_matrix_extraction.txt](datasets/published/csm_matrix_extraction.txt) | Ekstraksi antara tabel CSM untuk audit transkripsi. |
| [exclusions.json](datasets/published/exclusions.json) | Data yang dikeluarkan dan alasan; tidak diisi dengan dugaan. |
| [jhm_supplement.json](datasets/published/jhm_supplement.json) | Sepuluh kemunculan sumber tambahan, termasuk pemetaan enam duplikat inti. |
| [occurrences.json](datasets/published/occurrences.json) | 140 kemunculan input di sumber dengan locator dan klaim; duplikasi dipertahankan. |
| [reported_claims.csv](datasets/published/reported_claims.csv) | 819 klaim sumber terpisah yang belum otomatis dicocokkan ke matriks. |

## experiments/

| Berkas | Maksud/kegunaan |
|---|---|
| [__init__.py](experiments/__init__.py) | Penanda paket Python untuk impor dan pemanggilan python -m. |
| [audit_artifacts.py](experiments/audit_artifacts.py) | Audit data, agregat, alokasi/dual, tabel dan tautan dokumen tanpa menala eksperimen. |
| [diagnostics.py](experiments/diagnostics.py) | Audit sensitivitas skala biaya dan konvensi seri. |
| [enumerate_ties.py](experiments/enumerate_ties.py) | Enumerasi pilihan seri pada ketidakcocokan contoh kecil. |
| [jhm_protocol.md](experiments/jhm_protocol.md) | Protokol JHM terbatas, seri, varian dan penanganan cabang unverified. |
| [jhm_supplement.py](experiments/jhm_supplement.py) | Ekstraksi/audit input tambahan E19 dan L01 2x94; eksperimen terpisah. |
| [protocol.md](experiments/protocol.md) | Protokol utama: varian, data bersama, seed, metrik dan batas klaim. |
| [run_baselines.py](experiments/run_baselines.py) | Eksekusi baseline, LP, reproduksi klaim dan penyimpanan alokasi. |
| [run_jhm.py](experiments/run_jhm.py) | Percobaan JHM terbatas, empat varian, reproduksi dan sensitivitas seri. |
| [run_modifications.py](experiments/run_modifications.py) | Eksekusi 24 varian; --random membentuk dan menguji 300 input seed tetap. |
| [summarize.py](experiments/summarize.py) | Pembentuk statistik, tabel Markdown otomatis, grafik dan environment dari CSV tersimpan. |
| [timing.py](experiments/timing.py) | Pengukuran waktu terkontrol pada sampel kasus. |
| [verify.py](experiments/verify.py) | Pemeriksaan algoritma, anchor, enumerasi optimum kecil dan sifat rollout. |

## methods/

| Berkas | Maksud/kegunaan |
|---|---|
| [__init__.py](methods/__init__.py) | Registry 14 baseline dan fungsi solve untuk memilih implementasi. |
| [common.py](methods/common.py) | Validasi, balancing, biaya, kelayakan, basis bebas siklus dan degenerasi. |
| [constructive.py](methods/constructive.py) | Seleksi kandidat dan konstruksi NWCM/LCM/VAM/LDVAM/RAM/TDM1/TDM2/TDSM/THP. |
| [jhm.py](methods/jhm.py) | JHM terbatas dan empat variasi; cabang belum diketahui tidak diganti aturan lain. |
| [mrm.py](methods/mrm.py) | MRM narasi, orientasi default atau paksa baris/kolom. |
| [repair.py](methods/repair.py) | Interpretasi algoritma perbaikan SSM/CSM/RBSM/BCE, termasuk pencatatan kegagalan. |

## modifications/

| Berkas | Maksud/kegunaan |
|---|---|
| [__init__.py](modifications/__init__.py) | Ekspor VARIANTS dan solve_variant untuk impor Python. |
| [demo.py](modifications/demo.py) | CLI demo baseline-modifikasi-optimum, jejak dan JSON; tidak menimpa CSV penelitian. |
| [mrm_orientation_ensemble.md](modifications/mrm_orientation_ensemble.md) | Algoritma pilihan orientasi MRM, prior art, dummy/seri dan batas benchmark. |
| [README.md](modifications/README.md) | Indeks tiga dokumen modifikasi, status kebaruan, API dan cara menjalankan. |
| [thp_top2_rollout.md](modifications/thp_top2_rollout.md) | Langkah THP dua kandidat, beda dari dua tingkat penalti asli, sumber dan hasil. |
| [vam_top2_rollout.md](modifications/vam_top2_rollout.md) | Langkah VAM dua kandidat, asal ide, rumus, pseudocode, hasil dan batas kebaruan. |
| [variants.py](modifications/variants.py) | Registry dan implementasi 24 modifikasi kecil, termasuk tiga shortlist. |
| [worked_example.py](modifications/worked_example.py) | Membangun dan memeriksa contoh L05 yang sama pada empat Markdown, dengan seluruh simulasi kandidat/orientasi. |

## papers/external/

| Berkas | Maksud/kegunaan |
|---|---|
| [download_outcomes.json](papers/external/download_outcomes.json) | Status setiap unduhan antrean, termasuk kegagalan. |
| [download_queue.json](papers/external/download_queue.json) | Antrean unduhan sumber yang dipilih; belum menyatakan sukses. |
| [E01_hosseini2017.pdf](papers/external/E01_hosseini2017.pdf) | PDF unduhan: Hosseini 2017: TDM1/TDM2/TDSM. |
| [E01_hosseini2017.pdf.source.json](papers/external/E01_hosseini2017.pdf.source.json) | Metadata asal unduhan E01_hosseini2017.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E01_hosseini2017.txt](papers/external/E01_hosseini2017.txt) | Ekstraksi teks sumber: Hosseini 2017: TDM1/TDM2/TDSM. |
| [E02_rbsm_dataset.html](papers/external/E02_rbsm_dataset.html) | HTML sumber tersimpan: halaman dataset RBSM penulis. |
| [E02_rbsm_dataset.html.source.json](papers/external/E02_rbsm_dataset.html.source.json) | Metadata asal unduhan E02_rbsm_dataset.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E02_rbsm_dataset.txt](papers/external/E02_rbsm_dataset.txt) | Ekstraksi teks sumber: halaman dataset RBSM penulis. |
| [E03_ssm_dataset.html](papers/external/E03_ssm_dataset.html) | HTML sumber tersimpan: halaman tautan data SSM; tidak menyajikan matriks lengkap saat diakses. |
| [E03_ssm_dataset.html.source.json](papers/external/E03_ssm_dataset.html.source.json) | Metadata asal unduhan E03_ssm_dataset.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E03_ssm_dataset.txt](papers/external/E03_ssm_dataset.txt) | Ekstraksi teks sumber: halaman tautan data SSM; tidak menyajikan matriks lengkap saat diakses. |
| [E04_csm_landing.html](papers/external/E04_csm_landing.html) | HTML sumber tersimpan: halaman penerbit CSM. |
| [E04_csm_landing.html.source.json](papers/external/E04_csm_landing.html.source.json) | Metadata asal unduhan E04_csm_landing.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E05_mrm_landing.html](papers/external/E05_mrm_landing.html) | HTML sumber tersimpan: halaman penerbit MRM; bukan otomatis PDF penuh. |
| [E05_mrm_landing.html.source.json](papers/external/E05_mrm_landing.html.source.json) | Metadata asal unduhan E05_mrm_landing.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E06_csm_dataset.html](papers/external/E06_csm_dataset.html) | HTML sumber tersimpan: halaman dataset/hasil CSM penulis. |
| [E06_csm_dataset.html.source.json](papers/external/E06_csm_dataset.html.source.json) | Metadata asal unduhan E06_csm_dataset.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E07_csm_pdf_page.html](papers/external/E07_csm_pdf_page.html) | HTML sumber tersimpan: halaman akses PDF CSM. |
| [E07_csm_pdf_page.html.source.json](papers/external/E07_csm_pdf_page.html.source.json) | Metadata asal unduhan E07_csm_pdf_page.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E08_rbsm_drive.html](papers/external/E08_rbsm_drive.html) | HTML sumber tersimpan: halaman folder publik data RBSM. |
| [E08_rbsm_drive.html.source.json](papers/external/E08_rbsm_drive.html.source.json) | Metadata asal unduhan E08_rbsm_drive.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E09_edm_dataset.html](papers/external/E09_edm_dataset.html) | HTML sumber tersimpan: halaman matriks EDM penulis. |
| [E09_edm_dataset.html.source.json](papers/external/E09_edm_dataset.html.source.json) | Metadata asal unduhan E09_edm_dataset.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E11_csm.pdf](papers/external/E11_csm.pdf) | PDF unduhan: paper CSM 2026. |
| [E11_csm.pdf.source.json](papers/external/E11_csm.pdf.source.json) | Metadata asal unduhan E11_csm.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E11_csm.txt](papers/external/E11_csm.txt) | Ekstraksi teks sumber: paper CSM 2026. |
| [E12_csm_data.pdf](papers/external/E12_csm_data.pdf) | PDF unduhan: suplemen matriks CSM; konflik sumber diaudit. |
| [E12_csm_data.pdf.source.json](papers/external/E12_csm_data.pdf.source.json) | Metadata asal unduhan E12_csm_data.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E12_csm_data.txt](papers/external/E12_csm_data.txt) | Ekstraksi teks sumber: suplemen matriks CSM; konflik sumber diaudit. |
| [E13_csm_results.pdf](papers/external/E13_csm_results.pdf) | PDF unduhan: suplemen hasil perbandingan CSM. |
| [E13_csm_results.pdf.source.json](papers/external/E13_csm_results.pdf.source.json) | Metadata asal unduhan E13_csm_results.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E13_csm_results.txt](papers/external/E13_csm_results.txt) | Ekstraksi teks sumber: suplemen hasil perbandingan CSM. |
| [E14_csm_runtime.pdf](papers/external/E14_csm_runtime.pdf) | PDF unduhan: suplemen waktu CSM. |
| [E14_csm_runtime.pdf.source.json](papers/external/E14_csm_runtime.pdf.source.json) | Metadata asal unduhan E14_csm_runtime.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E14_csm_runtime.txt](papers/external/E14_csm_runtime.txt) | Ekstraksi teks sumber: suplemen waktu CSM. |
| [E17_capacity2024.pdf](papers/external/E17_capacity2024.pdf) | PDF unduhan: paper capacity-influenced 2024, prior art. |
| [E17_capacity2024.pdf.source.json](papers/external/E17_capacity2024.pdf.source.json) | Metadata asal unduhan E17_capacity2024.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E17_capacity2024.txt](papers/external/E17_capacity2024.txt) | Ekstraksi teks sumber: paper capacity-influenced 2024, prior art. |
| [E19_jnm2019.pdf](papers/external/E19_jnm2019.pdf) | PDF unduhan: Juman-Nawarathne 2019; Appendix A sumber benchmark JHM tambahan. |
| [E19_jnm2019.pdf.source.json](papers/external/E19_jnm2019.pdf.source.json) | Metadata asal unduhan E19_jnm2019.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E19_jnm2019.txt](papers/external/E19_jnm2019.txt) | Ekstraksi teks sumber: Juman-Nawarathne 2019; Appendix A sumber benchmark JHM tambahan. |
| [E20_ilcm2016.pdf](papers/external/E20_ilcm2016.pdf) | PDF unduhan: paper iLCM 2016, prior art aturan seri. |
| [E20_ilcm2016.pdf.source.json](papers/external/E20_ilcm2016.pdf.source.json) | Metadata asal unduhan E20_ilcm2016.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E20_ilcm2016.txt](papers/external/E20_ilcm2016.txt) | Ekstraksi teks sumber: paper iLCM 2016, prior art aturan seri. |
| [E21_jhm_thesis.pdf](papers/external/E21_jhm_thesis.pdf) | PDF unduhan: skripsi Indrawan 2021, hanya sampul satu halaman yang diperoleh. |
| [E21_jhm_thesis.pdf.source.json](papers/external/E21_jhm_thesis.pdf.source.json) | Metadata asal unduhan E21_jhm_thesis.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E21_jhm_thesis.txt](papers/external/E21_jhm_thesis.txt) | Ekstraksi teks sumber: skripsi Indrawan 2021, hanya sampul satu halaman yang diperoleh. |
| [E22_jhm_unhas2024.pdf](papers/external/E22_jhm_unhas2024.pdf) | PDF unduhan: skripsi Rahayu UNHAS 2024; PDF hanya sampul/Bab 1-2, HTML rekaman repositori. |
| [E22_jhm_unhas2024.pdf.source.json](papers/external/E22_jhm_unhas2024.pdf.source.json) | Metadata asal unduhan E22_jhm_unhas2024.pdf: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [E22_jhm_unhas2024.txt](papers/external/E22_jhm_unhas2024.txt) | Ekstraksi teks sumber: skripsi Rahayu UNHAS 2024; PDF hanya sampul/Bab 1-2, HTML rekaman repositori. |
| [E22_unhas_record.html](papers/external/E22_unhas_record.html) | HTML sumber tersimpan: skripsi Rahayu UNHAS 2024; PDF hanya sampul/Bab 1-2, HTML rekaman repositori. |
| [E22_unhas_record.html.source.json](papers/external/E22_unhas_record.html.source.json) | Metadata asal unduhan E22_unhas_record.html: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_metodeS2new.cpp](papers/external/rbsm_metodeS2new.cpp) | Kode C++ penulis RBSM untuk inspeksi; tidak dijalankan sebagai baseline proyek. |
| [rbsm_metodeS2new.cpp.source.json](papers/external/rbsm_metodeS2new.cpp.source.json) | Metadata asal unduhan rbsm_metodeS2new.cpp: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n01.txt](papers/external/rbsm_n01.txt) | Matriks mentah kasus n01 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n01.txt.source.json](papers/external/rbsm_n01.txt.source.json) | Metadata asal unduhan rbsm_n01.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n02.txt](papers/external/rbsm_n02.txt) | Matriks mentah kasus n02 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n02.txt.source.json](papers/external/rbsm_n02.txt.source.json) | Metadata asal unduhan rbsm_n02.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n03.txt](papers/external/rbsm_n03.txt) | Matriks mentah kasus n03 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n03.txt.source.json](papers/external/rbsm_n03.txt.source.json) | Metadata asal unduhan rbsm_n03.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n04.txt](papers/external/rbsm_n04.txt) | Matriks mentah kasus n04 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n04.txt.source.json](papers/external/rbsm_n04.txt.source.json) | Metadata asal unduhan rbsm_n04.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n05.txt](papers/external/rbsm_n05.txt) | Matriks mentah kasus n05 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n05.txt.source.json](papers/external/rbsm_n05.txt.source.json) | Metadata asal unduhan rbsm_n05.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n06.txt](papers/external/rbsm_n06.txt) | Matriks mentah kasus n06 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n06.txt.source.json](papers/external/rbsm_n06.txt.source.json) | Metadata asal unduhan rbsm_n06.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n07.txt](papers/external/rbsm_n07.txt) | Matriks mentah kasus n07 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n07.txt.source.json](papers/external/rbsm_n07.txt.source.json) | Metadata asal unduhan rbsm_n07.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n08.txt](papers/external/rbsm_n08.txt) | Matriks mentah kasus n08 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n08.txt.source.json](papers/external/rbsm_n08.txt.source.json) | Metadata asal unduhan rbsm_n08.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n09.txt](papers/external/rbsm_n09.txt) | Matriks mentah kasus n09 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n09.txt.source.json](papers/external/rbsm_n09.txt.source.json) | Metadata asal unduhan rbsm_n09.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n10.txt](papers/external/rbsm_n10.txt) | Matriks mentah kasus n10 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n10.txt.source.json](papers/external/rbsm_n10.txt.source.json) | Metadata asal unduhan rbsm_n10.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n11.txt](papers/external/rbsm_n11.txt) | Matriks mentah kasus n11 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n11.txt.source.json](papers/external/rbsm_n11.txt.source.json) | Metadata asal unduhan rbsm_n11.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n12.txt](papers/external/rbsm_n12.txt) | Matriks mentah kasus n12 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n12.txt.source.json](papers/external/rbsm_n12.txt.source.json) | Metadata asal unduhan rbsm_n12.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n13.txt](papers/external/rbsm_n13.txt) | Matriks mentah kasus n13 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n13.txt.source.json](papers/external/rbsm_n13.txt.source.json) | Metadata asal unduhan rbsm_n13.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n14.txt](papers/external/rbsm_n14.txt) | Matriks mentah kasus n14 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n14.txt.source.json](papers/external/rbsm_n14.txt.source.json) | Metadata asal unduhan rbsm_n14.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n15.txt](papers/external/rbsm_n15.txt) | Matriks mentah kasus n15 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n15.txt.source.json](papers/external/rbsm_n15.txt.source.json) | Metadata asal unduhan rbsm_n15.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n16.txt](papers/external/rbsm_n16.txt) | Matriks mentah kasus n16 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n16.txt.source.json](papers/external/rbsm_n16.txt.source.json) | Metadata asal unduhan rbsm_n16.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n17.txt](papers/external/rbsm_n17.txt) | Matriks mentah kasus n17 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n17.txt.source.json](papers/external/rbsm_n17.txt.source.json) | Metadata asal unduhan rbsm_n17.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n18.txt](papers/external/rbsm_n18.txt) | Matriks mentah kasus n18 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n18.txt.source.json](papers/external/rbsm_n18.txt.source.json) | Metadata asal unduhan rbsm_n18.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n21.txt](papers/external/rbsm_n21.txt) | Matriks mentah kasus n21 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n21.txt.source.json](papers/external/rbsm_n21.txt.source.json) | Metadata asal unduhan rbsm_n21.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n22.txt](papers/external/rbsm_n22.txt) | Matriks mentah kasus n22 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n22.txt.source.json](papers/external/rbsm_n22.txt.source.json) | Metadata asal unduhan rbsm_n22.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n23.txt](papers/external/rbsm_n23.txt) | Matriks mentah kasus n23 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n23.txt.source.json](papers/external/rbsm_n23.txt.source.json) | Metadata asal unduhan rbsm_n23.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n24.txt](papers/external/rbsm_n24.txt) | Matriks mentah kasus n24 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n24.txt.source.json](papers/external/rbsm_n24.txt.source.json) | Metadata asal unduhan rbsm_n24.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n25.txt](papers/external/rbsm_n25.txt) | Matriks mentah kasus n25 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n25.txt.source.json](papers/external/rbsm_n25.txt.source.json) | Metadata asal unduhan rbsm_n25.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n26.txt](papers/external/rbsm_n26.txt) | Matriks mentah kasus n26 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n26.txt.source.json](papers/external/rbsm_n26.txt.source.json) | Metadata asal unduhan rbsm_n26.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n27.txt](papers/external/rbsm_n27.txt) | Matriks mentah kasus n27 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n27.txt.source.json](papers/external/rbsm_n27.txt.source.json) | Metadata asal unduhan rbsm_n27.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n28.txt](papers/external/rbsm_n28.txt) | Matriks mentah kasus n28 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n28.txt.source.json](papers/external/rbsm_n28.txt.source.json) | Metadata asal unduhan rbsm_n28.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n29.txt](papers/external/rbsm_n29.txt) | Matriks mentah kasus n29 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n29.txt.source.json](papers/external/rbsm_n29.txt.source.json) | Metadata asal unduhan rbsm_n29.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n30.txt](papers/external/rbsm_n30.txt) | Matriks mentah kasus n30 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n30.txt.source.json](papers/external/rbsm_n30.txt.source.json) | Metadata asal unduhan rbsm_n30.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n31.txt](papers/external/rbsm_n31.txt) | Matriks mentah kasus n31 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n31.txt.source.json](papers/external/rbsm_n31.txt.source.json) | Metadata asal unduhan rbsm_n31.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n32.txt](papers/external/rbsm_n32.txt) | Matriks mentah kasus n32 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n32.txt.source.json](papers/external/rbsm_n32.txt.source.json) | Metadata asal unduhan rbsm_n32.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n33.txt](papers/external/rbsm_n33.txt) | Matriks mentah kasus n33 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n33.txt.source.json](papers/external/rbsm_n33.txt.source.json) | Metadata asal unduhan rbsm_n33.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n34.txt](papers/external/rbsm_n34.txt) | Matriks mentah kasus n34 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n34.txt.source.json](papers/external/rbsm_n34.txt.source.json) | Metadata asal unduhan rbsm_n34.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_n35.txt](papers/external/rbsm_n35.txt) | Matriks mentah kasus n35 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_n35.txt.source.json](papers/external/rbsm_n35.txt.source.json) | Metadata asal unduhan rbsm_n35.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_S1.txt](papers/external/rbsm_S1.txt) | Matriks mentah kasus S1 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_S1.txt.source.json](papers/external/rbsm_S1.txt.source.json) | Metadata asal unduhan rbsm_S1.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_S2.txt](papers/external/rbsm_S2.txt) | Matriks mentah kasus S2 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_S2.txt.source.json](papers/external/rbsm_S2.txt.source.json) | Metadata asal unduhan rbsm_S2.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_S3.txt](papers/external/rbsm_S3.txt) | Matriks mentah kasus S3 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_S3.txt.source.json](papers/external/rbsm_S3.txt.source.json) | Metadata asal unduhan rbsm_S3.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_S4.txt](papers/external/rbsm_S4.txt) | Matriks mentah kasus S4 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_S4.txt.source.json](papers/external/rbsm_S4.txt.source.json) | Metadata asal unduhan rbsm_S4.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |
| [rbsm_S5.txt](papers/external/rbsm_S5.txt) | Matriks mentah kasus S5 dari dataset penulis RBSM; provenance ada di .source.json. |
| [rbsm_S5.txt.source.json](papers/external/rbsm_S5.txt.source.json) | Metadata asal unduhan rbsm_S5.txt: URL, waktu, ukuran/hash dan rincian akses yang dicatat. |

## papers/

| Berkas | Maksud/kegunaan |
|---|---|
| [local_manifest.json](papers/local_manifest.json) | Lokasi, metadata, halaman, ukuran dan SHA-256 PDF lokal; pemetaan L01-L05. |

## papers/local_text/

| Berkas | Maksud/kegunaan |
|---|---|
| [L01.txt](papers/local_text/L01.txt) | Ekstraksi teks PDF lokal L01: BCE/IBFS; periksa tabel terhadap PDF. |
| [L02.txt](papers/local_text/L02.txt) | Ekstraksi teks PDF lokal L02: RBSM; periksa tabel terhadap PDF. |
| [L03.txt](papers/local_text/L03.txt) | Ekstraksi teks PDF lokal L03: SSM; periksa tabel terhadap PDF. |
| [L04.txt](papers/local_text/L04.txt) | Ekstraksi teks PDF lokal L04: modifikasi VAM AIP; periksa tabel terhadap PDF. |
| [L05.txt](papers/local_text/L05.txt) | Ekstraksi teks PDF lokal L05: THP; periksa tabel terhadap PDF. |

## papers/page_checks/

| Berkas | Maksud/kegunaan |
|---|---|
| [0AIP_p3.png](papers/page_checks/0AIP_p3.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [0AIP_p4.png](papers/page_checks/0AIP_p4.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [0AIP_p5.png](papers/page_checks/0AIP_p5.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [E01_hosseini2017_p11.png](papers/page_checks/E01_hosseini2017_p11.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [E01_hosseini2017_p9.png](papers/page_checks/E01_hosseini2017_p9.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [E11_csm_p4.png](papers/page_checks/E11_csm_p4.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [E12_csm_data_p1.png](papers/page_checks/E12_csm_data_p1.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [E19_appendix.png](papers/page_checks/E19_appendix.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |
| [L01_real.png](papers/page_checks/L01_real.png) | Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas. |

## report/

| Berkas | Maksud/kegunaan |
|---|---|
| [ablation_tables.md](report/ablation_tables.md) | Tabel otomatis pemisahan efek komponen perubahan. |
| [benchmark_catalog.md](report/benchmark_catalog.md) | Katalog otomatis semua matriks inti, sumber, klaim dan optimum. |
| [candidate_results.md](report/candidate_results.md) | Tabel otomatis biaya tiap kasus untuk tiga shortlist. |
| [hasil_riset_dan_kesimpulan.md](report/hasil_riset_dan_kesimpulan.md) | Sintesis Indonesia: semua metode, hasil, pilihan proyek dan roadmap. |
| [jhm_analysis.md](report/jhm_analysis.md) | Analisis JHM, sumber parsial, algoritma terbatas, hasil positif/negatif. |
| [jhm_results.md](report/jhm_results.md) | Tabel otomatis hasil JHM terbatas dan cakupan pengecualian. |
| [jhm_supplement.md](report/jhm_supplement.md) | Tabel/matriks otomatis audit sembilan contoh E19 dan aplikasi L01 2x94. |
| [manual_example.md](report/manual_example.md) | Demonstrasi THP 4x4 dan sertifikat dual optimum 985. |
| [modification_catalog.md](report/modification_catalog.md) | Ide tiap metode, langkah yang berubah, prior art, risiko dan status eksperimen. |
| [performance_tables.md](report/performance_tables.md) | Tabel otomatis statistik lengkap seluruh konfigurasi. |
| [reproduction_tables.md](report/reproduction_tables.md) | Tabel otomatis reproduksi klaim historis inti. |
| [research_report.md](report/research_report.md) | Laporan utama rinci 35 bagian. |
| [search_log.md](report/search_log.md) | Log pencarian dan batas akses; bukan bukti penelusuran seluruh literatur. |
| [source_inventory.md](report/source_inventory.md) | Referensi, DOI, klasifikasi, tingkat akses dan kegunaan benchmark. |
| [terminology_and_algorithms.md](report/terminology_and_algorithms.md) | Validasi akronim, algoritma dan konvensi implementasi. |

## results/

| Berkas | Maksud/kegunaan |
|---|---|
| [artifact_audit.txt](results/artifact_audit.txt) | Hasil pemeriksaan terakhir terhadap artefak tersimpan dan dokumen. |
| [baseline.csv](results/baseline.csv) | 1.204 percobaan baseline pada 86 input mentah. |
| [baseline_allocations.json](results/baseline_allocations.json) | Matriks alokasi baseline dan jejak yang disimpan. |
| [controlled_timing.csv](results/controlled_timing.csv) | Sampel pengukuran waktu setelah warmup dan pengulangan. |
| [currency_sensitivity.csv](results/currency_sensitivity.csv) | Pengaruh penskalaan biaya terhadap keputusan dan biaya dalam satuan asli. |
| [environment.json](results/environment.json) | Versi Python, NumPy, SciPy, pandas dan platform saat ringkasan dibuat. |
| [gap_comparison.png](results/gap_comparison.png) | Grafik raster mean gap tiga arah penelitian. |
| [gap_comparison.svg](results/gap_comparison.svg) | Grafik vektor mean gap, dapat diperbesar tanpa pecah. |
| [jhm_allocations.json](results/jhm_allocations.json) | Alokasi dan jejak JHM parsial yang berhasil. |
| [jhm_reproduction.csv](results/jhm_reproduction.csv) | Perbandingan klaim JHM lokal dengan interpretasi terbatas. |
| [jhm_restricted.csv](results/jhm_restricted.csv) | 1.930 percobaan JHM parsial dan varian, termasuk unverified. |
| [jhm_summary.csv](results/jhm_summary.csv) | Statistik JHM dengan cakupan berhasil dan pasangan yang sebanding. |
| [jhm_supplement.csv](results/jhm_supplement.csv) | 430 percobaan pada sepuluh kemunculan sumber tambahan. |
| [jhm_supplement_allocations.json](results/jhm_supplement_allocations.json) | Alokasi dan jejak yang berhasil pada audit tambahan. |
| [jhm_supplement_optimal.json](results/jhm_supplement_optimal.json) | Sepuluh sertifikat optimum tambahan, termasuk sumber yang duplikat inti. |
| [jhm_supplement_reproduction.csv](results/jhm_supplement_reproduction.csv) | 33 perbandingan klaim tambahan; duplikat sumber tidak dihitung sebagai kasus independen. |
| [jhm_tie_sensitivity.csv](results/jhm_tie_sensitivity.csv) | Biaya/alokasi JHM dengan dua konvensi seri, disimpan terpisah. |
| [jhm_verification.txt](results/jhm_verification.txt) | Ringkasan pemeriksaan kelayakan, basis dan anchor JHM. |
| [modification_allocations.json](results/modification_allocations.json) | Matriks alokasi modifikasi dan skor/jejak yang disimpan. |
| [modifications.csv](results/modifications.csv) | 2.064 percobaan 24 modifikasi pada 86 input mentah. |
| [optimal_certificates.json](results/optimal_certificates.json) | 86 optimum inti dengan alokasi, dual dan residual. |
| [random_benchmark.csv](results/random_benchmark.csv) | 11.400 percobaan 14 baseline dan 24 varian pada 300 input bersama. |
| [random_by_size_distribution.csv](results/random_by_size_distribution.csv) | Statistik dipisah menurut ukuran dan keluarga biaya acak. |
| [random_optimal_certificates.json](results/random_optimal_certificates.json) | 300 optimum acak dengan sertifikat numerik. |
| [reproduction.csv](results/reproduction.csv) | 207 perbandingan historis inti: klaim sumber versus reproduksi/LP. |
| [source_sensitivity.csv](results/source_sensitivity.csv) | Ringkasan sensitivitas setelah mengecualikan matriks sumber berkonflik. |
| [summary.csv](results/summary.csv) | Statistik semua konfigurasi: gap, hits, perbaikan, ties, memburuk, kegagalan dan waktu. |
| [tie_diagnostics.csv](results/tie_diagnostics.csv) | Hasil beberapa konvensi seri pada contoh yang diaudit. |
| [tie_enumeration.csv](results/tie_enumeration.csv) | Biaya yang dapat dicapai lewat seluruh seri yang diizinkan pada contoh kecil. |
| [verification.txt](results/verification.txt) | Ringkasan pemeriksaan algoritma dan enumerasi optimum kecil. |
| [worked_example_L05_Example1.json](results/worked_example_L05_Example1.json) | Bukti soal bersama: baseline, tiap kandidat/completion, margin, ketiga konstruksi MRM, alokasi dan sertifikat LP. |

## solver/

| Berkas | Maksud/kegunaan |
|---|---|
| [__init__.py](solver/__init__.py) | Penanda paket Python untuk impor dan pemanggilan python -m. |
| [optimal_lp.py](solver/optimal_lp.py) | LP SciPy/HiGHS untuk optimum pembanding dan sertifikat primal-dual. |
