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
