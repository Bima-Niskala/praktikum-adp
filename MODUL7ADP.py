def input_data():
    mahasiswa = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        nilai_akhir = 0
        peringkat = 0
        mahasiswa.append([nama, nim, uts, uas, tugas, nilai_akhir, peringkat])
    return mahasiswa

def hitung_nilai_akhir(mahasiswa):
    for m in mahasiswa:
        m[5] = 0.35 * m[3] + 0.35 * m[2] + 0.30 * m[4] 

def hitung_rata_rata(mahasiswa, indeks):
    total = 0
    jumlah = len(mahasiswa)
    for m in mahasiswa:
        total += m[indeks]
    return total / jumlah if jumlah > 0 else 0

def urutkan_mahasiswa(mahasiswa):
    n = len(mahasiswa)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if mahasiswa[j][5] < mahasiswa[j+1][5]: 
                mahasiswa[j], mahasiswa[j+1] = mahasiswa[j+1], mahasiswa[j]

def tentukan_peringkat(mahasiswa):
    for i in range(len(mahasiswa)):
        mahasiswa[i][6] = i + 1  

def tampilkan_tabel(mahasiswa):
    print("\n" + "-"*80)
    print("\n{:<10} {:<10} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
        'Nama', 'NIM', 'UTS', 'UAS', 'Tugas', 'Nilai Akhir', 'Peringkat'))
    for m in mahasiswa:
        print("\n" + "-"*80)
        print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<12.2f} {:<10}".format(
            m[0], m[1], m[2], m[3], m[4], m[5], m[6]))
    
    rata_uts = hitung_rata_rata(mahasiswa, 2)
    rata_uas = hitung_rata_rata(mahasiswa, 3)
    rata_tugas = hitung_rata_rata(mahasiswa, 4)
    rata_nilai_akhir = hitung_rata_rata(mahasiswa, 5)
    print("\n" + "-"*80)
    print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<12.2f}".format(
        'Rata-rata', '-', rata_uts, rata_uas, rata_tugas, rata_nilai_akhir))
    print("-"*80)
data_mahasiswa = input_data()
hitung_nilai_akhir(data_mahasiswa)
urutkan_mahasiswa(data_mahasiswa)
tentukan_peringkat(data_mahasiswa)
tampilkan_tabel(data_mahasiswa)