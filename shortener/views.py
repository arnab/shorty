from django.shortcuts import render

from shortener import forms

def home(request):
    form = forms.CreateShortURLForm()
    return render(request, 'shortener/home.html', {'form': form})
