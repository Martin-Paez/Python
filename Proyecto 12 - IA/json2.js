/* 
 * data = JSON
 * Se copia y pega el JSON  ( generado con IA ) porque un objeto de JS es igual a un JSON
 *
 * data = { "records": [ envios ] }
 * envio = { direccion, chofer }
 * direccion =  x: latitud , y: longitud 
 * chofer = prediccion con IA = codigo del chofer
 * 
 */
var data;
var http = new XMLHttpRequest();
http.open("GET", "http://localhost/x_y_nDriver_date_day_balanced.json", true);
http.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200)
    data = JSON.parse(this.responseText);
};
http.send();


// Esqueleto del algoritmo acoplado al html y al json (obj de js)

window.addEventListener("load", function() {
    // Parseo y ordeno datos
    var dots = _parseLocations(data['records']);
    var sorted = sortedList(dots);

    // Listo los choferes y las cantidades de envios por chofer
    var select = getById("drivers");
    _initSelect(select, sorted);
    _initTextArea(getById("drivers_nDot_list"), sorted);

    // Muestro los detalles del chofer seleccionado
    var label_n_dots = getById("label_n_dots");
    var mapContainer = getById("map"); 
    _loadSelection(dots[select.value], label_n_dots, mapContainer);

    // Agrego un listener para que se modifiquen los datos al seleccionar otro chofer
    select.addEventListener('change', function() {
        _loadSelection(dots[select.value], label_n_dots, mapContainer);
    });
});


// Funciones del back: desacopladas del html pero acopladas al algoritmo

function _parseLocations(locations) {
    var dots = {};
    for(x in locations) {
        let pred = locations[x]["prediction"];
        let pos = { lat: parseFloat(locations[x]["x"]),
                    lng:  parseFloat(locations[x]["y"]) };
        if (dots[pred] === undefined)
            dots[pred] = [];
        dots[pred].push(pos);
    }   
    return dots;
}

function _initSelect(select, sorted) {
    for (let p of sorted)
        addToSelect(select, p[0]);
}

function _loadSelection(dots, input, mapContainer) {
    input.value = dots.length;
    initMap(dots, mapContainer);
}

function _initTextArea(textarea, sorted) {
    var s = "Dot = Cod \n";
    var lines = 1;
    for(let [cod, dots] of sorted) {
        s += dots.length + " = " + cod + " \n";
        lines++;
    }
    textarea.innerHTML = s.trim();
    textarea.style.height = lines + "rem";
}


// Funciones reutilizables 

function sortedList(obj) {
    return Object.entries(obj).sort(function(a, b) {
        return b[1].length - a[1].length;
    });
}

function addToSelect(select, e) {
    const option = document.createElement("option");
    option.value = e;
    option.text = e;
    select.appendChild(option);
}

var map; 
function initMap(dots, container) {
    if (dots === undefined)
        return;

    const mapOptions = {
        zoom: 10,
        center: { lat: -34.640211, lng: -58.480778}
    };
    var map = new google.maps.Map(container, mapOptions);

    const redIcon = 'https://maps.google.com/mapfiles/ms/icons/red-dot.png';
    const greenIcon = 'https://maps.google.com/mapfiles/ms/icons/green-dot.png';
    
    var icon = redIcon;
    for(let pos of dots) {
        icon = greenIcon;
        const marker = new google.maps.Marker({
            position: pos,
            icon: { url: icon },
            map: map
        });
    }
}

function getById(id) { 
    return document.getElementById(id);
}