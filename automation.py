from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys  #-> biblioteca para poder dar "enter"
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller
from util import open_new_window

import time
import datetime as dt
# from selenium.webdriver.common.keys import Keys  #-> biblioteca para poder dar "enter"

chromedriver_autoinstaller.install()
navegador = webdriver.Chrome()


# sites para procurar 

navegador.get("https://br.indeed.com/")

time.sleep(1)
navegador.find_element('xpath', '//*[@id="text-input-what"]').send_keys("Python jr")
navegador.find_element('xpath', '//*[@id="text-input-what"]').send_keys(Keys.ENTER)
time.sleep(1)

navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.CONTROL + 'a')
navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.BACKSPACE)
navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.ENTER)
time.sleep(1)
navegador.find_element('xpath', '/html/body').send_keys(Keys.ESCAPE)
time.sleep(1)

# qtd_vagas =  navegador.find_element("xpath", '//*[@id="jobTitle-3ea7cb4ed438f8b5"]').get_attribute('title')
# //*[@id="jobTitle-e64d16e8c0bc4ead"]
# qtd_vagas =  navegador.find_element("class_name", 'css-5lfssm eu4oa1w0')
# jcs-JobTitle css-jspxzf eu4oa1w0
# jcs-JobTitle css-jspxzf eu4oa1w0

list_items = navegador.find_elements(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li')

vagas = []

qtd = 1

# Iterate over each li element
for li in list_items:
    # Find the relevant span within the li
    data = dt.datetime.now()
    
    
    title_element = li.find_element(By.XPATH, './/span')  # Relative XPath to find the span inside the current li
    title = title_element.text
    
    a_element = li.find_element(By.XPATH, './/a')  
    link = a_element.get_attribute('href')

    
    print(f'Título {qtd}: {title}')
    print(f'Link: {link}')

    vagas.append({
        'Titulo': title,
        'Link': link,
        'data_encontrada': data.strftime('%x')})


    qtd += 1  # Increment the counter (optional, based on your needs)


open_new_window(navegador)




# navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys("Cuiabá, MT")


# navegador.implicitly_wait(5)
# navegador.set_page_load_timeout(5)
# navegador.set_script_timeout(5)
# pausa = WebDriverWait(navegador, timeout=5)
# pausa.until(lambda x: revealed.is_displayed())



# navegador.get("https://www.nerdin.com.br/vagas?UF=HO")
# navegador.get("https://www.linkedin.com/jobs/")
# navegador.get("https://programathor.com.br/jobs")
# navegador.get("https://www.catho.com.br/area-candidato")
# navegador.get("https://portal.gupy.io/")

