from django.test import TestCase
from django.contrib import auth
from .models import *

'''
This is a test to help figure out superuser login issue
https://stackoverflow.com/questions/8844536/admin-page-on-django-is-broken
python manage.py test profiles_api_app.TestCase
'''
class AuthTestCase(TestCase):
    def setUp(self):
        self.u = UserProfile.objects.create_user('test@dom.com', 'iamtest', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')
