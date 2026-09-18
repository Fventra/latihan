# ============================================================
# LATIHAN 07
# Studi Kasus: Sistem Reservasi Kursi Bioskop
# ============================================================
#
# Deskripsi Masalah:
# Sebuah bioskop memiliki sejumlah kursi. Program digunakan
# untuk melakukan reservasi dan membatalkan reservasi.
#
# Spesifikasi Program:
#
# Input:
# - Jumlah kursi
#
# Setiap kursi memiliki status:
# - "Kosong"
# - "Terisi"
#
# Menu:
# 1. Lihat kursi
# 2. Pesan kursi
# 3. Batalkan kursi
# 4. Keluar
#
# Proses:
# - Gunakan while untuk menjalankan menu.
# - Gunakan looping untuk menampilkan seluruh kursi.
# - Saat memesan kursi, periksa apakah kursi masih kosong.
# - Saat membatalkan, periksa apakah kursi memang terisi.
# - Gunakan conditional untuk setiap kemungkinan kondisi.
#
# Buat fungsi:
# - tampilkan_kursi(kursi)
# - pesan_kursi(kursi, nomor)
# - batalkan_kursi(kursi, nomor)
#
# Fungsi harus mengubah status kursi sesuai operasi.
#
# Output:
# Tampilkan status kursi dan pesan setiap transaksi.
#
# KAMUS:
# kursi : list
# nomor, pilihan, i : int
#
# FUNGSI:
# tampilkan_kursi(kursi)
# pesan_kursi(kursi, nomor)
# batalkan_kursi(kursi, nomor)
#
# ============================================================

# Tulis kode Python kamu di bawah ini
# ============================================================
# LATIHAN 07
# Studi Kasus: Sistem Reservasi Kursi Bioskop
# ============================================================

jumlah_kursi = int(input("Masukkan jumlah kursi: "))

# Membuat semua kursi dalam keadaan kosong
kursi = ["Kosong"] * jumlah_kursi


def tampilkan_kursi(kursi):
    for i, status in enumerate(kursi):
        print(f"Kursi {i + 1}: {status}")


def pesan_kursi(kursi, nomor):
    indeks = nomor - 1

    if kursi[indeks] == "Kosong":
        kursi[indeks] = "Terisi"
        print(f"Kursi {nomor} berhasil dipesan.")
    else:
        print(f"Kursi {nomor} sudah terisi.")


def batalkan_kursi(kursi, nomor):
    indeks = nomor - 1

    if kursi[indeks] == "Terisi":
        kursi[indeks] = "Kosong"
        print(f"Reservasi kursi {nomor} berhasil dibatalkan.")
    else:
        print(f"Kursi {nomor} masih kosong.")


while True:
    print("""
===== MENU BIOSKOP =====
1. Lihat kursi
2. Pesan kursi
3. Batalkan kursi
4. Keluar
""")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        tampilkan_kursi(kursi)

    elif pilihan == 2:
        nomor = int(input("Masukkan nomor kursi: "))
        pesan_kursi(kursi, nomor)

    elif pilihan == 3:
        nomor = int(input("Masukkan nomor kursi: "))
        batalkan_kursi(kursi, nomor)

    elif pilihan == 4:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")



