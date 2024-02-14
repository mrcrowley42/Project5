// This function is called to insert mutiple data series in to a line chart
function do_sample_multi_data(element_id){
    let myChart = Chart.getChart(element_id);
    if(myChart != null){
        myChart.destroy();
    }
    let labels = [];
    let series = [];
    for (let item1 in sample_multi_chart_data){
        let location = sample_multi_chart_data[item1].location;
        let wmo_id = sample_multi_chart_data[item1].wmo_id;
        let observations = sample_multi_chart_data[item1].observations;
        let xyValues = [];
        for(let item2 in observations){
            xyValues.push([observations[item2].formatted_datetime, observations[item2].air_temp]);
        }
        //let labelled_data = {location:location, }
        series.push(xyValues)
    }

    const ctx = document.getElementById(element_id);
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
              {
            label: sample_multi_chart_data[0].location,
            data: series[0],
            borderWidth: 1
          },
              {
            label: sample_multi_chart_data[1].location,
            data: series[1],
            borderWidth: 1
          }
          ]
        },
        options: {
          scales: {
              x: {
              beginAtZero: false},
            y: {
              beginAtZero: false
            }
          }
        }});
}
