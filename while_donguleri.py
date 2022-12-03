"""
Python'da kullanabileceğimiz 2 tane döngü tipinden diğer "While"dır
Belirttiğimiz koşul doğru (True) olduğu sürece devam eden döngü tipidir
"""

#0'dan 100'e kadar olan tek ve çift sayıları yazdıralım
#Örnek: 1 tek sayıdır
#Örnek: 2 çift sayıdır
sayi = 1
while sayi < 101:
    if (int(sayi) % 2 == 0):
        print(f"{sayi} Sayı Çift")

    else:
        print(f"{sayi} Sayı Tek")
    sayi += 1

import xlrd



