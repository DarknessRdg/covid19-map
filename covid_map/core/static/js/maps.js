Highcharts.getJSON('https://raw.githubusercontent.com/IFPiaui/covid19-map/master/static_jsons/limites.json', function (geojson) {
    Highcharts.mapChart('mapaPiaui', {
        chart: {
            map: geojson
        },

        title: {
            text: 'Casos COVID-19 no Piauí'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0,
            stops: [[0, '#009688'], [0.001, '#ff6257'],[0.018, '#f44336'], [1, '#611b14']],
        },

        series: [{
            data: dataMapPiaui,
            keys: ['id', 'value'],
            joinBy: 'id',
            name: 'Confirmados',
            states: {
                hover: {
                    color: '#a4edba'
                }
            },
            dataLabels: {
                format: '{point.name}',
            }
        }]
    });
});