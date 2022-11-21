# Kaynak: https://tr.wikipedia.org/wiki/Python
bilgi = """Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir programlama dilidir.
Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır. Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma özelliği kazandırır.
Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir (Unix, Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web programlama, uygulama ve veri tabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir.
Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında yayınlandı. 2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, dilin son sürümü olan Python 2.7.x serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.6.x ve sonraki sürümlerinin geliştirilmesi devam etmektedir."""

# 1- "bilgi" değişkenindeki metin kaç paragraf?
paragraflar = (bilgi.split("\n"))
print(len(paragraflar))

# 2- "bilgi" değişkenindeki metin kaç cümle?
paragraflar = (bilgi.split("."))
print(len(paragraflar))
# 3- "bilgi" değişkenindeki metni küçük harfe çevirdiğimizde,
# "python" kelimesi kaç defa geçiyor?
print(paragraflar[0].lower().count("python"))

# 4- Kullanıcıdan input ile aralarına virgül koydurarak meyve isimleri alın.
print("Lütfen Yazacağınız Meyvelerin Arasına "," Koyunuz...")
Fruit_names = input("Meyve :")
newFrtNms = Fruit_names.replace(" ","").split(",")
print(Fruit_names)

# Bu meyve isimlerini listeye çevirin. İsimlerini alfabetik olarak sıralayın.

newFrtNms.sort()
print(newFrtNms)
# 5- Meyve isimlerini alfabetik olarak ters sıralayın.
newFrtNms.sort(reverse=True)
print(newFrtNms)


ogrenciler = ["Ahmet", "Mehmet", "Funda", "Bekir", "Halime", "Kasım", "Yeşim", "Eylül"]
# 6- "ogrenciler" listesinin 3 numaralı indise sahip elemanı(BEKIR)nı silin.
ogrenciler.pop(3)
print(ogrenciler)
# 7- "ogrenciler" listesinin sonuna "Ali" ekleyin
ogrenciler.append("Ali")
print(ogrenciler)
# 8- "ogrenciler" listesinin 5 numaralı indis konumuna "Fatma" ekleyin
ogrenciler.insert(5 ,"Fatma")
print(ogrenciler)
ogrenciler.sort()
print(ogrenciler)
hesaplar = {
    "youtube": {
        "url": "youtube.com/channel/UCVFdrLZc3mcLUjYSxqJAGZQ",
        "abone": 155,
        "katılma_tarihi": "17/04/2020",
        "görüntülenme": 7095,
        "videolar": [
            {
                "url": "youtube.com/watch?v=fv7PigKN5G4",
                "başlık": "Tasarım ve Üretim Atölyesi"
            },
            {
                "url": "youtube.com/watch?v=yJIGJGdB9VA",
                "başlık": "Teknoloji Kampı"
            },
            {
                "url": "youtube.com/watch?v=AlpKJHLWJ4s",
                "başlık": "Yaz Dil Kampı"
            }
        ]
    },
    "facebook": {
        "url": "facebook.com/teknolojiaihl",
        "takipçi": 960,
    },
    "instagram": {
        "url": "instagram.com/teknolojiaihl",
        "takipçi": 4112,
        "takip": 158,
        "gönderi": 239,
    }
}
# 9- YouTube kanalının adresini yazdırın.
print(hesaplar["youtube"]["url"])
# 10- YouTube kanalının abone sayısını ve görüntülenme
# sayısını bir cümle içinde yazıdırın.
# ÖRNEK: Kanalın 100 abonesi ve 4500 görüntülenmesi var.
Bilgi_Abone_YouTube = (hesaplar["youtube"]["abone"])
Bilgi_Goruntulenme_YouTube = (hesaplar["youtube"]["görüntülenme"])
Bilgi_Takipci_Facebook = (hesaplar["facebook"]["takipçi"])
Bilgi_Takipci_Instagram = (hesaplar["instagram"]["takipçi"])
Bilgi_Takip_Instagram = (hesaplar["instagram"]["takip"])

print("Kanalın Abone ve Görüntülenme Sayıları:  {}  {} ".format(Bilgi_Abone_YouTube, Bilgi_Goruntulenme_YouTube ) )

# 11- Facebook takipçi sayısını 15 artırıp ekrana yazdıralım.
print(str(Bilgi_Takipci_Facebook + 15))

# 12- Instagram takipçi ve takip sayısını toplamını ekrana yazdıralım
print(str(Bilgi_Takipci_Instagram + Bilgi_Takip_Instagram ) )

# 13- TAİHL sosyal medya hesaplarındaki toplam abone ve takipçi
# sayılarını ekrana yazdıralım

z = (hesaplar["youtube"]["abone"])
c = (hesaplar["facebook"]["takipçi"])
v = (hesaplar["instagram"]["takipçi"])

print(z + c + v )