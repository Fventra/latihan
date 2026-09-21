# ============================================================
# LATIHAN 08
# Studi Kasus: Pengelolaan Stok Barang
# ============================================================
#
# Deskripsi Masalah:
# Sebuah toko ingin membuat program sederhana untuk mengelola
# stok beberapa barang.
#
# Spesifikasi Program:
#
# Input:
# - Jumlah barang
# - Nama barang
# - Stok awal setiap barang
#
# Setelah data dimasukkan, program memiliki menu:
# 1. Lihat stok
# 2. Tambah stok
# 3. Kurangi stok
# 4. Keluar
#
# Proses:
# - Gunakan looping untuk menampilkan barang.
# - Gunakan while untuk menjalankan menu.
# - Saat mengurangi stok, stok tidak boleh menjadi negatif.
# - Jika stok suatu barang <= 5, tampilkan bahwa stok hampir
#   habis.
#
# Buat fungsi:
# - tampilkan_stok(...)
# - tambah_stok(...)
# - kurangi_stok(...)
# - cek_stok(...)
#
# Gunakan conditional di dalam fungsi cek_stok().
#
# Output:
# - Daftar stok barang
# - Pesan transaksi
# - Peringatan untuk stok yang hampir habis
#
# KAMUS:
# nama_barang : string
# stok, jumlah, pilihan, nomor, i : int
#
# FUNGSI:
# tampilkan_stok(...)
# tambah_stok(...)
# kurangi_stok(...)
# cek_stok(...)
#
# ============================================================
#
# Catatan:
# Kamu bebas menentukan struktur data yang digunakan.
# Tantangan utama adalah menggabungkan function, conditional,
# looping, dan pengelolaan beberapa data.
# ============================================================

# Tulis kode Python kamu di bawah ini

#inuput awal
jumlah_barang = int(input("Jumlah Barang: "))
list_nama = []
list_jumlah = []
test = 0

while test != jumlah_barang:
    nama = input("Nama barang: ")
    list_nama.append(nama)
    jumlah = input("Jumlah barang: ")
    list_jumlah.append(jumlah)
    test += 1

zipped = list(zip(list_jumlah, list_nama))

for jumlah, nama in zipped:
    print(f'{nama}: {jumlah}')





def menu():
    print('''---------------
    1. lihat stok
    2. Tambah stok
    3. Kurangi stok
    4. Keluar
    ---------------''')
    menu_t = int(input("Pilih Menu: "))
    return menu_t
menu()
while menu() != 4:
    if stock <= 5:
        print("Stok hampir habis")
    if menu() == 1:
        print(stock)

