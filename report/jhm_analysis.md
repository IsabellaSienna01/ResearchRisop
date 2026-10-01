# Hasil pendalaman JHM

Tanggal: 1 Oktober 2026. IHW dilewati atas permintaan pengguna. **A** = paper yang diberikan pengguna; **B** = literatur eksternal; **C** = implementasi, eksperimen, atau analisis proyek ini. Angka hasil eksperimen di bawah berasal dari berkas CSV, bukan perkiraan.

## Identitas dan batas sumber

JHM adalah **Juman & Hoque Method**, sebuah heuristik pembentukan solusi awal yang memulai dari alokasi demand per kolom, kemudian memperbaiki pelanggaran supply. Sumber asli adalah Juman dan Hoque (2015), *An efficient heuristic to obtain a better initial feasible solution to the transportation problem*, Applied Soft Computing, [DOI 10.1016/j.asoc.2015.05.009](https://doi.org/10.1016/j.asoc.2015.05.009). Preview penerbit dapat dibaca; pohon keputusan lengkap artikel asli belum berhasil diakses.

Sumber tambahan yang diperiksa:

| Sumber | Yang benar-benar tersedia | Implikasi |
|---|---|---|
| Indrawan, Affandi, Soesanto (2021), EPSILON 15(1), 27–45, [DOI 10.20527/epsilon.v15i1.2876](https://doi.org/10.20527/epsilon.v15i1.2876) | Metadata penerbit dan bagian halaman yang terindeks: teorema 4.2–4.4, langkah algoritma, sebagian contoh | Mendukung aturan seri dan keberadaan keputusan antarbaris yang lebih rumit; bukan akses utuh artikel |
| Skripsi Andry Nor Indrawan, ULM (2021), E21 | Satu halaman sampul | Tidak dipakai sebagai bukti algoritma atau angka |
| Sulfina Eka Rahayu, UNHAS (2024), E22, [rekaman repositori](https://repository.unhas.ac.id/36713/) | 24 halaman sampul dan Bab 1–2; ringkasan enam langkah JHM | Membantu memeriksa urutan perbaikan donor; bab hasil tidak tersedia. Tautan berkas penuh mengembalikan HTTP 401 |
| Juman & Nawarathne (2019), E19, [DOI 10.4038/cjs.v48i1.7584](https://doi.org/10.4038/cjs.v48i1.7584) | Artikel penuh, sembilan matriks Appendix A dan perbandingan JHM | Sumber benchmark tambahan; algoritma NM/JNM yang dimulai per baris tidak diganti nama menjadi JHM |
| Paper BCE L01 dan SSM L03 yang diberikan pengguna | Matriks, biaya JHM pembanding, dan pembahasan transfer | Menguji biaya dan alokasi pada contoh yang sumbernya tersedia penuh |

Unduhan E18 gagal karena sertifikat TLS kedaluwarsa lalu HTTP 403; akses melalui indeks hanya sebagian. Pada beberapa baris excess, teorema E18 melibatkan hubungan antarpenerima dan biaya urutan ketiga. Karena seluruh keputusan tersebut belum terverifikasi, tidak dibuat aturan pengganti yang kemudian disebut JHM asli.

## Algoritma yang benar-benar diimplementasikan

Nama eksperimen adalah **JHM terbatas / `JHM_single`**, bukan implementasi lengkap JHM 2015. Kode: [jhm.py](../methods/jhm.py); protokol: [jhm_protocol.md](../experiments/jhm_protocol.md).

1. Validasi matriks dan margin. Jika demand lebih besar, tambahkan dummy source berbiaya nol. Jika supply lebih besar, jangan masukkan dummy destination saat pemilihan awal; catat sisa supply sebagai alokasi dummy setelah perbaikan.
2. Alokasikan seluruh demand setiap kolom pada biaya minimum kolom. Seri minimum yang belum ditentukan sumber diselesaikan dengan indeks terkecil, sebagai konvensi implementasi.
3. Hitung `e_i = jumlah alokasi baris i − supply_i`. Bekukan baris dengan `e_i=0`. Jika pada pemilihan donor terdapat lebih dari satu baris excess, keluarkan status **unverified**; jangan gunakan fallback.
4. Pada donor i yang dipilih, untuk setiap sel positif `(i,j)`, cari penerima r berbiaya terendah di antara baris belum dibekukan. Hitung `Delta = C_rj − C_ij`.
5. Pilih Delta terkecil. Pada seri, interpretasi teorema 4.2 E18 mendahulukan biaya donor lebih tinggi; sisa seri menggunakan indeks.
6. Pindahkan `q = min(X_ij, e_i)` ke penerima. Penerima dapat menjadi excess. Selesaikan donor yang sudah dipilih sebelum memilih donor berikutnya; ini bukan memilih ulang seluruh baris setelah setiap transfer.
7. Bekukan baris yang tepat terpenuhi. Ulangi sampai tidak ada excess. Bila kemudian diperlukan cabang antarbaris yang belum terverifikasi, simpan status tersebut tanpa meneruskan dengan aturan karangan.
8. Audit konservasi, nonnegativitas, biaya asli, dan struktur basis. Sel basis nol melengkapi degenerasi tanpa menambah pengiriman epsilon.

Cabang ini berhasil pada **55/84** input inti dan **73/300** input acak. Sisanya tidak membuktikan kegagalan JHM asli: statusnya menunjukkan batas sumber/implementasi proyek. Karena itu, mean gap subset tersebut tidak boleh dibandingkan langsung dengan mean metode lain pada semua 84/300 input.

## Reproduksi dan pengaruh aturan seri

| Kasus | Biaya JHM dalam paper | JHM terbatas, seri biaya donor tinggi | Diagnostik seri indeks | Optimum LP |
|---|---:|---:|---:|---:|
| L01, Table 2, 3×4 | 460 | 460 | 460 | 435 |
| L03, Table 2, 3×3 | 475 | 473 | 475 | 465 |
| L01, aplikasi nyata 2×94 | 12.175.097 | 12.175.097 | Tidak diuji di tabel ini | 12.175.097 |

Pada L01, kedua aturan seri menghasilkan biaya sama, tetapi alokasi berbeda; alokasi tercetak cocok dengan seri indeks. Pada L03, seri indeks menjelaskan salah satu jalan menuju angka 475. Ini **tidak membuktikan** bahwa seluruh algoritma asli menggunakan seri indeks. Baseline tidak diubah setelah melihat hasil untuk memaksakan kecocokan. [Audit seri](../results/jhm_tie_sensitivity.csv) menyimpan keduanya.

Audit tambahan sepuluh kemunculan sumber memuat sembilan matriks E19 dan aplikasi nyata L01. Enam merupakan duplikat persis input inti; empat merupakan matriks baru, termasuk satu transkripsi Deshmukh yang perlu kehati-hatian. Dari sepuluh klaim biaya JHM tambahan, enam cocok, satu berbeda, dan tiga membutuhkan cabang yang belum terverifikasi. Rincian semua angka: [jhm_supplement.md](jhm_supplement.md).

Pada Deshmukh, E19 mencetak demand pertama **40**, bukan angka **5** dalam instance seimbang yang lazim di sumber lain. Angka 40 dipertahankan. JHM/VAM menghasilkan 883, berbeda dari klaim 743/779, meskipun LP masih menghasilkan 743. Kesamaan optimum saja ternyata tidak menjamin kesamaan instance; jangan mencocokkan data berdasarkan optimum atau label saja. Appendix B yang disebut dalam E19 tidak ada dalam PDF yang diperoleh; tujuh klaim berikutnya tidak memiliki matriks terverifikasi.

## Kelemahan yang diuji dan modifikasi

Transfer baseline memenuhi donor tanpa selalu membatasi defisit penerima. Kelemahan yang diuji adalah **pembentukan excess baru akibat ukuran transfer**, bukan sekadar pernyataan umum bahwa JHM bersifat greedy.

| Varian | Langkah yang diubah | Formula/aturan | Risiko dan biaya tambahan |
|---|---|---|---|
| `cap_receiver` | Ukuran transfer | `q = min(X_ij, e_i, -e_r)` untuk penerima defisit | Membatasi overshoot, tetapi bisa membekukan penugasan yang mahal; pekerjaan per kandidat hampir sama, jumlah transfer berubah |
| `net_tie` | Seri Delta | Dahulukan `q*Delta` terkecil, lalu aturan seri baseline | Biaya langsung tetap tidak menangkap akibat lanjutan; tanpa parameter kontinu |
| `cap_net_tie` | Kedua komponen di atas | Gabungan pembatasan dan seri neto | Ablasi untuk mengetahui apakah komponen kedua memberi manfaat |
| `top2_completion` | Pemilihan transfer | Selesaikan dua calon transfer menggunakan JHM terbatas baseline, pilih biaya akhir lebih rendah, komit hanya satu transfer | Hingga dua penyelesaian per keputusan; bila salah satu memerlukan cabang tidak diketahui, seluruh varian ditandai unverified |

Tidak ada LP dalam aturan pemilihan. LP hanya menghitung pembanding optimum. Pembatasan transfer merupakan prinsip kelayakan yang sudah dikenal; BCE/SSM telah memodifikasi keluarga transfer JHM; penyelesaian kandidat merupakan adaptasi rollout. Keempatnya **tidak diklaim baru**. Tidak ada bukti cukup bahwa kombinasi khusus yang diuji merupakan kontribusi orisinal.

## Hasil eksperimen berpasangan

Semua input dicoba dan semua pengecualian disimpan. Tabel menggunakan **irisan input yang berhasil pada baseline dan varian**, sehingga perbandingan mean memakai denominator sama.

| Suite / varian | Jumlah pasangan | Mean gap baseline % | Mean gap varian % | Membaik | Sama | Memburuk |
|---|---:|---:|---:|---:|---:|---:|
| Inti / cap_receiver | 55 | 2,0929 | 1,9147 | 15 | 28 | 12 |
| Inti / net_tie | 55 | 2,0929 | 1,9019 | 3 | 50 | 2 |
| Inti / cap_net_tie | 55 | 2,0929 | 1,9147 | 15 | 28 | 12 |
| Inti / top2_completion | 55 | 2,0929 | 1,0400 | 7 | 48 | 0 |
| Acak / cap_receiver | 73 | 3,6944 | 6,4576 | 14 | 39 | 20 |
| Acak / net_tie | 72 | 3,2725 | 3,0028 | 1 | 71 | 0 |
| Acak / cap_net_tie | 73 | 3,6944 | 6,4576 | 14 | 39 | 20 |
| Acak / top2_completion | 70 | 3,3185 | 0,8971 | 19 | 51 | 0 |

Gabungan cap+net_tie tidak menambah manfaat pada data ini. Varian completion mempunyai hasil lebih baik pada subset, tetapi keberhasilan hanya 70/300 input acak sangat membatasi generalisasi. Angka yang lebih kecil bukan dasar menempatkannya di atas VAM atau THP yang berjalan pada seluruh suite.

| Contoh | Baseline terbatas | cap_receiver | LP optimum | Gap awal % | Gap modifikasi % | Penghematan |
|---|---:|---:|---:|---:|---:|---:|
| L01 Table 2 | 460 | 435 | 435 | 5,7471 | 0 | 25 |
| L03 Table 2 | 473 | 465 | 465 | 1,7204 | 0 | 8 |
| L02 Table 7 | 8.350 | 7.750 | 7.750 | 7,7419 | 0 | 600 |
| L05 Example 1 | 1.045 | 985 | 985 | 6,0914 | 0 | 60 |
| RBSM_N01 / E19 Ramadan | 5.600 | 6.880 | 5.600 | 0 | 22,8571 | **−1.280** |

Selain dua klaim lokal yang disebut sebelumnya, biaya JHM lintas-paper di tabel ini adalah hasil implementasi kita, bukan klaim JHM yang dibuat paper pemilik matriks.

## Contoh manual pertama: L01 Table 2

```text
C = [[10, 2,20,11],
     [12, 7, 9,20],
     [ 4,14,16,18]]
s = [15,25,10]
d = [ 5,15,15,15]
```

Alokasi minimum per kolom membuat baris pertama memuat 30, baris kedua 15, dan baris ketiga 5. Excess donor pertama 15; defisit penerima kedua 10. Transfer termurah adalah kolom kedua dengan Delta=7−2=5.

Baseline memindahkan 15 dan membuat baris kedua excess 5. Modifikasi cap memindahkan 10, tepat memenuhi baris kedua. Donor pertama masih excess 5, lalu memindahkan 5 di kolom keempat ke baris ketiga. Alokasi akhir modifikasi:

```text
X = [[0, 5, 0,10],
     [0,10,15, 0],
     [5, 0, 0, 5]]
Z = 5*2 + 10*11 + 10*7 + 15*9 + 5*4 + 5*18 = 435.
```

LP mengonfirmasi optimum 435. Ini contoh yang mudah dipresentasikan, tetapi kegagalan pada Ramadan dan suite acak harus disertakan jika dijadikan bahan proyek.

## Kesimpulan khusus JHM

Ada peluang modifikasi yang konkret pada ukuran transfer dan aturan seri. Namun, **cap_receiver belum layak dinyatakan perbaikan JHM yang konsisten**: pada pasangan acak, mean gap naik dan kasus memburuk lebih banyak daripada membaik. Completion menjanjikan pada subset, tetapi implementasi lengkap dan cakupan benchmark masih menjadi hambatan utama.

Untuk proyek yang harus segera menghasilkan baseline terpercaya dan eksperimen menyeluruh, bukti saat ini lebih mendukung THP atau VAM. JHM cocok sebagai penelitian lanjutan tentang reproduksi dan keputusan transfer jika sumber lengkap dapat diperoleh. Hasil yang belum terverifikasi tidak dianggap salah, optimum, atau selesai.

Artefak: [seluruh 1.930 percobaan](../results/jhm_restricted.csv), [ringkasan](../results/jhm_summary.csv), [alokasi dan jejak keputusan](../results/jhm_allocations.json), [audit tambahan 430 percobaan](../results/jhm_supplement.csv), [sertifikat LP tambahan](../results/jhm_supplement_optimal.json), [pemeriksaan implementasi](../results/jhm_verification.txt).
