print("=====Tebak Angka BOM!!!=====")

print("Pemain 1")
n = int(input("Masukan Batas Angkanya ? : "))
b = int(input("Angka BOMNYA apa : "))

for i in range(1, n+1):
    if i % b == 0:
        print("BOM!!!")
    else:
        print(i)
print()

print("Pemain 2")
print("===============")
tebakan_angka = 0
while tebakan_angka < 1 or  tebakan_angka > n:
    tebakan_angka = int(input(f"Tebak Angka dari 1 sampai {n} : "))
    if tebakan_angka < 1 or  tebakan_angka > n :
        print(f"Tebakan angka hanya 1 sampai {n} ulangi")

if tebakan_angka % b == 0:
    print(f"Angka {tebakan_angka} BOM!!! KAMU KALAH")
else :
    print("SELAMAT KAMU MENANG, YEY SELAMAAT :)")

print("=====Permain Selesai=====")