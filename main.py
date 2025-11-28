from data import barang

keranjang = []

def daftar():
    print("============ DAFTAR MENU ============")
    print("KODE       NAMA            HARGA")
    print("=====================================")
    for kode, item in barang.items():
        print(f"{kode:<10} {item['nama']:<15} {item['harga']}")
    print("=====================================")
            
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
    print("DISKON : Rp",+int(dis))
    print("TOTAL BELANJA : Rp",+int(sub))
    print("TOTAL BAYAR : Rp",+int(totalB))
    print("=====================================")
    
    keranjang.clear()
    
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
