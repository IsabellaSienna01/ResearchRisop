# Hasil seluruh riset dan kesimpulan untuk proyek mahasiswa

Tanggal pembaruan: **1 Oktober 2026**. IHW **dilewati atas permintaan Anda**. Pendalaman JHM sudah dilakukan sampai implementasi cabang yang dapat diverifikasi, pengujian, dan analisis kegagalan. Ini sintesis seluruh pekerjaan yang benar-benar selesai; bagian yang belum terverifikasi tetap ditandai.

**Kesimpulan utama:** THP merupakan titik awal paling mudah dipertanggungjawabkan dari paper yang Anda berikan, VAM menawarkan hasil kualitas terkuat di antara tiga arah modifikasi yang dipilih, dan MRM merupakan alternatif dengan tambahan komputasi lebih kecil tetapi bukti perbaikannya bersyarat. JHM mempunyai titik modifikasi yang jelas, namun belum lebih siap daripada THP/VAM karena keterbatasan reproduksi algoritma lengkap dan hasil modifikasi sederhana yang tidak konsisten.

## 1. Cakupan dan cara membaca hasil

Lima PDF lokal telah diinventarisasi sebelum pencarian eksternal. Literatur kemudian ditelusuri melalui DOI, judul, penerbit, referensi, dan sumber tambahan penulis. **A** menunjukkan informasi dari paper Anda, **B** literatur eksternal, dan **C** analisis/hasil komputasi proyek ini. Sumber dibedakan dari klaim penulis dan dari hasil yang berhasil direproduksi.

| Pekerjaan | Hasil yang tersedia |
|---|---|
| Data utama | 140 kemunculan contoh dalam sumber; 86 matriks mentah berbeda; **84** setelah menghapus duplikasi yang setara setelah balancing |
| Baseline utama | 14 konfigurasi: NWCM, LCM, VAM, LDVAM, RAM, TDM1, TDM2, TDSM, THP, SSM, CSM, RBSM, BCE, MRM |
| Modifikasi utama | 24 variasi; 2.064 percobaan pada 86 input mentah |
| Uji tambahan acak | **300** masalah, seed 20261001, ukuran 3×3, 4×4, 5×5, 6×6, 10×10; biaya seragam, banyak seri, dan menceng |
| JHM lanjutan | 1.930 percobaan baseline terbatas + empat varian; pengecualian tetap disimpan |
| Audit sumber tambahan JHM | 10 kemunculan contoh, termasuk aplikasi nyata BCE 2×94; enam duplikat persis suite inti; 430 percobaan terpisah |
| Ground truth | LP transportasi melalui SciPy/HiGHS, pemeriksaan primal–dual, kelayakan, biaya, dan degenerasi; 24 optimum kecil juga diperiksa dengan enumerasi integer |

Angka 84 bukan seluruh benchmark asli dari setiap paper. Sebagian sumber hanya memberikan tabel hasil atau data yang saling bertentangan. Contoh tambahan JHM dipisahkan agar suite utama tetap sama; duplikat tidak dianggap validasi independen tambahan. **Empat belas konfigurasi juga bukan empat belas metode unik sesuai daftar awal**: IBFS pada DOI Anda adalah BCE; TDM punya dua varian; THP dan LDVAM merupakan tambahan.

Semua heuristik yang teridentifikasi di sini menghasilkan solusi awal. MODI/transportation simplex memperbaiki solusi tersebut; LP digunakan sebagai pembanding optimum. Biaya IBFS lebih rendah belum membuktikan jumlah iterasi optimisasi selanjutnya lebih sedikit.

## 2. Hasil setiap metode

Mean gap berikut menggunakan 84 input inti dengan konvensi implementasi yang dinyatakan. Nilai ini menunjukkan hasil pada dataset tersebut, bukan peringkat universal. Detail langkah, seri, balancing, dan algoritma tersedia dalam [terminologi dan algoritma](terminology_and_algorithms.md).

| Metode | Inti aturan dan hasil | Kelemahan/titik modifikasi | Kesimpulan praktis |
|---|---|---|---|
| **VAM** | Selisih dua biaya terkecil; mean gap **3,718%**; ketiga biaya VAM pada L05 berhasil direproduksi | Komit pada satu calon tanpa menghitung akibat sisa alokasi | Kandidat utama; top-2 completion teruji |
| **IHW** | Identitas sumber belum terverifikasi | Tidak dibuat ekspansi atau algoritma dugaan | **Dilewati**, bukan penelitian tertunda yang menunggu jawaban Anda |
| **SSM** | Supply Selection Method, DOI 2022; perbaikan alokasi berdasarkan supply dan jumlah baris excess; gap **2,603%**; contoh lokal 465 cocok | Prioritas supply awal dan transfer yang melewati defisit penerima | Baseline berguna; modifikasi khusus masih berupa rancangan, belum diuji di sini |
| **IBFS-related DOI** | DOI 10.1016/j.jksuci.2020.07.007 mendefinisikan **BCE** | Bukan metode terpisah | Jangan dihitung dua kali |
| **MRM** | Maximum Range Method versi biaya Wireko 2025; orientasi baris/kolom dikunci; gap **2,758%** | Keputusan orientasi pertama mengikat seluruh konstruksi | Kandidat ketiga bersyarat; 13 baseline asli cocok, tetapi ensemble tidak memperbaiki 13 contoh itu |
| **CSM** | Cost Supply Method 2026; skor supply × total biaya baris; gap **2,275%**; contoh 1.780 cocok | Skor statis, biaya transfer bruto, perbedaan narasi/pseudocode | Perlu penyelesaian inkonsistensi sumber sebelum menjadi proyek utama |
| **RBSM** | Rihan–Bilqis–Saikhu Method 2026; prioritas biaya × supply; gap **2,539%**; contoh 111 dan 7.750 cocok | Produk supply awal dan seri transfer; kode penulis berbeda dari narasi | Layak pembanding dengan label versi, belum pilihan pertama modifikasi |
| **JHM** | Juman & Hoque 2015; alokasi demand lalu perbaikan excess; baseline terbatas berhasil pada 55/84 dan 73/300 | Transfer dapat membuat penerima excess; seri memengaruhi hasil | Modifikasi sudah diuji, tetapi cakupan parsial melarang peringkat langsung dengan metode lengkap |
| **TDSM** | Jumlah pangkat selisih dari minimum baris, baseline theta=2; gap **2,285%** | Kuadrat memperbesar pengaruh selisih ekstrem; theta sumber tidak selalu jelas | Theta=1,5 sudah bagian keluarga formula terbitan; hasil 5 membaik, 8 memburuk pada 84 kasus |
| **TDM** | TDM1 memakai baris; TDM2 baris dan kolom; gap **2,801% / 3,747%** | Mengabaikan ukuran alokasi; jumlah sel memengaruhi skor garis | Beberapa angka sumber tidak dapat direproduksi bahkan dengan enumerasi seri; kandidat cadangan |
| **BCE** | Cabang modulo supply/selisih biaya; contoh lokal 435 cocok | Sensitif skala biaya dan belum jelasnya pembaruan first/second least cost | 15/84 dan 96/300 gagal/tidak tersedia dalam interpretasi ini; mean subset tidak layak dijadikan peringkat |
| **RAM** | Russell: pilih minimum `C_ij−maks_baris−maks_kolom`; gap **2,374%** | Maksimum dapat terdistorsi outlier; seri opportunity score | Pembanding kuat dan cukup sederhana; usulan modifikasi belum diuji |
| **LCM** | Pilih biaya global terkecil; gap **9,263%** | Rute murah dapat menghabiskan kapasitas yang lebih dibutuhkan tujuan lain | Sangat mudah dijelaskan, tetapi versi top-2 tetap kalah mean gap dari VAM biasa pada suite acak |
| **NWCM** | Alokasi sudut kiri atas berdasarkan urutan input; gap **35,083%** | Tidak mempertimbangkan biaya | Pembanding dasar; menambahkan pilihan biaya global akan mendekatkannya ke LCM, dengan risiko kebaruan rendah |
| **THP**, tambahan | Dua tingkat penalti rentang tertinggi, kemudian minimum biaya × alokasi; gap **7,023%** | Produk biaya saat ini tidak mengukur mahalnya solusi sisa | Kandidat paling jelas untuk presentasi dari paper Anda; ketiga baseline asli cocok |

SSM pada paper lain bisa berarti *Stepping Stone Method*, yang berbeda tahap dari Supply Selection Method. MRM untuk minimisasi waktu juga berbeda tujuan dari MRM biaya yang dipakai. Nama lengkap TDSM sebagaimana daftar Anda tidak secara eksplisit muncul di heading sumber Hosseini; rumus dan label TDSM terverifikasi, perlu hati-hati dalam penulisan ekspansi.

BCE menunjukkan contoh kelemahan konkret: pada matriks L01, mengalikan semua biaya dengan 10 mengubah hasil interpretasi algoritma dari 435 menjadi 460 ketika dikembalikan ke satuan biaya semula. Masalah optimisasinya ekuivalen, tetapi keputusan modulo berubah. Ini temuan eksperimen implementasi yang dinyatakan, bukan bukti bahwa seluruh versi BCE pasti gagal.

## 3. Bukti perbaikan yang benar-benar dihitung

Untuk minimisasi: `Gap = Z−Z_opt`; `Gap% = 100*(Z−Z_opt)/Z_opt`; `Accuracy = 100*Z_opt/Z` ketika Z≥Z_opt. Selisih persentase berikut merupakan penurunan **poin persentase**, bukan persentase penghematan biaya. Kasus biaya optimum nol ditangani terpisah dalam kode.

| Baseline → modifikasi | Mean gap inti: awal → baru | Membaik / sama / memburuk, n=84 | Mean gap acak: awal → baru | Membaik / sama / memburuk, n=300 |
|---|---|---|---|---|
| **VAM → top-2 VAM completion** | **3,718% → 0,876%** | **29 / 55 / 0** | **12,968% → 5,032%** | **117 / 183 / 0** |
| **THP → top-2 THP completion** | **7,023% → 2,132%** | **48 / 36 / 0** | **13,647% → 6,264%** | **182 / 118 / 0** |
| **MRM → pilihan terbaik orientasi** | **2,758% → 1,184%** | **24 / 60 / 0** | **10,904% → 6,159%** | **111 / 189 / 0** |
| LCM → top-2 LCM completion | 9,263% → 4,948% | 48 / 36 / 0 | 30,397% → 16,172% | 174 / 126 / 0 |

VAM mencapai optimum pada 44→63 dari 84 kasus; THP 26→52; MRM 46→66. Pada 300 kasus acak: VAM 128→154, THP 59→122, MRM 85→116. Tabel lengkap memuat median, simpangan baku, kasus terburuk, akurasi, dan kegagalan: [performance_tables.md](performance_tables.md).

| Masalah dan eksperimen | Baseline | Modifikasi | Optimum LP | Gap awal → baru | Penghematan |
|---|---:|---:|---:|---|---:|
| L05 Example 1, THP | 1.045 | 985 | 985 | 6,0914% → 0% | 60 |
| L05 Example 1, VAM | 1.095 | 985 | 985 | 11,1675% → 0% | 110 |
| L05 Example 2, VAM | 5.125 | 4.525 | 4.525 | 13,2597% → 0% | 600 |
| L01 Table 2, VAM | 475 | 435 | 435 | 9,1954% → 0% | 40 |
| E01 Hosseini Example 1, MRM | 3.710 | 3.460 | 3.460 | 7,2254% → 0% | 250 |

Empat baris pertama memiliki biaya baseline yang cocok dengan paper terkait. Baris MRM adalah **eksperimen lintas-paper kita**: paper Hosseini 2017 menyediakan matriks, bukan biaya MRM 2025. Tidak ada klaim bahwa Hosseini melaporkan metode yang belum terbit saat itu.

## 4. Apa yang sebenarnya diubah?

Penjelasan langkah demi langkah, pseudocode, sumber ide dan batas kebaruan kini tersedia terpisah dalam [VAM](../modifications/vam_top2_rollout.md), [THP](../modifications/thp_top2_rollout.md), dan [MRM](../modifications/mrm_orientation_ensemble.md), diperbarui 2 Oktober 2026. [Demo program](../modifications/README.md) menjalankan implementasi yang menghasilkan tabel di laporan ini. [Panduan folder](../STRUKTUR_FOLDER.md) menjelaskan setiap kelompok data, kode dan hasil.

**VAM dan THP:** pertahankan penalti, balancing, aturan jumlah alokasi, dan eliminasi baseline. Ubah hanya keputusan final sel. Ambil dua sel berbeda teratas menurut urutan baseline, termasuk pilihan asli. Untuk kandidat a=(i,j), hitung:

`q_a = min(sisa_supply_i, sisa_demand_j)`

`F(a) = q_a*C_ij + biaya penyelesaian heuristik H pada masalah sisa`

H adalah VAM asli untuk modifikasi VAM, THP asli untuk modifikasi THP. Pilih F terkecil, pertahankan urutan asli saat seri, komit hanya alokasi pertama, lalu ulangi. **LP tidak digunakan untuk memilih kandidat.** Ini look-ahead satu keputusan dengan penyelesaian heuristik penuh sebagai evaluasi, bukan sekadar satu scan biaya minimum.

Pada THP, dua tingkat penalti sudah bagian metode asli. Kontribusi eksperimen ini adalah evaluasi akibat pada masalah sisa **sesudah** filter THP, bukan mengklaim penemuan top-2. Menggunakan kebijakan penyelesaian yang sama dan selalu memasukkan pilihan baseline memberi sifat non-worsening relatif terhadap baseline deterministik itu. Alasannya: pilihan asli selalu tersedia dengan estimasi biaya baseline, dan argumen tersebut diulang pada setiap sisa masalah. Ini penerapan prinsip rollout yang sudah dikenal, bukan teorema baru atau jaminan optimum.

**MRM:** jalankan versi asli, versi dipaksa berorientasi baris, dan versi dipaksa berorientasi kolom; kembalikan hasil feasible berbiaya paling rendah. Semua aturan selain orientasi dipertahankan. Ini kombinasi konstruksi sederhana, dengan paling banyak tiga eksekusi baseline.

## 5. Hasil JHM: ada perbaikan, tetapi belum konsisten

[Analisis khusus JHM](jhm_analysis.md) memuat sumber, pseudocode terbatas, semua batas akses, contoh manual, dan tabel hasil. Ringkasan terpenting:

- Pada L01 Table 2, JHM terbatas mereproduksi **460**. Pembatasan transfer `q=min(alokasi_sel, excess_donor, defisit_penerima)` menghasilkan **435**, sama dengan optimum. Gap turun **5,7471% → 0%**.
- Pada L03, seri yang mendahulukan biaya donor lebih tinggi menghasilkan **473**, sedangkan paper melaporkan **475**. Seri indeks menghasilkan 475. Perbedaan ini didokumentasikan; baseline tidak diam-diam diubah untuk memaksakan kecocokan.
- Pada 55 pasangan input inti, pembatasan transfer memberi **15 membaik, 28 sama, 12 memburuk**. Pada 73 pasangan acak: **14 membaik, 39 sama, 20 memburuk**; mean gap malah naik **3,6944% → 6,4576%**.
- Contoh negatif jelas: Ramadan/RBSM_N01 naik **5.600 → 6.880**, padahal 5.600 sudah optimal. Overshoot yang tampak tidak baik secara lokal ternyata tidak selalu perlu dihilangkan.
- Top-2 completion JHM mengurangi mean gap **2,0929% → 1,0400%** pada 55 pasangan inti dan **3,3185% → 0,8971%** pada 70 pasangan acak, tanpa memburuk pada pasangan tersebut. Cakupan parsial ini tidak boleh dipakai untuk mengunggulkan JHM atas metode yang diuji pada seluruh suite.

Bagian beberapa baris excess dalam algoritma lengkap belum terverifikasi. Implementasi berhenti dengan status `unverified`, tidak menggantinya dengan heuristik lain. Pembatasan ini berasal dari akses sumber, bukan bukti bahwa JHM asli tidak bisa menyelesaikan input tersebut.

Audit lanjutan juga mengekstrak aplikasi nyata **2×94** dari paper BCE yang terlewat pada inventaris awal. Biaya BCE, VAM, dan JHM **12.175.097** cocok dengan paper serta optimum LP; TDM1 **12.208.071** juga cocok. TOCM-MT tetap klaim sumber yang tidak direproduksi. Dalam uji baru terpisah, THP 12.714.389→12.282.430, masih di atas optimum, dan MRM 12.264.685→12.175.097. Lihat [audit tambahan](jhm_supplement.md).

## 6. Modifikasi gagal, seri, dan ablasi

Tidak semua ide sederhana menguntungkan. Semua varian disimpan, termasuk:

| Ide | Hasil negatif penting |
|---|---|
| Penalti VAM × alokasi | Memburuk pada **31/84** dan **135/300** kasus |
| Penalti VAM × akar alokasi | Memburuk pada **22/84** dan **107/300** kasus |
| Dua kandidat LCM, pilih biaya × alokasi terendah | Memburuk pada **21/84** dan **118/300** kasus |
| THP dengan estimasi lower bound murah | Example 3 berubah **2.366 → 2.430** |
| THP dengan penyelesaian LCM | Memburuk pada **1/84** dan **16/300** kasus; jaminan relatif terhadap THP hilang |
| Skor LCM berbobot alpha=0,25 | Mean gap acak **31,928%**, lebih buruk daripada LCM **30,397%** |
| VAM top-2 ditambah seri alokasi maksimum | Tidak membantu dibanding top-2 biasa; memburuk pada satu kasus inti relatif baseline indeks |
| JHM cap + net tie | Tidak menambah manfaat dibanding cap saja pada data ini |

Ablasi menunjukkan bahwa evaluasi hanya keputusan pertama THP tetap menghasilkan **1.045**, sedangkan evaluasi berulang menghasilkan **985**. Pilihan yang menguntungkan baru muncul pada keputusan kedua. Pada VAM, top-2 sekali di awal menghasilkan mean gap inti 1,981%, sedangkan berulang 0,876%. Top-3 lebih baik lagi pada mean acak, tetapi membutuhkan lebih banyak perhitungan. Jangan menambahkan komponen tanpa menguji kontribusinya sendiri.

## 7. Literatur serupa dan batas kebaruan

THP 2021 dan IVAM 2011 sudah menggunakan penyaringan beberapa kandidat. iLCM 2016 sudah memiliki seri alokasi maksimum. Metode berbasis kapasitas 2024 sudah menghubungkan skor dengan jumlah alokasi. TDM2 dan eksponen fractional TDSM sudah diterbitkan. MRCM/MRRM dan varian rentang terdahulu mendahului MRM 2025. [Bertsekas, Tsitsiklis, dan Wu (1997)](https://www.mit.edu/~jnt/Papers/J066-97-rollout.pdf) merupakan prior art untuk prinsip rollout.

Pencarian tambahan menemukan [DSO-VAM, Rashid & Mondal (2026)](https://doi.org/10.4236/ojop.2026.152003), yang menggabungkan dua ukuran rentang, opportunity score, dan bobot kapasitas. Artikel dibaca sebagai bukti literatur serupa; **hasil numeriknya belum direproduksi** dan tidak dimasukkan dalam peringkat.

Dengan bukti sekarang, sebut usulan sebagai **adaptasi atau kombinasi aturan yang diuji secara reproducible**, bukan “metode baru yang belum pernah ada”. Untuk kombinasi spesifik VAM/THP dua sel dan completion yang diuji, tidak ditemukan kecocokan persis dalam sumber yang telah diperiksa, tetapi beberapa artikel pembanding lengkap masih tidak tersedia. Itu tidak membuktikan kebaruan. [Katalog modifikasi](modification_catalog.md) mencantumkan 2–4 arah tiap metode teridentifikasi, rumus, risiko, kompleksitas, parameter, dan status uji.

## 8. Kualitas sumber, komputasi, dan batas kesimpulan

Audit utama memuat **207 perbandingan klaim: 177 cocok, 23 berbeda, 7 tidak tersedia**. Ini jumlah pekerjaan audit, bukan tingkat keberhasilan metode; beberapa baris adalah klaim optimum atau pengulangan sumber. Hasil JHM terbaru dan audit tambahan dicatat terpisah agar catatan audit awal tidak ditimpa.

Paper AIP L04 memiliki ketidaksesuaian hitungan dan tabel ringkasan; contoh pertamanya menyebut optimum 61 walaupun alokasi feasible 55 tersedia dan LP mengonfirmasi 55. Beberapa hasil TDM/TDSM tidak dapat diperoleh melalui aturan dan seri yang diizinkan. Dataset CSM memuat konflik angka/label, sehingga label yang sama tidak otomatis berarti matriks sama. Analisis sensitivitas dengan menghapus dua matriks sumber yang berkonflik tidak mengubah arah kesimpulan tiga kandidat.

Tambahan waktu tidak selalu kecil. Pada pengukuran terkontrol 30 kasus dengan tiga pengulangan, median rasio waktu sekitar **7,3× untuk VAM**, **6,6× untuk THP**, dan **2,9× untuk MRM**. Ini hasil Python pada mesin ini. Jika B biaya satu konstruksi dan T jumlah alokasi, completion berulang kira-kira `O(k*T*B)`, bukan sekadar k kali baseline. Ensemble MRM paling banyak `3B`. Matriks besar seperti 2×94 lebih mahal untuk completion berulang.

Tidak ada jaminan dekat optimum untuk semua input. Gap terburuk VAM top-2 pada uji acak mencapai **152,063%**, THP **101,167%**, dan MRM **67,857%**. Uji acak satu seed bukan bukti untuk seluruh distribusi masalah nyata. Kegagalan interpretasi BCE, cabang JHM yang belum terverifikasi, data sumber yang hilang, dan beberapa tabel MRM besar yang belum tervalidasi visual tetap merupakan keterbatasan terbuka.

## 9. Pilihan proyek dan eksperimen pertama

| Arah | Kapan dipilih | Benchmark pertama | Risiko utama |
|---|---|---|---|
| **THP + evaluasi dua kandidat melalui completion** | Mengutamakan paper yang Anda miliki, kelemahan yang mudah dijelaskan, dan demonstrasi manual | L05, DOI 10.1109/ICTS52701.2021.9608005; **ketiga** contoh lengkap; pertama 1.045→985 | Hanya satu dari tiga contoh THP asli membaik; dua lainnya sudah optimum; prior art dan tambahan waktu |
| **VAM + top-2 VAM completion** | Mengutamakan kualitas rata-rata dari tiga arah terpilih dan baseline sederhana | Ketiga contoh L05; VAM asli cocok; dua membaik, satu sama | Kebaruan rendah untuk prinsip umum; aturan seri harus dibekukan |
| **MRM + pilihan terbaik orientasi** | Mengutamakan modifikasi singkat dan overhead relatif lebih kecil | Reproduksi 13 contoh MRM dahulu; kemudian E01 Example 1, 3.710→3.460 | **Tidak ada perbaikan pada 13 contoh kecil paper MRM sendiri**; membutuhkan benchmark lintas-paper |

Jika harus memilih satu sekarang, **pilih THP sebagai proyek pertama**, dengan VAM sebagai pembanding kuat. Judul kerja yang jujur: *Evaluasi Modifikasi Pemilihan Dua Kandidat Berbasis Penyelesaian Heuristik pada Two Highest Penalties untuk Mengurangi Optimality Gap Masalah Transportasi*. Judul ini menyatakan kegiatan dan tujuan tanpa menjanjikan optimum atau kebaruan yang belum dibuktikan.

Urutan pelaksanaan untuk tugas/presentasi:

1. Nyatakan versi THP, dua tingkat penalti berbeda, seri, dan dummy secara eksplisit.
2. Tampilkan reproduksi tiga contoh asli: 1.045, 4.525, 2.366; optimum 985, 4.525, 2.366.
3. Jelaskan keputusan kedua Example 1: biaya langsung 55 tampak lebih baik daripada 260, tetapi biaya total setelah completion menjadi 1.045 versus 985.
4. Tunjukkan perubahan hanya pada evaluasi kandidat, dengan rumus F(a); gunakan [contoh manual](manual_example.md).
5. Sajikan hasil ketiga contoh, lalu 84 kasus inti dan 300 acak; laporkan ties serta yang tetap nonoptimal.
6. Tampilkan ablasi first-only, top-2 berulang, lower bound, dan top-3; hindari hanya menampilkan pemenang.
7. Bahas waktu, degenerasi, batas dataset, dan literatur serupa sebelum menarik kesimpulan.

**Kesimpulan yang dapat Anda ambil:** mengevaluasi akibat sisa alokasi lebih menjanjikan pada eksperimen ini daripada sekadar mengalikan penalti dengan jumlah alokasi. Perbaikan harus dinilai pada masalah yang sama, terhadap LP, dengan baseline dan seri yang jelas. THP/VAM sudah memberikan bukti beberapa masalah dan uji acak; JHM cap memperlihatkan mengapa perubahan yang masuk akal secara lokal tetap harus diuji; MRM memberi pilihan sederhana dengan batas benchmark yang harus dinyatakan.

## 10. Berkas pendukung

- [Laporan rinci 35 bagian](research_report.md), [inventaris paper lokal](../paper_inventory.md), [referensi dan akses literatur](source_inventory.md), [log pencarian](search_log.md).
- [Data semua matriks inti](benchmark_catalog.md), [reproduksi klaim](reproduction_tables.md), [hasil seluruh baseline/modifikasi](performance_tables.md), [hasil tiap kasus shortlist](candidate_results.md), [ablasi](ablation_tables.md).
- [Analisis JHM](jhm_analysis.md), [hasil JHM terbatas](jhm_results.md), [audit sumber tambahan](jhm_supplement.md).
- [CSV baseline](../results/baseline.csv), [CSV modifikasi](../results/modifications.csv), [CSV acak](../results/random_benchmark.csv), [CSV JHM](../results/jhm_restricted.csv), [ringkasan statistik](../results/summary.csv).
- [README dan perintah reproduksi](../README.md), [status seluruh tahap](../progress.md).
- [Audit akhir](../results/artifact_audit.txt): ringkasan diperiksa terhadap hasil per kasus; 396 sertifikat primal–dual dan 4.333 alokasi tersimpan diperiksa ulang; tabel serta tautan lokal valid.
