

window.onload = function(){

    // alert(labels)

    var ctx = document.getElementById("study");

    var study = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: labels,
        
        datasets: [{
            label: '# of Votes',
            data: data,
            backgroundColor: [
                '#FFEA00',
                '#212121',
                '#2962FF',
                '#DD2C00'
            ],
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                },
                gridLines:{
                    color: "rgba(0, 0, 0, 0)",
                }

            }],
            xAxes:[{
                barPercentage:0.2,
                gridLines:{
                    color: "rgba(0, 0, 0, 0)",
                }
            }]
        },
        legend:{
            display:true,
            fullWidth:false,
            position:'bottom'            
        }
    }
});

var ctx1 = document.getElementById("dapat_pekerjaan");
var myChart = new Chart(ctx1, {
type: 'doughnut',
data: {
    labels: dapet_pekerjaan_labels,
    
    datasets: [{
        label: '# of Votes',
        data: data_tot_pekerja,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
        ],
        borderWidth: 1
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            },
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }],
        xAxes:[{
            barPercentage:0.2,
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }]
    },
    legend:{
        display:true,
        fullWidth:false,
        position:'bottom'            
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
}
});


var ctx2 = document.getElementById("pekerjaan_pertama");
var myChart = new Chart(ctx2, {
type: 'doughnut',
data: {
    labels: pekerjaan_pertama_labels,
    
    datasets: [{
        label: '# of Votes',
        data: data_pekerjaan_pertama,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)'
        ],
        borderWidth: 1
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            },
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }],
        xAxes:[{
            barPercentage:0.2,
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }]
    },
    legend:{
        display:true,
        fullWidth:false,
        position:'bottom'            
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
}
});

var ctx3 = document.getElementById("penghasilan_pertama");
var myChart = new Chart(ctx3, {
type: 'doughnut',
data: {
    labels: penghasilan_labels,
    
    datasets: [{
        label: '# of Votes',
        data: data_penghasilan_pertama,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',

        ],
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            },
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }],
        xAxes:[{
            barPercentage:0.2,
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }]
    },
    legend:{
        display:true,
        fullWidth:false,
        position:'bottom'            
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
}
});

var ctx4 = document.getElementById("sesuai_pekerjaan");
var myChart = new Chart(ctx4, {
type: 'doughnut',
data: {
    labels:sesuai_labels,
    
    datasets: [{
        label: 'Hallo World',
        data: data_sesuai,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
        ],
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            },
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }],
        xAxes:[{
            barPercentage:0.2,
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }]
    },
    legend:{
        display:true,
        fullWidth:false,
        position:'bottom'            
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
}
});

var ctx5 = document.getElementById("ipk_kelulusan");
var myChart = new Chart(ctx5, {
type: 'doughnut',
data: {
    labels: ipk_label,
    datasets: [{
        label: '# of Votes',
        data: data_ipk,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
        ],
        borderWidth: 1
    }]
},
options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            },
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }],
        xAxes:[{
            barPercentage:0.2,
            gridLines:{
                color: "rgba(0, 0, 0, 0)",
            }
        }]
    },
    legend:{
        display:true,
        fullWidth:false,
        position:'bottom'            
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
}
});

}