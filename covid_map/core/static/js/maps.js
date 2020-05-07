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
            stops: [[0, '#009688'],
            [0.001, '#f5554a'],
            [0.0018, '#f44336'],
            [0.01, '#f6685e'],
            [0.03, '#f44336'],
            [0.06, '#db3c30'],
            [0.09, '#c3352b'],
            [0.3, '#aa2e25'],
            [0.6, '#922820'],
            [0.9, '#7a211b'],
            [1, '#3a100c']],
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