print("Masukkan ukuran matriks A")
barisA = int(input("Jumlah baris: "))
kolomA = int(input("Jumlah kolom: "))
A = []
print("Masukkan elemen matriks A:")
for i in range(barisA):
    baris = []
    for j in range(kolomA):
        elemen = float(input("Elemen baris " + str(i+1) + " kolom " + str(j+1) + ": "))
        baris.append(elemen)
    A.append(baris)

print("Masukkan ukuran matriks B")
barisB = int(input("Jumlah baris: "))
kolomB = int(input("Jumlah kolom: "))
B = []
print("Masukkan elemen matriks B:")
for i in range(barisB):
    baris = []
    for j in range(kolomB):
        elemen = float(input("Elemen baris " + str(i+1) + " kolom " + str(j+1) + ": "))
        baris.append(elemen)
    B.append(baris)

ulang = "y"
while ulang == "y":
    print("\nMenu Kalkulator:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Determinan")
    print("5. Invers")
    print("6. Transpose")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        if barisA == barisB and kolomA == kolomB:
            print("Hasil penjumlahan:")
            for i in range(barisA):
                hasil = []
                for j in range(kolomA):
                    hasil.append(A[i][j] + B[i][j])
                print(hasil)
        else:
            print("Ukuran matriks tidak sama.")

    elif pilihan == "2":
        if barisA == barisB and kolomA == kolomB:
            print("Hasil pengurangan:")
            for i in range(barisA):
                hasil = []
                for j in range(kolomA):
                    hasil.append(A[i][j] - B[i][j])
                print(hasil)
        else:
            print("Ukuran matriks tidak sama.")

    elif pilihan == "3":
        if kolomA == barisB:
            print("Hasil perkalian:")
            for i in range(barisA):
                hasil = []
                for j in range(kolomB):
                    total = 0
                    for k in range(kolomA):
                        total = total + A[i][k] * B[k][j]
                    hasil.append(total)
                print(hasil)
        else:
            print("Jumlah kolom A harus sama dengan jumlah baris B.")

    elif pilihan == "4":
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            print("Determinan matriks A:", detA)
        else:
            print("Matriks A bukan 2x2, tidak bisa dihitung.")
        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            print("Determinan matriks B:", detB)

    elif pilihan == "5":
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            if detA != 0:
                print("Invers matriks A:")
                print([ [ A[1][1]/detA, -A[0][1]/detA ],
                        [ -A[1][0]/detA, A[0][0]/detA ] ])
            else:
                print("Matriks A tidak punya invers (determinan = 0)")
        else:
            print("Matriks A bukan 2x2")

        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            if detB != 0:
                print("Invers matriks B:")
                print([ [ B[1][1]/detB, -B[0][1]/detB ],
                        [ -B[1][0]/detB, B[0][0]/detB ] ])
            else:
                print("Matriks B tidak punya invers (determinan = 0)")
        else:
            print("Matriks B bukan 2x2")

    elif pilihan == "6":
        print("Transpose matriks A:")
        for j in range(kolomA):
            baris = []
            for i in range(barisA):
                baris.append(A[i][j])
            print(baris)

        print("Transpose matriks B:")
        for j in range(kolomB):
            baris = []
            for i in range(barisB):
                baris.append(B[i][j])
            print(baris)
    else:
        print("Pilihan tidak valid.")

    ulang = input("Ingin menghitung lagi? (y/n): ")
print("Terima kasih telah menggunakan kalkulator matriks.")