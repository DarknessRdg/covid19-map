from django.shortcuts import render, redirect
from .models import CasosPorCidadePiaui
import json
import requests
from datetime import date


def get_request_data(url):
    response = requests.get('http://coronavirus.pi.gov.br/public/api/casos/confirmados.json')
    response = json.loads(response.text)

    data_parsed = []
    for data in response:
        parsed = date(int(data['data'][:4:]), int(data['data'][5:7:]), int(data['data'][8:10:])), data['quantidade']
        data_parsed.append(parsed)
    return data_parsed


def casos_confirmados():
    url = 'http://coronavirus.pi.gov.br/public/api/casos/confirmados.json'
    return get_request_data(url)


def historico_mortes():
    url = 'http://coronavirus.pi.gov.br/public/api/casos/obitos.json'
    return get_request_data(url)



def index(requests):
    base = {
        'casos_por_cidades': CasosPorCidadePiaui.objects.all()
    }
    base['soma_obitos_por_cidade'] = sum([cidade.obitos for cidade in base['casos_por_cidades']])
    base['soma_casos_por_cidade'] = sum([cidade.casos for cidade in base['casos_por_cidades']])
    base['casosConfirmados'] = casos_confirmados()
    base['historicoMortes'] = historico_mortes()
    return render(requests, 'index.html', base)


def importar(request):
    file = request.FILES['arquivo'].read().decode('utf-8')
    cidades = file.replace("\r","").split("\n")
    book = []
    for linha in cidades:
        try:
            nome, idibge, casos, mortes = linha.split(',')
            book.append(CasosPorCidadePiaui(name=nome, idIBGE=idibge, casos=casos, obitos=mortes))
        except ValueError:
            pass
    if len(CasosPorCidadePiaui.objects.all()) == 0:
        CasosPorCidadePiaui.objects.bulk_create(book)
    else:
        CasosPorCidadePiaui.objects.bulk_update(book, fields=['casos', 'obitos'])
    return redirect('index')
