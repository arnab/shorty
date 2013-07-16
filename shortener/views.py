from django.shortcuts import render

from shortener import forms

def home(request):
    form = forms.CreateShortURLForm()
    return render(request, 'shortener/home.html', {'form': form})

def create(request):
    form = forms.CreateShortURLForm(request.POST)
    if form.is_valid():
        pass
    else:
        return render(request, 'shortener/home.html', {'form': form})
