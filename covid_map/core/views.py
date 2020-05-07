from django.shortcuts import render, redirect
from .models import CasosPorCidadePiaui

# Create your views here.

def index(requests):
    base = {
        'casos_por_cidades': CasosPorCidadePiaui.objects.all()
    }
    base['soma_obitos_por_cidade'] = sum([cidade.obitos for cidade in base['casos_por_cidades']])
    base['soma_casos_por_cidade'] = sum([cidade.casos for cidade in base['casos_por_cidades']])
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
    CasosPorCidadePiaui.objects.bulk_create(book)
    return redirect('index')


def upload(request):
    return render(request, 'importar_csv.html')