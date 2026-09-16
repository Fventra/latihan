# ============================================================
# LATIHAN 10 — FINAL BOSS
# Studi Kasus: Sistem Manajemen Perpustakaan Mini
# ============================================================
#
# Deskripsi Masalah:
# Buat program perpustakaan sederhana yang dapat mengelola
# daftar buku dan peminjaman buku.
#
# Spesifikasi Program:
#
# Setiap buku memiliki:
# - Judul
# - Status peminjaman
#
# Status buku:
# - "Tersedia"
# - "Dipinjam"
#
# Input Awal:
# - Jumlah buku
# - Judul setiap buku
#
# Menu:
# 1. Tampilkan semua buku
# 2. Cari buku
# 3. Pinjam buku
# 4. Kembalikan buku
# 5. Statistik perpustakaan
# 6. Keluar
#
# Proses:
#
# 1. Program harus terus berjalan menggunakan while sampai
#    pengguna memilih menu 6.
#
# 2. Gunakan looping untuk menampilkan seluruh buku.
#
# 3. Saat mencari buku:
#    - Minta judul buku.
#    - Periksa seluruh daftar menggunakan looping.
#    - Jika ditemukan, tampilkan statusnya.
#    - Jika tidak ditemukan, tampilkan pesan yang sesuai.
#
# 4. Saat meminjam:
#    - Cari buku berdasarkan judul.
#    - Jika buku tidak ditemukan, tampilkan pesan.
#    - Jika buku sudah dipinjam, tampilkan pesan.
#    - Jika tersedia, ubah status menjadi "Dipinjam".
#
# 5. Saat mengembalikan:
#    - Cari buku berdasarkan judul.
#    - Jika buku sedang dipinjam, ubah status menjadi
#      "Tersedia".
#    - Jika buku sudah tersedia, tampilkan pesan yang sesuai.
#
# 6. Statistik:
#    - Hitung jumlah buku tersedia.
#    - Hitung jumlah buku dipinjam.
#    - Hitung persentase buku yang sedang dipinjam.
#
# Buat fungsi minimal:
# - tampilkan_buku(...)
# - cari_buku(...)
# - pinjam_buku(...)
# - kembalikan_buku(...)
# - statistik_buku(...)
#
# Gunakan return pada fungsi yang membutuhkan hasil.
#
# Gunakan conditional untuk menangani seluruh kemungkinan
# keadaan buku.
#
# Output:
# Program harus memberikan pesan yang jelas untuk setiap
# pilihan dan transaksi pengguna.
#
# KAMUS:
# buku : list
# judul, status, kata_kunci : string
# pilihan, i, jumlah_tersedia, jumlah_dipinjam : int
# persentase : float
#
# FUNGSI:
# tampilkan_buku(...)
# cari_buku(...)
# pinjam_buku(...)
# kembalikan_buku(...)
# statistik_buku(...)
#
# ============================================================
#
# Tantangan tambahan:
# - Buat pencarian tidak membedakan huruf besar dan kecil.
# - Tangani input menu yang tidak valid.
# - Jangan biarkan program crash karena nomor buku
#   yang tidak tersedia.
# - Usahakan fungsi-fungsi memiliki tugas yang jelas.
#
# ============================================================

# Tulis kode Python kamu di bawah ini
