from django.test import TestCase
from django.urls import reverse


class TestPagesDisplay(TestCase):
    # Test home page displays
    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, "Making Your Voice Heard.")

    # Test send page displays
    def test_home(self):
        url = reverse('send')
        response = self.client.get(url)
        self.assertContains(response, "Template Preview")
        self.assertContains(response, "Copy text")

    # Test create template page displays
    def test_home(self):
        url = reverse('createTemp')
        response = self.client.get(url)
        self.assertContains(response, "Making Your Voice Heard.")
        self.assertContains(response, "Publish")

    # Test select template page displays
    def test_home(self):
        url = reverse('select')
        response = self.client.get(url)
        self.assertContains(response, "View and Select Templates")

    # Test gauth login page displays
    def test_home(self):
        url = reverse('gauth')
        response = self.client.get(url)
        self.assertContains(response, "Login with Google")
