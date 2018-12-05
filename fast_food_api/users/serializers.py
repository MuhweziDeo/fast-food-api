from rest_framework.authtoken.models import Token
from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}
        def create(self,validated_data):
            user=models.User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(make_password(validated_data['password']))
            user.save
            return user