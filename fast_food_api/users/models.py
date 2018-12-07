from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users require an email")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,username):
        user=self.create_user(email=email,password=password,username=username)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,max_length=60)
    username=models.CharField(unique=True,max_length=25)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    objects=CustomUserManager()
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Menu(models.Model):
    meal_name=models.CharField(unique=True,max_length=50)
    meal_price=models.IntegerField()

    def __str__(self):
        return self.meal_name

class Order(models.Model):
    meal=models.ForeignKey(Menu,related_name="meal",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    location=models.CharField(max_length=100)
    status=models.CharField(default="Pending",max_length=20)
    owner=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    date_order=models.DateField(auto_now=True)