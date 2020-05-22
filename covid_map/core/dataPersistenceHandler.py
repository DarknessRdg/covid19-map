#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:57:05 2020

@author: romulobarros
"""

from urllib import request
import csv
import json
import os
from datetime import date as dt
from .cepHashMap import cepHashMap
##############################
# INSERT PATH DIR
###

script_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(script_path, "data")

###############################
# INSERT CODE AREA (IBGE)
###

def getCodareaFromHashMap(cep):
    codarea = cepHashMap[cep]['codigo_ibge']
    return codarea


def beautifyHeaderItem(item):
    """
    "Traduz" os nomes dos itens de cabeçalho dos dados 
        da SESAPI para nomes mais adequados.
    """
    hashMapNomesDasVariaveis = {
        # "id": "1", "Município": "AGUA BRANCA", "Confirmados": "40",
        # "Óbitos": "5", "Incidência": "22,97", "População": "17411",
        # "CEP": "64460000"
        "id": "id",
        "Município": "city",
        "Confirmados": "confirmed",
        "Óbitos": "deaths",
        "Incidência": "incidence",
        "População": "population",
        "CEP": "cep"
    }

    return hashMapNomesDasVariaveis[item]

def uglifyHeaderItem(item):
    """
    "Traduz" os nomes dos itens de cabeçalho dos nosso dados 
        para os dados da SESAPI.
    """
    hashMapNomesDasVariaveis = {
        # "id": "1", "Município": "AGUA BRANCA", "Confirmados": "40",
        # "Óbitos": "5", "Incidência": "22,97", "População": "17411",
        # "CEP": "64460000"
        "id": "id",
        "city": "Município",
        "confirmed": "Confirmados",
        "deaths": "Óbitos",
        "incidence": "Incidência",
        "population": "População",
        "cep": "CEP"
    }

    return hashMapNomesDasVariaveis[item]

def createEmptyCityInfoDictionary():
    emptyCityDictionaries = {}
    for cep in cepHashMap:
        city = {}
        city['city'] = cepHashMap[cep]['nome']
        city['confirmed'] = 0
        city['deaths'] = 0
        city['incidence'] = 0
        city['population'] = None
        city['cep'] = cep
        city['codigo_ibge'] = cepHashMap[cep]['codigo_ibge']
        emptyCityDictionaries[cep] = city

    return emptyCityDictionaries

###############################
# FETCH
###


def fetchData():
    # URL do Google Spreadsheet do Painel Epidemiológico da Covid-19 - SESAPI
    url = 'https://docs.google.com/spreadsheets/d/1b-GkDhhxJIwWcA6tk3z4eX58f-f1w2TA2f2XrI4XB1w/export?format=csv&gid=532454257'
    dadosDaPagina = request.urlopen(url)

    # Os dados obtidos através do urllib vêm no formato bytes.
    # Portanto, precisamos transformá-los em caracteres utf-8
    dadosDecodificados = []
    for row in dadosDaPagina:
        dadosDecodificados.append(row.decode('utf-8'))

    dic_DadosPorMunicipio = csv.DictReader(dadosDecodificados)
    cabecalhoDaTabela = dic_DadosPorMunicipio.fieldnames

    emptyCityDictionaries = createEmptyCityInfoDictionary()
    dadosDeTodasAsCidades = []

    # Transformar os dados em CSV em dados em JSON
    for municipio in dic_DadosPorMunicipio:
        # vou iterando. Para cada registro, atualizo o registro correspondente em
        # emptyCityDictionaries para os valores de incidencia, obitos, confirmados, populacao
        if municipio[uglifyHeaderItem('city')] == "PIAUÍ":
            piaui = {"city": municipio[uglifyHeaderItem('city')], 
                    "confirmed": municipio[uglifyHeaderItem('confirmed')], 
                    "deaths": municipio[uglifyHeaderItem('deaths')], 
                    "incidence": municipio[uglifyHeaderItem('incidence')],
                    "population": municipio[uglifyHeaderItem('population')]
            }
            break
        cep = municipio['CEP']
        for item in municipio.keys():
            if item in ['Confirmados', 'Óbitos', 'Incidência', 'População']:
                emptyCityDictionaries.get(cep)[beautifyHeaderItem(item)] = municipio[item]
        
    for item in emptyCityDictionaries.values():
        dadosDeTodasAsCidades.append(item)
    dadosDeTodasAsCidades.append(piaui)

    jsonFinal = json.dumps(dadosDeTodasAsCidades, ensure_ascii=False)

    return jsonFinal

###############################
# SAVE
###

# Salva JSON final em arquivo


def saveData(data, filename='../data/1970-01-01.json'):
    arquivo = open(filename, 'x')
    arquivo.write(data)
    arquivo.close()
    return True

###############################
# LOAD SAVED DATA
###


def loadLocalData():
    ld = os.listdir(data_path)
    lista_de_datas = [dt.fromisoformat(arquivo.replace('.json', '')) for arquivo in os.listdir(data_path)]
    fileName = max(lista_de_datas).isoformat() + '.json' 
    arquivo = open(data_path + '/' + fileName, 'r')
    data = arquivo.read()
    arquivo.close()
    return data


###############################
# UPDATES
###
def checkUpdates():
    req = request.urlopen(
        'https://docs.google.com/spreadsheets/d/1b-GkDhhxJIwWcA6tk3z4eX58f-f1w2TA2f2XrI4XB1w/edit#gid=1514947706')

    DateOfUpdateText = ''
    for i in req:
        DateOfUpdateText = DateOfUpdateText + i.decode('utf-8')

    startPosition = DateOfUpdateText.find('Atualização')
    endPosition = startPosition + 32

    dateAndTime = DateOfUpdateText[startPosition:endPosition]

    dayStartPosition = startPosition + 13
    dayEndPosition = dayStartPosition + 10
    date = DateOfUpdateText[dayStartPosition:dayEndPosition]
    dashSeparatedDate = date.replace('/', '-')

    year = dashSeparatedDate[6:10]
    month = dashSeparatedDate[3:5]
    day = dashSeparatedDate[0:2]

    isoFormattedDate = year + '-' + month + '-' + day

    hourStartPosition = dayEndPosition + 4
    hourEndPosition = hourStartPosition + 5
    hour = DateOfUpdateText[hourStartPosition:hourEndPosition]
    dashSeparatedHour = hour.replace('h', '-')

    lastUpdate = dt.fromisoformat(isoFormattedDate)

    # comparar com a data representada pelo nome do arquivo local
    # descobrir qual a data representada pelo nome do arquivo local
    # localizar arquivo local e ler o seu nome
    lista_de_datas = [dt.fromisoformat(arquivo.replace('.json', '')) for arquivo in os.listdir(data_path)]
    # Pegando a maior data 
    
    localFileCreationDate = max(lista_de_datas)

    # transformar essa informação em uma data
    # se o lastUpdate for maior que o arquivo local, atualiza
    # comparar lastUpdate com o nome do arquivo local
    if (localFileCreationDate - lastUpdate).days != 0:
        data = fetchData()
        saveData(data, data_path + '/' + isoFormattedDate + '.json')
        return True
    else:
        return False