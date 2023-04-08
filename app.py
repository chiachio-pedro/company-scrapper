import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

landing_page = 'https://www.linkedin.com/login/pt'
webdriver_path = './webdriver/chromedriver'

email = input("Preencha seu E-Mail de Acesso ao LinkedIn: ")
password = input("Preencha sua Senha de Acesso ao LinkedIn: ")
company = input("Preencha um Termo de Busca para Encontrar Alguma Empresa: ")

# Formatando Empresa...
company = company.replace(" ", "%20")

# Criando Output de Respostas...
json = {'Nome da Empresa': [],
        'LinkedIn': [],
        'Site': [],
        'Telefone de Contato': []}

# Iniciando o WebDriver do Google Chrome...
service = Service(webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessando o LinkedIn...
driver.get(landing_page)
time.sleep(3)

# Preenchendo os Dados de Login e Acessando...
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)
time.sleep(3)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
time.sleep(3)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Procurando o Tipo de Empresa...
search_link = f"https://www.linkedin.com/search/results/companies/?keywords={company}"

driver.get(search_link)
time.sleep(3)

# Coletando todos os Links dos Resultados por Página Através de Iteração...
while True:

    cp_links = driver.find_elements(By.CLASS_NAME, "entity-result")
    linkedin_list = [link.find_elements(By.CLASS_NAME, "app-aware-link")[0].get_attribute('href') for link in cp_links]
    json['LinkedIn'].extend(linkedin_list)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    next_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Avançar']")

    if next_button.is_enabled():

        next_button.click()
        time.sleep(3)

    else:

        break

# Acessando as Páginas e Coletando Demais Informações...
for link in json['LinkedIn']:

    driver.get(link)
    time.sleep(3)

    # Coletando o Nome da Empresa...
    try:

        name = driver.find_element(By.CLASS_NAME, "org-top-card-summary__title")
        name = name.text

    except:

        name = 'Não Informado'

    json['Nome da Empresa'].append(name)

    # Coletando o Site da Empresa...
    driver.get(link + 'about/')
    time.sleep(2)

    try:

        probably_sites = driver.find_elements(By.CLASS_NAME, "link-without-visited-state")
        site = 'Não Informado'

        for probably_site in probably_sites:

            if ('www' in probably_site.text) or ('http' in probably_site.text):

                site = probably_site.text
                break

            else:

                continue

    except:

        site = 'Não Informado'

    json['Site'].append(site)

    # Coletando o Telefone de Contato da Empresa...
    try:

        probably_phones = driver.find_elements(By.CLASS_NAME, "link-without-visited-state")
        phone = 'Não Informado'

        for probably_phone in probably_phones:

            pattern = r'^[0-9!@#$%^&*(),.?":{}|<>_+=\-\[\]\\/\s]+$'

            if bool(re.match(pattern, probably_phone.text)):

                phone = probably_phone.text
                break

            else:

                continue

    except:

        phone = 'Não Informado'

    json['Telefone de Contato'].append(phone)

driver.quit()

df = pd.DataFrame(json).to_csv('lead_list.csv', sep=';', decimal=',', index=False)

print('Done!')
