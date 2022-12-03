ogrenciler = ["Eren", " Enes", "Ahmet"]
ogrenci_1 = input("Öğrenci ismi giriniz : ")
ogrenci_2 = input("Öğrenci ismi giriniz : ")
ogrenciler.append(ogrenci_1)
print(ogrenciler)
ogrenciler.append(ogrenci_2)
print(ogrenciler)
for ogrenci in ogrenciler:
    print(f"ogrencinin adı:{ogrenci}")

# İÇinde ikili sayılardan oluşan tuple verilerinin olduğu bir liste oluşturalım
sayilar = [(1, 2), (3, 4), (5, 6)]

for a, b in sayilar:
    print(f"1. sayı: {a},2. sayı {b}")

okul = "Sancaktepe Teknoloji Anadolu Imam Hatip Lisesi"
for kelime in okul.split(" "):
    print(f"{kelime}")

ogrenciler = {
    1: {
        "Ad" : "Halil",
        "Soyad" : "Hamarat",
        "Cinsiyet" : True,
        "Dersler" : ["Python" , "Matematik" , "TekTas"]
    },
    45: {
        "Ad" : "İsmail",
        "Soyad" : "YK",
        "Cinsiyet" : False,
        "Dersler" : "Zeka Nedir Nasıl Kullanılır"
    },
    36: {
        "Ad" : "Mehmet",
        "Soyad" : "Karagüler",
        "Cinsiyet" : True,
        "Dersler" : "Zihinsel Problemlerden Kurtuluş Yolları",

    }
}
for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı öğrenci: {ogrenci['Ad']}")




