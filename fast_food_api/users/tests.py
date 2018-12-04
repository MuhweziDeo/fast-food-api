from django.test import TestCase
from django.contrib.auth.models import User
from . import serializers
# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.user_data={
            "username":"dee",
            "password":"Adeo256.",
            "email":"dee@gmail.com"
        }



    def test_create_user(self):
        pass
        
