var temperature = document.getElementById('temperature');
var apikey = document.getElementById('apikey').value ;
var devicename = "dev1";
var led_status=0
function getdevice(){

    setTimeout(getdevice, 2000);
    var requests = $.get('/api/temperatura');
    
    var tm = requests.done(function (result){
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        addData(temp_chart, time, result['temperatura']);
        document.getElementById("card-temp").innerHTML = result['temperatura'];
        if (couter >= 20 ){
            removeData(temp_chart);
        }
        couter++;
        //setTimeout(getdevice, 2000);
    });

    var requests = $.get('/api/humedad');
    
    var tm = requests.done(function (result){
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        addData(humid_chart, time, result['humedad']);
        document.getElementById("card-humidity").innerHTML = result['humedad'];
        if (couter >= 20 ){
            removeData(humid_chart);
        }
        couter++;
    });

    var requests = $.get('/api/intruso');
    
    var tm = requests.done(function (result){
        document.getElementById("card-instruso").innerHTML = result['intruso'];
    });

    var requests = $.get('/api/ledhab');
    requests.done(function (result){
        
        var status=result['ledhab']
        if(led_status!=status)
        {
            var btn=document.getElementById("btn-ledhab")
            if (status){
                btn.className="w3-button w3-red w3-large w3-round-large"
                btn.innerHTML="Apagar luz de la habitación"
            }else{
                btn.className="w3-button w3-green w3-large w3-round-large"
                btn.innerHTML="Prender luz de la habitación"
            }
            led_status=status
        }

    });
    
}

function cambiarValor(){
    var requests = $.get('/api/accion/ledhab');
}

var btn=document.getElementById("btn-ledhab")
btn.onclick = cambiarValor

//temperature chart object created 
var temp_chart = new Chart(temperature, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(244, 67, 54, 0.1)',
            borderColor:'rgba(244, 67, 54, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var humidity = document.getElementById('humidity');
var humid_chart = new Chart(humidity, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(33, 150, 243, 0.1)',
            borderColor:'rgba(33, 150, 243, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
/*
var moisture = document.getElementById('moisture');
var moist_chart = new Chart(moisture, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Moisture W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(0, 150, 136, 0.1)',
            borderColor:'rgba(0, 150, 136, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
*/
/*
var light = document.getElementById('light');
var light_chart = new Chart(light, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Light W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(255, 152, 0, 0.1)',
            borderColor:'rgba(255, 152, 0, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

*/
function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

var couter = 0; 

getdevice();
//setTimeout(getdevice, 1000);