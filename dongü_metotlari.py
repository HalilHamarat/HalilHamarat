#METOT: range()
#range() fonksiyonunu belli bir aralıkta bulunan sayıları döndürmek için kullanırız
"""
liste = list(range(1, 10))
print(liste)

# ekrana 50 defa Python yazdıralım

for sayi in range(1, 51):
        print(f"{sayi}. Python")
"""
# Metot: enumerate
#İngilizcede enumerate kelimesi "numaralandırmak" anlamına gelir.
# fonksiyonun görevi nes
# ne elemanlarını numaralandırarak döndürmek

# python kelimesinin karakterlerini enumerate ile numaralandırıp ekrana yazalım
kelime = "python"
kelime_enum = enumerate(kelime)
print(kelime_enum)

for index, harf in enumerate(kelime):
    print(index, harf)

#Metot: zip()
#zip listeleri birleştirme işlemi yapar
sayilar = [1, 2, 3]
okunuslar = ["bir", "iki", "üç"]

sayilar_zip = list(zip(sayilar, okunuslar))
print(sayilar_zip)

for sayi, okunus in zip(sayilar, okunuslar):
    print(sayi, okunus)