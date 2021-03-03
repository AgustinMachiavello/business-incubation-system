$(document).ready(function(){
    $('.analytics-loader').each(function(index, currentElement){
        let analyticsHandle = currentElement.dataset.analytichandle;

        var query = window.location.search.substring(1);
        var url = `/analytics/${analyticsHandle}/?${query}`;
        if (analyticsHandle){
            $.ajax({
                type: 'GET',
                url: url,
                data: {},
                success: function (response) {
                    // Set display value
                    $(currentElement).children('.analytics-holder').each(function(i, e){
                        //e.innerHTML = response['value'];
                        console.log(response['value'])
                        if (response['value'] !== null) {
                            e.innerHTML = response['value'];
                        }
                        else {
                            e.classList.add("invisible");
                        } 
                    });
                    // Create display graph
                    $(currentElement).find('.chart-wrapper canvas').each(function(graphIndex, graphElement){
                        let data = response['data'];
                        let labels = response['labels']
                        if (data.length > 1) {
                            let charType = graphElement.dataset.chart;
                            createGraph(graphElement, charType, labels, data);
                        }
                    });
                },
                error: function (response) {
                    console.log('analytics error', response)
                }
            });
        };
    });
});


function createGraph(element, type, labels, data) {
    var ctx = element.getContext('2d');
    var chart = new Chart(ctx, {
    type: `${type}`,
    data: {
        labels: labels,
        datasets: [{
            data: data,
            backgroundColor: 'rgba(0, 123, 255, 0.3)',
            borderColor: 'rgba(0, 123, 255, 1)',
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false,
         },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    stepSize: 10
                }
            }]
        }
    }
    });
}