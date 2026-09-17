# ============================================================
# LATIHAN 06
# Studi Kasus: Sistem Penilaian Kompetisi
# ============================================================
#
# Deskripsi Masalah:
# Sebuah kompetisi memiliki beberapa peserta. Setiap peserta
# memperoleh tiga nilai dari juri.
#
# Spesifikasi Program:
#
# Input:
# - Jumlah peserta
# - Nama setiap peserta
# - Tiga nilai juri untuk setiap peserta
#
# Proses:
# 1. Gunakan looping untuk memproses seluruh peserta.
# 2. Buat fungsi hitung_nilai(n1, n2, n3) yang mengembalikan
#    rata-rata tiga nilai.
# 3. Tentukan status peserta:
#    - "Lolos" jika rata-rata >= 75
#    - "Tidak Lolos" jika rata-rata < 75
#
# 4. Simpan atau catat peserta dengan nilai tertinggi.
#
# 5. Jika terdapat peserta dengan rata-rata yang sama,
#    peserta yang diproses lebih dahulu dianggap sebagai
#    pemilik nilai tertinggi.
#
# Output:
# - Nilai rata-rata setiap peserta
# - Status setiap peserta
# - Nama peserta dengan nilai tertinggi
# - Nilai tertinggi
#
# KAMUS:
# n, i : int
# nama : string
# n1, n2, n3, rata_rata, tertinggi : float
# nama_tertinggi : string
# status : string
#
# FUNGSI:
# hitung_nilai(n1, n2, n3) -> float
#
# ============================================================

# Tulis kode Python kamu di bawah ini

jumlah_peserta = int(input("Berapa jumlah pesertanya: "))

daftar_nama = []
daftar_nilai = []
kelulusan = []


def hitung_nilai(n1, n2, n3):

    return  (n1 + n2 + n3) / 3

for i in range(jumlah_peserta):

    nama = str(input(f"Masukkan nama peserta {i+1}: "))
    daftar_nama.append(nama)
    n_1 = int(input("Penilaian nilai juri 1: "))
    n_2 = int(input("Penilaian nilai juri 2: "))
    n_3 = int(input("Penilaian nilai juri 3: "))

    rata2 = hitung_nilai(n_1, n_2, n_3)

    daftar_nilai.append(rata2)
     
    if rata2 >= 75:
           
        kelulusan.append("Lulus")

    else:
        kelulusan.append("Tidak Lulus")

    print(f"Nilai buat peserta {i+1} adalah {rata2}")

for n, v, k  in zip(daftar_nama, daftar_nilai, kelulusan):
    print(n, v, k)

gabungan = list(zip(daftar_nama, daftar_nilai, kelulusan))

tinggi = max(gabungan, key=lambda x: x[1])

daftar_nama, daftar_nilai, kelulusan = tinggi

print("Nilai tertinggi adalah:") 
print(daftar_nama, daftar_nilai, kelulusan)
