var map;
//We will store the station, latitude longitude pairs here
var stationMarkers = [];
var n = 0;

function init() {
    initMap();
    $('#detail_publish').click(function() {
	    t_name = $('#transport_name').val();
	    times = $('#times').val();
	    stations = parseStations();
	    data = {};
	    data.t_name=t_name;
	    data.times=times;
	    data.stations=stations;
	    stationCoordinates=[];
	    i = 0;
	    for (i = 0; i < n; i++) {
    //for (marker in stationMarkers) {
		marker = stationMarkers[i];
		coordinate = []
		coordinate[0] = marker.b;
		coordinate[1] = marker.c;
		stationCoordinates[i] = coordinate;
		
	    }
	    data.coords=stationCoordinates;
	    $.ajax({
		    url: "/query",
			type: "POST",
			data: JSON.stringify(data),
			dataType: "json",
			contentType: "application/json; charset=utf-8",
			//beforeSend: function() { $("#saveStatus").html("Saving").show(); },
			success: function(result) {
			alert(result.Result);
			//$("#saveStatus").html(result.Result).show();
		    }
		});/**/
	});
    
    
    google.maps.event.addListener(map, 'rightclick', function(event) {
	    placeStation(event.latLng);
	});
}


function placeStation(location) {
    marke = new google.maps.Marker({
	    position: location,
	    map: map,
	    title: "Hello"
	});
    stationMarkers[n] = location;
    $().add('#stops_list').append('<li>asdf</li>');   
    n++;
}
function parseStations() {
    //ez át kell írni hogy csak a stops_list id-n menjen végig
    var stations = [];
    $('li').each( 
		 function (index, Element) {
		     stations[index] = $(Element).text();
		 });
    return stations;
}

function addStation() {
    
}

function initMap() {
    //Maps
    var latlng = new google.maps.LatLng(46, 19);
    var myOptions = {
	zoom: 5,
	center: latlng,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
			      myOptions);

    /*
    marker = new google.maps.Marker({
	    position: new google.maps.LatLng(47,19),
	    map: map,
	    title: "Hello"
	});
    */
    marker.station_index;
    
    
}
