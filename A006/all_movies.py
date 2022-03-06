#%%
from selenium import webdriver
import pandas as pd
import time

#SCRIPT COM ERRO
#%%

driver = webdriver.Chrome('D:\Python\How_Exercicios\A006\src\chromedriver.exe')

def tem_item(xpath, driver = driver):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

time.sleep(5)
driver.implicitly_wait(40)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
#%%

tb_filmes = '/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[2]'

i = 0
while not tem_item(tb_filmes):
    i+=1
    if i > 50:
        break
    pass

tabela = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[2]')

#tabela.text
#print(tabela.get_attribute('innerHTML'))

#%%

df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]
df
#%%
##Trecho com erro
with open('print.png', 'wb') as f:
    f.write(driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[1]/tbody/tr[2]/td/div/div/div/a/img'))

#%%
driver.close()

#print(df.head())
#%%
#df[df['Ano']==1984]

df.to_csv('filmes_Nicolas_cage.csv', sep=';', index=False)