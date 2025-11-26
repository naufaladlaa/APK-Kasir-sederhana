from data import barang

keranjang = []

def daftar():
    print("============ DAFTAR MENU ============")
    print("KODE       NAMA            HARGA")
    print("=====================================")
    for kode, item in barang.items():
        print(f"{kode:<10} {item['nama']:<15} {item['harga']}")
    print("=====================================")
    
def menu_utama():
    while True:
        print("======== APK KASIR SEDERHANA ========")
        print("1. START")
        print("2. EXIT")
        
        pilihan = input("Masukan Perintah : ")
        
        if pilihan == "1":
            print("\nMemulai Program......\n")
            break
        elif pilihan == "2":
            print("\nTerima Kasih :D")
            exit()
        else:
            print("Pilihan tidak valid !!")
            
def tambah(kode, qty=1):
    if kode not in barang:
        daftar()
        print("Kode tidak ada !!")
    
    if kode in barang:
        keranjang.append({
            "kode":kode,
            "nama":barang[kode]['nama'],
            "harga":barang[kode]['harga'],
            "qty":qty
        })
        return True
    
def cek():
    if not keranjang:
        print("Keranjang Anda masih kosong !!")
        return
    print("============ ISI KERANJANG ============")
    for i,item in enumerate(keranjang, start=1):
        sub = item["harga"] * item["qty"]
        print(f"{i}. {item['nama']:<10} X {item['qty']} = {sub}")
    print()
    
def cekout():
    if not keranjang:
        print("Keranjang Anda masih kosong")
        return
    
    print("============ STRUK BELANJA ============")
    total = 0
    
    for item in keranjang:
        qty = item["qty"]
        
        sub = item["harga"] * qty        
        total += sub
        print(f"{item['nama']} X {qty} = {sub}")
    
    totalB = 0
    if sub > 75000:
        dis = (15 / 100) * sub
        totalB = sub - dis
    
    print("=====================================")  
    print("DISKON : Rp"+int(dis))
    print("TOTAL BELANJA : Rp"+int(sub))
    print("TOTAL BAYAR : Rp"+int(totalB))
    print("=====================================")
    
def edit(nama, qtyb):
    for item in keranjang:
        if item["nama"] == nama:
            if qtyb > 0:
                item["qty"] = qtyb
                return True
            elif qtyb == 0:
                keranjang.remove(item)
                return True
            else:
                return False
        print("Barang tidak ditemukan !!")
        return False
    
menu_utama()
    
while True:
    print("============ ANAK BUAH KAPAL ============")
    print("=========================================")
    print("1. DAFTAR BARANG")
    print("2. TAMBAH BARANG")
    print("3. CEK KERANJANG")
    print("4. EDIT KERANJANG")
    print("5. CHECKOUT")
    print("6. EXIT")
    
    pilihan = input("Masukan Perintah : ")
    
    if pilihan == "1":
        daftar()
    elif pilihan == "2":
        daftar()
        kode = input("Masukan Kode : ")
        qty = int(input("Masukan jumlah barang : "))
        tambah(kode, qty)
    elif pilihan == "3":
        cek()
    elif pilihan  == "4":
        cek()
        nama = input("nama barang : ").strip().upper()
        qtyb = int(input("Masukan Jumlah barang : "))
        edit(nama, qtyb)
    elif pilihan == "5":
        cekout()
    elif pilihan == "6":
        print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM !!")
        break
    
    input("\nTekan ENTER untuk kembali ke menu utama......")
