import uuid
from django.db import models

class ShortURL(models.Model):
    url = models.URLField(
        max_length=1000,
        verbose_name='URL to shorten',
    )
    short_code = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )

    def __unicode__(self):
        return self.short_code

    def save(self, *args, **kwargs):
        if not self.pk:
            # Has never been saved
            if self.short_code == '':
                self.short_code = choose_short_code()
        super(ShortURL, self).save(*args, **kwargs)

def generate_short_code():
    return str(uuid.uuid1())[0:7]

def choose_short_code():
    code = generate_short_code()
    while ShortURL.objects.filter(short_code=code).exists():
        code = generate_short_code()
    return code
