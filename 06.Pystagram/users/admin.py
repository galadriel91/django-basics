from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":('username', 'password')}),
        ('개인정보', {"fields":('last_name', 'first_name', 'email')}),
        ('추가정보', {"fields":('profile_image', 'description')}),
        ('권한설정', {"fields":('is_staff', 'is_superuser', 'is_active')}),
        ('중요일정', {"fields":('last_login', 'date_joined')}),
    ]
