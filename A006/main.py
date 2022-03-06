#%%
from selenium import webdriver
import sys

#SCRIPT COM ERRO

#%%

#driver.get('https://howedu.com.br/')
# %%
##Clique em botões
#driver.find_element_by_xpath('//*[id="PopupSignuoForm_0"]/div[2]/div[1]').click()
#driver.find_element_by_xpath('//*[@id="post-37"]/div/div/div/section[7]/div/div/div/div[3]/div/div/a/span/span').click()

# %%
cep = sys.argv[1]
if cep:
    driver = webdriver.Chrome('D:\Python\How_Exercicios\A006\src\chromedriver.exe')
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')

    # %%
    elem_cep = driver.find_element_by_name('endereco')
    elem_cmb = driver.find_element_by_name('tipoCEP')

    elem_cep.clear()
    elem_cep.send_keys('38412027')

    elem_cmb.click()
    driver.find_element_by_xpath('/html/body/main/form/div[1]/div[1]/div/div[2]/div/div[2]/select/option[6]').click()

    driver.find_element_by_id('btn_pesquisar').click()
    # %%

    logradouro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]').text
    bairro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]').text
    localidade = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]').text
    # %%
    print("""
    Para o CEP {} temos:
    Endereço: {}
    Bairro: {}
    Localidade: {}
    """.format(
    cep,
    logradouro,
    bairro,
    localidade
    ))








# %%
