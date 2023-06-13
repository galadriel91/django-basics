from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields':['username' , 'password']}),
        ('개인정보' , {'fields':['last_name' , 'first_name' , 'email']}),
        ('추가정보' , {'fields':['profile_image' , 'short_desc']}),
        ('권한' , {'fields':['is_staff' , 'is_active' , 'is_superuser']}),
        ('일정' , {'fields':['last_login' , 'date_joined']}),
    ]