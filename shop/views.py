import os.path
from os import listdir
from os.path import isfile, join
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.conf import settings
from .forms import PhotoForm, ConfirmPhotoForm

from .models import IMG_DIR, Photo
from .functions import get_exact_info


class Home(View):
    def get(self, request):
        count = Photo.objects.count()
        photos = Photo.objects.all().order_by('pk')
        context = {
            'count': count,
            'photos': photos
        }

        return render(request, 'index.html', context)


class AddNewPhoto(CreateView):
    def get_success_url(self):
        return reverse('confirm_photo', kwargs={'photo_id': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(AddNewPhoto, self).get_form_kwargs()
        return kwargs

    model = Photo
    # success_url = reverse_lazy('confirm_photo', kwargs={'photo_id': self.object.pk})
    template_name = 'create_photo.html'
    form_class = PhotoForm


def is_duplicate(photo):
    media_url = os.path.join(settings.MEDIA_ROOT, IMG_DIR)
    all_photos = [f for f in listdir(media_url) if isfile(join(media_url, f))]
    name, extension = (os.path.splitext(photo.name))
    index = name[::-1].find('_')
    slash_index = name[::-1].find('/')
    file_name = name[-slash_index:-index - 1] + extension

    return file_name in all_photos


class ConfirmPhoto(View):

    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.set_coordinates()
        photo.set_extra_info()
        photo.save()

        info = get_exact_info(photo.latitude, photo.longitude)

        form = ConfirmPhotoForm(instance=Photo.objects.get(pk=photo_id))

        context = {
            'form': form,
            'photo': photo,
            'is_duplicate': is_duplicate(photo)
        }

        return render(request, 'confirm_photo.html', context)

    def post(self, request, photo_id):
        form = ConfirmPhotoForm(request.POST, instance=Photo.objects.get(pk=photo_id))
        if form.is_valid():
            form.save()
            return redirect(reverse('shop-home'))
        return render(request, 'confirm_photo.html', {'form': form})


class DeletePhoto(View):
    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, photo.name))
        return redirect(reverse('shop-home'))


class UpdatePhoto(UpdateView):
    model = Photo
    fields = '__all__'
    template_name = 'confirm_photo.html'
    success_url = '/'

