print("====================")
print("===A-Teks_Editor====")
print("====================")

ketik = input("Ketikkan: ")

teks = ketik.format(ketik)

judulFile = input("Judul: ")

namaFile = open(judulFile + ".txt", "w")

# konversi teks ke file
namaFile.write(teks)

# tutup file
namaFile.close()
