from main import daftar,tambah,cek,cekout,edit

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