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

###############################
### FETCH
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

    dadosDeTodasAsCidades = []

    # Transformar os dados em CSV em dados em JSON
    for municipio in dic_DadosPorMunicipio:
        dadosDoMunicipio = {}
        for item in cabecalhoDaTabela:
            dadosDoMunicipio[item] = municipio[item]
        dadosDeTodasAsCidades.append(dadosDoMunicipio)

    jsonFinal = json.dumps(dadosDeTodasAsCidades, ensure_ascii= False)

    return jsonFinal

###############################
### SAVE
###

# Salva JSON final em arquivo
def saveData(data, filename = '../data/1970-01-01.json'):
    arquivo = open(filename, 'x')
    arquivo.write(data)
    arquivo.close()
    return True

###############################
### LOAD
###

def loadLocalData():
    ld = os.listdir('core/data/')
    fileName = ld[0]
    arquivo = open('core/data/' + fileName, 'r')
    data = arquivo.read()
    arquivo.close()
    return data

def checkUpdates():
    req = request.urlopen('https://docs.google.com/spreadsheets/d/1b-GkDhhxJIwWcA6tk3z4eX58f-f1w2TA2f2XrI4XB1w/edit#gid=1514947706')

    updateText = ''
    for i in req:
        updateText = updateText + i.decode('utf-8')

    posicaoInicial = updateText.find('Atualização')
    posicaoFinal = posicaoInicial + 32

    dateAndTime = updateText[posicaoInicial:posicaoFinal]

    posicaoInicialDoDia = posicaoInicial + 13
    posicaoFinalDoDia = posicaoInicialDoDia + 10
    date = updateText[posicaoInicialDoDia:posicaoFinalDoDia]
    dashSeparatedDate = date.replace('/', '-')

    year = dashSeparatedDate[6:10]
    month = dashSeparatedDate[3:5]
    day = dashSeparatedDate[0:2]

    isoFormattedDate = year + '-' + month + '-' + day

    posicaoInicialDaHora = posicaoFinalDoDia + 4
    posicaoFinalDaHora = posicaoInicialDaHora + 5
    hour = updateText[posicaoInicialDaHora:posicaoFinalDaHora]
    dashSeparatedHour = hour.replace('h', '-')

    last_update = dt.fromisoformat(isoFormattedDate)

    # comparar com a data representada pelo nome do arquivo local
    ### descobrir qual a data representada pelo nome do arquivo local
    ##### localizar arquivo local e ler o seu nome
    ld = os.listdir('core/data')
    print(os.curdir)
    fileName = ld[0]
    dateOfFile = fileName[0:10]
    localFileCreationDate = dt.fromisoformat(dateOfFile)

    ######## transformar essa informação em uma data
    # se o last_update for maior que o arquivo local, atualiza
    ### comparar last_update com o nome do arquivo local
    if (localFileCreationDate - last_update).days > 0:
        data = fetchData()
        saveData(data, 'core/data/' + isoFormattedDate + '.json')
        return True
    else:
        return False