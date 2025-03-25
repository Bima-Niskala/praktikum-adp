r = 0
c = 0
while r < 4 or c < 4:
    r = int(input("Masukkan jumlah baris kursi: "))
    c = int(input("Masukkan jumlah kolom kursi: "))
    if r < 4 or c < 4:
        print("Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.")

nomor_kursi = 1
for i in range(r):
    for j in range(c):
        print(f"{nomor_kursi:2}", end=" ")
        nomor_kursi += 1
    print()

while True:
    Pilihan = int(input("\nMasukkan nomor kursi yang ingin dipilih (0 untuk selesai): "))
    if Pilihan == 0:
        print("\nTerima kasih telah menggunakan layanan pemesanan tiket bioskop.")
        break
    if Pilihan < 1 or Pilihan > r * c:
        print("Nomor kursi tidak valid. Silakan coba lagi.")
        continue
    
    nomor_kursi = 1
    for i in range(r):
        for j in range(c):
            if nomor_kursi == Pilihan:
                print(" X", end=" ")
            else:
                print(f"{nomor_kursi:2}", end=" ")
            nomor_kursi += 1
        print()
