sayilar = [9, 12, 85, 3, 16, 34, 42, 99, 165, 15]
harfler = [ "t" , "c" , "a" , "e" , "z" , "m" , "h" , "g" ]

#listelerin eleman sayısını bulalım: len(liste)

print(len(harfler + sayilar))
print("-"*50)
#listenin en küçük değerli elemanını bulalım: min()

print(min(sayilar))
print(min(harfler))
print("-"*50)
#listenin en büyük değerli elemanını bulalım: max()
print(max(sayilar))
print(max(harfler))
print("-"*50)
# metin ve sayılardan oluşan listeleri birleştirip en büyüğünü bulalım
# birlesmis = sayilar + harfler
# print(max(birlesmis))
"""TypeError: '>' not supported between instances of 'str' and 'int'"""

#listenin sonuna yeni eleman ekleyelim: append()
sayilar.append(95)
print(sayilar)
print("-"*50)
harfler.append("j")
print(harfler)
print("-"*50)
#listenin istediğimiz konumuna yeni eleman ekleyelim:
sayilar.insert(3, "b")
print(sayilar)
print("-"*50)
#listenin sonundaki veya belirtilen elemanı silelim: pop()
harfler.pop()
print(harfler)
sayilar.pop(3)
print(sayilar)
print("-"*50)
#listede belirli bir değere sahip elemanları silelim: remove("değer")
harfler.append("a")
harfler.remove("a")
print(harfler)
print("-"*50)
#listedeki elemanları sıralayalım: sort()
sayilar.sort()
print(sayilar)

harfler.sort()
print(harfler)

sayilar.reverse()
print(sayilar)

print(sayilar.sort(reverse=True))

print("-"*50)

#listedeki isimlerin alfabetik sıraya göre sıralayalım
isimler = ["Eren", "Ersin", "Ahmet", "Kaan"]
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)

#listeyi temizleyelim clear()
isimler.clear()
print(isimler)