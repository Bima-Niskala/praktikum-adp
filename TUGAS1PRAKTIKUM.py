#Input Data Diri
nama = input("Nama : ")
umur = int(input("Umur : "))
jenis_kelamin  = input("Jenis Kelamin : ")


print("--------KODE DAN TUJUAN MASKAPAI--------")
print("3012 = Padang - Jakarta")
print("4015 = Padang - Batam")
print("4050 = Padang - Bandung")
kode = int(input("Masukan kode Maskapai : "))

if kode == 3012:
    rute = "Padang - Jakarta"
elif kode == 4015:
    rute = "Padang - Batam"
else:
    rute = "Padang - Bandung"

jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))

if kode == 3012:
    print("Pilih kelas Maskapai:")
    print("1. Ekonomi (Rp 800.000)")
    print("2. Bisnis (Rp 850.000)")
    print("3. First Class (Rp 900.000)")
    harga_ekonomi = 800000
    harga_bisnis = 850000
    harga_first_class = 900000
elif kode == 4015:
    print("Pilih kelas Maskapai:")
    print("1. Ekonomi (Rp 500.000)")
    print("2. Bisnis (Rp 550.000)")
    print("3. First Class (Rp 700.000)")
    harga_ekonomi = 500000
    harga_bisnis = 550000
    harga_first_class = 700000
elif kode == 4050:
    print("Pilih kelas Maskapai:")
    print("1. Ekonomi (Rp 700.000)")
    print("2. Bisnis (Rp 750.000)")
    print("3. First Class (Rp 850.000)")
    harga_ekonomi = 700000
    harga_bisnis = 750000
    harga_first_class = 850000
else:
    print()

pilihan_kelas = input("Masukkan pilihan kelas (ekonomi/bisnis/first class): ")

if pilihan_kelas == "ekonomi":
    harga_per_tiket = harga_ekonomi
elif pilihan_kelas == "bisnis":
    harga_per_tiket = harga_bisnis
elif pilihan_kelas == "first class":
    harga_per_tiket = harga_first_class
else:
    print("Kelas tidak valid.")

total_harga = harga_per_tiket * jumlah_tiket
if jumlah_tiket > 3:
    diskon = total_harga * 0.2
    total_harga = diskon
    print("Diskon 20% diberikan karena membeli lebih dari 3 tiket.")
else:
    diskon = 0

print("==================== STRUK PEMESANAN TIKET ====================")
print("Nama            :", nama)
print("Umur          :", umur, "tahun")
print("Jenis Kelamin   :", jenis_kelamin)
print("---------------------------------------------------------------")
print("Rute            :", rute)
print("Jumlah Tiket    :", jumlah_tiket, "tiket")
print("Kelas Pesawat   :", pilihan_kelas)
print("Harga per Tiket :", "Rp", format(harga_per_tiket, ','))
if diskon > 0:
    print("Diskon 20%      :", "Rp", format(diskon, ','))
print("Total Harga     :", "Rp", format(total_harga, ','))
print("===============================================================")
