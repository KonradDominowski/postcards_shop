const photos = document.querySelectorAll('.photo')
const photosList = document.querySelectorAll('.photo__list')
const carouselRows = document.querySelectorAll('.carousel__row')
const googleAPIKey = 'AIzaSyDX7nPdvEfWcI6pYl2Qgw3pkO98eWfftc4'

photos.forEach((photo, i) => {
	setTimeout(() => {
		photo.classList.add("slideRight");
	}, i * 150)
})

carouselRows.forEach((row, i) => {
	row.style.display = (getComputedStyle(row).display === 'flex') ? 'none' : 'flex'
})

let row = carouselRows[Math.floor(Math.random() * carouselRows.length)]
row.style.display = 'flex'

setInterval(() => {

	if (row) row.style.display = 'none'

	row = carouselRows[Math.floor(Math.random() * carouselRows.length)]

	row.style.display = 'flex'
}, 4000)


photosList.forEach(photo => {
	let a = photo.querySelector('a')
	let aPhoto = a.querySelector('img')

})


// Map
function initMap() {
	const mapOptions = {
		zoom: 4.2,
		center: {
			// Center of Europe
			lat: 48.10893,
			lng: 4.2107998
		},
		mapTypeId: 'hybrid'
	};

	const map = new google.maps.Map(document.getElementById("map"), mapOptions);
	let markers = []

	photosList.forEach(link => {
		let a = link.querySelector('a')
		let img = link.querySelector('img')

		let marker = new google.maps.Marker({
			position: {
				lat: Number(img.dataset.lat),
				lng: Number(img.dataset.lng)
			},
			map: map
		})

		let content = `
		<div class="info-window">
		<div class="info-window-link">		
		<a href="${a.href}"><img class="photo_small"
		src="${img.src}"
		alt="${img.alt}"></a>
		</div>
		<div class="info-window-text">
		<h3>${img.dataset.country}</h3><br>
		${img.dataset.city}<br>
		${img.dataset.tourism}<br>
		</div>
		</div>
		

		`

		const infowindow = new google.maps.InfoWindow({
			content: content,
			ariaLabel: "Uluru",
		});

		marker.addListener("mouseover", () => {
			infowindow.open({
				anchor: marker,
				map,
			});
		})

		// marker.addListener("mouseout", () => {
		// 	infowindow.close({
		// 		anchor: marker,
		// 		map,
		// 	});
		// })

		markers.push(marker)

	})
}
window.initMap = initMap;
