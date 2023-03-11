from django.forms import ModelForm, HiddenInput
from .models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ("photo",)


class ConfirmPhotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmPhotoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Photo
        exclude = ("photo",)
