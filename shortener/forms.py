from django import forms

class CreateShortURLForm(forms.Form):
    # TODO: make it non-required
    short_code = forms.CharField(max_length=30)
    url = forms.CharField(max_length=1000)
