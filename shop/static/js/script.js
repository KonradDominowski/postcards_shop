const photos = document.querySelectorAll('.photo')
const carouselRows = document.querySelectorAll('.carousel__row')

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