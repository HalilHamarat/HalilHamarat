"""
1. Aktüel ürünler sayfasına git https://www.bim.com.tr/Categories/100/aktuel-urunler.aspx
2. Gelecek hafta'ya tıkla
3. Tarihlere tıklayarak aşağıdaki işlemleri yap
    3.1. Ürünler içinde aşağıdaki işlemleri yap
        3.1.1. Ürün resmini kaydet
        3.1.2. Ürün bilgilerini oku
        3.1.3. Ürün fiyatını oku
"""

from selenium.webdriver.common.by import By
from time import sleep
from moduller.tarayici import Tarayici

# tarayıcıyı oluştur
tarayici_nesne = Tarayici()
tarayici = tarayici_nesne.al()

# 1. Aktüel ürünler sayfasına git
tarayici.get("https://www.bim.com.tr/Categories/100/aktuel-urunler.aspx")

# çerezleri kabul et
tarayici.find_element(By.XPATH, '//*[@id="form1"]/div/footer/div/div[5]/button[1]').click()

# 2. Gelecek haftaya tıkla
gelecek_hafta = tarayici.find_element(By.XPATH, "//span[normalize-space()='GELECEK HAFTA']").click()


# 3. Tarihlere tıklayarak aşağıdaki işlemleri yap
tarihler = tarayici.find_elements(By.XPATH, "//div[@class='subButtonArea subButtonArea-5 active']//a")

# tarihlerdeki işlemleri for içinde yapıcağız
for i, tarih in enumerate(tarihler):
    # tarayici.execute_script("window.scrollTo(0, 0);") yukarı kaydırma hatayı gidermedi
    tarih = tarayici.find_element(By.XPATH, f"//div[@class='subButtonArea subButtonArea-5 active']//a[{i+1}]")
    tarayici.execute_script("arguments[0].click();", tarih)
    # tarih.click()   sayfa yenileniyor


    # 3.1 ürünler içinde aşağıdaki işlemleri yap
    urunler = tarayici.find_elements(By.XPATH, "//div[contains(@class, 'product')]")
    for urun in urunler:
        try:
            ad = urun.find_element(By.XPATH, ".//h2[@class='title']")
        except:
            continue

        try:
            urun.find_element(By.TAG_NAME, "img").screenshot(f"./gorseller/{ad.text}.png")
        # ürünün adını alalım
        # 3.1.1. ürün resmini kaydet
        except:
            continue