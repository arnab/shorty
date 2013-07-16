from django import forms

# TODO: Can we use a model form
class CreateShortURLForm(forms.Form):
    url = forms.URLField(
        max_length=1000,
        label='URL to shorten',
        error_messages={'required': 'URL is required'}
    )
    short_code = forms.CharField(
        max_length=30,
        label='short code (optional)',
        required=False, # TODO: needs work
    )
