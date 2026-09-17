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
jumlah_kursi = int(input("Masukkan kursi total yang tersedia: "))

kursi = []
status_kursi = []



def tampilkan_kursi(jumlah_kursi):
    for _ in range(jumlah_kursi):
        kursi.append("Tersedia")

    for index, status in enumerate(kursi):
                status_kursi.append(f'kursi {index+1} {status}')

    return (f'Kursi {index+1} {status}')

def pesan_kursi(nomor):
    status_kursi.remove(((nomor)-1))
    status_kursi.insert(((nomor)-1), f'kursi {nomor} terisi')
    return status_kursi(nomor)

    
    
while True:

    
    print('''

Selamat datang di XXI !!!
1. Lihat Kursi
2. Pesan Kursi
3. Batalkan Kursi
4. Keluar

''')

    opsi = int(input("Ingin buka apa? "))
    if opsi == 1:

        print(tampilkan_kursi(jumlah_kursi))

    if opsi == 2:
        
        nomor = int(input("Beli kursi nomor berapa :"))
        pesan_kursi(nomor)

         

    











#Loop kalau ingin meminta ketersediaan kursi
for index, status in enumerate(kursi):
    status_kursi.append(f'kursi {index} {status}')
    print(f'Kursi {index+1} {status}')



