from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('menu',views.MenuView,base_name='menu')
router.register('orders',views.OrderView,base_name='orders')
urlpatterns = [
    path('signup/',views.UserView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('',include(router.urls)),
]
