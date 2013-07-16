from django.contrib import admin
from shortener.models import Visit, ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    pass

class VisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortURL, ShortURLAdmin)
admin.site.register(Visit, VisitAdmin)