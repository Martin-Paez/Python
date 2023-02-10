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
http.open("GET", "http://localhost/recorridos8.json", true);
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
var poligonoZonificador;
var globales  = { 
    markers : [],
    polygonLocations : [],
    polygonMarkers : []
};
var asignaciones = [];
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

    poligonoZonificador = new google.maps.Polygon( { 
        paths: globales.polygonLocations,
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#efe653',
        fillOpacity: 0.35,
        editable: true,
        map: map 
    });

    google.maps.event.addListener(map, 'click', function (e) {
        var position = e.latLng;
        globales.polygonLocations.push(position);
        globales.polygonMarkers.push(new google.maps.Marker({
            icon: 'https://maps.gstatic.com/intl/en_ALL/mapfiles/markers2/measle.png',
            position: position,
            map: map
        }));
        drawPolygon(globales.polygonLocations);
    });
}

function drawPolygon(points) {
    if (points.length < 3) {
        return;
    }
    // first delete the previous polygon
    if (poligonoZonificador) {
      poligonoZonificador.setMap(null);
    }
    // @see https://developers.google.com/maps/documentation/javascript/examples/polygon-simple
    poligonoZonificador = new google.maps.Polygon({
        paths: points,
        strokeColor: '#FF0000',
        strokeOpacity: 1,
        strokeWeight: 4,
        fillColor: '#efe653',
        fillOpacity: 0.35,
        editable: true,
        map: map
    });
  
    var place_polygon_path = poligonoZonificador.getPath();
    google.maps.event.addListener(place_polygon_path, 'set_at', polygonChanged);
    google.maps.event.addListener(place_polygon_path, 'insert_at', polygonChanged);
    displaySelectedMarkers(poligonoZonificador);
}

function polygonChanged() {
    displaySelectedMarkers(poligonoZonificador);
}

function displaySelectedMarkers(polygon) {
    // empty the input
    asignaciones = [];
    for (var i in globales.markers) {
        // @see https://developers.google.com/maps/documentation/javascript/examples/poly-containsLocation
        if (google.maps.geometry.poly.containsLocation(globales.markers[i].position, polygon)) {
  
            if (globales.markers[i].visible) {
              globales.markers[i].setIcon(new google.maps.MarkerImage("https://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|EF2A00"));
              AddAsignacionesSiNoExiste(globales.markers[i]);
              document.getElementById("mensaje").outerHTML = "<div id='mensaje'><h3>" + asignaciones.length + " seleccionados</h3></div>"
            }
        }
      else {
          globales.markers[i].setIcon(getPinIcon(globales.markers[i].zona,globales.markers[i].estado))
        }    
    }
}


function getById(id) { 
    return document.getElementById(id);
}