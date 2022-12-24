from selenium import webdriver

# ChromeDriver'ın yolunu belirtin
driver = webdriver.Chrome(r"C:\path\to\chromedriver.exe")

# Chrome tarayıcısını açın ve belirlediğiniz web sayfasına gidin
driver.get("https://www.google.com")

# Arama kutusuna belirlediğiniz arama sorgusunu girin
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python")

# Arama düğmesine tıklayın
search_button = driver.find_element_by_name("btnK")
search_button.click()

# Tarayıcıyı kapatın
driver.quit()