#tarayıcı nesnemizi import edelim
from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import By
tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()
from time import sleep

 #okulun adresini al
tarayici.get("https://teknolojiaihl.meb.k12.tr/")
tarayici.maximize_window()

#class seçici kullanarak bir elemana ulaşalım
baslik = tarayici.find_element(By.CLASS_NAME, "container")
baslik.screenshot("./foto/foto2.png")

#css seçimi ile elemana ulaşalım
arama_kutusu = tarayici.find_element(By.CSS_SELECTOR, "#araTextBox")
arama_kutusu.send_keys("inovasyon")
sleep(2)
arama_tus = tarayici.find_element( By.CSS_SELECTOR, "#araButton")
#arama_tus.click()
#sleep(5)

#name öz niteliği ile elemana ulaşalım
twitter_title = tarayici.find_element(By.NAME,"twitter:title")

print(twitter_title.get_attribute("content"))

#bağlantı metni ile elemana ulaşalım
okullarimiz = tarayici.find_element(By.LINK_TEXT,  "Okullarımız")
# okullarimiz.click()
# sleep(5)

#kısmi bağlantı metni ile elelmana ulaşalım
aile_birligi = tarayici.find_element(By.PARTIAL_LINK_TEXT, "Aile Birliği")
#aile_birligi.click()
#sleep(5)

#etiket adı ile elemanlara ulaşalım
linkler = tarayici.find_elements(By.TAG_NAME, "a")
print(len(linkler))

iletisim = tarayici.find_element(By.XPATH, '//*[@id="o_hakkinda"]')
iletisim.screenshot("./gorseller/iletisim.png")