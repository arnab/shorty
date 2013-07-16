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

    def test_create_without_url(self):
        """
        Should reject attemps to submit with no URL
        """
        response = self.client.post(reverse('shortener:create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "URL is required")

    def test_create_with_invalid_url(self):
        """
        Should reject attemps to submit with invalid URL
        """
        response = self.client.post(reverse('shortener:create'), {'url': 'url-to-shorten'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid URL")
