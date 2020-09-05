uang_kamu = int(input("Uang kamu berapa: "))

utang = 20000

if uang_kamu < utang:
    print("uang kamu tidak cukup!")
elif uang_kamu > 20000:
    print("Uang kamu kelebihan, saya akan mengembalikan", uang_kamu - utang)
elif uang_kamu == utang:
    print("ok utang kamu sudah lunas, thanks")
else:
    print("Wah parah, kamu ga bayar utang")
