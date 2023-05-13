from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUser(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':('username','password')}),
        ('개인정보', {'fields':('first_name','last_name','email')}),
        ('추가필드', {'fields':('profile_image','short_description')}),
        ('권한', {'fields':('is_active','is_superuser','is_staff')}),
        ('중요일정', {'fields':('last_login','date_joined')})
    ]