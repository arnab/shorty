from django.utils.html import mark_safe
from django.contrib import admin
from shortener.models import Visit, ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'url', 'is_blacklisted_site')

    def report_spammy_sites(self, short_url):
        is_spammy = short_url.is_blacklisted_site()
        spammy_or_not = "spammy!" if is_spammy else "cool."
        return "{0} is {1}".format(short_url.short_code, spammy_or_not)

    def detect_spammy_sites(self, request, queryset):
        # html = "<ul>"
        for short_code in queryset:
            short_url = ShortURL.objects.get(short_code=short_code)
            html = self.report_spammy_sites(short_url)
            self.message_user(request, mark_safe(html))

            # html += self.report_spammy_sites(short_url)
        # html += "</ul>"


    detect_spammy_sites.short_description = "Detect spam/phishing sites"
    detect_spammy_sites.allow_tags = True

    actions = [detect_spammy_sites]

class VisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortURL, ShortURLAdmin)
admin.site.register(Visit, VisitAdmin)