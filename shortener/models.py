from django.db import models

class ShortURL(models.Model):
    url = models.CharField(max_length=1000)
    short_code = models.CharField(
        max_length=30,
        unique=True,
    )

    def __unicode__(self):
        return self.short_code
