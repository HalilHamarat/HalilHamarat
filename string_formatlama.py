#Kullanıcıdan isim, soyad, yaş billgilerini alalım

isim= input("İsiminizi ilgili alana giriniz:")
soyad= input("Soyisminizi ilgili alana giriniz:")
yas= input("Yaşınızı ilgili alana giriniz:")

#FARKLI YÖNTEMLER
print("Adınız ve Soyadınız:  " + isim + "  " + soyad + " , Yaşınız: " + yas )
print("Adınız ve Soyadınız:  {}  {} , Yaşınız:   {}".format(isim, soyad , yas) )
print("Adınız ve Soyadınız:  {0}  {1} , Yaşınız:   {2}".format(isim, soyad , yas) )
print("Adınız ve Soyadınız:  {x}  {y} , Yaşınız:   {z}".format(x =isim, y=soyad , z=yas) )
print(f"Adınız ve Soyadınız:  {isim}  {soyad} , Yaşınız:   {yas}")