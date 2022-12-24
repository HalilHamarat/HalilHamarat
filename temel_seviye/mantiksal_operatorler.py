"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.
+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+
"""

# Futbolcuların 5 ve 8 asist üzerinde olanları başarılı sayalım
ftb1 = {
    "gol" : 5,
    "asist": 9
}
ftb2 = {
    "gol": 8,
    "asist": 10
}
ftb3 = {
    "gol": 12,
    "asist": 99
}
print(f"1. futbolcu : {(ftb1['gol'] > 5 and ftb1['asist'] > 8)}")
print(f"2. futbolcu : {(ftb2['gol'] > 5 and ftb2['asist'] > 8)}")
print(f"3. futbolcu : {(ftb3['gol'] > 5 and ftb3['asist'] > 8)}")

#futbolcuların golü 5 den fazlaysa veya asist i 8'den fazlaysa başarılı sayalım
print(f"1. futbolcu : {(ftb1['gol'] > 5 or ftb1['asist'] > 8)}")
print(f"2. futbolcu : {(ftb2['gol'] > 5 or ftb2['asist'] > 8)}")
print(f"3. futbolcu : {(ftb3['gol'] > 5 or ftb3['asist'] > 8)}")

# futbolcunun golü 5'ten büyük değilse başarısız olsun
print(f"1. futbolcu : {not(ftb1['gol'] > 5 )}")
print(f"2. futbolcu : {not(ftb2['gol'] > 5 )}")

