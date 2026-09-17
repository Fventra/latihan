# ============================================================
# LATIHAN 05
# Studi Kasus: Permainan Tebak Angka
# ============================================================
#
# Deskripsi Masalah:
# Buat permainan tebak angka. Program memiliki sebuah angka
# rahasia. Pemain harus menebaknya sampai benar atau sampai
# jumlah percobaan habis.
#
# Spesifikasi Program:
#
# Input:
# - Angka rahasia
# - Maksimal jumlah percobaan
# - Tebakan pemain pada setiap percobaan
#
# Proses:
# 1. Gunakan while untuk mengulang tebakan.
# 2. Jika tebakan lebih kecil dari angka rahasia, tampilkan
#    "Terlalu kecil".
# 3. Jika tebakan lebih besar, tampilkan "Terlalu besar".
# 4. Jika sama, permainan selesai.
# 5. Permainan juga selesai jika percobaan habis.
#
# Buat fungsi:
# cek_tebakan(tebakan, rahasia)
# yang mengembalikan:
# - -1 jika tebakan terlalu kecil
# -  0 jika tebakan benar
# -  1 jika tebakan terlalu besar
#
# Output:
# - Petunjuk setiap tebakan
# - Jumlah percobaan
# - Pesan menang atau kalah
#
# KAMUS:
# rahasia, tebakan, maksimal, percobaan : int
# hasil : int
#
# FUNGSI:
# cek_tebakan(tebakan, rahasia) -> int
#
# ============================================================

# Tulis kode Python kamu di bawah ini


def cek_tebakan(tebakan, rahasia):
        
        if ( tebakan < rahasia):

            print("Tebakan terlalu kecil!")
            return -1
        
        if (tebakan > rahasia):

            print("Tebakan terlalu besar!")
            return 1
        
        if (tebakan == rahasia ):

            print("Tebakan Tepat!")
            return 0
            
        

angka_rahasia = 40

tebakan_a = int(input("Masukkan tebakan anda: "))

while True:

    hasil = cek_tebakan(tebakan_a, angka_rahasia)

    if hasil != 0:
          
        tebakan_a = int(input("Jawaban salah!, coba lagi: "))
        
    else:
        break
