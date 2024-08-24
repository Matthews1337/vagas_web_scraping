from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys  #-> biblioteca para poder dar "enter"
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

import time
import datetime as dt
import pandas as pd
import sys
import os

from openpyxl import load_workbook
diretorio = os.getcwd()

from typing import Literal


def criar_planilha(df, *, path='', salvar_como: Literal['CSV', 'EXCEL']= 'EXCEL', nm_sheet='Novo'):
    data_windows = dt.datetime.now()
    file_name = f"Vagas_do_dia_{data_windows.strftime('%d')}"

    if salvar_como == 'CSV':
        file_path = os.path.join(path, f"{file_name}.csv")
        if os.path.exists(file_path):
            print(f"O arquivo {file_name}.csv já existe.")
        else:
            df.to_csv(file_path, index=False)
            print(f"Arquivo CSV criado em: {file_path}")

    elif salvar_como == 'EXCEL':
        # file_path = os.path.join(path, f"{file_name}.xlsx")
        file_path = f"{path}"  
        if os.path.exists(file_path):
            print(f"O arquivo {file_name}.xlsx já existe. Adicionando nova aba...")
            add_sheet_planilha(df_=df, file_path=file_path, nm_sheet=nm_sheet)  # Função para adicionar uma nova sheet
        else:
            df.to_excel(file_path, index=False)
            print(f"Arquivo Excel criado em: {file_path}")
    else:
        print('formato inválido!')



def add_sheet_planilha(df_, *, file_path='c:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/web_scraping/vagas_jr', nm_arquivo='vagas_do_dia', nm_sheet='nerdin'):
    # diretorio_planilhas = os.path.join(diretorio, "planilhas")
    # diretorio_planilhas = os.path.join("Vagas_do_dia_12.xlsx")
    # print(diretorio)
    data_windows = dt.datetime.now()
    nm_arquivo_dia = f'{nm_arquivo}_{data_windows.strftime("%d")}' 
    complete_path = f'{file_path}/{nm_arquivo_dia}.xlsx'
    with pd.ExcelWriter(complete_path, engine = 'openpyxl', mode='a', if_sheet_exists='replace') as writer:
    
        df_.to_excel(writer, sheet_name= nm_sheet)
        # writer.save()



def open_new_window(driver):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])



def get_vagas_indeed(pesquisar_por: str='Python jr', resumo = True, navegador = 'Edge')-> pd.DataFrame:
    
    chromedriver_autoinstaller.install()

    if navegador.title() == 'Edge':
        navegador = webdriver.Edge()
        
    elif navegador.title() == 'Chrome':
        navegador = webdriver.Chrome()
        

    navegador.get("https://br.indeed.com/")

    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="text-input-what"]').send_keys(pesquisar_por)
    navegador.find_element('xpath', '//*[@id="text-input-what"]').send_keys(Keys.ENTER)
    time.sleep(1)

    navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.CONTROL + 'a')
    navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.BACKSPACE)
    navegador.find_element('xpath', '//*[@id="text-input-where"]').send_keys(Keys.ENTER)
    time.sleep(1)
    navegador.find_element('xpath', '/html/body').send_keys(Keys.ESCAPE)
    time.sleep(1)
    
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    list_items = navegador.find_elements(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li')
    print(list_items)
    print(len(list_items))
    vagas = []
    qtd = 1
    # Iterate over each li element
    for li in list_items:
        try:
            # Find the relevant span within the li
            data = dt.datetime.now()
            title_element = li.find_element(By.XPATH, './/span')  # Relative XPath to find the span inside the current li
            title = title_element.text

            a_element = li.find_element(By.XPATH, './/a')  
            link = a_element.get_attribute('href')

            if resumo == True:
                print(f'Título {qtd}: {title}')
                print(f'Link: {link}')

            vagas.append({
                'Titulo': title,
                'Link': link,
                'data_encontrada': data.strftime('%x')
                })

            qtd += 1  # Increment the counter (optional, based on your needs)
        except Exception as e:
            print(f'Não foi possível encontrar o elemento!  [ERRO]: {e}')
            continue

    df_vagas = pd.DataFrame(vagas)
    navegador.close()
    return df_vagas



def get_vagas_nerdin(pesquisar_por: str ='', resumo = True, navegador = 'Edge'):
    chromedriver_autoinstaller.install()
    if navegador.title() == 'Edge':
        navegador = webdriver.Edge()
    elif navegador.title() == 'Chrome':
        navegador = webdriver.Chrome()
    navegador.get("https://www.nerdin.com.br/vagas?UF=HO")
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="PalavraChave"]').send_keys(pesquisar_por)
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="PalavraChave"]').send_keys(Keys.ENTER)
    time.sleep(1)
    # lista_vagas = navegador.find_element(By.C '//*[@id="divListaVagas"]').send_keys(Keys.ENTER)
    lista_vagas = navegador.find_element(By.ID, 'divListaVagas')
    divs_filhas = lista_vagas.find_elements(By.TAG_NAME, 'div')
    qtd = 1
    vagas_nerdin =[]
    data = dt.datetime.now()
    for vagas in divs_filhas:
        try:
            # div_2 = vagas.find_elements(By.TAG_NAME, 'div')
            a_element = vagas.find_elements(By.TAG_NAME, 'a')[0]
            link = a_element.get_attribute('href')
            vagas_nerdin.append({
            'Titulo': vagas.text,
            'Link': link,
            'data_encontrada': data.strftime('%d/%m/%Y')
            })
            qtd += 1
        except IndexError as e:
            # print(f'Erro ao encontrar o link: {e}')
            continue
    navegador.close()
    df_vagas_nerdin = pd.DataFrame(vagas_nerdin)
    df_vagas_nerdin = df_vagas_nerdin.drop_duplicates(subset='Link', keep='first')
    if resumo:
        print(f'Foram encontrados {df_vagas_nerdin.shape[0]} vagas!')
    return df_vagas_nerdin