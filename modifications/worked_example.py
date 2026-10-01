"""Build and verify the same paper-style worked example in all modification MDs.

Only the marked documentation sections and the example's evidence JSON are written.
Baseline/variant algorithms and frozen benchmark results are not changed.
"""
import json
from pathlib import Path

import numpy as np

from ..methods import solve
from ..methods.common import balance
from ..methods.constructive import construct, ranked_cells
from ..methods.mrm import solve_mrm
from ..solver.optimal_lp import optimal
from .variants import solve_variant

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
BEGIN = '<!-- BEGIN SHARED WORKED EXAMPLE -->'
END = '<!-- END SHARED WORKED EXAMPLE -->'
PROBLEM = 'L05_Example1'


def n(value):
    return f'{float(value):g}'


def cell(i, j):
    return f'x{i+1}{j+1}'


def vector(v):
    return '[' + ', '.join(n(x) for x in v) + ']'


def table(headers, rows):
    return ('| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join(['---'] * len(headers)) +
            ' |\n' + ''.join('| ' + ' | '.join(map(str, row)) + ' |\n' for row in rows) + '\n')


def penalty(values, method):
    ordered = sorted(values)
    if method == 'VAM':
        return float(ordered[1]-ordered[0]) if len(ordered)>1 else 0.0
    return float(ordered[-1]-ordered[0])


def tableau(C, s, d, rows, cols, method, axis=None):
    # Explicit active sets preserve MRM's zero-margin line until source-rule elimination.
    rp = {i: penalty(C[i, cols], method) for i in rows}
    cp = {j: penalty(C[rows, j], method) for j in cols}
    header = ['Sumber / tujuan'] + [f'D{j+1}' for j in cols] + ['Sisa supply', 'Penalti baris']
    body = [[f'S{i+1}']+[n(C[i,j]) for j in cols]+[n(s[i]),n(rp[i]) if axis!=1 else '—'] for i in rows]
    body += [['Sisa demand']+[n(d[j]) for j in cols]+[n(sum(s)), '—'],
             ['Penalti kolom']+[n(cp[j]) if axis!=0 else '—' for j in cols]+['—','—']]
    return table(header,body),rp,cp


def allocation_table(X, s, d):
    rows = [[f'S{i+1}']+[n(v) for v in row]+[n(sum(row)), n(s[i])] for i,row in enumerate(X)]
    rows += [['Jumlah kolom']+[n(v) for v in X.sum(axis=0)]+[n(X.sum()), '—'],
             ['Demand']+[n(v) for v in d]+[n(sum(d)), '—']]
    return table(['Alokasi']+[f'D{j+1}' for j in range(X.shape[1])]+['Jumlah baris','Supply'], rows)


def cost_expression(C, X):
    return ' + '.join(f'{n(X[i,j])}×{n(C[i,j])}' for i,j in zip(*np.nonzero(X))) or '0'


def sequence(trace):
    return ' → '.join(f'{cell(t["row"],t["column"])}={n(t["quantity"])}' for t in trace) or 'tidak ada pengiriman sisa'


def intro(p):
    C,s,d,_=balance(p['costs'],p['supply'],p['demand'])
    return ('## 6. Contoh soal bersama: L05 Example 1, dihitung sampai selesai\n\n'
            'Soal ini **sama persis** dengan contoh pada dua dokumen modifikasi lainnya dan '
            '[README](README.md#contoh-soal-bersama). Sumber matriks: paper lokal **L05**, '
            'Amaliah, Fatichah & Suryani (2021), Example 1, '
            '[DOI 10.1109/ICTS52701.2021.9608005](https://doi.org/10.1109/ICTS52701.2021.9608005). '
            'Hasil modifikasi di bawah adalah perhitungan proyek, bukan hasil varian yang diklaim paper tersebut.\n\n'
            '**Soal:** empat sumber S1–S4 harus memenuhi permintaan empat tujuan D1–D4. '
            'Angka di dalam tabel adalah biaya per unit. Tentukan alokasi dengan biaya total rendah.\n\n'+
            table(['Sumber']+[f'D{j+1}' for j in range(4)]+['Supply'],
                  [[f'S{i+1}']+[n(v) for v in C[i]]+[n(s[i])] for i in range(4)]+
                  [['Demand']+[n(v) for v in d]+[n(sum(d))]])+
            '`Σ supply = 50+55+75+60 = 240 = 90+65+30+55 = Σ demand`; '
            '**tidak diperlukan dummy**. Pada tabel residu, biaya per unit tetap; '
            'hanya baris/kolom aktif serta sisa margin yang berubah.\n\n'
            'Semua indeks penjelasan mulai dari **1**: `x13` berarti pengiriman S1 ke D3. '
            'JSON/kode menggunakan indeks mulai 0. Tanda `—` berarti tidak dihitung/tidak berlaku, bukan angka nol.\n\n')


def ending(C,s,d,baseline,modified,cert,method):
    X=np.asarray(modified['allocation'])
    u=np.array([1,0,5,2]); v=np.array([5,-1,0,1])
    assert np.all(u[:,None]+v[None,:]<=C) and u@s+v@d==985
    assert modified['cost']==985 and modified['basic'] and modified['feasible']
    gap=100*(baseline['cost']-cert['cost'])/cert['cost']
    accuracy=100*cert['cost']/baseline['cost']
    return ('### Hasil akhir, kelayakan, dan optimum\n\n'+allocation_table(X,s,d)+
            f'`Z_mod = {cost_expression(C,X)} = {n(modified["cost"])}.`\n\n'+
            table(['Ukuran','Baseline '+method,'Modifikasi'],[
                ['Biaya',n(baseline['cost']),n(modified['cost'])],
                ['Optimum LP',n(cert['cost']),n(cert['cost'])],
                ['Gap absolut',n(baseline['cost']-cert['cost']),'0'],
                ['Gap %',f'{gap:.4f}%','0%'],
                ['Accuracy = 100×Z_opt/Z',f'{accuracy:.4f}%','100%']])+
            f'Penghematan = `{n(baseline["cost"])}−985 = {n(baseline["cost"]-985)}`. '
            'Setiap jumlah baris sama dengan supply dan setiap jumlah kolom sama dengan demand. '
            'Ada enam sel positif, sedangkan `m+n−1=7`: ini **BFS degenerat**, bukan solusi tidak layak. '
            'Tambahkan `x14=0` sebagai sel basis yang tidak membentuk siklus; biaya tidak berubah.\n\n'
            'Optimum juga dapat diperiksa secara manual: ambil `u=[1,0,5,2]` dan '
            '`v=[5,−1,0,1]`. Semua `u_i+v_j≤C_ij`, dan nilai dual '
            '`u·s+v·d=(50+375+120)+(450−65+55)=545+440=985`. '
            'Solusi feasible di atas mencapai batas bawah 985, sehingga optimal pada soal ini. '
            'Potensial/LP ini hanya **verifikasi setelah algoritma**, tidak dipakai untuk memilih kandidat.\n\n'
            'Keberhasilan satu soal adalah ilustrasi mekanisme, bukan bukti keunggulan universal. '
            'Kesimpulan lintas-kasus tetap menggunakan seluruh suite yang dilaporkan.\n\n')


def rollout_section(p,base,cert):
    C,s,d,_=balance(p['costs'],p['supply'],p['demand']); s0=s.copy(); d0=d.copy()
    result=solve_variant(C,s,d,base+'_top2_rollout',trace=True)
    baseline=solve(C,s,d,base,trace=True)
    assert baseline['cost']==p['claims'][base]
    text=intro(p)
    text+=('### Pembanding baseline dan arti skor\n\n'
           f'Baseline {base} pada soal lengkap mengirim dalam urutan:\n\n`{sequence(baseline["trace"])}`.\n\n'
           f'Biayanya `{cost_expression(C,np.asarray(baseline["allocation"]))} = {n(baseline["cost"])}`; '
           'angka baseline ini cocok dengan paper L05.\n\n'
           'Di setiap iterasi, `B` adalah biaya yang sudah benar-benar dikomit. Untuk calon a, '
           '`F(a)=biaya alokasi sementara+biaya completion baseline pada sisa`. '
           'Kolom `B+F` adalah estimasi biaya total dari awal. **Jangan menjumlahkan F dari berbagai iterasi**; '
           'F bukan biaya tambahan yang semuanya dikirim. Calon dicoba satu per satu pada salinan margin yang sama; '
           'completion hanya simulasi. Setelah memilih calon, komit satu alokasi saja.\n\n')
    if base=='VAM':
        text+=('Penalti = biaya terkecil kedua dikurangi biaya terkecil (nilai seri tetap dihitung). '
               'Contoh awal: `P_S4=7−3=4`, `P_D4=3−1=2`. '
               'Urutkan garis berdasarkan penalti menurun, lalu baris sebelum kolom dan indeks meningkat; '
               'ambil minimum setiap garis termasuk seri, deduplikasi sel, lalu ambil dua calon pertama.\n\n')
    else:
        text+=('Penalti THP = maksimum−minimum. Contoh awal: `P_D4=9−1=8`, `P_S2=7−1=6`. '
               'Pilih dua tingkat penalti berbeda tertinggi, kumpulkan minimum seluruh garis pada tingkat itu, '
               'deduplikasi, urutkan `(CA=C×min(s,d), C, i, j)`, lalu ambil dua sel pertama.\n\n')
    committed=0.; X=np.zeros_like(C); evidence=[]
    for index,t in enumerate(result['trace'],1):
        rows=list(np.flatnonzero(s>1e-8)); cols=list(np.flatnonzero(d>1e-8))
        grid,rp,cp=tableau(C,s,d,rows,cols,base)
        pts=ranked_cells(C,s,d,base); selected=pts[:2]
        assert [list(a) for a in selected]==t['candidates']
        text+=f'### Iterasi {index}: B={n(committed)}\n\n'+grid
        if base=='THP':
            levels=sorted(set([*rp.values(),*cp.values()]),reverse=True)[:2]
            chosen_lines=[f'S{i+1}' for i in rows if rp[i] in levels]+[f'D{j+1}' for j in cols if cp[j] in levels]
            text+=f'Tingkat penalti terpilih: `{vector(levels)}`; garis: **{", ".join(chosen_lines)}**. '
            text+='Urutan sel setelah CA: `'+', '.join(f'{cell(i,j)} (CA={n(C[i,j]*min(s[i],d[j]))})' for i,j in pts)+'`.\n\n'
        else:
            lines=[(rp[i],0,int(i)) for i in rows]+[(cp[j],1,int(j)) for j in cols]
            lines.sort(key=lambda a:(-a[0],a[1],a[2]))
            text+='Urutan garis: `'+', '.join(f'{"S" if a==0 else "D"}{k+1}({n(v)})' for v,a,k in lines)+'`. '
            text+='Urutan sel setelah deduplikasi: `'+', '.join(cell(i,j) for i,j in pts)+'`.\n\n'
        candidate_rows=[]; candidates=[]
        for pos,(i,j) in enumerate(selected):
            q=min(s[i],d[j]); ss=s.copy(); dd=d.copy(); ss[i]-=q; dd[j]-=q
            Y,completion_trace=construct(C,ss,dd,base,trace=True)
            remaining=float(np.sum(C*Y)); immediate=float(q*C[i,j]); score=immediate+remaining
            assert score==t['scores'][pos]
            assert np.allclose(Y.sum(axis=1),ss) and np.allclose(Y.sum(axis=0),dd)
            candidate_rows.append([cell(i,j),n(q),n(C[i,j]),n(immediate),n(remaining),n(score),n(committed+score)])
            candidates.append(dict(cell=[i+1,j+1],quantity=float(q),remaining_supply=ss.tolist(),
                                   remaining_demand=dd.tolist(),completion=Y.tolist(),completion_trace=completion_trace,
                                   immediate=immediate,remaining_cost=remaining,score=score,total_estimate=committed+score))
        text+=table(['Calon','q=min(s,d)','C','q×C','Z sisa','F','B+F'],candidate_rows)
        for candidate in candidates:
            i,j=[a-1 for a in candidate['cell']]
            text+=(f'- **Simulasi {cell(i,j)}={n(candidate["quantity"])}:** '
                   f'sementara `s={vector(candidate["remaining_supply"])}`, `d={vector(candidate["remaining_demand"])}`. '
                   f'Completion {base}: `{sequence(candidate["completion_trace"])}`. '
                   f'Biaya sisa = `{cost_expression(C,np.asarray(candidate["completion"]))} = {n(candidate["remaining_cost"])}`.\n')
        text+='\n'
        assert t['chosen']==min(range(len(candidates)),key=lambda k:candidates[k]['score'])
        i,j=t['row'],t['column']; q=t['quantity']; old_s=s.copy(); old_d=d.copy()
        X[i,j]+=q; s[i]-=q; d[j]-=q; committed+=q*C[i,j]
        eliminated=[f'S{k+1}' for k in rows if s[k]==0]+[f'D{k+1}' for k in cols if d[k]==0]
        reason=('Hanya satu calon tersedia.' if len(candidates)==1 else
                'F seri; pilih calon pertama menurut urutan baseline.' if candidates[0]['score']==candidates[1]['score'] else
                'Pilih F terkecil.')
        text+=(f'**Keputusan:** {reason} Komit `{cell(i,j)}=min({n(old_s[i])},{n(old_d[j])})={n(q)}`. '
               f'Garis yang selesai: **{", ".join(eliminated)}**. '
               f'Sisa `s={vector(s)}`, `d={vector(d)}`; biaya terkomit menjadi **B={n(committed)}**.\n\n')
        evidence.append(dict(iteration=index,before_supply=old_s.tolist(),before_demand=old_d.tolist(),
                             row_penalties={str(k+1):v for k,v in rp.items()},column_penalties={str(k+1):v for k,v in cp.items()},
                             candidates=candidates,chosen=t['chosen'],after_supply=s.tolist(),after_demand=d.tolist(),committed_cost=committed))
    assert np.array_equal(X,np.asarray(result['allocation'])) and committed==result['cost']
    text+=ending(C,s0,d0,baseline,result,cert,base)
    text+=('### Jalankan soal yang sama\n\n```powershell\n'
           f'python -m research.modifications.demo --method {base.lower()} --problem {PROBLEM} --trace --json\n'
           '```\n\n'+rebuild_note())
    return text,dict(baseline=baseline,modified=result,iterations=evidence)


def mrm_construction(C,s0,d0,result,orientation):
    s=s0.copy(); d=d0.copy(); rows=list(range(len(s))); cols=list(range(len(d)))
    axis=orientation; X=np.zeros_like(C); text=''; evidence=[]; committed=0.
    for index,t in enumerate(result['trace'],1):
        grid,_,_=tableau(C,s,d,rows,cols,'MRM',axis)
        text+=f'#### Langkah {index}\n\n'+grid
        options=[]
        for a in ([axis] if axis is not None else [0,1]):
            for k in (rows if a==0 else cols):
                pts=[(k,j) for j in cols] if a==0 else [(i,k) for i in rows]
                costs=[C[i,j] for i,j in pts]
                target=min(pts,key=lambda p:(C[p],*p))
                options.append((-(max(costs)-min(costs)),min(costs),a,k,target))
        chosen=min(options); _,minimum,axis,k,(i,j)=chosen
        assert (i,j,axis)==(t['row'],t['column'],t['orientation'])
        si,dj=s[i],d[j]; q=min(si,dj); assert q==t['quantity']
        X[i,j]+=q; s[i]-=q; d[j]-=q; committed+=q*C[i,j]
        if si<dj: rows.remove(i); removed=f'S{i+1}'
        elif dj<si: cols.remove(j); removed=f'D{j+1}'
        elif axis==0: rows.remove(i); removed=f'S{i+1} saja; D{j+1} bermargin nol masih dipertahankan'
        else: cols.remove(j); removed=f'D{j+1} saja; S{i+1} bermargin nol masih dipertahankan'
        tied=[o for o in options if o[0]==chosen[0]]
        text+=(f'Pilih **{"baris S" if axis==0 else "kolom D"}{k+1}**, '
               f'rentang `{n(-chosen[0])}`, minimum biaya `{n(minimum)}`. ')
        if len(tied)>1:
            text+=('Ada seri rentang: `'+', '.join(f'{"S" if o[2]==0 else "D"}{o[3]+1} (min={n(o[1])})' for o in tied)+
                   '`; pecahkan dengan minimum biaya lebih rendah, lalu baris sebelum kolom dan indeks. ')
        text+=(f'Sel minimum dipilih menurut `(C,i,j)`: **{cell(i,j)}**. '
               f'Alokasi `min({n(si)},{n(dj)})={n(q)}`; biaya langkah `{n(q)}×{n(C[i,j])}={n(q*C[i,j])}`. '
               f'Hapus **{removed}**.\n\n'
               f'Sisa `s={vector(s)}`, `d={vector(d)}`; biaya terkomit **{n(committed)}**. '
               f'Orientasi {"baris" if axis==0 else "kolom"} tetap terkunci.\n\n')
        if q==0:
            text+=('Langkah nol ini tidak mengirim barang dan tidak menambah biaya; '
                   'ia mengeluarkan garis bermargin nol yang masih dipertahankan oleh aturan eliminasi MRM. '
                   'Jangan menghapus langkah ini dari replay algoritma.\n\n')
        evidence.append(dict(iteration=index,row=i+1,column=j+1,quantity=float(q),orientation=axis,
                             remaining_supply=s.tolist(),remaining_demand=d.tolist(),committed_cost=committed))
    assert np.array_equal(X,np.asarray(result['allocation'])) and committed==result['cost']
    text+=allocation_table(X,s0,d0)+f'Biaya konstruksi = `{cost_expression(C,X)} = {n(committed)}`.\n\n'
    return text,evidence


def rebuild_note():
    return ('Angka tableau, setiap completion, dan hasil akhir dicocokkan dengan fungsi program. '
            'Bukti terstruktur: [worked_example_L05_Example1.json](../results/worked_example_L05_Example1.json). '
            'Untuk membangun ulang bagian contoh pada ketiga Markdown dan README:\n\n'
            '```powershell\npython -m research.modifications.worked_example\n```\n\n'
            'Perintah tersebut memperbarui bagian contoh yang diberi penanda dan JSON contoh saja; '
            'aturan algoritma serta CSV suite utama tetap sama.\n')


def mrm_section(p,cert):
    C,s,d,_=balance(p['costs'],p['supply'],p['demand'])
    runs={name:solve_mrm(C,s,d,orientation=axis,trace=True)
          for name,axis in [('default',None),('rows',0),('columns',1)]}
    modified=solve_variant(C,s,d,'MRM_orientation_ensemble',trace=True)
    assert runs['default']['trace']==runs['columns']['trace']
    assert [runs[k]['cost'] for k in runs]==[1045,985,1045]
    assert modified['allocation']==runs['rows']['allocation']
    text=intro(p)
    text+=('### Rencana tiga konstruksi dari input yang sama\n\n'
           'Hitung `default`, `rows`, dan `columns` **masing-masing dari margin awal**. '
           'Pada soal ini default memilih kolom pada langkah pertama, sehingga seluruh jejaknya sama '
           'dengan konstruksi columns. Keduanya dihitung terpisah oleh kode; tabel lengkap di bawah '
           'mewakili kedua konstruksi yang identik tersebut. Rows memiliki tabel lengkap tersendiri. '
           'Biaya MRM 1045 pada matriks L05 ini adalah hasil hitungan kita, bukan angka MRM dalam paper THP 2021.\n\n'
           'Rentang = maksimum−minimum. Saat orientasi sudah terkunci, penalti orientasi lain diberi `—`. '
           'Baris/kolom bermargin nol yang belum dieliminasi tetap ikut rentang sesuai kode MRM.\n\n'
           '### Konstruksi A: default; juga jejak konstruksi C: paksa kolom\n\n'
           'Pada langkah pertama default mempertimbangkan baris dan kolom. Rentang tertinggi '
           '`D4=9−1=8` memilih kolom, minimum `C24=1`; orientasi berikutnya selalu kolom. '
           'Konstruksi columns langsung membatasi penilaian ke kolom dan memilih D4 yang sama.\n\n')
    body,default_evidence=mrm_construction(C,s,d,runs['default'],None); text+=body
    text+=('### Konstruksi B: paksa baris dari awal\n\n'
           'Kembali ke supply `[50,55,75,60]` dan demand `[90,65,30,55]`. '
           'Rentang kolom tidak digunakan, sekalipun nilainya lebih besar. '
           'Penalti baris awal `[5,6,6,4]`; S2 dan S3 seri 6, tetapi minimum biaya S2=1 '
           'lebih rendah dari S3=4, sehingga pilih S2.\n\n')
    body,rows_evidence=mrm_construction(C,s,d,runs['rows'],0); text+=body
    text+=('### Pilih konstruksi termurah\n\n'+
           table(['Konstruksi','Orientasi','Urutan alokasi termasuk langkah nol','Biaya'],
                 [[name,'baris' if run['orientation']==0 else 'kolom',sequence(run['trace']),n(run['cost'])]
                  for name,run in runs.items()])+
           '`Z_ensemble = min(1045,985,1045) = 985`; ambil **seluruh matriks hasil rows**. '
           'Tidak ada alokasi dari konstruksi default yang dicampurkan ke hasil rows. '
           'Perbedaan penting muncul setelah pengiriman pertama: default bergerak ke x13, '
           'sedangkan rows bergerak ke x32, sehingga kapasitas untuk D2 dibagi berbeda.\n\n')
    text+=ending(C,s,d,runs['default'],modified,cert,'MRM')
    text+=('### Jalankan soal yang sama\n\n```powershell\n'
           f'python -m research.modifications.demo --method mrm --problem {PROBLEM} --trace --json\n'
           '```\n\n'
           'Argumen `--problem` penting: demo MRM tanpa argumen ini tetap memakai E01_Example1 '
           'sebagai contoh default historis. Perintah di atas memakai L05_Example1 yang sama dengan VAM dan THP. '
           'Demo menampilkan jejak konstruksi pemenang; JSON bukti berikut menyimpan ketiga konstruksi.\n\n'+rebuild_note())
    return text,dict(constructions=runs,modified=modified,default_steps=default_evidence,rows_steps=rows_evidence)


def readme_section(p,evidence):
    C,s,d,_=balance(p['costs'],p['supply'],p['demand'])
    text=('## Contoh soal bersama\n\n'
          '**Ketiga dokumen kini memakai L05 Example 1 yang sama**, agar perbedaan keputusan terlihat '
          'pada matriks identik. Ini soal dari paper THP lokal, '
          '[Amaliah et al. (2021)](https://doi.org/10.1109/ICTS52701.2021.9608005). '
          'Masing-masing dokumen memuat tableau setiap iterasi, penjelasan seri, pembaruan margin, '
          'matriks akhir dan verifikasi optimum, seperti penyajian contoh numerik dalam paper.\n\n'+
          table(['Sumber','D1','D2','D3','D4','Supply'],
                [[f'S{i+1}']+[n(v) for v in C[i]]+[n(s[i])] for i in range(4)]+
                [['Demand']+[n(v) for v in d]+['240']]))
    text+=('Supply dan demand masing-masing 240, sehingga tidak memakai dummy. Indeks berikut mulai 1. '
           'Setiap algoritma dimulai lagi dari tabel awal, bukan melanjutkan hasil algoritma lain.\n\n')
    text+=table(['Algoritma','Langkah keputusan pada soal ini','Hasil'],[
        ['[VAM](vam_top2_rollout.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai)',
         '1. Penalti dua minimum → calon x44 dan x13. 2. Completion memberi 1095 dan 985 → pilih x13=30. '
         '3. Ulangi evaluasi: x24=55, x32=65, x11=20, x41=60, x31=10.', '1095 → 985'],
        ['[THP](thp_top2_rollout.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai)',
         '1. Dua tingkat rentang tertinggi menghasilkan calon x13 dan x24; F seri 1045 → x13=30. '
         '2. Pada iterasi berikutnya F(x24)=1015, F(x32)=955 → x32=65. '
         '3. Lanjut x24=55, x31=10, x11=20, x41=60.', '1045 → 985'],
        ['[MRM](mrm_orientation_ensemble.md#6-contoh-soal-bersama-l05-example-1-dihitung-sampai-selesai)',
         '1. Dari awal jalankan default (kolom): 1045. 2. Ulangi dari awal dengan rows: 985. '
         '3. Ulangi dari awal dengan columns: 1045. 4. Pilih seluruh alokasi rows.', '1045 → 985']])
    text+=('Penjelasan panjang VAM/THP menunjukkan **setiap kandidat dan seluruh urutan completion sementara**; '
           'penjelasan MRM menunjukkan **setiap langkah kedua orientasi**, termasuk alokasi nol untuk eliminasi. '
           'Pada VAM/THP, F mengecualikan biaya yang sudah dikomit; biaya itu ditampilkan sebagai B agar '
           'angka 955 tidak keliru dibaca sebagai total akhir 985.\n\n'
           'Ketiganya menghasilkan matriks yang sama:\n\n'+
           allocation_table(np.asarray(evidence['VAM']['modified']['allocation']),s,d)+
           '`Z=20×6+30×1+55×1+10×10+65×4+60×7=985`, sama dengan optimum LP '
           'dan batas dual yang ditunjukkan di setiap dokumen. Biaya MRM di sini dihitung proyek, '
           'bukan klaim MRM dari paper THP.\n\n'
           'Jalankan semuanya pada soal bersama tersebut:\n\n```powershell\n'
           f'python -m research.modifications.demo --problem {PROBLEM}\n'
           f'python -m research.modifications.demo --problem {PROBLEM} --trace --json\n'
           '```\n\n'+rebuild_note())
    return text


def replace_section(path,text):
    source=path.read_text(encoding='utf-8')
    block=BEGIN+'\n'+text.rstrip()+'\n'+END
    if BEGIN in source:
        assert source.count(BEGIN)==source.count(END)==1
        before,rest=source.split(BEGIN); _,after=rest.split(END)
        source=before+block+after
    else:
        source=source.rstrip()+'\n\n'+block+'\n'
    path.write_text(source,encoding='utf-8')


def main():
    cases=json.loads((ROOT/'datasets/published/benchmarks.json').read_text(encoding='utf-8'))
    p=next(p for p in cases if p['id']==PROBLEM)
    cert=optimal(p['costs'],p['supply'],p['demand'])
    assert cert['cost']==p['claims']['optimal']==985
    evidence=dict(problem=p,optimal=cert,index_convention='Report/candidate cells 1-based; raw algorithm traces 0-based')
    docs={}
    for base in ['VAM','THP']:
        docs[base.lower()+'_top2_rollout.md'],evidence[base]=rollout_section(p,base,cert)
    docs['mrm_orientation_ensemble.md'],evidence['MRM']=mrm_section(p,cert)
    docs['README.md']=readme_section(p,evidence)
    target=ROOT/'results/worked_example_L05_Example1.json'
    target.write_text(json.dumps(evidence,indent=2,allow_nan=False),encoding='utf-8')
    for filename,text in docs.items():
        replace_section(HERE/filename,text)
    print('PASS: every candidate completion, allocation replay, MRM orientation and optimum checked.')
    print('Updated 4 Markdown example sections and',target)


if __name__=='__main__':
    main()
