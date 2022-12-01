# 1- "Türkçe, Hayat Bilgisi, Matematik, Fen Bilimleri" elemanlarından oluşan liste oluşturalım
list = ["Türkçe" , "Hayat Bilgisi" , "Matematik" , "Fen Bilimleri"]

# 2- "Hayat Bilgisi" değerini "Sosyal Bilgiler" değeri ile değiştirelim
list.pop(1)
list.insert(1 , "Sosyal Bilgiler")
print(list)
# 3- "Coğrafya" listenin bir elemanı mıdır?


# 4- Listenin son 2 elemanı yerine "Görsel Sanatlar" ve "Müzik" değerlerini ekleyelim
list.pop(-1)
list.pop(-1)
print(list)
list.insert(-1, "Müzik")
list.insert(-1, "Görsel Sanatlar")
# 5- Listenin üzerine "Serbest Etkinlik" ve "Beden Eğitimi ve Oyun" değerlerini ekleyelim
list.append("Serbest Etkinlik")
list.append("Beden Eğitimi ve Oyun")
# 6- Listenin son elemanını silelim
list.pop()
# 7- Liste elemanlarını ters çevirelim
list.reverse()
print(list)
# 8- Liste elemanlarını alfabetik olarak sıralayalım
list.sort()
print(list)
# 9- 3 öğrenci için öğrenci no anahtarı ile ad, soyad, cinsiyet, yaş bilgilerinden oluşan bir dictionary oluşturalım
students = {
    13: {
        "Ad" : "Halil",
        "Soyad" : "Hamarat",
        "Cinsiyet" : True,
        "Yas" : "14"
    },
    45: {
        "Ad ": "İsmail",
        "Soyad" : "Yılmaz",
        "Cinsiyet" : False,
        "Yas" : "20"
    },
    36: {
        "Ad ": "Mehmet",
        "Soyad" : "Karagüler",
        "Cinsiyet" : True,
        "Yas" : "39",

    }
}

# 10- Kullanıcıdan öğrenci numarası alarak öğrenci bilgilerini ekrana yazdıralım
# ÖRNEK METİN: 100 nolu öğrencinin adı Eren Özdal ve cinsiyeti erkek
#print(("Öğrenci ismi :") + (students[13["Ad"]]) + ("Öğrenci Soyismi :") )
# 11- Kullanıcıdan 2 saynt' object is not subscriptableı alalım ve bu sayıları "a" ve "b" değişkenlerine atayalım.

# 12- "a"nın "b" ile toplamını "a" değişkenine atayıp ekrana yazdıralım.
a = 5
b = 6
a += b
print(a)
# 13- "a"nın "b" ile farkını "a" değişkenine atayıp ekrana yazdıralım.
a -= b
print(a)
# 14- "a"nın "b" ile çarpımını "a" değişkenine atayıp ekrana yazdıralım.
a *= b
print(a)
# 15- "a"nın "b"ye bölümünü "a" değişkenine atayıp ekrana yazdıralım.
a /= b
print(a)
# 16- "a"nın "b"ye bölümünden kalanı "a" değişkenine atayıp ekrana yazdıralım.

"""
a = a/b
y = (a //= b)
a - y = a
print(a)
"""

# 17- "a"nın "b" üssünü "a" değişkenine atayıp ekrana yazdıralım.
a **= b
# 18- "a"nın "b"ye kalansız bölümünü "a" değişkenine atayıp ekrana yazdıralım.

a //= b

# 19- Kullanıcıdan 2 sayı alıp, 1. sayı 2. sayıdan büyük mü ekrana yazdıralım.
# ÖRNEK METİN: 1. sayı, 2. sayıdan büyük mü: True
sayi1 = input("Sayı 1 i giriniz :")
sayi2 = input("Sayı 2 yi giriniz :")
if sayi1 > sayi2:
    print("Sayı 1 daha büyük")
if sayi1 < sayi2:
    print("Sayı 2 daha büyük")

# 20- Kullanıcıdan 1. sınav (%40) ve 2. sınav notu (%60) alıp ortalama hesaplayalım.

Sinav1 = float(input("1 . sınav notu"))
Sinav2 = float(input("2 . sınav notu"))

# Eğer ortalama 45 üzerindeyse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: 1. sınav: 50, 2. sınav: 70, Ortalama: 62. Geçti mi: True
Toplam = Sinav1 + Sinav2 
ort = Toplam / 2 
if ort > 45:
    print("True")
if ort < 45:
    print("False")
# 21- Kullanıcıdan bir sayı alalım ve bu sayı tekse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: Girilen sayı: 5. Tek mi: True

# 22- Kullanıcıdan bir sayı alalım ve bu sayı pozitifse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: Girilen sayı: -10. Pozitif mi: False

# 23- Kullanıcıdan alınan bir sayının 0-100 arasında olup olmadığını
# "and" operatörü ile bulup ekrana yazdıralım
# ÖRNEK METİN: Sayı: 110. 0-100 arasında mı: False