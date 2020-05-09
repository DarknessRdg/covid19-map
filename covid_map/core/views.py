from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import CasosPorCidadePiaui
from datetime import date
import json
import requests
import contextlib


def get_request_data(url):
    response = requests.get(url)
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


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = CasosPorCidadePiaui.objects.all()

        context['casos_por_cidades'] = queryset
        context['soma_obitos_por_cidade'] = sum([cidade.obitos for cidade in queryset])
        context['soma_casos_por_cidade'] = sum([cidade.casos for cidade in queryset])
        context['casosConfirmados'] = casos_confirmados()
        context['historicoMortes'] = historico_mortes()
        return context


class Upload(TemplateView):
    template_name = 'importar_csv.html'

    def post(self, request):
        file = request.FILES['arquivo'].read().decode('utf-8')
        cidades = file.replace('\r', '').split('\n')
        book = []
        for linha in cidades:
            with contextlib.suppress(ValueError):
                nome, idibge, casos, mortes = linha.split(',')
                book.append(CasosPorCidadePiaui(name=nome, idIBGE=idibge, casos=casos, obitos=mortes))

        if CasosPorCidadePiaui.objects.all().count() == 0:
            CasosPorCidadePiaui.objects.bulk_create(book)
        else:
            CasosPorCidadePiaui.objects.bulk_update(book, fields=['casos', 'obitos'])
        return redirect('index')
