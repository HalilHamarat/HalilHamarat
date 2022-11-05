liste = [1, 2, 3]
tuple = ("bir", "iki", "üç")

#tuple ı ekrana yazdıralım
print(liste)
print(type(liste))
print(tuple)
print(type(tuple))

#beliri bir elemanı ekrana yazdıralım
print(tuple[0])

#listenin ve tuple ın bir elemanını değiştirme
liste[0] = 7
"""
 tuple[0] = "yedi" 
 TypeError: 'tuple' object does not support item assignment
"""
print(tuple)

# tuple içindeki belirli bir elemanın indeksini bulalım: index()
print(tuple.index("bir"))

#tuple'ı birleştirelim
tuple1 = (1, 2, 3)
tuple2 = "bir", "iki", "üç"
tuple1_2 = tuple1 + tuple2
print(tuple1 + tuple2)
print(tuple1_2)