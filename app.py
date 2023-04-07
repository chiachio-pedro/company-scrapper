import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

landing_page = 'https://www.linkedin.com/login/pt'
webdriver_path = './webdriver/chromedriver'

email = input("Enter your LinkedIn e-mail:")
password = input("Enter your LinkedIn password:")

# Iniciando o WebDriver do Google Chrome...
service = Service(webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessando o LinkedIn...
driver.get(landing_page)
time.sleep(3)

# Preenchendo os Dados de Login e Acessando...
email_field = driver.find_element("id", "username")
email_field.send_keys(email)
time.sleep(2)
password_field = driver.find_element("id", "password")
password_field.send_keys(password)
time.sleep(2)
password_field.send_keys(Keys.RETURN)
time.sleep(5)
