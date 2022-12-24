from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
