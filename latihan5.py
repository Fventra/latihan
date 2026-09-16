# ============================================================
# Studi Kasus: Sistem Kasir Sederhana
# ============================================================
#
# Deskripsi Masalah:
# Sebuah toko memberikan diskon berdasarkan total pembelian.
# Program harus menghitung total belanja dan total yang harus
# dibayar pelanggan.
#
# Spesifikasi Program:
#
# Input:
# - Nama pelanggan (teks)
# - Harga barang pertama (Rupiah, bilangan bulat)
# - Harga barang kedua (Rupiah, bilangan bulat)
# - Harga barang ketiga (Rupiah, bilangan bulat)
#
# Proses:
# Hitung total belanja:
#
# total = harga1 + harga2 + harga3
#
# Jika total >= Rp500.000:
# - Pelanggan mendapat diskon 10%.
#
# Jika total < Rp500.000:
# - Pelanggan tidak mendapat diskon.
#
# Buat variabel boolean "dapat_diskon":
# - True jika total >= Rp500.000
# - False jika total < Rp500.000
#
# Hitung total yang harus dibayar setelah diskon.
#
# Output:
# - "Halo, [nama]!"
# - "Total Belanja: Rp [total]"
# - "Mendapat Diskon: [dapat_diskon]"
# - "Total Bayar: Rp [total_bayar]"
#
# KAMUS:
# nama : string
# harga1, harga2, harga3 : int
# total, diskon, total_bayar : float
# dapat_diskon : bool
#
# ALGORITMA:
# 1. Input nama pelanggan.
# 2. Input harga ketiga barang.
# 3. Hitung total belanja.
# 4. Tentukan apakah pelanggan mendapat diskon.
# 5. Hitung nominal diskon.
# 6. Hitung total yang harus dibayar.
# 7. Tampilkan hasil.
# ============================================================


# Tulis kode Python kamu di bawah ini