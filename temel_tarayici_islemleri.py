from time import sleep
from moduller.tarayici import Tarayici
tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

# Tarayıcıda gezinme
tarayici.get("https://github.com/erenmustafaozdal/taihl-bot-yazma-2022/blob/master/temel_tarayici_islemleri.py")
print(tarayici.current_url)
sleep(1)

# yeni adrese gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr/34/40/766892/teskilat_semasi.html")
print(tarayici.title)
sleep(1)

# geri dönelim
tarayici.back()
print(tarayici.title)
sleep(1)

# ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(1)

# pencere boyutunu yazdıralım
print(tarayici.get_window_size())

# pencere boyutu ayarlayalım
tarayici.set_window_size(500, 300)
sleep(2)

# pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.set_window_position(100, 500)
sleep(2)

# pencereyi tam ekran yapalım
tarayici.maximize_window()
sleep(2)

tarayici.save_screenshot("./görseller/bot-yazma.png")