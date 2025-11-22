from data import barang

keranjang = []

def daftar():
    print("===== DAFTAR NAMA BARANG =====")
    for nama, harga in barang.items():
        print(f" - {nama:<12} = {harga}")

def tambah(nama, qty =1):
    if nama in barang:
        keranjang.append({
            "nama": nama,
            "harga": barang[nama],
            "jumlah barang": qty
        })
        return True
    return False

def inputB():
    while True:
        nama = input("Masukan nama barang : ")
        
        if nama in barang:
            return nama
        else:
            print("Barang tidak ada atau salah ketik !!")
            daftar()
            print()
            
def cek():
    if not keranjang:
        print("Keranjang anda masih kosong !!")
    else :
        print("===== ISI KERANJANG =====")
        for i, item in enumerate(keranjang, start=1):
            nama = item["nama"]
            harga = item["harga"]
            qty = item["jumlah barang"]
            sub = harga * qty
            
            print(f"{i}. {nama:<10}X {qty} = {sub} ")
            
def edit(nama, qtyb):        
    for item in keranjang:
        if item["nama"] == nama:
            if qtyb > 0:
                item["jumlah barang"] = qtyb
                return True
            elif qtyb == 0:
                keranjang.remove(item)
                return True
            else:
                return False
        print("Barang tidak ditemukan !!")
        return False

def hapus(nama):
    for item in keranjang:
        if item["nama"] == nama:
            keranjang.remove(item)
            print(f"{nama} berhasil dihapus")
            return True
    
    print("Nama barang tidak ditemukan !!")
    return False

def cekout():
    if not keranjang:
        print("Keranjang anda masih kosong !!")
        return
    
    print("===== STRUK BELANJA =====")
    sub = 0
    for i, item in enumerate(keranjang, start=1):
        nama = item["nama"]
        harga = item["harga"]
        qty = item["jumlah barang"]
        total = harga * qty
        sub += total
        
        print(f"{i}. {nama:<10} {harga} X {qty} = {total}")
        
    totalb = 0
    if sub > 50000:
        dis = (10 / 100) * sub
        totalb = sub - dis
        
    print("==========================================")
    print("DISKON : Rp",+int(dis))
    print(f"TOTAL BELANJA : Rp.{sub}")
    print("TOTAL BAYAR : Rp.",+int(totalb))
    print("==========================================")
    keranjang.clear()
    
def menu():
    while True:
        print("==================================")
        print("========= APK KASIR v.10 =========")
        print("==================================")
        
        print("1. START")
        print("2. EXIT")
        
        pilihan = input("Pilih perintah : ")
        
        if pilihan == "1":
            print("\nMemulai Program....\n")
            break
        elif pilihan == "2":
            print("\nTerima kasih\n")
            exit()
        else:
            print("\nPilihan tidak valid !! \n")
menu()

while True:
    print("===================================")
    print("========= ANAK BUAH KAPAL =========")
    print("===================================")
    print("1. TAMBAH BARANG")
    print("2. EDIT KERANJANG")
    print("3. CHECKOUT")
    print("4. KELUAR")
    
    pilihan = input("Pilih menu : ")
    
    if pilihan == "1":
        daftar()
        nama = inputB()
        qty = int(input("Masukan jumlah barang : "))
        tambah(nama, qty)
    elif pilihan == "2":
        cek()
        nama = input("Masukan nama barang : ")
        qty = int(input("Masukan jumlah barang : "))
        print(f"{nama} telah di edit")
        edit(nama, qty)
    elif pilihan == "3":
        cekout()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program !! :D")
        break
    else : 
        print("Pilihan tidak valid !! ")

    input("\ntekan ENTER untuk kembali ke menu utama ....")