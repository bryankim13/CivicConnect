from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User #,AnonymousUser
from masterdata.models import Emailtemplate, Issue, Representative, client
from nutboxcivic import views
from nutboxcivic import forms


class testFavorites(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    
    def testFavList(self):
        testTemp = Emailtemplate(title = 'test', id = 1)
        testTemp.save()
        request = self.factory.get('/1/makeFav')
        request.user = self.user
        response = views.makeFavorite(request,1)
        self.assertTrue(request.user.clients.favorites.filter(id=1).exists())

    def testUnFav(self):
        testTemp = Emailtemplate(title = 'test', id = 1)
        testTemp.save()
        request = self.factory.get('/1/unfavorite')
        request.user = self.user
        request.user.clients.favorites.add(testTemp)
        response = views.unFavorite(request,1)
        self.assertFalse(request.user.clients.favorites.filter(id=1).exists())
    
    def testInFav(self):
        testTemp = Emailtemplate(title = 'test', id = 1)
        testTemp.save()
        request = self.factory.get('/favorites')
        request.user = self.user
        request.user.clients.favorites.add(testTemp)
        response = views.showFavorite(request)
        self.assertContains(response, 'test')

class TestPagesDisplay(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')


    # Test home page displays
    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, "Making Your Voice Heard.")

    # Test send page displays
    def test_send(self):
        url = reverse('send')
        request = self.factory.get(url)
        request.user = self.user
        #response = request.user.clients.get(url)
        response = views.usetemplatenoid(request)
        if self.user.is_authenticated:
            self.assertContains(response, "Template Preview")
            self.assertContains(response, "Copy text")
        else:
            self.assertContains(response, "Please sign in")


    # Test create template page displays
    def test_createTemplate(self):
        url = reverse('createTemp')
        response = self.client.get(url)
        self.assertContains(response, "Making Your Voice Heard.")
        self.assertContains(response, "Publish")

    # Test select template page displays
    def test_selectTemplate(self):
        url = reverse('select')
        response = self.client.get(url)
        self.assertContains(response, "View and Select Templates")

    # Test gauth login page displays
    def test_gauth(self):
        url = reverse('gauth')
        response = self.client.get(url)
        self.assertContains(response, "Login with Google")

    # Test profile page displays
    #def test_profile(self):
     #   url = reverse('profile')
      #  response = self.client.get(url)
       # self.assertContains(response, "Edit Your Profile")

    # Test favorite page displays
    #def test_favorite(self):
     #   url = reverse('favorite')
      #  response = self.client.get(url)
       # self.assertContains(response, "Your Favorite Templates!")

    # Test user page displays
    #def test_user(self):
     #   url = reverse('user')
      #  response = self.client.get(url)
       # self.assertContains(response, "Edit Your Profile")
