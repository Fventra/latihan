# ============================================================
# LATIHAN 01
# Studi Kasus: Sistem Tarif Pengiriman
# ============================================================
#
# Deskripsi Masalah:
# Sebuah perusahaan ekspedisi menentukan biaya pengiriman
# berdasarkan berat paket dan jenis layanan.
#
# Spesifikasi Program:
#
# Input Data:
# - Nama pengirim (string)
# - Berat paket dalam kg (float)
# - Jenis layanan: "reguler" atau "express" (string)
#
# Proses:
# 1. Biaya dasar ditentukan berdasarkan berat:
#    - berat <= 1 kg  : Rp10.000
#    - berat <= 5 kg  : Rp20.000
#    - berat > 5 kg   : Rp20.000 + Rp5.000 untuk setiap kg
#                         di atas 5 kg
#
# 2. Jika layanan adalah "express", biaya dasar ditambah 50%.
#
# 3. Buat fungsi hitung_biaya(berat, layanan) yang mengembalikan
#    total biaya pengiriman.
#
# 4. Gunakan conditional untuk menentukan tarif.
#
# Output:
# - Nama pengirim
# - Total biaya pengiriman
#
# KAMUS:
# nama, layanan : string
# berat : float
# total_biaya : float
#
# FUNGSI:
# hitung_biaya(berat, layanan) -> float
#
# ============================================================

# Tulis kode Python kamu di bawah ini

nama = str(input("input nama? "))
berat = float(input("input berat? "))
layanan = input("Mau pilih layanan apa?" \
"a. reguler" \
"b. express" \
"(pilih a atau b)")
while layanan != "a" and layanan != "b":
    print("hanya pilih a atau b!")
    layanan = (input("Mau pilih layanan apa?" \
    "a. reguler" \
    "b. express" \
    "(pilih a atau b)"))
    if layanan == "a" or layanan == "b":
        break
def hitung_biaya(berat, layanan):
    biaya = 0

    if berat < 0:
        print("Beratnya tidak valid")
    elif 0 < berat <= 1:
        biaya = 10000
    elif berat <= 5:
        biaya = 20000
    elif berat > 5:
        biaya = 20000 + (berat-5) * 5000
    if layanan == "b":
        biaya *= 1.5
    return biaya

sapaan = f'Hallo,  {nama}'
print(sapaan)
hasil_akhir = hitung_biaya(berat, layanan)
total = f'Biaya yang diperlukan adalah {hasil_akhir}'
print(total)
