const geolocationAPIKey = 'pk.764b02b9520ce1078da1f83298759512'
// const googleAPIKey = 'AIzaSyDX7nPdvEfWcI6pYl2Qgw3pkO98eWfftc4'
const googleAPIKey = 'AIzaSyDX7nPdvEfWcI6pYl2Qgdsdasfafas4'

const getMissingInfo = async function (coords) {
	const { lat: lat, lng: lng } = coords

	const url = `https://eu1.locationiq.com/v1/reverse?key=${geolocationAPIKey}&lat=${lat}&lon=${lng}&format=json&accept-language=en`

	try {
		const geoLocationResponse = await fetch(url)
		if (!geoLocationResponse.ok) throw new Error('Error getting geolocation data.')
		const locationData = await geoLocationResponse.json()
	}
	catch (err) {
		console.log(err)
	}

	data = locationData.address

	document.getElementById('id_country').value = data.country
	document.getElementById('id_city').value = data.city ?? data.town ?? data.village
	document.getElementById('id_tourist_attraction').value = data.attraction || ''
	document.getElementById('id_latitude').value = locationData.lat
	document.getElementById('id_latituderef').value = (locationData.lat > 0) ? 'N' : 'S'
	document.getElementById('id_longitude').value = locationData.lon
	document.getElementById('id_longituderef').value = (locationData.lon > 0) ? 'E' : 'W'
}


function initMap() {
	let marker;
	const dingli = { lat: 35.8530683, lng: 14.3779626 }
	const mapOptions = {
		zoom: 9,
		center: dingli,
		mapTypeId: 'hybrid'
	};

	// The map, centered at dingli
	const map = new google.maps.Map(document.getElementById("map"), mapOptions);


	// Delete existing marker, and create a new one on click location
	google.maps.event.addListener(map, 'click', e => {
		marker?.setMap(null)
		marker = new google.maps.Marker({
			position: e.latLng,
			map: map
		})
	});


	document.querySelector('.remove').addEventListener('click', e => {
		// console.log(marker.getPosition().lat())

		if (!marker) return

		let coords = {
			lat: marker.getPosition().lat(),
			lng: marker.getPosition().lng()
		}

		// document.querySelector('#map').style.display = 'none'
		getMissingInfo(coords)

	})
}

window.initMap = initMap;
