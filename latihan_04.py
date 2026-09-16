# ============================================================
# LATIHAN 04
# Studi Kasus: Kasir dengan Diskon Bertingkat
# ============================================================
#
# Deskripsi Masalah:
# Sebuah toko memberikan diskon berdasarkan total belanja.
#
# Spesifikasi Program:
#
# Input:
# - Jumlah jenis barang
# - Harga dan jumlah setiap barang
#
# Proses:
# 1. Gunakan looping untuk memasukkan setiap barang.
# 2. Hitung subtotal setiap barang.
# 3. Hitung total belanja.
#
# Diskon:
# - total >= Rp1.000.000 -> diskon 15%
# - total >= Rp500.000  -> diskon 10%
# - total >= Rp250.000  -> diskon 5%
# - selain itu          -> tidak ada diskon
#
# Buat fungsi:
# hitung_diskon(total) -> persentase diskon
#
# Gunakan conditional untuk menentukan diskon.
#
# Output:
# - Total sebelum diskon
# - Persentase diskon
# - Nominal diskon
# - Total yang harus dibayar
#
# KAMUS:
# n, i : int
# harga, jumlah : float
# subtotal, total, diskon, total_bayar : float
# persen_diskon : float
#
# FUNGSI:
# hitung_diskon(total) -> float
#
# ============================================================

# Tulis kode Python kamu di bawah ini

jumlah_jenis = float(input("Anda beli berapa jenis barang? "))
total = 0
def harga_total(harga, jumlah):
    total = harga * jumlah
    return total
def hitung_diskon(total_harga):
    if total_harga >= 250.0:
        return 0.85
    elif total_harga >= 500.0:
        return 0.90
    elif total_harga >= 1000.0:
        return 0.95
    else:
        return 1
while True:
    harga = float(input("Harga barang: "))
    jumlah = int(input("jumlahnya? "))
    total += harga_total(harga, jumlah)
    jumlah_jenis -= 1
    if jumlah_jenis == 0:
        diskon = hitung_diskon(total)
        harga_diskon = total * diskon
        print(f'Harga yang harus dibayarkan adalah: {harga_diskon}')
        break
    else:
        continue

    
    