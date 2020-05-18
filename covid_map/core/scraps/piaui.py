from unicodedata import normalize
from core.models import CasosPorCidadePiaui
import pandas as pd
import requests
import json
import difflib


def main():
    url = 'http://coronavirus.pi.gov.br/'
    pagina = pd.read_html(url)
    dados_governo = pagina[0]

    dados_governo.columns = ['Cidade', 'Confirmados', 'Óbitos', 'Letalidade']

    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/22/municipios'
    jsonCi = json.loads(requests.get(url).text)

    nomes = []
    ids = []
    for i in jsonCi:
        nomes.append(i['nome'])
        ids.append(i['id'])

    casos = [0 for i in range(len(nomes))]
    obitos = [0 for i in range(len(nomes))]

    for itrIB, cIBGE in sorted(enumerate(nomes), key=lambda x: (x[0], x[1])):
        for itrCO, cCOVID in enumerate(dados_governo.Cidade):
            if compara_cidades(cIBGE, cCOVID):
                casos[itrIB] = dados_governo.Confirmados.iloc[itrCO]
                obitos[itrIB] = dados_governo['Óbitos'].iloc[itrCO]

    bulk = []
    for nome, idibge, casos, mortes in zip(nomes, ids, casos, obitos):
        bulk.append(CasosPorCidadePiaui(name=nome, idIBGE=idibge, casos=casos, obitos=mortes))

    if CasosPorCidadePiaui.objects.all().exists():
        CasosPorCidadePiaui.objects.bulk_update(bulk, fields=['casos', 'obitos'])
    else:
        CasosPorCidadePiaui.objects.bulk_create(bulk)


def padronizar_cidade(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII').lower()


def compara_cidades(*args):
    cidade1, cidade2 = map(padronizar_cidade, args)

    min_percent_equal = 95
    diff = difflib.SequenceMatcher(None, cidade1, cidade2)
    percent_equal = round(diff.ratio(), 5) * 100

    return percent_equal >= min_percent_equal
