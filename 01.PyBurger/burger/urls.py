from django.urls import path, include
from .views import burger_list

urlpatterns = [
    path('', burger_list)
]
