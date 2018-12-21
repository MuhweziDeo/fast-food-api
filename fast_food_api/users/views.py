from django.shortcuts import render, redirect
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
from .permissions import IsOwner
# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from .models import User
from rest_framework.views import APIView

class UserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    # def perform_create(self,serializer):
    #     instance=serializer.save()
    #     instance.set_password(instance.password)
    #     instance.save()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user.is_active)
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            domain = current_site.domain
            uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
            print('######################',uid)
            token = account_activation_token.make_token(user)
            message = 'Hey {} \n Please click link to activate account\n{}/activate/{}/{}/'.format(
                user.username, domain, uid, token)
            to_email = user.email
            send_mail(subject, message, 'aggrey256@gmail.com', [to_email, ])
            return Response(serializer.data)
        return Response(serializer.errors)
        return Response('it works')


class ActivateAccount(APIView):
    def get(self,request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            print('####################',uid)
            user = User.objects.get(pk=uid)
            print('####################',user)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            # login(request, user)
            return Response('Account Activated')
        return Response('Couldnt perform task')


class LoginView(APIView):
    authentication_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.get_or_create(user=user)
            return Response({
                "token": user.auth_token.key
            })
        return Response({
            "message": "We cant authenticate u {}".format(username)
        })


class MenuView(viewsets.ModelViewSet):
    serializer_class = serializers.MenuSerializer
    queryset = models.Menu.objects.all()


class OrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    # def perform_create(self,serializer):
    #     serializer.save(owner=self.request.user)
    def partial_update(self, request, pk=None):
        order = models.Order.objects.get(id=pk)
        updated_order = self.serializer_class(
            order, data=request.data, partial=True)
        updated_order.is_valid(raise_exception=True)
        updated_order.save()
        return Response(updated_order.data)


class UserOrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        user_order = serializers.OrderSerializer(data=request.data)
        if user_order.is_valid():
            user_order.save(owner=self.request.user)
            return Response(user_order.data)
        return Response(user_order.errors)

    def list(self, request):
        queryset = models.Order.objects.filter(owner=request.user)
        user_orders = serializers.OrderSerializer(queryset, many=True)
        return Response(user_orders.data)

    # def retrieve(self,request,pk=None):
    #     order=get_object_or_404(models.Order,pk=pk)
    #     print(order.owner.id)
    #     if order.owner.id == request.user.id:
    #         serializer=serializers.OrderSerializer(order)
    #         print(request.user.id)
    #         return Response(serializer.data)
    #     return Response({
    #         "message":"U r not authenticated to view this"
    #     })
