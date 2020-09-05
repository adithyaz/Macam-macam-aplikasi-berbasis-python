# Penjumlahan
def tambah(a, b):
    return a + b

# Pengurangan


def kurang(a, b):
    return a - b

# Perkalian


def kali(a, b):
    return a * b

# Pembagian


def bagi(a, b):
    return a / b

# Menu


print("Pilih Operasi")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Pilih operasi matematika: ")

angka1 = int(input("Masukkan bilangan pertama: "))
angka2 = int(input("Masukkan bilangan kedua: "))

if(pilihan == '1'):
    print("Hasil dari ", angka1, " + ", angka2, " = ", tambah(angka1, angka2))

elif(pilihan == '2'):
    print("Hasil dari ", angka1, " - ", angka2, " = ", kurang(angka1, angka2))

elif(pilihan == '3'):
    print("Hasil dari ", angka1, " x ", angka2, " = ", kali(angka1, angka2))

elif(pilihan == '4'):
    print("Hasil dari ", angka1, " : ", angka2, " = ", bagi(angka1, angka2))

else:
    print("Kamu mengetik option yang salah")
