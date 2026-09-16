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

saldo_awal = int(input("Masukkan saldo awal: "))
saldo = saldo_awal
def tampilkan_menu():
    print( "Selamat datang di ATM" \
    "1. cek saldo" \
    "2. setor uang" \
    "3. tarik uang" \
    "4. keluar" \
    )
    menu = (input("pilih"))
    return int(menu)

def cek_saldo():
    return saldo

def setor_uang(saldo, jumlah):
    print(f"anda menyetor {jumlah}")
    return saldo + jumlah

def tarik_uang(saldo, jumlah):
    print(f"Anda menarik {jumlah}")
    return saldo - jumlah

while True :

    pilihan = tampilkan_menu()    
    if pilihan == 1:
        print(cek_saldo())
        continue

    elif pilihan == 2:
        jumlah_setor = int(input("Masukkan nominal: "))
        saldo = (setor_uang(saldo, jumlah_setor))
        print(saldo)
        continue

    elif pilihan == 3:
        jumlah_tarik = int(input("Masukkan nominal: "))
        saldo = (tarik_uang(saldo, jumlah_tarik))
        print(saldo)
        continue

    else:
        break
    
    