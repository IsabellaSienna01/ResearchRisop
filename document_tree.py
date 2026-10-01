"""Generate an exact file-by-file research index; no experiment/data changes."""
from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / 'FILE_INDEX.md'

# Paths are relative to research/. Descriptions explain purpose, not scientific claims.
DESCRIPTIONS = dict(line.split('|', 1) for line in '''README.md|Pintu masuk, tautan laporan dan perintah reproduksi.
STRUKTUR_FOLDER.md|Panduan hubungan folder, data, kode, eksperimen dan laporan.
FILE_INDEX.md|Indeks otomatis setiap berkas beserta kegunaannya.
progress.md|Status tahap penelitian, pengecualian dan keterbatasan yang masih terbuka.
paper_inventory.md|Inventaris lima PDF pengguna, contoh, klaim, DOI dan koreksi penemuan input 2x94.
requirements.txt|Daftar paket Python; versi eksperimen tercatat dalam results/environment.json.
document_tree.py|Generator indeks berkas ini; hanya menulis FILE_INDEX.md.
extract_local.py|Pemindaian/ekstraksi PDF lokal dan pembentukan manifest sumber.
read_text.py|Pembaca rentang baris teks dengan nomor baris.
render_pages.py|Merender halaman PDF terpilih untuk audit visual transkripsi.
fetch_source.py|Unduhan satu sumber terpilih dan catatan provenance; bukan solver.
prepare_downloads.py|Pembentukan antrean URL unduhan dari halaman sumber yang disimpan.
fetch_batch.py|Pengunduh antrean sumber dan pencatat hasil; tidak mengeksekusi kode unduhan.
build_datasets.py|Transkripsi/parsing input, deduplikasi dan pencatatan pengecualian.
extract_claims.py|Ekstraksi klaim angka paper tanpa menganggap matriksnya sudah diketahui.
papers/local_manifest.json|Lokasi, metadata, halaman, ukuran dan SHA-256 PDF lokal; pemetaan L01-L05.
datasets/published/occurrences.json|140 kemunculan input di sumber dengan locator dan klaim; duplikasi dipertahankan.
datasets/published/benchmarks.json|86 input mentah unik untuk eksperimen inti.
datasets/published/canonical_ids.json|84 ID inti untuk ringkasan setelah deduplikasi setara balancing.
datasets/published/exclusions.json|Data yang dikeluarkan dan alasan; tidak diisi dengan dugaan.
datasets/published/reported_claims.csv|819 klaim sumber terpisah yang belum otomatis dicocokkan ke matriks.
datasets/published/csm_matrix_extraction.txt|Ekstraksi antara tabel CSM untuk audit transkripsi.
datasets/published/jhm_supplement.json|Sepuluh kemunculan sumber tambahan, termasuk pemetaan enam duplikat inti.
datasets/generated/seed20261001.json|300 matriks acak tetap untuk input bersama seluruh metode.
methods/common.py|Validasi, balancing, biaya, kelayakan, basis bebas siklus dan degenerasi.
methods/constructive.py|Seleksi kandidat dan konstruksi NWCM/LCM/VAM/LDVAM/RAM/TDM1/TDM2/TDSM/THP.
methods/repair.py|Interpretasi algoritma perbaikan SSM/CSM/RBSM/BCE, termasuk pencatatan kegagalan.
methods/mrm.py|MRM narasi, orientasi default atau paksa baris/kolom.
methods/jhm.py|JHM terbatas dan empat variasi; cabang belum diketahui tidak diganti aturan lain.
methods/__init__.py|Registry 14 baseline dan fungsi solve untuk memilih implementasi.
modifications/README.md|Indeks tiga dokumen modifikasi, status kebaruan, API dan cara menjalankan.
modifications/vam_top2_rollout.md|Langkah VAM dua kandidat, asal ide, rumus, pseudocode, hasil dan batas kebaruan.
modifications/thp_top2_rollout.md|Langkah THP dua kandidat, beda dari dua tingkat penalti asli, sumber dan hasil.
modifications/mrm_orientation_ensemble.md|Algoritma pilihan orientasi MRM, prior art, dummy/seri dan batas benchmark.
modifications/variants.py|Registry dan implementasi 24 modifikasi kecil, termasuk tiga shortlist.
modifications/demo.py|CLI demo baseline-modifikasi-optimum, jejak dan JSON; tidak menimpa CSV penelitian.
modifications/worked_example.py|Membangun dan memeriksa contoh L05 yang sama pada empat Markdown, dengan seluruh simulasi kandidat/orientasi.
modifications/__init__.py|Ekspor VARIANTS dan solve_variant untuk impor Python.
solver/optimal_lp.py|LP SciPy/HiGHS untuk optimum pembanding dan sertifikat primal-dual.
experiments/protocol.md|Protokol utama: varian, data bersama, seed, metrik dan batas klaim.
experiments/jhm_protocol.md|Protokol JHM terbatas, seri, varian dan penanganan cabang unverified.
experiments/run_baselines.py|Eksekusi baseline, LP, reproduksi klaim dan penyimpanan alokasi.
experiments/run_modifications.py|Eksekusi 24 varian; --random membentuk dan menguji 300 input seed tetap.
experiments/run_jhm.py|Percobaan JHM terbatas, empat varian, reproduksi dan sensitivitas seri.
experiments/jhm_supplement.py|Ekstraksi/audit input tambahan E19 dan L01 2x94; eksperimen terpisah.
experiments/verify.py|Pemeriksaan algoritma, anchor, enumerasi optimum kecil dan sifat rollout.
experiments/diagnostics.py|Audit sensitivitas skala biaya dan konvensi seri.
experiments/enumerate_ties.py|Enumerasi pilihan seri pada ketidakcocokan contoh kecil.
experiments/timing.py|Pengukuran waktu terkontrol pada sampel kasus.
experiments/summarize.py|Pembentuk statistik, tabel Markdown otomatis, grafik dan environment dari CSV tersimpan.
experiments/audit_artifacts.py|Audit data, agregat, alokasi/dual, tabel dan tautan dokumen tanpa menala eksperimen.
results/baseline.csv|1.204 percobaan baseline pada 86 input mentah.
results/modifications.csv|2.064 percobaan 24 modifikasi pada 86 input mentah.
results/random_benchmark.csv|11.400 percobaan 14 baseline dan 24 varian pada 300 input bersama.
results/reproduction.csv|207 perbandingan historis inti: klaim sumber versus reproduksi/LP.
results/summary.csv|Statistik semua konfigurasi: gap, hits, perbaikan, ties, memburuk, kegagalan dan waktu.
results/random_by_size_distribution.csv|Statistik dipisah menurut ukuran dan keluarga biaya acak.
results/source_sensitivity.csv|Ringkasan sensitivitas setelah mengecualikan matriks sumber berkonflik.
results/baseline_allocations.json|Matriks alokasi baseline dan jejak yang disimpan.
results/modification_allocations.json|Matriks alokasi modifikasi dan skor/jejak yang disimpan.
results/worked_example_L05_Example1.json|Bukti soal bersama: baseline, tiap kandidat/completion, margin, ketiga konstruksi MRM, alokasi dan sertifikat LP.
results/optimal_certificates.json|86 optimum inti dengan alokasi, dual dan residual.
results/random_optimal_certificates.json|300 optimum acak dengan sertifikat numerik.
results/currency_sensitivity.csv|Pengaruh penskalaan biaya terhadap keputusan dan biaya dalam satuan asli.
results/tie_diagnostics.csv|Hasil beberapa konvensi seri pada contoh yang diaudit.
results/tie_enumeration.csv|Biaya yang dapat dicapai lewat seluruh seri yang diizinkan pada contoh kecil.
results/controlled_timing.csv|Sampel pengukuran waktu setelah warmup dan pengulangan.
results/environment.json|Versi Python, NumPy, SciPy, pandas dan platform saat ringkasan dibuat.
results/verification.txt|Ringkasan pemeriksaan algoritma dan enumerasi optimum kecil.
results/artifact_audit.txt|Hasil pemeriksaan terakhir terhadap artefak tersimpan dan dokumen.
results/gap_comparison.png|Grafik raster mean gap tiga arah penelitian.
results/gap_comparison.svg|Grafik vektor mean gap, dapat diperbesar tanpa pecah.
results/jhm_restricted.csv|1.930 percobaan JHM parsial dan varian, termasuk unverified.
results/jhm_summary.csv|Statistik JHM dengan cakupan berhasil dan pasangan yang sebanding.
results/jhm_allocations.json|Alokasi dan jejak JHM parsial yang berhasil.
results/jhm_reproduction.csv|Perbandingan klaim JHM lokal dengan interpretasi terbatas.
results/jhm_tie_sensitivity.csv|Biaya/alokasi JHM dengan dua konvensi seri, disimpan terpisah.
results/jhm_verification.txt|Ringkasan pemeriksaan kelayakan, basis dan anchor JHM.
results/jhm_supplement.csv|430 percobaan pada sepuluh kemunculan sumber tambahan.
results/jhm_supplement_reproduction.csv|33 perbandingan klaim tambahan; duplikat sumber tidak dihitung sebagai kasus independen.
results/jhm_supplement_allocations.json|Alokasi dan jejak yang berhasil pada audit tambahan.
results/jhm_supplement_optimal.json|Sepuluh sertifikat optimum tambahan, termasuk sumber yang duplikat inti.
report/hasil_riset_dan_kesimpulan.md|Sintesis Indonesia: semua metode, hasil, pilihan proyek dan roadmap.
report/research_report.md|Laporan utama rinci 35 bagian.
report/terminology_and_algorithms.md|Validasi akronim, algoritma dan konvensi implementasi.
report/source_inventory.md|Referensi, DOI, klasifikasi, tingkat akses dan kegunaan benchmark.
report/search_log.md|Log pencarian dan batas akses; bukan bukti penelusuran seluruh literatur.
report/modification_catalog.md|Ide tiap metode, langkah yang berubah, prior art, risiko dan status eksperimen.
report/benchmark_catalog.md|Katalog otomatis semua matriks inti, sumber, klaim dan optimum.
report/reproduction_tables.md|Tabel otomatis reproduksi klaim historis inti.
report/performance_tables.md|Tabel otomatis statistik lengkap seluruh konfigurasi.
report/candidate_results.md|Tabel otomatis biaya tiap kasus untuk tiga shortlist.
report/ablation_tables.md|Tabel otomatis pemisahan efek komponen perubahan.
report/manual_example.md|Demonstrasi THP 4x4 dan sertifikat dual optimum 985.
report/jhm_analysis.md|Analisis JHM, sumber parsial, algoritma terbatas, hasil positif/negatif.
report/jhm_results.md|Tabel otomatis hasil JHM terbatas dan cakupan pengecualian.
report/jhm_supplement.md|Tabel/matriks otomatis audit sembilan contoh E19 dan aplikasi L01 2x94.
papers/external/download_queue.json|Antrean unduhan sumber yang dipilih; belum menyatakan sukses.
papers/external/download_outcomes.json|Status setiap unduhan antrean, termasuk kegagalan.'''.splitlines())

SOURCES = {
    'E01': 'Hosseini 2017: TDM1/TDM2/TDSM',
    'E02': 'halaman dataset RBSM penulis',
    'E03': 'halaman tautan data SSM; tidak menyajikan matriks lengkap saat diakses',
    'E04': 'halaman penerbit CSM',
    'E05': 'halaman penerbit MRM; bukan otomatis PDF penuh',
    'E06': 'halaman dataset/hasil CSM penulis',
    'E07': 'halaman akses PDF CSM',
    'E08': 'halaman folder publik data RBSM',
    'E09': 'halaman matriks EDM penulis',
    'E11': 'paper CSM 2026',
    'E12': 'suplemen matriks CSM; konflik sumber diaudit',
    'E13': 'suplemen hasil perbandingan CSM',
    'E14': 'suplemen waktu CSM',
    'E17': 'paper capacity-influenced 2024, prior art',
    'E19': 'Juman-Nawarathne 2019; Appendix A sumber benchmark JHM tambahan',
    'E20': 'paper iLCM 2016, prior art aturan seri',
    'E21': 'skripsi Indrawan 2021, hanya sampul satu halaman yang diperoleh',
    'E22': 'skripsi Rahayu UNHAS 2024; PDF hanya sampul/Bab 1-2, HTML rekaman repositori',
}
LOCAL = {'L01': 'BCE/IBFS', 'L02': 'RBSM', 'L03': 'SSM', 'L04': 'modifikasi VAM AIP', 'L05': 'THP'}


def describe(path):
    key = path.as_posix()
    if key in DESCRIPTIONS:
        return DESCRIPTIONS[key]
    if '__pycache__' in path.parts or path.suffix == '.pyc':
        return 'Cache bytecode otomatis Python; bukan sumber algoritma atau hasil ilmiah.'
    if path.name == '__init__.py':
        return 'Penanda paket Python untuk impor dan pemanggilan python -m.'
    if path.parent.as_posix() == 'papers/local_text':
        return f'Ekstraksi teks PDF lokal {path.stem}: {LOCAL[path.stem]}; periksa tabel terhadap PDF.'
    if path.parent.as_posix() == 'papers/page_checks':
        return 'Gambar halaman sumber terpilih untuk audit visual angka/rumus; ID/halaman mengikuti nama berkas.'
    if path.name.endswith('.source.json'):
        return f'Metadata asal unduhan {path.name[:-12]}: URL, waktu, ukuran/hash dan rincian akses yang dicatat.'
    if path.parent.as_posix() == 'papers/external':
        if path.name.startswith('rbsm_'):
            if path.suffix == '.cpp':
                return 'Kode C++ penulis RBSM untuk inspeksi; tidak dijalankan sebagai baseline proyek.'
            return 'Matriks mentah kasus ' + path.stem[5:] + ' dari dataset penulis RBSM; provenance ada di .source.json.'
        match = re.match(r'(E\d+)_', path.name)
        if match and match[1] in SOURCES:
            form = {'.pdf': 'PDF unduhan', '.html': 'HTML sumber tersimpan',
                    '.txt': 'Ekstraksi teks sumber'}.get(path.suffix, 'Berkas sumber')
            return f'{form}: {SOURCES[match[1]]}.'
    raise ValueError(f'Add a purpose description before indexing new file: {key}')


def main():
    files = set()
    for folder, dirs, names in os.walk(ROOT):
        # Repository/tool internals are not research artifacts and may hold private config.
        dirs[:] = [d for d in dirs if d not in {'.git', '.codex', '.agents', '.aws', '.venv', 'venv'}]
        files.update((Path(folder) / name).relative_to(ROOT) for name in names)
    files.add(TARGET.relative_to(ROOT))
    groups = {}
    for path in sorted(files, key=lambda p: p.as_posix().lower()):
        groups.setdefault(path.parent.as_posix(), []).append((path, describe(path)))
    cache_count = sum('__pycache__' in p.parts or p.suffix == '.pyc' for p in files)
    lines = ['# Indeks setiap berkas research\n\n',
             'Dibuat oleh `python research/document_tree.py`. Ini daftar berkas saat generator terakhir dijalankan; '
             'tanggal riset dan pembaruan ada pada masing-masing dokumen. '
             '[Panduan hubungan folder](STRUKTUR_FOLDER.md) memberi penjelasan alur kerja.\n\n',
             f'Tercatat **{len(files)} berkas**, termasuk {cache_count} cache Python. '
             'Cache tidak dihitung sebagai data penelitian. Metadata internal .git, konfigurasi alat tersembunyi '
             'dan lingkungan virtual tidak diindeks. Deskripsi sumber menyatakan tingkat akses, '
             'bukan jaminan kebenaran klaim paper.\n']
    for parent, records in groups.items():
        lines += [f'\n## {"research/ (root)" if parent == "." else parent + "/"}\n\n',
                  '| Berkas | Maksud/kegunaan |\n|---|---|\n']
        for path, purpose in records:
            lines.append(f'| [{path.name}]({path.as_posix()}) | {purpose} |\n')
    TARGET.write_text(''.join(lines), encoding='utf-8')
    print(f'Wrote {TARGET}: {len(files)} files, {cache_count} Python caches')


if __name__ == '__main__':
    main()
