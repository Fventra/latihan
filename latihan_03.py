# ============================================================
# LATIHAN 03
# Studi Kasus: Analisis Nilai Ujian
# ============================================================
#
# Deskripsi Masalah:
# Seorang dosen ingin menganalisis nilai ujian dari sejumlah
# mahasiswa.
#
# Spesifikasi Program:
#
# Input:
# - Jumlah mahasiswa (int)
# - Nilai setiap mahasiswa (float)
#
# Proses:
# 1. Gunakan looping untuk menerima nilai seluruh mahasiswa.
# 2. Buat fungsi tentukan_grade(nilai) yang menghasilkan:
#    - A jika nilai >= 85
#    - B jika 75 <= nilai < 85
#    - C jika 65 <= nilai < 75
#    - D jika 50 <= nilai < 65
#    - E jika nilai < 50
#
# 3. Hitung:
#    - rata-rata nilai
#    - nilai tertinggi
#    - nilai terendah
#    - jumlah mahasiswa yang lulus
#
# 4. Mahasiswa lulus jika nilai >= 65.
#
# Output:
# - Rata-rata
# - Nilai tertinggi
# - Nilai terendah
# - Jumlah mahasiswa lulus
#
# KAMUS:
# n, i, jumlah_lulus : int
# nilai, total, rata_rata, tertinggi, terendah : float
# grade : string
#
# FUNGSI:
# tentukan_grade(nilai) -> string
#
# ============================================================

# Tulis kode Python kamu di bawah ini

def tentukan_grade(nilai):
    
    if nilai >= 85:
        return "A"
    if 75 <= nilai < 85:
        return "B"
    if 65 <= nilai < 75:
        return "C"
    else:
        return "tidak lulus"
nilai_total = []
jumlah_siswa = 0
while True:
    nilai = int(input("masukkan nilai: "))
    print(f' Nilai kamu adalah: {tentukan_grade(nilai)}')
    nilai_total.append(nilai)
    jumlah_siswa += 1
    conf = int(input("Apakaha masih ada nilai yang ingin diimput?:" \
    "1. Ya" \
    "2. Tidak"))
    if conf == 2:
        rata = sum(nilai_total) / jumlah_siswa
        nilai_max = max(nilai_total)
        nilai_min = min(nilai_total)
        print(rata)
        print(nilai_max)
        print(nilai_min)
        print(jumlah_siswa)
        break
    else:
        continue
    



    