	$(document).ready(function googleMap(lat, lon) {
		var mapProp= {
			center:new google.maps.LatLng(10,10),
			zoom:5,
		};
		var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
	});