from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('menu',views.MenuView,base_name='menu')
router.register('orders',views.OrderView,base_name='orders')
router.register('users/orders',views.UserOrderView,base_name='user-orders')
urlpatterns = [
    path('signup/',views.UserView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('',include(router.urls)),
    path('activate/<uidb64>/<token>/',
        views.ActivateAccount.as_view(), name='activate'),
    path('password-reset/',views.PasswordResetView.as_view(),name='password-reset'),
]
