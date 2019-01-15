

window.onload = function(){

    var barOptions_stacked = {
        tooltips: {
            enabled: false
        },
        hover :{
            animationDuration:0
        },
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero:true,
                    fontFamily: "'Open Sans Bold', sans-serif",
                    fontSize:11
                },
                scaleLabel:{
                    display:false
                },
                gridLines: {
                }, 
                stacked: true
            }],
            yAxes: [{
                gridLines: {
                    display:false,
                    color: "#fff",
                    zeroLineColor: "#fff",
                    zeroLineWidth: 0,
                },
                ticks: {
                    fontFamily: "'Open Sans Bold', sans-serif",
                    fontSize:11,
                    max:100,
                    min:0
                },
                stacked: true
            }]
        },
        legend:{
            display:false
        },
        
        animation: {
            onComplete: function () {
                var chartInstance = this.chart;
                var ctx = chartInstance.ctx;
                ctx.textAlign = "left";
                ctx.font = "9px Open Sans";
                ctx.fillStyle = "#fff";
    
                Chart.helpers.each(this.data.datasets.forEach(function (dataset, i) {
                    var meta = chartInstance.controller.getDatasetMeta(i);
                    Chart.helpers.each(meta.data.forEach(function (bar, index) {
                        data = dataset.data[index];
                        if(i==0){
                            ctx.fillText(data, 50, bar._model.y+4);
                        } else {
                            ctx.fillText(data, bar._model.x-25, bar._model.y+4);
                        }
                    }),this)
                }),this);
            }
        },
        pointLabelFontFamily : "Quadon Extra Bold",
        scaleFontFamily : "Quadon Extra Bold",
    };

    var optionDougnout = {
        responsive:true,
        animateRotate : true,
        animateScale: true,
        legend: {
            position: 'right' // place legend on the right side of chart
        },
    }

    var verticalTes = {
        responsive: true,
        legend: {
           position: 'center' // place legend on the right side of chart
        },
        scales: {
           xAxes: [{
              stacked: true // this should be set to make the bars stacked
           }],
           yAxes: [{
              stacked: true // this also..
           }]
        }
     }

     var lineBarOption = {
        responsive:true,
        showXLabels:10,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{
                ticks: {
                  // Make labels vertical
                  // https://stackoverflow.com/questions/28031873/make-x-label-horizontal-in-chartjs
                  minRotation: 90,
        
                  // Limit number of labels
                  // https://stackoverflow.com/questions/22064577/limit-labels-number-on-chartjs-line-chart
                  autoSkip: true,
                  maxTicksLimit: 10
                }
            }]
        },
        legend: {
            display: true,
            position: 'top',
            labels: {
              boxWidth: 80,
              fontColor: 'black'
            }
        }
     }

    var title_pertanyaan_f8 = [];
    var element_list_pertanyaan_f8 = [];

    for (var i = 0; i < pembeljaran.length; i++){
        title_pertanyaan_f8.push(pembeljaran[i]['title'])

        for (var k = 0 ; k < pembeljaran[i]['element'].length; k++){
            element_list_pertanyaan_f8.push(pembeljaran[i]['element'][k]);
        }
    }

    //console.log(pembeljaran)
    //console.log(element_list_pertanyaan_f8)

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: title_pertanyaan_f8,
            datasets: element_list_pertanyaan_f8
        },

        // Configuration options go here
        options: verticalTes
    });
    
    
    /*

    var ctx_9 = document.getElementById('chart_9');
    var myDoughnutChart = new Chart(ctx_9, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [pertanyaan_f9()[0]['responden'], pertanyaan_f9()[1]['responden']],
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    // '#fccd56'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                pertanyaan_f9()[0]['title'],
                pertanyaan_f9()[1]['title'],
            ]
        },
        options: optionDougnout
    });
    */

    var title_10 = [];
    var value_10 = [];

    for (var i = 0; i < pertanyaan_f10().length; i++){
        title_10.push(pertanyaan_f10()[i]['jawaban'])
        value_10.push(pertanyaan_f10()[i]['total'])
    }

    var ctx_10 = document.getElementById('chart_line_10');
    var myLineChart_10 = new Chart(ctx_10, {
        type: 'line',
        data: {
            labels: title_10,
            datasets:[{
                label:'total price',
                data: value_10,
                lineTension: 0,
                fill: false,
                borderColor: 'orange',
                pointBorderColor: 'orange',
                pointBackgroundColor: 'rgba(255,150,0,0.5)',
                pointRadius: 5,
                pointHoverRadius: 10,
                pointHitRadius: 30,
                pointBorderWidth: 2,
                pointStyle: 'rectRounded'
            }]
        },
        options:lineBarOption
    });


    var ctx_14 = document.getElementById('chart_line_14');
    var myDoughnutChart_14 = new Chart(ctx_14, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [pertanyaan_f14()[0]['total'], pertanyaan_f14()[1]['total']],
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    // '#fccd56'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                pertanyaan_f14()[0]['jawaban'],
                pertanyaan_f14()[1]['jawaban'],
            ]
        },
        options: optionDougnout
    });
    
    var lable_f15 = [];
    var value_f15 = [];

    for(var i =0; i < pertanyaa_f15().length; i++){
        lable_f15.push(pertanyaa_f15()[i]['jawaban']);
        value_f15.push(pertanyaa_f15()[i]['total'])
    } 

    
    var ctx_15 = document.getElementById('chart_line_15');
    var myDoughnutChart_15 = new Chart(ctx_15, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_f15,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: lable_f15
        },
        options: optionDougnout
    });
    
    var title_f16 = [];
    var value_f16 = [];

    for (var i = 0; i < pertanyaan_16().length; i++){
        title_f16.push(pertanyaan_16()[i]['jawaban']);
        value_f16.push(pertanyaan_16()[i]['total'])
    }

    var ctx_16 = document.getElementById('chart_line_16');
    var myDoughnutChart_15 = new Chart(ctx_16, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_f16,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_f16
        },
        options: optionDougnout
    });

    var title_f17 = [];
    var value_f17 = [];
    
    for (var i = 0; i < pertanyaan_17().length; i++){
        title_f17.push(pertanyaan_17()[i]['jawaban']);
        value_f17.push(pertanyaan_17()[i]['total']);
    }

    var ctx_17 = document.getElementById('chart_line_17');
    var myDoughnutChart_15 = new Chart(ctx_17, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_f17,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_f17
        },
        options: optionDougnout
    });

    var title_f18 = [];
    var value_f18 = [];

    for (var i = 0; i < pertanyaan_18().length; i++){
        title_f18.push(pertanyaan_18()[i]['jawaban']);
        value_f18.push(pertanyaan_18()[i]['avg'])
    }

    var ctx_18 = document.getElementById('chart_line_18');
    var myDoughnutChart_15 = new Chart(ctx_18, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_f18,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_f18
        },
        options: optionDougnout
    });

    var data_f19 = pertanyaan_19();

    var value_f19 = [
        data_f19[0]['sangat_baik'],
        data_f19[0]['baik'],
        data_f19[0]['cukup'],
        data_f19[0]['buruk'],
        data_f19[0]['sangat_buruk'],
    ];

    var barOptions = {
        responsive:true,
        scale:{
            yAxes:[{
                ticks:{
                    beginAtZero:true
                }
            }]
        }
    };
    
    var ctx_19 = document.getElementById('chart_line_19').getContext("2d");
    var myChart = new Chart(ctx_19, {
        type: 'bar',
        data: {
            labels: ["Sangat Baik", "Baik", "Cukup", "Buruk", "Sangat Buruk"],
            datasets: [{
                label: 'total',
                data: value_f19,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive:true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });


    var ctx_18 = document.getElementById('chart_line_18');
    var myDoughnutChart_15 = new Chart(ctx_18, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_f18,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_f18
        },
        options: optionDougnout
    });

    

    var title_pertanyaan_20 = [];
    var value_pertanyaan_20 = [];

    for (var i =0 ; i < pertanyaan_20().length; i++){
        title_pertanyaan_20.push(pertanyaan_20()[i]['jawaban']);
        value_pertanyaan_20.push(pertanyaan_20()[i]['total']);
    }

    console.log(title_pertanyaan_20)
    console.log(value_pertanyaan_20)


    var ctx_20 = document.getElementById('chart_line_20');
    var myDoughnutChart_15 = new Chart(ctx_20, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_pertanyaan_20,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_pertanyaan_20
        },
        options: optionDougnout
    });

    console.log(pertanyaan_21())

    var title_21 = [];
    var value_21 = [];

    for (var i = 0 ; i < pertanyaan_21().length; i++){
        title_21.push(pertanyaan_21()[i]['jawaban'])
        value_21.push(pertanyaan_21()[i]['total'])
    }

    var ctx_20 = document.getElementById('chart_line_21');
    var myDoughnutChart_15 = new Chart(ctx_20, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: value_21,
                backgroundColor:[
                    '#f15e83',
                    '#46BFBD',
                    '#fccd56',
                    '#37474F',
                    '#7E57C2'
                ]
            }],
        
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: title_21
        },
        options: optionDougnout
    });


    var option_stack_bar = {
        tooltips: {
          displayColors: true,
          callbacks:{
            mode: 'x',
          },
        },
        scales: {
          xAxes: [{
            stacked: true,
            gridLines: {
              display: false,
            }
          }],
          yAxes: [{
            stacked: true,
            display:true,
            ticks: {
              beginAtZero: true,
              max:100,
              min:0
            },
            type: 'linear',
          }]
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: { position: 'bottom' },
    }
    
    var title_22 = ['sangat buruk', 'buruk', 'cukup', 'baik', 'sangat baik'];

    var data_value = [];


    console.log(pertanyaan_22())

    for (var i = 0; i < pertanyaan_22().length; i++){
        var data_object = new Object();

        data_object.label = pertanyaan_22()[i]['jawaban'];
        data_object.data = [
            pertanyaan_22()[i]['sangat_buruk'],
            pertanyaan_22()[i]['buruk'],
            pertanyaan_22()[i]['cukup'],
            pertanyaan_22()[i]['baik'],
            pertanyaan_22()[i]['sangat_baik']
        ]

        data_value.push(data_object)
    }

    console.log('tes data 22 ? ',data_value)

    var ctx_22 = document.getElementById('chart_line_22');
    var chart = new Chart(ctx_22, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: title_22,
            datasets: data_value
        },

        // Configuration options go here
        options: option_stack_bar
    });

    //console.log(pertanyaan_23());

    var title_23 = ['sangat buruk', 'buruk', 'cukup', 'baik', 'sangat baik'];

    var data_value_23 = [];

    for (var i = 0; i < pertanyaan_23().length; i++){
        var data_object = new Object();

        data_object.label = pertanyaan_23()[i]['jawaban'];
        data_object.data = [
            pertanyaan_23()[i]['sangat_buruk'],
            pertanyaan_23()[i]['buruk'],
            pertanyaan_23()[i]['cukup'],
            pertanyaan_23()[i]['baik'],
            pertanyaan_23()[i]['sangat_baik']
        ]

        data_value_23.push(data_object)
    }

    var ctx_23 = document.getElementById('chart_line_23');
    var chart = new Chart(ctx_23, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: title_23,
            datasets: data_value_23
        },

        // Configuration options go here
        options: option_stack_bar
    });

    

    
}