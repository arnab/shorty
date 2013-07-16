from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.core.urlresolvers import reverse

from shortener import forms
from shortener.models import ShortURL

def home(request):
    form = forms.CreateShortURLForm()
    return render(request, 'shortener/home.html', {'form': form})

@require_POST
def create(request):
    form = forms.CreateShortURLForm(request.POST)
    if form.is_valid():
        ShortURL.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse('shortener:home'))
    else:
        return render(request, 'shortener/home.html', {'form': form})
