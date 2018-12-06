from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        user=models.User(
                username=validated_data['username'],
                email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Menu
        fields=('id','meal_name','meal_price')