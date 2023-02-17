const geolocationAPIKey = 'pk.764b02b9520ce1078da1f83298759512'
const googleAPIKey = 'AIzaSyDX7nPdvEfWcI6pYl2Qgw3pkO98eWfftc4'
const loading = document.querySelector('.sk-cube-grid')
const btnAllowChanging = document.getElementById('changeLocation')
const btnUpdateLocation = document.getElementById('updateLocation')
const form = document.getElementById(('photo_form'))


let allowChanging = false

btnUpdateLocation.style.display = 'none'
btnAllowChanging.addEventListener('click', function () {
	btnUpdateLocation.style.display = btnUpdateLocation.style.display ? '' : 'none'
	allowChanging = allowChanging ? false : true

	if (this.innerHTML == 'Change Marker Location') {
		this.innerHTML = 'Map marker can now be placed elsewhere.'
	} else {
		this.innerHTML = 'Change Marker Location'

	}
})

const getMissingInfo = async function (coords) {
	const { lat: lat, lng: lng } = coords


	const url = `https://eu1.locationiq.com/v1/reverse?key=${geolocationAPIKey}&lat=${lat}&lon=${lng}&format=json&accept-language=en`

	try {
		const geoLocationResponse = await fetch(url)
		if (!geoLocationResponse.ok) throw new Error('Error getting geolocation data.')
		const locationData = await geoLocationResponse.json()
		document.querySelector('.map-container').style.display = 'none'

		data = locationData.address
		document.getElementById('id_country').value = data.country
		document.getElementById('id_city').value = data.city ?? data.town ?? data.village
		document.getElementById('id_tourist_attraction').value = data.attraction || ''
		document.getElementById('id_latitude').value = lat
		document.getElementById('id_longitude').value = lng
	}
	catch (err) {
		console.error(err)
	}

}


function initMap() {
	let marker;
	let lat = Number(document.getElementById('id_latitude').value)
	let lng = Number(document.getElementById('id_longitude').value)

	const mapOptions = {
		zoom: 4.2,
		center: {
			// Center of Europe
			lat: 48.10893,
			lng: 4.2107998
		},
		mapTypeId: 'hybrid'
	};

	if (lat && lng) {
		mapOptions.zoom = 12
		mapOptions.center = { lat: lat, lng: lng }
	}


	// The map, centered at photo location
	const map = new google.maps.Map(document.getElementById("map"), mapOptions);

	if (lat && lng) {
		marker = new google.maps.Marker({
			position: mapOptions.center,
			map: map
		})
	}


	// Delete existing marker, and create a new one on click location
	google.maps.event.addListener(map, 'click', e => {
		if (!allowChanging) return

		marker?.setMap(null)
		marker = new google.maps.Marker({
			position: e.latLng,
			map: map
		})
	});


	btnUpdateLocation.addEventListener('click', e => {
		if (!marker) return

		let coords = {
			lat: Number(marker.getPosition().lat()).toFixed(8),
			lng: Number(marker.getPosition().lng()).toFixed(8)
		}

		document.querySelector('#map').style.filter = 'blur(5px)'
		loading.style.display = 'block'
		getMissingInfo(coords)

	})
}

window.initMap = initMap;
