ad = input("adınız: ")
soy = input("soyadınız: ")
notlar = input("sınav notları (virgülle ayrılmış)")


def ogrenci_kaydet(ad,soyad,notlar):
    notlar_list = [int(x) for x in notlar.split(",")]
    ortalama = sum(notlar_list) / len(notlar_list)

    dosya = open("ogrenciler.txt", mode="a")
    dosya.write(f"ad:{ad} , soyad:{soy} , notlar:{notlar} , ortalama:{notlar_list}")
    dosya.close()

while True:
    ne_yapilacak = input("Ne yapacaksınız (1 kaydet) (0 çık)")



    if ne_yapilacak == "0":
        break

    ad = input("ad")
    soyad = input("soyad")
    notlar = input("not")
    ogrenci_kaydet(ad, soyad, notlar)