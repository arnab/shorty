"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse

from django.test import TestCase


class ShortenerViewsTest(TestCase):
    def test_home_view_renders(self):
        """
        Can successfully get to the (main) entry-point view
        """
        response = self.client.get(reverse('shortener:home'))
        self.assertEqual(response.status_code, 200)
