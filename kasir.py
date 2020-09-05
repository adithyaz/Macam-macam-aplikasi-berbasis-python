password = input("Masukkan password: ")

if(password != "adit"):
    print("Password salah")
else:
    print("Aplikasi Kasir")
    print("==============\n")

    namaBarang = input("Masukkan nama barang: ")
    hargaBarang = int(input("Masukkan harga barang: "))
    kuantitas = int(input("Masukkan berapa barang yang dibeli: "))
    total = kuantitas*hargaBarang

    print("Nama Barang: ", namaBarang)
    print("Harga", namaBarang, ": " + str(hargaBarang), " x ", kuantitas)
    print("Total yang dibayar: " + str(total))
