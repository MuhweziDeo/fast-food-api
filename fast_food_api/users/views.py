from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from . import models
from .permissions import IsOwnerOrReadonly
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

class OrderView(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.OrderSerializer
    queryset=models.Order.objects.all()
    permission_classes=(permissions.IsAuthenticated,permissions.IsAdminUser)

    # def perform_create(self,serializer):
    #     serializer.save(owner=self.request.user)
    def partial_update(self,request,pk=None):
        order=models.Order.objects.get(id=pk)
        updated_order=self.serializer_class(order,data=request.data,partial=True)
        updated_order.is_valid(raise_exception=True)
        updated_order.save()
        return Response(updated_order.data)



class UserOrderView(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,IsOwnerOrReadonly,)
    serializer_class=serializers.OrderSerializer
    queryset=models.Order.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
    def create(self,request):
        user_order=serializers.OrderSerializer(data=request.data)
        if user_order.is_valid():
            user_order.save(owner=self.request.user)
            return Response(user_order.data)
        return Response(user_order.errors)

    def list(self,request):
        queryset=models.Order.objects.filter(owner=request.user)
        user_orders=serializers.OrderSerializer(queryset,many=True)
        print(user_orders.data)
        return Response(user_orders.data)
        
