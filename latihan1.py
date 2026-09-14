#soal ini akan dibuat oleh gemini
'''
Studi Kasus: Kalkulator Biaya Pengecatan Dinding
Deskripsi Masalah:
Seorang tukang cat bernama Pak Budi diminta untuk mengecat dinding sebuah ruangan. Ruangan tersebut berbentuk persegi panjang. Untuk menghitung estimasi biaya dan kebutuhan cat, Pak Budi perlu mengetahui total luas dinding yang akan dicat dan berapa liter cat yang dibutuhkan.

Terdapat jendela dan pintu di ruangan tersebut yang tentunya tidak akan dicat.

Spesifikasi Program:
Buatlah sebuah program Python (HitungBiayaCat) yang melakukan hal-hal berikut secara berurutan:

Input Data (Menerima masukan dari pengguna):

Minta pengguna memasukkan panjang ruangan (dalam meter, bisa berupa desimal).

Minta pengguna memasukkan lebar ruangan (dalam meter, bisa berupa desimal).

Minta pengguna memasukkan tinggi ruangan (dalam meter, bisa berupa desimal).

Minta pengguna memasukkan total luas pintu dan jendela (dalam meter persegi, bisa berupa desimal) yang tidak akan dicat.

Minta pengguna memasukkan harga cat per liter (dalam Rupiah, bilangan bulat).

Minta pengguna memasukkan nama pelanggan (berupa teks).

(Informasi Tambahan: Asumsikan 1 liter cat dapat menutupi 5 meter persegi dinding).

Proses (Melakukan perhitungan secara sekuensial):

Hitung total luas seluruh permukaan 4 dinding ruangan (tanpa memperhitungkan pintu/jendela terlebih dahulu).
Rumus Luas 4 Dinding = 2 * (Panjang * Tinggi) + 2 * (Lebar * Tinggi) atau Keliling Ruangan * Tinggi.

Hitung luas dinding bersih yang sebenarnya akan dicat.
Rumus Luas Bersih = Total Luas 4 Dinding - Total Luas Pintu/Jendela.

Hitung estimasi kebutuhan cat (dalam liter). Karena jumlah cat tidak mungkin pecahan dalam membelinya, tapi untuk kasus ini biarkan saja dalam bentuk desimal (kebutuhan riil).
Rumus Kebutuhan Cat = Luas Bersih / 5.

Hitung total estimasi biaya cat.
Rumus Total Biaya = Kebutuhan Cat * Harga Cat per Liter.

(Ekspresi Logika/Relasional): Pak Budi memberikan diskon khusus jika total luas yang dicat lebih besar dari 50 meter persegi. Buat sebuah variabel boolean (dapat_diskon) yang bernilai True jika luas bersih > 50, dan False jika sebaliknya. (Tidak perlu menghitung nominal diskon, cukup statusnya saja).

Output (Menampilkan hasil ke layar):

Cetak kalimat sapaan: "Halo, [Nama Pelanggan]!"

Cetak "Estimasi Luas Dinding yang Dicat: [Luas Bersih] meter persegi".

Cetak "Estimasi Kebutuhan Cat: [Kebutuhan Cat] liter".

Cetak "Total Biasi Cat: Rp [Total Biaya]".

Cetak "Status Diskon (Luas > 50 m2): [dapat_diskon]".
'''
# Kamus
'''
panjang, lebar, tinggi, luas_pintu, luas_jendela, luas_awal, luas_akhir, harga_cat,
'''



# Algoritma

panjang = int(input("Panjang ruangan: "))
lebar = int(input("Lebar ruangan: "))
tinggi = int(input("Tinggi ruangan: "))
luas_pintu = int(input("Luas pintu: "))
luas_jendela = int(input("Luas jendela: "))
harga_cat = int(input("Harga cat per liter: "))
nama = str(input("Nama anda: "))
cat = 0
luas_cat = cat * 5

luas_awal = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
luas_akhir = luas_awal - luas_jendela - luas_pintu
cat = luas_akhir / 5
biaya = cat * harga_cat
dapat_diskon = False
if luas_akhir >= 50:
    dapat_diskon = True
else:
    dapat_diskon = False

sapaan = "Hallo, " + str(nama)
print(sapaan)
print("Estimasi luas dinding yang akan dicat adalah " + str(luas_akhir) + " meter")
print("Estimasi kebutuhan cat adalah: " + str(cat) + " kaleng")
print("Total biaya adalah: " + str(biaya) + " rupiah")
print("status diskon: " + str(dapat_diskon))