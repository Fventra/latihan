sum_barang = int(input("Jumlah barang? "))
things = []
count1 = 0
while count1  != sum_barang:
    nama_barang = str(input("Nama Barang? "))
    jumlah = int(input("Jumlah? "))
    detail_barang = (nama_barang, jumlah)
    things.append(detail_barang)
    count1 += 1

def lihat_stok():
    count2 = 0
    for _ in things:
        nama, jumlah = things[count2]
        print(f'{nama} ada {jumlah} pcs')
        

def kurangi_stok():
    who = input("Mau yang mana? ")
    nilai_kurang = int(input("Kurang Berapa? "))
    for i, data in enumerate(things):
        for tuple in data:
            if tuple == who:
                things[i] = (things[i][0], things[i][1]-nilai_kurang)

def tambah_stok():
    who = input("Mau yang mana? ")
    nilai_tambah = int(input("Nambah Berapa? "))
    for i, data in enumerate(things):
        for tuple in data:
            if tuple == who:
                things[i] = (things[i][0], things[i][1]+nilai_tambah)
def cek_stok():
    for i, jumlah_stok in enumerate(things):
        print(f'stok barang {things[i][0]} adalah {things[i][1]}')
        if things[i][1] < 5:
            print(f'stok barang {things[i][0]} hampir habis')




def main():

    while True:
        print('''
        =======================================
        Selamat datang di pengelola stok barang
        =======================================
        silahkan pilih menu dibawah ini
        1.  Lihat Stok
        2.  Tambah Stok
        3.  Kurangi Stok
        4.  Keluar
        =======================================
        ''')
        menu = int(input("Ingin pilih apa: "))
        if menu == 1:
            lihat_stok()
        elif menu == 2:
            tambah_stok()
            lihat_stok()
        elif menu == 3:
            kurangi_stok()
            lihat_stok()
        else:
            break

main()