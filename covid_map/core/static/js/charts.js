var ctx = document.getElementById('casosConfirmados').getContext('2d');
var colorsPrimary = []
var colorsBorder = []
datasCasos.forEach(element => {
    colorsPrimary.push('rgba(0, 150, 136, 0.5)')
    colorsBorder.push('rgba(181, 14, 14, 1)')
});
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: datasCasos,
        datasets: [{
            label: 'Casos confirmados',
            data: valoresCasos,
            backgroundColor: colorsPrimary,
            borderColor: colorsBorder,
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