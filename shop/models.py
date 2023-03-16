from pathlib import Path
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .functions import clean_coordinates, get_exact_info
from django.contrib.postgres.fields import ArrayField
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image


from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

IMG_DIR = "shop/images/"


class UserTier(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    thumbnails = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    original_image = models.BooleanField(default=False)


class User(AbstractUser):
    tier = models.ForeignKey(
        UserTier,
        default=UserTier.objects.get(name="basic").pk,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Photo(models.Model):
    photo = models.ImageField(upload_to=IMG_DIR)
    name = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    tourist_attraction = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.CharField(max_length=16, blank=True, null=True)
    longitude = models.CharField(max_length=16, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def coordinates(self):
        if self.latitude and self.longitude:
            return f"{self.latitude}, {self.longitude}"

        return None

    def save(self, *args, **kwargs):
        self.name = self.photo.name
        super(Photo, self).save(*args, **kwargs)
        self.set_coordinates()
        self.set_extra_info()

        self.create_thumbnails()

    def create_thumbnails(self):
        for height in self.user.tier.thumbnails:
            output_size = (int(height), int(height))
            name, end = self.photo.path.split(".")
            img_path = name + f"thumbnail{height}." + end

            img = Image.open(self.photo)
            img.thumbnail(output_size)
            img.save(img_path)

            Thumbnail.objects.create(
                photo_id=self,
                thumbnail_size=height,
                thumbnail=File(
                    file=open(img_path, "rb"),
                    name=Path(img_path).name,
                ),
            )
            print(img_path)

    def set_coordinates(self):
        coordinates = clean_coordinates(
            os.path.join(settings.MEDIA_ROOT, self.photo.name)
        )
        if coordinates:
            self.latitude = coordinates["latitude"]
            self.longitude = coordinates["longitude"]

    def set_extra_info(self):
        """
        Extract additional information from photo metadata, such as country, city or tourist attraction.

        Return if there is no more information.
        """
        info = get_exact_info(self.latitude, self.longitude)

        if not info:
            return

        if "country" in info:
            self.country = info["country"]
        if "city" in info:
            self.city = info["city"]
        if "tourism" in info:
            self.tourist_attraction = info["tourism"]


class Thumbnail(models.Model):
    photo_id = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="thumbnail"
    )
    thumbnail_size = models.IntegerField()
    thumbnail = models.ImageField(upload_to=IMG_DIR, blank=True, null=True)
