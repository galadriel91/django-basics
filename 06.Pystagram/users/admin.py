from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUser(UserAdmin):
    fieldsets = [
        (None, {'fields':('username' , 'password')}),
        ('개인정보' , {'fields':('first_name', 'last_name', 'email')}),
        ('추가정보' , {'fields':('profile_image', 'short_desc')}),
        ('권한' , {'fields':('is_staff', 'is_active', 'is_superuser')}),
        ('접속' , {'fields':('last_login', 'date_joined')}),
    ]