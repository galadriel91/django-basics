from django.contrib import admin

from burger.models import Burger

# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass