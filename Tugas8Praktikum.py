data_buku = [
    "9786020321234,Python untuk Pemula,Andi Hermawan,10,50000,75000",
    "9789792223331,Logika Matematika,Budi Santosa,4,60000,85000",
    "9786021531456,Algoritma dan Pemrograman,Clara Tania,3,70000,95000",
    "9789791234567,Bahasa Indonesia SMA,Dian Wahyuni,7,40000,60000",
    "9786021933210,Sejarah Dunia,Kiki Amelia,2,65000,80000",
    "9789795678901,Belajar Excel Cepat,Rizal Fauzi,6,30000,50000",
    "9786026543210,Kalkulus Dasar,Teguh Wijaya,12,75000,100000",
    "9786027894561,Fisika Modern,Ahmad Zaki,5,85000,120000",
    "9789798889991,Bisnis Online Praktis,Maya Sari,3,45000,70000",
    "9786021112233,Kimia Organik,Rina Kusuma,1,80000,110000"
]

with open("inventaris_buku.txt", "w") as file:
    for baris in data_buku:
        file.write(baris + "\n")

list_buku=[]

with open("inventaris_buku.txt","r") as file:
    for line in file:
        isbn, judul, penulis, stok, harga_beli, harga_jual = line.strip().split(",")
        buku = {
            "ISBN": isbn,
            "Judul": judul,
            "Penulis": penulis,
            "Stok": int(stok),
            "Harga Beli": int(harga_beli),
            "Harga Jual": int(harga_jual)
        }
    list_buku.append(buku)

with open("laporan_inventaris.txt", "w") as file:
    file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
    for buku in list_buku:
        potensi_keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
        buku["Potensi Keuntungan"] = potensi_keuntungan
        baris = f'{buku["ISBN"]},{buku["Judul"]},{buku["Penulis"]},{buku["Stok"]},{buku["Harga Beli"]},{buku["Harga Jual"]},{potensi_keuntungan}\n'
        file.write(baris)

potensi_tertinggi = list_buku[0]
potensi_terendah = list_buku[0]

for buku in list_buku:
    if buku["Potensi Keuntungan"] > potensi_tertinggi["Potensi Keuntungan"]:
        potensi_tertinggi = buku
    if buku["Potensi Keuntungan"] < potensi_terendah["Potensi Keuntungan"]:
        potensi_terendah = buku

total_nilai_inventaris = 0
for buku in list_buku:
    total_nilai_inventaris += buku["Stok"] * buku["Harga Beli"]

buku_rendah_stok = []
for buku in list_buku:
    if buku["Stok"] < 5:
        buku_rendah_stok.append(buku)

print(" Buku dengan Potensi Keuntungan Tertinggi:")
print("Judul:", potensi_tertinggi["Judul"])
print("Potensi Keuntungan: Rp", potensi_tertinggi["Potensi Keuntungan"])

print("\n Buku dengan Potensi Keuntungan Terendah:")
print("Judul:", potensi_terendah["Judul"])
print("Potensi Keuntungan: Rp", potensi_terendah["Potensi Keuntungan"])

print("\n Total Nilai Inventaris (berdasarkan Harga Beli): Rp", total_nilai_inventaris)

print("\n Daftar Buku yang Stoknya Kurang dari 5 (Perlu Restock):")
for buku in buku_rendah_stok:
    print(f'Judul: {buku["Judul"]}, Stok: {buku["Stok"]}')