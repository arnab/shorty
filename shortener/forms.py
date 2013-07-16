from django import forms

class CreateShortURLForm(forms.Form):
    url = forms.CharField(
        max_length=1000,
        label='URL to shorten',
    )
    short_code = forms.CharField(
        max_length=30,
        label='short code (optional)',
        required=False, # TODO: needs work
    )
