import uuid
import re
from django.db import models
from django.db.models import Count
from django.db import connection

class ShortURL(models.Model):
    SPAM_BLACKLIST = ['spammer.net']

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

    def visits_by_browser(self):
        return self.visit_set.all().values('browser').annotate(count=Count('browser'))

    def visits_by_hour(self):
        cursor = connection.cursor()
        sql = """
        select EXTRACT(HOUR from visited_at) AS hour, count(id) AS count
        from shortener_visit
        where short_url_id = {0}
        group by hour
        """.format(self.id)
        cursor.execute(sql)
        # return dictfetchall(cursor)
        return cursor.fetchall()

    def is_blacklisted_site(self):
        return any([
            site in self.url for site in self.SPAM_BLACKLIST
        ])
    is_blacklisted_site.boolean = True
    is_blacklisted_site.short_description = 'Blacklisted site?'

class Visit(models.Model):
    short_url = models.ForeignKey(ShortURL)
    visited_at = models.DateTimeField()
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0} {1} {2} at {3}".format(self.os, self.browser, self.version, self.visited_at)

def generate_short_code():
    return str(uuid.uuid1())[0:7]

def choose_short_code():
    code = generate_short_code()
    while ShortURL.objects.filter(short_code=code).exists():
        code = generate_short_code()
    return code

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
