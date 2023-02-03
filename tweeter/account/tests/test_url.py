from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import dashboard, register
from django.contrib.auth import views as auth_views


class TestsUrls(SimpleTestCase):

    def test_dashboard(self):
        """
        Test dashboard url
        """
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logount(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
