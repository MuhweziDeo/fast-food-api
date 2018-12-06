from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from . import models
# Create your views here.

class UserView(generics.CreateAPIView):
    serializer_class=serializers.UserSerializer

    # def perform_create(self,serializer):
    #     instance=serializer.save()
    #     instance.set_password(instance.password)
    #     instance.save()

class LoginView(APIView):
    authentication_classes=()
    def post(self,request,):
        username=request.data.get("username")
        password=request.data.get("password")
        user =authenticate(username=username,password=password)
        if user:
            Token.objects.get_or_create(user=user)
            return Response({
                "token":user.auth_token.key
            })
        return Response({
            "message":"We cant authenticate u {}".format(username)
        })

class MenuView(viewsets.ModelViewSet):
    serializer_class=serializers.MenuSerializer
    queryset=models.Menu.objects.all()
