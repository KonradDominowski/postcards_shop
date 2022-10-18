import os

from django.conf import settings
from django.db import models
from .functions import clean_coordinates, get_exact_info


IMG_DIR = 'shop/images/'


class Photo(models.Model):
    photo = models.ImageField(upload_to=IMG_DIR)
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    tourist_attraction = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.CharField(max_length=16, blank=True, null=True)
    latituderef = models.CharField(max_length=1, blank=True, null=True)
    longitude = models.CharField(max_length=16, blank=True, null=True)
    longituderef = models.CharField(max_length=1, blank=True, null=True)

    def coordinates(self):
        if self.latitude and self.latituderef and self.longitude and self.longituderef:
            return f"{self.latitude}°{self.latituderef}, {self.longitude}°{self.longituderef}"

        return None

    def save(self, *args, **kwargs):
        self.name = self.photo.name
        super(Photo, self).save(*args, **kwargs)

    def set_coordinates(self):
        coordinates = clean_coordinates(os.path.join(settings.MEDIA_ROOT, self.photo.name))
        if coordinates:
            self.latitude = coordinates['latitude']
            self.latituderef = coordinates['latitude_ref']
            self.longitude = coordinates['longitude']
            self.longituderef = coordinates['longitude_ref']

    def set_extra_info(self):
        info = get_exact_info(self.latitude, self.longitude)

        if 'country' in info:
            self.country = info['country']
        if 'city' in info:
            self.city = info['city']
        if 'tourism' in info:
            self.tourist_attraction = info['tourism']

