numaralar = []
for i in range(100, 200):
    numaralar.append(i)
print(numaralar)



numaralar2 = [sayi for sayi in range(100,200)]
print(numaralar2)

ciftsayilar = [sayi for sayi in range(100,200) if sayi %2 ==0]
print(ciftsayilar)

numaralar3 = [f"{sayi} TEK" if sayi %2 ==1 else f"{sayi} ÇİFT" for sayi in range(100,200)]
print(numaralar3)

liste = []
for x in range(3):
    for f in range(3):
        liste.append((x, f))
print(liste)
liste2 = [(x,y) for x in range(3) for y in range(3)]
print(liste2)