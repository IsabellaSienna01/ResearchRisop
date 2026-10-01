# THP dengan evaluasi dua kandidat melalui penyelesaian THP

Dokumentasi implementasi per **2 Oktober 2026**. ID kode: **`THP_top2_rollout`**. Nama ini adalah label varian eksperimen proyek.

Untuk belajar melalui angka, langsung ke [bagian 6: contoh soal bersama, semua iterasi](#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai). Soalnya identik dengan contoh pada dokumen VAM dan MRM.

## 1. Asal metode dan status kebaruan

| Komponen | Referensi | Hubungannya dengan modifikasi |
|---|---|---|
| Baseline THP | Amaliah, Fatichah & Suryani (2021), *Two Highest Penalties: A Modified Vogels Approximation Method to Find Initial Basic Feasible Solution of Transportation Problem*, IEEE ICTS, 318–323, [DOI 10.1109/ICTS52701.2021.9608005](https://doi.org/10.1109/ICTS52701.2021.9608005) | Paper lokal **L05**, sumber utama algoritma dan tiga contoh yang direproduksi |
| Beberapa kandidat | THP sendiri; juga [Korukoglu & Balli (2011), IVAM](https://doi.org/10.3390/mca16020370) | Dua tingkat penalti dan penggunaan beberapa calon sudah ada; bukan kontribusi baru proyek |
| Prinsip completion/rollout | [Bertsekas, Tsitsiklis & Wu (1997)](https://www.mit.edu/~jnt/Papers/J066-97-rollout.pdf), [DOI 10.1023/A:1009635226865](https://doi.org/10.1023/A:1009635226865) | Referensi konsep evaluasi pilihan melalui heuristik lanjutan; bukan paper THP-rollout |
| Rancangan yang diuji | Kode dan eksperimen proyek | Setelah filter THP asli, ambil dua sel teratas, evaluasi dengan completion THP, dan ulangi pada setiap alokasi |

**Klasifikasi: C, kombinasi/adaptasi ide yang sudah ada; kebaruan belum terbukti.** Kode ini dibuat dalam proyek, bukan disalin dari kode resmi penulis THP. Paper THP tidak boleh dikutip seolah-olah melaporkan hasil varian completion kita. Prinsip top-2 dan rollout sudah memiliki referensi; yang diuji adalah kombinasi aturan yang dijelaskan di bawah. Belum ditemukan kecocokan persis dalam sumber yang sudah diperiksa, tetapi itu bukan bukti originalitas.

## 2. Algoritma THP baseline

1. Validasi C, s, d; tambahkan dummy nol jika total berbeda. Gunakan hanya baris/kolom dengan sisa margin positif.
2. Hitung rentang setiap garis aktif: `P_l = max(C pada garis l) − min(C pada garis l)`.
3. Ambil **dua nilai penalti berbeda tertinggi**. Semua garis yang memiliki salah satu nilai tersebut ikut; jika hanya ada satu tingkat, ambil tingkat itu.
4. Dari setiap garis terpilih, kumpulkan semua sel dengan biaya minimum. Hapus duplikat sel yang dipilih melalui baris sekaligus kolom.
5. Untuk setiap sel calon, hitung `CA_ij=C_ij*min(s_i,d_j)`. Urutkan CA menaik, lalu biaya C menaik, lalu indeks baris/kolom menaik untuk seri tersisa. Baseline memilih urutan pertama.
6. Alokasikan `q=min(s_i,d_j)`; perbarui margin, keluarkan garis habis, ulangi sampai supply habis. Lakukan audit dan lengkapi basis nol bila degenerat.

**Dua tingkat penalti dapat menghasilkan lebih dari dua garis dan lebih dari dua sel.** Ini berbeda dari pembatasan dua sel pada modifikasi. Seri akhir yang tidak ditentukan paper dilengkapi dengan indeks; konvensi ini dinyatakan dan berhasil mereproduksi ketiga biaya THP lokal.

## 3. Titik kelemahan dan perubahan tepat

CA mengukur pengeluaran pengiriman saat ini. Nilai CA kecil bisa menang hanya karena kuantitas kecil, padahal pilihan itu meninggalkan rute mahal. Hipotesis eksperimen: bandingkan juga biaya penyelesaian sisa.

**Langkah 1–4 dan 6 tidak berubah. Langkah 5 diubah setelah urutan CA terbentuk:**

1. Ambil dua sel berbeda pertama dari urutan CA THP; gunakan satu jika hanya satu tersedia. Calon asli selalu ikut.
2. Untuk tiap calon a, coba sementara alokasi maksimum `q_a=min(s_i,d_j)`.
3. Selesaikan masalah sisa dengan **THP baseline**, memakai dua tingkat penalti, CA dan seri yang sama.
4. Hitung `F(a)=q_a*C_ij+Z_THP(sisa setelah a)`.
5. Pilih F minimum; seri mempertahankan urutan CA semula. Komit hanya alokasi pertama calon terpilih, kemudian ulangi seluruh proses pada margin baru.

```text
Balance(C,s,d); X = 0
while masih ada supply:
    L = garis pada dua tingkat rentang tertinggi, termasuk semua seri
    K_all = minimum-cost cells dari L, tanpa duplikasi
    urutkan K_all berdasarkan (CA, C, indeks_baris, indeks_kolom)
    K = dua sel pertama K_all
    for a in K:
        coba q_a = min(s_i,d_j)
        F[a] = q_a*C_ij + biaya completion THP baseline pada sisa
    komit hanya pengiriman a dengan F minimum; seri mengikuti K
    perbarui margin
return audit(X)
```

Ini evaluasi satu keputusan dengan completion penuh. Bukan rekursi ke THP modifikasi, bukan LP untuk menilai calon, dan bukan modifikasi yang hanya dilakukan pada keputusan pertama. Varian first-only dan completion LCM mempunyai ID eksperimen terpisah.

## 4. Contoh, hasil, dan keterbatasan

Input lengkap L05 Example 1:

```text
C = [[6,3,1,4], [7,6,2,1], [10,4,5,9], [7,7,7,3]]
s = [50,55,75,60]
d = [90,65,30,55]
```

THP asli dan modifikasi sama-sama memulai dengan `x13=30` (indeks penjelasan mulai 1). Pada keputusan kedua, CA memilih `x24=55` dengan biaya langsung 55 daripada `x32=65` dengan biaya langsung 260. Akan tetapi, total setelah completion, termasuk biaya pertama 30, adalah **1045 versus 985**. Modifikasi memilih x32. [Contoh manual lengkap](../report/manual_example.md) menunjukkan seluruh alokasi, degenerasi, dan sertifikat dual yang membuktikan optimum 985.

| Contoh asli L05 | THP asli | Varian ini | Optimum LP |
|---|---:|---:|---:|
| Example 1 | 1045 | 985 | 985 |
| Example 2 | 4525 | 4525 | 4525 |
| Example 3 | 2366 | 2366 | 2366 |

Hanya **satu dari tiga** contoh THP asli membaik; dua lainnya sudah optimal. Evaluasi hanya pada keputusan pertama masih menghasilkan 1045. Jadi keuntungan contoh pertama memerlukan pemeriksaan keputusan berikutnya, sesuai hasil ablasi.

| Dataset | Mean gap awal → baru | Membaik / sama / memburuk |
|---|---|---|
| 84 input kanonik paper/dataset penulis | 7,023% → 2,132% | 48 / 36 / 0 |
| 300 input acak | 13,647% → 6,264% | 182 / 118 / 0 |

Completion dengan kebijakan THP yang sama, calon asli tetap tersedia, dan aturan seri tetap memberi non-worsening relatif terhadap baseline tersebut. Ini bukan jaminan optimal dan bukan dominasi atas VAM atau metode lain. Mengganti completion dengan LCM atau lower bound mengubah sifat perbandingan; varian tersebut memang memiliki kasus memburuk.

Tambahan pekerjaan kira-kira `O(2*T*B)`, dengan T jumlah alokasi dan B biaya satu THP. Tidak ada bobot terlatih; k=2 tetap. Median rasio waktu pada sampel sebelumnya sekitar 6,6× THP. Gap acak terburuk masih 101,167%; hasil rata-rata tidak menyatakan selalu dekat optimum.

## 5. Kode dan cara menjalankan

[variants.py](variants.py) memuat `THP_top2_rollout` dan cabang `mode='rollout'`. [constructive.py](../methods/constructive.py) membentuk kandidat THP dan menjalankan baseline/completion. [common.py](../methods/common.py) melakukan balancing dan audit.

```powershell
python -m research.modifications.demo --method thp
python -m research.modifications.demo --method thp --problem L05_Example1 --trace --json
python -m research.modifications.demo --method thp --problem L05_Example3
```

Jalankan dari root `Risop`. Default menampilkan `baseline=1045, modified=985, optimal=985`. Pemanggilan data sendiri: `solve_variant(C,s,d,'THP_top2_rollout',trace=True)`. Jejak berisi kandidat, skor F dan keputusan; indeks mulai 0. LP di demo hanya pembanding yang dihitung setelah heuristik.

[README folder](README.md) menjelaskan dependensi dan format keluaran. [summary.csv](../results/summary.csv), [candidate_results.md](../report/candidate_results.md), serta [ablation_tables.md](../report/ablation_tables.md) memuat bukti seluruh kasus. Angka varian ini adalah hasil proyek, bukan klaim numerik paper THP asli.

<!-- BEGIN SHARED WORKED EXAMPLE -->
## 6. Contoh soal bersama: L05 Example 1, dihitung sampai selesai

Soal ini **sama persis** dengan contoh pada dua dokumen modifikasi lainnya dan [README](README.md#contoh-soal-bersama). Sumber matriks: paper lokal **L05**, Amaliah, Fatichah & Suryani (2021), Example 1, [DOI 10.1109/ICTS52701.2021.9608005](https://doi.org/10.1109/ICTS52701.2021.9608005). Hasil modifikasi di bawah adalah perhitungan proyek, bukan hasil varian yang diklaim paper tersebut.

**Soal:** empat sumber S1–S4 harus memenuhi permintaan empat tujuan D1–D4. Angka di dalam tabel adalah biaya per unit. Tentukan alokasi dengan biaya total rendah.

| Sumber | D1 | D2 | D3 | D4 | Supply |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 |
| S2 | 7 | 6 | 2 | 1 | 55 |
| S3 | 10 | 4 | 5 | 9 | 75 |
| S4 | 7 | 7 | 7 | 3 | 60 |
| Demand | 90 | 65 | 30 | 55 | 240 |

`Σ supply = 50+55+75+60 = 240 = 90+65+30+55 = Σ demand`; **tidak diperlukan dummy**. Pada tabel residu, biaya per unit tetap; hanya baris/kolom aktif serta sisa margin yang berubah.

Semua indeks penjelasan mulai dari **1**: `x13` berarti pengiriman S1 ke D3. JSON/kode menggunakan indeks mulai 0. Tanda `—` berarti tidak dihitung/tidak berlaku, bukan angka nol.

### Pembanding baseline dan arti skor

Baseline THP pada soal lengkap mengirim dalam urutan:

`x13=30 → x24=55 → x12=20 → x32=45 → x31=30 → x41=60`.

Biayanya `20×3 + 30×1 + 55×1 + 30×10 + 45×4 + 60×7 = 1045`; angka baseline ini cocok dengan paper L05.

Di setiap iterasi, `B` adalah biaya yang sudah benar-benar dikomit. Untuk calon a, `F(a)=biaya alokasi sementara+biaya completion baseline pada sisa`. Kolom `B+F` adalah estimasi biaya total dari awal. **Jangan menjumlahkan F dari berbagai iterasi**; F bukan biaya tambahan yang semuanya dikirim. Calon dicoba satu per satu pada salinan margin yang sama; completion hanya simulasi. Setelah memilih calon, komit satu alokasi saja.

Penalti THP = maksimum−minimum. Contoh awal: `P_D4=9−1=8`, `P_S2=7−1=6`. Pilih dua tingkat penalti berbeda tertinggi, kumpulkan minimum seluruh garis pada tingkat itu, deduplikasi, urutkan `(CA=C×min(s,d), C, i, j)`, lalu ambil dua sel pertama.

### Iterasi 1: B=0

| Sumber / tujuan | D1 | D2 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 | 5 |
| S2 | 7 | 6 | 2 | 1 | 55 | 6 |
| S3 | 10 | 4 | 5 | 9 | 75 | 6 |
| S4 | 7 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 30 | 55 | 240 | — |
| Penalti kolom | 4 | 4 | 6 | 8 | — | — |

Tingkat penalti terpilih: `[8, 6]`; garis: **S2, S3, D3, D4**. Urutan sel setelah CA: `x13 (CA=30), x24 (CA=55), x32 (CA=260)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x13 | 30 | 1 | 30 | 1015 | 1045 | 1045 |
| x24 | 55 | 1 | 55 | 990 | 1045 | 1045 |

- **Simulasi x13=30:** sementara `s=[20, 55, 75, 60]`, `d=[90, 65, 0, 55]`. Completion THP: `x24=55 → x12=20 → x32=45 → x31=30 → x41=60`. Biaya sisa = `20×3 + 55×1 + 30×10 + 45×4 + 60×7 = 1015`.
- **Simulasi x24=55:** sementara `s=[50, 0, 75, 60]`, `d=[90, 65, 30, 0]`. Completion THP: `x13=30 → x12=20 → x32=45 → x31=30 → x41=60`. Biaya sisa = `20×3 + 30×1 + 30×10 + 45×4 + 60×7 = 990`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x13=min(50,30)=30`. Garis yang selesai: **D3**. Sisa `s=[20, 55, 75, 60]`, `d=[90, 65, 0, 55]`; biaya terkomit menjadi **B=30**.

### Iterasi 2: B=30

| Sumber / tujuan | D1 | D2 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 4 | 20 | 3 |
| S2 | 7 | 6 | 1 | 55 | 6 |
| S3 | 10 | 4 | 9 | 75 | 6 |
| S4 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 55 | 210 | — |
| Penalti kolom | 4 | 4 | 8 | — | — |

Tingkat penalti terpilih: `[8, 6]`; garis: **S2, S3, D4**. Urutan sel setelah CA: `x24 (CA=55), x32 (CA=260)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x24 | 55 | 1 | 55 | 960 | 1015 | 1045 |
| x32 | 65 | 4 | 260 | 695 | 955 | 985 |

- **Simulasi x24=55:** sementara `s=[20, 0, 75, 60]`, `d=[90, 65, 0, 0]`. Completion THP: `x12=20 → x32=45 → x31=30 → x41=60`. Biaya sisa = `20×3 + 30×10 + 45×4 + 60×7 = 960`.
- **Simulasi x32=65:** sementara `s=[20, 55, 10, 60]`, `d=[90, 0, 0, 55]`. Completion THP: `x24=55 → x31=10 → x11=20 → x41=60`. Biaya sisa = `20×6 + 55×1 + 10×10 + 60×7 = 695`.

**Keputusan:** Pilih F terkecil. Komit `x32=min(75,65)=65`. Garis yang selesai: **D2**. Sisa `s=[20, 55, 10, 60]`, `d=[90, 0, 0, 55]`; biaya terkomit menjadi **B=290**.

### Iterasi 3: B=290

| Sumber / tujuan | D1 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- |
| S1 | 6 | 4 | 20 | 2 |
| S2 | 7 | 1 | 55 | 6 |
| S3 | 10 | 9 | 10 | 1 |
| S4 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 55 | 145 | — |
| Penalti kolom | 4 | 8 | — | — |

Tingkat penalti terpilih: `[8, 6]`; garis: **S2, D4**. Urutan sel setelah CA: `x24 (CA=55)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x24 | 55 | 1 | 55 | 640 | 695 | 985 |

- **Simulasi x24=55:** sementara `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`. Completion THP: `x31=10 → x11=20 → x41=60`. Biaya sisa = `20×6 + 10×10 + 60×7 = 640`.

**Keputusan:** Hanya satu calon tersedia. Komit `x24=min(55,55)=55`. Garis yang selesai: **S2, D4**. Sisa `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit menjadi **B=345**.

### Iterasi 4: B=345

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S1 | 6 | 20 | 0 |
| S3 | 10 | 10 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 90 | 90 | — |
| Penalti kolom | 4 | — | — |

Tingkat penalti terpilih: `[4, 0]`; garis: **S1, S3, S4, D1**. Urutan sel setelah CA: `x31 (CA=100), x11 (CA=120), x41 (CA=420)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x31 | 10 | 10 | 100 | 540 | 640 | 985 |
| x11 | 20 | 6 | 120 | 520 | 640 | 985 |

- **Simulasi x31=10:** sementara `s=[20, 0, 0, 60]`, `d=[80, 0, 0, 0]`. Completion THP: `x11=20 → x41=60`. Biaya sisa = `20×6 + 60×7 = 540`.
- **Simulasi x11=20:** sementara `s=[0, 0, 10, 60]`, `d=[70, 0, 0, 0]`. Completion THP: `x31=10 → x41=60`. Biaya sisa = `10×10 + 60×7 = 520`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x31=min(10,90)=10`. Garis yang selesai: **S3**. Sisa `s=[20, 0, 0, 60]`, `d=[80, 0, 0, 0]`; biaya terkomit menjadi **B=445**.

### Iterasi 5: B=445

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S1 | 6 | 20 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 80 | 80 | — |
| Penalti kolom | 1 | — | — |

Tingkat penalti terpilih: `[1, 0]`; garis: **S1, S4, D1**. Urutan sel setelah CA: `x11 (CA=120), x41 (CA=420)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x11 | 20 | 6 | 120 | 420 | 540 | 985 |
| x41 | 60 | 7 | 420 | 120 | 540 | 985 |

- **Simulasi x11=20:** sementara `s=[0, 0, 0, 60]`, `d=[60, 0, 0, 0]`. Completion THP: `x41=60`. Biaya sisa = `60×7 = 420`.
- **Simulasi x41=60:** sementara `s=[20, 0, 0, 0]`, `d=[20, 0, 0, 0]`. Completion THP: `x11=20`. Biaya sisa = `20×6 = 120`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x11=min(20,80)=20`. Garis yang selesai: **S1**. Sisa `s=[0, 0, 0, 60]`, `d=[60, 0, 0, 0]`; biaya terkomit menjadi **B=565**.

### Iterasi 6: B=565

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S4 | 7 | 60 | 0 |
| Sisa demand | 60 | 60 | — |
| Penalti kolom | 0 | — | — |

Tingkat penalti terpilih: `[0]`; garis: **S4, D1**. Urutan sel setelah CA: `x41 (CA=420)`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x41 | 60 | 7 | 420 | 0 | 420 | 985 |

- **Simulasi x41=60:** sementara `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`. Completion THP: `tidak ada pengiriman sisa`. Biaya sisa = `0 = 0`.

**Keputusan:** Hanya satu calon tersedia. Komit `x41=min(60,60)=60`. Garis yang selesai: **S4, D1**. Sisa `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`; biaya terkomit menjadi **B=985**.

### Hasil akhir, kelayakan, dan optimum

| Alokasi | D1 | D2 | D3 | D4 | Jumlah baris | Supply |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 20 | 0 | 30 | 0 | 50 | 50 |
| S2 | 0 | 0 | 0 | 55 | 55 | 55 |
| S3 | 10 | 65 | 0 | 0 | 75 | 75 |
| S4 | 60 | 0 | 0 | 0 | 60 | 60 |
| Jumlah kolom | 90 | 65 | 30 | 55 | 240 | — |
| Demand | 90 | 65 | 30 | 55 | 240 | — |

`Z_mod = 20×6 + 30×1 + 55×1 + 10×10 + 65×4 + 60×7 = 985.`

| Ukuran | Baseline THP | Modifikasi |
| --- | --- | --- |
| Biaya | 1045 | 985 |
| Optimum LP | 985 | 985 |
| Gap absolut | 60 | 0 |
| Gap % | 6.0914% | 0% |
| Accuracy = 100×Z_opt/Z | 94.2584% | 100% |

Penghematan = `1045−985 = 60`. Setiap jumlah baris sama dengan supply dan setiap jumlah kolom sama dengan demand. Ada enam sel positif, sedangkan `m+n−1=7`: ini **BFS degenerat**, bukan solusi tidak layak. Tambahkan `x14=0` sebagai sel basis yang tidak membentuk siklus; biaya tidak berubah.

Optimum juga dapat diperiksa secara manual: ambil `u=[1,0,5,2]` dan `v=[5,−1,0,1]`. Semua `u_i+v_j≤C_ij`, dan nilai dual `u·s+v·d=(50+375+120)+(450−65+55)=545+440=985`. Solusi feasible di atas mencapai batas bawah 985, sehingga optimal pada soal ini. Potensial/LP ini hanya **verifikasi setelah algoritma**, tidak dipakai untuk memilih kandidat.

Keberhasilan satu soal adalah ilustrasi mekanisme, bukan bukti keunggulan universal. Kesimpulan lintas-kasus tetap menggunakan seluruh suite yang dilaporkan.

### Jalankan soal yang sama

```powershell
python -m research.modifications.demo --method thp --problem L05_Example1 --trace --json
```

Angka tableau, setiap completion, dan hasil akhir dicocokkan dengan fungsi program. Bukti terstruktur: [worked_example_L05_Example1.json](../results/worked_example_L05_Example1.json). Untuk membangun ulang bagian contoh pada ketiga Markdown dan README:

```powershell
python -m research.modifications.worked_example
```

Perintah tersebut memperbarui bagian contoh yang diberi penanda dan JSON contoh saja; aturan algoritma serta CSV suite utama tetap sama.
<!-- END SHARED WORKED EXAMPLE -->
