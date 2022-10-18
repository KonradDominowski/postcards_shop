from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import PhotoForm, ConfirmPhotoForm

from .models import Photo


# TODO - Check for duplicate picture when adding
class Home(View):
    def get(self, request):
        count = Photo.objects.count()
        names = [photo.photo.name for photo in Photo.objects.all()]
        for photo in Photo.objects.all():
            print(photo.photo.name)
            print(photo.longitude)
            print(photo.coordinates())

        return HttpResponse(f'''Hello, masz {count} zdjęć: {names}''')


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


class ConfirmPhoto(View):
    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.set_coordinates()
        photo.save()

        form = ConfirmPhotoForm(instance=Photo.objects.get(pk=photo_id))

        return render(request, 'confirm_photo.html', {'form': form, 'photo': photo})

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
        return redirect(reverse('shop-home'))
