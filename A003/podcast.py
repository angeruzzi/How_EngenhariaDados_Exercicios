# %%
#pip install bs4
#pip install pandas
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd 

# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts'
# %%
ret = requests.get(url)
# %%
ret.text
# %%

soup = bs(ret.text)

# %%

soup.find('h5')

# %%
soup.find('h5').text

# %%
soup.find('h5').a
# %%
soup.find('h5').a['href']
# %%

lst_podcast = soup.find_all('h5')

for item in lst_podcast:
    print (f"EP: {item.text} - Link: {item.a['href']}")

#Lista apenas a primeira exibição
# %%

urlGeral = 'https://portalcafebrasil.com.br/todos/podcasts/page{}/?ajax=true'

# %%
urlGeral.format(5)


# %%
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')
# %%
get_podcast(urlGeral.format(5))
# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

i = 1
lst_podcast = []
lst_get = get_podcast(urlGeral.format(i))

while len(lst_get) > 0:
    log.debug(f"Coletado {len(lst_get)} episódios do link: {urlGeral.format(i)}")
    lst_podcast = lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(urlGeral.format(i))
# %%

len(lst_podcast)

# %%
lst_podcast
# %%
df = pd.DataFrame(columns=['nome', 'link'])
# %%

for item in lst_podcast:
    df.loc[df.shape[0]] = [item.text, item.a['href']]

# %%
df
# %%
df.to_csv('banco_de_podcast.csv', sep=';', index=False)
# %%



