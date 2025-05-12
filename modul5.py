mahasiswa = []
nilai = []
n = int(input("Masukkan jumlah mahasiswa: "))
for i in range(n):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    pre = float(input("Nilai Pretest: "))
    post = float(input("Nilai Posttest: "))
    makalah = float(input("Nilai Makalah: "))
                    
    nilai_akhir = (pre * 0.4) + (post * 0.4) + (makalah * 0.2)
    mahasiswa.append({
        "nama": nama,
        "nilai_akhir": nilai_akhir
    })
    nilai.append(nilai_akhir)

print("="*40)
print("No | Nama Mahasiswa     | Nilai Akhir")
print("-"*40)
i = 0
while i < len(mahasiswa):
    print(f"{i+1:2} | {mahasiswa[i]['nama']:<18} | {mahasiswa[i]['nilai_akhir']:.2f}")
    i += 1
print("="*40)

total = 0
for i in range(len(nilai)):
    total += nilai[i]
rata_rata = total / len(nilai)
print(f"Rata-rata Nilai Akhir Kelas: {rata_rata:.2f}")

nilai_tertinggi = nilai[0]
nilai_terendah = nilai[0]
for i in range(1, len(nilai)):
    if nilai[i] > nilai_tertinggi:
        nilai_tertinggi = nilai[i]
    if nilai[i] < nilai_terendah:
        nilai_terendah = nilai[i]

print("\nMahasiswa dengan Nilai Tertinggi:")
for i in range(len(mahasiswa)):
    if mahasiswa[i]["nilai_akhir"] == nilai_tertinggi:
        print(f"{mahasiswa[i]['nama']} ({nilai_tertinggi:.2f})")
print("\nMahasiswa dengan Nilai Terendah:")
for i in range(len(mahasiswa)):
    if mahasiswa[i]["nilai_akhir"] == nilai_terendah:
        print(f"{mahasiswa[i]['nama']} ({nilai_terendah:.2f})")
print("\nMahasiswa dengan Nilai di Atas Rata-rata:")
for i in range(len(mahasiswa)):
    if mahasiswa[i]["nilai_akhir"] > rata_rata:
        print(f"{mahasiswa[i]['nama']} ({mahasiswa[i]['nilai_akhir']:.2f})")