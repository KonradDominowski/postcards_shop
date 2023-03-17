from .models import Photo, Thumbnail
from rest_framework import serializers


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = (
            "thumbnail_size",
            "thumbnail",
        )


class OriginalPhotoThumbnailsSerializer(serializers.ModelSerializer):
    thumbnail = ThumbnailSerializer(many=True, required=False)

    class Meta:
        model = Photo
        fields = ("photo", "thumbnail")


class ThumbnailsSerializer(serializers.ModelSerializer):
    thumbnail = ThumbnailSerializer(many=True, required=False)

    class Meta:
        model = Photo
        fields = ("thumbnail",)


class PhotoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request", None)
        validated_data["user"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Photo
        fields = ("photo",)
