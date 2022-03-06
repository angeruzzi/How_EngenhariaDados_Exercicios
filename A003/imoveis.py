# %%
from numpy import arange
from pkg_resources import ensure_directory
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# %%
url = 'https://vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'

# %%

i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%
soup
# %%
houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
qtd_imoveis = float(soup.find('strong', {'class': 'results-summary__count js-total-records'}).text.replace('.',''))

# %%
qtd_imoveis
##len(houses)
# %%
df = pd.DataFrame(
    columns=[ 
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'wlink'
    ]
)

i = 0
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f"Valor i: {i} \t\t qtd_imoveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'})

    for house in houses:
        try:
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'property-card__detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try:
            wc = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            wc = None
        try:
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = None
        try:
            valor = house.find('div', {'class': 'property-card__price'}).p.text.strip()
        except:
            valor = None
        try:
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try:
            wlink = 'https://vivareal.com.br'+house['href']
        except:
            wlink = None

        df.loc[df.shape[0]] = [ 
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink
        ]

# %%
print(descricao)
print(endereco)
print(area)
print(quartos)
print(wc)
print(vagas)
print(valor)
print(condominio)
print(wlink)

# %%
df
# %%
