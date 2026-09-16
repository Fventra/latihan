# ============================================================
# LATIHAN 02
# Studi Kasus: Mesin ATM Sederhana
# ============================================================
#
# Deskripsi Masalah:
# Buat program ATM sederhana yang dapat melakukan beberapa
# transaksi berdasarkan pilihan pengguna.
#
# Spesifikasi Program:
#
# Input:
# - Saldo awal
#
# Program kemudian berulang kali menampilkan menu:
# 1. Cek saldo
# 2. Setor uang
# 3. Tarik uang
# 4. Keluar
#
# Proses:
# - Gunakan while agar menu terus muncul sampai pengguna
#   memilih "4".
# - Untuk setor, saldo bertambah sesuai jumlah setor.
# - Untuk tarik, periksa terlebih dahulu apakah saldo mencukupi.
# - Jika saldo tidak mencukupi, transaksi ditolak.
# - Gunakan conditional untuk memproses pilihan menu.
#
# Buat fungsi:
# - tampilkan_menu()
# - setor(saldo, jumlah)
# - tarik(saldo, jumlah)
#
# Fungsi setor() dan tarik() harus mengembalikan saldo terbaru.
#
# Output:
# Tampilkan pesan yang sesuai untuk setiap transaksi.
#
# KAMUS:
# saldo, jumlah : float
# pilihan : int
#
# FUNGSI:
# tampilkan_menu()
# setor(saldo, jumlah) -> float
# tarik(saldo, jumlah) -> float
#
# ============================================================

# Tulis kode Python kamu di bawah ini
