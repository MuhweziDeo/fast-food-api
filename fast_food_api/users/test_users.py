from django.test import TestCase,Client
from django.contrib.auth.models import User
from . import serializers
from django.urls import reverse
import json
# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.user_data={
            "username":"dee",
            "password":"Adeo256.",
            "email":"dee@gmail.com"
        }
        self.test_client=Client()
        self.serializer=serializers.UserSerializer()



    def test_create_user(self):
        pass

class ViewTestCase(TestCase):
    def setUp(self):
        self.test_client=Client()
        self.user_data={
            "username":"dee",
            "password":"Adeo256.",
            "email":"dee@gmail.com"
        }
    def test_signup(self):
        resp=self.test_client.post(reverse("signup"),content_type='application/json',data=json.dumps(self.user_data))
        self.assertEqual(resp.status_code,201)
        self.assertIn("dee",str(resp.data))

        
