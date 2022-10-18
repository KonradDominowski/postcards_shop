import os

from django.db import models
from .functions import clean_coordinates


class Photo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='shop/images/')
    country = models.CharField(max_length=32, blank=True, null=True)
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
        coordinates = clean_coordinates(self.photo.name)
        if coordinates:
            self.latitude = coordinates['latitude']
            self.latituderef = coordinates['latitude_ref']
            self.longitude = coordinates['longitude']
            self.longituderef = coordinates['longitude_ref']
