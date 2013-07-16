import datetime
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST, require_safe
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from shortener import forms
from shortener.models import ShortURL, Visit

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

@require_safe
def show(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    Visit.objects.create(visited_at=datetime.datetime.utcnow()) # failing it should be ok
    return HttpResponseRedirect(short_url.url)
