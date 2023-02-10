const photos = document.querySelectorAll('.photo')

photos.forEach((photo, i) => {
	setTimeout(() => {
		photo.classList.add("slideRight");
	}, i * 150)
})