from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=50,min_length=5,allow_blank=False)
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}
        def create(self,validated_data):
            user=User(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            user.save
            return user