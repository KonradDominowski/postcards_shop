from .models import Photo, Thumbnail
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import (
    PremiumPhotoSerializer,
    BasicPhotoSerializer,
    PhotoSerializer,
    ThumbnailSerializer,
)
from rest_framework import generics
from rest_framework.response import Response


class PhotoListView(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = PhotoSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(user_id=user.id)


class ThumbnailListView(generics.ListAPIView):
    serializer_class = ThumbnailSerializer
    queryset = Thumbnail.objects.all()
