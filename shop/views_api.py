from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import PhotoSerializer
from rest_framework import generics
from rest_framework.response import Response


class PhotoListView(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(user_id=user.id)


class PhotoDetailsView(generics.RetrieveAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
