print("Hallo saya akan mengecek umur kamu")

lahir = int(input("Tahun berapa anda lahir: "))
tahun_sekarang = int(input("Tahun berapa sekarang: "))

cek = tahun_sekarang-lahir

if(lahir > 2020):
    print("Kamu bohong, tidak bisa")
elif(tahun_sekarang != 2020):
    print("Kamu bohong kan, sekarang tahun 2020")
else:
    print("Jadi umur kamu sekarang adalah: " + str(cek) + " tahun")
