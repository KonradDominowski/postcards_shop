from .models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail_200_px = serializers.SerializerMethodField()

    def get_thumbnail_200_px(self, obj):
        request = self.context.get("request")
        photo_url = obj.photo.url + "/200"

        return request.build_absolute_uri(photo_url)

    def create(self, validated_data):
        request = self.context.get("request", None)
        print("TEST")
        print("TEST")
        print("TEST")
        print("TEST")
        print("TEST")
        print("TEST")
        print("TEST")
        print("TEST")
        validated_data["user"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Photo
        fields = (
            "id",
            "photo",
            "name",
            "country",
            "city",
            "tourist_attraction",
            "latitude",
            "longitude",
            "thumbnail_200_px",
        )
