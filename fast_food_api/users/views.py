from django.shortcuts import render
from rest_framework import generics
from . import serializers
# Create your views here.

class UserView(generics.CreateAPIView):
    authentication_classes=()
    permission_classes=()
    serializer_class=serializers.UserSerializer
