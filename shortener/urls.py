from django.conf.urls import patterns, include, url

from shortener import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^create/?$', views.create, name='create'),
)
