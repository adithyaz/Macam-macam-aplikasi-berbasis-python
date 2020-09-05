print("Aplikasi Kalkulator Plus-Plus\n")


# Luas Persegi


def luasPersegi(s):
    return s * s

# Volume Balok


def volumeBalok(p, lu, t):
    return p*lu*t

# Luas Segitiga


def luasSegitiga(a, t):
    return a*t


def luasLingkaran(r):
    phi = 3.14
    return phi*r*r


option = ["1. Luas Persegi", "2. Volume Balok",
          "3. Luas Segitiga", "4. Luas Lingkaran"]
for mtk in option:
    print(mtk)

optional = input("Option berapa yang ingin anda pilih: ")

if optional == "1":
    sisi = int(input("Masukkan nilai sisi: "))
    print("Hasilnya adalah: ", luasPersegi(sisi))
elif optional == "2":
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    print("Hasilnya adalah: ", volumeBalok(panjang, lebar, tinggi))
elif optional == "3":
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    print("Hasilnya adalah", luasSegitiga(alas, tinggi))
elif optional == "4":
    jari_jari = int(input("Masukkan nilai jari-jari: "))
    print("Hasilnya adalah", luasLingkaran(jari_jari))
else:
    print("Kamu tidak memasukkan option")
