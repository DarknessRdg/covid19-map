from django.shortcuts import render, redirect
from .models import CasosPorCidadePiaui
import json
import requests
from datetime import date

# Create your views here.

def casos_confirmados():
    rq = requests.get('http://coronavirus.pi.gov.br/public/api/casos/confirmados.json')
    dados = json.loads(rq.text)
    base = []
    for dado in dados:
        base.append([date(int(dado['data'][:4:]), int(dado['data'][5:7:]), int(dado['data'][8:10:])), dado['quantidade']])
    return base


def historico_mortes():
    rq = requests.get('http://coronavirus.pi.gov.br/public/api/casos/obitos.json')
    dados = json.loads(rq.text)
    base = []
    for dado in dados:
        base.append([date(int(dado['data'][:4:]), int(dado['data'][5:7:]), int(dado['data'][8:10:])), dado['quantidade']])
    return base


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


def upload(request):
    return render(request, 'importar_csv.html')