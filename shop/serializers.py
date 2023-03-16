from .models import Photo, Thumbnail
from rest_framework import serializers


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = (
            "thumbnail_size",
            "thumbnail",
        )


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail = ThumbnailSerializer(many=True, required=False)

    def create(self, validated_data):
        request = self.context.get("request", None)
        validated_data["user"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Photo
        fields = ("photo", "thumbnail")
        # fields = ("photo",)


class PremiumPhotoSerializer(serializers.ModelSerializer):
    photo_thumbnail_200 = serializers.ImageField(read_only=True)
    photo_thumbnail_400 = serializers.ImageField(read_only=True)

    def create(self, validated_data):
        request = self.context.get("request", None)
        validated_data["user"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Photo
        fields = (
            "photo_thumbnail_200",
            "photo_thumbnail_400",
            "photo",
        )


class BasicPhotoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        print("Hi")
        super().__init__(*args, **kwargs)

    photo_thumbnail_200 = serializers.ImageField(read_only=True)

    def create(self, validated_data):
        request = self.context.get("request", None)
        validated_data["user"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Photo
        fields = ("photo_thumbnail_200",)
