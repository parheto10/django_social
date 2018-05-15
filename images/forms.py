import urllib
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Images

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [
            'titre',
            'url',
            'description',
        ]

        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Url incorrect, verifier SVP !!')
        return url


    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_nom = '{}.{}'.format(slugify(image.titre), image_url.rsplit('.', 1)[1].lower())

        #telechager image a partir de l ur donnee
        response = urllib.urlopen(image_url)
        image.image.save(image_nom, ContentFile(response.read()),
                         save=False)

        if commit:
            image.save()
        return image

