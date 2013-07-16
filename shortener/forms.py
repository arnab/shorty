from django.forms import ModelForm

from shortener.models import ShortURL

class CreateShortURLForm(ModelForm):
    class Meta:
        model = ShortURL
