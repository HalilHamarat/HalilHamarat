url = "https://teknolojiaihl.meb.k12.tr"

# 1- "url" içinde kaç karakter olduğunu yazdır.
print(len(url))


# 2- "url" içindeki "meb" sözcüğünü ekrana yazdırın.

print(url[22])
print(url[23])
print(url[24])

# 3- "url" içindeki "k12" sözcüğünü ekrana yazdırın.
print(url[26])
print(url[27])
print(url[28])


# 4- Kullanıcıdan adını, en sevdiği yemeği alın ve cümle içinde yazdırın.
# ÖRNEK CÜMLE: Adınız: halil. En sevdiğiniz yemek: köfte

yemek = "köfte"
isim = "halil"

print("Adınız: " + isim + ", En Sevdiğiniz Yemek: " + str(yemek))


# 5- Öğrencinin 2 sınav notunu alın. Notunu hesaplayıp cümle içinde yazdırın.
# 1. sınav oranı: %35
# 2. sınav oranı: %65

x = input("1. yazılı : ")
y = input("2. yazılı : ")
print((float(x)*0.35)+(float(y)*0.65))



# ÖRNEK CÜMLE: 1. sınav: 70 puan, 2. sınav: 90 puan, Notunuz: 83.0

# 6- Kullanıcının adını alın ve yan yana 100 defa yazdırın.



ad = input("adın ne:  ")

a = 0

while a < 100:
    a = a+1
    print(""+ ad)

    "yapan kişi halilhamarat"