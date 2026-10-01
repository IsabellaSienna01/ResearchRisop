# VAM dengan evaluasi dua kandidat melalui penyelesaian VAM

Dokumentasi implementasi per **2 Oktober 2026**. ID kode: **`VAM_top2_rollout`**. Ini nama kerja eksperimen, bukan nama metode yang diklaim telah diterbitkan.

Untuk belajar melalui angka, langsung ke [bagian 6: contoh soal bersama, semua iterasi](#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai). Soalnya identik dengan contoh pada dokumen THP dan MRM.

## 1. Asal metode dan status kebaruan

| Komponen | Asal / referensi | Yang dipakai dalam proyek |
|---|---|---|
| Baseline VAM | Atribusi historis Reinfeld & Vogel (1958), *Mathematical Programming*; buku asli tidak diakses. Aturan dan angka baseline dibaca dari paper THP lokal L05, [Amaliah, Fatichah & Suryani (2021)](https://doi.org/10.1109/ICTS52701.2021.9608005) | Penalti selisih dua minimum dan alokasi maksimum feasible; seri dinyatakan secara deterministik |
| Pembatasan kandidat | [Korukoglu & Balli (2011), IVAM](https://doi.org/10.3390/mca16020370), serta THP L05 | Bukti bahwa top-k/seleksi beberapa calon sudah ada; kode ini tidak mereproduksi IVAM lengkap |
| Penyelesaian heuristik kandidat | [Bertsekas, Tsitsiklis & Wu (1997), Rollout Algorithms for Combinatorial Optimization](https://www.mit.edu/~jnt/Papers/J066-97-rollout.pdf), [DOI](https://doi.org/10.1023/A:1009635226865) | Dasar konsep evaluasi keadaan lanjutan dengan heuristik; diterapkan pada alokasi transportasi |
| Rancangan persis di sini | Implementasi dan eksperimen proyek | Dua sel berbeda pertama dalam urutan kandidat VAM, termasuk pilihan baseline; completion VAM; komit satu alokasi; ulangi |

**Klasifikasi kebaruan: C, kombinasi/adaptasi ide yang sudah ada.** Tidak ada satu paper di atas yang kami klaim mendefinisikan persis nama `VAM_top2_rollout`. Kode ditulis dalam proyek ini; konsep VAM, top-k, dan rollout bukan penemuan proyek. Belum ditemukan kecocokan persis dalam sumber yang ditelaah, tetapi pencarian tidak membuktikan originalitas. Gunakan frasa *adaptasi evaluasi dua kandidat berbasis penyelesaian VAM*, bukan klaim “metode baru pertama”.

## 2. Langkah baseline yang dipertahankan

1. Seimbangkan total supply/demand dengan dummy nol bila perlu; abaikan margin nol saat menentukan garis aktif.
2. Pada setiap baris dan kolom aktif, urutkan biaya dengan pengulangan nilai tetap dihitung. Penalti `P = minimum_kedua − minimum_pertama`; satu sel tersisa memberi penalti 0.
3. Urutkan garis menurut P menurun. Seri penalti: baris sebelum kolom, lalu indeks meningkat. Pilih minimum biaya pada garis pertama; seri sel memakai indeks meningkat.
4. Alokasikan `q=min(s_i,d_j)`, kurangi margin, hilangkan garis habis; jika keduanya habis, keduanya tidak aktif untuk scoring berikutnya.
5. Ulangi sampai sisa supply nol. Audit alokasi dan lengkapi basis degenerat dengan sel nol tanpa mengubah biaya.

VAM memiliki beberapa aturan seri dalam literatur. Hasil di sini berlaku untuk versi deterministik ini; varian seri biaya/alokasi lain disimpan dengan nama berbeda.

## 3. Kelemahan dan langkah yang berubah

VAM mengukur regret lokal dari dua biaya, tetapi keputusan satu sel dapat menghabiskan kapasitas untuk tujuan lain. **Langkah yang diubah adalah komit sel setelah urutan penalti dibuat**, bukan rumus penalti atau besarnya pengiriman.

Pembentukan kandidat harus mengikuti kode secara tepat:

1. Bentuk urutan garis dari langkah baseline.
2. Untuk tiap garis, masukkan **semua sel yang seri pada biaya minimum**, dalam urutan indeks.
3. Gabungkan daftar itu mengikuti urutan garis dan hapus sel duplikat sambil mempertahankan kemunculan pertama.
4. Ambil dua sel pertama; bila hanya satu, pakai satu. Pilihan baseline selalu berada di urutan pertama.

Artinya, kedua calon **bisa berasal dari garis yang sama** jika ada seri minimum. Istilah “dua kandidat” tidak berarti selalu dua penalti berbeda atau dua garis berbeda. Ini rincian implementasi proyek dalam `ranked_cells()`.

Untuk setiap kandidat `a=(i,j)`, buat margin sementara setelah pengiriman `q_a=min(s_i,d_j)` dan hitung:

`F(a) = C_ij*q_a + Z_VAM(masalah sisa setelah a)`.

`Z_VAM` adalah penyelesaian penuh memakai **baseline VAM yang sama**, tanpa memanggil lagi modifikasi secara rekursif. Biaya yang sudah dikomit sebelumnya sama untuk semua calon, sehingga boleh tidak dimasukkan dalam pembandingan. Pilih F terkecil; saat F seri pertahankan urutan calon asli. Komit **hanya pengiriman pertama** calon terpilih, lalu hitung ulang kandidat.

```text
Balance(C,s,d); X = 0
while masih ada supply:
    K = dua sel berbeda pertama dari ordered_VAM_candidates(C,s,d)
    for a=(i,j) in K:
        q = min(s[i],d[j])
        (s2,d2) = margin setelah sementara mengirim q di a
        Y = baseline_VAM_completion(C,s2,d2)
        F[a] = q*C[i,j] + sum(C*Y)
    a_best = argmin F, pertahankan urutan K pada seri
    komit q di a_best ke X dan perbarui (s,d)
return audit(X)
```

LP tidak digunakan dalam F. Pemanggilan LP pada demo hanya untuk menghitung optimum pembanding setelah kedua heuristik selesai.

## 4. Bukti eksperimen dan batas jaminan

| Dataset | Mean gap baseline → modifikasi | Membaik / sama / memburuk |
|---|---|---|
| 84 input kanonik paper/dataset penulis | 3,718% → 0,876% | 29 / 55 / 0 |
| 300 input acak tetap | 12,968% → 5,032% | 117 / 183 / 0 |

L05 Example 1: **1095 → 985**, optimum **985**. Calon pertama baseline adalah sel (4,4), alternatif berikutnya (1,3), menggunakan indeks penjelasan mulai 1. Completion masing-masing memberi total 1095 dan 985. L05 Example 2: **5125 → 4525**, optimum 4525; Example 3 tetap 2388, optimum 2366. Perbaikan tidak selalu mencapai optimum.

Karena pilihan baseline tersedia dan completion memakai kebijakan yang sama, pada setiap keadaan estimasi terbaik tidak lebih mahal dari biaya baseline. Dengan pengurangan garis aktif dan pengulangan argumen pada masalah sisa, biaya akhir tidak lebih mahal dari **baseline yang sama**. Ini penerapan prinsip rollout, bukan teorema baru. Jaminan tersebut tidak otomatis berlaku untuk completion LCM, estimasi lower bound, baseline dengan seri lain, atau modifikasi yang membuang calon asli.

Dengan T jumlah alokasi dan B biaya satu konstruksi, implementasi sederhana memerlukan sekitar `O(2*T*B)`; parameter kontinu tidak ada, k=2 tetap. Pengukuran terdahulu memberi median rasio waktu sekitar 7,3× baseline pada sampel 30 kasus. Mean gap lebih baik tidak menjamin gap kecil di setiap kasus; maksimum gap acak varian ini mencapai 152,063%.

## 5. Kode dan cara menjalankan

- [variants.py](variants.py): entri `VAM_top2_rollout`, `solve_variant()`, cabang `mode='rollout'`.
- [constructive.py](../methods/constructive.py): `ranked_cells()` dan `construct()` sebagai baseline/completion.
- [common.py](../methods/common.py): balancing serta audit.

```powershell
python -m research.modifications.demo --method vam
python -m research.modifications.demo --method vam --problem L05_Example1 --trace --json
```

Jalankan dari root `Risop`; hasil pertama harus `baseline=1095, modified=985, optimal=985`. Untuk data sendiri: `solve_variant(C,s,d,'VAM_top2_rollout',trace=True)`. Jejak menyimpan calon, F, indeks calon terpilih, dan kuantitas; indeks mulai 0. Instruksi dependensi ada di [README folder](README.md).

Rujukan hasil: [summary.csv](../results/summary.csv), [semua kasus shortlist](../report/candidate_results.md), [ablasi](../report/ablation_tables.md), [batas kebaruan](../report/modification_catalog.md). Semua angka tabel ini adalah hasil komputasi proyek pada data yang disimpan, bukan angka hasil VAM-rollout yang dikutip dari paper referensi.

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

Baseline VAM pada soal lengkap mengirim dalam urutan:

`x44=55 → x23=30 → x32=65 → x11=50 → x21=25 → x41=5 → x31=10`.

Biayanya `50×6 + 25×7 + 30×2 + 10×10 + 65×4 + 5×7 + 55×3 = 1095`; angka baseline ini cocok dengan paper L05.

Di setiap iterasi, `B` adalah biaya yang sudah benar-benar dikomit. Untuk calon a, `F(a)=biaya alokasi sementara+biaya completion baseline pada sisa`. Kolom `B+F` adalah estimasi biaya total dari awal. **Jangan menjumlahkan F dari berbagai iterasi**; F bukan biaya tambahan yang semuanya dikirim. Calon dicoba satu per satu pada salinan margin yang sama; completion hanya simulasi. Setelah memilih calon, komit satu alokasi saja.

Penalti = biaya terkecil kedua dikurangi biaya terkecil (nilai seri tetap dihitung). Contoh awal: `P_S4=7−3=4`, `P_D4=3−1=2`. Urutkan garis berdasarkan penalti menurun, lalu baris sebelum kolom dan indeks meningkat; ambil minimum setiap garis termasuk seri, deduplikasi sel, lalu ambil dua calon pertama.

### Iterasi 1: B=0

| Sumber / tujuan | D1 | D2 | D3 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 1 | 4 | 50 | 2 |
| S2 | 7 | 6 | 2 | 1 | 55 | 1 |
| S3 | 10 | 4 | 5 | 9 | 75 | 1 |
| S4 | 7 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 30 | 55 | 240 | — |
| Penalti kolom | 1 | 1 | 1 | 2 | — | — |

Urutan garis: `S4(4), S1(2), D4(2), S2(1), S3(1), D1(1), D2(1), D3(1)`. Urutan sel setelah deduplikasi: `x44, x13, x24, x32, x11, x12`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x44 | 55 | 3 | 165 | 930 | 1095 | 1095 |
| x13 | 30 | 1 | 30 | 955 | 985 | 985 |

- **Simulasi x44=55:** sementara `s=[50, 55, 75, 5]`, `d=[90, 65, 30, 0]`. Completion VAM: `x23=30 → x32=65 → x11=50 → x21=25 → x41=5 → x31=10`. Biaya sisa = `50×6 + 25×7 + 30×2 + 10×10 + 65×4 + 5×7 = 930`.
- **Simulasi x13=30:** sementara `s=[20, 55, 75, 60]`, `d=[90, 65, 0, 55]`. Completion VAM: `x24=55 → x32=65 → x11=20 → x41=60 → x31=10`. Biaya sisa = `20×6 + 55×1 + 10×10 + 65×4 + 60×7 = 955`.

**Keputusan:** Pilih F terkecil. Komit `x13=min(50,30)=30`. Garis yang selesai: **D3**. Sisa `s=[20, 55, 75, 60]`, `d=[90, 65, 0, 55]`; biaya terkomit menjadi **B=30**.

### Iterasi 2: B=30

| Sumber / tujuan | D1 | D2 | D4 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 4 | 20 | 1 |
| S2 | 7 | 6 | 1 | 55 | 5 |
| S3 | 10 | 4 | 9 | 75 | 5 |
| S4 | 7 | 7 | 3 | 60 | 4 |
| Sisa demand | 90 | 65 | 55 | 210 | — |
| Penalti kolom | 1 | 1 | 2 | — | — |

Urutan garis: `S2(5), S3(5), S4(4), D4(2), S1(1), D1(1), D2(1)`. Urutan sel setelah deduplikasi: `x24, x32, x44, x12, x11`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x24 | 55 | 1 | 55 | 900 | 955 | 985 |
| x32 | 65 | 4 | 260 | 695 | 955 | 985 |

- **Simulasi x24=55:** sementara `s=[20, 0, 75, 60]`, `d=[90, 65, 0, 0]`. Completion VAM: `x32=65 → x11=20 → x41=60 → x31=10`. Biaya sisa = `20×6 + 10×10 + 65×4 + 60×7 = 900`.
- **Simulasi x32=65:** sementara `s=[20, 55, 10, 60]`, `d=[90, 0, 0, 55]`. Completion VAM: `x24=55 → x11=20 → x41=60 → x31=10`. Biaya sisa = `20×6 + 55×1 + 10×10 + 60×7 = 695`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x24=min(55,55)=55`. Garis yang selesai: **S2, D4**. Sisa `s=[20, 0, 75, 60]`, `d=[90, 65, 0, 0]`; biaya terkomit menjadi **B=85**.

### Iterasi 3: B=85

| Sumber / tujuan | D1 | D2 | Sisa supply | Penalti baris |
| --- | --- | --- | --- | --- |
| S1 | 6 | 3 | 20 | 3 |
| S3 | 10 | 4 | 75 | 6 |
| S4 | 7 | 7 | 60 | 0 |
| Sisa demand | 90 | 65 | 155 | — |
| Penalti kolom | 1 | 1 | — | — |

Urutan garis: `S3(6), S1(3), D1(1), D2(1), S4(0)`. Urutan sel setelah deduplikasi: `x32, x12, x11, x41, x42`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x32 | 65 | 4 | 260 | 640 | 900 | 985 |
| x12 | 20 | 3 | 60 | 900 | 960 | 1045 |

- **Simulasi x32=65:** sementara `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`. Completion VAM: `x11=20 → x41=60 → x31=10`. Biaya sisa = `20×6 + 10×10 + 60×7 = 640`.
- **Simulasi x12=20:** sementara `s=[0, 0, 75, 60]`, `d=[90, 45, 0, 0]`. Completion VAM: `x32=45 → x41=60 → x31=30`. Biaya sisa = `30×10 + 45×4 + 60×7 = 900`.

**Keputusan:** Pilih F terkecil. Komit `x32=min(75,65)=65`. Garis yang selesai: **D2**. Sisa `s=[20, 0, 10, 60]`, `d=[90, 0, 0, 0]`; biaya terkomit menjadi **B=345**.

### Iterasi 4: B=345

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S1 | 6 | 20 | 0 |
| S3 | 10 | 10 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 90 | 90 | — |
| Penalti kolom | 1 | — | — |

Urutan garis: `D1(1), S1(0), S3(0), S4(0)`. Urutan sel setelah deduplikasi: `x11, x31, x41`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x11 | 20 | 6 | 120 | 520 | 640 | 985 |
| x31 | 10 | 10 | 100 | 540 | 640 | 985 |

- **Simulasi x11=20:** sementara `s=[0, 0, 10, 60]`, `d=[70, 0, 0, 0]`. Completion VAM: `x41=60 → x31=10`. Biaya sisa = `10×10 + 60×7 = 520`.
- **Simulasi x31=10:** sementara `s=[20, 0, 0, 60]`, `d=[80, 0, 0, 0]`. Completion VAM: `x11=20 → x41=60`. Biaya sisa = `20×6 + 60×7 = 540`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x11=min(20,90)=20`. Garis yang selesai: **S1**. Sisa `s=[0, 0, 10, 60]`, `d=[70, 0, 0, 0]`; biaya terkomit menjadi **B=465**.

### Iterasi 5: B=465

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 10 | 0 |
| S4 | 7 | 60 | 0 |
| Sisa demand | 70 | 70 | — |
| Penalti kolom | 3 | — | — |

Urutan garis: `D1(3), S3(0), S4(0)`. Urutan sel setelah deduplikasi: `x41, x31`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x41 | 60 | 7 | 420 | 100 | 520 | 985 |
| x31 | 10 | 10 | 100 | 420 | 520 | 985 |

- **Simulasi x41=60:** sementara `s=[0, 0, 10, 0]`, `d=[10, 0, 0, 0]`. Completion VAM: `x31=10`. Biaya sisa = `10×10 = 100`.
- **Simulasi x31=10:** sementara `s=[0, 0, 0, 60]`, `d=[60, 0, 0, 0]`. Completion VAM: `x41=60`. Biaya sisa = `60×7 = 420`.

**Keputusan:** F seri; pilih calon pertama menurut urutan baseline. Komit `x41=min(60,70)=60`. Garis yang selesai: **S4**. Sisa `s=[0, 0, 10, 0]`, `d=[10, 0, 0, 0]`; biaya terkomit menjadi **B=885**.

### Iterasi 6: B=885

| Sumber / tujuan | D1 | Sisa supply | Penalti baris |
| --- | --- | --- | --- |
| S3 | 10 | 10 | 0 |
| Sisa demand | 10 | 10 | — |
| Penalti kolom | 0 | — | — |

Urutan garis: `S3(0), D1(0)`. Urutan sel setelah deduplikasi: `x31`.

| Calon | q=min(s,d) | C | q×C | Z sisa | F | B+F |
| --- | --- | --- | --- | --- | --- | --- |
| x31 | 10 | 10 | 100 | 0 | 100 | 985 |

- **Simulasi x31=10:** sementara `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`. Completion VAM: `tidak ada pengiriman sisa`. Biaya sisa = `0 = 0`.

**Keputusan:** Hanya satu calon tersedia. Komit `x31=min(10,10)=10`. Garis yang selesai: **S3, D1**. Sisa `s=[0, 0, 0, 0]`, `d=[0, 0, 0, 0]`; biaya terkomit menjadi **B=985**.

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

| Ukuran | Baseline VAM | Modifikasi |
| --- | --- | --- |
| Biaya | 1095 | 985 |
| Optimum LP | 985 | 985 |
| Gap absolut | 110 | 0 |
| Gap % | 11.1675% | 0% |
| Accuracy = 100×Z_opt/Z | 89.9543% | 100% |

Penghematan = `1095−985 = 110`. Setiap jumlah baris sama dengan supply dan setiap jumlah kolom sama dengan demand. Ada enam sel positif, sedangkan `m+n−1=7`: ini **BFS degenerat**, bukan solusi tidak layak. Tambahkan `x14=0` sebagai sel basis yang tidak membentuk siklus; biaya tidak berubah.

Optimum juga dapat diperiksa secara manual: ambil `u=[1,0,5,2]` dan `v=[5,−1,0,1]`. Semua `u_i+v_j≤C_ij`, dan nilai dual `u·s+v·d=(50+375+120)+(450−65+55)=545+440=985`. Solusi feasible di atas mencapai batas bawah 985, sehingga optimal pada soal ini. Potensial/LP ini hanya **verifikasi setelah algoritma**, tidak dipakai untuk memilih kandidat.

Keberhasilan satu soal adalah ilustrasi mekanisme, bukan bukti keunggulan universal. Kesimpulan lintas-kasus tetap menggunakan seluruh suite yang dilaporkan.

### Jalankan soal yang sama

```powershell
python -m research.modifications.demo --method vam --problem L05_Example1 --trace --json
```

Angka tableau, setiap completion, dan hasil akhir dicocokkan dengan fungsi program. Bukti terstruktur: [worked_example_L05_Example1.json](../results/worked_example_L05_Example1.json). Untuk membangun ulang bagian contoh pada ketiga Markdown dan README:

```powershell
python -m research.modifications.worked_example
```

Perintah tersebut memperbarui bagian contoh yang diberi penanda dan JSON contoh saja; aturan algoritma serta CSV suite utama tetap sama.
<!-- END SHARED WORKED EXAMPLE -->
