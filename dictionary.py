"""
Dictionary "anahtar","değer" ikililerinden oluşur
    "ad": Eren
    "soyad" : ozdal

"""
"""
#belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yapalım
numaralar = [66,75]
isimler = ["Ahmet", "Mehmet"]
numara = int(input("Öğrenci numarası yazınız"))


konum1 = numaralar.index(66)
print(isimler[konum1])


konum2 = numaralar.index(75)
print(isimler[konum2])

#belirli bir numaraya sahip bir öğrenciyi bulma işlemini dictionary ile yapalım
ogrenciler = {66: "Ahmet", 75: "Mehmet"}
print(ogrenciler[numara])
"""
#detaylı örnek
kisiler = {
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
print(kisiler[1]["Dersler"])
print(kisiler[45]["Dersler"])
print(kisiler[36]["Dersler"])

veri_tipi= {
    "ikinci" : {

    },
    "üçüncü" : {


    }
}
print(veri_tipi)

