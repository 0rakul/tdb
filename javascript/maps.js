function initMap() {
    //Maps
    var latlng = new google.maps.LatLng(47, 19);
    var myOptions = {
	zoom: 14,
	center: latlng,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    
    var map = new google.maps.Map(document.getElementById("map_canvas"),
				  myOptions);
    map.setCenter(47, 19);
    var marker = new google.maps.Marker({
					    position: new google.maps.LatLng(47,19),
					    map: map,
					    title: "Hello"
					});
    
}

