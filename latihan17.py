# ============================================================
# LATIHAN 17 — FINAL BOSS
# Studi Kasus: Sistem Manajemen Toko Online
# ============================================================
#
# Deskripsi Masalah:
# Buat program toko online sederhana yang dapat mengelola
# produk, keranjang belanja, transaksi, dan stok.
#
# OBJEKTIF:
# - Menampilkan daftar produk.
# - Mencari produk.
# - Menambahkan produk ke keranjang.
# - Mengubah jumlah produk di keranjang.
# - Menghapus produk dari keranjang.
# - Menghitung total belanja.
# - Memberikan diskon berdasarkan kondisi tertentu.
# - Melakukan checkout.
# - Mengurangi stok setelah checkout berhasil.
# - Menampilkan ringkasan transaksi.
#
# SYARAT IMPLEMENTASI:
# - Gunakan function untuk setiap operasi utama.
# - Gunakan parameter dan return secara tepat.
# - Gunakan while untuk menu utama.
# - Gunakan looping untuk pencarian dan pengolahan data.
# - Gunakan conditional untuk validasi dan aturan bisnis.
# - Gunakan struktur data yang sesuai untuk produk dan keranjang.
# - Program tidak boleh berhenti hanya karena pengguna
#   memasukkan input yang tidak valid.
#
# SYARAT BERHASIL:
# - Produk dapat ditampilkan dan dicari.
# - Produk yang stoknya tidak cukup tidak dapat dimasukkan
#   melebihi stok tersedia.
# - Keranjang dapat ditambah, diubah, dan dikurangi.
# - Total belanja selalu mengikuti isi keranjang.
# - Diskon diterapkan hanya ketika syarat terpenuhi.
# - Checkout mengubah stok dengan benar.
# - Transaksi tidak dapat dilakukan jika keranjang kosong.
# - Ringkasan transaksi dapat ditampilkan.
# - Program tetap berjalan sampai pengguna memilih keluar.
#
# TANTANGAN TAMBAHAN:
# - Pisahkan program menjadi function-function kecil dengan
#   tanggung jawab yang jelas.
# - Hindari menulis kode yang sama berkali-kali.
# - Buat validasi input sebanyak yang menurutmu diperlukan.
# - Usahakan program mudah dikembangkan jika fitur baru
#   ingin ditambahkan.
#
# KAMUS:
# produk, keranjang : list/dict
# nama, kode, pilihan, status : string
# harga, stok, jumlah, total, diskon, total_akhir : float/int
# i, indeks : int
# dapat_diskon : bool
#
# ============================================================

# Tulis kode Python kamu di bawah ini
