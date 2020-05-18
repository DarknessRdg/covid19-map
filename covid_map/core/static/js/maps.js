Highcharts.getJSON('https://raw.githubusercontent.com/IFPiaui/covid19-map/master/static_jsons/malha.geojson', function (geojson) {
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
            stops: [[0, '#e0f2f1'], [0.001, '#b2dfdb'],[0.018, '#80cbc4'], [0.1, '#4db6ac'],
            [0.15, '#26a69a'], [0.2, '#009688'], [0.4, '#00897b'], [0.6, '#00897b'], [0.8, '#00897b'],
            [1, '#00897b']],
        },

        series: [{
            data: dataMapPiaui,
            keys: ['codarea', 'value'],
            joinBy: 'codarea',
            name: 'Confirmados',
            states: {
                hover: {
                    color: '#a4edba'
                }
            },
            dataLabels: {
                format: '{point.name}',
            }
        }],

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom',
                        layout: 'horizontal'
                    }
                }
            }]
        }

    });
});


Highcharts.mapChart('mapaBrasil', {
    chart: {
      map: 'countries/br/br-all'
    },
  
    title: {
      text: 'Casos por estado'
    },
  
    subtitle: {
      text: 'Casos com base na última atualização dos estados'
    },
  
    mapNavigation: {
      enabled: true,
      buttonOptions: {
        verticalAlign: 'bottom'
      }
    },
  
    colorAxis: {
        min: 0,
        stops: [[0, '#e0f2f1'], [0.001, '#b2dfdb'],[0.018, '#80cbc4'], [0.1, '#4db6ac'],
            [0.15, '#26a69a'], [0.2, '#009688'], [0.4, '#00897b'], [0.6, '#00897b'], [0.8, '#00897b'],
            [1, '#00897b']],
    },
  
    series: [{
      data: dataMapBrasil,
      name: 'Confirmados',
      states: {
        hover: {
          color: '#b2dfdb'
        }
      },
      dataLabels: {
        enabled: true,
        format: '{point.name}'
      }
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    align: 'center',
                    verticalAlign: 'bottom',
                    layout: 'horizontal'
                }
            }
        }]
    }

  });