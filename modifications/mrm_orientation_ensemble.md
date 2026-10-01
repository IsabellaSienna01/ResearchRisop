# MRM dengan pemilihan hasil terbaik dari beberapa orientasi

Dokumentasi implementasi per **2 Oktober 2026**. ID kode: **`MRM_orientation_ensemble`**. Istilah *ensemble* di sini berarti menghitung beberapa konstruksi deterministik lalu memilih biaya terendah; tidak ada machine learning.

Untuk belajar melalui angka, langsung ke [bagian 6: contoh soal bersama, kedua orientasi sampai selesai](#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai). Soalnya identik dengan contoh pada dokumen VAM dan THP. Contoh E01 yang disebut sebelumnya tetap menjadi benchmark tambahan, bukan soal bersama ini.

## 1. Asal metode dan status kebaruan

| Komponen | Referensi | Batas pemakaian |
|---|---|---|
| Baseline MRM biaya | Wireko et al. (2025), *The maximum range method for finding initial basic feasible solution for transportation problems*, Results in Control and Optimization 19, 100551, [DOI](https://doi.org/10.1016/j.rico.2025.100551) | Versi narasi dengan orientasi terkunci; bukan MRM minimisasi waktu |
| Rentang kolom | Kalhoro, Abdulrehman, Shaikh & Soomro (2021), *The Maximum Range Column Method—Going Beyond the Traditional Initial Basic Feasible Solution Methods for the Transportation Problems*, JMCMS 16(1), 74–86, [halaman penerbit](https://www.journalimcms.org/journal/the-maximum-range-column-method-going-beyond-the-traditional-initial-basic-feasible-solution-methods-for-the-transportation-problems/), [DOI 10.26782/jmcms.2021.01.00006](https://doi.org/10.26782/jmcms.2021.01.00006) | Bukti pendekatan orientasi kolom sudah ada; bukan klaim bahwa semua seri/eliminasi identik dengan versi proyek |
| Rentang baris/kolom dan kombinasi | Zainal Arifin (2021), *Solving Transportation Problem with Maximum Range Method*, skripsi UNDIP, [rekaman repositori](https://eprints.undip.ac.id/84177/) | Abstrak membahas MRCM/MRRM dan kombinasi; algoritma penuh belum diaudit. Tidak diasumsikan identik dengan ensemble ini |
| Rancangan yang diuji | Implementasi dan eksperimen proyek | Pertahankan baseline, hitung orientasi paksa baris dan kolom, lalu pilih yang paling murah |

**Klasifikasi: C, kombinasi/adaptasi ide yang sudah ada.** MRM baseline, rentang baris/kolom, dan prinsip memilih yang terbaik dari beberapa solusi bukan penemuan baru proyek. Tiga-run policy persis di sini tidak diklaim berasal utuh dari satu paper, dan tidak diklaim original. Belum ditemukan kecocokan persis dalam sumber yang diperiksa; full text sebagian sumber belum tersedia. Kode ditulis dalam proyek sebagai implementasi kebijakan yang dinyatakan, bukan kode resmi penulis.

DOI MRCM di atas diverifikasi dari halaman penerbit pada 2 Oktober 2026. PDF yang ditemukan mencetak string DOI placeholder; string itu tidak dipakai sebagai DOI yang sah.

## 2. MRM baseline yang menjadi acuan

1. Seimbangkan supply/demand dengan dummy biaya nol. Abaikan margin nol pada pembentukan awal daftar aktif.
2. Hitung rentang biaya `R_l=max(C pada garis l)−min(C pada garis l)`.
3. Tanpa dummy baru, pilihan pertama membandingkan garis baris dan kolom. Rentang terbesar menang; seri memilih minimum biaya garis lebih rendah, lalu baris sebelum kolom, kemudian indeks lebih kecil.
4. Dengan dummy source baru, versi narasi mengutamakan orientasi **baris**. Dengan dummy destination baru, orientasi **kolom**.
5. Setelah orientasi dipilih, **kunci orientasi tersebut**. Iterasi selanjutnya menghitung rentang hanya pada orientasi yang sama.
6. Di garis terpilih, pilih biaya minimum; seri memakai indeks paling barat laut. Alokasikan `q=min(s_i,d_j)`.
7. Jika hanya supply habis, hapus baris; jika hanya demand habis, hapus kolom. Jika keduanya habis bersamaan, hapus hanya garis sesuai orientasi terpilih. Garis bermargin nol lainnya masih ikut sampai pilihan berikutnya mengeluarkannya; langkah alokasi nol bisa tercatat.
8. Ulangi sampai supply habis, hitung biaya asli, dan audit basis/degenerasi.

Langkah eliminasi simultan ini **tidak boleh diganti diam-diam** dengan kontrak VAM/THP yang mengabaikan kedua garis habis. Versi narasi mereproduksi 13/13 biaya contoh kecil MRM, tetapi listing MATLAB dan satu narasi contoh sumber tidak sepenuhnya konsisten; lihat [kontrak algoritma](../report/terminology_and_algorithms.md#mrm-contract-e15-narrative-sections-31-32).

## 3. Kelemahan yang ditarget dan langkah modifikasi

Rentang pertama belum tentu memilih orientasi yang murah untuk semua keputusan selanjutnya. Modifikasi menguji **komitmen orientasi awal**; rumus rentang, minimum biaya, kuantitas, seri, dan eliminasi di masing-masing konstruksi tetap.

```text
X_default = MRM(C,s,d, orientation=None)  # aturan asli, termasuk dummy
X_rows    = MRM(C,s,d, orientation=0)    # paksa baris dari awal
X_columns = MRM(C,s,d, orientation=1)    # paksa kolom dari awal
pilih X dengan biaya asli terendah
jika seri: default dahulu, kemudian rows, kemudian columns
return X beserta hasil audit
```

Secara matematis:

`Z_mod = min(Z_default, Z_rows, Z_columns)`.

Tiga konstruksi dimulai dari **input yang sama dan lengkap**, bukan meneruskan konstruksi pertama atau berganti orientasi pada setiap iterasi. Pada konstruksi paksa, orientasi eksplisit mengesampingkan aturan default pemilihan orientasi dummy, tetapi dummy nol dan kelayakan tetap ditangani. Jika input sudah berisi dummy eksplisit, kode tidak menebak bahwa suatu baris nol pasti dummy; representasi input harus konsisten saat dibandingkan.

Untuk masalah seimbang, default biasanya sama dengan salah satu orientasi paksa. Implementasi tetap memanggil ketiganya agar baseline asli selalu tersedia. Karena baseline termasuk kandidat hasil, `Z_mod <= Z_default` langsung mengikuti operasi minimum. Tidak ada teorema optimalitas baru atau penggunaan LP untuk memilih hasil.

## 4. Hasil dan risiko penelitian

| Dataset | Mean gap awal → baru | Membaik / sama / memburuk |
|---|---|---|
| 84 input kanonik | 2,758% → 1,184% | 24 / 60 / 0 |
| 300 input acak | 10,904% → 6,159% | 111 / 189 / 0 |

**Tidak satu pun dari 13 contoh kecil paper MRM sendiri membaik.** Ketiga contoh asli yang tidak optimal tetap 248 vs optimum 240, 415 vs 410, dan 450 vs 430. Karena itu, ensemble ini tidak cocok untuk proyek yang hanya boleh menunjukkan perbaikan pada 13 contoh tersebut.

Contoh perbaikan pertama yang dipakai proyek adalah **E01_Example1**, matriks Hosseini (2017), [DOI 10.12988/ams.2017.75178](https://doi.org/10.12988/ams.2017.75178). Hasil MRM yang kita hitung **3710 → 3460**, optimum LP **3460**, gap **7,2254% → 0%**. Hosseini hanya menjadi sumber matriks; paper 2017 itu tidak melaporkan MRM 2025. Input lengkap dan margin tercatat di [benchmark_catalog.md](../report/benchmark_catalog.md).

Tambahan kerja paling banyak tiga konstruksi baseline, sekitar `3B`, tanpa bobot/parameter yang perlu dipilih. Median rasio waktu sampel terdahulu sekitar 2,9× MRM. Keuntungannya lebih ringan dibanding completion berulang, tetapi semua konstruksi bisa sama-sama membuat keputusan buruk; maksimum gap acak masih 67,857%.

## 5. Kode dan cara menjalankan

- [variants.py](variants.py), entri `MRM_orientation_ensemble` dan cabang `mode='orientation'`: menjalankan tiga konstruksi dan `min(..., key=cost)`.
- [mrm.py](../methods/mrm.py), `solve_mrm(..., orientation=None/0/1)`: baseline dan orientasi paksa.
- [common.py](../methods/common.py): keseimbangan dan audit kelayakan/basis.

```powershell
python -m research.modifications.demo --method mrm
python -m research.modifications.demo --method mrm --problem E01_Example1 --trace --json
```

Hasil default: `baseline=3710, modified=3460, optimal=3460`. Pemanggilan data sendiri: `solve_variant(C,s,d,'MRM_orientation_ensemble',trace=True)`.

`trace` yang dikembalikan fungsi modifikasi adalah jejak **konstruksi pemenang**, bukan tiga jejak sekaligus. Untuk melihat biaya semua konstruksi secara eksplisit, jalankan contoh Python ini pada C,s,d yang sama:

```python
from research.methods.mrm import solve_mrm

for nama, orientasi in [('default', None), ('rows', 0), ('columns', 1)]:
    hasil = solve_mrm(C, s, d, orientation=orientasi, trace=True)
    print(nama, hasil['cost'], hasil['orientation'])
```

LP dipakai hanya untuk optimum pembanding di demo; kode ensemble sendiri tidak memanggil solver. [README folder](README.md) memuat dependensi dan cara menjalankan keseluruhan suite. [candidate_results.md](../report/candidate_results.md) dan [summary.csv](../results/summary.csv) menyimpan hasil semua kasus; [source_inventory.md](../report/source_inventory.md) menjelaskan tingkat akses sumber.

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

### Rencana tiga konstruksi dari input yang sama

Hitung `default`, `rows`, dan `columns` **masing-masing dari margin awal**. Pada soal ini default memilih kolom pada langkah pertama, sehingga seluruh jejaknya sama dengan konstruksi columns. Keduanya dihitung terpisah oleh kode; tabel lengkap di bawah mewakili kedua konstruksi yang identik tersebut. Rows memiliki tabel lengkap tersendiri. Biaya MRM 1045 pada matriks L05 ini adalah hasil hitungan kita, bukan angka MRM dalam paper THP 2021.

Rentang = maksimum−minimum. Saat orientasi sudah terkunci, penalti orientasi lain diberi `—`. Baris/kolom bermargin nol yang belum dieliminasi tetap ikut rentang sesuai kode MRM.

### Konstruksi A: default; juga jejak konstruksi C: paksa kolom

Pada langkah pertama default mempertimbangkan baris dan kolom. Rentang tertinggi `D4=9−1=8` memilih kolom, minimum `C24=1`; orientasi berikutnya selalu kolom. Konstruksi columns langsung membatasi penilaian ke kolom dan memilih D4 yang sama.

#### Langkah 1

| Sumber / tujuan | D1 | D2 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 | 5 |
| S2 | 7 | 6 | 2 | 1 | 55 | 6 |
| S3 | 10 | 4 | 5 | 9 | 75 | 6 |
| S4 | 7 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 30 | 55 | 240 | — |
| Penalti kolom | 4 | 4 | 6 | 8 | — | — |

Pilih **kolom D4**, rentang `8`, minimum biaya `1`. Sel minimum dipilih menurut `(C,i,j)`: **x24**. Alokasi `min(55,55)=55`; biaya langkah `55×1=55`. Hapus **D4 saja; S2 bermargin nol masih dipertahankan**.

Sisa `s=[50, 0, 75, 60]`, `d=[90, 65, 30, 0]`; biaya terkomit **55**. Orientasi kolom tetap terkunci.

#### Langkah 2

| Sumber / tujuan | D1 | D2 | D3 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 50 | — |
| S2 | 7 | 6 | 2 | 0 | — |
| S3 | 10 | 4 | 5 | 75 | — |
| S4 | 7 | 7 | 7 | 60 | — |
| Sisa demand | 90 | 65 | 30 | 185 | — |
| Penalti kolom | 4 | 4 | 6 | — | — |

Pilih **kolom D3**, rentang `6`, minimum biaya `1`. Sel minimum dipilih menurut `(C,i,j)`: **x13**. Alokasi `min(50,30)=30`; biaya langkah `30×1=30`. Hapus **D3**.

Sisa `s=[20, 0, 75, 60]`, `d=[90, 65, 0, 0]`; biaya terkomit **85**. Orientasi kolom tetap terkunci.

#### Langkah 3

| Sumber / tujuan | D1 | D2 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 20 | — |
| S2 | 7 | 6 | 0 | — |
| S3 | 10 | 4 | 75 | — |
| S4 | 7 | 7 | 60 | — |
| Sisa demand | 90 | 65 | 155 | — |
| Penalti kolom | 4 | 4 | — | — |

Pilih **kolom D2**, rentang `4`, minimum biaya `3`. Ada seri rentang: `D1 (min=6), D2 (min=3)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x12**. Alokasi `min(20,65)=20`; biaya langkah `20×3=60`. Hapus **S1**.

Sisa `s=[0, 0, 75, 60]`, `d=[90, 45, 0, 0]`; biaya terkomit **145**. Orientasi kolom tetap terkunci.

#### Langkah 4

| Sumber / tujuan | D1 | D2 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- |
| S2 | 7 | 6 | 0 | — |
| S3 | 10 | 4 | 75 | — |
| S4 | 7 | 7 | 60 | — |
| Sisa demand | 90 | 45 | 135 | — |
| Penalti kolom | 3 | 3 | — | — |

Pilih **kolom D2**, rentang `3`, minimum biaya `4`. Ada seri rentang: `D1 (min=7), D2 (min=4)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x32**. Alokasi `min(75,45)=45`; biaya langkah `45×4=180`. Hapus **D2**.

Sisa `s=[0, 0, 30, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit **325**. Orientasi kolom tetap terkunci.

#### Langkah 5

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S2 | 7 | 0 | — |
| S3 | 10 | 30 | — |
| S4 | 7 | 60 | — |
| Sisa demand | 90 | 90 | — |
| Penalti kolom | 3 | — | — |

Pilih **kolom D1**, rentang `3`, minimum biaya `7`. Sel minimum dipilih menurut `(C,i,j)`: **x21**. Alokasi `min(0,90)=0`; biaya langkah `0×7=0`. Hapus **S2**.

Sisa `s=[0, 0, 30, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit **325**. Orientasi kolom tetap terkunci.

Langkah nol ini tidak mengirim barang dan tidak menambah biaya; ia mengeluarkan garis bermargin nol yang masih dipertahankan oleh aturan eliminasi MRM. Jangan menghapus langkah ini dari replay algoritma.

#### Langkah 6

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 30 | — |
| S4 | 7 | 60 | — |
| Sisa demand | 90 | 90 | — |
| Penalti kolom | 3 | — | — |

Pilih **kolom D1**, rentang `3`, minimum biaya `7`. Sel minimum dipilih menurut `(C,i,j)`: **x41**. Alokasi `min(60,90)=60`; biaya langkah `60×7=420`. Hapus **S4**.

Sisa `s=[0, 0, 30, 0]`, `d=[30, 0, 0, 0]`; biaya terkomit **745**. Orientasi kolom tetap terkunci.

#### Langkah 7

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 30 | — |
| Sisa demand | 30 | 30 | — |
| Penalti kolom | 0 | — | — |

Pilih **kolom D1**, rentang `0`, minimum biaya `10`. Sel minimum dipilih menurut `(C,i,j)`: **x31**. Alokasi `min(30,30)=30`; biaya langkah `30×10=300`. Hapus **D1 saja; S3 bermargin nol masih dipertahankan**.

Sisa `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`; biaya terkomit **1045**. Orientasi kolom tetap terkunci.

| Alokasi | D1 | D2 | D3 | D4 | Jumlah baris | Supply |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 0 | 20 | 30 | 0 | 50 | 50 |
| S2 | 0 | 0 | 0 | 55 | 55 | 55 |
| S3 | 30 | 45 | 0 | 0 | 75 | 75 |
| S4 | 60 | 0 | 0 | 0 | 60 | 60 |
| Jumlah kolom | 90 | 65 | 30 | 55 | 240 | — |
| Demand | 90 | 65 | 30 | 55 | 240 | — |

Biaya konstruksi = `20×3 + 30×1 + 55×1 + 30×10 + 45×4 + 60×7 = 1045`.

### Konstruksi B: paksa baris dari awal

Kembali ke supply `[50,55,75,60]` dan demand `[90,65,30,55]`. Rentang kolom tidak digunakan, sekalipun nilainya lebih besar. Penalti baris awal `[5,6,6,4]`; S2 dan S3 seri 6, tetapi minimum biaya S2=1 lebih rendah dari S3=4, sehingga pilih S2.

#### Langkah 1

| Sumber / tujuan | D1 | D2 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 | 5 |
| S2 | 7 | 6 | 2 | 1 | 55 | 6 |
| S3 | 10 | 4 | 5 | 9 | 75 | 6 |
| S4 | 7 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 30 | 55 | 240 | — |
| Penalti kolom | — | — | — | — | — | — |

Pilih **baris S2**, rentang `6`, minimum biaya `1`. Ada seri rentang: `S2 (min=1), S3 (min=4)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x24**. Alokasi `min(55,55)=55`; biaya langkah `55×1=55`. Hapus **S2 saja; D4 bermargin nol masih dipertahankan**.

Sisa `s=[50, 0, 75, 60]`, `d=[90, 65, 30, 0]`; biaya terkomit **55**. Orientasi baris tetap terkunci.

#### Langkah 2

| Sumber / tujuan | D1 | D2 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 | 5 |
| S3 | 10 | 4 | 5 | 9 | 75 | 6 |
| S4 | 7 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 30 | 0 | 185 | — |
| Penalti kolom | — | — | — | — | — | — |

Pilih **baris S3**, rentang `6`, minimum biaya `4`. Sel minimum dipilih menurut `(C,i,j)`: **x32**. Alokasi `min(75,65)=65`; biaya langkah `65×4=260`. Hapus **D2**.

Sisa `s=[50, 0, 10, 60]`, `d=[90, 0, 30, 0]`; biaya terkomit **315**. Orientasi baris tetap terkunci.

#### Langkah 3

| Sumber / tujuan | D1 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 1 | 4 | 50 | 5 |
| S3 | 10 | 5 | 9 | 10 | 5 |
| S4 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 30 | 0 | 120 | — |
| Penalti kolom | — | — | — | — | — |

Pilih **baris S1**, rentang `5`, minimum biaya `1`. Ada seri rentang: `S1 (min=1), S3 (min=5)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x13**. Alokasi `min(50,30)=30`; biaya langkah `30×1=30`. Hapus **D3**.

Sisa `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit **345**. Orientasi baris tetap terkunci.

#### Langkah 4

| Sumber / tujuan | D1 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- |
| S1 | 6 | 4 | 20 | 2 |
| S3 | 10 | 9 | 10 | 1 |
| S4 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 0 | 90 | — |
| Penalti kolom | — | — | — | — |

Pilih **baris S4**, rentang `4`, minimum biaya `3`. Sel minimum dipilih menurut `(C,i,j)`: **x44**. Alokasi `min(60,0)=0`; biaya langkah `0×3=0`. Hapus **D4**.

Sisa `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit **345**. Orientasi baris tetap terkunci.

Langkah nol ini tidak mengirim barang dan tidak menambah biaya; ia mengeluarkan garis bermargin nol yang masih dipertahankan oleh aturan eliminasi MRM. Jangan menghapus langkah ini dari replay algoritma.

#### Langkah 5

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S1 | 6 | 20 | 0 |
| S3 | 10 | 10 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 90 | 90 | — |
| Penalti kolom | — | — | — |

Pilih **baris S1**, rentang `0`, minimum biaya `6`. Ada seri rentang: `S1 (min=6), S3 (min=10), S4 (min=7)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x11**. Alokasi `min(20,90)=20`; biaya langkah `20×6=120`. Hapus **S1**.

Sisa `s=[0, 0, 10, 60]`, `d=[70, 0, 0, 0]`; biaya terkomit **465**. Orientasi baris tetap terkunci.

#### Langkah 6

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 10 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 70 | 70 | — |
| Penalti kolom | — | — | — |

Pilih **baris S4**, rentang `0`, minimum biaya `7`. Ada seri rentang: `S3 (min=10), S4 (min=7)`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. Sel minimum dipilih menurut `(C,i,j)`: **x41**. Alokasi `min(60,70)=60`; biaya langkah `60×7=420`. Hapus **S4**.

Sisa `s=[0, 0, 10, 0]`, `d=[10, 0, 0, 0]`; biaya terkomit **885**. Orientasi baris tetap terkunci.

#### Langkah 7

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 10 | 0 |
| Sisa demand | 10 | 10 | — |
| Penalti kolom | — | — | — |

Pilih **baris S3**, rentang `0`, minimum biaya `10`. Sel minimum dipilih menurut `(C,i,j)`: **x31**. Alokasi `min(10,10)=10`; biaya langkah `10×10=100`. Hapus **S3 saja; D1 bermargin nol masih dipertahankan**.

Sisa `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`; biaya terkomit **985**. Orientasi baris tetap terkunci.

| Alokasi | D1 | D2 | D3 | D4 | Jumlah baris | Supply |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 20 | 0 | 30 | 0 | 50 | 50 |
| S2 | 0 | 0 | 0 | 55 | 55 | 55 |
| S3 | 10 | 65 | 0 | 0 | 75 | 75 |
| S4 | 60 | 0 | 0 | 0 | 60 | 60 |
| Jumlah kolom | 90 | 65 | 30 | 55 | 240 | — |
| Demand | 90 | 65 | 30 | 55 | 240 | — |

Biaya konstruksi = `20×6 + 30×1 + 55×1 + 10×10 + 65×4 + 60×7 = 985`.

### Pilih konstruksi termurah

| Konstruksi | Orientasi | Urutan alokasi termasuk langkah nol | Biaya |
| --- | --- | --- | --- |
| default | kolom | x24=55 → x13=30 → x12=20 → x32=45 → x21=0 → x41=60 → x31=30 | 1045 |
| rows | baris | x24=55 → x32=65 → x13=30 → x44=0 → x11=20 → x41=60 → x31=10 | 985 |
| columns | kolom | x24=55 → x13=30 → x12=20 → x32=45 → x21=0 → x41=60 → x31=30 | 1045 |

`Z_ensemble = min(1045,985,1045) = 985`; ambil **seluruh matriks hasil rows**. Tidak ada alokasi dari konstruksi default yang dicampurkan ke hasil rows. Perbedaan penting muncul setelah pengiriman pertama: default bergerak ke x13, sedangkan rows bergerak ke x32, sehingga kapasitas untuk D2 dibagi berbeda.

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

| Ukuran | Baseline MRM | Modifikasi |
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
python -m research.modifications.demo --method mrm --problem L05_Example1 --trace --json
```

Argumen `--problem` penting: demo MRM tanpa argumen ini tetap memakai E01_Example1 sebagai contoh default historis. Perintah di atas memakai L05_Example1 yang sama dengan VAM dan THP. Demo menampilkan jejak konstruksi pemenang; JSON bukti berikut menyimpan ketiga konstruksi.

Angka tableau, setiap completion, dan hasil akhir dicocokkan dengan fungsi program. Bukti terstruktur: [worked_example_L05_Example1.json](../results/worked_example_L05_Example1.json). Untuk membangun ulang bagian contoh pada ketiga Markdown dan README:

```powershell
python -m research.modifications.worked_example
```

Perintah tersebut memperbarui bagian contoh yang diberi penanda dan JSON contoh saja; aturan algoritma serta CSV suite utama tetap sama.
<!-- END SHARED WORKED EXAMPLE -->
