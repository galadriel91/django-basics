from django.contrib import admin
from .models import Burger

# Register your models here.
@admin.register(Burger)
class Burger(admin.ModelAdmin):
    pass