from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(PhotoForm, self).__init__(*args, **kwargs)
    #     self.fields['photo'].required = True

    class Meta:
        model = Photo
        fields = ('photo', )


class ConfirmPhotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmPhotoForm, self).__init__(*args, **kwargs)
        # self.fields['photo'].required = False

    class Meta:
        model = Photo
        # fields = '__all__'
        exclude = ('photo', )

