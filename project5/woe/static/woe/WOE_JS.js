function toggle_visibility(element, force) {
    if (element.hidden == false || force == false) {
        element.hidden = true;
    } else {
        element.hidden = false;
    }
}
 
function create_graph() {
    drop1 = document.getElementById("dropdown_ex1");
    drop2 = document.getElementById("dropdown_ex2");
        
    const xyValues = [
      {x:5, y:1},
      {x:6, y:1},
      {x:7, y:2},
      {x:8, y:3},
      {x:9, y:5},
      {x:10, y:8},
      {x:11, y:13},
      {x:12, y:21},
      {x:13, y:34},
      {x:14, y:55},
      {x:15, y:89}
    ];

    const xyValues2 = [
      {x:5, y:89},
      {x:6, y:55},
      {x:7, y:34},
      {x:8, y:21},
      {x:9, y:13},
      {x:10, y:8},
      {x:11, y:5},
      {x:12, y:3},
      {x:13, y:2},
      {x:14, y:1},
      {x:15, y:1}
    ];

    new Chart("chart_ex", {
      type: "scatter",
      data: {
        datasets: [{
          pointRadius: drop1.value,
          pointBackgroundColor: "rgba(0,150,200,1)",
          data: xyValues
        },{
          pointRadius: drop2.value,
          pointBackgroundColor: "rgba(0,200,150,1)",
          data: xyValues2
        }]
      },
      options:{}
    });
};

function doStuff() {
    graphSpace = document.getElementById("graph_space");
    toggle_visibility(graphSpace);
    create_graph();
};

function show_selected(element) {
    console.log(element.value, "selected");
};

function do_ajax(dropdown, div_id) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
    if (this.readyState === 4 && this.status === 200) {
        document.getElementById(div_id).innerHTML = '' + this.responseText;
    }
    };
    //xhttp.open("GET", "table_data.html", true);
    let resource = '/table_data?limit=1&wmo=' + dropdown.value;
    xhttp.open('GET', resource, true);
    xhttp.send();
}

document.addEventListener("DOMContentLoaded", (event)=>{
    do_ajax(document.getElementById('location_select'), 'ajax_example');
});

function show_hide_divs(dropdown) {
    let div_list = document.getElementsByClassName(dropdown.value);
    for (item in div_list) {
        toggle_visibility(item, item.id === dropdown.value)
    }
}