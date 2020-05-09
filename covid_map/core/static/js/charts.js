var ctx = document.getElementById('casosConfirmados').getContext('2d');
var colorsPrimary1 = []
var colorsBorder1 = []
datasCasos.forEach(element => {
    colorsPrimary1.push('rgba(0, 150, 136, 0.5)')
    colorsBorder1.push('rgba(181, 14, 14, 1)')
});
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: datasCasos,
        datasets: [{
            label: 'Casos confirmados',
            data: valoresCasos,
            backgroundColor: colorsPrimary1,
            borderColor: colorsBorder1,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Data'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Casos'
                }
            }]
        }
    }
});


var ctx2 = document.getElementById('historicoMortes').getContext('2d');
var colorsPrimary2 = []
var colorsBorder2 = []
datasHistMortes.forEach(element => {
    colorsPrimary2.push('rgba(244, 67, 54, 0.5)')
    colorsBorder2.push('rgba(183, 28, 28, 1)')
});
var myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: datasHistMortes,
        datasets: [{
            label: 'Óbitos',
            data: valoresHistMortes,
            backgroundColor: colorsPrimary2,
            borderColor: colorsBorder2,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Data'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Mortes'
                }
            }]
        }
    }
});


var ctx3 = document.getElementById('novosCasos').getContext('2d');
var colorsPrimary3 = []
var colorsBorder3 = []
datasNovosCasos.forEach(element => {
    colorsPrimary3.push('rgba(0, 150, 136, 0.5)')
    colorsBorder3.push('rgba(181, 14, 14, 1)')
});
var myChart3 = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: datasNovosCasos,
        datasets: [{
            label: 'Novos casos por dia',
            data: valoresNovosCasos,
            backgroundColor: colorsPrimary3,
            borderColor: colorsBorder3,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Data'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Casos'
                }
            }]
        }
    }
});
