from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import By
tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

tarayici.get("https://teknolojiaihl.meb.k12.tr/")
tarayici.maximize_window()

baslik = tarayici.find_element(By.CLASS_NAME,"conainer")