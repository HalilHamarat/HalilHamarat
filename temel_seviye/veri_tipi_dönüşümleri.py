# #KULLANICIDAN 2 SAYI ALIP TOPLAMA İŞLEMİ YAPAN PROGRAM

# sayi1 = float(input("1. sayıyı giriniz"))
# sayi2 = float(input("2. sayıyı giriniz"))
# print(sayi1+sayi2)
# print( type(sayi1+sayi2) )

x = 1.0
#İnt
y = 1.2
#Float
ad = "Eren"
#String
sinav_basarili_mi = True
#boolean (bool)

print(x+y)
#print(x+ad)
#hata verdi (int ile str birleştirilemez)
print(x+sinav_basarili_mi)

print(type(x))
print(type(y))
print(type(ad))
print(type(sinav_basarili_mi))

#Float'tan int'e
print(int(y))
print(int(x))

#booldan str'ye
print(sinav_basarili_mi)
print(str(sinav_basarili_mi))

#bool'dan int'e
print(int(sinav_basarili_mi))

#int'teen str'ye
print(str(x)) #str olarak 1

#str'den int'e
print(ad)
#print(int(ad)) #metin int'e dönüşmez!
h = "36"
print(int(h))