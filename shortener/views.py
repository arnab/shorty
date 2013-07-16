import datetime
from itertools import groupby
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST, require_safe
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from shortener import forms
from shortener.models import ShortURL, Visit
from shortener.helpers import parse_browser

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
    os, browser, version = parse_browser(request.META['HTTP_USER_AGENT'])
    # failing it should be ok
    Visit.objects.create(
        short_url=short_url,
        os = os, browser = browser, version = version,
        visited_at=datetime.datetime.utcnow(),
    )
    return HttpResponseRedirect(short_url.url)

@require_safe
def info(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    visits_by_browser = short_url.visits_by_browser()
    visits_by_hour = short_url.visits_by_hour()
    return render(request, 'shortener/info.html', {
        'short_url': short_url,
        'visits_by_browser': visits_by_browser,
        'visits_by_hour': visits_by_hour,
    })
