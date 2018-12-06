from django.contrib import admin

# Register your models here.
from .models import User,Menu

admin.site.register(Menu)
admin.site.register(User)
