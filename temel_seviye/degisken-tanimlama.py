# Değişkenler olmadan 2 öğrencinin sınav notlarını hesaplayalım
#print( (80*0.4) + (75*0.6) )
#print( (45*0.4) + (60*0.6) )
############################################################
# #DEĞİŞKENLERLE İKİ ÖĞRENCİNİN SINAV NOTLARINI HESAPLAYALIM
# sinav1_yuzde = 0.4
# sinav2_yuzde = 0.6
#
# #print( (80*sinav1_yuzde ) + (75*sinav2_yuzde) )
# #print( (45*sinav1_yuzde ) + (60*sinav2_yuzde) )
############################################################
# DEĞİŞKEN TANIMLAMA KURALLARI

 # Rakam İle Başlayamaz !

 # 1say = 85
 # print(1sayi)
 #
 # sayi1 = 85
 # print(sayi1)
 ###          ###

 #Büyük Küçük Harflere Duyarlıdır ! !

 # number = 12
 # NUMBER = 15
 #
 # print(number)
 # print(NUMBER)
 ###          ###

 #Türkçe Karakter Kullanılamaz ! ! !

 #yaş = 18 hatalı kullanımdır

 # yas = 18 #Türkçe Karakter Olmadan Türkçe Yazmak (TAVSİYE EDİLMEZ)
 # age = 17
 # print(yas)
 # print(age)

#DEĞİŞKENLERDEKİ VERİLERİ BİRLEŞTİRME

x = 1 #İnt
y = 1.2 #Float
ad = "Eren" #String
sinav_basarili_mi = True #boolean (bool)

print(x+y)
#print(x+ad)  hata verdi (int ile str birleştirilemez)
print(x+sinav_basarili_mi)
#print(ad+sinav_basarili_mi) hata verdi (TypeError: can only concatenate str (not "bool") to str)