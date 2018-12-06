from django.shortcuts import render
from rest_framework import generics
from . import serializers
# Create your views here.

class UserView(generics.CreateAPIView):
    serializer_class=serializers.UserSerializer

    def perform_create(self,serializer):
        instance=serializer.save()
        instance.set_password(instance.password)
        instance.save()

